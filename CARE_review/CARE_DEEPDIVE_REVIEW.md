# CARE / ScaleWorks Deep-Dive Evidence Review

*PICOS-structured review of three partner-selected interventions — **CMAM**, **Breastfeeding support** (facility + community), and **Antenatal MMS** — for CARE and IA partners (Save the Children, Mercy Corps).*

**Generated:** 2026-08-03  ·  **Evidence records:** 984  ·  **Scope:** evidence only — cost / cost-effectiveness is a separate later phase and is deliberately excluded here.

> **How to read.** Each intervention is rated on two axes: **Evidence strength (A/B/C)** and **Implementation readiness (High/Moderate/Low/Unclear)** — the latter reflects coverage, adherence, delivery-platform fit, and barriers, because partners identified adherence/coverage (not efficacy) as the binding constraint. PICOS spec: `CARE_review/docs/PICOS_specification.md`.

---

## Community-based Management of Acute Malnutrition (CMAM)  (children 6–59 months, SAM & MAM)
**Evidence: B  |  Implementation readiness: Moderate (CHW-coverage lever now well-evidenced)  |  Scalability: Growing (national in Ethiopia)  |  Tier 1**

- **Evidence base.** 239 on-topic records — a systematic-review/meta-analysis backbone (12 MA, 12 SR) plus an unusually deep base of **program-evaluations** and 32 RCTs, so the implementation axis is directly evidenced, not inferred. Core reviews: the twin acute-malnutrition syntheses (PMID 37131422 *Campbell* and 31906272 *Nutrients* — **same 42 studies / 35,017 children; count shared findings once**), the LNS-for-MAM meta-analysis (PMID 28934235), an RUTF-vs-standard meta-analysis (PMID 24564235), the Cochrane iCCM review (PMID 33565123, CD012882), the Cochrane supplementary-feeding overview (PMID 30480324, CD010578), and the CHW-operational review (DOI 10.1111/mcn.12719). Certainty is **low-to-moderate GRADE**, concentrated in Africa and resting on **active-control comparisons** — hence **Evidence B**.

- **Clinical effect sizes** (recovery/anthropometric unless flagged mortality):
  - **RUTF/community treatment vs standard therapy:** nutritional recovery RR 1.51 (95% CI 1.04–2.2, 3 studies) with no significant mortality difference (PMID 24564235) — the closest signal to a treatment-vs-standard benefit.
  - **MAM — LNS vs fortified blended food:** recovery RR 1.08 (1.02–1.14), 8 studies, N=8,934; failure-to-recover RR 0.70 (0.58–0.85) (PMID 28934235). RUSF vs corn-soy blend recovery RR 1.07 (1.02–1.13), 6 studies (PMID 31906272).
  - **Integrated community-based vs no community strategy:** recovery RR 1.04 (1.00–1.09), N=1,957 (dominant trial Maust 2015); mortality null RR 0.93 (0.60–1.45) (PMID 37131422, 31906272).
  - **SAM adjunct — prophylactic antibiotics (uncomplicated SAM, all-cause mortality):** RR 0.74 (0.55–0.98), 3 studies, N=6,944 (PMID 37131422 / 31906272 — **the twin reviews; one finding**), driven by the large Malawi RCT (Trehan 2013, amoxicillin/cefdinir added to RUTF; DOI 10.1056/nejmoa1202851); the strongest mortality signal, but an adjunct drug, not the food component. Routine-antibiotic evidence is otherwise mixed (DOI 10.1371/journal.pone.0053184), and in *complicated* SAM co-trimoxazole was null on all-cause mortality (HR 0.90, 0.71–1.16; DOI 10.1016/s2214-109x(16)30096-1).
  - **Lower-dairy RUTF is worse:** recovery RR 0.93 (0.87–1.0), weight-gain SMD −0.20 (−0.26 to −0.15), 6 studies (DOI 10.1093/advances/nmab027) — milk content matters, and milk is the main cost driver.
  - **RUTF formulation head-to-heads** otherwise largely equivalent (soya-maize-sorghum better for anaemia, RD 12.6 (2.1–23.1), DOI 10.1186/s12889-019-7170-x).

