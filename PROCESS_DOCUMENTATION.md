# Automated Evidence Synthesis Pipeline: Process Documentation

## Overview

This pipeline automates the identification, ranking, and synthesis of academic evidence on nutrition interventions in low- and middle-income countries (LMICs). It combines programmatic literature search and scoring (Stages 1-3) with LLM-based review and synthesis (Stage 4).

---

## Stage 1: Literature Retrieval

**Objective:** Cast a wide net across the academic literature to collect all potentially relevant meta-analyses, systematic reviews, and review papers on nutrition interventions in LMICs.

**Source:** OpenAlex API (free, no API key required, structured metadata, 250M+ works indexed)

**Method:**
- 16 predefined search queries are executed sequentially against the OpenAlex `/works` endpoint
- Each query targets a specific intervention domain (e.g., micronutrient supplementation, complementary feeding, cash transfers, WASH, school feeding)
- Each query is constructed as a Boolean string combining:
  - **Intervention terms** (e.g., `"iron supplementation"`, `"food fortification"`)
  - **Setting terms** (e.g., `"LMIC"`, `"low-income"`, `"developing countries"`)
  - **Study type terms** (e.g., `"meta-analysis"`, `"systematic review"`)
- Up to 300 results per query (3 pages x 100 results) are retrieved
- Results are deduplicated by OpenAlex work ID across all queries

**Output:** A deduplicated set of candidate papers with full metadata (title, abstract, publication year, citation count, journal, DOI, open access status)

**Parameters:**
- `per_page`: 100 (OpenAlex maximum)
- `max_pages`: 3 per query
- `filter`: `type:article|review`
- Rate limiting: 0.3s between pages, 0.5s between queries

