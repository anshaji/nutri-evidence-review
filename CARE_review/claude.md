# CARE Deep-Dive — Working Context

Session memory for this workstream: why things are the way they are, what state
we're in, and where the traps are. Complements — does not duplicate —
`README.md` (the index), `docs/PROCESS_deepdive.md` (the method), and
`../claude.md` (core pipeline architecture).

**Last updated:** 2026-08-04 · **Team:** Akash (lead), Liz (senior review)
**Target delivery:** 2026-08-08

---

## Why this workstream exists

CARE and IA partners (Save the Children, Mercy Corps) reviewed our initial
15-intervention synthesis and narrowed to **three interventions** for a deeper,
PICOS-structured review: **CMAM**, **Breastfeeding support**, **Antenatal MMS**.

**The end goal is not the review.** It is: *identify one country to co-design a
national-level intervention leveraging existing government infrastructure.*
Keep that in view — the review is an input to a country decision, and the country
decision is still outstanding (see Open Gaps).

### The partner steer that reshaped everything

> **Save the Children:** "Adherence/coverage — not efficacy — is the binding
> constraint… we've known these are the High Impact Nutrition Interventions yet
> we still aren't achieving the WHA Targets because gov'ts/NGOs/donors haven't
> cracked this nut of (sustainable) operationalization."

They also chose these three deliberately to test the ScaleWorks model from
**three different scaling positions**: commodity-based (MMS), behavioural/SBCC
(breastfeeding), health-system treatment (CMAM). That framing is in the PICOS
spec (§6) but **has not yet made it into the review** — see Open Gaps.

