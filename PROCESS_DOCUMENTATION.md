# Automated Evidence Synthesis Pipeline v3.0: Process Documentation

## Overview

This pipeline identifies nutrition interventions for **children under 5** and
**women of reproductive age (WRA)** in low- and middle-income countries (LMICs)
that are both **well evidence-backed** and **cost-effective**, with realistic
pathways to government-led scaling.

It runs in **two phases** separated by a manual review checkpoint, then a manual
synthesis:

1. **Phase 1 — Evidence.** Retrieve meta-analyses / systematic reviews from
   PubMed and the economics/development literature from OpenAlex, *population-
   targeted* and **excluding cost-effectiveness**. Deduplicate, score, rank,
   take the top 200, and retrieve full text. A human/LLM reviews the result and
   writes a shortlist of interventions.
2. **Phase 2 — Cost-effectiveness.** For *each shortlisted intervention*, run a
   targeted cost-effectiveness search (PubMed + OpenAlex + an optional local CEA
   registry).
3. **Synthesis.** A human/LLM combines both datasets in-conversation, under a
   grounding checklist, and a verifier lints the result.

**Why two phases?** A deep audit of the earlier single-phase pipeline (the
Vitamin A Supplementation case study, see end of this document) found its broad
cost-effectiveness track returned **zero usable CEAs for the actual
interventions**, yet the synthesis still assigned cost-effectiveness ratings
from background knowledge. Splitting the pipeline means cost-effectiveness is
only ever searched — and only ever rated — for the interventions that survive
the evidence screen.

**Implementation:** Python 3.10+ **standard library only** (`urllib`, `json`,
`csv`, `xml.etree.ElementTree`); no pip dependencies.

```
                     PHASE 1 (code/11_fetch_papers.py)            PHASE 2 (code/15_run_cea.py)     SYNTHESIS
                ┌──────────────────────────────────────────┐      ┌────────────────────────┐   ┌────────────┐
 PubMed Track A │ 12 domains × 2 passes (MA, SR)            │      │ per shortlisted        │   │ human/LLM  │
 OpenAlex Track C│ 4 nutrition-sensitive queries           │ ───► │ intervention:          │   │ combines   │
                │ + POPULATION filter + LMIC filter        │ rank │  PubMed CEA + OpenAlex  │ ► │ both sets  │
                │ → dedup → enrich → score (8 comp.)       │ top  │  + optional registry   │   │ → verify   │
                │ → PMC full text (top 200)                │ 200  │ → filter/rank CEAs      │   │            │
                └──────────────────────────────────────────┘  │   └────────────────────────┘   └────────────┘
              data/top_papers_for_review.json ─── manual review ─► data/shortlist.json ─► data/cea_by_intervention.json
```

---

# PHASE 1 — Evidence

Entry point: `python3 code/11_fetch_papers.py` → `code/10_main.py:run_phase1()`.

## Stage 1: Literature retrieval (two tracks, no cost-effectiveness)

| Source | Role | API | Rate limit |
|--------|------|-----|-----------|
| PubMed (E-Utilities) | Primary — biomedical evidence | esearch + efetch | 10 req/s with API key |
| OpenAlex | Supplementary — economics/development literature | REST | ~0.3 s between requests |

### Track A — Meta-analyses & systematic reviews (PubMed)

Twelve intervention-domain queries (`code/03_queries.py:TRACK_A_QUERIES`), each
run in **two passes**:

- **Pass 1 (primary tier):** `meta-analysis[pt] OR "Cochrane Database Syst Rev"[Journal]` — confirmed meta-analyses.
- **Pass 2 (supplementary tier):** `systematic review[pt] OR "systematic review"[tiab]`.

The twelve domains: micronutrient supplementation · food fortification ·
complementary feeding · breastfeeding promotion · acute malnutrition management ·
maternal nutrition · WASH + nutrition · school feeding · growth monitoring ·
deworming · nutrition-sensitive agriculture · integrated/multi-sectoral.

