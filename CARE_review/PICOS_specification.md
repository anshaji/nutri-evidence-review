# PICOS Specification — CARE/ScaleWorks Deep-Dive Evidence Review

**Status:** v0 draft for internal review (Akash → Liz → CARE)
**Date:** 2026-07-22
**Interventions:** CMAM · Breastfeeding (facility-based) · Breastfeeding (community-based) · Antenatal MMS
**Companion docs:** `workplan_care_deep_dive.docx` · `../output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md`

---

## 0. Why this document exists

> **Scope decision (2026-07-22): evidence first, cost later.** Per partner
> steer, this pass runs **evidence only** — the pipeline's Phase 1. Cost /
> cost-effectiveness outcomes are pulled out of the active scope and deferred
> to Phase 2 (`code/15_run_cea.py`), analyzed after the evidence base is
> validated. The *non-cost* implementation outcomes (coverage, adherence,
> delivery-platform, barriers) stay in this evidence pass. The four §7 open
> decisions are proceeding on their recommended defaults (development-primary;
> cash+SBCC-for-BF in, general CF out; SQ-LNS light reference only;
> country-agnostic retrieval) pending Liz/CARE review.

The initial 15-intervention synthesis answered *"does it work?"* The partner
technical experts told us that is the wrong binding question. Their consensus,
led by Save the Children:

> *"Adherence/coverage — not efficacy — is the binding constraint. These are
> the High-Impact Nutrition Interventions we've prioritized for decades; we
> still miss the WHA targets because no one has cracked sustainable
> operationalization."*

So this review re-scopes each intervention around a **dual outcome axis**:

1. **Clinical / biological** — the efficacy evidence (kept, but not the centre of gravity).
2. **Implementation / scaling** — coverage, adherence, cost-per-beneficiary, delivery-platform feasibility, and institutional barriers. **This is the axis the co-design decision turns on.**

Every PICOS block below therefore carries an explicit implementation-outcome
row, and the study-type row is widened to admit implementation science,
program evaluations, and costing studies — not just SRs/MAs.

**End goal:** identify **one country** to co-design a national-level
intervention leveraging existing government infrastructure. PICOS choices that
follow are made to serve that decision, not to maximize the size of the
evidence bundle.

---

## 1. Cross-cutting parameters (apply to all four blocks unless overridden)

| Parameter | Specification |
|---|---|
| **Setting / geography** | LMICs (World Bank low- + lower-middle-income). Sub-stratify development vs humanitarian/emergency contexts — partners flagged that the binding constraints differ (see §6). Country-scoping shortlist handled separately in the background study. |
| **Time horizon** | Intervention effect windows as reported. For implementation outcomes, prioritize studies with ≥6-month delivery/coverage follow-up (adherence decays; short pilots overstate it). |
| **Publication window** | No hard date cut, but weight post-2013 (Lancet Maternal & Child Nutrition series) for clinical and post-2016 for implementation/cost. |
| **Language** | English-language records (pipeline limitation — flag as a coverage caveat). |
| **Comparator philosophy** | Where a "no-intervention" arm is unethical or absent (CMAM SAM), the *policy-relevant* comparison is **simplified/lower-cost vs standard protocol**, not treatment vs nothing. Encode this per block. |
| **Equity lens** | Capture whether effects/coverage differ by wealth quintile, rural/urban, displacement status, HIV status — the co-design target is national reach, so distributional coverage matters as much as mean effect. |

---

## 2. CMAM — Community-based Management of Acute Malnutrition

