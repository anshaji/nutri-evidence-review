# Nutrition Evidence Review Pipeline

## Overview

Evidence-synthesis pipeline that identifies nutrition interventions for **children under 5** and **women of reproductive age (WRA)** in LMICs with the strongest evidence, cost-effectiveness, and government-scaling pathways.

A **two-phase core** with a manual review checkpoint, plus a **full-corpus extension** (see below) that scales the review from the top 200 to the whole corpus:

- **Phase 1 (Evidence):** PubMed + OpenAlex, population-targeted, *no* cost-effectiveness. Dedup, score, rank, retrieve full text.
- **Phase 2 (Cost-effectiveness):** per shortlisted intervention, a targeted CEA search (PubMed + OpenAlex + optional local registry).
- **Synthesis:** combine both datasets under a grounding checklist; a verifier lints every number.

The two-phase split is the structural fix for the VAS audit's CEA blind spot: cost-effectiveness is only searched for interventions that survive the evidence screen.

**Repo:** https://github.com/anshaji/nutri-evidence-review · **Local:** /Users/akashshaji/Documents/GitHub/nutri-evidence-review/

## Architecture

Python 3.13. Phase 1/2 core is standard-library only; the full-corpus extension adds **PyMuPDF** (`fitz`). pip works on this machine (the old "pip is broken" note was stale). `code/__init__.py` aliases numbered modules so `code/01_config.py` imports as `code.config`.

```
code/
  01_config 02_models 03_queries 04_pubmed_client 05_openalex_client
  06_dedup 07_citation_enrichment 08_scoring 09_fulltext_client
  10_main / 11_fetch_papers                     # Phase 1 orchestrator + entry point
  12_cea_client 13_ghcea_registry 14_cea_main / 15_run_cea   # Phase 2
  16_verify / 17_verify_synthesis               # claim verifier (lint)
  18_notes.R
  19_fulltext_all / 20_fetch_fulltext_all       # full-corpus full text (PMC + Unpaywall)
  21_build_extraction_inputs 22_merge_evidence_db           # per-study evidence DB
  23_build_synthesis_inputs 24_cap_sample                   # synthesis prep + scope cap
  25_assemble_synthesis 26_extract_ratings                  # assemble tiered doc
prompts/  shortlist_prompt.md  synthesis_prompt.md  extraction_prompt.md
data/     README.md (optional CEA registry CSV)
```

`from __future__ import annotations` must be the first import in any module using `int | None` in a TypedDict (models, pubmed_client, openalex_client).

## Phase 1 — Evidence (`python3 code/11_fetch_papers.py`)

1. **Retrieval (no CEA).** Track A (PubMed): 12 intervention domains × 2 passes (meta-analysis tier, systematic-review tier). Track C (OpenAlex): nutrition-sensitive literature (cash transfers, social protection, food subsidies). Every query ANDs in a `POPULATION_FILTER` (under-5 OR WRA, MeSH + tiab); `build_pubmed_query` / `build_openalex_search` are the single chokepoints.
2. **Dedup.** PMID → **Cochrane-version collapse** (records sharing a `cochrane_id` keep the newest; older tagged `superseded_by` — a version update is not new evidence) → OpenAlex ID → cross-source DOI (prefer PubMed record, merge OpenAlex citations).
3. **Score** (8 components, max ≈ 95): study design 20, topic 25, setting 10, recency 10, citations 12, open-access 3, meta-analysis-tier bonus 5, **population relevance 10**.
4. **Full text (Stage 3.5).** PMID → PMCID (NCBI ID Converter) → `efetch db=pmc` JATS XML → sections + tables, cached in `data/raw_responses/pmc/`. (Superseded by the full-corpus extension, which runs full text over *all* papers, not just the top 200.)
5. **Manual review → shortlist.** Reviewed in-conversation per `prompts/shortlist_prompt.md`; author `data/shortlist.json` (from `.template.json`).

## Phase 2 — Cost-effectiveness (`python3 code/15_run_cea.py [data/shortlist.json]`)

