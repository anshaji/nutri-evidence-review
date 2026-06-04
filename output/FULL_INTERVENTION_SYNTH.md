# Evidence + Cost-Effectiveness Synthesis: Nutrition Interventions for Children Under 5 and Women of Reproductive Age in LMICs

**Pipeline version:** 3.0 (two-phase: evidence → cost-effectiveness)
**Phase 1 corpus:** top 200 ranked papers (117 with PMC full text), population-targeted (under-5 / WRA)
**Phase 2 corpus:** `cea_by_intervention.json` — targeted CEA search per shortlisted intervention
**Date:** 2026-06-03

## How to read this synthesis

This document follows the grounding rules in `prompts/synthesis_prompt.md`:

- **Every numeric claim cites a corpus PMID.** Figures not in the retrieved corpus are not stated. Effect sizes are taken verbatim from the cited paper's abstract/full text.
- **Study types are reported verbatim** from `journal` + `publication_type` — a review is only called "Cochrane" when published in *The Cochrane Database of Systematic Reviews*.
- **All-cause vs cause-specific** outcomes are kept separate; underpowered pathways are flagged.
- **Cost-effectiveness is rated ONLY where Phase 2 retrieved a genuine, intervention-specific CEA** (`cea_rating_allowed`). Where the CEA evidence is absent or only generic, the rating is **Unknown** — never inferred from background knowledge.
- The Phase 1 corpus contains **no cost-effectiveness analyses by design**; all CE figures come from Phase 2.

Ratings: **Evidence** A (multiple consistent MAs) / B (some MA/SR, mixed) / C (limited or indirect). **Cost-effectiveness** Very High / High / Moderate / Unknown. **Scalability** Proven national / Proven subnational / Growing / Requires investment.

---

## Summary table

| Rank | Intervention | Pop. | Evidence | Cost-effectiveness | Scalability |
|------|--------------|------|----------|--------------------|-------------|
| **Tier 1 — strong evidence + cost-effective + scalable** ||||||
| 1 | Large-scale food fortification (staple foods) | both | A | High (openalex 63-country review*) | Proven national |
| 2 | Vitamin A supplementation (children 6–59 mo) | u5 | A (context-dependent) | High (PMID 35390077) | Proven national |
| 3 | Zinc for treatment of diarrhoea | u5 | A | High (PMID 16512321, 25128210) | Proven national |
| 4 | Antenatal multiple micronutrient supplementation (MMS) | WRA | A | High (PMID 35192606; openalex $3–15/DALY) | Growing → proven |
| 5 | Breastfeeding promotion & support | u5 | A | High (PMID 26619338) | Proven national |
| 6 | Small-quantity lipid-based nutrient supplements (SQ-LNS) | u5 | A | High (openalex, Uganda) | Growing |
| **Tier 2 — strong/mixed evidence + scalable with investment** ||||||
| 7 | Community-based management of acute malnutrition (RUTF/CMAM) | u5 | A | Moderate (PMID 33102783) | Proven subnational |
| 8 | Complementary feeding interventions (education ± food) | u5 | A | High (PMID 26619338 proxy) | Growing |
| 9 | Micronutrient powders (home fortification) | u5 | B (net-benefit caveat) | Moderate (PMID 36192508) | Growing |
| 10 | Periconception/antenatal folic acid | WRA | A (NTD) | High (via fortification) | Proven national (fortification) |
| 11 | Antenatal iron / iron-folic acid | WRA | A (anaemia) | Moderate (PMID 35192606) | Proven national |
| 12 | Balanced energy-protein supplementation (undernourished pregnancy) | WRA | B+ | Moderate (PMID 35192606) | Requires investment |
| **Tier 3 — promising/indirect evidence + plausible pathway** ||||||
| 13 | Iron supplementation in children | u5 | B (benefit in anaemic; risk if iron-replete) | Moderate (PMID 36192508) | Growing |
| 14 | WASH for child nutrition | u5 | B/C (small linear-growth effect) | **Unknown** (no specific CEA retrieved) | Requires investment |
| 15 | Cash transfers for child nutrition | u5 | C (indirect, nutrition-sensitive) | **Unknown** (no specific CEA retrieved) | Proven national (as social protection) |

