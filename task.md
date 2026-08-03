# Task Tracker — CARE/ScaleWorks Deep-Dive Review

**Project:** Targeted PICOS evidence review of 3 nutrition interventions for CARE/IA partners
**Start:** 2026-07-10
**Target delivery:** 2026-08-08 (4 weeks)
**Team:** Akash (lead), Liz (review, back week 4)

---

## Week 1-2: Background study + PICOS design (Jul 10 – Jul 24)

### Background study
- [ ] CMAM: review canonical studies, current WHO protocols, simplified-approach evidence, country case studies
- [ ] Breastfeeding (facility-based): BFHI evidence, early initiation / skin-to-skin, health worker training models
- [ ] Breastfeeding (community-based): CHW/peer counsellor models, mother-to-mother support, repeated-contact protocols
- [ ] MMS: IFA-to-MMS transition evidence, WHO conditional recommendation, country rollout experience (Bangladesh, Burkina Faso, Tanzania)
- [ ] Country scoping: identify 3-5 candidate countries with existing government nutrition infrastructure, high malnutrition burden, IA partner presence (CARE/SC/MC). Surface for CARE feedback before model runs.
- [ ] Review partner feedback document in detail — extract specific sub-intervention preferences and country signals

### PICOS framework
- [x] Define Population for each intervention (restrict to in-scope but not fully closed)
- [x] Define Intervention packages (especially breastfeeding disaggregation: facility vs community)
- [x] Define Comparisons (simplified vs standard protocols for CMAM; MMS vs IFA; facility vs community for BF)
- [x] Define Outcomes: clinical (mortality, anthropometry, micronutrient status) + implementation (coverage, adherence, cost-per-beneficiary, delivery platform, institutional barriers)
- [x] Define Study types: include implementation science, cost-effectiveness, program evaluations alongside MAs/SRs
- [x] Document PICOS in a shared format for Liz review → `docs/PICOS_specification.md` (v0 draft 2026-07-22)
- [ ] Liz + CARE review of PICOS v0; resolve 4 open decisions (emergency/dev split; cash+ breadth; SQ-LNS shadow arm; country pre-commitment)

### Outputs
- [ ] Background brief per intervention (short, 2-3 pages each)
- [x] PICOS specification document → `docs/PICOS_specification.md` (v0)
- [ ] Country shortlist (3-5 candidates with rationale)
- [x] Workplan shared with CARE and org → `CARE_review/workplan_care_deep_dive.docx`

---

## Week 2-3: Model fine-tuning + runs (Jul 17 – Jul 31)

### Pipeline adaptation
- [x] Update `code/03_queries.py` with PICOS-targeted queries per intervention → `DEEPDIVE_BLOCKS` (4 blocks: CMAM, BF-facility, BF-community, MMS)
- [x] Add implementation science / program evaluation search terms → `IMPL_OUTCOME_FILTER` + `IMPL_TYPE_FILTER` (3rd pass per block; NO cost terms — cost = Phase 2)
- [ ] Add country-specific filters or queries for shortlisted countries (deferred — country-agnostic retrieval per §7 decision 4)
- [x] Adjust scoring to weight implementation/scaling outcomes → `score_implementation_relevance` (0–12) + `deepdive_score` (leaves `score_paper` untouched)
- [x] Test queries on small runs, validate retrieval relevance → esearch counts sane (CMAM 27/41/74, BF-fac 57/109/353, BF-com 46/84/321, MMS 46/61/85)
- [x] Deep-dive orchestrator + entry point → `code/27_deepdive.py`, `code/28_run_deepdive.py`

