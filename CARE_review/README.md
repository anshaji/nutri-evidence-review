# CARE / ScaleWorks Deep-Dive

Everything for the CARE workstream lives in this folder — deliverables, method
documentation, the prompts that define the method, and the working dataset.

**What it is:** a PICOS-structured, implementation-weighted evidence review of three
partner-selected interventions — **CMAM**, **Breastfeeding support** (facility +
community), and **Antenatal MMS** — for CARE and IA partners (Save the Children,
Mercy Corps).

**Scope:** evidence only. Cost/cost-effectiveness is deferred to the pipeline's
Phase 2 and is deliberately excluded here.

---

> **Picking this up after a break?** Read **[claude.md](claude.md)** first — it
> carries the working context: why decisions were made, current state, open gaps
> against CARE's original ask, and the traps.

## 📄 Deliverables — start here

| File | What it is |
|---|---|
| **CARE_DEEPDIVE_REPORT.docx** | **The deliverable.** ~29pp partner-facing report. Generated — do not hand-edit. |
| **[CARE_DEEPDIVE_REPORT.md](CARE_DEEPDIVE_REPORT.md)** | Same report in markdown (assembled from `report/`). Verified: **240 cited claims, 0 not-in-corpus**. |
| **[report/](report/)** | **Edit here.** The nine source sections — exec summary, method, cross-cutting synthesis, country shortlist, three intervention chapters, limitations, appendices. |
| [CARE_DEEPDIVE_REVIEW.md](CARE_DEEPDIVE_REVIEW.md) | *Superseded* predecessor, kept as a record. Its three sections became chapters 5–7. |
| **[workplan_care_deep_dive.docx](workplan_care_deep_dive.docx)** | Partner-facing workplan (objectives, PICOS scope, timeline, deliverables). |

**Markdown is the source of truth; the .docx is generated from it.** Edit
`report/*.md`, then:

```bash
bash CARE_review/code/render_report.sh   # assemble → .docx → verify every number
```

### What the report answers

| CARE's question | Where |
|---|---|
| Does it work? | §5–7, one chapter per intervention |
| Can we scale it, through what? | §3.3 (three scaling positions), §5.4, §6.3–6.4, §7.5–7.6 |
| What blocks it? | §5.6, §6.6, §7.7 |
| **Where?** | **§4 — scored shortlist of 18 eligible countries.** No lead named by design; §4.6 sets out what would settle it. |
| Cost | Out of scope — Phase 2 (§2.1, §8.1) |

## 📚 Method documentation — `docs/`

| File | What it covers |
|---|---|
| **[docs/PICOS_specification.md](docs/PICOS_specification.md)** | PICOS per intervention, the dual clinical + implementation outcome axis, and the four scoping decisions on record. |
| **[docs/PROCESS_deepdive.md](docs/PROCESS_deepdive.md)** | End-to-end method: the stage funnel, operational lessons, and known limitations. Read `../docs/PROCESS_main_pipeline.md` first for the underlying pipeline. |
| **[docs/METHODS_PAPER_PLAN.md](docs/METHODS_PAPER_PLAN.md)** | Plan for writing this up as a methods paper — the argument, what's novel, the traditional-vs-this comparison, and the validation studies still needed. |

## 🧩 Prompts — `prompts/`

These define the method as much as the code does.

| File | Stage |
|---|---|
| **[prompts/deepdive_extraction_prompt.md](prompts/deepdive_extraction_prompt.md)** | Per-study extraction + the extended record schema (`bf_delivery_setting`, `comparison_type`, `implementation_findings`). |
| **[prompts/deepdive_synthesis_prompt.md](prompts/deepdive_synthesis_prompt.md)** | Per-intervention synthesis, dual-axis ratings, grounding rules. |

## ⚙️ Code — `code/`

The deep-dive layer owns all its own logic; it reuses the core pipeline
(`../code/`) as infrastructure rather than duplicating it.

