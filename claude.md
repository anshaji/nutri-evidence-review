# Nutrition Evidence Review Pipeline

## Project Overview

Automated evidence synthesis pipeline that identifies nutrition interventions with the strongest evidence base, cost-effectiveness, and realistic pathways to government-led scaling in LMIC settings.

**Repository:** https://github.com/anshaji/nutri-evidence-review
**Local path:** /Users/akashshaji/Documents/GitHub/nutri-evidence-review/

## Architecture

Modular Python pipeline (stdlib-only, no pip dependencies):

```
fetch_papers.py              # Entry point (thin wrapper)
pipeline/
├── __init__.py
├── config.py                # Constants, .env loader, API keys, paths
├── queries.py               # All query definitions (12 Track A + Track B + 4 Track C)
├── models.py                # Paper TypedDict (unified schema)
├── pubmed_client.py         # PubMed E-Utilities esearch/efetch + XML parsing
├── openalex_client.py       # Track C fetcher (economics/development literature)
├── citation_enrichment.py   # Batch DOI lookup in OpenAlex for citation counts
├── dedup.py                 # Within-source + cross-source deduplication
├── scoring.py               # 7-component scoring (MeSH + publication_type based)
├── fulltext_client.py       # PMC full-text retrieval for top papers (Stage 3.5)
└── main.py                  # Orchestrator: runs tracks, deduplicates, scores, exports
```

## Pipeline Stages

### Stage 1: Retrieval (3 tracks)
- **Track A (PubMed):** 12 intervention domains x 2 passes (meta-analysis primary tier, systematic review supplementary tier)
- **Track B (PubMed):** Cost-effectiveness analyses (no publication type restriction)
- **Track C (OpenAlex):** Nutrition-sensitive interventions (cash transfers, social protection, food subsidies)

### Stage 2: Deduplication (3 phases)
1. Within PubMed: by PMID
2. Within OpenAlex: by OpenAlex ID
3. Cross-source: by DOI (prefer PubMed record, merge citation count from OpenAlex)

### Stage 3: Scoring (7 components, max 85 points)
| Component | Max | Source |
|-----------|-----|--------|
| Study Design | 20 | PubMed publication_type field |
| Topic Relevance | 25 | MeSH term set matching |
| Setting Relevance | 10 | MeSH geographic terms |
| Recency | 10 | Step function on year |
| Citation Impact | 12 | OpenAlex cited_by_count |
| Open Access | 3 | OpenAlex is_oa field |
| Tier Bonus | 5 | +5 for confirmed meta-analyses |

### Stage 3.5: Full-Text Retrieval (PMC Open Access)
- Converts PMIDs → PMCIDs via NCBI ID Converter API (batch of 200)
- Fetches structured full-text XML from PMC for open-access papers
- Parses into sections (Introduction, Methods, Results, Discussion) + tables
- Caches raw XML in `raw_responses/pmc/` for reproducibility
- Papers without PMC availability are flagged as "abstract_only"
- Typically 40-60% of top papers have PMC full text
- Module: `pipeline/fulltext_client.py`

### Stage 4: LLM Review
- Top 100 papers reviewed (with full text where available)
- Two synthesis outputs:
  - `INTERVENTION_SYNTHESIS.md` — Abstract-only synthesis (18 interventions, lighter)
  - `FULL_INTERVENTION_SYNTH.md` — Full-text-enhanced synthesis (20 interventions, detailed effect sizes, subgroup analyses, implementation data)
- Full-text papers get deeper synthesis (effect sizes with CIs, subgroups, implementation details)
- Abstract-only papers flagged with lower confidence in synthesis
- Interventions tiered by evidence strength, cost-effectiveness, and scalability
- Includes PMIDs, citation counts, journal names, cross-cutting findings

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

- `papers_database.json` — full database (all fields)
- `papers_ranked.csv` — ranked spreadsheet view
- `top_papers_for_review.json` — top 100 for LLM review (includes full text where available)
- `raw_responses/` — raw XML/JSON from APIs (PubMed, OpenAlex, PMC)
- `raw_responses/pmc/` — cached PMC full-text XML files (one per PMCID)
- `INTERVENTION_SYNTHESIS.md` — abstract-only synthesis (18 interventions)
- `FULL_INTERVENTION_SYNTH.md` — full-text-enhanced synthesis (20 interventions, detailed effect sizes)
- `PROCESS_DOCUMENTATION.md` — full methodology documentation

All data outputs are gitignored (regenerated by pipeline).

## Running the Pipeline

```bash
cd /Users/akashshaji/Documents/GitHub/nutri-evidence-review
python3 fetch_papers.py
```

Expected runtime: ~3-4 minutes (includes PMC full-text retrieval). Expected yield: ~1,500-3,000 PubMed papers + ~300-500 OpenAlex papers after dedup. PMC full text retrieved for ~57 of top 100 papers.

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

### Pipeline reliability fixes (prioritized, from the VAS audit)
1. **Prompt hardening (Stage 4, cheap, do first).** Ground every claim in provided metadata: state study type/source verbatim from `journal` + `publication_type` (never infer "Cochrane" unless `journal` == "Cochrane Database of Systematic Reviews"); require a corpus PMID on every numeric claim (else emit `not in corpus`); separate all-cause from cause-specific evidence and flag underpowered pathways; report both fixed/random estimates and name any dominant trial the review identifies.
2. **Cochrane-ID dedup + CEA-rating guard (structural, cheap).** Collapse records sharing a Cochrane review ID (e.g. CD008524) so a version update is not counted as new evidence (`dedup.py`); forbid assigning a cost-effectiveness rating unless a CEA record exists, else output `Unknown` (`scoring.py` / `main.py`).
3. **Claim-verification pass (new `verify.py`, medium effort).** For each `{value, pmid}`, confirm the PMID is in the corpus and that its title/abstract supports the claim (string match + LLM check). Catches misattribution and external-knowledge leaks.
4. **Trial-level extraction / evidence graph (large effort).** Parse included-studies lists and forest-plot weights from full text; match trials by registry ID (NCT/ISRCTN) or author+year; build `Review → trials → weights`. Enables overlap/double-counting detection and DEVTA-class insights.
5. **Dedicated CEA data source.** Integrate the Tufts CEA Registry / GHCEA or DCP3 rather than relying on PubMed Track B for cost-effectiveness.

### Longer-term / methodological
- List of LMIC countries (standardized)
- PubMed & Web of Science discovery validation
- Comparison between OpenAlex & PubMed-Web of Science coverage
- Building a structure for extraction of information from meta-analyses
- Automating Stage 4 LLM review with structured prompts
- Unpaywall integration for additional full-text coverage (currently PMC-only)
- PDF parsing for papers without PMC XML availability