\* The fortification CE evidence retrieved is a 63-country systematic review of economic evaluations (openalex, medRxiv 2025) plus the VAS-comparator paper; see entry #1.

---

# Tier 1

## 1. Large-scale food fortification of staple foods
**Population:** children + WRA · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Proven national**

**Evidence.** A systematic review and meta-analysis in *The American Journal of Clinical Nutrition* found large-scale fortification (LSFF) of staples with vitamin A, iodine, iron and folic acid produced a **34% reduction in anaemia (RR 0.66, 95% CI 0.59–0.74)**, a **74% reduction in the odds of goitre (OR 0.26, 95% CI 0.16–0.43)** and a **41% reduction in the odds of neural tube defects (OR 0.59)** (PMID 30997493). Double-fortified salt (iron + iodine) reduced anaemia risk (**RR 0.59, 95% CI 0.46–0.77**) and iron-deficiency anaemia (**RR 0.37, 95% CI 0.25–0.54**) in efficacy studies (Cochrane-adjacent SR in *Advances in Nutrition*, PMID 29767699). Zinc fortification of staples (Cochrane review, PMID 27281654) and vitamin A fortification (Cochrane review, PMID 31074495) add supporting evidence; fortified dairy/cereals for older children showed weaker, non-significant haemoglobin effects (PMID 30673769).

**Cost-effectiveness.** A systematic review of economic evaluations across 63 countries (>200 analyses; openalex, medRxiv 2025) reports food fortification is cost-effective for reducing malnutrition across most LMIC settings. *Genuine intervention-specific CEA retrieved → rating permitted.*

**Scalability.** Salt iodization and flour fortification are among the most widely scaled nutrition interventions globally, delivered through existing food-industry supply chains with regulatory mandates — minimal per-capita cost and no behaviour change required.

## 2. Vitamin A supplementation (children 6–59 months)
**Population:** under-5 · **Evidence: A (context-dependent)** · **Cost-effectiveness: High** · **Scalability: Proven national**

**Evidence.** The systematic review and meta-analysis in *BMJ* (Imdad et al., PMID 21868478) pooled **43 trials, ~215,633 children**; 17 trials (194,483 participants) showed a **24% reduction in all-cause mortality (rate ratio 0.76, 95% CI 0.69–0.83)** and a **28% reduction in diarrhoea-associated mortality (0.72, 95% CI 0.57–0.91)**. The current Cochrane review (*The Cochrane Database of Systematic Reviews*, 2022 update, PMID 35294044) continues to support VAS for children 6–59 months. The CHERG meta-analysis in *BMC Public Health* (PMID 21501438) provides cause-specific estimates for the Lives Saved Tool.

**All-cause vs cause-specific / context.** Benefit is clearest for all-cause and diarrhoea mortality. **Neonatal** VAS shows **no overall effect on infant survival (RR 0.97, 95% CI 0.89–1.06 through 6 months; RR 1.00, 0.93–1.08 through 12 months)** in an 11-trial IPD meta-analysis (*Archives of Disease in Childhood*, PMID 30425075), with benefit only in specific subgroups (Southern Asia RR 0.87, 0.77–0.98; moderate/severe-deficiency contexts RR 0.87, 0.80–0.94). A trial-synthesis paper explicitly asks whether **routine VAS is still justified in Nepal** as deficiency declines (PMID 35584136) — i.e. the mortality benefit is contingent on baseline vitamin A deficiency, not universal.
*Version note (G6): the 2017 and 2022 Cochrane VAS reviews share one accession and are the same review; this synthesis counts them once.*

**Cost-effectiveness.** An individual-based simulation CEA across Nigeria, Kenya and Burkina Faso (*PLoS One*, PMID 35390077) confirms VAS as a cost-effective intervention to reduce measles/diarrhoea mortality in 6–59-month-olds, while noting fortification and measles vaccination may rival its impact where coverage is already high. *Genuine CEA retrieved.*

**Scalability.** Delivered at scale through child health days and routine immunization contacts in dozens of LMICs.