Per shortlisted intervention: PubMed `CEA_TERM_SKELETON AND (name/synonyms[tiab] OR mesh) AND LMIC`, an OpenAlex cost-terms search, and an optional local CEA-registry match. Writes `data/cea_by_intervention.json` with `cea_papers`, `registry_matches`, and **`cea_rating_allowed`** — false when no CEA record exists, which forces the synthesis to record cost-effectiveness as `Unknown` rather than invent one.

*CEA registry:* an **optional local CSV** (`data/ghcea_registry.csv`), not a live API — neither the Tufts/CEVR GHCEA registry (a JS app) nor DCP3 (a PDF) is reachable from stdlib `urllib`. Absent it, Phase 2 runs on the PubMed/OpenAlex backbone with zero registry matches. See `data/README.md`.

## Synthesis + verification

Combine the evidence and CEA corpora per `prompts/synthesis_prompt.md` grounding rules: study type **verbatim** from `journal`+`publication_type`; a **corpus citation on every number**; all-cause vs cause-specific kept separate; report fixed/random + name the dominant trial; version ≠ evidence; CEA-rating guard. Then `python3 code/17_verify_synthesis.py <synthesis.md>` lints every numeric claim — flags `NOT_IN_CORPUS` (misattribution/leak) and unsupported numbers.

## Full-Corpus Extension (v4 — 1,000-paper working set)