Every query is assembled by the single chokepoint `build_pubmed_query()`:

```
[intervention terms] AND [POPULATION_FILTER] AND [LMIC_FILTER] AND [type_filter]
```

**Population filter (new in v3 — the under-5 / WRA target).** A paper on
*either* population qualifies (OR logic), via MeSH plus title/abstract terms:

```
("infant"[MeSH] OR "child, preschool"[MeSH]
 OR "infant nutritional physiological phenomena"[MeSH]
 OR "pregnant women"[MeSH] OR "pregnancy"[MeSH]
 OR "maternal nutritional physiological phenomena"[MeSH]
 OR "reproductive health"[MeSH]
 OR "under-five"[tiab] OR "under 5"[tiab] OR "preschool"[tiab] OR "infant"[tiab]
 OR "neonatal"[tiab] OR "young child"[tiab]
 OR "women of reproductive age"[tiab] OR "reproductive age"[tiab]
 OR "pregnant"[tiab] OR "pregnancy"[tiab] OR "maternal"[tiab]
 OR "antenatal"[tiab] OR "prenatal"[tiab])
```

Because it lives in `build_pubmed_query`, it propagates automatically to all
24 Track A sub-queries (12 domains × 2 passes).

**LMIC filter.** Uses the curated `"developing countries"[MeSH]` descriptor
(which maps to all individual LMIC country names) plus tiab fallbacks
(`low income`, `middle income`, `LMIC`, `sub-saharan africa`, `south asia`,
`southeast asia`).

### Track C — Nutrition-sensitive interventions (OpenAlex)

Four free-text queries for literature PubMed indexes poorly: cash transfers,
social protection, food subsidies / public distribution, conditional cash
transfers. Each search string is wrapped by `build_openalex_search()`, which
ANDs in the OpenAlex equivalent of the population clause.

### Cost-effectiveness is **not** searched in Phase 1

The old "Track B" CEA query is removed from Phase 1. Its cost-term skeleton is
retained in `queries.py` and reused, per-intervention, in Phase 2.

### E-Utilities mechanics

1. **esearch** — submit the query, receive up to `PUBMED_RETMAX` (500) PMIDs + total count (JSON).
2. **efetch** — submit PMIDs in batches of `PUBMED_BATCH_SIZE` (200), receive XML.
3. **Parse** — title, abstract (structured sections joined), publication year, journal, authors (first 5), DOI, publication types, MeSH descriptors, and the **Cochrane accession** (`CDxxxxxx`, extracted from the DOI — new in v3).
4. Raw XML/JSON saved to `data/raw_responses/` for reproducibility.

## Stage 2: Deduplication

Run in order (`code/06_dedup.py`):

1. **Within PubMed by PMID** — when the same paper appears across queries/passes, keep the higher-priority tier (primary > supplementary).
2. **Cochrane version dedup (new in v3)** — collapse records sharing a `cochrane_id` (e.g. CD008524), keep the newest `publication_year`, and tag the dropped older version `superseded_by`. *A Cochrane review update is the same review, not new evidence* — this prevents the version-double-counting the VAS audit found.
3. **Within OpenAlex by OpenAlex ID.**
4. **Cross-source by normalized DOI** — when a paper is in both sources, keep the PubMed record (richer MeSH / publication types) and merge `cited_by_count` + open-access status from OpenAlex.

*Representative run:* PubMed 1,194 → 531 (PMID) → 506 (25 Cochrane versions collapsed); OpenAlex 2,000 → 1,515; merged set ≈ 1,993 papers.

## Stage 3: Citation enrichment + scoring

**Citation enrichment** (`citation_enrichment.py`): for PubMed papers lacking a
citation count, batch-look-up DOIs in OpenAlex (50 per request) to populate
`cited_by_count` and `is_open_access`.