### Model runs (EVIDENCE ONLY — cost deferred to Phase 2)
- [x] Run deep-dive Phase 1 → `data/deepdive/{block}.json`. **Blocks: cmam, breastfeeding, mms** (BF collapsed from 2→1; facility/community now tagged at extraction, not retrieval — see PICOS §3 note)
- [x] Review per-block retrieval relevance: MMS excellent, CMAM good (minor bleed → on_topic filter), BF diluted by generic MNCH → fixed with title-anchor + [Majr] (BF top-50 now 100% PubMed)
- [x] Retrieval validated & final: cmam 500, breastfeeding 640, mms 531 = 1,671 papers → `data/deepdive/`
- [x] Add `bf_delivery_setting` (facility/community/both) + `comparison_type` + `implementation_findings` to extraction prompt → `prompts/deepdive_extraction_prompt.md`
- [ ] Run Phase 2 (CEA) per intervention → DEFERRED (cost analyzed later)
- [x] Run full-text retrieval (deep-dive corpus) → 981/1,636 (60%); shared `data/fulltext/`
- [x] Run extraction (per-study evidence DB): **ALL 981 full-text papers extracted** (112/148 batches; 984 records, 648 on-topic). Only **652 abstract-only papers** remain (breadth, no full-text depth).
- [x] Run synthesis per intervention → **REFRESHED on full-text-complete base** (648 on-topic: CMAM 239, BF 193, MMS 203). Deepened implementation axis; corrected MMS safety caveat (WHO technical correction overturned the home-birth mortality signal).
- [x] Run verifier → 0 not-in-corpus, 125/130 supported (rest benign: recaps/headers/metadata/adjacency)

### Outputs
- [x] Per-intervention evidence database → `data/deepdive/evidence_db.json` (interim, 260 records)
- [x] Per-intervention synthesis sections → `data/deepdive/synthesis_sections/{cmam_sam_mam,breastfeeding,anc_mmn}.md`
- [x] Assembled deep-dive review document → `CARE_review/CARE_DEEPDIVE_REVIEW.md` (INTERIM)

### OPTIONAL — 652 abstract-only papers remain (all full-text already done)
- These add breadth/country-specificity, not full-text depth. Batches: the original missing set minus the 8 priority (1000–1007) already run.
- To finish: re-run resume workflow (`deepdive-extraction-resume-wf_bc5df201-711.js`) with remaining <1000 indices as `args.missing`; session-limited ~30/burst.
- Then `merge` → regenerate digests → optional final refresh. Full-text-complete deliverable is already in `CARE_review/CARE_DEEPDIVE_REVIEW.md`.

---

## Week 4: Review + delivery (Jul 31 – Aug 8)

### Review
- [ ] Liz reviews first pass of all 3 intervention syntheses
- [ ] Incorporate Liz's feedback — rerun model if necessary
- [ ] Cross-check country recommendations against partner capacity and government infrastructure

### Delivery
- [ ] Final deep-dive review document (formatted)
- [ ] Country recommendation with rationale
- [ ] Share with CARE
- [ ] Internal debrief — capture learnings for the methods paper

---

## Completed outputs

| Date | Output | Location |
|------|--------|----------|
| 2026-06-05 | Initial 15-intervention synthesis (Phase 1+2) | `output/FULL_INTERVENTION_SYNTH.md` |
| 2026-06-09 | Full-corpus 23-intervention synthesis (v4) | `output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md` |
| 2026-07-10 | Workplan for CARE deep-dive | `CARE_review/workplan_care_deep_dive.docx` |
| 2026-07-22 | PICOS specification (3 interventions, dual-axis) | `docs/PICOS_specification.md` |
| 2026-07-23 | **Interim** deep-dive review (CMAM/BF/MMS, 175 on-topic records) | `CARE_review/CARE_DEEPDIVE_REVIEW.md` |

---

## Standing decisions

- **3 interventions confirmed:** CMAM, Breastfeeding (disaggregated), MMS
- **Breastfeeding split into 2 packages:** facility-based (BFHI) + community/CHW postnatal
- **Outcome scope expanded:** clinical + implementation/scaling (coverage, adherence, cost, barriers)
- **End goal:** one country for national-level co-design with CARE
- **Paper angle:** methods paper on LLM-assisted rapid review (CEGA working paper → journal)