- **Real-world program performance — recovery falls short of standards and doesn't improve with scale (NEW):**
  - Pooled SAM recovery **71.2%** across 54 sub-Saharan studies (N=140,148) — **below the >75% Sphere minimum** — comparable inpatient (70.4%) vs outpatient (71.1%) (PMID 32187182). Ethiopian OTP: recovery 70%, defaulter 10%, non-recovery 15% (PMID 32631260); inpatient recovery 70.5%, mortality 10.3%, defaulter 13.8% (DOI 10.1186/s12889-019-7466-x).
  - **Recovery *declined* as the national program matured** (72% pre-2015 → 69% post-2015; PMID 32631260) — a caution that scaling can dilute quality.
  - SAM carries ~**11% under-5 case mortality** in Africa (PMID 39885605); post-discharge relapse/loss-to-follow-up is high (LTFU 0–45%; HIV+ relapse 14.3% vs 2.0%; DOI 10.1371/journal.pone.0202053); inpatient refeeding-syndrome prevalence 8.7–34.8% by definition (PMID 41007088).

- **Baseline coverage is the core problem — routine CMAM reaches only ~⅓ of cases (NEW, quantified).** Across **44 SQUEAC/SLEAC coverage assessments in 21 countries (2012–13), mean estimated CMAM coverage was ~one-third of SAM cases** (DOI 10.1371/journal.pone.0128666; corroborated DOI 10.3389/fpubh.2016.00198). Program completion is often worse than recovery statistics imply: a real-world Mozambican OTP saw only **21.7% complete treatment (77% dropout)** (PMID 34583347), and a Ghanaian OTP in Tamale recovered just **33.6%** — far below the Sphere standard (DOI 10.1155/2015/641784). This is the operationalization gap ScaleWorks exists to close.

- **The coverage lever — decentralising treatment to CHWs roughly doubles coverage (NEW, consistent across program evaluations):**
  - **Mali (Kayes/Bafoulabé):** SAM treatment coverage 28.7%→57.1% and 20.4%→61.1% after adding CHWs as treatment providers (up to +40.7pp; DOI 10.1186/s12960-022-00771-8).
  - **Tanzania:** CHW home treatment coverage **80.9% vs facility 41.7%**, with default 6.5% vs ~21% and superior cure (RR 1.17, 1.05–1.31; DOI 10.1038/s41598-021-81811-6).
  - **Mauritania:** SQUEAC coverage 53.6%→71.7% with CHW decentralisation; CHW default 2.6% vs facility 3.8% (DOI 10.3390/children8121132).
  - **Niger (humanitarian, simplified ComPAS protocol):** coverage rose +51.7pp (simplified) vs +35.6pp (standard), using **70 vs 95 RUTF sachets per cured child** (DOI 10.3390/nu15081975).
  - CHWs achieve high-quality MUAC diagnosis/treatment (75–97% correct with supervision) and can integrate into iCCM (DOI 10.9745/ghsp-d-18-00105, 10.1111/mcn.12719). **Ethiopia is the only country delivering CHW-managed SAM at national scale** (~40,000 Health Extension Workers; DOI 10.1186/s12961-021-00757-3).

- **Comparison arms (PICOS C) — simplified vs standard holds up:**
  - **ComPAS (combined SAM+MAM):** recovery non-inferior (RD 0.03, −0.05–0.10, N=2,488), removes the need for two products (DOI 10.1371/journal.pmed.1003192; humanitarian coverage gains above).
  - **OptiMA (reduced RUTF dosing):** recovery non-inferior (RD 2.0, −2.0–6.4) with **~46% less RUTF** (78 vs 147 sachets/child; DOI 10.1016/j.eclinm.2023.101878).