> **CARE (TE#2):** breastfeeding must be split — "strong facility-based support
> around delivery" vs "targeted counselling… through CHWs with repeated contacts."

Raw partner feedback: `~/Downloads/IA member nutrition TE feedback on interventions.docx`

---

## Decisions on record (and the reasoning)

| Decision | Why |
|---|---|
| **Evidence first, cost later** | User instruction. Cost/CEA is deferred to the pipeline's existing Phase 2. Cost terms are excluded from queries, extraction *and* synthesis. The usual cost-effectiveness rating is replaced by **Implementation readiness**. |
| **Implementation is a first-class axis** | Direct response to the Save the Children steer. Drove a third retrieval pass, a new scoring component, and three new extraction fields. |
| **Breastfeeding: 4 blocks → 3** | **This was a finding, not a convenience.** Facility-vs-community top-lists came back near-identical even after fixing dilution, because broad BF reviews genuinely cover both. The distinction is a per-study *delivery-channel judgment*, so it moved from retrieval to extraction (`bf_delivery_setting`). |
| **Title-anchor on the OpenAlex arm (BF only)** | BF retrieval was diluted by generic MNCH reviews (IMCI, lay health workers, even aflatoxin education). PubMed papers already passed a precise `[Majr]`/`[ti]` query so they're trusted; only OpenAlex is gated. Took BF top-50 to 100% PubMed. |
| **Country-agnostic retrieval** | PICOS §7 decision 4 — layering country-fit at synthesis avoids biasing the evidence base toward pre-selected countries. |
| **Full-corpus scope** | User chose this over a top-N cap. |
| **Development-primary; cash+SBCC-for-BF in; general CF out; SQ-LNS light reference** | PICOS §7 decisions 1–3, taken on recommended defaults, still pending Liz/CARE review. |

---

## Where we are (2026-08-04)

**Extraction: 112/156 batches — all 981 full-text papers done, 652 abstract-only remaining.**
The full-text core is complete; what's left adds breadth, not depth.

| | Records |
|---|---|
| Total / on-topic | 984 / **648** |
| CMAM · Breastfeeding · MMS | 239 · 193 · 203 |
| With implementation findings | 630 (97%) |

**Deliverable:** `CARE_DEEPDIVE_REVIEW.md` — verified **130 cited claims, 0 not-in-corpus**.
Ratings: MMS **A**, CMAM **B**, Breastfeeding **A** — all Tier 1.

**Fact-checked (2026-08-04):** 268 numeric values audited against *their specific
cited record* (not just corpus presence); record counts and source descriptions
exact; interpretive claims traced to record text. Two precision fixes applied.

---

## Open gaps — what CARE asked for that we have NOT delivered

1. **Country shortlist / recommendation.** The stated end goal. Raw material
   exists: 618/648 records carry country tags, and 14 countries have evidence
   across all three interventions (Ethiopia 144, India 117, Bangladesh 106 lead).
   Ethiopia stands out on the corpus's own evidence — the only country running
   CHW-managed SAM nationally. **Not scored, not recommended.**
2. **Cross-cutting synthesis.** No summary table, and no comparison across Save
   the Children's three scaling positions (specified in PICOS §6).
3. **652 abstract-only papers** un-extracted.
4. **Cost / Phase 2** — deferred by design, not a gap.
5. **Complementary feeding** — both CARE TEs advocated pairing counselling with
   food/nutrient support; scoped out to keep to three interventions.

---

## Traps and gotchas

**Session limits fragment extraction.** Roughly 26–46 batches per window before
hitting the usage cap. This is why every agent prompt is **idempotent** (checks
for its own output file and skips) — it's what makes resume work. Don't remove that.

**Workflow args can arrive as a JSON string.** The first extraction launch
returned in 20 ms with 0 agents: `Array.from({length: undefined})`. Always
`const A = typeof args === 'string' ? JSON.parse(args) : (args || {})`.
**A suspiciously fast "success" is a failure — verify agents actually spawned.**

**Batch order ≠ evidence value.** The token-balancer front-loads big papers but
imperfectly; 125 full-text papers were still unextracted at batch 104. When a run
is resource-fragmented, re-prioritise by evidence value and re-batch.

**The MMS safety caveat was wrong once — don't reintroduce it.** An early draft
treated "MMS raises neonatal mortality where births are at home" as near-
disqualifying. Full-text extraction surfaced the **WHO technical correction** that
overturned it (corrected RR 1.05 [0.85–1.30] vs original 1.22 [0.95–1.57]), and
attributed the residual signal to **iron dose**. It is a country-selection
*consideration*, not a filter.

**Twin publications.** PMID 37131422 (*Campbell*) and 31906272 (*Nutrients*), both
2020, are one 42-study/35,017-child evidence base. The antibiotic mortality
RR 0.74 is **one** finding, not two.

**Verifier flags are mostly benign.** DOI digits parse as numbers, section
headings, fractions like "4–8 contacts". The load-bearing number is
**`NOT_IN_CORPUS = 0`**. Don't chase the rest.

---

## Where things live (post-reorg, 2026-08-03/04)

Everything CARE is in this folder. Paths changed — old references are stale.

```
CARE_review/
  CARE_DEEPDIVE_REVIEW.md   the deliverable
  code/                     queries, scoring, retrieval, pipeline + entry points
  docs/                     PICOS spec, process doc, methods-paper plan
  prompts/                  extraction + synthesis prompts
  data/                     working dataset (~66M, GITIGNORED)
```

- `DEEPDIVE_DIR` in `../code/01_config.py` → `./CARE_review/data`. Single source
  of truth for every deep-dive path.
- The deep-dive **owns its queries and scoring**; core files carry no deep-dive
  logic. It reuses core infrastructure (`pubmed_client`, `dedup`, `fulltext_all`,
  `build_extraction_inputs`, `merge_evidence_db`, the verifier).
- Imports are **absolute** (`from code.…`) so the repo root must be on `sys.path`;
  entry points and `code/__init__.py` handle it.
- **`data/fulltext/` deliberately stays in `../data/`** — shared with the main
  pipeline; moving it would break caching for both.

### Run it (from repo root)

```bash
python3 CARE_review/code/run_retrieval.py            # retrieval
python3 CARE_review/code/run_pipeline.py corpus      # → fulltext → cards → merge → assemble
python3 code/17_verify_synthesis.py CARE_review/CARE_DEEPDIVE_REVIEW.md \
        CARE_review/data/deepdive_corpus.json CARE_review/data/evidence_db.json
```

---

## ⚠️ The dataset is local-only

`CARE_review/data/` (~66 MB) is gitignored — correct for generated data, but it
means **no backup**. `evidence_db.json` in particular represents many hours of
agent extraction across multiple session windows. If it's lost, rebuilding means a
full re-retrieval plus 112 extraction batches. Consider archiving it or committing
just that 4.5 MB file.

---

## Repo state

Work is on branch **`repo-cleanup`** (8 commits ahead of `main`), not yet merged:

```bash
git checkout main && git merge repo-cleanup
```

The cleanup also moved the separate **TRACE** project out to
`~/Documents/GitHub/trace` (44 MB, 3,517 files) — it needs `git init` if you want
it versioned.

---

## Next moves

1. **Country-fit analysis** → the 3–5 shortlist and a recommendation. Closes the
   biggest gap against the original ask; data is ready.
2. **Cross-cutting synthesis** — summary table + three-scaling-positions comparison.
3. Render the review to `.docx` for Liz/CARE.
4. Optionally finish the 652 abstract-only papers.
5. **Methods paper** — plan in `docs/METHODS_PAPER_PLAN.md`. The cheapest
   high-value next experiment is the adversarial verifier test (plant fabricated
   numbers, measure detection rate); the gold-standard benchmark against published
   Cochrane/Campbell reviews is the non-negotiable one before submission.