*Partner steer (Save the Children, CARE TE#1): CMAM "stands on its own" as a
health-system treatment package; the innovation frontier is **cost efficiency
and coverage via simplified / combined / community protocols**. SCUS has a
Gates proposal along these lines (link with Habtamu).*

| | Specification |
|---|---|
| **P — Population** | Children 6–59 months with acute malnutrition. Split **SAM** (WHZ < −3, MUAC < 11.5 cm, or bilateral oedema) and **MAM** (WHZ −3 to −2, MUAC 11.5–12.5 cm). Include uncomplicated (outpatient-eligible) as the primary scope; complicated/inpatient SAM as secondary context. Flag conflict/displacement sub-populations explicitly (evidence near-absent — synthesis found only 8/91 CMAM publications reported coverage in conflict settings). |
| **I — Intervention** | The CMAM package and its **simplification / integration innovations**: (a) standard outpatient therapeutic care (RUTF for SAM, RUSF/LNS for MAM); (b) **simplified protocols** — combined SAM+MAM treatment, MUAC-only admission/discharge, reduced/optimized RUTF dosing, family-MUAC screening; (c) **community-delivered** models — CHW/community-health-volunteer treatment (not just screening), iCCM integration; (d) low-cost local alternatives (e.g. Tom Brown blended flour) where evidence exists. |
| **C — Comparison** | **Primary: simplified vs standard protocol** (combined vs separate SAM/MAM; MUAC-only vs WHZ; reduced vs standard RUTF dose; CHW-delivered vs facility-delivered). Secondary: alternative therapeutic foods head-to-head (LNS vs FBF, RUSF vs CSB) — but flag these as active-control efficacy, *not* the scaling question. Treatment-vs-no-treatment only where ethically available (observational natural-history). |
| **O — Outcomes** | **Clinical:** recovery rate, non-recovery/default, mortality (all-cause), relapse/SAM-recurrence, weight/MUAC gain velocity, length of stay, refeeding-syndrome safety. **Implementation (priority):** treatment coverage (% of caseload reached), geographic/referral coverage, default & adherence rates, cost per child treated & **cost per DALY averted**, RUTF supply-chain/financing feasibility, CHW workload/feasibility, integration into iCCM/PHC. |
| **S — Study types** | SR/MA and RCT/cRCT for clinical effect; **program evaluations, implementation-science studies, coverage surveys (SQUEAC/SLEAC), costing & CEA studies, operational cohorts** for the scaling axis. Qualitative barrier studies admitted for the barriers outcome. |

**Design notes / what the synthesis already tells us (so the rerun goes beyond it):**
- Efficacy across therapeutic foods is a *solved, near-null* question (RUTF formulations largely equivalent, RR ~1.03–1.08). Do **not** re-centre the review there.
- The real signals are: prophylactic antibiotics ↓ mortality (RR 0.74) — an *adjunct*, flag separately; iCCM ↑ care-seeking coverage 68% (RR 1.68) but one trial showed possible under-5 mortality harm (HR 1.18) — a delivery-platform caution worth surfacing.
- CEA is **Very High and corpus-grounded** (mostly < US$150/DALY; simplified protocols save ~US$5.70/child). Coverage is the binding constraint (one Indian cohort: only ~5% of community SAM reached treatment). → **The rerun's job is to characterize the simplified-protocol coverage/cost frontier, not re-prove efficacy.**
- **Double-counting flag to carry forward:** pmid_37131422 (Campbell) and pmid_31906272 (Nutrients) are twin publications of one 42-study review — count the antibiotic mortality finding once.

---

> **Retrieval decision (2026-07-22): one BF search, split tagged at extraction.**
> The first run showed retrieval cannot cleanly separate facility vs community —
> broad BF reviews (BFHI, IYCF, "scaling up BF promotion") genuinely cover both,
> so two setting-scoped searches returned near-identical top sets and were
> diluted by generic MNCH delivery-platform reviews. Fixed by collapsing to a
> **single title-anchored breastfeeding retrieval** (`breastfeeding` block,
> anchored on BF `[Majr]`/`[ti]`), then assigning each study a **delivery-setting
> tag (facility / community / both)** at extraction. Packages A and B below
> remain the analytical frame the *synthesis* reports against — they are just no
> longer two separate searches.

## 3. Breastfeeding — Package A: Facility-based support around delivery

*Partner steer (CARE TE#2, Save the Children, Mercy Corps): BF is "the behavior
we aim for," not an intervention — so it must be disaggregated. Package A =
**strong facility-based support around delivery**: early initiation,
skin-to-skin, staff practices, BFHI.*

| | Specification |
|---|---|
| **P — Population** | Mother–newborn dyads at/around facility delivery in LMICs. Include term healthy dyads (primary); note preterm/LBW and HIV-exposed as distinct sub-populations. Sub-population of interest to CARE: emergency/IDP/transit settings where *skilled BF support* is the gap. |
| **I — Intervention** | Facility-delivered BF support at/around birth: **early initiation (<1 h), skin-to-skin contact, Baby-Friendly Hospital Initiative (BFHI) implementation, in-service & pre-service health-worker training, rooming-in, Code enforcement on BMS marketing** within the facility. |
| **C — Comparison** | Standard facility care without structured BF support; pre- vs post-BFHI implementation; trained vs untrained delivery staff. Where possible, facility-only vs facility+community (bridges to Package B). |
| **O — Outcomes** | **Clinical:** early initiation rate, exclusive breastfeeding (EBF) at discharge / 4–6 wk / 6 mo, any-BF duration, neonatal thermoregulation & glucose (skin-to-skin proximal markers), neonatal mortality (bundled-package caveat). **Implementation (priority):** BFHI coverage/accreditation sustainability, health-worker training retention & practice fidelity, staffing feasibility, cost per facility / per dyad, integration into existing ANC–delivery–PNC platform. |
| **S — Study types** | SR/MA + RCT/cRCT for proximal BF outcomes; BFHI **implementation & scale-up evaluations**, health-system studies, before/after facility studies, costing studies for the scaling axis. |

**Design notes:**
- Synthesis anchors: skin-to-skin ↑ EBF RR 1.36–1.38 (Cochrane, moderate certainty); professional-led initiation support RR 1.43. These are *proximal-outcome* wins with solid certainty — Package A's clinical case is **stronger and more facility-attributable** than Package B's.
- BFHI (PMID 26924775) and the "breastfeeding gear" scale-up model (PMID 23153733) are named national delivery vehicles → good scaling-pathway evidence to mine.
- **Attribution caveat to preserve:** the strongest mortality/CEA numbers come from *home-visit bundles* (LeFevre Bangladesh, US$103/DALY) that co-deliver EBF with other newborn care — the facility-only contribution is not isolated. The rerun should try to separate facility-attributable effect from bundled effect.

---

## 4. Breastfeeding — Package B: Community / early-postnatal counselling

*Partner steer (CARE TE#2): **targeted counselling during pregnancy and the
early postnatal period, ideally through CHWs with repeated contacts**; peer /
mother-to-mother support; cash+SBCC for PLWs in food-insecure areas. Save the
Children frames BF+CF jointly as an SBCC / behavioral-science problem where the
binding constraint is adherence.*

| | Specification |
|---|---|
| **P — Population** | Pregnant women and mothers of infants 0–6 months in LMIC community settings. Sub-populations: food-insecure PLWs (for the cash+SBCC arm), HIV-exposed dyads, rural/hard-to-reach. |
| **I — Intervention** | Community-delivered BF support: **CHW / peer / lay-counsellor counselling with a defined contact schedule (repeated contacts), mother-to-mother support groups, home visits, cash-transfer + SBCC bundles** enabling dietary access. Characterize by *intensity* (number/timing of contacts) — the partner emphasis on "repeated contacts" makes contact-dose a key modifier. |
| **C — Comparison** | Usual community care / no structured counselling; **counselling-alone vs counselling+cash/food** (partner hypothesis: pairing behaviour change with a food/nutrient component beats standalone SBCC in food-insecure settings); high- vs low-intensity contact schedules; peer vs professional deliverer. |
| **O — Outcomes** | **Clinical:** EBF at 6 mo, any-BF duration, early initiation (community-driven), infant morbidity where reported. **Implementation (priority):** **adherence to counselling contacts, coverage of target dyads, CHW/peer feasibility & retention, cost per additional EBF-month & per DALY, delivery-platform fit (which existing community cadre), social-norm / gender / workplace barriers** (partner-named demand-side constraints). |
| **S — Study types** | SR/MA + RCT/cRCT; **implementation-science & program evaluations of CHW/peer models, SBCC effectiveness studies, cash+ evaluations, costing studies**, qualitative barrier studies (social norms, taboos, gender). |

**Design notes:**
- Synthesis anchors: LMIC support packages ↑ EBF (promotion 100%, education 80%, counselling 58% of comparisons favour intervention — vote-counting, not GRADE); community peer counselling Uganda ICER US$11,353/DALY but **US$68 per additional EBF-month** (cost-effective *for BF prevalence*, not for diarrhoea). → outcome-dependent CEA must be reported honestly.
- This package is where **adherence/coverage is genuinely the binding constraint** — the clinical certainty is lower (much very-low GRADE) but the operational question is live and un-cracked. This is the block most aligned with Save the Children's central thesis.
- **Cash+SBCC arm** is a deliberate addition responding to CARE TE#2 and TE#1 — likely thin in the current corpus; expect the rerun to need expanded search terms (cash transfer, SBCC, social protection).

---

## 5. MMS — Antenatal Multiple Micronutrient Supplementation

*Partner steer (Save the Children): MMS is **commodity-based**; scaling
challenges are **logistics, financing, adherence** — similar to SQ-LNS. The
policy-live question is the **IFA→MMS transition**. Mercy Corps: extremely
limited experience but keen to explore.*

| | Specification |
|---|---|
| **P — Population** | Pregnant women in LMICs (antenatal). Note adolescent-pregnancy sub-group (underpowered/mixed safety signals in current evidence — handle cautiously). Child outcome = birth outcomes. |
| **I — Intervention** | Antenatal MMS — typically the **15-micronutrient UNIMMAP** formulation — delivered through the ANC platform as a substitution for IFA. Scope the **transition mechanics**: procurement, financing, supply chain, counselling for adherence, first/second-trimester initiation, weight-gain monitoring. |
| **C — Comparison** | **Primary: MMS vs IFA** (the policy-relevant transition comparison). Secondary: MMS vs folic-acid-alone / placebo (for completeness); MMS+balanced-energy-protein vs MMS alone (targeted food component). |
| **O — Outcomes** | **Clinical:** LBW, SGA, preterm, small-vulnerable-newborn types, gestational weight gain, maternal anaemia. **Explicitly NOT mortality** as the headline (corpus shows null mortality/growth vs IFA — see caveat). **Implementation (priority):** **adherence/compliance to daily supplementation, ANC coverage & initiation timing, procurement & financing feasibility, supply-chain/logistics, incremental cost per DALY & tablet-price differential, national-transition readiness**. |
| **S — Study types** | SR/MA + RCT (efficacy is well-established — don't over-invest); **implementation studies, national-transition case studies (Bangladesh, Burkina Faso, Tanzania, India, Pakistan), costing/microsimulation, adherence studies**. |

**Design notes:**
- Efficacy is **settled and Grade A on birth outcomes** (MMS vs IFA: SVN types RR 0.71–0.91, IPD n=42,618, low heterogeneity; dominant trial JiVitA-3/West 2014). CEA is excellent and grounded (US$3–253/DALY; NI transition tool US$23.61/DALY). → **The rerun's value-add is almost entirely on the implementation/transition axis**, not efficacy.
- **Hard caveat to lock in:** do NOT present MMS as a mortality intervention — multiple records show null mortality vs IFA. The birth-outcome benefit is real; the mortality claim is not corpus-supported.
- Adherence is the named binding constraint (Save the Children: "commodity-based → logistics, financing, adherence"). Current corpus is thin on real-world adherence — expect to expand implementation-search terms.
- **Adolescent safety flag:** the Burkina Faso weekly periconceptional iron+FA harm signal (preterm RR 2.22) is a *different regimen*, not MMS — keep it out of the MMS effect estimate but note it.

---

## 6. Comparison logic across the three "positions" (Save the Children's frame)

Save the Children explicitly chose these three to **test the ScaleWorks model
from three different scaling positions**. Preserving that framing sharpens the
cross-intervention synthesis:

| Position | Interventions | Binding scaling constraint | What the review must characterize |
|---|---|---|---|
| **Commodity-based** | MMS (analogous: SQ-LNS) | Logistics, financing, adherence | Transition mechanics, procurement, supply chain, real-world adherence |
| **Behaviour / SBCC** | Breastfeeding B (community), + CF-adjacent | Behavioural adherence, social norms, contact dose | Counselling intensity, cash+ pairing, CHW feasibility, demand-side barriers |
| **Health-system treatment** | CMAM | Health-system strengthening, coverage, cost efficiency | Simplified/community protocols, coverage frontier, RUTF financing |

Breastfeeding Package A (facility) sits at the boundary of "behaviour" and
"health-system" — it is a *facility-platform* delivery of a behavioural
outcome, which is analytically useful (it isolates the platform from the
behaviour that Package B tests in the community).

---

## 7. Open decisions for review (Liz / CARE)

1. **Emergency vs development split** — do we scope both, or restrict to development contexts for the co-design target? CARE flagged emergency-specific BF/CMAM gaps; partners' national-scaling goal leans development. *(Recommend: development primary, emergency as a tagged sub-analysis.)*
2. **Cash+ / SBCC breadth** — how far do we expand into complementary-feeding and cash-transfer literature for Breastfeeding B? Risk of scope creep vs partner's explicit ask to pair behaviour change with a food/nutrient component. *(Recommend: include cash+SBCC-for-BF, exclude general CF for now — CF was a separate intervention partners de-prioritized here.)*
3. **SQ-LNS as an MMS shadow arm** — Mercy Corps/CARE floated SQ-LNS. Include as a light comparative "commodity-based" reference, or hold out entirely? *(Recommend: light reference in the cross-cutting section, not a full PICOS block — keeps the three-intervention scope clean.)*
4. **Country pre-commitment** — do we let the country shortlist shape the search (country-specific queries), or keep search country-agnostic and layer country-fit at synthesis? *(Recommend: country-agnostic retrieval, country-fit scoring at synthesis — avoids biasing the evidence base.)*

---

*Next step after sign-off: translate each block's I/C/O into pipeline query
terms (`code/03_queries.py`), expand implementation-science / program-evaluation
search vocabulary, and adjust scoring to weight implementation outcomes — then
run Phase 1 per intervention.*