**Scoring** (`code/08_scoring.py`) — 8 components, max ≈ 95:

| # | Component | Max | Source |
|---|-----------|-----|--------|
| 1 | Study design authority | 20 | PubMed `publication_type` (keyword fallback for OpenAlex) |
| 2 | Topic relevance | 25 | MeSH intervention/outcome term sets (keyword fallback) |
| 3 | Setting relevance | 10 | MeSH geographic terms (keyword fallback) |
| 4 | Recency | 10 | Step function on publication year |
| 5 | Citation impact | 12 | `cited_by_count` brackets |
| 6 | Open access | 3 | `is_open_access` |
| 7 | Tier bonus | 5 | +5 for confirmed meta-analyses (primary tier) |
| 8 | **Population relevance (new in v3)** | **10** | under-5 / WRA MeSH set, or keyword fallback |

Component 8 makes the target population a first-class ranking signal, so under-5
/ WRA evidence rises into the top 200. Papers are sorted by total score
descending.

## Stage 3.5: Full-text retrieval (PMC open access)

For the **top 200** papers (`TOP_N_FOR_REVIEW = 200`, raised from 100):

1. Convert PMIDs → PMCIDs via the NCBI ID Converter API (batch of 200). *(The converter returns PMIDs as integers — they must be cast to `str()` to match the paper dict keys.)*
2. `efetch db=pmc` for each PMCID; parse the `<body>` into sections (Introduction/Methods/Results/Discussion) and tables.
3. Cache raw XML in `data/raw_responses/pmc/{PMCID}.xml`; subsequent runs reuse it.
4. Papers without a downloadable body are flagged `fulltext_source: "abstract_only"` (Cochrane/Wiley and some Elsevier journals restrict PMC XML).

*Representative run:* 193 of the top 200 had PMIDs, 160 were PMC-indexed, 117
yielded full-text bodies.

## Stage 4: Manual review → shortlist

The top 200 (`data/top_papers_for_review.json`, with full text where available)
are reviewed **in-conversation** — no API automation — guided by
`prompts/shortlist_prompt.md`. The reviewer identifies distinct interventions,
each backed by multiple corpus papers, and writes **`data/shortlist.json`** (from
`data/shortlist.template.json`):

```json
{
  "interventions": [
    {"name": "vitamin A supplementation in children",
     "synonyms": ["retinol supplementation", "vitamin A capsule"],
     "mesh": ["Vitamin A", "Vitamin A Deficiency"],
     "population": "under-5"}
  ]
}
```

`name` is required (used in PubMed `[tiab]`, OpenAlex search, and registry
matching); `synonyms` and `mesh` broaden the Phase 2 search; `population` is
informational. Avoid ambiguous short abbreviations (e.g. "VAS" also means Visual
Analog Scale) — they cause false positives in OpenAlex's free-text search.

---

# PHASE 2 — Cost-effectiveness

Entry point: `python3 code/15_run_cea.py [data/shortlist.json]` →
`code/14_cea_main.py:run_phase2()`. For **each** shortlisted intervention:

### 1. Targeted retrieval (`code/12_cea_client.py`)

- **PubMed** — `build_cea_pubmed_query()` assembles
  `CEA_TERM_SKELETON AND (name/synonyms[tiab] OR mesh[MeSH]) AND LMIC_FILTER`,
  where the skeleton is the cost-term half of the old Track B
  (`cost-benefit analysis[MeSH]`, `cost-effectiveness`, `cost per DALY`,
  `cost-utility`, `incremental cost`, …). Run via the reused `esearch`
  (`retmax = CEA_PER_INTERVENTION_RETMAX`, 100) + `efetch` + parser.
- **OpenAlex** — `build_cea_openalex_search()` (cost terms AND name/synonyms AND
  low-income/LMIC/developing), run with `max_pages = CEA_OPENALEX_MAX_PAGES` (2).
