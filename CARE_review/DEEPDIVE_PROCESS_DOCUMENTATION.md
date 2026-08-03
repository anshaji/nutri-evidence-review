# CARE/ScaleWorks Deep-Dive: Process Documentation

**What this documents:** the end-to-end method used to produce
`CARE_review/CARE_DEEPDIVE_REVIEW.md` — a PICOS-structured, implementation-weighted
evidence review of three interventions (CMAM, Breastfeeding support, Antenatal MMS)
for CARE and IA partners (Save the Children, Mercy Corps).

**Relationship to the main pipeline:** this is a *layer over* the v3/v4 pipeline
documented in `PROCESS_DOCUMENTATION.md`, not a replacement. It reuses the same
clients, dedup, citation enrichment, full-text retrieval, and verifier. Only the
**query layer**, the **ranking**, and the **extraction schema** are new. All
deep-dive outputs are namespaced under `data/deepdive/` so the original pipeline's
data is never touched; `data/fulltext/` and `data/raw_responses/` are deliberately
**shared** so network caching is reused across both.

**Run date:** 2026-07-22 → 2026-07-30 · **Status:** full-text evidence complete
(981/981 full-text papers extracted); 652 abstract-only papers outstanding.

---

## 0. Why this review is shaped differently

The initial 15-intervention synthesis answered *"does it work?"*. Partner technical
experts said that was the wrong binding question. The steer, in their words:

> **Save the Children:** "Adherence/coverage — not efficacy — is the binding
> constraint… we've known these are the High Impact Nutrition Interventions yet we
> still aren't achieving the WHA Targets because gov'ts/NGOs/donors haven't cracked
> this nut of (sustainable) operationalization."