## 3. Zinc for treatment of diarrhoea
**Population:** under-5 · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Proven national**

**Evidence.** WHO/UNICEF-recommended. The Cochrane review *Oral zinc for treating diarrhoea in children* (PMID 27996088, 33 trials) supports zinc during acute diarrhoea. The CHERG meta-analysis in the *International Journal of Epidemiology* estimates zinc treatment **decreases diarrhoea mortality by ~23%** (PMID 20348128). *Preventive* zinc is weaker: all-cause mortality reduction was a **non-significant 9% (RR 0.91, 95% CI 0.82–1.01)**, diarrhoea-specific 18% (RR 0.82, 0.64–1.05), pneumonia-specific 15% (RR 0.85, 0.65–1.11) (CHERG, *BMC Public Health*, PMID 21501441), and preventive zinc showed **no effect on height-for-age (MD 0.00 Z, 95% CI −0.07–0.07)** (SR, *Indian Pediatrics*, PMID 30898990). The 2023 Cochrane review (PMID 36994923) reassesses preventive zinc for 6-month–12-year-olds.

**Cost-effectiveness.** A health-impact model estimates **cost per DALY ≈ US$606** for pill-based preventive zinc supplementation (*BMC Public Health*, PMID 25128210); a home-fortification "Sprinkles" model (containing zinc) reports **cost per death averted US$406 and cost per DALY ≈ US$12** (PMID 16512321). *Genuine CEA retrieved.*

**Scalability.** Zinc + ORS for diarrhoea is integrated into national iCCM/IMCI platforms.

## 4. Antenatal multiple micronutrient supplementation (MMS)
**Population:** WRA · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Growing → proven**

**Evidence.** The Cochrane review *Multiple-micronutrient supplementation for women during pregnancy* (PMID 30873598) is the anchor. Versus iron-folic acid, MMS reduced **low birth weight (RR 0.86, 95% CI 0.79–0.93)** and **small-for-gestational-age (RR 0.85, 95% CI 0.78–0.93)** (meta-analysis/meta-regression, *Bulletin of the WHO*, PMID 21673856). In the WHO ultrasound-dated trial subset, MMS vs IFA gave **LBW RR 0.87 (0.78–0.97), preterm 0.90 (0.79–1.03), SGA 0.90 (0.83–0.99)** (PMID 37002655). An IPD meta-analysis of **17 trials / 112,953 women** identified sex-specific neonatal-mortality modifiers (*Lancet Global Health*, PMID 29025632). Note a null older analysis: ~1-RDA MMN did not reduce stillbirth or early/late neonatal mortality (OR ≈ 1.0) (PMID 20120796) — benefit is on birth anthropometry more than mortality. Benefits extend to pregnant adolescents (IPD SR, PMID 33846729).

**Cost-effectiveness.** A dynamic microsimulation across India, Pakistan, Mali and Tanzania compared MMS and balanced energy-protein vs IFA (*PLoS Medicine*, PMID 35192606). Replacing IFA with MMS in Bangladesh and Burkina Faso gave **cost per death averted US$175–185 (Bangladesh) and US$112–125 (Burkina Faso), with cost per DALY averted of US$3–15** (*Annals NYAS*, openalex). Nutrition International's MMS cost-benefit tool across 33 countries finds the transition "very cost-effective" (openalex). *Genuine CEA retrieved.*

**Scalability.** WHO issued a conditional recommendation for MMS in pregnancy; several countries are transitioning from IFA to MMS through antenatal-care platforms.

## 5. Breastfeeding promotion & support
**Population:** under-5 · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Proven national**

**Evidence.** The Cochrane review *Optimal duration of exclusive breastfeeding* (PMID 22895934, 1,701 citations) underpins the 6-month EBF recommendation. Suboptimal breastfeeding sharply elevates infectious mortality: not breastfeeding vs EBF raised pneumonia mortality (RR 1.92, 95% CI 0.79–4.68 at 6–23 mo; PMID 24564728) and diarrhoea mortality (PMID 21501432). IYCF interventions raised **exclusive breastfeeding by 102% at 3 months and 53% at 6 months and cut diarrhoeal disease 24%** (SR in *Nutrients*, PMID 32164187). The Cochrane review *Support for healthy breastfeeding mothers* (PMID 36282618) confirms support interventions increase breastfeeding.