- Deduplicate (PMID, then cross-source DOI) and score with the same
  `score_paper()` used in Phase 1.

### 2. Filter + rank for genuine, on-topic CEAs

The OpenAlex arm is loosely matched, and the general relevance score does not
reward "CEA-ness", so the raw bucket is filtered and re-ranked:

- **Keep** a paper if it came from PubMed (a cost term was *required* at query
  time) **or** if its text/MeSH contains a cost-effectiveness marker
  (`cea_hits > 0`).
- **Rank** by `cea_rank_score = relevance_score + min(cea_hits, 5) × 5`, so a
  genuine, on-topic CEA outranks both a topically-strong-but-weak-CEA paper and
  an off-topic-but-CEA-heavy paper (e.g. a cochlear-implant CEA that matched an
  ambiguous synonym).

### 3. Optional local CEA registry (`code/13_ghcea_registry.py`)

A research spike found neither the Tufts/CEVR Global Health CEA Registry (a
client-side JavaScript app) nor DCP3 (a PDF supplement) is reachable from
stdlib `urllib`. So the registry is an **optional local CSV** the user downloads
once (see `data/README.md`). If present it is matched against each intervention
(name + synonyms, tolerant column aliases); if absent, Phase 2 prints a notice
and proceeds on the PubMed/OpenAlex backbone with zero registry matches.

### 4. CEA-rating guard + output

Each intervention record sets
`cea_rating_allowed = (has CEA papers) OR (has registry matches)`. When false,
the synthesis **must** record cost-effectiveness as `Unknown` rather than invent
one. Output is written to **`data/cea_by_intervention.json`** with, per intervention:
`cea_papers` (filtered, ranked), `registry_matches`, `registry_available`,
`num_cea_papers`, and `cea_rating_allowed`.

---

# Synthesis (in-conversation) + verification

The reviewer combines `data/top_papers_for_review.json` (Phase 1) and
`data/cea_by_intervention.json` (Phase 2) into the tiered intervention writeup
(`output/FULL_INTERVENTION_SYNTH.md`), following the hard grounding rules in
`prompts/synthesis_prompt.md`:

- State study type **verbatim** from `journal` + `publication_type` (never infer "Cochrane" unless the journal is *The Cochrane Database of Systematic Reviews*).
- Attach a **corpus PMID to every numeric claim** (else write `not in corpus`); never import figures from background knowledge.
- Keep **all-cause vs cause-specific** outcomes separate; flag underpowered pathways.
- Report both fixed/random estimates and name any dominant trial the review identifies.
- **Version ≠ evidence** — Cochrane updates sharing one accession are counted once.
- **CEA-rating guard** — assign a cost-effectiveness rating only where `cea_rating_allowed` is true; otherwise `Unknown`.

**Claim verifier** (`code/17_verify_synthesis.py` → `code/16_verify.py`): parses every
`{value, PMID}` claim from the finished synthesis and checks (a) the PMID is in
the corpus (`data/papers_database.json` / `data/cea_by_intervention.json`) and (b) the
cited paper's text contains the claimed number. It reports `NOT_IN_CORPUS`
(misattribution / external-knowledge leak), `NEEDS_REVIEW` (in corpus but number
not found — semantic check left to the reviewer), and unsourced numeric claims.

---

## Configuration (`code/01_config.py`)

| Knob | Default | Purpose |
|------|---------|---------|
| `TOP_N_FOR_REVIEW` | 200 | Phase 1 top-N + full-text breadth |
| `POPULATION_SCORE_MAX` | 10 | Scoring component 8 cap |
| `PUBMED_RETMAX` / `PUBMED_BATCH_SIZE` | 500 / 200 | esearch cap / efetch batch |
| `CEA_PER_INTERVENTION_RETMAX` | 100 | Phase 2 PubMed cap per intervention |
| `CEA_OPENALEX_MAX_PAGES` | 2 | Phase 2 OpenAlex page cap |
| `SHORTLIST_PATH` / `CEA_OUTPUT_PATH` | `./data/shortlist.json` / `./data/cea_by_intervention.json` | Phase 1→2 handoff / Phase 2 output |
| `GHCEA_LOCAL_PATH` / `DCP3_LOCAL_PATH` | `./data/*.csv` | Optional CEA registry files |