- **Persistent barriers (NEW depth):** RUTF **stock-outs** are pervasive — one Ghana district found 0/8 facilities with RUTF in stock and only 25% of staff trained (DOI 10.1016/j.jtumed.2023.02.002); **RUTF sharing/trading** within households is common (62.9% reported sharing in one cohort; DOI 10.1182/bloodadvances.2023010789; also flagged in Ethiopian OTP, PMID 32631260); distance/transport cost suppress care-seeking (South Sudan: 91.3% care-seeking but only 54.3% CMAM enrolment, 14.9% reached by a nutrition volunteer; PMID 40361061); health-worker turnover erodes capacity (Colombia: 40.6% of trained counsellors left; PMID 40296067). Note a **counter-signal**: clinic-based *systematic* screening enrolled 98% of detected cases vs 8% for community mass screening in Burundi (PMID 32003813) — facility screening is not always the weaker channel.

- **Coverage ≠ treatment even when screening scales:** integrating SQ-LNS into CHV screening raised screening coverage +40pp but left treatment coverage at 7.6% (Mali; DOI 10.1371/journal.pmed.1002892); real-world WHO-guideline uptake reaches only ~25% of 20 high-burden countries nationwide (DOI 10.3310/hta16190).

- **Demand-side (cash) improves adherence and outcomes:** a DRC cluster-RCT adding an unconditional cash transfer to SAM treatment improved recovery HR 1.35 (1.10–1.69), cut relapse to MAM HR 0.21 (0.11–0.41), and lowered defaulting (1.4% vs 6.0%) (DOI 10.1186/s12916-017-0848-y).

- **Equity:** iCCM showed a pro-poor gradient for infant mortality (PMID 33565123); HIV+ children recover far less (SAM recovery POR 0.19; PMID 32187182; MAM 63% vs 88%; PMID 28934235); concurrent wasting+stunting concentrates in fragile/conflict states (3.6% vs 2.24%; PMID 34486229), where coverage evidence is thinnest.

- **Mechanism.** RUTF enables outpatient rehabilitation of uncomplicated SAM at home; RUSF/LNS treat MAM; F75/F100 stabilise complicated inpatient cases. Community MUAC screening (by CHWs *or* caregivers) plus decentralised distribution converts a hospital-bound problem into a primary-care one — the dominant coverage lever — and simplified/combined protocols cut commodity load while holding recovery.

- **Caveats.**
  - **Twin-publication double-counting (G6):** PMID 37131422 (*Campbell*, 2020) and 31906272 (*Nutrients*, 2020) report **identical estimates across multiple outcomes** — antibiotic mortality RR 0.74 (0.55–0.98), 3 studies, N=6,944; recovery RR 1.04, N=1,957; RUSF-vs-CSB RR 1.07, N=5,744 — indicating one underlying 42-study / 35,017-child evidence base published twice. Count these findings **once**, not as independent confirmations.
  - **Active-control ceiling** caps the grade at B; recovery is measured against another food/protocol, rarely against no treatment.
  - **Program-performance shortfall:** the operational reality (recovery ~71%, below Sphere; declining with scale; stockouts) is the honest headline for "can we scale it?" — the CHW-coverage evidence shows *how* to raise reach, but quality and supply chain remain binding.
  - *Refresh note:* **all 981 full-text papers are now extracted** (984 records, 648 on-topic across the 3 interventions); only abstract-only records remain outstanding, so the full-text evidence is complete.


---

## Breastfeeding Promotion & Support  (mothers & infants 0–6 months; disaggregated facility vs community)
**Evidence: A  |  Implementation readiness: Moderate  |  Scalability: Proven national (coverage below target)  |  Tier 1**

- **Evidence base.** 193 on-topic records (30 MA, 29 SR, 12 RCT, plus qualitative and program-evaluations). Backbone: the Cochrane support review (PMID 36282618, CD001141, 116 trials, 98,816 pairs), the Cochrane skin-to-skin review (PMID 41120189, CD003519), a high-certainty KMC mortality meta-analysis (DOI 10.1136/bmjgh-2022-010728), an overview of Cochrane BF reviews (PMID 36761137), a peer-support meta-regression (PMID 22277543), a home-based postnatal meta-analysis (PMID 31852432), a "what works at scale" review of 115 reviews (PMID 35315573), plus qualitative barrier syntheses. Proximal- and now distal-outcome effects are consistent → **Evidence A**.