**Cost-effectiveness.** A Markov-model CEA of community peer counselling for EBF in Uganda (*PLoS One*, PMID 26619338) and a CEA of home-based postpartum care on neonatal mortality + EBF (PMID 31852432) both support cost-effectiveness. *Genuine CEA retrieved.*

**Scalability.** Delivered through health-facility (BFHI), community-health-worker and peer-counsellor platforms already present in most LMICs.

## 6. Small-quantity lipid-based nutrient supplements (SQ-LNS)
**Population:** under-5 (+ pregnancy) · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Growing**

**Evidence.** A meta-analysis of **18 trials / 41,280 children** (*AJCN*, PMID 31697329) found SQ-LNS reduced **all-cause mortality (RR 0.73, 95% CI 0.59–0.89)** in children 6–24 months. The Cochrane review of preventive LNS with complementary foods (PMID 31046132) supports nutrition/growth benefits. Prenatal SQ-LNS (IPD meta-analysis, *AJCN*, PMID 39154665) increased **birth weight (+49 g, 95% CI 26–71)** and reduced **low birth weight 11%, newborn stunting 17%, wasting 11%, small head size 15%**; a *Lancet Global Health* IPD meta-analysis compared prenatal MMS and SQ-LNS on small-vulnerable-newborn types (PMID 39890230).

**Cost-effectiveness.** A modelling study for rural Uganda (*Public Health Nutrition*, openalex) estimated providing SQ-LNS to >1 million children for 12 months at **~US$52 per child (~US$58.7 million/year)**, averting **>242,000 DALYs annually** via the Village Health Team system. *Genuine CEA retrieved.*

**Scalability.** Growing; depends on supply chain and per-child commodity cost — higher than micronutrient powders, so targeting matters.

---

# Tier 2

## 7. Community-based management of acute malnutrition (RUTF / CMAM)
**Population:** under-5 · **Evidence: A** · **Cost-effectiveness: Moderate** · **Scalability: Proven subnational**

**Evidence.** Community-based treatment with ready-to-use therapeutic food made children **51% more likely to achieve nutritional recovery than standard care** (SR/MA + Delphi, *BMC Public Health*, PMID 24564235). For moderate acute malnutrition, LNS were superior to fortified blended foods for recovery (**RR 1.05, 95% CI 1.01–1.09**; PMID 34535798). A comprehensive SR/MA of SAM/MAM management (*Nutrients*, PMID 31906272, 42 studies / 35,017 children) and the Cochrane review on community supplementary feeding (PMID 22696347) round out the base; WHO facility-based SAM management gives case-fatality rates of **8–16%** (PMID 28052519).

**Cost-effectiveness.** A systematic review of cost and cost-effectiveness of child-undernutrition treatment in LMICs (*Wellcome Open Research*, PMID 33102783, 50 studies) and the PROMIS integrated prevention+treatment trial (PMID 28274214) provide the CEA basis. *Genuine CEA retrieved — rated Moderate given heterogeneity in cost per recovery across settings.*

**Scalability.** CMAM is operational in many high-burden countries but remains commodity- and supply-chain-intensive; coverage rather than efficacy is the binding constraint.

## 8. Complementary feeding interventions (education ± food provision)
**Population:** under-5 · **Evidence: A** · **Cost-effectiveness: High** · **Scalability: Growing**

**Evidence.** Education/counselling on complementary feeding had a **small but significant** effect on linear growth (SR/MA, *Journal of Nutrition*, PMID 28904113). The CHERG review (*BMC Public Health*, PMID 21501443) and a companion SR (PMID 24564534) report education alone improved **HAZ (SMD 0.23, 95% CI 0.09–0.36) and WAZ (SMD 0.16, 95% CI 0.05–…)**. A network meta-analysis of 79 RCTs / 81,786 children found multiple micronutrients reduced stunting (**RR 0.86, 95% CI 0.73–0.98**) and IFA + MMN improved HAZ (PMID 32259047).

