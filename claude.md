# Nutrition Evidence Review Pipeline

## Project Overview

Automated evidence synthesis pipeline that identifies nutrition interventions for **children under 5** and **women of reproductive age (WRA)** with the strongest evidence base, cost-effectiveness, and realistic pathways to government-led scaling in LMIC settings.

The pipeline runs in **two phases** with a manual review checkpoint between them:
- **Phase 1 (Evidence):** PubMed + OpenAlex, population-targeted, *no* cost-effectiveness. Rank, take top 200, retrieve full text, emit review-ready JSON. A human/LLM reviews it in-conversation and authors a shortlist of interventions.
- **Phase 2 (Cost-effectiveness):** for each shortlisted intervention, a targeted CEA deep-search (PubMed + OpenAlex + optional local registry).
- **Final synthesis:** human/LLM uses both datasets in-conversation (no API automation).

This split is the structural fix for the VAS audit's CEA blind spot: cost-effectiveness is only searched for the interventions that actually survive the evidence screen.

**Repository:** https://github.com/anshaji/nutri-evidence-review
**Local path:** /Users/akashshaji/Documents/GitHub/nutri-evidence-review/

## Architecture

Modular Python pipeline (stdlib-only, no pip dependencies):

```
fetch_papers.py              # Phase 1 entry point (evidence)
run_cea.py                   # Phase 2 entry point (cost-effectiveness, takes shortlist.json)
verify_synthesis.py          # Claim-verification lint for a finished synthesis
pipeline/
├── __init__.py
├── config.py                # Constants, .env loader, API keys, paths, Phase 2 knobs
├── queries.py               # Track A (12) + Track C (4) + population filter + CEA builders
├── models.py                # Paper TypedDict (+ cochrane_id, superseded_by), extract_cochrane_id
├── pubmed_client.py         # PubMed E-Utilities esearch/efetch + XML parsing
├── openalex_client.py       # Track C fetcher (economics/development literature)
├── citation_enrichment.py   # Batch DOI lookup in OpenAlex for citation counts
├── dedup.py                 # PMID + Cochrane-version + OpenAlex + cross-source dedup
├── scoring.py               # 8-component scoring (adds Population Relevance)
├── fulltext_client.py       # PMC full-text retrieval for top papers (Stage 3.5)
├── main.py                  # Phase 1 orchestrator (run_phase1)
├── cea_client.py            # Phase 2: targeted CEA retrieval per intervention
├── ghcea_registry.py        # Phase 2: optional local CEA-registry CSV lookup
├── cea_main.py              # Phase 2 orchestrator (run_phase2)
└── verify.py                # Post-synthesis claim verification (corpus membership + support)
prompts/
└── synthesis_prompt.md      # Stage 4 grounding checklist (hardening rules + CEA-rating guard)
data/
└── README.md                # How to add an optional local CEA registry CSV
```

## Pipeline Stages

## PHASE 1 — Evidence (`python3 fetch_papers.py` → `run_phase1`)

### Stage 1: Retrieval (2 tracks — NO cost-effectiveness)
- **Track A (PubMed):** 12 intervention domains x 2 passes (meta-analysis primary tier, systematic review supplementary tier)
- **Track C (OpenAlex):** Nutrition-sensitive interventions (cash transfers, social protection, food subsidies)
- **Population targeting:** every query ANDs in a `POPULATION_FILTER` (under-5 OR WRA: Infant/Child Preschool/Pregnant Women/maternal MeSH + tiab). A paper on **either** population qualifies. `build_pubmed_query` is the single chokepoint feeding all 24 Track A sub-queries; Track C searches are wrapped with `build_openalex_search`.

### Stage 2: Deduplication
1. Within PubMed: by PMID
2. **Cochrane version dedup:** collapse records sharing a `cochrane_id` (e.g. CD008524), keep newest, tag older `superseded_by` — a version update no longer counts as new evidence
3. Within OpenAlex: by OpenAlex ID
4. Cross-source: by DOI (prefer PubMed record, merge citation count from OpenAlex)

### Stage 3: Scoring (8 components, max ≈ 95 points)
| Component | Max | Source |
|-----------|-----|--------|
| Study Design | 20 | PubMed publication_type field |
| Topic Relevance | 25 | MeSH term set matching |
| Setting Relevance | 10 | MeSH geographic terms |
| Recency | 10 | Step function on year |
| Citation Impact | 12 | OpenAlex cited_by_count |
| Open Access | 3 | OpenAlex is_oa field |
| Tier Bonus | 5 | +5 for confirmed meta-analyses |
| **Population Relevance** | **10** | **under-5 / WRA MeSH or keyword fallback** |

### Stage 3.5: Full-Text Retrieval (PMC Open Access)
- Converts PMIDs → PMCIDs via NCBI ID Converter API (batch of 200)
- Fetches structured full-text XML from PMC for open-access papers
- Parses into sections (Introduction, Methods, Results, Discussion) + tables
- Caches raw XML in `raw_responses/pmc/` for reproducibility
- Papers without PMC availability are flagged as "abstract_only"
- Runs over **all top 200** papers (was top 100)
- Module: `pipeline/fulltext_client.py`