- **The pivot finding (PMID 36282618):** support reduces breastfeeding cessation whether delivered by professionals *or* lay/peer supporters, is **more effective in LMICs than HICs** (meta-regression RR 1.15, 1.05–1.27), and a **moderate-intensity schedule of ~4–8 postnatal contacts outperforms low-intensity** (RR 0.82, 0.70–0.95 for EBF at 6 months). The authors call the remaining question "a scaling-up issue" — efficacy is settled; **contact intensity and coverage are the binding constraints.**

### Package A — Facility-based support around delivery

- **Clinical effect sizes (facility) — now including a high-certainty mortality benefit:**
  - **Kangaroo Mother Care (KMC):** reduces neonatal mortality **RR 0.68 (0.53–0.87)**, 12 studies, N=10,505 (**high-certainty**), plus severe infection RR 0.85 (0.79–0.92) and EBF at discharge RR 1.48 (1.44–1.52) (DOI 10.1136/bmjgh-2022-010728) — anchored by the landmark WHO iKMC RCT, where continuous skin-to-skin plus exclusive breastfeeding initiated *before* stabilization reduced neonatal mortality (DOI 10.1056/nejmoa2026486). Hospital-based KMC alone: in-hospital mortality RR 0.79 (0.70–0.90), 28-day RR 0.81 (31 RCTs, N=8,561; PMID 41613333). The benefit is **dose-dependent (≥8 h/day)** and drove WHO's 2022 preterm-care guidelines and Global Position Paper calling to reorganise newborn care around KMC (DOI 10.1016/s0140-6736(23)01000-0) — the strongest single facility-package result in the corpus.
  - **Skin-to-skin contact (Cochrane CD003519):** exclusive breastfeeding at discharge–1 month RR 1.36 (1.19–1.56) and at 6 weeks–6 months RR 1.38 (1.09–1.74); infant temperature MD +0.28 °C (PMID 41120189). Moderate certainty — but no LIC trials, only 12/69 in LMICs.
  - **Early-initiation via health-system strengthening:** in South Asia, provider-facing/health-system-strengthening interventions raised early initiation **RR 2.76 (1.96–3.88)** — far above the behavioral-intervention subgroup (RR 1.48) (PMID 40426155). Overall early-initiation interventions RR 1.55 (1.24–1.95).
- **Implementation (facility):** delivered through the ANC–delivery–postnatal platform. The constraint is scale/coverage, not efficacy: <4% of African deliveries occur in BFHI-designated hospitals and only ~60% in any facility (PMID 39764605); KMC scale-up is slow and infrastructure-sensitive (NICU space, staffing, gender-norm barriers in LMICs; PMID 41602019, 26818943), and immediate-KMC readiness needs major, variable investment (PMID 37301974). So the facility package has **strong efficacy (mortality + EBF) but a wide coverage gap.**

### Package B — Community / early-postnatal counselling

- **Clinical effect sizes (community):**
  - **Home-based postnatal care:** neonatal mortality RR 0.76 (0.62–0.92) and EBF OR 2.88 (1.57–5.29); **CHW-delivered drove the mortality benefit (RR 0.69) whereas health-professional-delivered did not (RR 1.26)**; >70% coverage OR 4.06; >3 visits larger effects (PMID 31852432). KMC's mortality benefit also held community-initiated (RR 0.71; DOI 10.1136/bmjgh-2022-010728).
  - **Peer support (meta-regression):** any breastfeeding RR 0.85 (0.77–0.94) and exclusive RR 0.82 (0.76–0.88), **markedly stronger in LMICs (RR 0.70 / 0.63) than HICs (0.93 / 0.90)** (PMID 22277543).
  - **Community intervention packages:** early initiation by ancillary nurse-midwives RR 1.93 (1.55–2.39, N=72,464); community health education RR 1.56 (1.37–1.77) (PMID 36761137). BF support packages in LMICs: 58% of comparisons positive (promotion 80%, education 55%; PMID 33672692).
  - **mHealth:** EBF at 5–6 months OR 1.74 (1.34–2.29) across 22 LMIC studies — but effects concentrate among wealthier/urban/educated women, and one-way messaging is ineffective (PMID 41742073).
