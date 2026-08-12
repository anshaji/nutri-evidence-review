# CARE Deep-Dive — Working Context

Session memory for this workstream: why things are the way they are, what state
we're in, and where the traps are. Complements — does not duplicate —
`README.md` (the index), `docs/PROCESS_deepdive.md` (the method), and
`../claude.md` (core pipeline architecture).

**Last updated:** 2026-08-07 · **Team:** Akash (lead), Liz (senior review)
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
| CMAM · Breastfeeding · MMS | 243 · 193 · 212 |
| With implementation findings | 630 (97%) · **2,470 findings** across 6 dimensions |

**Current deliverable: `CARE_DEEPDIVE_REPORT.md` + `.docx`** — the partner-facing
report, ~40pp. Verified **276 cited claims, 0 not-in-corpus**. Nine chapters: exec
summary, method, cross-cutting synthesis, country shortlist, three intervention
chapters, limitations, appendices. Ratings unchanged: MMS **A**, CMAM **B**,
Breastfeeding **A**, all Tier 1.

**Restructured 2026-08-04 (v2) after reviewer feedback.** The reframe that drove
it: per notes from the call with Johnathan, *the goal is to present the literature
to CARE — the reading they lack capacity to do* — not only to hand them a
decision. Changes:
- Each intervention chapter now opens with **top 2–3 most effective levers**,
  ranked against an explicitly stated criterion (§5.2, §6.2, §7.2). The criterion
  must be stated because effect sizes on different outcomes aren't commensurable.
- New **§3.6 — three packaged program options** (facility newborn / community
  treatment / antenatal commodity), mapped to the three scaling positions, with a
  comparison table. This is the "distil to 2–3 alternatives" ask.
- New **§3.5 + per-chapter combining sections.** Honest finding: 173 records
  mention combination, only **9 test one**. Within-intervention and
  intervention-plus-cash are evidenced; **cross-intervention is untested**, and
  the Mali SQ-LNS case shows integration *reducing* CMAM enrolment. Don't
  manufacture a combination story — the gap is the finding.
- New **per-chapter country subsections** (§5.8, §6.8, §7.9) — intervention-
  specific, cross-referenced to §4, which stays whole. §4's candidacy gate
  requires evidence in *all three* interventions; distributing it would destroy
  the co-design logic, so both exist deliberately.
- New **§1.5 CEO-level outcome** — recommends **coverage** as the governing
  metric, not a clinical effect size, with the quality caveat attached.
- New **§1.8 scope-check table** mapping Johnathan's six questions to where each
  is answered, including two honest "partly" entries.
- **Abbreviations expanded on first use** + **Appendix A glossary** (reviewer had
  to look terms up). Audience is specialists but readership includes generalists.

**v3 — 22 inline comments actioned (`~/Downloads/CARE_DEEPDIVE_REVIEW_LB.pdf`,
marked against the *old* review, so several were already fixed by v2).** Extract
them with PyMuPDF `page.annots()` — they are PDF annotations, invisible in the
rendered page. The substantive ones and how they were answered:
- **"So what if CHWs increase coverage when SAM treatment doesn't seem to have an
  effect?"** A misreading — but the document caused it by running "recovery is
  71% and falling" straight into "coverage is the lever" with nothing bridging.
  §5.5 now opens with the objection answered directly: 71% recovery is not "no
  effect" (Sphere 75% is a *performance benchmark*, not an efficacy threshold);
  but the active-control ceiling means lives-saved-per-child-covered is
  unmeasurable, and quality degraded as Ethiopia scaled. Landing position:
  *coverage is the largest gain, and only holds if quality and post-discharge
  support are resourced with it.*
- **"Is the problem coverage, or that we can't find and recruit patients?"** Good
  question — the corpus separates them. §5.4 now splits **case-finding** from
  **conversion to treatment** (Mali: screening +40pp, treatment coverage 7.6%;
  Burundi: facility screening 98% vs community 8%).
- **"Evidence on programs that do follow-up?"** Yes — 45 CMAM records touch
  post-discharge. Added the multi-country relapse cohort: **22–63% relapse within
  6 months, pooled RR 3.3 (2.8–4.0)** (DOI 10.1016/s2214-109x(24)00415-7).
  Material: a child counted "recovered" often isn't, durably.
- **"Grades assigned to the corpus, not individual studies?"** Legitimate
  ambiguity. §2.5 now states explicitly that our A/B/C is a judgment over an
  intervention's *whole* corpus, one level above the GRADE that source authors
  apply per-outcome.