> **CARE (TE#2):** breastfeeding must be disaggregated — "strong facility-based
> support around delivery" vs "targeted counselling… through CHWs with repeated
> contacts."

> **Save the Children:** the three interventions were chosen to "test the model…
> from three different positions" — commodity-based (MMS), behavioural/SBCC
> (breastfeeding), health-system treatment (CMAM).

Three design consequences follow, and they drive every stage below:

1. **A dual outcome axis.** Every intervention is assessed on clinical outcomes
   *and* implementation outcomes (coverage, adherence, delivery platform, barriers,
   scalability, equity). Implementation is not a footnote — it is a first-class
   retrieval target, a first-class ranking signal, and a first-class schema field.
2. **Cost is out of scope for this pass.** Per the user's "evidence first, cost
   later" instruction, cost/CEA is deferred to the pipeline's existing Phase 2
   (`code/15_run_cea.py`). Cost terms are excluded from queries, extraction, and
   synthesis. The usual "cost-effectiveness" rating is replaced by an
   **Implementation readiness** rating.
3. **Breastfeeding is disaggregated** — but see §2.2: *where* the split happens
   turned out to be a methodological finding.

---

## Pipeline at a glance

```
PICOS spec (human)                       CARE_review/PICOS_specification.md
   │
   ▼
Stage 1  PICOS-targeted retrieval        code/28_run_deepdive.py
         3 blocks × (MA + SR + IMPL) + OpenAlex
   │                                      → data/deepdive/{block}.json  (1,671 papers)
   ▼
Stage 2  Relevance validation (human-in-loop)   → title-anchor fix, BF re-scope
   │
   ▼
Stage 3  Corpus assembly                 …pipeline.py corpus   → deepdive_corpus.json (1,636)
   │
   ▼
Stage 4  Full-text retrieval             …pipeline.py fulltext → data/fulltext/  (981, 60%)
   │
   ▼
Stage 5  Cards + token-balanced batches  …pipeline.py cards    → extraction_inputs/ (156 batches)
   │
   ▼
Stage 6  Multi-agent extraction          Workflow, 1 Sonnet agent/batch
   │                                      → evidence_db/batch_*.json  (984 records)
   ▼
Stage 7  Merge + validate                …pipeline.py merge    → evidence_db.json (648 on-topic)
   │
   ▼
Stage 8  Per-intervention synthesis      prompts/deepdive_synthesis_prompt.md
   │                                      → synthesis_sections/{cat}.md
   ▼
Stage 9  Verification (lint every number) code/17_verify_synthesis.py
   │
   ▼
Stage 10 Assembly                        …pipeline.py assemble → CARE_DEEPDIVE_REVIEW.md
```

---

## Stage 0 — PICOS specification (human-authored, reviewed)

**Output:** `CARE_review/PICOS_specification.md`

Written *before* any retrieval, from the partner feedback document plus the existing
full-corpus synthesis. Four blocks were specified (CMAM, BF-facility, BF-community,
MMS), each with Population / Intervention / Comparison / Outcomes / Study-types, plus
cross-cutting parameters and four explicitly-flagged open decisions.

**Why first:** the PICOS is what the query layer, the scoring weights, and the
extraction schema are all derived from. Drafting it first meant the background
reading could be *targeted* at gaps rather than open-ended.

**Open decisions and how they were resolved** (recorded in the spec, §7):

| Decision | Resolution |
|---|---|
| Emergency vs development scope | Development-primary; emergency as tagged sub-analysis |
| Cash+/SBCC breadth for BF | Include cash+SBCC-for-BF; exclude general complementary feeding |
| SQ-LNS as an MMS shadow arm | Light comparative reference only, not a full block |
| Country pre-commitment | **Country-agnostic retrieval**, country-fit at synthesis — avoids biasing the evidence base toward pre-selected countries |

---

## Stage 1 — PICOS-targeted retrieval

**Code:** `code/03_queries.py` (`DEEPDIVE_BLOCKS`), `code/27_deepdive.py`
**Run:** `python3 code/28_run_deepdive.py [block …]`
**Output:** `data/deepdive/{cmam,breastfeeding,mms}.json` + `deepdive_combined.csv`

Each block runs **three PubMed passes plus an OpenAlex arm**, all routed through the
existing `build_pubmed_query` chokepoint so the population and LMIC filters are
applied identically to the main pipeline:

| Pass | Content filter | Study-type filter | Purpose |
|---|---|---|---|
| **MA** | intervention [AND setting] | `MA_FILTER` | Clinical backbone |
| **SR** | intervention [AND setting] | `SR_FILTER` | Clinical breadth |
| **IMPL** | intervention [AND setting] **AND `IMPL_OUTCOME_FILTER`** | `IMPL_TYPE_FILTER` | **The novel pass** |
| **OpenAlex** | free-text equivalent, ± impl terms | — | Non-PubMed literature |

**The implementation pass is the methodological core of this review.** Two new filters:

- `IMPL_OUTCOME_FILTER` — coverage, adherence, compliance, uptake, retention,
  default, implementation, scale-up, delivery platform, feasibility, program/process
  evaluation, barriers, facilitators, fidelity, health system, community health
  worker. **Deliberately contains no cost terms** (cost = Phase 2).
- `IMPL_TYPE_FILTER` — widens beyond MA/SR to admit RCTs, evaluation studies,
  observational studies, cluster-randomised, program/process evaluations, mixed
  methods, qualitative, cohort, feasibility, cross-sectional, coverage surveys.
  Implementation evidence does not live in meta-analyses; without this filter it is
  invisible to the pipeline.

**Ranking change** (`code/08_scoring.py`): a new component
`score_implementation_relevance` (0–12, from implementation MeSH + keywords) is added
to the base `score_paper` via `deepdive_score`. This is **additive**, so a paper strong
on both clinical and implementation grounds ranks highest. `score_paper` itself is
untouched — the original pipeline's ranking is unchanged.

**Pre-flight validation:** before the full fetch, `esearch` counts only were pulled
for all 12 passes to catch empty or runaway queries cheaply:

| Block | MA | SR | IMPL |
|---|---|---|---|
| cmam | 27 | 41 | 74 |
| breastfeeding-facility | 57 | 109 | 353 |
| breastfeeding-community | 46 | 84 | 321 |
| mms | 46 | 61 | 85 |

All non-empty, all under the 500 retmax. The large BF implementation counts are
expected — that is where the operational literature concentrates.

---

## Stage 2 — Relevance validation (human-in-the-loop checkpoint)

**This stage is not automated and should not be.** After retrieval, the top-ranked
papers per block were inspected before committing to the expensive downstream stages.
It caught a real defect.

### 2.1 What the check found

- **MMS — clean.** Top hits on-target; adherence/compliance studies surfacing as
  intended.
- **CMAM — good.** Minor topical bleed (a fortification review, an adolescent-pregnancy
  review), which the extraction `on_topic` flag removes later.
- **Breastfeeding — diluted.** The top was dominated by *generic MNCH delivery-platform*
  reviews (IMCI, lay health workers, "community intervention packages", even aflatoxin
  education) rather than breastfeeding-specific evidence. Cause: the broad BF
  intervention clause combined with the implementation-scoring bonus floated generic
  delivery reviews to the top.

### 2.2 The finding: retrieval cannot separate facility from community

A diagnostic re-ranking showed that requiring a breastfeeding term **in the title**
fixed the dilution — but it also revealed that the **facility and community top-lists
were nearly identical even after the fix**. Broad BF reviews (BFHI, IYCF, "scaling up
BF promotion") genuinely cover *both* settings, so they match both retrievals.

**Conclusion:** facility-vs-community is a **per-study delivery-channel judgment**, not
a query-able distinction. The split was therefore moved from *retrieval* to
*extraction*, via a `bf_delivery_setting` field.

**Two changes followed:**
1. Blocks collapsed 4 → 3 (`cmam`, `breastfeeding`, `mms`).
2. A `title_anchor` regex was added to the BF block, gating the **OpenAlex** arm only
   (PubMed papers already passed a precise `[Majr]`/`[ti]` query and are trusted).

**Result:** OpenAlex 600 → 367 kept; the BF top-50 became **100% PubMed** and
genuinely breastfeeding-specific.

### 2.3 Retrieval funnel

| Block | Papers | Implementation-heavy (score ≥6) |
|---|---|---|
| cmam | 500 | 76 |
| breastfeeding | 640 | 94 |
| mms | 531 | 97 |
| **Total** | **1,671** | |

---

## Stage 3 — Corpus assembly

**Run:** `python3 code/30_run_deepdive_pipeline.py corpus`
**Output:** `data/deepdive/deepdive_corpus.json`

Union of the three blocks, deduped by `paper_key` (PMID > OpenAlex ID > DOI). Papers
appearing in more than one block keep a **list** in `deepdive_blocks` and the higher
relevance score — a paper on MMS for breastfeeding women legitimately belongs to both.

**1,671 → 1,636 unique** (35 multi-block).

---

## Stage 4 — Full-text retrieval

**Run:** `python3 code/30_run_deepdive_pipeline.py fulltext`
**Output:** `data/fulltext/{key}.json` (**shared** with the main pipeline)

Reuses `code/19_fulltext_all.py` unchanged apart from a `db_path` parameter, so the
deep-dive corpus can be annotated without touching `papers_database.json`. Two routes:

1. **PMC** — PMID *or DOI* → PMCID via the NCBI ID Converter → `efetch db=pmc` JATS.
2. **Unpaywall PDF fallback** — repository-preferred OA PDF → PyMuPDF.

**Result: 981/1,636 (60%)** — 908 PMC + 73 PDF. Only ~9% was already cached from the
main pipeline, confirming the PICOS-targeted queries surfaced a substantially
different literature.

*Note on the 40% without full text:* Cochrane/Wiley restrict PMC full text and their
OA PDFs are usually closed too. Those papers are extracted from abstract + metadata.

---

## Stage 5 — Extraction cards + token-balanced batching

**Run:** `python3 code/30_run_deepdive_pipeline.py cards`
**Output:** `data/deepdive/extraction_inputs/{key}.json` + `batches.json`

One self-contained **card** per paper (metadata + abstract + a Methods/Results-biased
full-text excerpt capped at 9,000 words), so an extraction agent needs exactly one
`Read` per paper. Cards additionally carry `deepdive_blocks` and `implementation_score`.

Cards are greedily bin-packed into **token-balanced batches** (~70k tokens, max 18
papers) so each agent gets a bounded context. **1,636 cards → 148 batches** (avg 11.1
papers/batch; large full-text papers get small or singleton batches).

---

## Stage 6 — Multi-agent extraction

**Prompt:** `prompts/deepdive_extraction_prompt.md`
**Mechanism:** `Workflow` — one Sonnet agent per batch, ~16 concurrent
**Output:** `data/deepdive/evidence_db/batch_XXXX.json`

Each agent reads the manifest, finds its own batch index, reads the prompt, reads its
cards, and writes one record per card. It returns only a one-line summary — records go
to disk, never back through context.

### The extended schema (what makes this review different)

Beyond the base v4 fields (study design verbatim, effect sizes with CIs, `included_trials`,
`dominant_trial`, `cochrane_id`, `on_topic`), three fields were added:

| Field | Purpose |
|---|---|
| **`bf_delivery_setting`** | `facility` / `community` / `both` / `n/a` — the split moved here from retrieval (§2.2). Judged on the *delivery channel described*, not where the mother lives. |
| **`comparison_type`** | The PICOS "C" — `simplified_vs_standard`, `combined_vs_separate`, `mms_vs_ifa`, `community_vs_facility`, `counselling_plus_food_vs_counselling`, `head_to_head_products`, … |
| **`implementation_findings[]`** | Structured `{dimension, finding, value, source}` where dimension ∈ coverage / adherence / delivery_platform / barriers / scalability / equity. **The core deliverable of the re-scope.** |

Inherited grounding rules are restated in the prompt: study design verbatim from
`publication_type`+`journal`; all-cause vs cause-specific separate; fixed vs random
both, name the dominant trial; effect sizes require CIs; `cochrane_id` passthrough.
**Cost fields are explicitly excluded** — agents are told to ignore ICERs and
cost-per-DALY even where present.

### Operational lessons (these matter for reproducibility)

1. **Idempotency is mandatory.** Each agent first checks whether its output file
   already exists and is a valid non-empty array; if so it skips. This is what makes
   the run resumable across interruptions — and it was needed.
2. **Session limits fragment the run.** Extraction was capped at roughly 26–46 batches
   per window before hitting the usage limit, requiring several resume bursts. Because
   of idempotency, each resume only ran genuinely-missing batches.
3. **Args can arrive as a JSON string.** The first workflow launch returned in 20 ms
   with 0 agents: `args.n_batches` was `undefined` because the args object reached the
   script as a string, so `Array.from({length: undefined})` produced an empty array.
   Fix: `const A = typeof args === 'string' ? JSON.parse(args) : (args || {})`.
   **Lesson: always verify a fan-out actually spawned agents — a 20 ms "success" is a
   failure.**
4. **Batch order ≠ evidence value.** The token-balancer front-loads large full-text
   papers, but not perfectly: after 104 batches, **125 full-text papers were still
   un-extracted**, mixed into later batches alongside abstract-only records. They were
   re-batched into a dedicated priority set (indices 1000+) and run first, which
   completed full-text coverage in one short burst. **Lesson: when a run is
   resource-fragmented, re-prioritise by evidence value, not by batch index.**

---

## Stage 7 — Merge + validation

**Run:** `python3 code/30_run_deepdive_pipeline.py merge`
**Output:** `data/deepdive/evidence_db.json`, `evidence_by_intervention.json`

Validates each record against required fields, normalises stray keys, cross-checks
coverage against the corpus, and writes any still-missing keys to
`evidence_db_missing.json` so a resume can target them.

**Schema-fidelity check** (this is the evidence the re-scope worked):

| Signal | Result |
|---|---|
| Records / on-topic | 984 / **648** |
| Records with ≥1 implementation finding | **630 / 648 (97%)** |
| `bf_delivery_setting` distribution | facility 62 · community 27 · both 65 · n/a 39 |
| Records with country tags | 618 / 648 |

Per-intervention: CMAM 239 (12 MA, 12 SR, 32 RCT, 48 program-evaluations),
Breastfeeding 193 (30 MA, 29 SR, 12 RCT), MMS 203 (33 MA, 16 SR, 30 RCT).

---

## Stage 8 — Per-intervention synthesis

**Prompt:** `prompts/deepdive_synthesis_prompt.md`
**Output:** `data/deepdive/synthesis_sections/{cmam_sam_mam,breastfeeding,anc_mmn}.md`

One section per intervention, written against the evidence DB with full-text cards
available for tracing exact effect sizes. Structure: evidence base → clinical effect
sizes → **implementation evidence (priority axis)** → comparison arms → mechanism →
caveats.

**Ratings — note the substitution:**

- **Evidence strength** — A / B / C (unchanged).
- **Implementation readiness** — High / Moderate / Low / Unclear. **Replaces the
  cost-effectiveness rating**, because cost is deferred. Derived from the
  `implementation_findings` across records.
- **Scalability** — Proven national / Proven subnational / Growing / Requires investment.

To keep the working set tractable, per-intervention **digests** are generated from the
evidence DB (backbone + program-evaluations + qualitative in full, plus the richest
observational records), rather than reading 200+ raw JSON records.

*Practical note:* Stages 6 and 8 are normally multi-agent. During a session-limit
window the synthesis was written in the main loop from the digests instead — same
inputs, same prompt, same grounding rules.

---

## Stage 9 — Verification

**Run:**
```bash
python3 code/17_verify_synthesis.py CARE_review/CARE_DEEPDIVE_REVIEW.md data/deepdive/deepdive_corpus.json data/deepdive/evidence_db.json
```

The verifier lints **every numeric claim** against the corpus + extracted outcomes +
full text, flagging three classes: `NOT_IN_CORPUS` (misattribution or training-data
leak), unsupported numbers, and unsourced numbers.

**Latest result: 130 cited claims · 125 supported · 0 NOT_IN_CORPUS · 9 unsourced.**

`NOT_IN_CORPUS = 0` is the load-bearing result — it means no number was imported from
outside the retrieved evidence. The residual flags are parser artifacts (DOI digits
read as numbers, section headings, fractions like "4–8 contacts", and summary recaps
of figures cited in full earlier).

### Independent fact-check (beyond the verifier)

The automated verifier checks whether a number exists *somewhere* in the corpus. A
separate audit was run to check **attribution** — whether the *specific cited record*
actually contains the claim:

| Check | Result |
|---|---|
| 268 values matched against their own cited record | ✅ all resolve |
| Record counts vs DB (239/193/203 + tier splits) | ✅ exact |
| Source descriptions (journal + study type verbatim, G1) | ✅ exact, incl. 4 Cochrane IDs |
| Interpretive claims traced to record text | ✅ verbatim-supported |

The audit produced two precision improvements: the MMS safety caveat gained the WHO
technical correction's actual figures (corrected RR 1.05 [0.85–1.30] vs original 1.22
[0.95–1.57]) and its actionable iron-dose recommendation; and the twin-publication
caveat now shows its basis (identical estimates across three outcomes).

---

## Stage 10 — Assembly

**Run:** `python3 code/30_run_deepdive_pipeline.py assemble`
**Output:** `CARE_review/CARE_DEEPDIVE_REVIEW.md`

Stitches the three sections in a fixed display order with a header stating record
count, generation date, and the explicit scope caveat that cost is excluded.

---

## The funnel, end to end

| Stage | Count |
|---|---|
| Retrieved (3 blocks, 12 query passes) | 1,671 |
| Unique corpus after dedup | 1,636 |
| With full text (PMC 908 + PDF 73) | 981 (60%) |
| Extraction cards → batches | 1,636 → 156 |
| Batches extracted | 112 |
| Evidence records | 984 |
| **On-topic records (synthesis input)** | **648** |
| Records with implementation findings | 630 (97%) |
| Cited claims in final document | 130 (0 not-in-corpus) |

---

## Reproducing the run

```bash
# Stage 1 — retrieval (all blocks, or one)
python3 code/28_run_deepdive.py
python3 code/28_run_deepdive.py breastfeeding

# Stages 3-5
python3 code/30_run_deepdive_pipeline.py corpus
python3 code/30_run_deepdive_pipeline.py fulltext
python3 code/30_run_deepdive_pipeline.py cards

# Stage 6 — multi-agent extraction (Workflow; one Sonnet agent per batch,
#           reading prompts/deepdive_extraction_prompt.md). Idempotent + resumable.

# Stages 7, 9, 10
python3 code/30_run_deepdive_pipeline.py merge
python3 code/17_verify_synthesis.py CARE_review/CARE_DEEPDIVE_REVIEW.md \
        data/deepdive/deepdive_corpus.json data/deepdive/evidence_db.json
python3 code/30_run_deepdive_pipeline.py assemble
```

**New/changed code:** `code/03_queries.py` (`DEEPDIVE_BLOCKS`, `IMPL_*`),
`code/08_scoring.py` (`score_implementation_relevance`, `deepdive_score`),
`code/27_deepdive.py`, `code/28_run_deepdive.py`, `code/29_deepdive_pipeline.py`,
`code/30_run_deepdive_pipeline.py`; parameterised `code/19_fulltext_all.py`,
`code/21_build_extraction_inputs.py`, `code/22_merge_evidence_db.py`.
**Prompts:** `prompts/deepdive_extraction_prompt.md`, `prompts/deepdive_synthesis_prompt.md`.

---

## Known limitations

1. **652 abstract-only papers not yet extracted.** All 981 full-text papers are done,
   so the evidence-rich core is complete; the remainder would add breadth and
   country-specificity, not depth.
2. **Cost/CEA deliberately absent.** By design — Phase 2, not yet run.
3. **No country shortlist.** The stated end goal ("identify one country to co-design")
   is *not* delivered by this document. The raw material exists (618/648 records carry
   country tags; 14 countries have evidence across all three interventions), but the
   scoring and recommendation step has not been done.
4. **No cross-cutting synthesis.** The three sections stand alone; there is no summary
   table and no comparison across Save the Children's three scaling positions
   (commodity / behaviour / health-system), which the PICOS spec (§6) specified.
5. **English-language records only** — a pipeline-level coverage caveat.
6. **`bf_delivery_setting` is a per-study judgment**, and "both"-tagged reviews pool
   the two channels — so the facility-vs-community contrast is assembled from
   setting-tagged studies, not a head-to-head trial.
7. **Complementary feeding excluded**, though CARE TE#1 and TE#2 both advocated
   pairing counselling with food/nutrient support. A scoping decision, not an evidence
   finding.

---

## Design decisions worth carrying forward

- **Separate the implementation search from the clinical search.** A single query
  cannot serve both; the third pass with its own outcome *and* study-type filter is
  what surfaced coverage surveys, program evaluations, and CHW-delivery studies that
  an efficacy-only pipeline ranks near the bottom.
- **Make implementation relevance additive to the base score**, not a replacement —
  papers strong on both axes should win.
- **Some distinctions cannot be retrieved, only extracted.** The facility-vs-community
  split is the worked example; the diagnostic (near-identical top-lists across two
  supposedly distinct queries) generalises.
- **Validate retrieval relevance before spending on full text and extraction.** The
  BF dilution would have propagated silently through every downstream stage.
- **Design agent tasks to be idempotent and file-writing.** It is what made a
  multi-day, session-limited, 112-batch extraction recoverable.
- **Phase-separate cost from evidence.** It keeps the evidence pass honest (no
  cost-effectiveness framing leaking into clinical judgments) and matches how partners
  actually sequence decisions.