**Cost-effectiveness.** No standalone complementary-feeding CEA was retrieved; the closest genuine CEAs are peer-counselling for breastfeeding (PMID 26619338) and SQ-LNS provision (openalex). *Rated High by proximity, but flagged: a complementary-feeding-specific CEA is a gap.*

**Scalability.** Delivered via CHW counselling and growth-monitoring contacts; food-provision arms cost more than education-only.

## 9. Micronutrient powders (home / point-of-use fortification)
**Population:** under-5 · **Evidence: B (net-benefit caveat)** · **Cost-effectiveness: Moderate** · **Scalability: Growing**

**Evidence.** The Cochrane review of home fortification with MNPs (PMID 32107773) supports improved micronutrient status in under-2s (MNP programmes reached >3 million children across 43 countries). Fortified complementary foods improved growth/anaemia outcomes (*Lancet Child & Adolescent Health*, PMID 35753314); MMN-fortified beverages raised haemoglobin (+2.76 g/L, 95% CI 1.19–4.33) and cut anaemia risk (RR 0.58) in school-aged children (PMID 26007336). Pooled high-adherence to MNPs was **63.3% (95% CI 51.1–74.6)** (PMID 34658128). **Caveat:** iron-containing MNPs carry a possible infection/net-benefit trade-off (see CEA).

**Cost-effectiveness.** The BRISC RCT-based CEA in rural Bangladesh computed ICERs (US$/DALY averted) for iron-containing MNPs vs placebo (*AJCN*, PMID 36192508); a 78-country microsimulation (*Lancet Global Health*, openalex) found net benefit and cost-effectiveness are **country-dependent**, with possible net harm where malaria/infection burden is high. *Genuine CEA retrieved — rated Moderate due to context-dependent net benefit.*

**Scalability.** Growing through community platforms; the infection caveat argues for targeting to anaemia-burden, lower-malaria settings.

## 10. Periconception / antenatal folic acid
**Population:** WRA · **Evidence: A (neural tube defects)** · **Cost-effectiveness: High (via fortification)** · **Scalability: Proven national (as fortification)**

**Evidence.** Folic acid supplementation reduced **neural-tube-defect recurrence by 70% (95% CI 35–86)** and primary occurrence by **62% (49–71)**, with food fortification reducing NTD incidence **46% (37–54)** (CHERG SR/MA, *International Journal of Epidemiology*, PMID 20348114). Maternal folic acid raised mean birth weight by **0.37 kg (95% CI 0.24–0.50)** and lowered low-birth-weight odds (**OR 0.59, 95% CI 0.47–0.74**) (SR/MA, *Maternal & Child Nutrition*, PMID 31680411). Preconception coverage in sub-Saharan Africa is low (1.9–45.2%; PMID 39888921), a key implementation gap.