**Limitations:**
- OpenAlex search is relevance-ranked but not exhaustive; some relevant papers may not appear in the top 300 for any query
- Abstracts are available for most but not all papers (reconstructed from OpenAlex's inverted index format)
- Full text is not retrieved — only titles, abstracts, and metadata

---

## Stage 2: Relevance Scoring

**Objective:** Rank all collected papers by a composite relevance score that prioritizes high-quality evidence, recency, topic relevance, and citation impact.

**Method:** Each paper receives a numerical score (0-100+) computed as the sum of five components:

### Component 1: Study Type Score (0-15 points)
Keyword matching on title + abstract. Points are additive if multiple keywords match.

| Keyword | Points | Rationale |
|---------|--------|-----------|
| `"meta-analysis"` | 15 | Gold standard for evidence synthesis |
| `"cochrane"` | 14 | Rigorous, standardized methodology |
| `"umbrella review"` | 14 | Review of reviews — highest-level synthesis |
| `"systematic review"` | 12 | Structured evidence synthesis |
| `"cost-effectiveness"` / `"cost-effective"` / `"cost-benefit"` | 10 | Directly relevant to scaling decisions |
| `"randomized controlled trial"` | 8 | High internal validity |
| `"evidence review"` | 8 | Structured evidence assessment |
| `"lancet"` | 5 | High-impact venue (appears in abstract citations) |

### Component 2: Topic Relevance Score (0-~50 points)
Keyword presence matching on title + abstract. Binary: keyword is present or not. Points are additive across all matched keywords.

**Setting keywords:**

| Keyword | Points |
|---------|--------|
| `"lmic"` | 5 |
| `"low-income"` | 4 |
| `"middle-income"` | 4 |
| `"developing countr"` | 4 |
| `"sub-saharan africa"` | 4 |
| `"south asia"` | 4 |

**Scaling/policy keywords:**

| Keyword | Points |
|---------|--------|
| `"scaling"` | 6 |
| `"scale-up"` | 6 |
| `"government"` | 5 |
| `"national program"` | 5 |
| `"policy"` | 4 |
| `"implementation"` | 3 |

**Nutrition domain keywords:**

| Keyword | Points |
|---------|--------|
| `"stunting"` | 4 |
| `"wasting"` | 4 |
| `"undernutrition"` | 4 |
| `"child nutrition"` | 4 |
| `"maternal nutrition"` | 4 |
| `"complementary feeding"` | 4 |
| `"micronutrient"` | 4 |
| `"malnutrition"` | 3 |
| `"anemia"` / `"anaemia"` | 3 |
| `"breastfeeding"` | 3 |
| `"supplementation"` | 3 |
| `"fortification"` | 3 |
| `"food security"` | 3 |

### Component 3: Recency Score (0-10 points)
Step function based on publication year.

| Paper Age | Points | Rationale |
|-----------|--------|-----------|
| 0-5 years | 10 | Current evidence, reflects latest program data |
| 6-10 years | 7 | Still relevant, may miss recent developments |
| 11-15 years | 4 | Foundational but potentially outdated |
| 16-20 years | 2 | Historical importance only |
| 20+ years | 0 | Likely superseded |

### Component 4: Citation Impact (0-12 points)
Step function based on raw citation count.

| Citations | Points | Rationale |
|-----------|--------|-----------|
| 500+ | 12 | Landmark paper |
| 200-499 | 10 | Highly influential |
| 100-199 | 8 | Well-cited |
| 50-99 | 6 | Moderately cited |
| 20-49 | 4 | Some influence |
| 5-19 | 2 | Limited citations |
| 0-4 | 0 | New or niche |

### Component 5: Open Access Bonus (0-3 points)

| Condition | Points | Rationale |
|-----------|--------|-----------|
| Open access | 3 | Accessible for verification; more likely to be used in LMIC policy |

### Known Limitations of Scoring
- **Binary keyword matching:** A paper mentioning "low-income" once scores the same as one entirely focused on low-income settings. No frequency weighting.
- **No negative signals:** A paper saying "unlike in low-income settings" still earns points for containing "low-income."
- **Citation bias toward older papers:** Older papers have had more time to accumulate citations. The recency score partially offsets this but doesn't fully correct it.
- **No semantic understanding:** The scorer cannot distinguish between a paper that studies an intervention and one that merely references it.
- **Additive scoring:** Keywords in the same category stack. A paper mentioning many nutrition terms scores higher even if it's not more relevant.

## Notes
 -- **List of LMIC countries**
 -- **PubMed & Web of Science for discovery validation**
 -- **Comparison between OpenAlex & PubMed-Web of Science**
 -- **Building a structure for extraction of information from Meta-analysis** - Meta analysis of a meta analysis - concerns on mixing reviews with meta-analysis - maybe meta-analysis only constraint?
---

## Stage 3: Database Export

**Objective:** Save scored papers in multiple formats for review and reuse.

**Outputs:**

| File | Format | Contents |
|------|--------|----------|
| `papers_database.json` | JSON | All papers with full metadata, abstracts, and scores |
| `papers_ranked.csv` | CSV | All papers in tabular format, sorted by score descending |
| `top_papers_for_review.json` | JSON | Top 75 papers only (input for Stage 4) |

**Fields per paper:**
- `openalex_id`: Unique identifier in OpenAlex
- `title`: Paper title
- `publication_year`: Year of publication
- `study_type`: Classified as one of: Umbrella Review, Systematic Review & Meta-Analysis, Meta-Analysis, Cochrane Review, Systematic Review, Scoping Review, Narrative Review, RCT, Review, Article
- `cited_by_count`: Total citation count from OpenAlex
- `source`: Journal or publication venue
- `doi_url`: DOI link or best available URL
- `is_open_access`: Boolean
- `abstract`: Reconstructed full abstract text
- `relevance_score`: Composite score from Stage 2

---

## Stage 4: LLM Review and Synthesis

**Objective:** Review the top-ranked papers and produce a structured list of nutrition interventions ranked by evidence strength, cost-effectiveness, and scalability through government-led programs in LMIC settings.

**Input:** The top 75 papers from Stage 3 (titles, abstracts, metadata, and scores).

**LLM prompt (implicit task framing):**

> You are reviewing the abstracts and metadata of the top 75 papers from a systematic search of the nutrition intervention literature in LMICs. These papers were retrieved from OpenAlex using 16 search strategies and ranked by a composite score weighting study type, recency, citation impact, LMIC relevance, and open access status.
>
> Your task:
>
> 1. **Identify distinct interventions.** Read across all 75 abstracts and extract every discrete nutrition intervention that appears. Group closely related variants (e.g., "iron supplementation" and "iron-folic acid supplementation") under a single intervention heading with variants noted.
>
> 2. **Rate each intervention on three dimensions:**
>    - **Evidence strength** (A/B/C): Based on number and quality of meta-analyses/systematic reviews, consistency of effect sizes across studies, and study type hierarchy (Cochrane/umbrella reviews > meta-analyses > systematic reviews > narrative reviews)
>    - **Cost-effectiveness**: Based on any cost-effectiveness data reported in abstracts, plus general knowledge of intervention delivery costs (Very High / High / Moderate / Low / Unknown)
>    - **Scalability through government-led programs**: Based on evidence of national-level implementation, compatibility with existing delivery platforms (ANC, immunization, schools, social protection), and infrastructure requirements (Proven at national level / Proven subnational / Growing / Requires major investment)
>
> 3. **Rank interventions into tiers:**
>    - Tier 1: Strong evidence (A) + proven scalability + high cost-effectiveness
>    - Tier 2: Strong evidence (A or B+) + scalable with investment
>    - Tier 3: Promising evidence (B or C+) + plausible scaling pathway
>
> 4. **For each intervention, document:**
>    - The intervention name and brief description
>    - Evidence rating with justification (cite specific papers by author, year, journal, citation count)
>    - Mechanism of action (one sentence)
>    - Government scaling pathway (how a LMIC government would implement this)
>    - Key supporting papers from the database
>
> 5. **Synthesize cross-cutting findings:** Identify 4-6 patterns that emerge across the full body of evidence (e.g., integration effects, critical windows, delivery platforms, equity considerations).
>
> 6. **Produce a summary table** with columns: Rank, Intervention, Evidence Rating, Cost-Effectiveness, Scalability, Primary Target Population.
>
> **Constraints:**
> - Base your synthesis only on information present in the paper titles, abstracts, and metadata provided. Do not fabricate findings or effect sizes not present in the abstracts.
> - Where abstracts are truncated or uninformative, note this and rely on title + metadata for classification.
> - Flag any papers that appear misclassified or irrelevant to the core question.
> - Distinguish between nutrition-specific interventions (directly address nutrition) and nutrition-sensitive interventions (address underlying determinants).

**LLM review process:**
- Papers are read in batches (top 40, then 41-75) due to context window constraints
- The LLM reads each paper's title, abstract (up to 500-600 characters), publication year, study type, citation count, and journal
- Interventions are extracted by identifying what each paper studies, then grouping across papers
- Evidence ratings are assigned based on the number and type of supporting papers, not on any single paper

**Output:** `INTERVENTION_SYNTHESIS.md` — a structured document containing the tiered intervention list, individual intervention profiles, summary table, and cross-cutting findings.

---

## Reproducibility

To rerun the pipeline:

```bash
cd nutrition_evidence/
python3 fetch_papers.py
```

The script uses only Python standard library (`urllib`, `json`, `csv`). No external packages required. Results may vary slightly across runs due to OpenAlex index updates and relevance ranking changes.

To modify:
- **Search queries:** Edit `SEARCH_QUERIES` list in `fetch_papers.py`
- **Scoring weights:** Edit `TYPE_SCORES`, `TOPIC_SCORES`, and the step functions in `score_paper()`
- **Number of papers for review:** Change `top_n` in `main()` (default: 75)
- **Email for polite API use:** Change `MAILTO` constant

---

## Pipeline Summary Diagram

```
Stage 1: RETRIEVAL          Stage 2: SCORING           Stage 3: EXPORT           Stage 4: LLM REVIEW
                                                                                  
16 search queries ──►  OpenAlex API  ──►  3,519 papers  ──►  Score each paper  ──►  papers_database.json
(Boolean strings)      (titles,           (deduplicated)     (5 components:        papers_ranked.csv
                        abstracts,                            type, topic,          top_papers_for_review.json
                        metadata)                             recency, cites,                │
                                                              open access)                   │
                                                                                             ▼
                                                                                    LLM reads top 75
                                                                                    abstracts + metadata
                                                                                             │
                                                                                             ▼
                                                                                    INTERVENTION_SYNTHESIS.md
                                                                                    (17 interventions, tiered,
                                                                                     with evidence ratings)
```