- **Implementation (community):** the strength is LMIC effectiveness, distal reach (neonatal survival via CHW home visits), and contact-dose dependence; the weakness is fidelity documentation (only 5/17 peer-support trials reported contacts received; PMID 22277543). Platforms are established (Women's Development Army; PMID 30257661).

### Which package is stronger? (partners' central question, on the fuller base)

- **Facility (A) is stronger than the interim suggested:** it now carries **both** a high-certainty *mortality* intervention (KMC, RR 0.68) and proximal EBF gains (skin-to-skin RR 1.36), and health-system strengthening produces the single largest early-initiation effect (RR 2.76). Its gap is coverage/scale, not evidence.
- **Community (B):** the stronger LMIC-specific *continuation* signal (peer support EBF RR 0.63) and CHW-delivered survival benefit, coverage- and dose-dependent.
- **Best supported overall — they are complementary, and the corpus now points to a specific configuration:** **KMC/skin-to-skin + early initiation anchored at the facility, followed by CHW-delivered repeated postnatal counselling (4–8 contacts) in the community.** KMC works in *both* settings (facility RR 0.62, community RR 0.71), and the flagship review shows support works through either channel and is more effective in LMICs — so a facility-anchored start with community continuation is the best-evidenced package, matching CARE TE#2's steer.

- **Cross-cutting implementation evidence.**
  - **Coverage gap everywhere:** EBF/early-initiation sit below the 70% WHA target — Ghana EBF 50%, Nepal 43%, West Africa EBF 36.5%/EIBF 48.7% (PMID 37208682, 37269619, 39764605). Notably Nepal EBF was higher in community-set (57.8%) than facility-set studies (30.1%) (PMID 37269619).
  - **The evidence base is HIC-skewed at scale:** of 115 reviews, only 17.4% were LMIC-only, just 7% addressed structural/policy levers (Code, maternity benefits), and multilevel/multicomponent programs were most effective (PMID 35315573).
  - **Barriers (demand side):** maternal employment/return to work (most-studied), caesarean delivery (2.28–10.54× lower EBF), perceived insufficient milk, discarding colostrum, family/grandmother influence, and HIV-related stigma (PMID 28965508, 34090461, 41024075).
  - **Policy levers:** WHO-Code implementation is uneven (South Asia 69–94/100; PMID 37937076); paid maternity leave and Code enforcement shifted BF historically.
  - **Cash/incentives:** RCT evidence is low-quality but suggestive (3/6 incentive trials positive; PMID 41257659) — consistent with CARE's cash+SBCC steer, not yet a firm base.

- **Caveats.**
  - *Attribution:* the home-visit mortality signal (RR 0.76) comes from bundles co-delivering EBF with other newborn care — the BF-specific share is not isolated (PMID 31852432). KMC's effect is cleaner (skin-to-skin + BF are its mechanism).
  - *Setting tags are study-level judgments;* "both"-tagged reviews (the flagship Cochrane support review) pool facility and community delivery.
  - *HIC dilution* persists in skin-to-skin and at-scale reviews; LMIC-specific estimates are flagged where separated.
  - *Refresh note:* **all 981 full-text papers are now extracted** (full-text evidence complete, incl. the KMC mortality trials and setting split); only abstract-only records remain outstanding.


---

## Antenatal Multiple Micronutrient Supplementation (MMS)  (pregnant women; child birth outcomes)
**Evidence: A  |  Implementation readiness: Moderate (adherence ~41–46% is the constraint)  |  Scalability: Requires investment  |  Tier 1**

- **Evidence base.** 203 on-topic records — a deep meta-analytic backbone (33 MA, 16 SR, 30 RCT) plus real-world adherence/coverage studies. MMS-vs-IFA birth-outcome benefit is consistent across the IPD *Lancet Global Health* meta-analysis (PMID 39890230, 14 trials, N=42,618), the Campbell review (PMID 37051178, 72 studies) and its *Nutrients* companion (PMID 32075071), a modular *AJCN* review (PMID 37331760), a 169-RCT network meta-analysis (PMID 31348509, N=302,061), the *CMAJ* meta-analysis (DOI 10.1503/cmaj.081777), and long-term follow-up (PMID 27306908) → **Evidence A**, with the explicit caveat that mortality/growth are not improved over IFA.

- **Clinical effect sizes — MMS vs IFA (birth outcomes):**
  - **Low birthweight** RR 0.85 (0.77–0.93), 28 studies, N=79,972 (PMID 37051178, 32075071); RR 0.88 (0.85–0.91), 18 studies (PMID 37331760); MMN >4 micronutrients RR 0.79 (0.71–0.88) (PMID 37051178).
  - **SGA** RR 0.93 (0.88–0.98), 19 studies (PMID 37051178); **stillbirth** RR 0.91 (0.86–0.98), 22 studies (PMID 37051178).
  - **Small-vulnerable-newborn types (IPD):** preterm–SGA–LBW RR 0.73 (0.64–0.84); preterm–SGA RR 0.71 (0.62–0.82) — 14 studies, N=42,618 (PMID 39890230).
  - **Maternal status:** third-trimester haemoglobin MD +0.67 g/dL (0.49–0.84), GRADE moderate (PMID 42067194); reduced late-pregnancy vitamin A/B-12/D deficiency (JiVitA-3, DOI 10.1093/jn/nxz046).
  - **Nuance on preterm:** across 169 RCTs, maternal MMN reduced preterm birth vs standard of care (OR 0.54, 0.27–0.97) but the **MMN-vs-IFA network comparison was null (OR 0.90, 0.78–1.01)** (PMID 31348509) — MMS's specific edge over IFA is on LBW/SGA/stillbirth, not preterm.

- **HARD caveat — MMS is not a mortality intervention over IFA (G4).** Perinatal mortality RR 1.00 (0.90–1.11), maternal mortality RR 1.04 (0.71–1.51) (PMID 32075071); no long-term offspring mortality (RD −0.05, N=88,057) or growth benefit (PMID 27306908).

- **Safety signal — contested, likely not real, but worth monitoring.** An early subgroup analysis suggested MMS neonatal-mortality risk *increased* where most births were at home (60%-facility-birth threshold; DOI 10.1186/1471-2458-11-s3-s19). However, a **WHO technical correction of that subgroup analysis found no evidence that MMS increases neonatal mortality** once errors were fixed and additional trials added — **corrected pooled RR 1.05 (0.85–1.30) vs the original 1.22 (0.95–1.57)** — and attributed the residual signal largely to **iron dose**, recommending programmes choose an MMS formulation whose iron dose matches their current iron-only dose (e.g. 60 mg Fe where 60 mg is already used) (DOI 10.1093/jn/nxy279). A task-force IPD analysis of ~113,000 pregnancies reaffirmed the birth-outcome benefit (DOI 10.1111/nyas.14271; updated WHO evidence: MMS ↓ LBW ~12% vs IFA, DOI 10.1136/bmjgh-2020-003375). So this is **not a solid contraindication** — but where skilled birth attendance is very low, the birth-outcome gains are smaller and MMS should be introduced alongside facility-delivery strengthening rather than as a standalone fix. A useful country-selection consideration, not a hard filter.

- **Implementation evidence (priority axis) — adherence is the binding constraint, now quantified:**
  - **Real-world adherence is ~41–46% and below WHO targets.** Pooled IFAS adherence in Ethiopia was **41.4%** (33–50%, 15 studies; DOI 10.1186/s12884-020-2835-0) and **46.2%** (34.8–57.6, 20 studies; DOI 10.1186/s12978-019-0848-9), ranging 19.7% (Afar) to 60% (Addis Ababa). **Facility-based adherence (47.3%) exceeded community-based (37.2%)** (DOI 10.1186/s12884-020-2835-0) — the ANC facility contact is where adherence is strongest. Single-site studies span a wide range — ~35–41% in parts of Ethiopia (DOI 10.3389/fpubh.2022.978084, 10.1371/journal.pone.0227090) up to **77–82% in north India / West Bengal** (DOI 10.4103/jfmpc.jfmpc_1742_20, 10.4103/jfmpc.jfmpc_392_20) — adherence is highly context-dependent, not uniformly low, and responds to counselling and ANC contact.
  - **Adherence drivers are ANC contact and counselling:** early ANC registration (<16 wk) OR 2.54 and ≥4 ANC visits OR 3.66 (DOI 10.1186/s12884-020-2835-0); receiving counselling/information OR 2.34 (DOI 10.1186/s12978-019-0848-9). Intermittent (weekly) dosing improves adherence over daily (RR 1.60, 1.34–1.91) at slightly lower haemoglobin (PMID 39780191).
  - **Barriers:** fear of side effects (46.4%) and forgetfulness (30.75%) are the leading non-adherence reasons (DOI 10.1186/s12978-019-0848-9); GI side effects recur across reviews (PMID 39780191, 32110886); large capsules, and community rumours about an over-large baby / male-partner gatekeeping in Niger (PMID 30103529).
  - **Coverage is low and ANC-gated:** only 37% of pregnant women in Bihar received any IFA and 24% consumed ≥90 days (PMID 30499258); ~50% of women in sub-Saharan Africa lack skilled ANC/delivery (DOI 10.1371/journal.pone.0222566) — and ≥1 skilled ANC visit itself lowers neonatal mortality RR 0.61 (0.43–0.86).
  - **What raises coverage/adherence:** the most effective South Asian programmes combined **community home-visit delivery of free supplements + quality counselling + husband/family engagement + supply-chain strengthening** (PMID 30499258); participatory women's groups + cash/food transfers raised iron-folate consumption 2.5–4.6× and attendance to 96% in Nepal (DOI 10.1093/jn/nxy109). CHW platforms already dispense IFA at scale (DOI 10.1186/s12960-018-0304-x).
  - **Scalability:** WHO recommends antenatal MMS in the context of rigorous research (PMID 39890230, 42067194); only 2 of 72 studies were effectiveness trials (PMID 32075071). National ANC platforms (India's Anemia Mukt Bharat / NIPI) exist to carry an IFA→MMS substitution (DOI 10.3390/nu13082745, 10.3389/fendo.2021.619176).

- **Comparison arms (PICOS C).** Primary: **MMS vs IFA** (the transition question). Secondary **SQ-LNS vs IFA/MMS**: prenatal SQ-LNS improved birthweight (MD +48.7 g), LBW (RR 0.89), newborn stunting (RR 0.83) vs IFA (PMID 39154665), with larger effects in vulnerable subgroups — a commodity-based option if partners want one beyond MMS.

- **Mechanism.** MMS (typically the 15-micronutrient UNIMMAP formulation; only 11 of 34 trials used UNIMMAP, PMID 37051178) corrects concurrent maternal deficiencies constraining fetal growth — acting on fetal growth/gestational duration (LBW/SGA), not survival.

- **Caveats.**
  - *Efficacy is settled; the value-add is implementation* — the real deliverable is the IFA→MMS transition and lifting adherence from ~45% toward target.
  - *Health-system context:* an early home-birth neonatal-mortality signal was overturned by a WHO technical correction (DOI 10.1093/jn/nxy279); MMS is not contraindicated by low facility delivery, but its birth-outcome gains are larger where antenatal/delivery care is stronger — a country-selection consideration, not a filter.
  - *Adjacent records:* preconception folic-acid/IFA reviews (PMID 32110886, 37131925), fortification (DOI 10.1186/2046-4053-2-67, 10.1186/1471-2458-11-s3-s19 partly), zinc (DOI 10.1111/j.1365-3016.2012.01289.x) and anaemia-determinant reviews were retrieved by comparator/population terms and are context, not core MMS-vs-IFA evidence.
  - *Refresh note:* **all 981 full-text papers are now extracted** (full-text evidence complete); only abstract-only records remain outstanding.


---