| File | Role |
|---|---|
| **[code/queries.py](code/queries.py)** | The 3 intervention blocks + the implementation-pass filters (`IMPL_OUTCOME_FILTER`, `IMPL_TYPE_FILTER`). No cost terms. |
| **[code/scoring.py](code/scoring.py)** | `score_implementation_relevance` (0–12) and `deepdive_score` — additive over the core scorer, which is left untouched. |
| **[code/retrieval.py](code/retrieval.py)** | Stage 1 orchestrator — MA + SR + IMPL passes per block, dedup, enrich, rank. |
| **[code/pipeline.py](code/pipeline.py)** | Stages 3–10 — corpus assembly, full text, cards, merge, assemble. |
| **[code/country_analysis.py](code/country_analysis.py)** | Country normalisation + scoring behind §4 and Appendix C. Documents the two artifacts it controls for: CHW-cadre-name bias and multi-country cross-tagging. |
| **[code/build_reference_docx.py](code/build_reference_docx.py)** | Builds the styled pandoc template (Cambria/Calibri — both ship with Office, so no embedding). |
| **[code/render_report.sh](code/render_report.sh)** | Assemble sections → `.docx` → run the verifier. One command. |
| **[code/run_retrieval.py](code/run_retrieval.py)** · **[code/run_pipeline.py](code/run_pipeline.py)** | Entry points. |

*Reused from the core pipeline:* `pubmed_client`, `openalex_client`, `dedup`,
`citation_enrichment`, `fulltext_all`, `build_extraction_inputs`,
`merge_evidence_db`, and the verifier (`17_verify_synthesis.py`).

## 💾 Working dataset — `data/` *(~66 MB, gitignored)*

Generated by the pipeline. **Not in git** — regenerable, but expensive to rebuild
(a full re-retrieval plus 112 extraction batches).

| Path | Contents |
|---|---|
| `data/cmam.json` · `breastfeeding.json` · `mms.json` | Per-block ranked retrieval sets (1,671 papers) |
| `data/deepdive_combined.csv` | **Browsable spreadsheet** of all retrieval — open this to eyeball the corpus |
| `data/deepdive_corpus.json` | 1,636 deduped papers, full-text annotated |
| `data/extraction_inputs/` | 1,637 per-paper extraction cards + batch manifest |
| `data/evidence_db/` | 112 raw per-batch extraction outputs |
| **`data/evidence_db.json`** | **The structured evidence database** — 984 records, the most valuable artifact here |
| `data/evidence_by_intervention.json` | Rollup by intervention |
| `data/digests/` | Per-intervention working digests used to write the synthesis |
| `data/synthesis_sections/` | The three section sources that assemble into the review |

**Shared, not here:** full text lives in `../data/fulltext/` (2,196 files, 221 MB)
because it is shared with the main pipeline, and the API cache in
`../data/raw_responses/`.

---

## Running it

All commands run from the repo root. Paths are configured by `DEEPDIVE_DIR` in
`code/01_config.py`, which points at `CARE_review/data`.

```bash
python3 CARE_review/code/run_retrieval.py                        # retrieval (all blocks)
python3 CARE_review/code/run_pipeline.py corpus        # merge blocks → corpus
python3 CARE_review/code/run_pipeline.py fulltext      # full text (shared cache)
python3 CARE_review/code/run_pipeline.py cards         # extraction cards + batches
#   → run the extraction workflow (one agent per batch, idempotent/resumable)
python3 CARE_review/code/run_pipeline.py merge         # → evidence_db.json
#   → write synthesis sections per CARE_review/prompts/deepdive_synthesis_prompt.md
python3 CARE_review/code/run_pipeline.py assemble      # → CARE_DEEPDIVE_REVIEW.md

# Verify every number against the corpus
python3 code/17_verify_synthesis.py CARE_review/CARE_DEEPDIVE_REVIEW.md \
        CARE_review/data/deepdive_corpus.json CARE_review/data/evidence_db.json
```

## Status

- ✅ All 981 full-text papers extracted; 648 on-topic records; verifier clean
  (240 cited claims, 0 not-in-corpus).
- ✅ **Country shortlist** — 18 eligible countries scored; Ethiopia and India lead.
  No single country named, by decision; §4.6 lists what would settle it.
- ✅ **Cross-cutting synthesis** — summary table plus the three-scaling-positions
  comparison specified in PICOS §6.
- ✅ **Partner-facing `.docx`** rendered and reproducible.
- ⬜ **652 abstract-only papers** not yet extracted (breadth, not depth).
- ⬜ **Cost / Phase 2** — deferred by design.
- ⬜ **Liz's senior review**, then send to CARE (target 2026-08-08).

See `../task.md` for live task state.