- **"Tier 1" was used 5× and never defined.** Now defined in §2.5 — and flagged
  as carrying no discriminating information here, since partners selected all
  three from the Tier 1 set.
- **"Non-inferior" read as "3% better".** Now explained at §2.6 and at both points
  of use: non-inferiority means *not worse by more than a pre-set margin*.
- **"Can you explain how?"** on facility/community complementarity — it was
  asserted, not argued. §6.6 now makes it a four-step argument (different
  moments, different outcomes, each insufficient alone, KMC works in both
  channels so the channel isn't the choice) and names the untested handover risk.
- Also: **"pro-poor gradient"** → plain English; **RD** → "absolute difference";
  **RR** → "risk ratio, also called relative risk" (reviewer's term); remaining
  editorialising cut ("unusually deep base…", "the operationalization gap
  ScaleWorks exists to close").

**Cost was asked twice more in the margins** (combined-vs-standard protocol CEA;
MMS vs IFA vs SQ-LNS). Decision: **leave deferred** — §8.1 already names the two
cost-shaped findings that should seed Phase 2. Third signal now; expect it again.

**v4 — judgment layer removed, claims fact-checked, summary added (2026-08-05).**

**No more grades.** A/B/C evidence strength, implementation readiness and Tier 1
are **gone** (§2.5 explains why in the document itself). The letter was doing
three jobs at once — describing a structural feature of the literature, the
synthesis-tier proportion, and implying a verdict — and readers took the third.
Chapters now say plainly what the evidence contains, establishes, and cannot
answer. Where a *source* reports GRADE, we quote it as they stated it.

**No more country scoring.** The 100-point composite and ranking are **gone**.
Reason recorded in §4.1: the two artifacts already noted above (cadre-name bias,
multi-country cross-tagging) each moved countries several places, which showed
the ordering was sensitive to choices with no evidential basis. `country_analysis.py`
still runs and still produces the counts — Appendix D uses them descriptively —
but the `score`/`score_components` fields are no longer used in the document.

**Fact-check of the five headline claims found three problems.** Do not restore
the old phrasings:
- "About one in three treated" → **38.3%**, and it is **2012–13** data
  (DOI 10.1371/journal.pone.0128666). No comparably broad newer estimate found.
- "Fewer than half of pregnant women adhere" → both pooled sources are
  **Ethiopia-only**; our own corpus reports 77–82% in north India. Never state
  globally.
- "Mali 28.7%→57.1%" → true for Kayes, and Bafoulabé 20.4%→61.1%, **but Kita did
  not change (28.4%→28.5%)**. Omitting the third district was cherry-picking.
- "Tanzania 41.7%→80.9%" → **not a before/after.** Two concurrent areas,
  non-randomised pilot.
- "Nepal 23%→91%" → real, but **tracked ANC coverage 49%→94%** over the same
  period, so the volunteer component cannot be credited alone; and 91% is *any*
  consumption (≥180-day compliance stayed 42%).

**MMS mortality was overstated as a null.** "Improves birth outcomes but not
survival" is **wrong** — MMS reduces **stillbirth RR 0.91**, replicated in 4 of 5
syntheses on ~100k pregnancies (one dissents at 0.95 ns). §7.4 now separates:
stillbirth reduced; **perinatal mortality null is well-powered** (RR 1.00,
0.90–1.11) and load-bearing; **maternal (0.71–1.51) and long-term offspring
(−5.25 to 5.15) nulls are uninformative** — absence of evidence, not evidence of
absence. Don't cite those two as showing no effect.

**Two deliverables now**, both rendered and verified by `render_report.sh`:
`CARE_DEEPDIVE_REPORT.docx` (~41pp, 292 claims) and `CARE_DEEPDIVE_SUMMARY.docx`
(~5pp, 24 claims), source in `report/` and `brief/`. The summary initially
verified at **0 cited claims** because it was written without inline citations
while asserting traceability — citations added. **Any new document must go
through the verifier, not just the full report.**

**v5 — slide deck (2026-08-05).** `CARE_DEEPDIVE_DECK.pptx`, 17 slides, generated
from `code/build_deck.js` via `bash CARE_review/code/render_deck.sh`. Tracks the
*summary*, not the full report. Same rule as the .docx: **generated, never
hand-edited** — edit the script. Deep pine / sage / burnt-clay palette, Cambria
headers + Calibri body (both QA-safe and shipped with Office). 14 citations
carried onto the slides.

**Trap: the reviewer edits the .docx, and `render_report.sh` overwrites it.**
It happened — edits were made to `CARE_DEEPDIVE_SUMMARY.docx` at 12:03 after an
11:36 render. Before re-rendering, **extract the .docx and port changes back into
`brief/`or `report/`**:
`python3 -c "import zipfile,re,html; print(html.unescape(re.sub(r'<[^>]+>','',zipfile.ZipFile('X.docx').read('word/document.xml').decode())))"`
Their v1 edits, now merged: subtitle shortened to "Evidence Review"; the
self-referential opener, the "earlier draft scored countries" explanation, the
open-decisions section and the trailing full-report pointer all cut; "no trial
combines" scoped to "no trial **in our corpus**". The pattern is consistent —
**they strip commentary about the report's own process and keep the substance.**
Write that way by default.

**No LibreOffice on this machine**, so `soffice`-based slide rendering and visual
QA are unavailable. Substitute used: schema validation (`scripts/office/validate.py`),
plus a geometry pass over the packed XML estimating text height against box height
to catch overflow and out-of-bounds shapes. It flags mixed-font-size runs as false
positives — it uses the largest size for the whole string.

`CARE_DEEPDIVE_REVIEW.md` is the **superseded** predecessor (130 cited claims),
kept as a record. Its three sections were rewritten into chapters 5–7.

**Fact-checked (2026-08-04):** 268 numeric values audited against *their specific
cited record* (not just corpus presence); record counts and source descriptions
exact; interpretive claims traced to record text. Two precision fixes applied.

---

**v6 — independent review, fact-check, and the combined CARE report (2026-08-07).**

A second, **methodologically independent** review was built from scratch — no
inheritance from the pipeline corpus, every source read at its primary record.
Purpose: check the deep-dive, and cover what it deliberately excluded (cost) or
could not reach (WHO guidelines, UN burden datasets).

**New artifacts, all in `final-report/` unless noted:**

| File | What it is |
|---|---|
| `../INDEPENDENT_EVIDENCE_REVIEW.md/.docx` | The independent review. §10 source register with per-item verification status; **§11 corrections log**; corrected passages highlighted yellow |
| `../REVIEW_COMPARISON.md/.docx` | Deep-dive vs independent: 13 convergent findings, 14 adjudicated conflicts, what each has that the other lacks |
| `CARE_FINAL_REPORT.md/.docx` | **The CARE deliverable.** ~4,500 words, four figures, glossary, reference list. Corrections applied silently — no disagreement visible |
| `CARE_FINAL_REPORT_MARKED.docx` | Same content, 26 corrected passages highlighted. **Internal only** |
| `CARE_EVIDENCE_SUMMARY.md` | Longer intermediate draft. **SUPERSEDED — banner added, never fact-checked, do not circulate** |
| `make_figures.py`, `make_marked.py`, `render.sh` | Figure generator, marked-copy deriver, one-command build |

**Build rule:** `CARE_FINAL_REPORT.md` is the single source of truth.
`bash final-report/render.sh` rebuilds figures → clean .docx → marked .md → marked
.docx. `make_marked.py` **fails loudly** if a corrected passage no longer matches,
so the two copies cannot silently drift. Never hand-edit `CARE_FINAL_REPORT_MARKED.md`.

**The fact-check found 16 corrections. Do not reintroduce any of these.**

| Wrong | Right |
|---|---|
| KMC applies to "the newborn" | **Preterm or low-birth-weight infants only.** RR 0.68 (0.53–**0.86**, not 0.87), 11 trials. Inflates eligible population ~7× |
| KMC "the only high-certainty finding" | Only high-certainty **mortality** benefit. Cochrane rates four MMS outcomes high |
| "~11% case fatality" as CMAM's counterfactual | That is mortality **among treated** children. Use Olofin HR **11.63** vs weight-for-height Z ≥ −1 — and note those are general-population cohorts, not treated-vs-untreated |
| MMS stillbirth "replicated in 4 of 5 syntheses" | **Contested.** Cochrane 0.95 (0.86–1.04) high certainty, null. Two of the "five" are one Bhutta-group analysis published twice |
| Maternal mortality "null at high certainty" | **Not GRADE-rated at all.** RR 1.06 (0.72–1.54) — imprecise, not a precise null |
| RUTF formulations "interchangeable" | On **recovery** only. Standard RUTF also reduces relapse (RR 0.84) at high certainty, so substitution is not cost-free |
| Simplified protocols "hold recovery" | **ComPAS** met non-inferiority on ITT *and* per-protocol; **OptiMA failed per-protocol**. Standard beat both in the 1,140 children with MUAC <115mm or oedema |
| WHO 2023 "retains weight-based dosing" | It **revised** it: 150–220 → **150–185 kcal/kg/day**, with an endorsed step-down to 100–130. Dosing stays weight-indexed; the ceiling moved |
| EBF "70% global target" | WHA target is **60% by 2030** (was 50% by 2025). 70% is the Collective's **early-initiation** target — different indicator |
| Ethiopia recovery "fell as programme matured" | A subgroup split by **publication year** of 19 studies, CIs overlapping. Not a time series |
| West Africa EBF 36.5% / EIBF 48.7% | **Not in the source.** It reports Anglophone 41.2% / Francophone 30.1% and 51.7% / 45.5%; no combined figure exists |
| Community packages "bundle tetanus, clean delivery, resuscitation, cord care" | That list is from the review's **Background** as generic examples. The 26 trials vary widely. RR 0.75 is a random-effects average, I² = 85% |
| Cochrane BF "no provider effect" | Add **"power was limited"** — absence of evidence, not equivalence |
| "4–8 contacts outperform fewer" | It is the **middle** category — an intermediate optimum, doubly hedged in the source |
| **Nigeria wasting 6.5%** | **11.6% (2021 NFCMS).** GHO still carries only 2020; World Bank has the newer survey. Moves Nigeria from near the SSA average to roughly double it |
| **Chad wasting 9.0%** | **7.8% (2022).** 9.0% matched no data point — it came from a model summarising a bulk API response rather than raw values |

**A second, final fact-check (2026-08-07, after the report was assembled) found five more.**
Every load-bearing number in `CARE_FINAL_REPORT.md` was re-traced to its primary
source. Most held to the decimal; these did not.

| Wrong | Right |
|---|---|
| MMS birth-size benefit "established at high certainty" for low birthweight **and** SGA | **LBW high, SGA moderate** (Keats CD004905). Figure 1 had it right; the §2 prose had drifted away from the figure |
| MMS procurement gap "$0.9–1.7 per pregnancy" | **$0.9 production** (Engle-Stone, $0.004878 × 180 tablets) or **$1.4 procurement** (Verney 2023, $3.42 vs $2.00). $0.9–1.7 spliced a production floor onto a procurement ceiling; the cited catalogue prices give $1.07–1.67 |
| **Bangladesh wasting 9.8%**, labelled 2022 | **10.7% (2022).** 9.8% is the 2019 round. Changes the reading: Bangladesh is not "unremarkable" — it sits close to Niger and well above the SSA average |
| **Pakistan wasting 6.1%** | **7.1% (2018).** 6.1% matches no data point in WHO GHO or the World Bank series |
| **Nepal wasting 6.9%** | **7.0% (2022).** Both sources give 7.0 |

Three of the five are burden data — the same failure class as Nigeria and Chad.
**Country burden values are the least stable thing in this report and should be
re-pulled from the API before any circulation**, not carried forward from a
previous draft. `code/` has no script for this; the checks were ad-hoc curl
against `ghoapi.azureedge.net` (WHO GHO), `api.worldbank.org` and
`sdmx.data.unicef.org`. Worth writing one.

Verified clean this round and not worth re-checking: every effect estimate and CI
in Figure 1; all five cost studies including the Tekeste 43%/47% composition and
the Rogers Pakistan per-treated ($291 vs $301) / per-recovered ($382 vs $363)
inversion; Menon's four EBF percentages and both DiD estimates; the WHO 2023
recommendation strengths and certainties (cash transfers **are** conditional/moderate,
CHW conditional/very low); WHO 2022 KMC (strong, high, 8–24 h) and its statement
that "in all but one of the studies, the infants were stabilized before enrolment";
WHO 2020 MMS wording; UNICEF LBW country figures (India 27.4, Bangladesh 23.0,
Nepal 19.7) and regional (SSA 13.9, South Asia 24.8 — UNICEF regions, **not** the
UNSDG 24.4); JME regional wasting (SSA 5.9, South Asia 14.1, 2024 reference year).

**Three method lessons worth carrying to the paper.**

1. **The verifier catches none of this.** Every one of the 16 passed it. Traceability
   ≠ fidelity: a number can trace to a real record and still carry the wrong
   population, comparator, certainty rating or vintage. **A population-fidelity
   check is the highest-value upgrade** — match the population attached to an
   effect estimate in synthesis against the population field in the extraction record.
2. **Never read values out of a bulk API response via a model summary.** That is
   how Chad's 9.0% appeared. Query per-entity, or parse the JSON.
3. **Currency is a failure mode of its own.** Nigeria was not wrong when written —
   it went stale. Check whether a newer national survey exists before quoting.

## Open gaps — status against CARE's original ask

1. ~~**Country shortlist**~~ — **DONE (2026-08-04).** `code/country_analysis.py`
   scores 18 eligible countries; §4 of the report. Ethiopia 89.1 and India 74.9
   separate clearly; Bangladesh 42.5; Nepal/Pakistan/Kenya/Ghana/Malawi are a
   near-tied group (31.1–24.8) and must be presented as undifferentiated.
   **Deliberately no lead candidate named** — user decision. §4.6 lists the
   non-corpus facts that would settle it.
2. ~~**Cross-cutting synthesis**~~ — **DONE.** §3: side-by-side table, the three
   scaling positions (PICOS §6), and the common CHW-platform thread.
3. **652 abstract-only papers** un-extracted. Still open; breadth not depth.
4. **Cost / Phase 2** — deferred by design, not a gap.
5. **Complementary feeding** — both CARE TEs advocated pairing counselling with
   food/nutrient support; scoped out. Now an explicit open decision in §8.4.

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
headings, fractions like "4–8 contacts". Also: when a line carries **several
citations**, the verifier checks *every* number on that line against *each*
source, so co-cited claims flag each other. The load-bearing number is
**`NOT_IN_CORPUS = 0`**. Don't chase the rest.

**Exception, deliberate (2026-08-05): the summary now expects `NOT_IN_CORPUS = 6`.**
`brief/01_brief.md` §7 lists eleven sources added at expert review from *outside*
the retrieved corpus — WHO guidelines and landmark trials PubMed/OpenAlex
retrieval did not reach. Six carry a PMID/DOI, so the verifier correctly flags
them. They are marked **†** in the body and confined to §7's table; **if a †
citation ever appears in body text with an identifier, or the count moves off 6,
that is a real regression.** Full report is unchanged at 0.

**Verification does not check population fidelity — this is the known hole.** The
verifier confirms a number is traceable to a corpus record. It does *not* confirm
that the population, comparator or certainty rating attached to that number
survived into prose. An expert fact-check on 2026-08-05 found the summary
describing a **preterm/low-birth-weight** KMC effect (BMJ Glob Health 2023,
RR 0.68) as applying to all newborns — ~7× the eligible population — plus a
"continuous KMC" descriptor absent from the source, a West Africa coverage pair
that is the unweighted mean of two figures the authors never pooled, and a 70%
breastfeeding target that is the wrong indicator *and* superseded (WHA78 set 60%
EBF by 2030). **All four passed the verifier.** Fixed in the summary; see
`EXPERT_REVIEW_OF_DEEPDIVE.md` for the full errata and the report-side items
still outstanding. A population-fidelity check is the highest-value verifier
upgrade and good material for the methods paper.

**Do not invent terminology.** A coined phrase — "crisis-affected belt" — read
like a term of art and got as far as a figure title and legend before the user
caught it. Nothing defines it. Use existing designations: **the Sahel, the Horn of
Africa, and Yemen** (named separately — it is in neither). Same discipline applies
to any grouping label a partner might try to look up.

**Colour that looks like a threshold but encodes a category must say so.** Figure 3
highlights India plus the highest-burden Sahel/Horn/Yemen countries. Burkina Faso
(9.3%) is orange while Bangladesh (9.8%) is blue, which reads as an error unless
the legend states that colour marks *membership of a concentration, not a
prevalence cut-off*. It now does, with the Chad/Mali exception in the footnote.

**Country scoring has two traps — both were live and both distorted the
ranking.** Recorded in `code/country_analysis.py`, but worth knowing before
touching it:
- **Never detect government platforms by naming CHW cadres.** An early version
  matched ASHA/Anganwadi/HEW/LHW etc. The list of names is an artifact of the
  author, not of the evidence, so it inflated whichever countries got named —
  India led on 9/12 sampled platform hits being cadre names vs Malawi's 1/12.
  Score on **generic** language only (national scale, government-led, MoH,
  routine system); keep named cadres for qualitative profile text.
- **Multi-country records must not feed country-level signals.** A review naming
  9 countries was crediting all 9 with what was usually one country's platform
  evidence — the Ethiopian HEP quote was scoring for Malawi, Kenya and Pakistan.
  Signals now come only from records tagged ≤3 countries (70% of tagged records
  are single-country, 76% are ≤3). **This moved Malawi from 4th to 8th.**

**Record volume is not country suitability.** Publication counts measure research
attention. Volume gates candidacy; implementation and platform evidence rank.

**Concatenating report sections needs a blank line between files.** `cat`-ing
`report/*.md` without one lets the next file's `# Chapter` title be swallowed as
a lazy paragraph continuation — it then renders as *body text* in the .docx,
silently. This shipped 8 of 9 chapter titles as prose before it was caught.
`render_report.sh` inserts the separator; don't "simplify" it back to a plain `cat`.

---

## Where things live (post-reorg, 2026-08-03/04)

Everything CARE is in this folder. Paths changed — old references are stale.

```
CARE_review/
  final-report/                   THE CARE DELIVERABLE (v6) — see below
    CARE_FINAL_REPORT.md          source of truth; edit here only
    CARE_FINAL_REPORT_MARKED.*    derived review copy, highlighted
    CARE_EVIDENCE_SUMMARY.md      SUPERSEDED, do not circulate
    make_figures.py               4 figures → figures/*.png
    make_marked.py                derives the marked copy; fails on drift
    render.sh                     one-command rebuild of everything
  INDEPENDENT_EVIDENCE_REVIEW.*   independent review + corrections log
  REVIEW_COMPARISON.*             deep-dive vs independent, adjudicated
  CARE_DEEPDIVE_REPORT.md/.docx   the pipeline report (assembled — do not hand-edit)
  report/                   01_exec … 09_appendix — the editable source sections
  CARE_DEEPDIVE_REVIEW.md   superseded predecessor, kept as a record
  code/                     queries, scoring, retrieval, pipeline + entry points
    country_analysis.py     country scoring → data/country_analysis.json
    build_reference_docx.py styled pandoc template (Cambria/Calibri, Office-safe)
    render_report.sh        assemble → .docx → verify, one command
    assets/reference.docx   generated template
  docs/                     PICOS spec, process doc, methods-paper plan
  prompts/                  extraction + synthesis prompts
  data/                     working dataset (~66M, GITIGNORED)
```

**Markdown is the source of truth; the .docx is generated.** Edit `report/*.md`
and re-run `render_report.sh` — never edit the .docx or the assembled .md, both
are overwritten. This is what keeps the verifier (which reads markdown) able to
guarantee 0 not-in-corpus.

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
python3 CARE_review/code/country_analysis.py         # country scoring (§4, Appendix C)
bash    CARE_review/code/render_report.sh            # assemble + render .docx + verify
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

1. **Send `final-report/CARE_FINAL_REPORT.docx` to CARE** after Liz's review.
   Target 2026-08-08. Use the clean copy, not `_MARKED`.
2. **Decide what happens to `CARE_EVIDENCE_SUMMARY.md`** — superseded and
   uncorrected. Either delete it or port the corrections; it should not sit
   un-flagged next to the deliverable.
3. **The pipeline report `CARE_DEEPDIVE_REPORT.md` still carries all 16 errors.**
   It has not been corrected. Either fix it or mark it superseded before anyone
   reads it alongside the final report.
4. **Four references need page ranges** (Smith 2017, Sudfeld & Smith 2019, Kashi
   2019, Engle-Stone 2019) — verified by PMID/DOI, print pages not confirmed.
5. **Get partner answers to §8.4** — the five open decisions, especially whether
   complementary feeding comes back into scope and whether any countries are
   already ruled in or out.
6. **Cost / Phase 2**, once the country conversation has narrowed. Two findings
   already in the report are cost findings in disguise and should seed it: OptiMA
   holds recovery on ~46% less RUTF, and cutting RUTF dairy (the main cost driver)
   measurably worsens recovery.
7. Optionally finish the 652 abstract-only papers.
8. **Methods paper** — plan in `docs/METHODS_PAPER_PLAN.md`. The cheapest
   high-value next experiment is the adversarial verifier test (plant fabricated
   numbers, measure detection rate); the gold-standard benchmark against published
   Cochrane/Campbell reviews is the non-negotiable one before submission. Note the
   two country-scoring artifacts caught in this session (cadre-name bias,
   multi-country cross-tagging) are good material for the paper's
   "what automated synthesis gets wrong" section.