### Stage 4: Manual Review → shortlist
- Top 200 papers reviewed **in-conversation** (no API automation), guided by `prompts/synthesis_prompt.md`
- Human/LLM shortlists interventions and authors `shortlist.json` (from `shortlist.template.json`)

## PHASE 2 — Cost-Effectiveness (`python3 run_cea.py [shortlist.json]` → `run_phase2`)

- Reads `shortlist.json`; for **each** shortlisted intervention runs a targeted CEA search:
  - PubMed: `CEA_TERM_SKELETON` AND (name/synonyms[tiab] OR mesh[MeSH]) AND LMIC (`build_cea_pubmed_query`)
  - OpenAlex: cost terms AND (name OR synonyms) AND LMIC (`build_cea_openalex_search`)
  - Optional local registry match (`ghcea_registry.py`) — see Phase 2 CEA registry note
- Dedups + scores, writes `cea_by_intervention.json` (per-intervention `cea_papers`, `registry_matches`, `cea_rating_allowed`)
- **CEA-rating guard (#2b):** `cea_rating_allowed` is false when an intervention has no CEA papers and no registry match → the synthesis must record cost-effectiveness as `Unknown`, never invent one

## Final Synthesis (in-conversation)
- Human/LLM uses **both** `top_papers_for_review.json` (Phase 1) and `cea_by_intervention.json` (Phase 2), following `prompts/synthesis_prompt.md`
- Outputs `INTERVENTION_SYNTHESIS.md` (abstract-only) and `FULL_INTERVENTION_SYNTH.md` (full-text-enhanced, effect sizes/subgroups)
- Run `python3 verify_synthesis.py <synthesis.md>` afterward to lint every numeric claim against the corpus

## Key Technical Decisions

- **Python 3.13 stdlib-only** — pip is broken on this machine; uses urllib, json, csv, xml.etree.ElementTree
- **`from __future__ import annotations`** required in models.py, pubmed_client.py, openalex_client.py for `int | None` syntax in TypedDict
- **PubMed as primary source** — authoritative MeSH terms and publication_type metadata beat keyword heuristics
- **OpenAlex retained for Track C only** — economics/development literature not well-indexed in PubMed
- **Citation enrichment** — batch DOI lookup in OpenAlex (50 DOIs per request) to get cited_by_count for PubMed papers
- **PMC full-text** — NCBI ID Converter API (batch 200) to get PMCIDs, then efetch db=pmc for XML; ~57/100 top papers have full text (28 Cochrane reviews are publisher-restricted)
- **PMID type normalization** — ID Converter returns PMIDs as integers; must str() them to match paper dict keys
- **Raw responses saved** to `raw_responses/` for reproducibility (PubMed XML, OpenAlex JSON, PMC XML)

## Configuration

- API key stored in `.env` (gitignored), auto-loaded by `pipeline/config.py`
- No need to manually export — just `python3 fetch_papers.py`
- NCBI rate limit: 10 req/s with key (0.11s delay)

## Outputs

**Phase 1:**
- `papers_database.json` — full database (all fields)
- `papers_ranked.csv` — ranked spreadsheet view
- `top_papers_for_review.json` — top 200 for review (includes full text where available)
- `raw_responses/` — raw XML/JSON from APIs (PubMed, OpenAlex, PMC); `raw_responses/pmc/` cached full-text XML

**Phase 2:**
- `shortlist.json` — human-authored intervention shortlist (from `shortlist.template.json`)
- `cea_by_intervention.json` — per-intervention CEA evidence + registry matches
- `raw_responses/cea/` — cached per-intervention CEA XML

**Synthesis:**
- `INTERVENTION_SYNTHESIS.md` / `FULL_INTERVENTION_SYNTH.md` — the two synthesis modes
- `PROCESS_DOCUMENTATION.md` — full methodology documentation

All data outputs (incl. `shortlist.json`, `cea_by_intervention.json`, `data/*.csv`) are gitignored (regenerated/authored).

## Running the Pipeline

```bash
cd /Users/akashshaji/Documents/GitHub/nutri-evidence-review

# Phase 1 — evidence (~3-4 min)
python3 fetch_papers.py

# → review top_papers_for_review.json in-conversation, then:
cp shortlist.template.json shortlist.json   # and edit it with the shortlisted interventions

# Phase 2 — cost-effectiveness (scales with #interventions)
python3 run_cea.py                          # or: python3 run_cea.py path/to/shortlist.json

# → produce synthesis in-conversation (prompts/synthesis_prompt.md), then lint:
python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md
```

Phase 1 expected yield: somewhat lower than the pre-population-filter pipeline (the under-5/WRA clause tightens Track A). PMC full text retrieved for ~50%+ of the top 200.

## Phase 2 CEA registry note

The "dedicated CEA source" is an **optional local CSV**, not a live API. A research spike found neither the Tufts/CEVR Global Health CEA Registry (a client-side JS app — `urllib` gets an empty shell) nor DCP3 (a PDF supplement) is reachable from stdlib `urllib`. So `data/README.md` documents a one-time manual download to `data/ghcea_registry.csv`; if absent, Phase 2 runs fine on the PubMed/OpenAlex CEA backbone and reports zero registry matches.

## Known Issues / Gotchas

- **NCBI ID Converter returns PMIDs as int** — must cast to str() for dict key matching
- **Cochrane reviews block PMC full text** — 28/85 PMC-available papers have no `<body>` element (publisher restricts XML download)
- **`from __future__ import annotations`** must be first import in modules using `int | None` in TypedDict
- **pip is broken** on this machine — all code must use stdlib only

## Validation Findings — Vitamin A Supplementation (VAS) Case Study

A deep manual audit of the VAS synthesis surfaced a set of recurring LLM-reasoning and structural gaps. These generalize to the whole pipeline and should guide future work.

### LLM reasoning gaps (Stage 4 synthesis)
- **Study-type misclassification.** The synthesis labelled Imdad 2011 (a CHERG-methods meta-analysis in *BMC Public Health*, built to feed the Lives Saved Tool / LiST) as a "Cochrane review." The authoritative `journal` and `publication_type` fields were in context but ignored — the LLM pattern-matched on "systematic review by Imdad."
- **Version vs. evidence confusion.** The 2017 and 2022 Cochrane reviews are the **same review** (CD008524); the 2022 update found **no new RCTs** (same 47 studies, 1,223,856 children, near-identical conclusions). The synthesis presented them as three independent "evidence generations" — double-counting one review and inflating apparent robustness.
- **Effect-size divergence not traced to its cause.** All-cause mortality is RR 0.88 (fixed-effect) vs RR 0.76 (random-effect). This is driven by the **DEVTA trial** (India, ~1M children, RR ~0.96), which holds ~61.7% of the fixed-effect weight. The random-effect estimate ≈ Imdad 2011's ~24% reduction. The LLM flagged "models differ" but never named DEVTA — the actual explanation a domain expert reaches for immediately.
- **Mechanism left unexamined.** The genuinely thin evidence is *cause-specific* mortality (diarrhoea/measles pathways are underpowered and inconsistent), not the all-cause finding. The synthesis dwelt on the all-cause effect-size dispute and missed the real gap.

### Structural / data gaps (retrieval + architecture)
- **CEA blind spot.** VAS was rated "Very High" cost-effectiveness, but Track B retrieved **zero usable CEA papers** for it. PubMed is not where CEAs live.
- **External-knowledge leak.** Figures like "$1–3 per child per year" and "823,000 deaths preventable" came from LLM training data, not the corpus. The 823K figure is actually the Lancet **Breastfeeding** Series (PMID 26869575) — misattributed to VAS.
- **No trial-overlap detection.** The pipeline treats each meta-analysis as an atomic blob and cannot tell that reviews share primary trials, that one trial dominates a pooled estimate, or that an update supersedes a prior version.
- **Root cause:** the pipeline has **no entity model of the evidence** — no representation of `Review → {included trials, weights, version-of}`. The data to detect the version/overlap/DEVTA issues is sitting in the retrieved full-text XML, but it is never extracted into structure.

## Future Work

### Pipeline reliability fixes (from the VAS audit)
1. **✅ DONE — Prompt hardening (Stage 4).** Grounding checklist committed at `prompts/synthesis_prompt.md` (verbatim study type, corpus PMID on every number, all-cause vs cause-specific split, fixed/random + dominant trial, version≠evidence).
2. **✅ DONE — Cochrane-ID dedup + CEA-rating guard.** `deduplicate_cochrane` in `dedup.py` collapses records sharing a `cochrane_id`; the two-phase split + `cea_rating_allowed` flag (`cea_main.py`) + prompt rule enforce `Unknown` cost-effectiveness when no CEA record exists.
3. **✅ DONE — Claim-verification pass.** `pipeline/verify.py` + `verify_synthesis.py`: corpus-membership + numeric-support checks (automated); semantic support flagged for in-conversation review.
4. **⏳ DEFERRED (next milestone) — Trial-level extraction / evidence graph (large effort).** Parse included-studies lists and forest-plot weights from full text; match trials by registry ID (NCT/ISRCTN) or author+year; build `Review → trials → weights`. Enables overlap/double-counting detection and DEVTA-class insights. **This is the remaining big piece.**
5. **✅ PARTIAL — Dedicated CEA data source.** Phase 2 supports an optional local CEA registry CSV (`ghcea_registry.py`) since neither GHCEA nor DCP3 is API-reachable (see Phase 2 CEA registry note). Targeted PubMed/OpenAlex CEA search is the always-on backbone.

### Longer-term / methodological
- List of LMIC countries (standardized)
- PubMed & Web of Science discovery validation
- Comparison between OpenAlex & PubMed-Web of Science coverage
- Building a structure for extraction of information from meta-analyses
- Automating Stage 4 LLM review with structured prompts
- Unpaywall integration for additional full-text coverage (currently PMC-only)
- PDF parsing for papers without PMC XML availability