Scales the review beyond the top 200 to a large, **ranking-independent** working set, adds a per-study **evidence database** (the deferred evidence-graph seed), and runs extraction + synthesis as **multi-agent workflows** (a deliberate deviation from "in-conversation, no automation" — ~2,000 papers can't fit one context).

- **Full text for the whole corpus** (`19`/`20`): resolves each paper's PMID *or DOI* → PMCID via the NCBI ID Converter (it accepts DOIs, reaching OpenAlex papers too), reuses the PMC efetch+JATS path, and falls back to **Unpaywall → OA-PDF (repository-preferred) → PyMuPDF**. Written per-paper to `data/fulltext/{key}.json`; the master DB is annotated with flags only. Latest: **1,378/1,996 (69%)** full text (1,206 PMC + 172 PDF).
- **Per-study extraction** (`21`/`22`): one card per paper → fan-out of Sonnet agents (one per token-balanced batch, each writes its own batch file) → validated records merged to `data/evidence_db.json` + `evidence_by_intervention.json`. Each record carries study design verbatim, population, effect sizes with CIs, **`included_trials`**, **`dominant_trial`**, `cochrane_id`, `on_topic` (schema: `prompts/extraction_prompt.md`).
- **Scope cap** (`24`): `code/24_cap_sample.py 1000` caps to a 1,000-paper set chosen **independently of the relevance ranking** (reuse already-extracted + uniform-random top-up, fixed seed).
- **Synthesis** (`23`,`25`,`26`): per-intervention bundles (records + matched CEA + `cea_rating_allowed`, plus the **re-shortlist delta** of interventions the top-200 missed) → one strong-model agent per intervention (writes `data/synthesis_sections/{cat}.md`) → assemble the tiered `output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md`.
- **Verifier upgraded** (`16`): recognises PMID **and** DOI/paper-key citations and checks numbers against full text + extracted outcomes (not just abstracts), since full text no longer lives in the DB.

Latest run: 23 interventions tiered; verifier = 639 cited claims, **0 not-in-corpus**. The extension produced the DEVTA-class insight automatically (vitamin A: DEVTA named at 65.2% of pooled weight, fixed RR 0.88 vs random 0.76) — the exact gap the VAS audit flagged.

## Running

```bash
# Phase 1/2 (original flow)
python3 code/11_fetch_papers.py                             # Phase 1 (~3-4 min)
cp data/shortlist.template.json data/shortlist.json         # review top papers, then edit
python3 code/15_run_cea.py                                  # Phase 2
python3 code/17_verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md

# Full-corpus extension
python3 code/20_fetch_fulltext_all.py        # full text for all papers (resumable, cached)
python3 code/21_build_extraction_inputs.py   # cards + batches → run extraction workflow (1 agent/batch)
python3 code/22_merge_evidence_db.py         # → data/evidence_db.json
python3 code/24_cap_sample.py 1000           # optional: cap scope, not rank-bounded
python3 code/23_build_synthesis_inputs.py    # bundles → run synthesis workflow (1 agent/intervention)
python3 code/26_extract_ratings.py && python3 code/25_assemble_synthesis.py
python3 code/17_verify_synthesis.py output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md
```

Config: `NCBI_API_KEY` in a gitignored `.env`, auto-loaded by `code/01_config.py` (10 req/s with key vs 3 without). All `data/` outputs are gitignored (regenerated/authored). Caching (`data/raw_responses/`, `data/fulltext/`, `data/evidence_db/batch_*.json`) makes every stage resumable.

## Why the design is this way — VAS audit

A manual audit of an early single-phase VAS synthesis surfaced the failures below; each is now addressed structurally.

| Failure in the old pipeline | Fix |
|---|---|
| **CEA blind spot** — VAS rated "Very High" with zero corpus CEAs (PubMed isn't where CEAs live) | Two-phase split + `cea_rating_allowed` guard → `Unknown` without a CEA record |
| **Version ≠ evidence** — 2017 & 2022 Cochrane (both CD008524) counted as independent generations | Cochrane-ID dedup collapses shared accessions, keeps newest |
| **External-knowledge leak** — "823,000 deaths" (actually Lancet *Breastfeeding*, PMID 26869575) imported from training data | Grounding prompt (corpus citation per number) + verifier flags `NOT_IN_CORPUS` |
| **Study-type misclassification** — a *BMC Public Health* meta-analysis labelled "Cochrane" | Grounding rule: study type verbatim from `journal`+`publication_type` |
| **No dominant-trial / overlap detection** — DEVTA held the pooled estimate but was never named | Extraction captures `included_trials`+`dominant_trial` (delivered the DEVTA insight; cross-review overlap still TODO) |
| **No population targeting** — only LMIC geography was filtered | Population filter in every query + scoring component 8 |

## Known gotchas

- **NCBI ID Converter returns PMIDs as int** — `str()` them to match paper-dict keys.
- **Cochrane/Wiley restrict PMC full text** — some PMC-indexed reviews have no `<body>` and stay abstract-only (the Unpaywall PDF fallback rarely helps — those PDFs are closed too).
- **`from __future__ import annotations`** must be the first import in any module using `int | None` in a TypedDict.

## Current task — CARE/ScaleWorks deep-dive review (July 2026)

CARE and IA partners (Save the Children, Mercy Corps) reviewed the initial 15-intervention synthesis and converged on **3 interventions** for a targeted PICOS-style evidence review:

1. **Community-based Management of Acute Malnutrition (CMAM/RUTF)** — health-system treatment package; innovation around simplified/community protocols, cost efficiency, coverage expansion
2. **Breastfeeding Promotion & Support** — disaggregated into (a) facility-based support around delivery (BFHI, early initiation, skin-to-skin) and (b) community/CHW postnatal counselling (peer support, repeated contacts)
3. **Antenatal Multiple Micronutrient Supplementation (MMS)** — commodity-based; logistics, financing, adherence, IFA→MMS transition

**End goal:** identify one country to co-design a national-level intervention leveraging existing government infrastructure. The review must answer not just "does it work?" but "can we scale it, where, through what, and what are the barriers?"

**Key framing from partners:**
- Save the Children: "Adherence/coverage — not efficacy — is the binding constraint." These are known high-impact interventions; the question is sustainable operationalization.
- CARE: disaggregate breastfeeding into facility-based vs community-based packages; pair complementary feeding counselling with food/nutrient support; CMAM innovation around simplified approaches.
- Mercy Corps: high experience in BF/CF, moderate in CMAM, limited in MMS/SQ-LNS but keen to explore.

**Approach:** fine-tune the pipeline model for PICOS-structured review per intervention. Outcomes include clinical endpoints AND implementation/scaling outcomes (coverage, adherence, cost-per-beneficiary, delivery platform feasibility, institutional barriers). Comparison arms include simplified vs standard protocols (especially CMAM).

**Timeline:** see `task.md` for detailed tracking. ~4 weeks: background study + PICOS design (wk 1-2) → model runs (wk 2-3) → review with Liz + share with CARE (wk 4).

**Deep-dive pipeline (evidence-only; cost = Phase 2, deferred):** PICOS spec in
`CARE_review/docs/PICOS_specification.md`. Retrieval is a separate layer over the
main pipeline — `DEEPDIVE_BLOCKS` in `code/03_queries.py` (3 blocks: `cmam`,
`breastfeeding`, `mms`), each run through MA + SR + **implementation** passes
(`IMPL_OUTCOME_FILTER` coverage/adherence/delivery/barriers — *no cost terms* —
× `IMPL_TYPE_FILTER` program-evaluation/trial/cohort designs). Ranking adds
`score_implementation_relevance` (0–12) via `deepdive_score` (leaves
`score_paper` untouched). Orchestrator `CARE_review/code/retrieval.py`, entry
`CARE_review/code/run_retrieval.py [block ...]`. Output: ranked `CARE_review/data/{block}.json`
+ `deepdive_combined.csv`. **Breastfeeding is one title-anchored retrieval**
(`[Majr]`/`[ti]`, OpenAlex title-gated) — facility vs community is tagged per
study at **extraction**, not retrieval (broad BF reviews cover both). Latest run
(2026-07-22): cmam 500, breastfeeding 640, mms 531 = 1,671 papers; validated
(MMS/CMAM on-topic, BF de-diluted, top-50 all PubMed).

**Partner feedback:** raw feedback from Mercy Corps, Save the Children, and CARE technical experts in `/Users/akashshaji/Downloads/IA member nutrition TE feedback on interventions.docx`.

**Status (2026-08-07):** the CARE deliverable is now
`CARE_review/final-report/CARE_FINAL_REPORT.docx` — a combined report drawing on
the pipeline deep-dive plus a **methodologically independent hand-verified
review** (`CARE_review/INDEPENDENT_EVIDENCE_REVIEW.md`) built to check it and to
cover what the pipeline could not reach: cost, WHO guidelines, and UN burden
datasets. The two are compared in `CARE_review/REVIEW_COMPARISON.md`. Full
detail, including the 16 corrections the fact-check produced, is in
`CARE_review/CLAUDE.md`.

**Paper angle:** the pipeline + this deep-dive may constitute a methods paper on LLM-assisted rapid evidence review (automated retrieval + grounded synthesis + verification). Working paper target: CEGA or SSRN → *Research Synthesis Methods* or *Systematic Reviews*.

## Open work

- **Population-fidelity check in the verifier — highest-value upgrade.** An
  independent fact-check of the CARE deep-dive (2026-08-07) found 16 corrections,
  and **every one passed the verifier**. Traceability is not fidelity: a number can
  trace to a real corpus record and still carry the wrong population, comparator,
  certainty rating or vintage. The worst case described a **preterm/low-birth-weight**
  effect (KMC, RR 0.68) as applying to all newborns — a ~7× overstatement of the
  eligible population. A check comparing the population attached to an effect
  estimate in synthesis against the population field in the extraction record would
  have caught that, plus two others in the same set. This is also the strongest
  material the methods paper has for "what automated synthesis gets wrong".
- **Cross-review trial matching + forest-plot weight overlap** to auto-detect double-counting — the remaining big piece of the evidence graph (extraction now captures the per-review trial lists it needs). *The same fact-check found the pipeline had double-counted one Bhutta-group MMS analysis published twice as independent corroboration — the exact failure this would catch.*
- Standardized LMIC country list; OpenAlex vs PubMed/Web-of-Science coverage validation.
- Structured/automated Stage-4 review prompts.