API key: put `NCBI_API_KEY=...` in a gitignored `.env`; auto-loaded by
`config.py` (10 req/s with key vs 3 without).

## Outputs

All data lives in `data/`:

**Phase 1:** `data/papers_database.json` (full DB) · `data/papers_ranked.csv`
(ranked table) · `data/top_papers_for_review.json` (top 200 with full text) ·
`data/raw_responses/` (PubMed XML, OpenAlex JSON, PMC XML).
**Phase 2:** `data/shortlist.json` (human-authored) ·
`data/cea_by_intervention.json` · `data/raw_responses/cea/`.
**Synthesis:** `output/FULL_INTERVENTION_SYNTH.md`. All data outputs are
gitignored (regenerated/authored).

## Running

```bash
python3 code/11_fetch_papers.py                             # Phase 1 (~3–4 min)
cp data/shortlist.template.json data/shortlist.json         # review data/top_papers_for_review.json, then edit
python3 code/15_run_cea.py                                  # Phase 2
python3 code/17_verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md   # lint the synthesis
```

Caching: PMC full-text and per-intervention CEA XML are cached under
`data/raw_responses/`, so repeat runs are much faster.

---

## Validation findings — Vitamin A Supplementation (VAS) case study

The two-phase redesign was driven by a manual audit of a VAS synthesis produced
by the earlier single-phase pipeline. The audit surfaced recurring failures and
each is now addressed structurally:

| Failure in the old pipeline | Fix in v3 |
|-----------------------------|-----------|
| **CEA blind spot** — VAS rated "Very High" cost-effectiveness with zero usable CEAs in the corpus (PubMed isn't where CEAs live). | Two-phase split: CEA searched per shortlisted intervention; `cea_rating_allowed` guard forces `Unknown` without a CEA record. |
| **Version vs. evidence confusion** — the 2017 and 2022 Cochrane reviews (same accession CD008524) counted as independent evidence. | Cochrane-version dedup collapses shared accessions, keeping the newest. |
| **External-knowledge leak / misattribution** — figures like "823,000 deaths" (actually the Lancet *Breastfeeding* series) imported from training data. | Grounding prompt (corpus PMID per claim) + `verify_synthesis.py` flags `NOT_IN_CORPUS`. |
| **Study-type misclassification** — a *BMC Public Health* meta-analysis labelled "Cochrane". | Grounding rule: study type stated verbatim from `journal` + `publication_type`. |
| **No population targeting** — only LMIC geography was filtered. | Population filter in every query + scoring component 8. |
| **No entity model of evidence** (trial overlap / dominant-trial effects). | *Deferred* — a trial-level evidence graph (parse included-studies + forest-plot weights) is the next milestone. |

## Version history

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-05-22 | OpenAlex only, 16 keyword queries, binary keyword scoring. |
| v2.0 | 2026-05-24 | Multi-source (PubMed + OpenAlex), MeSH-based scoring, two-tier MA/SR separation, citation enrichment, modular architecture. |
| v2.1 | 2026-05-24 | Stage 3.5 PMC full-text retrieval; full-text-enhanced synthesis; `.env` auto-loading. |
| v3.0 | 2026-06-03 | **Two-phase restructure** (evidence → cost-effectiveness) with manual shortlist checkpoint. Population targeting (filter + scoring component 8). Cochrane-version dedup. Top-N → 200. Per-intervention CEA search + optional local registry + `cea_rating_allowed` guard. Grounding prompt and `verify_synthesis.py` claim verifier. |
