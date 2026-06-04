# Automated Evidence Synthesis Pipeline v2.0: Process Documentation

> **⚠️ This document describes the v2.x single-phase methodology.** The pipeline
> has since been restructured into a **two-phase design (v3.0)** — evidence
> retrieval (Phase 1, no cost-effectiveness) → manual intervention shortlist →
> targeted cost-effectiveness search (Phase 2) — with population targeting
> (under-5 / WRA), Cochrane-version deduplication, an 8th scoring component, and
> a synthesis claim-verifier. For the current architecture see
> [claude.md](claude.md) and [README.md](README.md). The Stage 1–3 retrieval and
> scoring mechanics below remain largely accurate; the track structure (Track B
> is removed from Phase 1) and the synthesis flow have changed.

## Overview

This pipeline automates the identification, ranking, and synthesis of academic evidence on nutrition interventions in low- and middle-income countries (LMICs). It combines multi-source programmatic literature search (PubMed + OpenAlex), structured scoring using authoritative metadata, and LLM-based review and synthesis.

**Repository:** [github.com/anshaji/nutri-evidence-review](https://github.com/anshaji/nutri-evidence-review)

---

## Stage 1: Literature Retrieval

**Objective:** Retrieve all meta-analyses, systematic reviews, and Cochrane reviews on nutrition interventions in LMICs, plus a parallel track for cost-effectiveness analyses and nutrition-sensitive interventions from the economics literature.

**Sources:**

| Source | Role | API | Rate Limit |
|--------|------|-----|-----------|
| PubMed (E-Utilities) | Primary — biomedical literature | esearch + efetch | 10 req/s (with API key) |
| OpenAlex | Supplementary — economics/development literature | REST API | 0.3s between requests |

### Track A: Meta-Analyses & Systematic Reviews (PubMed)

**Two-pass approach:**
- **Pass 1 (Primary tier):** Retrieves only confirmed meta-analyses using `meta-analysis[pt]` publication type filter
- **Pass 2 (Supplementary tier):** Retrieves systematic reviews using `systematic review[pt]` filter

**Query structure:**
```
[intervention MeSH/keywords] AND [LMIC filter] AND [publication type filter]
```

**LMIC filter (reusable across all queries):**
```
("developing countries"[MeSH] OR "low income"[tiab] OR "middle income"[tiab]
 OR "LMIC"[tiab] OR "sub-saharan africa"[tiab] OR "south asia"[tiab]
 OR "southeast asia"[tiab])
```

Using `"developing countries"[MeSH]` is key — this is a curated MeSH descriptor that maps to all individual LMIC country names without needing to enumerate them.

**The 12 intervention domain queries:**

| # | Domain | Key MeSH/Keywords |
|---|--------|-------------------|
| 1 | Micronutrient supplementation | `"micronutrients"[MeSH]`, `"dietary supplements"[MeSH]`, iron, zinc, vitamin A, folic acid |
| 2 | Food fortification | `"food, fortified"[MeSH]`, flour fortification, salt iodization, biofortification |
| 3 | Complementary feeding | `"infant nutritional physiological phenomena"[MeSH]`, complementary feeding, weaning |
| 4 | Breastfeeding promotion | `"breast feeding"[MeSH]`, `"lactation"[MeSH]`, kangaroo mother care |
| 5 | Acute malnutrition management | severe acute malnutrition, RUTF, CMAM |
| 6 | Maternal nutrition | `"prenatal nutritional physiological phenomena"[MeSH]`, maternal nutrition |
| 7 | WASH + nutrition | `"water purification"[MeSH]`, `"hygiene"[MeSH]`, `"sanitation"[MeSH]` AND nutrition/stunting |
| 8 | School feeding | school feeding, school meal, school nutrition |
| 9 | Growth monitoring & promotion | growth monitoring, `"nutrition surveillance"[MeSH]` |
| 10 | Deworming | `"anthelmintics"[MeSH]`, deworming AND nutrition/growth/anemia |
| 11 | Nutrition-sensitive agriculture | `"agriculture"[MeSH]`, homestead food production AND nutrition/diet |
| 12 | Integrated/multi-sectoral | `"nutrition programs and policies"[MeSH]`, nutrition-sensitive, nutrition-specific |

### Track B: Cost-Effectiveness Analyses (PubMed)

Separate track because CEAs are rarely meta-analyses — they come as original research articles.

```
("cost-benefit analysis"[MeSH] OR "cost-effectiveness"[tiab] OR "cost per DALY"[tiab]
 OR "cost-benefit"[tiab] OR "cost effective"[tiab] OR "incremental cost"[tiab])
AND ("nutrition"[tiab] OR "malnutrition"[tiab] OR "stunting"[tiab]
     OR "supplementation"[tiab] OR "fortification"[tiab]
     OR "breastfeeding"[tiab] OR "complementary feeding"[tiab])
AND [LMIC filter]
```

No publication type restriction — CEAs are indexed as regular journal articles.

### Track C: Supplementary Sweep (OpenAlex)

Retained for intervention domains PubMed covers poorly — the economics and development literature on nutrition-sensitive interventions:

| # | Query Domain |
|---|-------------|
| 1 | Cash transfers + nutrition/food security/dietary diversity |
| 2 | Social protection + child nutrition/malnutrition |
| 3 | Food subsidies / public distribution systems |
| 4 | Conditional cash transfers + nutrition/child health |

These queries use OpenAlex's full-text search with Boolean operators and target reviews/evidence syntheses.

### Retrieval Parameters

| Parameter | PubMed | OpenAlex |
|-----------|--------|----------|
| Max results per query | 500 (via `retmax`) | 500 (5 pages x 100) |
| Rate limiting | 10/s with API key | 0.3s between pages |
| Deduplication | PMID across queries | OpenAlex ID, then DOI-match against PubMed set |
| Abstract retrieval | `efetch` with `rettype=xml` | Inverted index reconstruction |
| Batch size | 200 PMIDs per efetch request | 100 per page |

### PubMed E-Utilities Method

1. **esearch** — submit query string, receive list of PMIDs + total count (JSON response)
2. **efetch** — submit PMIDs in batches of 200, receive full article records in XML
3. **Parse XML** — extract title, abstract (structured sections joined), MeSH terms, publication types, DOI, journal, year, authors
4. **Deduplicate** across all queries by PMID

### Cross-Source Deduplication

After PubMed + OpenAlex retrieval:
1. Within PubMed: by PMID (when a paper appears in multiple queries, keep the highest-tier version)
2. Within OpenAlex: by OpenAlex work ID
3. Cross-source: by DOI (normalize: strip prefix, lowercase)
   - When DOI matches, **prefer PubMed record** (richer metadata: MeSH, publication types)
   - Merge `cited_by_count` and `is_open_access` from OpenAlex into the PubMed record

### Output

A deduplicated candidate set with full metadata. Fields include:
- `id`, `title`, `abstract`, `publication_year`, `journal`, `doi`, `pmid`, `openalex_id`
- `source_db`: "pubmed" or "openalex"
- `publication_type`: list from PubMed indexing (authoritative, not inferred)
- `mesh_terms`: list of MeSH descriptor names
- `study_type`: human-readable classification
- `tier`: "primary" (meta-analysis), "supplementary" (systematic review), "cea", or "nutrition-sensitive"
- `query_origin`: which of the 12+1+4 queries found it
- `cited_by_count`: from OpenAlex cross-reference
- `is_open_access`: boolean

### Raw Response Archiving

All raw API responses are saved to `raw_responses/` for reproducibility:
- PubMed: `pubmed_{tier}_{domain}_{timestamp}.xml`
- OpenAlex: `openalex_{domain}_{timestamp}.json`

---

## Stage 2: Relevance Scoring

**Objective:** Rank all collected papers by a composite relevance score that leverages authoritative metadata (MeSH terms, publication types) for PubMed papers and falls back to keyword heuristics for OpenAlex papers.

**Method:** Each paper receives a numerical score (0-85) computed as the sum of seven components:

### Component 1: Study Design Authority (0-20 points)

**For PubMed papers:** Direct mapping from the authoritative `publication_type` field assigned by NLM indexers.

| Publication Type | Points | Rationale |
|-----------------|--------|-----------|
| Meta-Analysis | 20 | Gold standard for evidence synthesis |
| Systematic Review | 17 | Structured evidence synthesis |
| Randomized Controlled Trial | 14 | High internal validity |
| Review | 10 | May include Cochrane/umbrella reviews |
| Practice Guideline | 10 | Authoritative clinical guidance |
| Clinical Trial | 8 | Experimental evidence |
| Comparative Study | 6 | Structured comparison |
| Evaluation Study | 6 | Program evaluation |

When a paper has multiple publication types (e.g., both "Meta-Analysis" and "Systematic Review"), the **highest** score is taken.

**For OpenAlex papers (keyword fallback, capped at 15):**
- `"meta-analysis"` → 15
- `"umbrella review"` → 15
- `"cochrane"` → 14
- `"systematic review"` → 12
- `"cost-effectiveness"` → 10
- `"randomized controlled trial"` → 8

### Component 2: Topic Relevance (0-25 points)

**For PubMed papers:** Based on MeSH term set matching against curated intervention and outcome term sets.

Scoring logic:
- Matches against intervention MeSH set (e.g., Micronutrients, Food Fortified, Breast Feeding): +4 per match, max 12
- Matches against outcome MeSH set (e.g., Nutritional Status, Growth Disorders, Malnutrition): +3 per match, max 9
- Bonus for having BOTH intervention AND outcome MeSH terms: +4
- Total capped at 25

**For OpenAlex papers (keyword fallback, capped at 20):**
- Keyword presence matching: stunting (4), wasting (4), child nutrition (4), micronutrient (4), complementary feeding (4), malnutrition (3), breastfeeding (3), supplementation (3), fortification (3), food security (3)

### Component 3: Setting Relevance (0-10 points)

**For PubMed papers:** MeSH geographic terms.

Relevant MeSH: "Developing Countries", "Africa South of the Sahara", "Asia, Southeastern", "Asia, Southern", "India", "Bangladesh", "Ethiopia", "Nigeria", etc.

Scoring: +4 per matching MeSH term, capped at 10.

**For OpenAlex papers (keyword fallback):**
- `"lmic"` (5), `"low-income"` (4), `"middle-income"` (4), `"developing countr"` (4), `"sub-saharan africa"` (4), `"south asia"` (4)
- Capped at 10

### Component 4: Recency (0-10 points)

Step function based on publication year (unchanged from v1):

| Paper Age | Points | Rationale |
|-----------|--------|-----------|
| 0-5 years | 10 | Current evidence |
| 6-10 years | 7 | Still relevant |
| 11-15 years | 4 | Foundational |
| 16-20 years | 2 | Historical |
| 20+ years | 0 | Likely superseded |

### Component 5: Citation Impact (0-12 points)

Step function based on `cited_by_count` (from OpenAlex cross-reference):

| Citations | Points |
|-----------|--------|
| 500+ | 12 |
| 200-499 | 10 |
| 100-199 | 8 |
| 50-99 | 6 |
| 20-49 | 4 |
| 5-19 | 2 |
| 0-4 | 0 |

### Component 6: Open Access Bonus (0-3 points)

| Condition | Points |
|-----------|--------|
| Open access | 3 |

### Component 7: Tier Bonus (0-5 points)

| Condition | Points | Rationale |
|-----------|--------|-----------|
| Paper from Track A Pass 1 (confirmed meta-analysis) | 5 | Prioritizes the purest evidence synthesis |
| All others | 0 | — |

### What Changed from v1 Scoring

| Issue in v1 | Fix in v2 |
|-------------|-----------|
| Binary keyword matching for study type | Authoritative `publication_type` from PubMed NLM indexers |
| Keyword matching for topic relevance | MeSH term set matching (curated, hierarchical) |
| No negative signals | MeSH terms are assigned by human indexers — if "Developing Countries" isn't tagged, the paper genuinely isn't focused on LMICs |
| All study types mixed together | Two-tier system separates meta-analyses from systematic reviews at query time |
| Citation data only from OpenAlex | Cross-reference enrichment brings citation counts to PubMed papers |
| Additive keyword stacking | MeSH scoring uses caps per category to prevent gaming |

### Remaining Limitations

- **OpenAlex papers still use keyword fallback** — capped at lower scores but still noisy
- **Citation bias persists** for older papers (partially offset by recency score)
- **No full-text access** — scoring is based on metadata and abstracts only
- **MeSH indexing lag** — very recent papers may not yet have MeSH terms assigned
- **OpenAlex citation counts may lag** a few months behind reality

---

## Stage 3: Database Export

**Objective:** Save scored papers in multiple formats for review and reuse.

**Outputs:**

| File | Format | Contents |
|------|--------|----------|
| `papers_database.json` | JSON | All papers with full metadata, abstracts, and scores |
| `papers_ranked.csv` | CSV | All papers in tabular format, sorted by score descending |
| `top_papers_for_review.json` | JSON | Top 100 papers (input for Stage 4) |

**Fields per paper:**

| Field | Type | Source |
|-------|------|--------|
| `id` | string | Canonical ID (pmid:XXXXX or OpenAlex URL) |
| `title` | string | Paper title |
| `abstract` | string | Full abstract text |
| `publication_year` | int/null | Year of publication |
| `journal` | string | Journal name |
| `doi` | string/null | DOI (normalized) |
| `pmid` | string/null | PubMed ID |
| `openalex_id` | string/null | OpenAlex work ID |
| `source_db` | string | "pubmed" or "openalex" |
| `study_type` | string | Classified type (see below) |
| `publication_type` | list[string] | Raw from PubMed indexing |
| `mesh_terms` | list[string] | MeSH descriptor names |
| `cited_by_count` | int | From OpenAlex cross-reference |
| `is_open_access` | boolean | Open access status |
| `query_origin` | string | Which query found this paper |
| `tier` | string | "primary", "supplementary", "cea", or "nutrition-sensitive" |
| `relevance_score` | float | Composite score (0-85) |

**Study type classification:**
- Systematic Review & Meta-Analysis
- Meta-Analysis
- Systematic Review
- Cochrane Review
- Umbrella Review
- Cost-Effectiveness Analysis
- RCT
- Practice Guideline
- Review
- Article

---

## Stage 3.5: Full-Text Retrieval (PMC Open Access)

**Objective:** Retrieve structured full-text content from PubMed Central for top-scored papers that have open-access PMC versions, enabling deeper LLM synthesis with effect sizes, subgroup analyses, and implementation details not present in abstracts.

**Method:**

1. **PMID to PMCID conversion** — Batch API call to NCBI ID Converter (`https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/`) with up to 200 PMIDs per request
2. **PMC full-text fetch** — E-Utilities efetch with `db=pmc` for each PMCID
3. **XML parsing** — Extract structured sections (Introduction, Methods, Results, Discussion), tables (labels, captions, content), and concatenate into readable text
4. **Caching** — Raw XML saved to `raw_responses/pmc/{PMCID}.xml` for reproducibility and to avoid re-fetching

**Coverage:**
- Typically 85/99 PubMed papers have a PMCID (PMC-indexed)
- Of those, ~57 have downloadable full-text XML (body element present)
- ~28 are publisher-restricted (Cochrane reviews and some Elsevier journals block XML download despite PMC indexing)
- Final coverage: ~57% of top 100 papers have structured full text

**Output fields added to papers:**
- `fulltext_source`: "pmc" or "abstract_only"
- `fulltext`: dict with `sections` (list of {title, text}), `tables` (list of {label, caption, content}), and `full_text` (concatenated plain text)
- `pmcid`: PMC identifier (if available)

**Module:** `pipeline/fulltext_client.py`

**Known limitations:**
- NCBI ID Converter returns PMIDs as integers — must cast to str() for matching
- Some publishers (Cochrane/Wiley, Elsevier) restrict PMC XML body access
- No PDF parsing fallback (would require non-stdlib libraries)

---

## Stage 4: LLM Review and Synthesis

**Objective:** Review the top-ranked papers and produce a structured list of nutrition interventions ranked by evidence strength, cost-effectiveness, and scalability through government-led programs in LMIC settings.

**Input:** The top 100 papers from Stage 3.5 (titles, abstracts, metadata, MeSH terms, tiers, scores, AND structured full text for ~57 papers).

**Two synthesis modes:**

### Mode A: Abstract-Only Synthesis (lighter)

Uses only abstracts and metadata. Produces `INTERVENTION_SYNTHESIS.md`.

### Mode B: Full-Text-Enhanced Synthesis (deeper)

Uses full text (Results sections, tables, subgroup analyses) where available, with abstracts as fallback. Produces `FULL_INTERVENTION_SYNTH.md`.

**LLM prompt (task framing):**

> You are reviewing the top 100 papers from a multi-source systematic search of the nutrition intervention literature in LMICs. Papers were retrieved from PubMed (using MeSH terms and publication type filters) and OpenAlex (for nutrition-sensitive literature). They are ranked by a composite score weighting study design authority, MeSH-based topic relevance, setting relevance, recency, citation impact, and tier assignment.
>
> For 57 papers, you have access to structured full text (Results sections, tables, discussion) from PubMed Central. For the remaining 43 papers, you have abstracts and metadata only. Full-text papers are marked with `fulltext_source: "pmc"`.
>
> Papers are organized into tiers:
> - **Primary tier:** Confirmed meta-analyses (highest evidence quality)
> - **Supplementary tier:** Systematic reviews
> - **CEA tier:** Cost-effectiveness analyses
> - **Nutrition-sensitive tier:** Cash transfers, social protection, food subsidies (from economics literature)
>
> Your task:
>
> 1. **Identify distinct interventions.** Read across all papers and extract every discrete nutrition intervention. Group closely related variants under a single heading.
>
> 2. **Rate each intervention on three dimensions:**
>    - **Evidence strength** (A/B/C): Based on number and quality of meta-analyses, consistency of findings, study type hierarchy
>    - **Cost-effectiveness**: From CEA tier papers + general knowledge (Very High / High / Moderate / Low / Unknown)
>    - **Scalability**: Evidence of national implementation, platform compatibility, infrastructure needs (Proven national / Proven subnational / Growing / Requires investment)
>
> 3. **Rank interventions into tiers:**
>    - Tier 1: Strong evidence (A) + proven scalability + high cost-effectiveness
>    - Tier 2: Strong evidence (A or B+) + scalable with investment
>    - Tier 3: Promising evidence (B or C+) + plausible scaling pathway
>
> 4. **For each intervention, document:**
>    - Evidence rating with justification (cite specific papers by PMID, year, journal, citations)
>    - **Specific effect sizes with confidence intervals** (from full-text Results sections where available)
>    - Mechanism of action
>    - Government scaling pathway
>    - Key supporting papers from the database
>
> 5. **Synthesize cross-cutting findings** (4-6 patterns across the evidence base)
>
> 6. **Produce a summary table** (Rank, Intervention, Evidence, Cost-Effectiveness, Scalability, Target)
>
> **Constraints:**
> - Base synthesis on information in provided full text, abstracts, and metadata
> - For full-text papers: extract and report actual effect sizes (RR, OR, SMD, MD with 95% CIs)
> - For abstract-only papers: report only what is stated in the abstract
> - Do not fabricate effect sizes not present in the source material
> - Use MeSH terms and publication types to validate classification
> - Flag papers where full text was not available for key claims
> - Distinguish nutrition-specific from nutrition-sensitive interventions
> - Note where subgroup analyses (from full text) modify the headline finding

**LLM review process:**
- Papers are read in batches (top 40, then 41-100) due to context window constraints
- For each paper, the LLM reads: title, abstract, publication year, study type, publication types, MeSH terms, tier, citation count, journal, score
- For full-text papers: additionally reads the Results section text and table data
- MeSH terms help the LLM verify what intervention and population each paper actually studies
- Tier assignment helps the LLM weight evidence appropriately (primary > supplementary)
- Full-text access enables extraction of: pooled effect estimates, forest plot data, subgroup analyses, implementation context, and study heterogeneity metrics

**Outputs:**
- `INTERVENTION_SYNTHESIS.md` — Abstract-only synthesis (lighter, 18 interventions)
- `FULL_INTERVENTION_SYNTH.md` — Full-text-enhanced synthesis (deeper, 20 interventions with effect sizes)

---

## Reproducibility

To rerun the pipeline:

```bash
cd nutri-evidence-review/
# Option A: use .env file (auto-loaded by config.py)
echo "NCBI_API_KEY=your_key_here" > .env
python3 fetch_papers.py

# Option B: export environment variable
export NCBI_API_KEY=your_key_here
python3 fetch_papers.py
```

**Dependencies:** Python 3.10+ standard library only (`urllib`, `json`, `csv`, `xml.etree.ElementTree`). No external packages required.

**Runtime:** ~3-4 minutes with NCBI API key (includes PMC full-text retrieval), ~7 minutes without key.

- Stage 1 (retrieval): ~50s PubMed + ~12s OpenAlex
- Stage 2 (dedup + enrich + score): ~35s
- Stage 3.5 (PMC full text): ~60-90s (cached on subsequent runs: instant)
- Export: ~5s

**Caching:** PMC full-text XML is cached in `raw_responses/pmc/`. Subsequent runs skip already-downloaded articles, making repeat runs much faster.

**To modify:**
- **Search queries:** Edit `pipeline/queries.py` (TRACK_A_QUERIES, TRACK_B_QUERY, TRACK_C_QUERIES)
- **Scoring weights:** Edit `pipeline/scoring.py` (PUBTYPE_SCORES, MeSH term sets, component functions)
- **Number of papers for review:** Edit `TOP_N_FOR_REVIEW` in `pipeline/config.py` (default: 100)
- **API configuration:** Edit `pipeline/config.py` or create `.env` file with `NCBI_API_KEY=your_key`
- **Full-text retrieval:** Edit `pipeline/fulltext_client.py` (batch sizes, parsing logic)

---

## Pipeline Architecture Diagram

```
                    STAGE 1: RETRIEVAL                     STAGE 2      STAGE 3     STAGE 3.5       STAGE 4
                                                          SCORING      EXPORT      FULL TEXT        LLM REVIEW

Track A Pass 1 ──► PubMed: 12 queries x meta-analysis[pt] ─┐
(meta-analyses)     484 papers                               │
                                                             │
Track A Pass 2 ──► PubMed: 12 queries x systematic review[pt]│
(syst. reviews)     945 papers                               ├──► Dedup ──► Enrich ──► Score ──► PMC Full Text ──► Export
                                                             │    (PMID)    (citations   (7        (top 100)        │
Track B ─────────► PubMed: CEA query (no [pt] filter)  ─────┤    (DOI)     via OpenAlex) components) ~57 papers     │
(cost-effect.)      490 papers                               │                                     with body       │
                                                             │                                                      │
Track C ─────────► OpenAlex: 4 queries (econ/dev lit) ──────┘                                                      │
(nutrition-         2000 papers                                                                                     │
 sensitive)                                                                              papers_database.json       │
                                                                                         papers_ranked.csv          │
                    Final deduplicated set: 2,700 papers                                  top_papers_for_review.json │
                    (1,158 PubMed + 1,542 OpenAlex)                                      (with full text)           │
                                                                                                                    ▼
                                                                                                  LLM reviews top 100
                                                                                                  full text + abstracts
                                                                                                          │
                                                                                          ┌─────────��─────┴──────────────┐
                                                                                          ▼                              ▼
                                                                              INTERVENTION_SYNTHESIS.md    FULL_INTERVENTION_SYNTH.md
                                                                              (abstract-only, lighter)     (full-text-enhanced, deeper)
```

---

## File Structure

```
nutri-evidence-review/
├── fetch_papers.py              # Entry point: python3 fetch_papers.py
├── pipeline/
│   ├── __init__.py
│   ├── config.py                # API keys, .env loader, rate limits, output paths
│   ├── queries.py               # All query definitions (12 + 1 + 4)
│   ├── models.py                # Paper TypedDict (unified schema)
│   ├── pubmed_client.py         # E-Utilities: esearch, efetch, XML parsing
│   ├── openalex_client.py       # Track C: OpenAlex fetcher
│   ├── citation_enrichment.py   # DOI-based cross-reference for citation counts
│   ├── dedup.py                 # 3-phase deduplication logic
│   ├── scoring.py               # 7-component scoring algorithm
│   ├── fulltext_client.py       # PMC full-text retrieval (Stage 3.5)
│   └── main.py                  # Orchestrator: runs all stages
├── .env                         # API key (gitignored)
├── raw_responses/               # Saved API responses (gitignored)
│   ├── pubmed_*.xml             # PubMed efetch responses
│   ├── openalex_*.json          # OpenAlex API responses
│   └── pmc/                     # PMC full-text XML (one file per PMCID)
│       ├── PMC6572871.xml
│       └── ...
├── papers_database.json         # Full output (gitignored)
├── papers_ranked.csv            # CSV output (gitignored)
├── top_papers_for_review.json   # Top 100 with full text (gitignored)
├── PROCESS_DOCUMENTATION.md     # This file
├── INTERVENTION_SYNTHESIS.md    # Abstract-only synthesis (Mode A)
└── FULL_INTERVENTION_SYNTH.md   # Full-text-enhanced synthesis (Mode B)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-05-22 | Initial pipeline: OpenAlex only, 16 keyword queries, binary keyword scoring |
| v2.0 | 2026-05-24 | Multi-source (PubMed + OpenAlex), MeSH-based scoring, two-tier MA/SR separation, citation enrichment, modular architecture |
| v2.1 | 2026-05-24 | Added Stage 3.5: PMC full-text retrieval for top papers. Full-text-enhanced synthesis (FULL_INTERVENTION_SYNTH.md). .env auto-loading. API key masked from source. |
| v3.0 | 2026-06-03 | **Two-phase restructure.** Phase 1 (evidence, no CEA) + Phase 2 (targeted per-intervention cost-effectiveness). Population targeting (under-5 / WRA) as query filter + scoring component (8th component). Cochrane-version dedup. Top-N raised to 200. Synthesis claim-verifier (`verify_synthesis.py`) and grounding prompt (`prompts/synthesis_prompt.md`). See [claude.md](claude.md). |