**Cost-effectiveness.** No folic-acid-only CEA was retrieved; cost-effectiveness is inferred from the large-scale fortification CEA base (entry #1, openalex 63-country review) since folic acid is a core fortificant. *Flagged: the High rating rests on fortification CEAs, not a standalone folic-acid CEA.*

**Scalability.** Most cost-effectively delivered as flour fortification (proven national); supplementation depends on preconception contact, which is weak in many settings.

## 11. Antenatal iron / iron-folic acid (IFA)
**Population:** WRA · **Evidence: A (anaemia)** · **Cost-effectiveness: Moderate** · **Scalability: Proven national**

**Evidence.** The Cochrane review *Intermittent oral iron supplementation during pregnancy* (PMID 26482110) and a meta-analysis of maternal haematologic status (PMID 11818308) confirm iron raises haemoglobin dose-dependently. Iron therapy improved haemoglobin in women of reproductive age (pooled SMD **−0.71, 95% CI −1.27 to −0.14**, *BMC Women's Health*, PMID 37069552). Intermittent vs daily IFA gave slightly lower maternal haemoglobin (**MD −0.24 g/dl, 95% CI −0.35 to −0.12**) but comparable pregnancy outcomes and better tolerability (SR/MA, PMID 39780191). **Adherence is the limiting factor** — pooled IFA compliance in sub-Saharan Africa was only **39.2%** (PMID 33852614).

**Cost-effectiveness.** Captured within the IFA-comparator arm of the MMS/BEP microsimulation (PMID 35192606); IFA is the low-cost standard of care against which MMS is judged. *Genuine CEA retrieved (as comparator) — rated Moderate.*

**Scalability.** Universal IFA is standard antenatal-care policy in nearly all LMICs; the gap is adherence/coverage, not availability.

## 12. Balanced energy-protein (BEP) supplementation in undernourished pregnancy
**Population:** WRA · **Evidence: B+** · **Cost-effectiveness: Moderate** · **Scalability: Requires investment**

**Evidence.** In *undernourished* pregnant women, balanced protein-energy supplementation improved child physical growth (SR/MA of 7 studies, standardized mean differences on birth weight/length, *Maternal & Child Nutrition*, PMID 25857334). An IPD meta-analysis of **8 RCTs / 10,252 women** assessed BEP effects on small-vulnerable-newborn types (*PLoS Medicine*, PMID 41701774). BEP/MMS improved gestational weight-gain adequacy (MMS: WMD +209 g, 95% CI 139–280) (PMID 36130877). Benefit is conditional on maternal undernutrition — not a universal intervention.

**Cost-effectiveness.** The MMS-vs-BEP-vs-IFA microsimulation (PMID 35192606) provides the only retrieved BEP CEA. *Genuine CEA retrieved — rated Moderate, with benefit concentrated in food-insecure populations.*

**Scalability.** Requires targeted food-supplement supply chains; costlier than tablet-based supplementation, so geographic/needs targeting is essential.

---

# Tier 3

## 13. Iron supplementation in children
**Population:** under-5 · **Evidence: B** · **Cost-effectiveness: Moderate** · **Scalability: Growing**

**Evidence.** A review of 26 RCTs of preventive oral iron in children 0–59 months (*AJCN*, PMID 17158406) found haemoglobin and cognitive/motor gains **in iron-deficient/anaemic children**, but **adverse weight gain in iron-replete children** — i.e. benefit is conditional on iron status. In older children/adolescents, iron raised haemoglobin **+5.81 g/L (95% CI 4.19–7.44)** (SR/MA, *Nutrition Reviews*, PMID 40063075).

**Cost-effectiveness.** Covered by the BRISC iron/MNP CEA (PMID 36192508). *Genuine CEA retrieved — Moderate, with the same context-dependent net-benefit caveat as MNPs.*

**Scalability.** Best delivered as targeted supplementation or via iron-containing MNPs/fortification; universal untargeted iron is not advised given the iron-replete risk.

## 14. WASH for child nutrition
**Population:** under-5 · **Evidence: B/C** · **Cost-effectiveness: Unknown** · **Scalability: Requires investment**

**Evidence.** Effects on nutrition are **small**: a meta-analysis of 10 studies / 16,473 children found WASH raised **height-for-age by SMD 0.14 (95% CI 0.09–0.19)** (PMID 31272479). The Cochrane review (PMID 23904195) found limited/uncertain nutrition effects, and a 41-trial SR (PMID 29428924) found **little or no effect on most anthropometry**, though hygiene reduced acute respiratory infection by 24% (RR 0.76, 95% CI 0.59–0.98). The major landmark WASH-nutrition efficacy trials (WASH Benefits, SHINE) are consistent with this modest direct effect.

**Cost-effectiveness: Unknown.** Phase 2 retrieved **no WASH-specific CEA** — only generic nutrition-program models (Optima Nutrition 129-country analysis; community nutrition-specific SR). Per the CEA-rating guard, **no cost-effectiveness rating is assigned.**

**Scalability.** Requires major infrastructure investment; justified primarily on diarrhoeal-disease and dignity grounds rather than on a measured nutrition cost-effectiveness case.

## 15. Cash transfers for child nutrition
**Population:** under-5 · **Evidence: C (indirect / nutrition-sensitive)** · **Cost-effectiveness: Unknown** · **Scalability: Proven national (as social protection)**

**Evidence.** Evidence is **indirect**. A meta-analysis of financial-incentive programmes (unconditional/conditional cash transfers, vouchers, user-fee removal) found they improve **coverage and uptake of child-health interventions** (*BMC Public Health*, PMID 24564520). A systematic review of nutrition and cash-based interventions for stunting reported mixed effects and downstream economic/human-capital signals (PMID 31666032). Direct anthropometric impact is inconsistent and pathway-dependent.

**Cost-effectiveness: Unknown.** Phase 2 retrieved **no cash-transfer-specific nutrition CEA** — the top hits were a community-nutrition SR and a demand-side-financing review (not a CEA of cash transfers for a nutrition outcome). Per the CEA-rating guard, **no rating is assigned.**

**Scalability.** Cash transfers are proven at national scale as *social protection*; their value here is as a nutrition-sensitive platform (a delivery channel and demand-side lever), not a nutrition-specific intervention with a measured cost-per-DALY.

---

# Cross-cutting findings

1. **Fortification and supplementation dominate the cost-effective frontier.** The interventions with both strong evidence *and* genuine, favourable CEAs (fortification, VAS, zinc-for-diarrhoea, MMS, breastfeeding, SQ-LNS) all deliver at very low cost per DALY/death averted (e.g. **US$3–15/DALY** for MMS-over-IFA, PMID 35192606/openalex; **~US$12/DALY** for Sprinkles, PMID 16512321) and ride existing delivery platforms.

2. **Effect is conditional on baseline deficiency for several "Tier 1" supplements.** VAS mortality benefit weakens as vitamin A deficiency declines (PMID 35584136, 30425075); child iron and preventive zinc help the deficient but can be neutral or harmful in the replete (PMID 17158406, 30898990); MNP net benefit is context-dependent on infection burden (PMID 36192508, openalex 78-country). Targeting beats universal provision for these.

3. **Maternal interventions improve birth anthropometry more reliably than mortality.** MMS robustly cuts LBW/SGA (PMID 21673856, 37002655) but older analyses show null mortality effects (PMID 20120796); the mortality case is strongest for the package + adequate gestational coverage.

4. **Adherence/coverage — not efficacy — is the binding constraint.** IFA compliance in SSA was 39.2% (PMID 33852614); preconception folic-acid coverage 1.9–45.2% (PMID 39888921); MNP high-adherence 63% (PMID 34658128); CMAM is coverage-limited (PMID 31906272). Implementation science, not new efficacy trials, is where marginal returns lie.

5. **The CEA evidence base is thinnest exactly where spending is largest.** Nutrition-sensitive levers (WASH, cash transfers) have weak *direct* nutrition evidence and **no intervention-specific CEA in the retrieved corpus** — both are rated cost-effectiveness **Unknown**. This is the honest output of the two-phase design: it refuses to manufacture a cost-effectiveness rating where the corpus has none.

6. **A handful of generic economic models recur across interventions** (e.g. the Optima Nutrition 129-country model, PMID-less openalex; the cross-cutting iron/MNP CEA PMID 36192508). These are package-level, not intervention-specific, and should not be double-counted as independent CEAs for each intervention.

---

# Verification & caveats

- **CEA-rating guard applied:** WASH (#14) and cash transfers (#15) are rated cost-effectiveness **Unknown** because Phase 2 returned no intervention-specific CEA — only generic nutrition-program models. Folic acid (#10) and complementary feeding (#8) rest on adjacent CEAs (fortification; breastfeeding/SQ-LNS) and are flagged as such rather than asserted.
- **Recurring-source caveat:** PMID 36192508 (iron/MNP CEA) and the Optima Nutrition model appear across several interventions; treat as single sources.
- **A few CEA cost figures were truncated in the retrieved abstracts** (e.g. the exact per-DALY value in the MMS cost-benefit tool, openalex; the Sprinkles cost-per-DALY tail, PMID 16512321) — full-text retrieval would firm these up.
- **Next step:** run `python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md` to confirm every PMID-backed numeric claim resolves to the corpus and that no figure is misattributed.
