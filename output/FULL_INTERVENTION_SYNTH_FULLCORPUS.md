# Nutrition Intervention Synthesis — Full-Corpus Run

*Children under 5 and women of reproductive age (WRA) in LMICs. Interventions rated on evidence strength, cost-effectiveness, and scalability, and tiered accordingly.*

## How this was produced

This synthesis scales the pipeline beyond the original top-200 review to a **1,000-paper working set** drawn from the full corpus of 1,996 retrieved papers. Pipeline: (1) retrieve evidence (PubMed + OpenAlex, population-targeted); (2) **full-text retrieval for the whole corpus** — 1,378/1,996 (69%) via PMC (PMID *and* DOI→PMCID) with an Unpaywall→PDF fallback; (3) **per-study structured extraction** into an evidence database (study design, population, effect sizes with CIs, included trials, dominant trial, Cochrane accession) via a fan-out of extraction agents; (4) cap to a **1,000-paper set selected independently of the relevance ranking** (592 already-extracted + 408 uniformly random, seed 20260709); (5) **per-intervention synthesis** grounded in the extraction DB + Phase-2 CEA, one agent per intervention, under the standing grounding rules (corpus citation on every number, verbatim study type, all-cause vs cause-specific split, fixed/random + dominant trial, version≠evidence, CEA-rating guard); (6) automated claim verification.

**23 interventions** met the evidence threshold for a full section. Cost-effectiveness is rated **only** where a Phase-2 CEA record exists (`cea_rating_allowed`), else **Unknown**.

## Summary table

| Tier | Intervention | Population | Evidence | Cost-effectiveness | Scalability | Papers |
|------|--------------|-----------|:--------:|:-----------------:|-------------|:------:|
| 1 | Breastfeeding promotion and support | women of reproductive age & children under 5 | A | High | Proven national | 48 |
| 1 | Complementary Feeding Interventions — education/counselling + food supplementation for children 6–23 months | children under 5; some maternal/IYCF overlap | A | High | Proven subnational | 27 |
| 1 | Large-Scale Food Fortification of Staple Foods & Condiments | children under 5 & women of reproductive age, LMIC | A | Very High | Proven national | 23 |
| 1 | Antenatal Multiple Micronutrient Supplementation (MMS) | Women of reproductive age / pregnant women; child birth outcomes | A | Very High | Requires investment (WHO-recommended, national transitions underway) | 9 |
| 1 | Zinc supplementation in children | children under 5; one review spans WRA/adults | A | High | Growing | 9 |
| 1 | Vitamin A supplementation in children 6–59 months | children under 5 | A | Moderate | Proven national | 6 |
| 1 | Community-Based Management of Acute Malnutrition (CMAM) — SAM & MAM treatment | children under 5, 6–59 months | B | Very High | Proven national | 11 |
| 1 | Periconception & Antenatal Folic Acid (and Iron-Folic Acid) Supplementation | Women of reproductive age / periconception & pregnancy, LMIC | B | Very High | Proven national | 2 |
| 2 | Cash Transfers for Child & Maternal Nutrition (conditional & unconditional) | children under 5 & women of reproductive age | A | Moderate | Proven national | 71 |
| 2 | Multiple micronutrient supplementation & fortification for children under 5 and pregnant women | both under-5 and WRA | A | Unknown | Growing | 9 |
| 2 | Balanced Energy-Protein (BEP) Supplementation in Pregnancy | women of reproductive age; offspring birth outcomes | A | High | Requires investment | 6 |
| 2 | Small-Quantity Lipid-Based Nutrient Supplements (SQ-LNS) | children under 5 & women of reproductive age, LMIC | A | High | Requires investment | 6 |
| 2 | Multisectoral & nutrition-sensitive intervention packages | children under 5 & women of reproductive age | B | Unknown | Growing | 43 |
| 2 | Maternal Nutrition — Antenatal Supplementation, Counselling & Preconception Care | women of reproductive age; some infant/child outcomes | B | Unknown | Requires investment | 42 |
| 2 | Nutrition-sensitive social protection (cash/food transfers, maternity protection, wage & safety-net policy) | children under 5 & women of reproductive age | B | Unknown | Proven national | 17 |
| 2 | Iron supplementation / iron-containing interventions for young children | children under 5; some records also cover WRA | B | Moderate | Requires investment | 12 |
| 2 | Antenatal Iron-Folic Acid (IFA) Supplementation | Women of reproductive age / pregnant women | B | High | Proven national | 11 |
| 2 | Multiple Micronutrient Powders (MNP) — home / point-of-use fortification | children under 5, esp. 6–23 months | B | Moderate | Growing | 3 |
| 3 | Nutrition-Sensitive Agriculture & Food Systems | children under 5 & women of reproductive age, LMIC | B | Unknown | Requires investment | 30 |
| 3 | Water, Sanitation and Hygiene (WASH) interventions for child nutrition | children under 5; some maternal/WRA evidence | B | Moderate | Requires investment | 5 |
| 3 | Growth Monitoring and Promotion (GMP) | children under 5 | C | Unknown | Growing | 4 |
| 3 | School Feeding / Publicly Procured School Meals | children under 5 via intergenerational pathway; school-age children 5–18; women of reproductive age as future mothers | C | Unknown | Proven national | 3 |
| 3 | Vitamin D supplementation for children under 5 (and status in WRA) | children under 5; women of reproductive age | C | Unknown | Requires investment | 3 |


# Tier 1 — Strong evidence, cost-effective, scalable now

## Breastfeeding promotion and support  (women of reproductive age & children under 5)
**Evidence: A  |  Cost-effectiveness: High  |  Scalability: Proven national  |  Tier 1**

- **Evidence base:** The bundle holds 48 records for this intervention: 13 meta-analyses, 20 systematic reviews, 8 other reviews, 5 observational studies, and 2 other designs. Three are Cochrane reviews with distinct Cochrane IDs — CD001141 (breastfeeding support, PMID 36282618), CD003519 (skin-to-skin contact, PMID 41120189), CD001688 (breastfeeding initiation, PMID 27827515) — so they represent three separate reviews and are counted once each (no shared-`cochrane_id` version collapse needed). The effectiveness signal is consistent across multiple meta-analyses and Cochrane reviews for the proximal outcomes (breastfeeding initiation, exclusivity, and duration), supporting an **A** grade. GRADE certainty is moderate for the flagship support and skin-to-skin outcomes and low-to-very-low for initiation-promotion pooled effects (see below).

- **Effect sizes:**

  *Support / counselling (proximal breastfeeding outcomes)* — Cochrane review "Support for healthy breastfeeding mothers with healthy term babies" (Systematic review & meta-analysis / Cochrane Database of Systematic Reviews, PMID 36282618, 116 trials, 98,816 mother–infant pairs). "Breastfeeding only" support reduced cessation of any breastfeeding at 6 months RR 0.93 (95% CI 0.89–0.97) and exclusive breastfeeding at 6 months RR 0.90 (0.88–0.93); at 4–6 weeks, any breastfeeding RR 0.88 (0.79–0.97) and exclusive RR 0.83 (0.76–0.90); "breastfeeding plus" support reduced stopping exclusive breastfeeding at 6 months RR 0.79 (0.70–0.90). Moderate-certainty GRADE for the primary outcomes; other "plus"/secondary outcomes uncertain.

  *Skin-to-skin contact* — Cochrane review (Systematic review & meta-analysis / Cochrane Database of Systematic Reviews, PMID 41120189). Exclusive breastfeeding at hospital discharge–1 month RR 1.36 (95% CI 1.19–1.56; random-effect; 12 studies, n=1,556) and at 6 weeks–6 months RR 1.38 (1.09–1.74; random-effect; 11 studies, n=1,135). Infant axillary temperature MD +0.28 °C (0.14–0.41) and blood glucose MD +10.49 mg/dL (8.39–12.59; fixed-effect). Moderate certainty for exclusive breastfeeding, temperature, and glucose; low-to-very-low for maternal blood-loss/placental-separation outcomes.

  *Breastfeeding initiation* — Cochrane review "Interventions for promoting the initiation of breastfeeding" (Cochrane review, PMID 27827515). Healthcare-professional-led education/support RR 1.43 (95% CI 1.07–1.92; 5 studies, n=564); non-healthcare-professional-led RR 1.22 (1.06–1.40; 8 studies, n=5,712); early initiation within 1 hour (non-professional-led) RR 1.70 (0.98–2.95; 3 studies, n=76,373 — CI crosses 1). GRADE low-to-very-low.

  *Early initiation, South Asia* — Systematic review & meta-analysis (PMID 40426155). Overall RR 1.55 (95% CI 1.24–1.95; random-effect; 19 studies); health-system-strengthening RR 2.76 (1.96–3.88); behavioural RR 1.48 (1.14–1.93); mHealth RR 1.08 (0.97–1.20; non-significant). **Dominant trial:** Bhandari 2012 / Taneja 2015 India IMNCI health-system trial (~29,589 intervention vs ~30,604 control; OR 5.21, 4.33–6.28). Heterogeneity I²=99.56%; moderate GRADE (downgraded for risk of bias, inconsistency, small-study effects).

  *Overview of SRs (initiation/exclusivity)* — Systematic review (PMID 36761137): community-based intervention packages by ancillary nurse-midwives RR 1.93 (1.55–2.39; 11 studies, n=72,464); community health educational interventions RR 1.56 (1.37–1.77; 19 studies, n=126,375).

  *Support packages in LMIC (<6 months)* — Systematic review, vote-counting synthesis (PMID 33672692): share of comparisons favouring intervention for exclusive breastfeeding — promotion 100% (95% CI 56–100; 5 studies), education 80% (49–94; 10 studies), counselling 58% (31–80; 12 studies), training 55% (26–81; 9 studies). Not GRADE-rated.

  *Distal / clinical outcomes (all-cause vs cause-specific — kept separate and flagged as thinner):*
  - Home-based postpartum care package (co-delivering EBF promotion): **all-cause neonatal mortality** RR 0.76 (95% CI 0.62–0.92; random-effect; 9 trials, n=93,083; PMID 31852432) and exclusive breastfeeding OR 2.88 (1.57–5.29; 6 trials, n=20,624). GRADE moderate (mortality) / high (EBF). Note this is a bundled home-visit package, not breastfeeding support in isolation.
  - **RSV lower-respiratory infection** (cause-specific; observational only, no RCTs, variable quality — underpowered/indirect): individual-study estimates only, e.g. RSV bronchiolitis hospitalisation OR 0.21 (0.06–0.79; Linstow, Denmark, n=200) and oxygen-therapy requirement OR 0.256 (0.074–0.892; Jang, South Korea, n=203); no pooled effect (PMID 36746518). **Flagged as underpowered/indirect.**
  - **HIV-exposed dyads:** exclusive breastfeeding uptake with MCH support RR 1.38 (95% CI 1.06–1.80; random-effect; 8 studies, n=3,481); GRADE very low; I²=62.5%; **dominant trial** Suryavanshi 2022 (n=1,191). Peer-support subgroup for any breastfeeding RR 1.00 (0.78–1.28), non-significant (PMID 40850640).
  - **Asthma/allergy** (PMID 26192405) and **cognition/educational attainment** (PMID 36057881): low-quality, mostly cross-sectional; no usable pooled measure with CI in corpus for these — **treated as indirect, not evidence of a mortality/morbidity benefit.**

  *Context / prevalence (not effect estimates):* pooled exclusive-breastfeeding prevalence 43% (95% CI 34–53; PMID 37269619) and 50% (41–60; Ghana, PMID 37208682) — both well below the 70% World Health Assembly target, indicating large headroom.

- **Mechanism of action:** Exclusive and early breastfeeding delivers optimal infant nutrition and passive/active immune protection, reducing gastrointestinal and respiratory infection; early initiation (skin-to-skin, within 1 hour) improves thermoregulation (temperature MD +0.28 °C) and glucose stability (MD +10.49 mg/dL) and establishes lactation. Support/counselling and skin-to-skin act on the behavioural and physiological determinants of initiation, exclusivity, and duration — the pathway upstream of the infection and mortality outcomes.

- **Cost-effectiveness:** `cea_rating_allowed` is **true** (132 CEA papers retrieved; 0 registry matches). Grounded estimates in the CEA set: community-based peer counselling in Uganda ICER US$11,353 per DALY averted and US$68 per additional month of exclusive/predominant breastfeeding (PMID 26619338) — the authors judged it unlikely to be cost-effective specifically for reducing *diarrhoea*, but cost-effective for raising breastfeeding prevalence; the home-based postnatal package co-delivering EBF cost US$103.44 per DALY averted and US$2,939 per neonatal death averted in Bangladesh (LeFevre 2013, within PMID 31852432); telephone-based peer support (RUBY RCT, Australia) ICER A$4,146 per additional mother breastfeeding at 6 months (A$1,393 excluding donated volunteer time; OpenAlex W4379875208); and a narrative CEA review found peer support cost £19–£107 per additional month of exclusivity (OpenAlex W3109666226). Estimates are heterogeneous and outcome-dependent (very favourable for breastfeeding/neonatal-survival endpoints, less so for single-disease endpoints like diarrhoea), so the rating is **High** rather than Very High.

- **Government scaling pathway:** Strong platform fit. Delivers through existing maternal-and-child-health touchpoints — antenatal care, facility delivery and immediate postnatal care (skin-to-skin, early initiation), and community health workers / peer counsellors for post-discharge support. The health-system-strengthening arm (IMNCI, dominant Taneja/Bhandari India trial) and community-based packages by nurse-midwives (RR 1.93) show the effect is realised at national/programmatic scale, and the Baby-Friendly Hospital Initiative (PMID 26924775) and "breastfeeding gear" scale-up model (PMID 23153733) are established national delivery vehicles — supporting **Proven national** scalability. Complementary policy levers appear in the corpus: paid maternity leave ≥6 months and Code enforcement on breastmilk-substitute marketing (PMIDs 37208682, 42031488, 44).

- **Caveats:**
  - *Version vs evidence:* the three Cochrane reviews carry distinct IDs (CD001141, CD003519, CD001688) and are counted once each; no version double-counting.
  - *All-cause vs cause-specific:* the robust signals are proximal/behavioural (initiation, exclusivity, duration) and, in a bundled package, all-cause neonatal mortality (RR 0.76). Cause-specific pathways (RSV, diarrhoea, asthma/allergy, cognition) are underpowered, observational, or indirect and should not be presented as established mortality/morbidity effects.
  - *Heterogeneity:* very high for initiation meta-analyses (I²=99.56% South Asia; I²=62.5% HIV), with single trials dominating pooled estimates (Taneja/Bhandari India; Suryavanshi 2022 HIV) — pooled point estimates should be read with the dominant-trial context.
  - *Attribution:* the strongest mortality/CEA numbers (PMID 31852432) come from home-visit packages that co-deliver EBF alongside other newborn-care components; the breastfeeding-specific contribution is not isolated.
  - *CEA outcome-dependence:* cost-effectiveness verdicts flip with the chosen endpoint (favourable for breastfeeding-months / neonatal survival; unfavourable for diarrhoea alone in the Uganda analysis).

## Complementary Feeding Interventions — education/counselling + food supplementation for children 6–23 months  (children under 5; some maternal/IYCF overlap)

**Evidence: A  |  Cost-effectiveness: High  |  Scalability: Proven subnational  |  Tier 1**

- **Evidence base:** The bundle holds 27 records for this intervention (tiers: 4 meta-analyses, 11 systematic reviews, 3 other reviews, 1 RCT, 5 observational/cross-sectional, 3 other). The core effectiveness question — does improving the 6–23-month diet improve growth — is anchored by **multiple, consistent systematic reviews and meta-analyses that converge on a small-but-significant positive effect on linear growth**, which is why the evidence grade is A. The strongest, most directly on-point records are the Panjwani & Heidkamp CHERG/LiST meta-analysis (PMID 28904113, *The Journal of Nutrition* 2017, "Systematic Review & Meta-Analysis"), the Lassi et al. education-and-provision review (PMID 24564534, *BMC Public Health* 2013, "Systematic Review"), and an IYCF systematic review (PMID 32164187, *Nutrients* 2020, "Systematic Review"). Food-specific meta-analyses (egg — PMID 42137196; early-life protein — PMID 41338694) qualify and refine the picture. GRADE/certainty ratings are not stated verbatim in these records; effects are consistently described as "small but significant."

- **Effect sizes** (all growth outcomes are continuous z-score effects; there is no all-cause-mortality pooled estimate in this bundle, so the all-cause vs cause-specific split does not arise for the growth records — the one mortality-adjacent figure is a stunting-incidence RR, flagged below):
  - **Nutrition education/counselling → linear growth (LAZ):** SMD **0.11 (95% CI 0.01, 0.22)** in food-secure populations; no significant effect on ponderal growth (WLZ) (PMID 28904113).
  - **Complementary-food supplementation (± education) → growth in food-insecure settings:** LAZ SMD **0.08 (95% CI 0.04, 0.13)** and WLZ SMD **0.05 (95% CI 0.01, 0.08)** (PMID 28904113).
  - **Education on complementary feeding alone (Lassi review):** HAZ SMD **0.23 (95% CI 0.09, 0.36)**, WAZ SMD **0.16 (95% CI 0.05, 0.27)**, and a significant reduction in stunting **RR 0.71 (95% CI 0.56, 0.91)** (PMID 24564534). No significant impact on absolute height/weight gain.
  - **IYCF review (descriptive pooled shifts, certainty limited):** complementary-feeding education → +0.41 SD WAZ and +0.25 SD HAZ (food-secure); complementary-food provision ± education → +0.14 SD HAZ and 36% decrease in stunting; supplementary food → +0.15 SD WHZ (PMID 32164187). These are single-review descriptive estimates, not independent pooled CIs, and the authors state evidence for growth outcomes is "limited."
  - **Egg-based supplementation (SSA, 7 RCTs, 3,673 children):** significant improvement in **WAZ MD 0.33 (95% CI 0.11, 0.55)** and **WHZ MD 0.30 (95% CI 0.12, 0.48)**, but **no effect on linear growth: HAZ MD 0.05 (95% CI −0.05, 0.14)** (PMID 42137196). Heterogeneity was high (I² = 93% for WAZ; ~89% for WHZ per full text), with Ethiopia studies and longer (24-month) durations driving larger effects; Egger's test/funnel plot suggested some publication bias.
  - **Early-life protein supplementation → obesity/body composition:** null. WLZ SMD **0.0 (95% CI −0.09, 0.09)** in LMICs and **0.17 (95% CI −0.12, 0.47)** in HICs; fat-free mass SMD −0.05 (95% CI −0.31, 0.21); fat mass SMD 0.17 (95% CI −0.41, 0.74) (PMID 41338694). Interpreted as: complementary-feeding protein quantity/source does not drive later obesity — reassuring, not a growth-benefit claim.

- **Mechanism of action:** From 6 months, breast milk alone no longer meets energy/protein/micronutrient needs; the 6–23-month window is the critical growth-faltering period (PMID 24564534). Two mechanistic levers: (1) behaviour-change **education/counselling** improves diet quality, frequency, diversity, and hygiene using foods already in the home (effective mainly where food is available, i.e. food-secure settings); (2) **direct food/supplement provision** (fortified blended foods, animal-source foods such as eggs, SQ-LNS) fills an absolute nutrient gap where diets are insufficient (food-insecure settings). The evidence shows the effective lever depends on food security — education where food is available, provision where it is not.

- **Cost-effectiveness:** cea_rating_allowed is **true** (141 CEA papers retrieved, 0 registry matches). Grounded ICERs from the CEA record:
  - **SQ-LNS, rural Uganda:** ~$52 per child for 12 months via the existing Village Health Team platform; **~$242 per DALY averted** (>242,000 DALYs/yr, 3,689 deaths averted), described as potentially more cost-effective than micronutrient powders or complementary-food provision (OpenAlex W4386045834, *Public Health Nutrition* 2023).
  - **Community-based prevention/treatment of acute malnutrition, Indian urban slums (ICDS Anganwadi platform):** **$23 per DALY averted (95% UI 19–28)** — "highly cost-effective" (OpenAlex W2900168001, *PLoS ONE* 2018).
  - **Market-based home fortification with micronutrient powder, Bangladesh:** **$159.3 (12,558 BDT) per DALY averted**, "highly cost-effective" vs the ~$1,516 GDP-per-capita threshold (OpenAlex W3096300085, *Public Health Nutrition* 2020).
  - **Price subsidies on fortified packaged complementary foods, Pakistan:** net cost per DALY ranging from a $783 cost to a **$65 return per DALY averted**, most cost-effective when targeted at poorer households (OpenAlex W2884580373, *Public Health Nutrition* 2018).
  These sit well below common LMIC willingness-to-pay thresholds, supporting a **High** rating (not "Very High": the estimates are model-based, delivery-mode-specific, and vary by product/setting; the largest impacts come at high total programme cost).

- **Government scaling pathway:** Strong platform fit. The CEA studies were modelled or run on **existing government delivery systems** — India's ICDS/Anganwadi network and Uganda's Village Health Team community-health-worker system — rather than standalone verticals, which is the realistic route to national scale. Education/counselling integrates into routine antenatal, immunisation, and growth-monitoring contacts and community-health-worker home visits; food/SQ-LNS provision requires supply-chain and financing investment but can ride the same platforms. Effectiveness is materially higher when delivered by trained/healthcare-professional-led workers (PMID 32164187). Classified **Proven subnational** (documented at scale in ICDS and CHW programmes; not yet a single proven national complementary-feeding programme in the corpus).

- **Caveats:**
  - **Effect sizes are small** (LAZ SMDs 0.08–0.23); complementary feeding shifts the growth distribution modestly rather than eliminating stunting, and both anchor reviews call for large high-quality RCTs (PMID 28904113, PMID 24564534).
  - **Food security is an effect modifier, not noise:** education works in food-secure settings; provision is needed in food-insecure settings. Pooling across contexts masks this — report subgroup, not overall, estimates.
  - **Heterogeneity is high** for the food-specific meta-analyses (egg I² = 93%, with possible publication bias; PMID 42137196).
  - **Outcome specificity:** eggs improved weight (WAZ/WHZ) but **not** linear growth (HAZ); protein supplementation was null for both growth and later obesity. Growth-outcome evidence is described as "limited" in the IYCF review (PMID 32164187) even where breastfeeding-outcome evidence is strong.
  - **Version/overlap:** these reviews share the LiST/CHERG evidence lineage (PMID 28904113 explicitly updates the prior LiST review; PMID 24564534 also feeds LiST), so they partly overlap in included trials and should not be treated as fully independent replications. No shared cochrane_id was flagged in the bundle, and no single dominant trial (DEVTA-analogue) is identified in these records.
  - Several bundle records are off-target for the intervention itself (dietary-exposure/dental-caries reviews, qualitative syntheses, women's-empowerment determinants) and were not used for effect estimates. The JAMA allergenic-food-timing meta-analysis (record 24) and the Cochrane fruit/vegetable review (record 22) carry no abstract or effect numbers in this bundle (not in corpus), so no figures are drawn from them.

## Large-Scale Food Fortification of Staple Foods & Condiments (children under 5 & women of reproductive age, LMIC)

**Evidence: A  |  Cost-effectiveness: Very High  |  Scalability: Proven national  |  Tier 1**

Scope note: "food fortification" in this bundle spans several vehicles (wheat/maize flour, rice, salt, condiments/seasonings, oils, sugar, milk/cereal foods, non-dairy beverages, fortified complementary foods, and fortified blended food aid) and several nutrients (iron, vitamin A, zinc, iodine, folic acid, multiple micronutrients). Evidence and cost-effectiveness vary by nutrient-vehicle pairing; ratings below are anchored to the strongest micronutrient-status outcomes (anaemia/iron, iodine, folate/NTDs), which are consistently supported, and are explicitly hedged for the outcomes that are not (growth, cause-specific morbidity/mortality).

### Evidence base
The bundle contains 23 records, of which the core intervention evidence is **3 Cochrane reviews / meta-analyses and 4 other systematic-reviews-with-meta-analysis, plus 1 narrative review** on fortified food aid. The remaining records are observational/food-security or modeling papers that describe determinants and context rather than the intervention itself, and are not used for effect estimates.

Core evidence records (study type stated verbatim from each record):
- **Cochrane review** — Fortification of condiments and seasonings with iron (PMID 37665781, *The Cochrane database of systematic reviews*, 2023; 16 RCTs; GRADE very low to moderate; all 16 studies at overall high risk of bias).
- **Cochrane review** — Fortification of staple foods with vitamin A (PMID 31074495, *The Cochrane database of systematic reviews*, 2019; cochrane_id CD010068; 10 RCTs, 4,455 participants; GRADE very low to moderate).
- **Meta-analysis** (Cochrane) — Fortification of staple foods with zinc (PMID 27281654, *The Cochrane database of systematic reviews*, 2016; cochrane_id CD010697; 8 trials, 709 participants; GRADE low to very low).
- **Systematic Review & Meta-Analysis** — Micronutrient-fortified complementary foods, infants 6–23 months (PMID 35753314, *The Lancet. Child & adolescent health*, 2022; WHO-commissioned, PROSPERO CRD42021245876; 16 RCTs/CCTs; GRADE moderate for anaemia/haemoglobin/growth/retinol).
- **Systematic review & meta-analysis** — Double-fortified salt (iron+iodine) (PMID 29767699, *Advances in nutrition*, 2018; 12 efficacy + 2 effectiveness studies).
- **Systematic Review & Meta-Analysis** — Multiple-micronutrient fortified non-dairy beverages, school-aged children (PMID 26007336, *Nutrients*, 2015; certainty moderate).
- **Systematic review & meta-analysis** — Micronutrient-fortified dairy/cereal foods, children/adolescents 5–15 y (PMID 30673769, *PloS one*, 2019; GRADE very low for haematologic, low for anthropometrics).
- **Narrative/other review** — Fortified blended food aid products, infants and young children (key oa_W2133536497, *Nutrition Reviews*, 2009; no meta-analysis, no numeric effect sizes).

Consistency: across independent reviews and vehicles, **iron/multiple-micronutrient fortification consistently reduces anaemia and iron deficiency**, and salt iodization / double-fortified salt consistently improves iron status; **growth outcomes (stunting, weight/height-for-age) are consistently null**. This cross-review consistency on the micronutrient-status outcomes supports an **Evidence: A** rating, with the important qualification that certainty is high only for haematologic/micronutrient-status endpoints, not for anthropometric or mortality endpoints.

### Effect sizes (measure + 95% CI + corpus PMID; all-cause vs cause-specific / outcome-specific kept separate)

Anaemia / iron status (the strongest and most consistent domain):
- Fortified complementary foods (6–23 mo): **anaemia RR 0.57 (95% CI 0.39–0.82)**, i.e. the ~43% reduction described in the abstract; haemoglobin **MD +3.44 g/L (1.33–5.55)**; iron deficiency (ferritin <12 µg/L) **RR 0.39 (0.21–0.75)** — random-effects, moderate certainty (PMID 35753314).
- Double-fortified salt, efficacy studies: **anaemia RR 0.59 (0.46–0.77)**; iron deficiency anaemia **RR 0.37 (0.25–0.54)**; haemoglobin SMD 0.28 (0.11–0.44) (PMID 29767699).
- Iron-fortified condiments/seasonings: **anaemia RR 0.34 (0.18–0.65)**; ferritin MD +14.81 µg/L (5.14–24.48); iron deficiency RR 0.33 (0.11–1.01, CI crosses 1) (PMID 37665781).
- MMN non-dairy beverages, school-age children: **anaemia RR 0.58 (0.29–0.88)**; iron deficiency RR 0.34 (0.21–0.55); iron deficiency anaemia RR 0.17 (0.06–0.53); haemoglobin MD +2.76 g/L (1.19–4.33) (PMID 26007336).
- Fortified dairy/cereal foods, 5–15 y: main-analysis **anaemia RR 0.87 (0.76–1.01) — null**, haemoglobin MD +0.09 g/dL (−0.01–0.18) null; but iron-deficiency anaemia RR 0.38 (0.18–0.81) and iron deficiency RR 0.62 (0.40–0.97) reduced (very low certainty) (PMID 30673769). This is the one review where the primary anaemia endpoint was null, driven by the older/school-age population and heterogeneous vehicles.

Iodine (universal salt iodization; from CEA/benefit record, not a bundle effect-size review): USI prevented an estimated 720 million cases of clinical iodine-deficiency disorders and ~20.5 million newborn cases annually (PMID 32458745).

Folate / neural tube defects (cause-specific): NTD prevention is supported by the CEA literature rather than a bundle effect-size meta-analysis (see cost-effectiveness); the bundle's own effect-size reviews do not report NTD risk ratios (not in corpus as a pooled RR).

Vitamin A status (cause-specific target, largely null as a single nutrient):
- Vitamin A **alone** in staple foods: serum retinol **MD +0.03 µmol/L (−0.06–0.12) null**; subclinical VAD **RR 0.45 (0.19–1.05) — CI crosses 1**; night blindness RR 0.11 (0.01–1.98) null (PMID 31074495).
- Vitamin A **plus other micronutrients**: subclinical VAD **RR 0.27 (0.16–0.49)** reduced vs unfortified food (PMID 31074495). No trials reported morbidity, mortality, or adverse effects — the clinical (cause-specific) VAD pathway is **underpowered**.

Zinc status:
- Zinc as sole added nutrient: serum/plasma zinc **MD +2.12 µmol/L (1.25–3.00)** improved; but stunting **RR 0.88 (0.36–2.13)** and underweight **RR 3.10 (0.52–18.38)** are null/uninformative (very wide CIs); zinc + other micronutrients gives no serum-zinc benefit MD +0.03 (−0.67–0.72) (PMID 27281654).

Growth / anthropometrics (consistently null across reviews — flagged):
- Complementary foods: weight-for-age Z **MD −0.01 (−0.07–0.06)**; length/height-for-age Z **MD −0.01 (−0.21–0.20)**; serum retinol MD +0.03 (−0.02–0.08) all null (PMID 35753314).
- Dairy/cereal foods: HAZ/stunting MD +0.022 SD (−0.069–0.122) null (PMID 30673769).

All-cause vs cause-specific: the bundle's fortification reviews report **no all-cause mortality outcome** (not in corpus); benefits are on intermediate micronutrient-status endpoints (anaemia, iron/iodine/zinc status) and on the cause-specific NTD pathway via folic acid (supported through the CEA/modeling literature). Mortality and cause-specific morbidity endpoints are absent or underpowered and should not be claimed. No record has a `dominant_trial` set, so there is no single-trial-dominated pooled estimate to flag (contrast with vitamin A supplementation/DEVTA).

### Mechanism of action
Fortification adds micronutrients to widely consumed staples/condiments during industrial processing, raising habitual dietary intake without requiring behaviour change or clinical contact. Iron and multiple micronutrients correct iron/erythropoiesis deficits (reducing anaemia and iron deficiency); iodine in salt supports thyroid hormone synthesis and fetal neurodevelopment; folic acid in flour raises maternal periconceptional folate, closing the neural-tube during early gestation; zinc/vitamin A raise circulating status. The pathway to functional/growth and mortality endpoints is longer and more diluted, which is consistent with the null anthropometric findings and the underpowered clinical-VAD pathway above.

### Cost-effectiveness (cea_rating_allowed = true; 129 CEA papers retrieved, 0 registry matches)
The CEA evidence base is large and strongly favourable, supporting a **Very High** rating:
- Multi-country systematic review of economic evaluations across 63 countries (>40 LMICs): **58% (135/232) of analyses had ICERs < $150 per DALY averted**, and 87% (201/232) fell within a 50%-of-GDP-per-capita threshold; 84% (190/227) cost-effective at a 35%-of-GDP LMIC threshold (PMID 41620176 / OpenAlex W4411259514).
- Folic acid flour fortification investment case: **$14.90 per DALY averted** and $957 per death averted (PMID 29363765).
- Folic acid fortification, Chile: **I$89 per DALY averted** (0.8% of GDP per capita) with net cost savings of I$2.3 million (PMID 17363103).
- Wheat flour fortification, urban Cameroon: **$115 per DALY averted for anaemia, $50 per DALY for NTDs** — "very cost-effective" by WHO criteria (OpenAlex W3191010533).
- Universal salt iodization: estimated global economic benefit of ~$33 billion from IDD reduction 1993–2019 (PMID 32458745).
- Iron-containing MNP home fortification (78 countries): median **$3,576 per DALY averted** in the 54 countries with net benefit, but **net harm in 24 (largely high-malaria) countries** — a genuine cost-effectiveness caveat for iron MNPs in malaria-endemic settings (OpenAlex W3044712618).

Caveat within the rating: folic acid, iodine, and staple-flour iron fortification are unambiguously very cost-effective; iron **MNP** home fortification is context-dependent (can be net-harmful where malaria burden is high), and single-nutrient zinc/vitamin-A fortification alone has weaker efficacy so its cost-effectiveness is less certain.

### Government scaling pathway
Fortification is one of the most proven-at-national-scale nutrition delivery models. Salt iodization is mandated in most countries and had reduced iodine-deficient countries to 19 by 2019 (PMID 32458745); mandatory wheat/maize flour and rice fortification operate at national scale in numerous LMICs (e.g. India state programmes, Ghana, Burkina Faso, Cameroon, Chile). Platform fit is strong because delivery rides on existing food-processing value chains and regulatory (mandatory-standard) levers rather than health-system contact, giving very low marginal cost per person reached and high population coverage. Government roles are standard-setting, mandatory legislation, premix procurement/quality control, and industry compliance monitoring. This supports **Scalability: Proven national**. Documented constraints: coverage is consistently **lower among the most vulnerable** and varies greatly by vehicle and country (PMID 28404836 in the CEA set), and private-sector compliance is a recurring bottleneck.

### Caveats
- **Vehicle/nutrient heterogeneity:** "food fortification" is not one intervention. Effects are robust for iron/MMN → anaemia and for iodine and folate, weak/null for single-nutrient zinc and vitamin A, and consistently null for growth/anthropometrics. Do not generalize the anaemia effect to growth or mortality.
- **Underpowered / absent pathways:** clinical vitamin A deficiency, morbidity, and mortality outcomes were not reported by the fortification RCTs (PMID 31074495); growth outcomes are null across reviews (PMID 35753314, 30673769); zinc anthropometric CIs are uninformatively wide (PMID 27281654).
- **Risk of bias / low certainty:** all 16 iron-condiment trials were high risk of bias with very-low-to-moderate GRADE (PMID 37665781); zinc and dairy/cereal reviews are low/very-low certainty (PMID 27281654, 30673769).
- **Context-dependent harm:** iron MNP home fortification can be net-harmful in high-malaria settings (OpenAlex W3044712618) — a real safety/CEA flag, not a universal endorsement of iron.
- **Effectiveness gap:** double-fortified salt effect sizes shrink sharply from efficacy (anaemia RR 0.59) to effectiveness studies (haemoglobin SMD only 0.03, 0.01–0.05) (PMID 29767699), and coverage among vulnerable groups is lower (PMID 28404836) — real-world impact is smaller than efficacy trials imply.
- **Version/overlap:** no `cochrane_id` collisions in this bundle (the vitamin A CD010068 and zinc CD010697 Cochrane reviews are distinct reviews on distinct nutrients), so no double-counting of a single review across versions. No dominant single trial in any pooled estimate.
- **CEA source note:** 0 registry matches (Tufts/DCP3 registry not API-reachable); all cost-effectiveness figures are from retrieved PubMed/OpenAlex economic evaluations cited above, not from a curated registry or background knowledge.

## Antenatal Multiple Micronutrient Supplementation (MMS)  (Women of reproductive age / pregnant women; child birth outcomes)

**Evidence: A  |  Cost-effectiveness: Very High  |  Scalability: Requires investment (WHO-recommended, national transitions underway)  |  Tier 1**

- **Evidence base:** The bundle holds 9 records — by study_design (verbatim): 1 **Cochrane review** (PMID 26621223, *The Cochrane database of systematic reviews*, CD010994, an ANC-coverage review that is adjacent rather than core-MMS), 2 **Meta-analysis** records (PMID 39890230 *Lancet Global Health*; PMID 36130877 *American Journal of Clinical Nutrition*), and 6 **Systematic review & meta-analysis / Systematic review** records (PMIDs 37051178, 42067194, 27306908, 32075071, 33846729, plus the un-PMID'd *Lancet* adolescent review). No two records share a cochrane_id, so there is no version double-counting within the core MMS evidence. The consistent finding across the MMS-vs-IFA meta-analyses (PMID 39890230, 37051178, 32075071, 33846729, 36130877) is a benefit on **birth-outcome** endpoints (LBW, SGA, preterm, small-vulnerable-newborn types) with **null effects on mortality and long-term child outcomes** (PMID 27306908, 32075071). GRADE/certainty where stated: moderate-to-high for IFA-related maternal anaemia and LBW (PMID 37051178); moderate certainty for MMS-vs-IFA maternal anaemia and very-low-to-low certainty for counseling/weight-gain outcomes (PMID 42067194); the adolescent *Lancet* review reports mostly high risk-of-bias evidence (only 3 of 75 reports low risk; no PMID in corpus). Overall this supports **Evidence A** for the birth-outcome benefit (multiple consistent meta-analyses), with an explicit caveat that mortality/growth benefits are not established.

- **Effect sizes** (measure + 95% CI + corpus PMID; birth outcomes vs mortality kept separate):

  *Birth outcomes — MMS vs IFA (benefit):*
  - Low birthweight, MMN vs iron±FA: RR 0.85 (0.77–0.93), 28 studies, n=79,972; and RR 0.79 (0.71–0.88) for MMN with >4 micronutrients (19 studies, n=68,138) — PMID 37051178.
  - Small-for-gestational-age, MMN vs iron±FA: RR 0.93 (0.88–0.98), 19 studies, n=52,965 — PMID 37051178.
  - Stillbirth, MMN vs iron±FA: RR 0.91 (0.86–0.98), 22 studies, n=96,772 — PMID 37051178.
  - Small-vulnerable-newborn types, MMS vs IFA (IPD meta-analysis, 14 studies, n=42,618, random-effects): preterm–SGA–LBW RR 0.73 (0.64–0.84); preterm–AGA–LBW RR 0.82 (0.74–0.91); term–SGA–LBW RR 0.91 (0.85–0.96); preterm–SGA RR 0.71 (0.62–0.82) — PMID 39890230. Full text confirms the largest reductions fall on the newborn types "conferring the greatest risk of neonatal mortality" (preterm–SGA–LBW, preterm–AGA–LBW, preterm–SGA), with low heterogeneity (I² generally <15%) — PMID 39890230.
  - Adolescents (<20y), MMN vs IFA (IPD, 13 studies, n=15,283): LBW OR 0.81 (0.74–0.88, two-stage); preterm birth OR 0.88 (0.80–0.98); SGA OR 0.86 (0.79–0.95); birth weight +49 g (33–65) — PMID 33846729. Effects similar to adult women, possibly greater SGA benefit in adolescents.
  - Gestational weight gain, MMS vs IFA (IPD, 14 studies, n=45,507): % adequacy MD +0.86 (0.28–1.44); total GWG +209 g (139–280); severely inadequate GWG RR 0.971 (0.956–0.987) — PMID 36130877.

  *Maternal anaemia:*
  - IFA vs folic acid alone: RR 0.52 (0.41–0.66), 5 studies, n=15,540 — PMID 37051178. MMS vs FA (Liu et al., within PMID 42067194): anaemia RR 0.71 (0.62–0.82), Hb MD +0.06 g/dL (0.03–0.09).

  *Mortality / long-term child outcomes — NULL (kept separate; underpowered pathways flagged):*
  - Long-term (up to 9y) follow-up of 9 trials (n=88,057), MMN vs IFA: all-cause child mortality risk difference −0.05 per 1000 livebirths (−5.25 to 5.15); WAZ MD 0.02 (−0.03 to 0.07); HAZ MD 0.01 (−0.04 to 0.06); neonatal mortality RR 1.01 (0.90–1.16) — all null — PMID 27306908.
  - PMID 32075071 (72 studies, n=451,723): maternal/neonatal/perinatal/infant mortality null across all comparisons (direction reported; point estimates not in the abstract-derived record → effect sizes **not in corpus** for this record).
  - Adolescent trial-level signals (PMID for *Lancet* review **not in corpus**): JiVitA-3 infant mortality RR 0.95 (0.86–1.06, null); SUMMIT early infant mortality RR 0.82 (0.70–0.95, overall benefit not seen in the adolescent subgroup); one Burkina Faso weekly periconceptional iron+FA signal of **harm** in nulliparous adolescents, preterm birth RR 2.22 (1.39–3.61) — flagged as an underpowered/subgroup safety signal, not an MMS finding.
  - ANC-coverage Cochrane review (PMID 26621223): combined health-system+community interventions reduced perinatal mortality OR 0.74 (0.57–0.95) and LBW OR 0.61 (0.46–0.80); single interventions had null effect on pregnancy-related deaths OR 0.69 (0.45–1.08). GRADE: high for ANC 4+ visits/facility delivery, moderate for perinatal mortality/LBW, low for pregnancy-related deaths.

  **Dominant trial:** across the core IPD meta-analyses the estimates are driven by **West et al. 2014 (JiVitA-3, Bangladesh)** — the largest MMS trial (n≈17,115), contributing 48.7% of the pooled adolescent IPD sample (PMID 33846729) and substantial weight in the SVN meta-analysis (PMID 39890230). SUMMIT (Indonesia) is the second dominant trial in the adolescent literature.

- **Mechanism of action:** MMS (typically the 15-micronutrient UNIMMAP formulation) supplies iron and folic acid plus 13 additional vitamins/minerals (vitamin A, D, E, B-complex, zinc, copper, selenium, iodine) during pregnancy, correcting concurrent maternal micronutrient deficiencies that constrain fetal growth. The measurable effect is on fetal growth and gestational duration — reduced LBW/SGA/preterm and improved gestational weight gain — rather than on downstream mortality, which the corpus shows is not reliably improved over IFA.

- **Cost-effectiveness: Very High** (cea_rating_allowed = true; 87 CEA papers retrieved, 0 registry matches). Grounded estimates:
  - MMS cost-benefit tool across 33 LMICs: **cost per DALY averted US$23.61**, benefit-cost ratio US$41–US$1,304 : $1 (Nutrition International; *Maternal & Child Nutrition* 2023, OpenAlex W4382344552; no PMID).
  - Replacing IFA with MMS in Bangladesh & Burkina Faso: **cost per DALY averted US$3–US$15**; cost per death averted US$175–185 (Bangladesh) / US$112–125 (Burkina Faso) (*Annals NYAS* 2019, DOI 10.1111/nyas.14132; no PMID).
  - Microsimulation across India/Pakistan/Mali/Tanzania: **ICER for universal MMS vs baseline IFA US$52 (Pakistan) to US$253 (Tanzania) per DALY** — US$70 India, US$72 Mali (PMID 35192606, *PLoS Medicine* 2022). MMS + targeted balanced-energy-protein averts more DALYs while remaining cost-effective.
  - MINIMat (early food + MMS): incremental US$27–34 per life-year saved (PMID 26018633).
  All figures fall far below standard LMIC willingness-to-pay thresholds, supporting a **Very High** rating.

- **Government scaling pathway:** MMS is delivered through the existing antenatal-care platform as a direct substitution for IFA tablets, so it requires no new delivery channel — the marginal cost is the tablet-price differential. WHO now recommends antenatal MMS (including IFA) in the context of rigorous research/implementation (per PMID 35192606 and 42067194), and Nutrition International's costing tool is built for national transition decisions (W4382344552). Effective health-system delivery depends on first/second-trimester initiation plus individualized counseling and weight-gain monitoring within primary health care (PMID 42067194). Rated **Requires investment**: proven platform fit but active national IFA→MMS transitions are still scaling rather than fully institutionalized.

- **Caveats:**
  - *All-cause vs cause-specific / mortality:* the robust, consistent benefit is on **birth outcomes** (LBW/SGA/preterm/SVN), not mortality. Multiple records show null effects on maternal, neonatal, perinatal, infant, and long-term child mortality and growth (PMID 27306908, 32075071); do not present MMS as a mortality intervention on this corpus.
  - *Dominant-trial dependence:* JiVitA-3 (and SUMMIT) drive the pooled estimates; pooled effects are sensitive to these two trials (PMID 39890230, 33846729).
  - *Underpowered subgroups:* adolescent-specific and cause-specific/mortality subgroups are underpowered; the Burkina Faso weekly periconceptional iron+FA harm signal RR 2.22 (1.39–3.61) is a subgroup safety flag in a *different* regimen, not MMS (source: adolescent *Lancet* review, PMID **not in corpus**).
  - *Version/overlap:* no cochrane_id collisions within the bundle; the ANC-coverage Cochrane review (CD010994) is a distinct, adjacent review and is not part of the core MMS-vs-IFA evidence.
  - *External figures excluded:* no cost or mortality figure has been imported from background knowledge; every number above is tagged to a corpus PMID/DOI/OpenAlex ID or marked "not in corpus."

## Zinc supplementation in children (children under 5; one review spans WRA/adults)
**Evidence: A  |  Cost-effectiveness: High  |  Scalability: Growing  |  Tier 1**

- **Evidence base:** The bundle holds **9 records** — 4 tagged *Meta-analysis* / *Cochrane review* and 5 *Systematic review* (self-described study types verbatim below). Two are Cochrane reviews (journal = *The Cochrane database of systematic reviews*): **CD009384** (preventive zinc, pmid 36994923) and **CD005436** (oral zinc for treating diarrhoea, pmid 27996088); a third Cochrane review covers otitis media (**CD006639**, pmid 24974096). Each cochrane_id appears once — no version double-counting. Evidence converges cleanly by outcome: zinc **treats** acute diarrhoea (multiple consistent meta-analyses, moderate–high GRADE for the >6-month/malnourished subgroups) and **prevents** diarrhoea incidence, but shows **no all-cause mortality benefit** and **no anthropometric/stunting benefit** at the population level. GRADE certainty is stated per-outcome and is high only for a subset (see caveats).

- **Effect sizes** (measure + 95% CI + corpus PMID/key; all-cause vs cause-specific kept separate):

  *Diarrhoea treatment — CD005436, "Meta-analysis" (pmid 27996088):*
  - Diarrhoea duration, age >6 mo (acute): **MD −11.46 h (−19.72, −3.19)**, 9 studies, n=2,581 [pmid 27996088].
  - Diarrhoea duration, malnourished children: **MD −26.39 h (−36.54, −16.23)**, 5 studies, n=419 [pmid 27996088] — largest benefit; GRADE high for this subgroup.
  - Diarrhoea persisting to day 7 (>6 mo): **RR 0.73 (0.61, 0.88)**, 6 studies, n=3,865 [pmid 27996088].
  - Age <6 mo: **MD +5.23 h (−4.00, 14.45)** — null, no benefit under 6 months [pmid 27996088].
  - Harm — vomiting (>6 mo): **RR 1.57 (1.32, 1.86)**, n=2,605 [pmid 27996088].

  *Diarrhoea treatment — "Systematic Review & Meta-Analysis", 104 RCTs / 18,822 cases (pmid 24284615):*
  - Diarrhoea episodes lasting >3 days, pooled: **RR 0.74 (0.68, 0.80)**, n=18,822; non-Chinese studies only **RR 0.78 (0.67, 0.90)** [pmid 24284615]. Concordant with CD005436's day-7 RR 0.73.
  - Harm — vomiting (non-Chinese): **RR 1.83 (1.40, 2.39)** [pmid 24284615].

  *Prevention — CD009384, "Cochrane review" (pmid 36994923); abstract-only, publisher-restricted full text:*
  - **All-cause mortality: RR 0.93 (0.84, 1.03)** — null, 16 studies, n=143,474 [pmid 36994923]. No dominant_trial is flagged in the record; this is a clean pooled estimate, not a fixed-vs-random divergence (contrast with vitamin A/DEVTA — not applicable here).
  - Cause-specific mortality (all underpowered, all CIs cross 1): diarrhoea **RR 0.95 (0.69, 1.31)** [pmid 36994923]; LRTI **RR 0.86 (0.64, 1.15)**; malaria **RR 0.90 (0.77, 1.06)**.
  - Diarrhoea **incidence: RR 0.91 (0.90, 0.93)**, 39 studies, n=19,468 [pmid 36994923] — consistent morbidity benefit.
  - Linear growth: **height SMD 0.12 (0.09, 0.14)**, 74 studies, n=20,720 [pmid 36994923] — small.

  *Growth (LMIC, "Systematic review", pmid 30898990):*
  - Height-for-age Z: **MD 0.00 (−0.07, 0.07)** null; stunting **RR 1.00 (0.95, 1.06)**; wasting **RR 0.94 (0.82, 1.06)**; underweight **RR 1.08 (0.96, 1.21)** — all null [pmid 30898990]. Small gains only in change-in-length **MD 0.43 cm (0.16, 0.70)** and change-in-weight **MD 0.11 kg (0.05, 0.17)**. Authors conclude growth-promotion use "appears unjustified."

  *Umbrella review, 43 meta-analyses ("Systematic review", key oa_W4210842995):*
  - Childhood diarrhoea incidence **RR 0.89 (0.82, 0.97)**; pneumonia incidence **RR 0.87 (0.81, 0.94)**; ALRI incidence **RR 0.65 (0.52, 0.82)**; height gain **MD 0.43 cm (0.16, 0.70)** [oa_W4210842995]. Stunting **RR 1.00 (0.95, 1.06)** — null. AMSTAR2 mostly critically low; GRADE mostly very low.

  *Adjunct treatment for pneumonia ("Systematic review & meta-analysis", pmid 20348118):* zinc as adjunct to pneumonia case management showed **no benefit** (hospitalisation-hours effect 13%, 95% CI −37 to 45 — null) [pmid 20348118]. All-cause mortality benefit in that review is attributable to community antibiotic case management (**RR 0.79, 0.70–0.88**), *not* zinc.

  *Otitis media — CD006639, "Meta-analysis" (pmid 24974096):* mixed — one trial rate ratio **0.69 (0.61, 0.79)**; benefit concentrated in severely malnourished infants (**MD −1.12 episodes, −2.21 to −0.03**, n=39) [pmid 24974096].

  *Adherence ("Systematic review & meta-analysis", pmid 41178278):* pooled adherence **63.45% (51.62, 75.28)** for the 10-day regimen vs **34.58% (7.08, 62.09)** for 14-day, I²=98% [pmid 41178278] — favours the shorter WHO regimen.

  *Note:* pmid 26818403 is a **published protocol only** (PROSPERO CRD42015023778) — no results; excluded from effect synthesis.

- **Mechanism of action:** Zinc is a cofactor in >100 metalloenzymes and stabilises transcription factors; it supports intestinal epithelial repair and ion transport (shortening diarrhoeal episodes) and modulates cell-mediated/mucosal immunity (reducing respiratory and diarrhoeal incidence). Effect is largest where baseline zinc status is poor — hence the strongest treatment benefit in malnourished children [pmid 27996088].

- **Cost-effectiveness:** cea_rating_allowed = **true** (51 CEA papers, 0 registry matches). Grounded figures from cea_record: preventive zinc pill supplementation **US$606/DALY** (biscuits US$1,211; water filtration US$879), estimated to avert 1.423 DALYs/100 households/yr, "highly cost-effective" [pmid 25128210]; sub-Saharan Africa modelling gives **US$462–3,111 per life saved**, most cost-effective as weekly/intermittent preventive dosing [pmid 23964393]; a WHO-CHOICE child-health CEA ranked zinc/vitamin-A fortification and supplementation among the most cost-effective child interventions [pmid 16282378]. Counter-evidence: a Tanzania decision model found prophylactic zinc **US$4,950/DALY averted (1,678–17,933)** — above local thresholds, i.e. context-dependent [oa W4220848949]. Net: **High**, not Very High, because the most favourable ICERs are for treatment/targeted preventive dosing while blanket prevention is borderline in some settings.

- **Government scaling pathway:** Therapeutic zinc is already **WHO/UNICEF standard of care** for childhood diarrhoea (zinc + ORS), delivered through IMCI, community case management (CHWs), and essential-medicine supply chains — a proven, low-cost delivery rail. The bundle shows the binding constraint is **adherence, not efficacy**: switching to the **10-day regimen** roughly doubles completion (63% vs 35%) [pmid 41178278], and caregiver education plus provider counselling are the named levers. Preventive supplementation can ride child-health-day and community-nutrition platforms [pmid 23964393]. Scalability = **Growing** (treatment rail proven; population-wide prevention still requires investment and targeting).

- **Caveats:**
  - **Outcome-specific, not blanket, benefit.** Zinc's strong, consistent effect is on **diarrhoea duration/incidence and pneumonia/ALRI incidence**; it does **not** reduce all-cause mortality (RR 0.93, CI crosses 1) [pmid 36994923] and does **not** reduce stunting/wasting/underweight [pmid 30898990]. Do not aggregate into an all-cause mortality claim.
  - **Underpowered pathways.** All cause-specific mortality estimates (diarrhoea, LRTI, malaria) have wide CIs crossing 1 and are explicitly underpowered; the CD005436 full text flags trials as "significantly underpowered to detect or exclude an effect on mortality" [pmid 27996088].
  - **Heterogeneity / quality.** I²=98% in the adherence meta-analysis [pmid 41178278]; the umbrella review's 43 meta-analyses are mostly AMSTAR2 critically-low and GRADE very-low [oa_W4210842995]; pmid 24284615 pools 89 previously unincorporated Chinese studies whose duration effects differ markedly from non-Chinese trials.
  - **Harm signal.** Zinc consistently raises vomiting risk (RR 1.57 [pmid 27996088]; RR 1.83 [pmid 24284615]).
  - **Under-6-month and iron co-supplementation** attenuate benefit: no effect <6 months [pmid 27996088]; iron co-supplementation reduced zinc's benefit in CD009384 subgroup analysis [pmid 36994923].
  - **Two Cochrane reviews are abstract-only** in the corpus (publisher-restricted PMC XML), so their forest-plot/model detail could not be traced beyond the reported pooled estimates.

## Vitamin A supplementation in children 6–59 months  (children under 5)
**Evidence: A  |  Cost-effectiveness: Moderate  |  Scalability: Proven national  |  Tier 1**

- **Evidence base:** Six records in the bundle, all in under-5 populations: four labelled Meta-Analysis / systematic review & meta-analysis and two systematic reviews (bundle `tiers`: meta_analysis 4, systematic_review 2). No two records share a `cochrane_id`, so there is no version double-counting to collapse (record 3 is the only true Cochrane review, CD006090, on LRTI). Across the effectiveness syntheses the **preventive-VAS all-cause-mortality benefit in children 6–59 months is consistent**: Imdad/BMJ fixed-effect RR 0.76 (PMID 21868478), the CHERG/LiST-methods meta-analysis RR 0.75 (PMID 21501438), and the 1995 WHO field-trial meta-analysis RR 0.77 (PMID 8846487) all converge on a ~24–25% reduction. Certainty is stated as GRADE High for all-cause mortality and Moderate for diarrhoea-specific mortality (PMID 21868478; PMID 21501438). This convergence of multiple consistent meta-analyses supports **Evidence Grade A** for the *all-cause-mortality* endpoint in the 6–59-month age group.

- **Effect sizes:**
  - **All-cause mortality (6–59 months) — the robust finding.**
    - Fixed-effect RR **0.76 (95% CI 0.69–0.83)**, 16 trials, 194,483 participants, moderate heterogeneity I²=48% (PMID 21868478, full text).
    - **DEVTA-inclusive** fixed-effect RR **0.88 (95% CI 0.84–0.94)**, 17 trials, 1,194,483 participants (PMID 21868478, full text). The **dominant trial is DEVTA** (India, ~1 million children); the full text states this single trial "accounted for **65.2%** of the combined effect," which is what drives the estimate up from 0.76 to 0.88. This is a sensitivity/subgroup analysis, not a separate review — the same review reports both.
    - Random-effect / independent-corpus corroboration: RR **0.75 (95% CI 0.64–0.88)** (PMID 21501438, CHERG-methods) and RR **0.77 (95% CI 0.71–0.84)** (PMID 8846487, WHO field trials). Age-restricted: the mortality benefit held for infants 6–11 months (RR **0.69, 95% CI 0.54–0.90**) but was null at 0–5 months (RR **0.97, 95% CI 0.73–1.29**) (PMID 8846487).
  - **Cause-specific mortality (kept separate — the genuinely thinner evidence).**
    - Diarrhoea-specific mortality: RR **0.72 (95% CI 0.57–0.91)**, 7 trials (PMID 21868478); RR **0.70 (95% CI 0.58–0.86)**, 7 trials (PMID 21501438) — a consistent benefit (GRADE Moderate).
    - Measles-specific mortality: RR **0.80 (95% CI 0.51–1.24)** (PMID 21868478) and RR **0.71 (95% CI 0.43–1.16)** (PMID 21501438) — **underpowered, CI crosses 1** in both syntheses.
    - Pneumonia-specific mortality: RR **0.94 (95% CI 0.67–1.30)** (PMID 21501438) and RR **0.98 (95% CI 0.75–1.28)** (PMID 8846487) — **null**; pneumonia incidence also null, RR 0.95 (95% CI 0.89–1.01) (PMID 8846487).
    - Meningitis-specific mortality: RR **0.73 (95% CI 0.22–2.48)** (PMID 21501438) — **null, very imprecise**.
  - **Morbidity.** Measles incidence RR **0.50 (95% CI 0.37–0.67)** and diarrhoea incidence RR **0.85 (95% CI 0.82–0.87)** (PMID 21868478).
  - **Lower respiratory tract infection.** No overall protective effect; benefit only in the poor-nutritional-status / low-serum-retinol subgroup, and increased incidence in well-nourished children — no pooled RR reported (narrative synthesis, PMID 18254093, Cochrane review). The review concludes VAS should **not** be given universally to prevent LRTIs.
  - **Neonatal (0–28 days) VAS — distinct population, does NOT work.** All-cause mortality null at 1 month RR **0.99 (95% CI 0.90–1.08)**, 6 months RR **0.98 (0.89–1.07)**, 12 months RR **1.04 (0.94–1.14)**, with a harm signal for bulging fontanelle RR **1.53 (95% CI 1.12–2.09)** (PMID 37133295, GRADE High). (Note: the probiotic outcomes in PMID 37133295 — e.g. all-cause mortality RR 0.80 — are a *separate co-bundled intervention*, not vitamin A.)

- **Mechanism of action:** Vitamin A (retinol) corrects deficiency that impairs epithelial-barrier integrity and innate/adaptive immune function; repletion reduces severity/case-fatality of infections (notably measles and diarrhoeal disease), which is why the mortality signal is strongest for diarrhoea and where measles burden is high, and why benefit concentrates in deficient/6–59-month children rather than well-nourished or neonatal populations.

- **Cost-effectiveness:** `cea_rating_allowed` is **true** (94 CEA papers retrieved; 0 registry matches). The most directly relevant CEA record is an individual-based microsimulation using GBD 2019 (PMID 35390077, *PLoS One* 2022): ICER **$860/DALY** (95% UI 320–3,530) in Nigeria, **$550/DALY** (240–2,230) in Kenya, and **$220/DALY** (80–2,470) in Burkina Faso for scaling up VAS 2019–2023. Notably this record concludes VAS **"may no longer be as cost-effective in low-income regions as it has been previously,"** because updated GBD 2019 effect estimates lowered the modelled impact. Given ICERs in the low-hundreds-to-~$860/DALY range but an explicit downward revision, the rating is **Moderate** (context-dependent by country/baseline coverage) rather than the historically cited "Very High." The frequently quoted "$1–3 per child per year" figure is **(not in corpus)** and is deliberately excluded.

- **Government scaling pathway:** VAS is already delivered at national scale in many LMICs, primarily via **Child Health Days** and campaign platforms integrated with immunisation, and via community health workers (PMID 39584721). The implementation review of 12 African countries identifies the operational levers: Child Health Days and CHW involvement are the most-cited *facilitators*; capsule **stock-outs**, limited resources, and lack of staff incentives are the most common *barriers* (10 studies, PMID 39584721). Platform fit is strong (existing routine/campaign delivery), so scalability is rated **Proven national**, contingent on supply-chain reliability.

- **Caveats:**
  - **Version ≠ evidence / no double-counting:** the three converging mortality meta-analyses (PMIDs 21868478, 21501438, 8846487) are independent syntheses over overlapping primary trials, not evidence "generations"; the 0.76→0.88 shift within PMID 21868478 is **one review's** DEVTA sensitivity analysis, not a new study.
  - **DEVTA dominance:** DEVTA holds 65.2% of the pooled all-cause-mortality effect (PMID 21868478); the "true" per-child mortality benefit is genuinely uncertain between the ~24% (DEVTA-excluded) and ~12% (DEVTA-included) estimates.
  - **All-cause vs cause-specific split:** the robust finding is *all-cause* mortality in 6–59-month deficient children; **cause-specific pathways are weaker** — diarrhoea-mortality is consistent (Moderate certainty), but measles-, pneumonia-, and meningitis-specific mortality estimates are **underpowered with CIs crossing 1**.
  - **Population boundaries:** benefit is age-bounded — **null in neonates and at 0–5 months**, with a bulging-fontanelle harm signal in neonates (PMID 37133295); LRTI prevention shows no universal benefit and possible harm in the well-nourished (PMID 18254093).
  - **Cost-effectiveness is declining, not fixed:** the corpus CEA explicitly downgrades VAS as measles vaccination and food fortification expand and GBD effect estimates fall (PMID 35390077).

## Community-Based Management of Acute Malnutrition (CMAM) — SAM & MAM treatment  (children under 5, 6–59 months)

**Evidence: B  |  Cost-effectiveness: Very High  |  Scalability: Proven national  |  Tier 1**

- **Evidence base:** The bundle holds 11 on-topic records for CMAM/SAM-MAM treatment: 2 systematic reviews with meta-analysis (pmid_31906272 "Systematic review & meta-analysis", *Nutrients* 2020; pmid_41007088 "Systematic review & meta-analysis", *Children* 2025), 1 systematic review + meta-analysis for MAM (pmid_34535798 "Systematic Review & Meta-Analysis", *Trans R Soc Trop Med Hyg* 2021), 3 further systematic reviews (pmid_28934235 "Systematic review", *PLoS One* 2017; pmid_37131422 "Systematic review", *Campbell Systematic Reviews* 2020; pmid_33832950 "Systematic review", *BMJ Global Health* 2021), 1 Cochrane review on integrated delivery (pmid_33565123 "Cochrane review", *The Cochrane database of systematic reviews* 2021, CD012882), 3 observational/cohort records (oa_W2981160048 "Cohort", *PLoS Medicine* 2019; oa_W2108976338 retrospective records review, *Archives of Public Health* 2015; oa_W3047706909 "Other" qualitative, *Int J Equity Health* 2020), and 1 narrative/policy review (oa_W1982147559 "Narrative/other review", *J Pediatr Gastroenterol Nutr* 2012). Certainty is mostly **low to moderate GRADE**, repeatedly downgraded for risk of bias, heterogeneity, imprecision and small samples; no outcome reaches high certainty. Evidence is heavily concentrated in **African settings** and rests on **active-control comparisons** (one food/protocol vs another) rather than treatment-vs-no-treatment RCTs, which is why the grade is B rather than A.

- **Effect sizes** (all treatment-recovery / anthropometric unless flagged as mortality):

  *MAM treatment — LNS vs fortified blended foods (recovery, all-cause):*
  - Recovery rate, LNS vs specially-formulated fortified foods: **RR 1.08 (95% CI 1.02–1.14)**, 8 studies, 8,934 children (pmid_28934235); non-recovery reduced **RR 0.70 (0.58–0.85)**, 7 studies (pmid_28934235); certainty low.
  - Recovery from MAM, LNS vs FBF, random-effects: **RR 1.05 (95% CI 1.01–1.09)**, 13 trials (pmid_34535798).
  - Recovery, RUSF vs corn-soy blend (CSB): **RR 1.07 (95% CI 1.02–1.13)**, 6 studies, 5,744 children; severe wasting reduced **RR 0.74 (0.57–0.95)**, I²=0%, 3 studies (pmid_31906272).

  *SAM treatment — RUTF / community delivery:*
  - Recovery, standard vs alternative RUTF (community management): **RR 1.03 (95% CI 0.99–1.08)**, null, 5 studies, 5,743 (pmid_31906272) — formulations largely equivalent.
  - Weight gain, standard RUTF vs F100 (inpatient milk): **MD +5.5 g/kg/day (95% CI 2.92–8.08)**, single study, n=70 (pmid_31906272) — small, imprecise.
  - Integrated community-based management vs no community strategy: recovery **RR 1.04 (95% CI 1.00–1.09)** (dominant trial **Maust 2015**, Sierra Leone, cRCT, 1,957 participants, moderate quality; pmid_37131422); mortality null **RR 0.93 (0.60–1.45)** (pmid_37131422).

  *SAM adjunct — prophylactic antibiotics (mortality, cause-agnostic all-cause):*
  - Mortality, prophylactic antibiotics vs none in uncomplicated SAM: **RR 0.74 (95% CI 0.55–0.98)**, 3 studies, 6,944 children, moderate certainty — a ~26% all-cause mortality reduction (pmid_37131422; identical estimate independently in pmid_31906272). Recovery RR 1.06 (1.03–1.08); weight gain MD +0.67 g/kg/day (0.28–1.06). This is the single strongest mortality signal in the bundle, but it is an **adjunct drug**, not CMAM's core food component.

  *High- vs low-dose vitamin A in SAM (cause-agnostic mortality, UNDERPOWERED — flag):*
  - Mortality, high- vs low-dose vitamin A: **RR 7.07 (95% CI 0.37–135.13)**, 1 study, n=207 (pmid_37131422) — the CI spans two orders of magnitude; effectively no information. No dosing conclusion is supportable.

  *Refeeding syndrome (inpatient SAM, harm/safety):*
  - Pooled RFS prevalence (random-effects logit): **14% (95% CI 5.7%–30.4%)**, wide 8.7%–34.8% across studies driven by phosphate definition; mortality among those who developed RFS pooled ~**3% (95% CI 0%–7%)** but up to 18.2% in single studies (pmid_41007088); low-to-very-low certainty.

  *Prognosis / natural history (observational context, not intervention effects):*
  - SAM mortality hazard, fully adjusted: **HR 2.56 (95% CI 0.99–6.70)**; MUAC 11.5–<12.5 cm vs ≥12.5 cm HR 3.87 (1.63–9.18); case-fatality only 1.2% (SAM) and 1.1% (MAM) in rural eastern India, with only ~5% of SAM cases referred (oa_W2981160048) — argues untreated community SAM is less uniformly fatal than the classic 10–20% figure and that referral coverage is the binding constraint.
  - Inpatient SAM in-hospital mortality 46% overall (declining 51%→34.8% 2009–2013), HIV+ HR 1.8 (1.6–2.0), 9,540 admissions, Zambia (oa_W2108976338) — high inpatient death rates where HIV/comorbidity load is heavy.

  Numbers not in the corpus (e.g. global SAM burden, deaths preventable) are deliberately omitted — **(not in corpus)**.

- **Mechanism of action:** Acute malnutrition (SAM: WHZ < −3, MUAC < 11.5 cm, or bilateral oedema; MAM: WHZ −3 to −2, MUAC 11.5–12.5 cm) is treated by restoring energy/protein and micronutrients through calibrated therapeutic foods. RUTF (energy-dense lipid paste, no water needed, microbiologically safe) allows **outpatient** rehabilitation of uncomplicated SAM at home; RUSF/LNS treat MAM and prevent deterioration to SAM; F75/F100 milks stabilise complicated inpatient cases. Community screening (MUAC by CHWs/caregivers) plus decentralised distribution converts a hospital-bound problem into a primary-care one, raising coverage — the dominant driver of population impact. Prophylactic antibiotics act on occult bacterial infection in immunocompromised wasted children, explaining the mortality benefit.

- **Cost-effectiveness:** `cea_rating_allowed = true` (154 CEA papers retrieved; 0 registry matches). Grounded ICERs, all directly on CMAM/SAM/MAM:
  - Community-based SAM treatment, Zambia decision-tree: **US$53 per DALY averted**, US$203/case, US$1,760/life saved vs no treatment (pmid:20950075).
  - CMAM integrated into existing health services, Malawi: **US$42 per DALY averted**; CMAM overall **US$26–53 per DALY averted** vs US$1,344 for facility-based management (pmid:33102783).
  - Community prevention+treatment programme, Mumbai slums: **US$23 per DALY averted (95% UI 19–28)** (oa/W2900168001).
  - MAM screening+treatment (RUSF), Mali: **US$347 per DALY averted**, US$9,821/death averted (oa/W2943588395); MAM by community health volunteers, Kenya: **US$397 per DALY averted** vs US$637 control (oa/W4400735251).
  - Outpatient treatment settings, systematic review: **US$20–145 per DALY averted (provider)**, US$68–161 (societal) (oa/W4388487972).
  - Decentralised CHW delivery, Gao/Mali: cost per DALY averted **US$53–60 (intervention) vs US$173 (control)**; RUTF US$5.70 cheaper per child under simplified protocol (oa/W4406623706).
  These cluster far below any LMIC GDP-per-capita threshold (mostly < US$150/DALY), so **Very High** is well supported by corpus CEA — not imported. Note the CEA figures come from the Phase-2 CEA corpus, not from the effect-size records above.

- **Government scaling pathway:** CMAM is among the most **proven-at-national-scale** nutrition treatment models: the narrative policy record reports **55 countries implementing CMAM** with RUTF as a lower-cost alternative to inpatient care, and standardised inpatient protocols cutting SAM case-fatality from 30–50% to <5% (oa_W1982147559). Delivery fits existing platforms: outpatient therapeutic programmes at primary health centres, CHW/community health volunteer screening (MUAC), and integrated community case management (iCCM), which the Cochrane review found **probably increases careseeking coverage by 68% (RR 1.68, 95% CI 1.24–2.27)** vs usual facility services (pmid_33565123). Decentralisation and simplified protocols lower unit cost while raising coverage (oa/W4406623706). Binding constraints are RUTF supply chain/financing, referral coverage (only ~5% of community SAM reached treatment in one Indian cohort, oa_W2981160048), and continuity of care.

- **Caveats:**
  - **Overlap / double-counting:** pmid_37131422 (*Campbell Systematic Reviews* 2020) and pmid_31906272 (*Nutrients* 2020) are the **same evidence base** — both synthesise 42 studies / 35,017 children and report the identical antibiotic mortality estimate RR 0.74 (0.55–0.98). Count this mortality finding **once**, not twice; the two records are twin publications of one review, not independent confirmations.
  - **Active-control ceiling:** most anthropometric estimates compare one therapeutic food to another (LNS vs FBF, RUSF vs CSB, RUTF vs F100); they establish relative superiority, not the absolute treatment-vs-no-treatment benefit, which the ethics of SAM make hard to trial. This caps the evidence grade at B.
  - **All-cause vs cause-specific:** the only robust mortality signal is **all-cause** (antibiotics RR 0.74). Cause-specific mortality pathways are not resolved in the bundle. The high- vs low-dose vitamin A mortality estimate (RR 7.07, CI 0.37–135.13, n=207; pmid_37131422) is **grossly underpowered** — no dosing inference is warranted.
  - **Heterogeneity & geography:** evidence concentrated in Africa (pmid_28934235 explicitly African-only); refeeding-syndrome prevalence swings 8.7%–34.8% purely on definition (pmid_41007088). Conflict-setting effectiveness data are near-absent — only 8/91 publications reported coverage/effectiveness (pmid_33832950).
  - **iCCM signal of possible harm:** in the Cochrane review, under-five mortality in one trial rose (HR 1.18, 95% CI 1.01–1.37; pmid_33565123) with very-low certainty — a delivery-platform caution, not a verdict on RUTF itself.

## Periconception & Antenatal Folic Acid (and Iron-Folic Acid) Supplementation  (Women of reproductive age / periconception & pregnancy, LMIC)

**Evidence: B  |  Cost-effectiveness: Very High  |  Scalability: Proven national  |  Tier 1**

- **Evidence base:** The bundle holds **2 systematic reviews with meta-analysis**, both in women of reproductive age in LMICs, neither a Cochrane review:
  - PMID 32110886 — "Effects of Preconception Care and Periconception Interventions on Maternal Nutritional Status and Birth Outcomes in LMICs" (study design verbatim: *Systematic review & meta-analysis*; journal: *Nutrients*). Pooled 45 RCTs/quasi-experimental studies across four intervention families (delay first pregnancy, optimize inter-pregnancy intervals, periconception folic acid, periconception iron-folic acid). GRADE was applied per outcome; certainty ranged from **low to moderate** on the reproductive-health outcomes it graded (PMID 32110886, fulltext).
  - PMID 31680411 — "Maternal folic acid supplementation and infant birthweight in LMICs" (study design verbatim: *Systematic Review & Meta-Analysis*; journal: *Maternal & child nutrition*). 17 studies, 275,421 women (13 cohort + 4 RCTs); risk of bias via Newcastle-Ottawa (cohorts) and Cochrane RoB (RCTs) (PMID 31680411, fulltext).
  - Consistency is **directionally strong** (every pooled point estimate favors supplementation) but the evidence is **mixed in certainty**: several key estimates rest on very few RCTs, cross the null, or carry high heterogeneity. Hence **Evidence B**, not A — the direction is robust across two independent reviews, but no outcome is anchored on multiple large consistent RCT-only meta-analyses.

- **Effect sizes** (measure + 95% CI + corpus PMID; distinct outcome pathways kept separate):

  *Neural tube defect prevention (periconceptional folic acid vs placebo):*
  - **RR 0.53, 95% CI 0.41–0.67** (three studies; n = 248,056; **random-effect**; heterogeneity χ² p = 0.36, **I² = 0%**) — a 47% reduction (PMID 32110886, fulltext). Note the *abstract* of the same review reports this as "RR 0.53, 95% CI 0.41–0.77; two studies"; the **full text supersedes it** with the tighter 0.41–0.67 CI over three studies, which is the figure adopted here. This pooled estimate is dominated by the very large Chinese community-intervention cohort that supplies the bulk of the 248,056 participants (no single-trial `dominant_trial` field was set in the record, but the participant mass is concentrated in the large public-programme study rather than distributed across the small RCTs).

  *Anemia in women (periconceptional iron-folic acid vs placebo) — distinct from NTD pathway:*
  - Overall: **RR 0.66, 95% CI 0.53–0.81** (six studies; n = 3,430; random-effect; **I² = 88%**, high heterogeneity) (PMID 32110886, abstract + fulltext).
  - Weekly supplementation subgroup: **RR 0.70, 95% CI 0.55–0.88** (six studies; n = 2,661) (PMID 32110886, fulltext).
  - Daily supplementation subgroup: **RR 0.49, 95% CI 0.21–1.21** (two studies; n = 1,532) — **crosses the null / underpowered** (PMID 32110886, fulltext).
  - School-setting subgroup: **RR 0.66, 95% CI 0.51–0.86** (four studies; n = 3,005) (PMID 32110886, fulltext). The benefit is concentrated in weekly, school-delivered regimens; the daily-only estimate is not statistically significant.

  *Birthweight outcomes (maternal folic acid supplementation vs control) — third, separate pathway:*
  - Mean birthweight, all designs: **MD +0.37 kg, 95% CI 0.24–0.50** (9 studies) (PMID 31680411).
  - Mean birthweight, **RCT subset only**: **MD +0.56 kg, 95% CI 0.15–0.97** (3 studies) — larger effect but wide CI on a thin RCT base (PMID 31680411).
  - Low birthweight incidence, all designs: **OR 0.59, 95% CI 0.47–0.74** (10 studies) (PMID 31680411).
  - Low birthweight incidence, **RCT subset**: **OR 0.68, 95% CI 0.30–1.58** (2 studies) — **crosses the null / underpowered** once restricted to RCTs (PMID 31680411, fulltext).
  - Small-for-gestational-age (excl. postconceptional-use Zheng 2016): **OR 0.63, 95% CI 0.39–1.01** (5 studies) — borderline, upper CI touches 1.01; and including Zheng 2016: **OR 0.71, 95% CI 0.46–1.08** (6 studies) — **not significant** (PMID 31680411, abstract + fulltext).

  *Reproductive-spacing pathway (education to delay first pregnancy — nutrition-sensitive):*
  - Ever used contraception: **RR 1.71, 95% CI 1.42–2.05** (two studies; n = 911; I² = 0%) (PMID 32110886).

- **Mechanism of action:** Folate is a one-carbon cofactor essential for pyrimidine/purine and DNA synthesis; adequate periconceptional folate status supports the rapid cell division of early neural-tube closure (weeks 3–4 of gestation), which is why the exposure window must be *periconceptional*, not late-antenatal (PMID 31680411, fulltext; PMID 32110886, fulltext). Iron co-supplementation corrects the iron deficiency that drives most maternal anemia; folate additionally supports erythropoiesis. Improved maternal folate status is the plausible route to reduced intrauterine growth restriction (the dominant cause of LBW in LMICs) and thus higher mean birthweight.

- **Cost-effectiveness: Very High.** `cea_rating_allowed` is **true** (59 CEA papers retrieved, 0 registry matches). Grounded figures from the bundle's `cea_record`:
  - Antenatal MMS-vs-IFA transition cost per DALY averted **averages US$23.61** across 33 countries; benefit-cost ratios US$41–US$1,304 : $1 (Verney et al. 2023, *Maternal & Child Nutrition*, DOI 10.1111/mcn.13523, cea_record).
  - MMS vs baseline IFA ICERs: **US$52 (95% UI 28–78) Pakistan, US$70 (43–104) India, US$72 (37–118) Mali, US$253 (112–481) Tanzania** (PMID 35192606, *PLoS Medicine*).
  - Replacing IFA with MMS: **cost per DALY averted US$3–US$15**; cost per death averted US$112–185 in Bangladesh/Burkina Faso (Engle-Stone et al. 2019, DOI 10.1111/nyas.14132, cea_record).
  - Weekly IFA + deworming in WRA (Vietnam): **US$4.24 per anemia case prevented/year**, benefit:cost 6.7:1 (Casey et al. 2011, DOI 10.1371/journal.pone.0023723, cea_record).
  - Optima Nutrition 129-country analysis: IFA for non-pregnant women **US$35 per anaemia case averted**; MMS for pregnant women US$47 (Scott et al. 2020, DOI 10.1186/s12916-020-01786-5, cea_record).
  - All ICERs sit far below typical LMIC willingness-to-pay thresholds → **Very High**. (Caveat: most CEA records evaluate the IFA→MMS *transition* or IFA+deworming for anemia; a pure periconceptional-folate-vs-nothing ICER is not isolated in the corpus.)

- **Government scaling pathway:** IFA supplementation in pregnancy is already the **long-standing global standard of care delivered through antenatal care (ANC)** in LMICs (PMID 42128491; Berti et al. 2017, cea_record), so the delivery platform (ANC + community health workers) is proven and nationally established in most LMICs. The periconception/adolescent window is deliverable through school-based weekly IFA programs (the anemia benefit was strongest in school settings — RR 0.66, 95% CI 0.51–0.86; PMID 32110886), and Vietnam's weekly IFA + deworming shows a costed subnational-to-national model (cea_record). Fortification of flour is a complementary population-level NTD-prevention route noted in the CEA literature (PMID 34673787). Net: **Proven national** platform fit via existing ANC and school-health systems.

- **Caveats:**
  - **Version/overlap:** No shared `cochrane_id` between the two records; they are independent reviews counted once each. There is no evidence of double-counting, but the two reviews may share underlying primary trials (both draw on LMIC folate/IFA RCTs) — trial-level overlap was not verified.
  - **Underpowered / non-significant pathways:** The **RCT-only** estimates weaken on restriction — LBW OR 0.68 (CI 0.30–1.58) and mean-birthweight MD +0.56 kg (CI 0.15–0.97, only 3 RCTs); SGA is non-significant (OR 0.63, CI 0.39–1.01; and 0.71, CI 0.46–1.08); daily (non-weekly) IFA for anemia is non-significant (RR 0.49, CI 0.21–1.21). The **strong, low-heterogeneity finding is NTD prevention** (I² = 0%); the birthweight and daily-anemia pathways are the genuinely thin spots.
  - **Heterogeneity:** Overall anemia pooling has **I² = 88%**, driven by dose schedule (weekly vs daily) and setting (school vs work) — the pooled point estimate masks this and should be read via the subgroups.
  - **Effect concentration:** The NTD estimate's participant mass (248,056) is concentrated in large community-programme studies rather than balanced across RCTs; the small RCTs contribute little weight, so the estimate reflects programmatic/observational scale as much as trial evidence.
  - **CEA scope mismatch:** cost-effectiveness figures largely concern IFA→MMS transitions and anemia management, not folic-acid-alone vs no supplementation; the "Very High" rating is well-supported for the IFA/MMS supplementation family this intervention sits within, but a folate-monotherapy ICER is not directly in corpus.


# Tier 2 — Strong or mixed evidence, scalable with investment

## Cash Transfers for Child & Maternal Nutrition (conditional & unconditional)  (children under 5 & women of reproductive age)
**Evidence: A  |  Cost-effectiveness: Moderate  |  Scalability: Proven national  |  Tier 2**

- **Evidence base:** The bundle holds 71 records for this intervention, including 6 meta-analyses and 13 systematic reviews (plus 14 RCTs and 22 observational studies). The nutrition-specific core is anchored by two random-effects meta-analyses from the same team in *BMJ Global Health* — Manley et al. 2020 (74 studies; `oa_W3115538441`) and its 2022 update "More evidence…" (55 additional articles, 129 estimates total; `oa_W4220654904`). These are complemented by a Cochrane review of community food-access interventions (*Cochrane Database of Systematic Reviews* 2020, `oa_W1775096410`, cochrane_id CD011504, GRADE-rated), a *PLoS Medicine* meta-analysis of cash-plus vs cash-alone (`oa_W3204861800`), a GRADE-assessed systematic review of social-assistance programs and birth outcomes (*The Journal of Nutrition* 2021, `pmid_34590144`), and a *PLoS ONE* meta-analysis of cash transfers and common mental disorders (`oa_W4321488779`). Direction of effect on linear growth is consistent across the two independent nutrition meta-analyses; magnitude is consistently small. Certainty is high for food security (UCTs, CD011504) but low-to-very-low for several anthropometric and birth-outcome endpoints.

- **Effect sizes** (all figures corpus-sourced; nutrition/anthropometric outcomes are the primary endpoints — kept separate from health-service and mental-health pathways below):

  *Linear growth / stunting (child anthropometry):*
  - Height-for-age z-score (HAZ): +0.03 ± 0.03 (p<0.03), Manley 2020 (`oa_W3115538441`); updated to +0.024 (95% CI 0.004 to 0.044; p<0.02), Manley 2022 (`oa_W4220654904`). Both random-effects.
  - Stunting prevalence: −2.1% (95% CI −3.5% to −0.7%), Manley 2020 (`oa_W3115538441`); −1.35% (95% CI −2.35 to −0.35; p<0.01), Manley 2022 (`oa_W4220654904`).
  - Wasting: not significant in 2020 (+1.2%, 95% CI −0.1% to 2.5%; p<0.07, `oa_W3115538441`); reported significant in 2022 (−1.31%, 95% CI −2.16% to 0.46%; p<0.01, `oa_W4220654904`) — note the reported CI crosses zero, so treat this as borderline.
  - Weight-for-age (WAZ): +0.02 (95% CI −0.03 to 0.08; p<0.42), not significant (`oa_W3115538441`); WAZ and WHZ non-significant in 2022 (`oa_W4220654904`).

  *Diet-quality mediators (mechanism pathway):*
  - Animal-source-food consumption: +4.5% (95% CI 2.9% to 6.0%) in 2020, rising to +6.72% (95% CI 5.24% to 8.20%; p<0.01) in 2022 (`oa_W3115538441`, `oa_W4220654904`).
  - Dietary diversity: +0.73 (95% CI 0.28 to 1.19) in 2020; +0.55 (95% CI 0.30 to 0.81; p<0.01) in 2022 (`oa_W3115538441`, `oa_W4220654904`).
  - Diarrhoea incidence: −2.7% (95% CI −5.4% to −0.0%; p<0.05) in 2020; −1.74% (95% CI −2.79% to −0.68%; p<0.05) in 2022 (`oa_W3115538441`, `oa_W4220654904`).

  *Cash-plus vs cash-alone (`oa_W3204861800`):* Cash + food transfers beat cash alone for HAZ (d = 0.08 SD, 95% CI 0.03 to 0.14; p=0.02) and stunting (OR = 0.82, 95% CI 0.74 to 0.92; p=0.01), but not for WHZ (d = −0.13, 95% CI −0.42 to 0.16) or WAZ (d = −0.06, 95% CI −0.28 to 0.15). Cash + nutrition BCC and cash + psychosocial stimulation added no anthropometric benefit over cash alone.

  *Birth outcomes (WRA — GRADE very-low certainty, `pmid_34590144`):* across 6 evaluations of 4 cash-transfer programs, significant birth-weight effects ranged 31–578 g; neonatal-mortality effects (3 studies, 2 significant) ranged 0.6–3.1 deaths/1000 live births. All-cause vs cause-specific note: only all-cause/composite birth outcomes were pooled; cause-specific neonatal mortality pathways are underpowered and were not disaggregated.

  *Cochrane food-access certainty gradient (`oa_W1775096410`, CD011504):* UCTs — high-certainty improvement in food security, low-certainty reduction in stunting; food vouchers — moderate-certainty reduction in stunting; CCTs — high-certainty slight cognitive gain but only low-certainty effect on stunting/wasting; income-generation and social-environment interventions — no clear effect on stunting/wasting.

  *Other pathways (kept separate from anthropometry):* common mental disorders — depression/anxiety SMD −0.102 (95% CI −0.151 to −0.053, 11 studies; moderate certainty), attenuating at long follow-up (SMD −0.051, 95% CI −0.139 to 0.037; low certainty) (`oa_W4321488779`); single-study service-utilisation signals include a +45 pp (95% CI 18 to 72) ANC-visit increase (Afghanistan CCT) and MUAC gains of 0.9–1.3 cm from Somalia transfers (`oa_W4207018050`).

- **Mechanism of action:** Cash relaxes the household budget constraint, and the corpus traces the biological pathway through improved diet quality rather than caloric quantity — higher dietary diversity and animal-source-food intake plus reduced diarrhoea incidence (Manley 2020/2022), which translate into modest HAZ/stunting gains. Effects on weight-based indices (WAZ/WHZ/wasting) are weak, consistent with cash acting on chronic linear-growth pathways more than acute wasting. Conditionalities (health visits, school attendance) appear to drive the cognitive-development benefit seen for CCTs but not UCTs (CD011504, `oa_W1775096410`). "Cash-plus food" is the only combination that reliably outperforms cash alone (`oa_W3204861800`).

- **Cost-effectiveness:** *Moderate.* cea_rating_allowed is **true** (143 CEA papers retrieved; 0 registry matches, registry unavailable). However, the retrieved CEA literature does not yield a consolidated cost-per-DALY or ICER for cash transfers against child-nutrition endpoints. The most on-point evidence is a systematic review of economic evaluations of undernutrition interventions (*Health Policy and Planning* 2020, DOI 10.1093/heapol/czaa149) which found 62 economic evaluations (56 cost-effectiveness analyses), dominated by fortification and preventive interventions, and explicitly warned that heterogeneous "off-the-shelf" models make cross-intervention prioritisation difficult — i.e., no clean pooled ICER for cash. A concrete demand-side cost anchor exists for an immunization co-benefit: small mobile CCTs of ~USD 0.8–2.4 per immunization visit (≤USD 15 per fully immunized child) raised full immunization coverage in Karachi (*EClinicalMedicine* 2022). Given real but small anthropometric effects, delivery-cost overhead of cash disbursement, and the absence of a favourable pooled cost-per-DALY specific to nutrition outcomes, **Moderate** is the defensible rating — not "Very High." (No cost-per-DALY figure for the linear-growth effect is present in the corpus — not in corpus.)

- **Government scaling pathway:** Cash transfers have the strongest real-world scaling track record of any intervention in this review. Large national CCT/UCT programs referenced in the corpus — Brazil's Bolsa Família, Mexico's PROGRESA/Oportunidades, Colombia's Familias en Acción (`oa_W1917605324`, `pmid_31666032`), and India's Janani Suraksha Yojana conditional transfer for institutional delivery — already operate at national scale on established social-protection and finance-ministry payment rails, not health-system platforms. This "proven national" delivery is the intervention's decisive strength: the platform and disbursement machinery exist in most target LMICs, so scaling is a matter of targeting, conditionality design, and adding a nutrition "plus" component rather than building new delivery infrastructure.

- **Caveats:**
  - *Version ≠ evidence.* Manley 2020 (`oa_W3115538441`) and Manley 2022 (`oa_W4220654904`) are the **same review lineage** by the same team; 2022 extends the 2018 search and shares the earlier included studies. They are counted here as **one evolving evidence base**, not two independent confirmations — the 2022 estimates supersede/subsume 2020.
  - *Effects are small and heterogeneous.* Both meta-analyses and the cash-plus review explicitly flag high heterogeneity and "small overall" magnitude; HAZ gains (~0.02–0.03 SD) are near the threshold of practical significance.
  - *Underpowered / low-certainty pathways.* Birth-weight and neonatal-mortality evidence is GRADE very-low (`pmid_34590144`); wasting/WAZ effects are inconsistent (borderline or null across `oa_W3115538441`/`oa_W4220654904`); several service-utilisation and MUAC signals rest on single studies (`oa_W4207018050`) and should not be pooled.
  - *No dominant-trial concentration flagged.* Unlike vitamin A (DEVTA), none of the nutrition meta-analyses in the bundle report a single trial dominating the pooled estimate (`dominant_trial` empty across records); the small effect reflects genuine dispersion across many programs, not one outlier.
  - *CEA is indirect.* The cost-effectiveness rating rests on adjacent economic-evaluation literature and a co-benefit (immunization) cost anchor, not a nutrition-specific ICER — hence Moderate, with explicit uncertainty.

## Multiple micronutrient supplementation & fortification for children under 5 and pregnant women  (both under-5 and WRA)

**Evidence: A  |  Cost-effectiveness: Unknown  |  Scalability: Growing  |  Tier 2**

- **Evidence base:** The bundle holds 9 records on this intervention family. Two are quantitative evidence syntheses of primary interest: a Bayesian **network meta-analysis** of 169 RCTs / 302,061 participants (JAMA Network Open, key `pmid_31348509`) and a **Systematic Review & Meta-Analysis** of 197 studies (Nutrients, key `pmid_31973225`). Three further **systematic reviews** are present (Journal of Global Health umbrella SR, `pmid_35003711`; BMC Women's Health economic-consequences SR, `pmid_25887257`; Health Promotion Perspectives India SR, `oa_W4294716244`), plus one **Systematic review & meta-analysis** (Frontiers in Public Health, `pmid_41919290`), one **modeling study** (Health Policy and Planning KIPS/LiST investment framework, `oa_W2588434224`), one **observational cohort** (BMJ Global Health India NFHS decomposition, `oa_W2895885405`), and one **narrative/other review** (Public Health Reviews, `oa_W334494545`). None carries a `journal` of "Cochrane Database of Systematic Reviews", so **no record here is a Cochrane review** (several *cite* Cochrane reviews as inputs). GRADE/certainty is stated in only two records: `pmid_41919290` reports "Low to moderate (GRADE)"; `pmid_25887257` describes its own evidence base as "low" (29 studies, narrative not meta-analytic). The two flagship meta-analyses do not report an overall GRADE grade in the bundle. Direction of effect is consistent across the two flagship syntheses for the core outcomes (anaemia, linear growth, preterm birth), supporting an **A** grade with the caveat that effects are intervention- and outcome-specific rather than uniform.

- **Effect sizes** (all with corpus key attached; all-cause vs cause-specific kept separate):

  *Maternal multiple micronutrients (MMN) in pregnancy — birth outcomes (`pmid_31348509`, random-effects Bayesian NMA):*
  - Preterm birth: OR 0.54 (95% CrI 0.27–0.97) vs standard of care.
  - Mean birth weight: MD 0.08 kg (95% CrI 0.00–0.17).
  - Iron+calcium (comparator arm in same network): preterm birth OR 0.16 (95% CrI 0.03–0.87); calcium alone OR 0.76 (95% CrI 0.56–0.98).
  - **Note on the apparent MMN discrepancy** (`pmid_31348509` full text): the OR 0.54 for MMN vs standard of care contrasts with a Cochrane MMN review's RR 0.95 (95% CI 0.90–1.01) for preterm birth *cited within this paper (not a corpus record)*; the authors reconcile this by noting the Cochrane comparison was MMN vs "iron ± folic acid", whereas their NMA compared MMN vs standard of care. When compared head-to-head against IFA in their own network, MMN gave OR 0.90 (95% CrI 0.78–1.01) — i.e. no clear advantage over IFA. This is a comparator-definition effect, not a genuine effect-size conflict.

  *Direct child MMN — linear growth (`pmid_31348509`):*
  - LAZ during exclusive breastfeeding (child MMN): MD 0.20 (95% CrI 0.03–0.35); maternal MMN in the same window was null (MD −0.02, 95% CrI −0.18–0.14).
  - HAZ during complementary feeding (child MMN): MD 0.14 (95% CrI 0.02–0.25).

  *Anaemia — all random-effects RRs from `pmid_31973225`:*
  - Iron: RR 0.55 (95% CI 0.44–0.70; 28 studies; I²=82%).
  - MMN: RR 0.69 (95% CI 0.56–0.85; 14 studies; I²=79%).
  - Iron-folic acid: RR 0.80 (95% CI 0.66–0.97; I²=65%).
  - MNP (micronutrient powders), efficacy: RR 0.76 (95% CI 0.69–0.84; 34 studies; I²=75%).

  *Growth / stunting (`pmid_31973225`):*
  - LNS (lipid-based nutrient supplement), stunting: RR 0.90 (95% CI 0.84–0.96; 15 studies; I²=40%) — LNS was the only strategy in this review to improve stunting and underweight; MMN only slightly increased length-for-age (MD 0.09, 95% CI 0.00–0.17).

  *Cause-specific morbidity (`pmid_31973225`):*
  - Zinc, diarrhoea incidence: RR 0.89 (95% CI 0.82–0.97; 31 studies; I²=86%). Zinc had **no** significant effect on anaemia, stunting, wasting, or all-cause mortality.

  *All-cause mortality — vitamin A (kept explicitly separate; `pmid_31973225`):*
  - Cumulative-incidence pooling: RR 0.90 (95% CI 0.80–1.02; I²=26%) — upper CI just crosses 1.0. **Dominant-trial flag:** although this record's `dominant_trial` field is empty, the full text states one cluster-RCT in north India contributed **122,813 deaths within a 5-year trial** to the risk-ratio pool — this is the DEVTA-class dominance pattern flagged in the project's VAS audit. The rate-ratio pooling showed no effect. The review notes its 10% estimate is "consistent with" a Cochrane VAS review's RR 0.88 (95% CI 0.83–0.93) *cited within the paper (not a corpus record)*, the difference driven by post-1995 date restrictions excluding older trials. **Do not treat the RR 0.88 figure as corpus-grounded** — it is a citation inside `pmid_31973225`, not an independent record here.
  - Cause-specific vitamin A pathways from the modeling record `oa_W2588434224` (values imported by that paper from prior meta-analyses, used as LiST inputs — traceable to the corpus record but not that paper's own estimates): diarrhoea incidence RR 0.85 (95% CI 0.82–0.87); diarrhoea mortality RR 0.72 (95% CI 0.57–0.91). These are narrower cause-specific pathways and should be read as model inputs, not fresh pooled evidence.

  *Population-level / observational (`oa_W2895885405`, India NFHS-3→NFHS-4):* child anaemia fell 11 percentage points and pregnant-woman anaemia 7.6 points (2006→2016); child Hb +4.5 g/L (95% CI 4.17–4.84); coverage of nutrition/health interventions (ANC, IFA, deworming, vitamin A, ICDS) explained 18% of the child Hb change in decomposition. This is ecological/associational, not causal.

  *Modeled projection (`oa_W2588434224`):* scaling the KIPS bundle to 90% coverage plus nutrition-sensitive gains is projected to yield **65 million fewer stunted children by 2025** (from a 159-million 2015 baseline, via the Lives Saved Tool). This is a modeled figure, not a measured effect.

- **Mechanism of action:** Micronutrients (iron, folic acid, vitamin A, zinc, iodine, and combined MMN) correct deficiencies that impair haematopoiesis (anaemia), linear growth, immune function, and — for maternal supplementation — placental/fetal growth, lowering preterm birth and raising birth weight. Different micronutrients act on different pathways, which is why the bundle shows outcome-specific effects: iron/MMN/MNP/fortification act on anaemia; LNS (energy + micronutrients in a food base) on stunting/underweight; zinc on diarrhoea; vitamin A on infection-mediated mortality. No single formulation improves all outcomes (`pmid_31973225` key finding).

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is **false** and `cea_record` is **null**, so per the CEA guard no cost-effectiveness rating may be assigned. Note: `pmid_25887257` reports downstream *economic-return* associations (e.g. up to +46% adult wages after early childhood protein supplementation in Guatemala/INCAP; +20% adult income men / +6% women after maternal iron in Indonesia; +0.82 additional schooling years for girls after in-utero iodine in Tanzania) and `oa_W2588434224` reports financing needs (annual cost rising from US$2.6bn to US$7.4bn; US$39.2bn shortfall under business-as-usual). These are income/productivity and budget figures, **not** ICERs or cost-per-DALY, so they cannot support a cost-effectiveness rating and are reported here only as context.

- **Government scaling pathway:** Strong platform fit. Delivery vehicles already embedded in LMIC government systems appear across records: antenatal care and IFA supplementation, large-scale staple-food fortification (wheat flour via public distribution system in Tamil Nadu/Punjab, `oa_W4294716244`), micronutrient powders and LNS through health-facility/community platforms (`pmid_31973225`), and India's ICDS (`oa_W2895885405`). Fortification is highlighted as the recommended long-term, government-mandatable strategy (`pmid_31973225`, `oa_W334494545`). The KIPS investment framework (`oa_W2588434224`) is explicitly a national-scale-up model. Scalability is rated **Growing** rather than "Proven national" because the corpus documents real programmatic delivery (India fortification, ICDS) but the flagship effect evidence is dominated by efficacy trials, and full national scale-up in the modeling record is projected, not yet achieved, and requires a multi-fold financing increase.

- **Caveats:**
  - **Version/overlap:** no record carries a `cochrane_id`, so no version-collapse is needed within this bundle; but two records (`pmid_31348509`, `pmid_31973225`) *cite* overlapping Cochrane VAS/MMN reviews — those cited figures (Cochrane VAS RR 0.88; Cochrane MMN RR 0.95) are **not corpus records** and must not be counted as independent evidence.
  - **Dominant trial / all-cause mortality fragility:** the vitamin A all-cause mortality RR 0.90 (`pmid_31973225`) is heavily influenced by a single north-India cluster-RCT contributing 122,813 deaths (DEVTA-class dominance); the upper CI crosses 1.0 and the rate-ratio pooling was null. This is the genuinely fragile pathway, not the anaemia or linear-growth findings.
  - **Underpowered / inconsistent pathways:** cause-specific vitamin A mortality pathways (diarrhoea/measles) are, as flagged project-wide, thinner; here they enter only as modeling inputs (`oa_W2588434224`). Zinc showed no mortality or nutritional-status benefit despite a diarrhoea effect (`pmid_31973225`). MNPs carried a 30% increased diarrhoea risk (RR 1.30, 95% CI 1.11–1.53, `pmid_31973225`) — a safety signal, not a benefit.
  - **Heterogeneity:** anaemia analyses in `pmid_31973225` carry high I² (65–86%); the Frontiers record `pmid_41919290` reports HRs from a mix of intervention and observational data and its notes flag formulaic/AI-generated phrasing — its effect sizes (e.g. rickets HR 1.51, 95% CI 1.26–1.82) are treated at face value and weighted cautiously.
  - **Study-type discipline:** `oa_W2588434224` is a modeling study and `oa_W2895885405` is observational; their headline figures (65M fewer stunted children; 11-point anaemia drop) are model/ecological outputs and must not be read as pooled trial effects.
  - **Economic figures are not CEA:** the +46% wage / financing figures above are downstream-return and budget numbers, not cost-effectiveness ratios; the cost-effectiveness rating remains Unknown.

## Balanced Energy-Protein (BEP) Supplementation in Pregnancy  (women of reproductive age; offspring birth outcomes)

**Evidence: A  |  Cost-effectiveness: High  |  Scalability: Requires investment  |  Tier 2**

- **Evidence base:** The bundle holds 6 on-topic records: 3 meta-analyses, 1 systematic review (scoping), and 2 primary/protocol RCTs. The meta-analytic tier is:
  - **Individual participant data meta-analysis** of 11 RCTs in 8 LMICs, N=12,549 — study type **"Meta-analysis"**, *PLoS Medicine* 2025 (PMID 39899474).
  - **Systematic review & meta-analysis** of 15 LMIC trials — study type **"Systematic review & meta-analysis"**, *Campbell Systematic Reviews* 2021 (PMID 37131924). This is a **Campbell Collaboration review, NOT a Cochrane review** (journal is "Campbell systematic reviews").
  - **Systematic Review & Meta-Analysis** of 7 RCTs in undernourished women, N=2,367 — study type **"Systematic Review & Meta-Analysis"**, *Maternal & Child Nutrition* 2015 (PMID 25857334).
  - Supporting **Systematic review** (scoping, not GRADE-assessed, no pooled estimates) of 21 trials/programmes — *Maternal and Child Nutrition* 2024 (key oa_W4400205023).
  - Two **RCT** records from the Nepal LBWSAT programme: the results paper (*PLoS ONE* 2018, key oa_W2799402066) and its protocol (*BMC Pregnancy and Childbirth* 2016, key oa_W2534157601, no results reported).

  Effects are **directionally consistent across the three meta-analyses** for maternal weight gain and birth outcomes, with effect magnitude larger in undernourished/targeted subgroups. Certainty is **low-to-moderate (GRADE, varies by outcome)** per the Campbell review (PMID 37131924); the 2015 MA rated component trials mixed (2 strong, 3 moderate, 2 weak per EPHPP) (PMID 25857334); the scoping review was not GRADE-assessed (oa_W4400205023). Grade **A** is supported by multiple consistent meta-analyses, tempered by heterogeneous certainty.

- **Effect sizes** (all corpus-grounded; maternal, birth, and mortality outcomes kept separate):

  *Maternal — gestational weight gain (GWG), IPD MA, random-effect, PMID 39899474:*
  - GWG percent adequacy: **MD +5.87 percentage points (95% CI 2.18 to 9.56)**, 11 studies, N=12,549.
  - Total GWG at delivery: **MD +0.59 kg (95% CI 0.12 to 1.05)**, 10 studies, N=12,290.
  - Severely inadequate GWG: **RR 0.90 (95% CI 0.83 to 0.99)**; inadequate GWG: **RR 0.93 (95% CI 0.89 to 0.97)**.
  - Excessive GWG: **RR 1.16 (95% CI 0.99 to 1.37)** — not significant (PMID 39899474, full text).
  - Effect was larger in the **targeted-delivery subgroup**: GWG percent adequacy MD **+16.02 (95% CI 12.00 to 20.03)**, 2 studies (PMID 39899474, full text).

  *Birth outcomes — Campbell MA, PMID 37131924:*
  - Birth weight: **MD +107.28 g (95% CI 68.51 to 146.04)**, 8 studies, N=2,190.
  - Low birth weight: **RR 0.60 (95% CI 0.41 to 0.86)**, 3 studies, N=1,830.
  - Small-for-gestational-age: **RR 0.71 (95% CI 0.54 to 0.94)**, 5 studies, N=1,844.

  *Birth weight — 2015 MA in undernourished women, PMID 25857334 (standardized):*
  - Pooled birthweight: **SMD 0.20 (95% CI 0.03 to 0.38)** across 7 RCTs, N=2,367 — significant overall, but **null in both subgroup analyses** (vs no-intervention control SMD 0.41, 95% CI −0.08 to 0.90; vs alternative-supplement control SMD 0.17, 95% CI −0.06 to 0.40), and **null for birth length** (SMD 0.22, 95% CI −0.04 to 0.50) and **head circumference** (SMD 0.17, 95% CI −0.07 to 0.41).

  *Mortality — cause-specific vs all-cause (report separately; these are underpowered single-study estimates from the scoping review, oa_W4400205023, not pooled):*
  - Stillbirth (Campbell MA, PMID 37131924): **RR 0.39 (95% CI 0.19 to 0.80)**, 3 studies, N=1,913.
  - Perinatal mortality (Campbell MA, PMID 37131924): **RR 0.50 (95% CI 0.30 to 0.84)**, 1 study, N=1,446 — **single trial, underpowered; treat with caution.**
  - Neonatal mortality signals are **inconsistent and single-trial**: WINGS multi-component intervention IRR 0.52 (95% CI 0.29 to 0.95, benefit) vs Women First trial RR 1.79 (95% CI 1.08 to 2.97, **harm**) (both oa_W4400205023). No pooled all-cause mortality estimate exists in this corpus — this pathway is **genuinely thin**.

  *Nutrition-sensitive delivery (Nepal LBWSAT RCT, oa_W2799402066):* PLA women's groups **plus food** raised birthweight by **+78 g (95% CI 13.9 to 142.0)** vs control (N=626); PLA **alone** (+28.9 g, 95% CI −37.7 to 95.4) and PLA **plus cash** (+50.5 g, 95% CI −15.0 to 116.1) were null — the food transfer, not the groups or cash, drove the effect. Downstream child weight-for-age at 0–16 months was null (food arm MD −0.033, 95% CI −0.121 to 0.056).

- **Mechanism of action:** BEP supplements provide additional dietary energy with protein contributing ≤25% of energy (often as lipid-based nutrient supplements, fortified blended flours, milk-based beverages, or local snacks), frequently co-formulated with micronutrients. In energy-constrained pregnancies this raises maternal gestational weight gain and, downstream, fetal growth — reducing low birth weight and SGA. Benefit concentrates in **undernourished/food-insecure women** (the targeted subgroup shows the largest GWG effect; PMID 39899474), consistent with a nutrient-repletion rather than pharmacologic mechanism.

- **Cost-effectiveness (grounded in cea_record; cea_rating_allowed = true; 89 CEA papers, 0 registry matches):**
  - **Directly on-intervention:** A dynamic microsimulation across India, Pakistan, Mali, and Tanzania (*PLoS Medicine* 2022, PMID 35192606) found **MMS + targeted BEP** vs baseline IFA cost **$54 (95% UI $32–77) per DALY averted in Pakistan, $73 ($40–104) in Mali, $83 ($58–111) in India, and $245 ($127–405) in Tanzania**, averting more DALYs than universal MMS while remaining cost-effective.
  - **Supporting food-supplementation CEAs (Bangladesh MINIMat):** early prenatal food + micronutrient supplementation averted one DALY at **US$24** (openalex W2786565366, *PLoS ONE* 2018) and one life-year saved at **US$27–34** for government/NGO delivery (PMID 26018633, *BMC Pregnancy and Childbirth* 2015).
  - These ICERs sit well below typical LMIC GDP-per-capita willingness-to-pay thresholds, supporting a **High** rating. It is not rated Very High because the strongest direct estimate is for **BEP targeted alongside MMS** (not standalone universal BEP), and the standalone food-supplement CEAs come from a single setting (Bangladesh MINIMat).

- **Government scaling pathway:** BEP fits the **antenatal care (ANC) platform** — the same delivery channel used for IFA/MMS — so it can piggyback on existing ANC contacts, supply chains, and community health worker networks. The evidence and CEA both point to **targeted delivery** (undernourished / low-BMI women) as the efficient strategy rather than universal provision (PMID 39899474; PMID 35192606). Nutrition-sensitive variants can be delivered via women's-group platforms combined with **food transfers**, which outperformed cash or groups alone in Nepal (oa_W2799402066). Rated **Requires investment**: procurement/formulation of energy-protein supplements, targeting/screening logistics, and cold-or-dry supply chains are heavier than a micronutrient tablet, and no record here documents an at-scale national BEP programme.

- **Caveats:**
  - **Version/overlap:** No shared cochrane_id (none of the records is Cochrane), but the three meta-analyses **share primary trials** (e.g. Ceesay 1997, Huybregts 2009, Kardjati/Tontisirin, Mora, Girija appear across PMID 37131924, PMID 25857334, and the IPD MA PMID 39899474). They are **not independent evidence generations** — the same historical LMIC BEP trials are re-pooled. No single dominant trial was flagged (dominant_trial empty across records).
  - **Underpowered pathways:** perinatal mortality (single trial, PMID 37131924) and neonatal mortality (conflicting single-trial signals including a harm signal in Women First, oa_W4400205023) are **cause-specific/mortality outcomes that are thin and should not be reported as robust**. The solid finding is **maternal GWG and birth-weight/LBW/SGA**, not mortality.
  - **Heterogeneity & conditionality:** the 2015 MA (PMID 25857334) shows birthweight benefit is significant only in the pooled all-trials analysis and **dissolves in both subgroups**, and effects are stronger in undernourished/targeted populations — benefit is **conditional on baseline undernutrition**, not universal.
  - **Design limits:** one RCT record (oa_W2534157601) is a **protocol only** with no results; the 2024 review (oa_W4400205023) is a **scoping review with no pooled estimates** and was not GRADE-assessed.

## Small-Quantity Lipid-Based Nutrient Supplements (SQ-LNS)  (children under 5 & women of reproductive age, LMIC)
**Evidence: A  |  Cost-effectiveness: High  |  Scalability: Requires investment  |  Tier 2**

- **Evidence base:** The bundle holds 6 on-topic records: 2 meta-analyses, 2 RCTs, 1 narrative/other review, and 1 cross-sectional study. The two meta-analyses anchor the evidence and target different populations:
  - **Child linear growth** — a *Meta-Analysis* (Scientific Reports, 2025; PMID 41125609) pooling 15 SQ-LNS RCTs / 18 comparisons, N=36,970, across 10 LMICs. It closely re-uses the Dewey et al. 2021 SQ-LNS trial set, so it should be counted as **one** body of trial evidence, not an independent generation.
  - **Prenatal / birth outcomes** — an individual-participant-data *Systematic Review & Meta-Analysis* (Am J Clin Nutr, 2024; PMID 39154665) of 4 LMIC RCTs (Bangladesh, Ghana, Malawi, Guatemala), **GRADE moderate** for SQ-LNS vs IFA/standard-of-care and **GRADE low** vs multiple micronutrient supplements (only 2 trials).
  The remaining records are supporting/mixed: PROCOMIDA (RCT, J Nutr 2018; DOI 10.1093/jn/nxy138), the Chad RUSF cluster-RCT (PLoS Med 2012; DOI 10.1371/journal.pmed.1001313), a narrative review (Proc Nutr Soc 2017; PMID 28285607) that judged single-trial evidence "inconclusive," and a small cross-sectional Uganda study (BMC Nutrition 2017; DOI 10.1186/s40795-017-0140-8). Consistency is high for the pooled linear-growth and birth-outcome signals; single trials of full food-supplement packages are more mixed.

- **Effect sizes** (all-cause growth/anthropometry — no all-cause mortality outcome is reported in the bundle; mortality effects are *not in corpus*):
  - *Child linear growth (PMID 41125609, fixed-effect):* pooled LAZ mean difference **0.15 (95% CI 0.12, 0.17)**, I²=59% (95% CI 21, 74); height-age MD **11.5 days (95% CI 9.4, 13.5)**, I²=60%. The paper reports random-effects sensitivity analyses did not change direction/interpretation (exact random-effects estimates *not separately reported in corpus*). Its novel Proportion-of-Maximal-Benefit metric was **11% (95% CI 9.4, 12)** with I²=90% — high between-trial heterogeneity. **Dominant/notable trial:** iLiNS-Zinc (Burkina Faso) carried the largest single-trial LAZ effect (LAZ MD 0.25–0.27 vs passive control per full text); the Haiti trial was an outlier where height-age MD (24 days) diverged from LAZ MD (0.04) due to baseline age imbalance.
  - *Prenatal SQ-LNS vs IFA/SOC (PMID 39154665):* birth weight MD **+48.7 g (95% CI 26.1, 71.2)**; low birth weight **RR 0.89 (95% CI 0.80, 0.99)**; newborn stunting **RR 0.83 (95% CI 0.74, 0.93)**; underweight at 6 mo prevalence ratio **0.85 (95% CI 0.73, 0.99)**. Preterm birth was **null (RR 0.94, 95% CI 0.80, 1.10)**. Full text states fixed- and random-effects models produced identical estimates for nearly all outcomes (low heterogeneity). Effects were generally larger in female infants.
  - *Prenatal SQ-LNS vs MMS (PMID 39154665, GRADE low, 2 trials):* head-circumference-for-gestational-age z-score MD **0.11 (95% CI −0.01, 0.23)** — the only outcome approaching significance vs MMS; SQ-LNS was **not** shown superior to MMS on birth outcomes.
  - *Supporting single trials:* Chad RUSF (DOI 10.1371/journal.pmed.1001313) did **not** reduce wasting (IRR 0.86, 95% CI 0.67, 1.11) but improved linear-growth velocity (0.03 HAZ/mo, 95% CI 0.01, 0.04), anemia (OR 0.52, 95% CI 0.34, 0.82), and reduced diarrhea (IRR 0.71, 95% CI 0.63, 0.80) and fever (IRR 0.77, 95% CI 0.70, 0.86). In PROCOMIDA (DOI 10.1093/jn/nxy138) the **LNS individual ration showed no significant stunting effect** (−3.0 pp, CIs not reported), while CSB (−11.1 pp) and MNP (−6.5 pp) rations did — a cautionary within-trial signal that LNS is not uniformly the best-performing supplement in a full food-assisted package.

- **Mechanism of action:** SQ-LNS (~20 g/d for children; a fortified peanut/oil/milk-powder paste) delivers essential fatty acids plus a full micronutrient package in a small, energy-dense, ready-to-eat vehicle added on top of the normal diet. In pregnancy it supplies maternal micronutrients and energy to support fetal growth (birth weight, newborn linear growth). In infancy/early childhood it fills the nutrient gap during the 6–24-month complementary-feeding window to reduce linear-growth faltering, anemia, and, per the CEA modelling paper, mortality and developmental disability.

- **Cost-effectiveness:** **High.** Grounded in the Uganda modelling study (OpenAlex W4386045834): delivering SQ-LNS daily to all children in rural Uganda (>1 million) for 12 months (6–18 mo) via the Village Health Team system would cost **~$52/child (2020 USD)** (~$58.7M/yr), averting >242,000 DALYs annually (3,689 deaths, >160,000 anemia cases, ~6,000 developmental-disability cases), for an estimated **$242 per DALY averted** — the paper concludes SQ-LNS may be more cost-effective than MNP or complementary food, but total program cost is high. Corroborating: a 129-country Optima Nutrition analysis (OpenAlex W3098882970) reports lipid-based supplements as a high-impact stunting intervention but at a relatively high average **cost per stunting case averted of $1,795** when added to an expanding package. The two figures are consistent — cheap per DALY, more expensive per stunting case, and expensive in aggregate at universal coverage.

- **Government scaling pathway:** Delivery fits existing community-health platforms — the Uganda model routes SQ-LNS through Village Health Teams, and PROMIS (PMID 28274214) integrated SQ-LNS with acute-malnutrition screening on community (Mali) and facility (Burkina Faso) platforms. Realistic scaling levers named in the corpus: targeting the most vulnerable populations and eliminating taxes on SQ-LNS to improve financial feasibility (W4386045834). The main barrier is commodity cost and supply chain at universal coverage, so this reads as **Requires investment** rather than proven national scale-up.

- **Caveats:**
  - **Version/overlap:** The 2025 growth meta-analysis (PMID 41125609) is a methodological re-analysis built on the Dewey et al. 2021 trial set — the same underlying RCTs — so it does not constitute independent replication; count the growth evidence once.
  - **Heterogeneity:** Growth outcomes show moderate-to-high between-trial heterogeneity (LAZ I²=59%, PMB I²=90%); effects are context-dependent on trial duration, SQ-LNS dose/composition, and baseline population (echoed by the "inconclusive" narrative review, PMID 28285607).
  - **Underpowered / weaker pathways:** SQ-LNS vs MMS in pregnancy rests on only 2 trials (GRADE low) with no clear superiority; wasting was null in the Chad RCT; and the Uganda cross-sectional study (small n=122, non-randomized) is associational only. No all-cause **or** cause-specific mortality outcome is present in the retrieved effect data — mortality benefits are asserted only in the CEA modelling paper's inputs, not measured in this bundle.

## Multisectoral & nutrition-sensitive intervention packages  (children under 5 & women of reproductive age)

**Evidence: B  |  Cost-effectiveness: Unknown  |  Scalability: Growing  |  Tier 2**

- **Evidence base:** The bundle holds 43 papers, but they are heterogeneous and mostly *not* effectiveness trials of a single intervention. By verbatim study type there are only **two systematic reviews reporting pooled/synthesized effect estimates for multisectoral packages** — Das et al. 2025 (*Nutrition reviews*, "Systematic review & meta-analysis"; `pmid_40220307`) and the Lancet Global Health double-burden review (`pmid_38301666`, "Systematic Review", vote-counting not meta-analysis) — plus **one Cochrane review** of a delivery platform (IMCI, *The Cochrane database of systematic reviews*, `pmid_27378094`, `cochrane_id CD010123`). The remainder are systematic/scoping reviews without pooled effects (`oa_W3135752043`, `oa_W2979564905`, `oa_W2735715117`, `pmid_19426470`, `pmid_32889522`), **3 RCTs** (two are protocols with no results — `oa_W2883672169`, `oa_W2162780252` — and one reporting trial, Sugira Muryango, `oa_W3123264537`), **5 modeling studies** (Optima Nutrition / LiST projections), and a large body of **observational decomposition / policy-tracing "Stories of Change" case studies** (Ghana, Nepal, Nigeria, India, Ethiopia, Indonesia). Consistency is *mixed*: the direction of benefit is fairly consistent for integrated delivery and package scale-up, but pooled effects are small, borderline, or null, and most "effects" are correlational trend decompositions rather than causal estimates. GRADE/certainty where stated is **low-to-moderate** (IMCI: "Low to moderate (GRADE); mortality low-certainty, wasting moderate-certainty"; Das 2025: "Mixed; 12 of 68 studies high quality, 30 moderate, 7 low"). This supports an **Evidence B** (some MA/SR, mixed or conditional), not A.

- **Effect sizes** (all-cause vs cause-specific / anthropometric outcomes kept separate; corpus keys attached):

  *Integrated nutrition–health–immunization delivery (SR & MA, conflict-affected LMIC; `pmid_40220307`):*
  - Underweight (WAZ), children <5: **OR 0.72 (95% CI 0.57–0.92)**, random effects, 3 studies / n=1,515 — a 28% reduction in odds. (`pmid_40220307`)
  - Stunting (HAZ), children <5: **OR 0.88 (95% CI 0.78–1.00)**, random effects, 5 studies / n=5,661; P=.05, I²=22% — **borderline** significant. (`pmid_40220307`)
  - Wasting (WHZ), children <5: **no significant effect** (OR not estimable/null), 4 studies / n=4,795. (`pmid_40220307`)

  *IMCI / IMNCI delivery platform (Cochrane review CD010123; `pmid_27378094`) — all-cause mortality vs anthropometry separated:*
  - Under-five mortality (all-cause): **RR 0.85 (95% CI 0.78–0.93)**, post-hoc pooled 2 trials / n=65,570 (dominant trial **Arifeen 2009, Bangladesh**). (`pmid_27378094`)
  - Child mortality (Bangladesh trial alone): **RR 0.87 (95% CI 0.68–1.10)** — null. (`pmid_27378094`)
  - Infant mortality: **HR 0.85 (0.77–0.94)**; Neonatal mortality: **HR 0.91 (0.80–1.03)** — null (Bhandari 2012, India). (`pmid_27378094`)
  - Stunting: **RR 0.94 (0.84–1.06)** — null; Wasting: **RR 1.04 (0.87–1.25)** — null. (`pmid_27378094`) i.e. mortality benefit but **no effect on nutritional status**.

  *Maternal/newborn community delivery (SR, stillbirths; `pmid_19426470`):*
  - Perinatal mortality, trained vs untrained TBAs: **OR 0.70 (0.59–0.83)**, 4 studies / n≈27,000 (dominant trial **Jokhio et al., Pakistan**; stillbirth aOR 0.69, 0.57–0.83). (`pmid_19426470`)
  - Community-based intervention packages: perinatal mortality **RR 0.71 (0.61–0.84)**; stillbirths **RR 0.87 (0.73–1.03)** — null. (`pmid_19426470`)
  - Antenatal social support (Hodnett Cochrane, cited within): stillbirth/neonatal death **RR 1.15 (0.89–1.51)** — null. (`pmid_19426470`)

  *Reporting RCT — Sugira Muryango parenting + social protection, Rwanda (`oa_W3123264537`):*
  - ASQ-3 gross motor: **MD 0.294 SD (0.118–0.470)**; communication **0.139 (0.009–0.268)**; problem-solving **0.159 (0.035–0.282)** at 12 mo, n=1,049. (`oa_W3123264537`)
  - Harsh discipline IRR **0.741 (0.657–0.835)**; IPV IRR **0.616 (0.458–0.828)**. (`oa_W3123264537`)
  - **Child growth (HAZ/WAZ/WHZ/MUAC): null** — no significant anthropometric effect. (`oa_W3123264537`)

  *Double-burden SR (vote-counting, not MA; `pmid_38301666`):* food/supplement-based MCH interventions reduce undernutrition but carry an **overnutrition signal** — large-for-gestational-age **OR 1.58 (1.04–2.38)** with prenatal micronutrients (Burkina Faso); 89% (52–99%) of overnutrition outcomes worsened across 9 supplement studies; CCT (Mexico Oportunidades) stunting −10% and overweight −8% (both "significant" per review, no CI reported → *CIs not in corpus*). (`pmid_38301666`)

  *Modeling (package scale-up, not empirical) — for context only:* Optima Nutrition 129-country model attributes stunting impact largely to IPTp + IYCF education + vitamin A + LNS, with cost-per-stunting-case-averted **US$267 (IYCF education)** to **US$1,989 (vitamin A, wasting)** (`oa_W3098882970`); Osendarp/COVID model projects **+9.3M wasting (6.44–13.62M)**, **+168,000 under-5 deaths (47,000–283,000)** absent mitigation (`oa_W3183654847`). These are **model outputs, not effect sizes.**

- **Mechanism of action:** "Multisectoral" is not one biological mechanism but a **convergence strategy**: nutrition-specific inputs (IYCF/breastfeeding, micronutrients, supplementary/therapeutic feeding) are combined with nutrition-sensitive drivers (WASH/reduced open defecation, maternal education, antenatal/facility care, social protection/cash transfers, food security). The pathway to stunting/anaemia reduction runs through improved dietary intake *and* reduced infection/enteric burden *and* raised household wealth and caregiver knowledge — which is why the population-level decompositions (Nepal `pmid_32889522`: parental education ~20–30%, maternal nutrition ~14–20%; Nigeria `oa_W4220686575`; India `oa_W4223641438`: health/nutrition coverage 11–23% of decline) attribute change to *bundles* of determinants rather than any single input. The delivery mechanism is a shared platform (community health workers/FCHVs, ANC/PNC, immunization contacts) that co-locates several interventions.

- **Cost-effectiveness: Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is **false** and `cea_record` is **null**; per the CEA guard, no rating is assigned. (Note: modeling papers in the corpus report cost figures — e.g. package cost per DALY averted US$141–143 in Nigeria/DRC, `oa_W2404704713`; cost per stunting case averted US$267–1,989, `oa_W3098882970` — but these are model outputs for specific single interventions or bundled packages, **not** a validated CEA of "multisectoral packages" as an intervention class, so they cannot ground a cost-effectiveness rating here.)

- **Government scaling pathway:** This is the category's genuine strength. Every national success story in the bundle is government-led and platform-based: Ethiopia's MDG-4 achievement via the health extension programme + Productive Safety Net Programme (`oa_W2763443614`), Nepal's FCHV-delivered vitamin A/IFA/salt iodization + MSNP (`oa_W3201152902`, `pmid_32889522`), Ghana's IYCF/WASH/social-protection mix (`oa_W3211819176`), and India's four-state convergence model (`oa_W4223641438`). Platform fit is high — the interventions ride existing ANC/PNC, immunization, community-health-worker, and social-protection systems. The implementation-science reviews (`oa_W3135752043`, `oa_W4362467295`) identify the real constraints: inadequate human resources/training (barrier in 38% of studies), weak monitoring/evaluation (17.6%), inadequate funding (14.7%), and the need for strong intersectoral coordination and a **costed national nutrition plan** (absent in Ghana, `oa_W4226031647`). Hence **Scalability: Growing** with substantial investment/coordination required — proven subnationally and nationally in several countries but dependent on governance quality and funding.

- **Caveats:**
  - *Version/overlap & double-counting:* Only one Cochrane record (`CD010123`, IMCI) — counted once; no duplicate cochrane_ids. But many records **re-cite the same underlying evidence** (Optima Nutrition / LiST outputs recur across `oa_W3183654847`, `oa_W3098882970`, `oa_W2763443614`, `oa_W2404704713`; several Nepal/Ghana case studies overlap sources) — apparent robustness is inflated by shared modeling machinery, not independent trials.
  - *Design ceiling:* the strongest causal evidence (2 RCTs that report) shows **null anthropometric/growth effects** (Sugira Muryango; IMCI stunting/wasting); benefits concentrate on mortality (IMCI, TBA training) and child development (parenting), not on the nutrition status this synthesis targets. Most "effects" are **ecological/decomposition correlations**, not attributable to a defined intervention.
  - *Underpowered / null cause-specific and anthropometric pathways:* wasting (`pmid_40220307` null, 4 studies), stunting borderline (OR 0.88, CI touches 1.00), community-package stillbirths null (RR 0.87, 0.73–1.03).
  - *Harm signal:* food/supplement-based MCH interventions carry an overnutrition/LGA risk (OR 1.58, 1.04–2.38; `pmid_38301666`) — the "double burden" trade-off.
  - *Heterogeneity:* 25 countries, conflict and non-conflict settings, and widely varying package compositions; Das 2025 quality mixed (only 12/68 high). External figures (e.g. US$10.3bn to scale, ~1.1M lives — cited to Shekar in `oa_W2399542084`) are **not independently in corpus** and must not be treated as validated.

## Maternal Nutrition — Antenatal Supplementation, Counselling & Preconception Care (women of reproductive age; some infant/child outcomes)

**Evidence: B  |  Cost-effectiveness: Unknown  |  Scalability: Requires investment  |  Tier 2**

This is a heterogeneous "other maternal nutrition" bucket spanning balanced protein-energy (BPE) supplementation, multiple-micronutrient supplementation (MMS/MMN), lipid-based nutrient supplements (LNS), single-vitamin supplementation, calcium and iron in pregnancy, antenatal/preconception nutrition counselling, and dietary-diversity work. It is *not* a single intervention, so the ratings below reflect the strongest coherent signals (BPE, MMS, calcium, iron) rather than the whole grab-bag; weaker components (dietary education, mental-health, male-involvement, preconception counselling) are flagged as C-level or indirect.

### Evidence base
- **42 records.** By tier: 7 records tagged meta-analysis, 17 systematic review, 11 other-review (narrative/scoping), 4 observational, 2 modeling, 1 other. Population: 33 WRA-only, 7 both, 1 under-5, 1 other.
- Two records are Cochrane reviews (journal = *Cochrane Database of Systematic Reviews*): the community-based supplementary-feeding overview (`pmid_30480324`, CD010578) and treatments for iron-deficiency anaemia (`pmid_21975735`, CD003094). Several other umbrella reviews cite Cochrane pooled estimates second-hand and are labelled by their actual journal (e.g. `oa_W4389168563` is *Campbell Systematic Reviews*, `oa_W4303969006` is *Public Health Nutrition* — despite source metadata mislabelling them "Cochrane Review").
- Consistency is **strong for antenatal BPE and MMS on birth-size outcomes** (multiple independent SRs converge), **strong for iron on anaemia and calcium on pre-eclampsia**, but **mixed-to-null for counselling, single-vitamin, vitamin D, n-3 LCPUFA, and preconception interventions**, and **absent for hard maternal/perinatal mortality**. GRADE certainty where stated ranges very-low to high; the highest-certainty estimates are MMS on LBW/stillbirth (rated high in `pmid_37331760`).

### Effect sizes (all-cause/birth-size vs cause-specific separated)

**Balanced protein-energy (BPE) supplementation in pregnancy** — the most consistent food-based signal, replicated across two records with identical pooled values:
- LBW: RR 0.68 (95% CI 0.51–0.92), 5 studies, N=4196 (`pmid_37331760`, full text confirmed).
- SGA: RR 0.79 (95% CI 0.69–0.90), 7 studies, N=4408 (`pmid_37331760`; same estimate in `pmid_30480324`).
- Stillbirth: RR 0.60 (95% CI 0.39–0.94), 5 studies, N=3408 (`pmid_37331760`; `pmid_30480324`).
- Preterm birth: RR 0.96 (95% CI 0.80–1.16) — null (`pmid_37331760`).
- Birth weight: MD +40.96 g (95% CI 4.66–77.26), 11 studies, N=5385 (`pmid_30480324`).

**Multiple-micronutrient supplementation (MMS/MMN) vs iron/iron-folic acid:**
- LBW: RR 0.88 (95% CI 0.85–0.91), 18 studies, N=68,801 — high-certainty (`pmid_37331760`, full text).
- SGA: RR 0.92 (95% CI 0.88–0.97), 17 studies, N=57,348 (`pmid_37331760`).
- Stillbirth: RR 0.95 (95% CI 0.86–1.04) — null, high-certainty (`pmid_37331760`).
- Preterm birth: RR 0.95 (95% CI 0.90–1.01) — null (`pmid_37331760`).
- **Dominant-trial / mortality note:** the historical MMN safety concern (peri-/neonatal mortality signal) was resolved by the large Bangladesh **JiVitA-3** trial, which `pmid_37331760` identifies as the key RCT showing no net mortality effect; JiVitA-3's own trial publication is not in this corpus, so it is referenced only through the corpus review. This is the one record with an explicit `dominant_trial` for mortality safety.

**LNS vs MMN:** LBW RR 0.92 (95% CI 0.86–0.98), 4 studies, N=2727 (`pmid_37331760`) — a further small increment over MMN.

**Iron supplementation in pregnancy** (from the reparative-strategies umbrella review, full text confirmed, `oa_W4389374447`):
- Maternal anaemia at term: RR 0.30 (95% CI 0.19–0.46), 14 studies.
- Iron deficiency at term: RR 0.43 (95% CI 0.27–0.66), 7 studies.
- LBW: RR 0.81 (95% CI 0.68–0.97), 11 studies.
- Treatment of established IDA (oral iron vs placebo): incidence of anaemia RR 0.38 (95% CI 0.26–0.55), 1 study N=125 (Cochrane CD003094, `pmid_21975735`).

**Calcium supplementation** (cause-specific — pre-eclampsia pathway, calcium-deficient populations):
- Pre-eclampsia: RR 0.45 (95% CI 0.31–0.65), 13 studies (`oa_W4389374447`, full text); consistent RR 0.48 (95% CI 0.33–0.69), 12 studies, N=15,206 in `pmid_19426467`.
- Severe maternal morbidity/mortality: RR 0.80 (95% CI 0.66–0.98), 4 studies (`oa_W4389374447`).
- **But stillbirth/perinatal death is null:** calcium → stillbirth-or-death-before-discharge RR 0.89 (95% CI 0.73–1.09), 10 studies, N=15,141 (`pmid_19426467`). Anti-platelet agents (aspirin) similarly cut pre-eclampsia (RR 0.83, 95% CI 0.77–0.89) but not perinatal mortality (RR 0.91, 95% CI 0.81–1.03, IPD meta-analysis) (`pmid_19426467`). **Pre-eclampsia prevention does not translate into a demonstrated perinatal-mortality benefit in these pooled data** — an underpowered/inconsistent cause-specific pathway.

**Single-vitamin supplementation** (biomarker, not clinical outcomes) — `pmid_40752545`, meta-analysis, 76 RCTs across 20 LMICs, **low-certainty** (55/73 trials high risk of bias): maternal B-12 deficiency OR 0.43 (95% CI 0.19–0.95); vitamin A deficiency OR 0.55 (95% CI 0.43–0.71); vitamin D deficiency OR 0.30 (95% CI 0.14–0.64). Effects on *infant/cord* concentrations were inconsistent — improves maternal status, unproven downstream benefit.

**Counselling / behavioural (weaker, C-level):** interactive antenatal nutrition counselling raised caloric intake (MD +81.65 kcal, 95% CI 15.37–147.93, moderate certainty) and timely breastfeeding initiation (RR 1.72, 95% CI 1.42–2.09, 1 RCT) but had **no effect on anaemia (RR 0.77, 95% CI 0.50–1.20), stillbirths (RR 0.81, 95% CI 0.52–1.27), or cesarean** (`oa_W4389168563`). Community health-worker educational counselling reduced neonatal mortality (RR 0.87, 95% CI 0.78–0.96, 26 studies) per the reparative review (`oa_W4389374447`). Maternal mental-health interventions raised exclusive breastfeeding (RR 1.39, 95% CI 1.13–1.71, moderate certainty) but showed **null** effects on stunting, underweight, and cognition (`pmid_33070789`).

**Preconception nutrition (South Asia):** micronutrient-only supplementation did *not* significantly change birth size; food supplementation and complex multi-component packages improved outcomes, best when started ≥90 days pre-conception; no meta-analysis was possible (`pmid_40421124`, dominant example Taneja 2022, n=13,500, Delhi). Vitamin D (`pmid_22742603`) and n-3 LCPUFA (`pmid_22742604`) evidence is drawn almost entirely from high-income settings and is flagged `lmic:false` — indirect for this population.

### Mechanism of action
Undernourished mothers enter pregnancy with energy, protein and micronutrient deficits (documented directly here: e.g. pregnant-woman micronutrient adequacy 37% vs 52–57% for mothers-in-law/household heads in rural Nepal, `oa_W2793432169`; 100% calcium-intake inadequacy in Niger, `oa_W2907574845`). BPE and MMS supply the substrate for fetal growth, raising birth weight and cutting SGA/LBW; iron corrects the anaemia that itself predicts LBW (LBW–anaemia OR 3.32, 95% CI 1.14–9.69, `pmid_39889649`); calcium acts on the vascular/pre-eclampsia pathway. Counselling and preconception care work upstream on dietary quality, supplement uptake, and care-seeking — a longer, more diffuse causal chain, which is why their measured biological effects are smaller and less consistent.

### Cost-effectiveness
**Unknown — no CEA record was retrieved for this intervention bucket.** `cea_rating_allowed` is **false** and `cea_record` is **null** in the bundle; per the CEA guard, no rating is assigned. The corpus does contain a CEA-methodology systematic review (`pmid_33280036`) reporting nutrition ICERs (e.g. zinc fortification $226–594/DALY in China; zinc supplementation $14–55/DALY; therapeutic zinc $40/DALY in Tanzania) — but these are **zinc/fortification illustrations, not evaluations of BPE/MMS/calcium/iron/counselling**, and that review's central finding is that ICERs for the same intervention vary by orders of magnitude with costing perspective. So no defensible cost-effectiveness figure can be attached to this bucket from the corpus.

### Government scaling pathway
The core supplements ride existing platforms: **antenatal care (ANC) contacts** for MMS, calcium and iron-folic acid, and **community health workers / women's groups** for counselling and food supplementation. Platform fit is strong in principle but coverage and quality are the binding constraints in the corpus: ANC4+ coverage only 44.1% in rural Burkina Faso (`oa_W2805467408`); ~20% ANC underutilisation in Indonesia with 55% population-attributable risk from low wealth + low education (`oa_W2031361998`); nutrition counselling delivered at only 44% of first ANC visits in Malawi and under-delivered globally (`oa_W4303969006`, 37-study gap analysis). Intensive multi-platform counselling (facility + community) *did* improve dietary diversity and cut household food insecurity (e.g. −22.3 pp food insecurity, Bangladesh) but such packages are project-run and hard to scale; two South Asian preconception packages delivered via **government CHWs** were the exceptions flagged as scalable (`pmid_40421124`). Net: proven supplements need investment in ANC reach/quality and equitable targeting, hence **Requires investment**.

### Caveats
- **Bucket, not intervention.** Ratings are anchored on BPE/MMS/calcium/iron; counselling, mental-health, male-involvement, vitamin D, n-3 LCPUFA and preconception-counselling components are individually weaker (C / indirect) and should not inherit the B rating.
- **All-cause birth-size benefit is real; cause-specific mortality benefit is not demonstrated.** MMS stillbirth RR 0.95 (null), calcium stillbirth RR 0.89 (null), aspirin perinatal mortality RR 0.91 (null) — the pre-eclampsia-prevention → mortality link is underpowered/unshown in pooled data.
- **Version/overlap:** the same BPE pooled estimates (SGA RR 0.79; stillbirth RR 0.60) appear in both `pmid_37331760` and `pmid_30480324` — one evidence base, counted once. Many umbrella reviews (`oa_W4389374447`, `oa_W2124429964`, `pmid_17521431`) re-cite Cochrane pooled RRs rather than adding new data.
- **Certainty/heterogeneity:** single-vitamin meta-analysis is low-certainty (75% of trials high risk of bias, `pmid_40752545`); counselling outcomes very-low to moderate; mental-health breastfeeding I²=61%.
- **External-validity leak risk:** vitamin D (`pmid_22742603`) and n-3 LCPUFA (`pmid_22742604`) evidence is predominantly high-income (`lmic:false`) — do not generalise to LMIC WRA.
- **Many records are descriptive** (food-taboo prevalence, ANC determinants, intra-household allocation, macrosomia risk factors) — useful for design/targeting, not intervention effect sizes.

## Nutrition-sensitive social protection (cash/food transfers, maternity protection, wage & safety-net policy)  (children under 5 & women of reproductive age)
**Evidence: B  |  Cost-effectiveness: Unknown  |  Scalability: Proven national  |  Tier 2**

- **Evidence base:** 17 papers in the bundle, but the design mix is weak for causal inference. There are **no completed meta-analyses and no RCTs**. The two records tagged `systematic_review` are (1) a **scoping review** (Kanchi et al. 2023, *International Breastfeeding Journal*, study_design "Systematic review"/"Scoping Review", 17 primary studies, mostly qualitative/cross-sectional, certainty rated **Low** in the record; `oa_W4318452037`) and (2) a **protocol only** — a planned Campbell systematic review & meta-analysis of women's empowerment interventions with **no results yet** (Campbell Systematic Reviews, 2017; `oa_W2956504476`; the record itself flags it "should likely be excluded pending the completed review"). The remaining records are one narrative review of paid parental leave (`oa_W2751631156`), several other narrative/commentary reviews (`oa_W2037563577`, `oa_W4405280869`, `oa_W4224225581`, `oa_W2929035401`), quasi-experimental / non-randomised policy evaluations (`oa_W2742068156`, `oa_W3109934363`, `oa_W3048777227`), observational risk-factor / cohort studies (`oa_W4224215360`, `oa_W3107133543`, `oa_W4321787370`, `oa_W4400914715`, `oa_W2947967871`, `oa_W2062393093`), and one CGE modelling study (`oa_W3184414752`). Consistency is only moderate: income/wage/leave levers point toward benefit, but at least one national evaluation (Brazil Zero Hunger, `oa_W3048777227`) found overall investment did **not** alleviate child malnutrition or infant mortality. Hence **Evidence B** (some SR-level and quasi-experimental signal, mixed and largely observational; no pooled RCT evidence).

- **Effect sizes** (measure + 95% CI + corpus key; all-cause vs cause-specific kept separate):
  - **Paid maternity leave → infant mortality (all-cause).** Each additional month of paid maternity leave associated with **7.9 fewer infant deaths per 1,000 live births (95% CI 3.7–12.0), ~13% relative reduction**, across ~300,000 births in 20 LMICs (Nandi et al., as reported in the narrative review `oa_W2751631156`). Note this is a review citing an underlying primary study, not an independent pooled estimate.
  - **Paid maternity leave → immunization (cause-specific/service outcome).** Each additional *week* of paid leave raised probability of **DTP1 by 1.38, DTP2 by 1.62, DTP3 by 2.17 percentage points** (~250,000 births, 20 LMICs; Hajizadeh et al. via `oa_W2751631156`); no CIs given in card, and **no** significant effect on BCG.
  - **Paid leave / breastfeeding breaks → exclusive breastfeeding (mechanism outcome).** Canada's 6-month→~1-year leave extension raised 6-month EBF by **7.7–9.1 percentage points**; guaranteed paid breastfeeding breaks to ≥6 months associated with EBF **8.9 percentage points higher** across 182 countries (both via `oa_W2751631156`).
  - **Minimum-wage growth → child anthropometry.** Quasi-experimental diff-in-diff across 23 LMICs (DHS 2003–2012): a 10% minimum-wage increase associated with **−0.054 pp stunting (95% CI −0.084 to −0.025)** and **−0.031 pp anthropometric failure (95% CI −0.057 to −0.005)**; **no significant** effect on underweight or wasting (`oa_W2742068156`). Effects are small in absolute terms.
  - **PSNP (Ethiopian safety net) → stunting (observational).** Non-beneficiary vs beneficiary households had higher stunting odds, **AOR 1.91 (95% CI 1.24–2.95)**; household food insecurity AOR 2.60 (1.86–3.64) (`oa_W4321787370`, cross-sectional, n=717 — correlational only).
  - **Cash + counselling + food (India) → diet diversity (observational).** Government cash during pregnancy → maternal minimum dietary diversity **OR 1.45 (95% CI 1.23–1.70)**; exposure to all three interventions → mothers **OR 2.40 (1.61–3.57)** and children **OR 3.54 (2.10–5.97)**. Countervailing signal: receiving government food → higher child unhealthy-food consumption **OR 1.34 (1.10–1.63)** (`oa_W4400914715`, cross-sectional).
  - **Structural poverty (Liberia) → severe acute malnutrition (observational).** Income >US$50/month **AOR 0.14 (95% CI 0.05–0.45)**; maternal literacy **AOR 0.21 (0.06–0.68)** (`oa_W3107133543`, case-control, n=100).
  - **Mechanism/context — economic shocks → wasting (all-cause anthropometric).** A 10% GNI decline predicts a **14.4% increase in moderate/severe wasting (elasticity −0.144, 95% CI −0.213 to −0.076)** and **22.2% increase in severe wasting (−0.222, 95% CI −0.118 to −0.325)** across 52 LMICs / 1.26M children (`oa_W4224215360`).
  - **Self-help-group membership → maternal service use: null.** SHG membership showed no significant association with 3+ ANC visits (OR 0.87, 95% CI 0.66–1.15), institutional delivery (OR 1.05, 0.78–1.42), or PNC (OR 1.08, 0.80–1.46) after adjustment (`oa_W2947967871`).
  - Figures such as **"823,000 child deaths preventable"** and **"$35 saved per $1"** appear in the bundle only as *within-card background citations* (`oa_W4318452037` cites the Lancet Breastfeeding Series for the 823k figure; `oa_W4224225581` is a Nature comment citing a modelled ROI). They are **not** primary findings of any study in this corpus and are not used as effect estimates here.

- **Mechanism of action:** Nutrition-*sensitive* — these interventions act on the household economic and time-use determinants of nutrition rather than delivering nutrients directly. Income transfers, minimum wages and safety nets raise purchasing power for food and health care and buffer against price/economic shocks (the shock–wasting elasticity in `oa_W4224215360` is the clearest mechanistic evidence). Maternity protection (paid leave, breastfeeding breaks, childcare) works by preserving mother–infant proximity and time, enabling exclusive breastfeeding and timely immunization/postnatal care (`oa_W2751631156`, `oa_W4318452037`). User-fee abolition works by removing the financial barrier to service utilization for pregnant women and under-5s (`oa_W2062393093`).

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is false and `cea_record` is null; no ICER or cost-per-DALY exists in the corpus for this intervention class. (The lone ROI figure in the bundle is a secondary citation in a commentary and is not a CEA of any specific programme.)

- **Government scaling pathway:** Strong platform fit — these *are* government instruments. Delivery vehicles already operate at national scale in the corpus countries: conditional cash transfers and family-farming support (Brazil Bolsa Família / Zero Hunger, `oa_W3048777227`), public-works safety nets (Ethiopia PSNP, `oa_W4321787370`; India MGNREGA, `oa_W3109934363`/`oa_W4318452037`), statutory maternity leave and workplace lactation law (Indonesia/Nigeria/Philippines/Vietnam advocacy, `oa_W4405280869`), minimum-wage legislation (`oa_W2742068156`), social grants (South Africa, `oa_W2037563577`), and health-financing reform via user-fee abolition (Niger, `oa_W2062393093`). Scalability is therefore **Proven national**, but effectiveness for nutrition specifically depends on design/implementation (weak administrative capacity delayed transfers in India; incentive-bonus perverse effects in Niger; Brazil's overall investment showed no malnutrition/mortality benefit).

- **Caveats:**
  - **No RCTs or completed meta-analyses**; the two "systematic review" records are a *scoping review* (Low certainty) and a *protocol with no results*. Version/overlap is not an issue (no shared `cochrane_id`), but the protocol should not be counted as evidence.
  - Most quantitative estimates are **cross-sectional/observational associations** (Liberia n=100, Ethiopia n=717, India survey) — no temporal causality, susceptible to confounding despite adjustment.
  - **Heterogeneous and sometimes null/adverse signals:** minimum wage helps stunting but not wasting/underweight; SHG membership null; government food linked to *higher* child unhealthy-food intake; Brazil Zero Hunger overall null for malnutrition/mortality.
  - **Underpowered / indirect nutrition pathways:** several strong papers (paid-leave review, maternity-protection scoping review, economic-shock cohort, COVID diet-affordability model) measure *upstream determinants or service/breastfeeding proxies*, not directly measured child nutrition outcomes, and much of the paid-leave evidence is drawn from high-income settings within a narrative review.
  - Effect-size provenance: the strongest infant-mortality and breastfeeding numbers come from a **narrative review citing primary studies** (`oa_W2751631156`), not independently pooled — treat as indicative, not GRADE-graded.

## Iron supplementation / iron-containing interventions for young children (children under 5; some records also cover WRA)

**Evidence: B  |  Cost-effectiveness: Moderate  |  Scalability: Requires investment  |  Tier 2**

- **Evidence base:** The bundle holds 12 records. By verbatim `study_design`/`journal`, these are: 4 meta-analyses / SR-with-MA (PMID 30654514 "Systematic Review & Meta-Analysis", *Nutrients*; PMID 36767153 "Meta-analysis", *Int J Environ Res Public Health*; PMID 17158406 "Meta-Analysis", *The American Journal of Clinical Nutrition*; PMID 33371907 "Systematic review & meta-analysis", *British Journal of Nutrition*); 3 systematic reviews (PMID 31479458 iron-containing cookware, *PLoS One*; PMID 34444903 WRA anemia overview, *Nutrients*; and the SR component of the above); 2 narrative/other reviews (DOI 10.3390/ijerph18052449; DOI 10.3390/nu6104093); and 3 cross-sectional surveys (Ethiopia DOI 10.1017/s1368980099000336; two Mexico surveys DOI 10.1590/s0036-36342003001000005 and .../008). **None is a Cochrane review** (no record has `cochrane_id` set), so none is labelled as such. Critically, most records are *prevalence / epidemiology* of anemia and iron-deficiency, not intervention-effect trials. Only two records carry intervention-effectiveness estimates (PMID 30654514, PMID 17158406) and one an efficacy SR of a delivery vehicle (PMID 31479458). GRADE was not applied in any record; where certainty is stated it is study-quality scoring (e.g. PMID 31479458: "not GRADE-assessed; 9/11 studies scored 4–7 on modified EPOC; high heterogeneity precluded meta-analysis"; PMID 36767153: "91.67% of studies rated high quality (JBI)").

- **Effect sizes (intervention effectiveness — all-cause / hematologic outcomes):**
  - Iron supplementation in early childhood (PMID 17158406, *Am J Clin Nutr* meta-analysis of 26 RCTs, ages 0–59 mo, developing countries): among iron-deficient or anemic children, **hemoglobin concentration improved with iron supplementation** (direction: benefit; the record reports no pooled MD or 95% CI — pooled effect size not in corpus). Reductions in cognitive and motor development deficits were seen in iron-deficient/anemic children, particularly with longer-duration, lower-dose regimens (no CI in corpus).
  - LAC anemia interventions (PMID 30654514, SR & meta-analysis): pooled anemia **prevalence** fell from **45% to 25%** after nutritional interventions (p<0.01, 14 intervention studies, n=6,600); national-level programs specifically cut prevalence from **40% (95% CI 29.02–51.06) to 18% (95% CI 8.87–27.02)** (n≈4,500). These are program-level anemia reductions (fortification + supplementation + other), **not** an iron-supplementation-specific pooled relative risk.
  - Iron-containing cookware (PMID 31479458, SR): statistically significant Hb increase in **4/8 (50%)** pot studies among children and **2/7 (28.6%)** among females of reproductive age; Hb mean-difference range **−0.4 to 1.2 g/dL** (pots) and **0.32 to 1.18 g/dL** (ingots). Mixed/heterogeneous — no pooled estimate (meta-analysis precluded by heterogeneity).
  - Program-associated WRA reductions (PMID 34444903): flour-fortification programs associated with **−4.4% CAGR** in WRA anemia (median across 8 studies); iron-supplement use in pregnancy associated with lower anemia odds (non-users vs users **aOR 1.23, 95% CI 1.09–1.40**, Zimbabwe); 4+ ANC visits **aOR 0.73, 95% CI 0.59–0.91** (Ethiopia).

- **Effect sizes (cause-specific / safety — kept separate and flagged underpowered):** The efficacy meta-analysis (PMID 17158406) explicitly separates safety signals from the all-cause hematologic benefit: **weight gain was adversely affected in iron-replete children** (benefit is confined to iron-deficient children); in **malaria-endemic Zanzibar, iron supplementation was associated with a significant increase in serious adverse events**, whereas in **Nepal no effect on mortality** was found. The record notes "most studies found no effect on morbidity, although few had sample sizes or study designs adequate for drawing conclusions" — i.e. **morbidity/mortality pathways are underpowered**, and the safety concern (malaria) is the binding constraint, not the hematologic benefit. No dominant single trial is tagged in any record (`dominant_trial` empty throughout); no fixed-vs-random split is reported in the corpus.

- **Mechanism of action:** Iron corrects iron-deficiency anemia by supplying the substrate for hemoglobin synthesis and erythropoiesis, raising Hb and iron stores (ferritin) in deficient children; adequate iron also supports myelination and neurotransmitter synthesis, the plausible route to the cognitive/motor benefits seen in deficient children (PMID 17158406). The safety hazard is the mirror image: free/unbound iron can promote pathogen growth and oxidative stress, which underlies the excess serious adverse events in malaria-endemic settings (PMID 17158406) and motivates targeting deficient children rather than universal untargeted supplementation.

- **Cost-effectiveness:** `cea_rating_allowed` is **true** (44 CEA papers, 0 registry matches). The evidence is **mixed / context-dependent**, so **Moderate**:
  - Direct iron supplementation in under-2s, rural Bangladesh (BRISC trial CEA, PMID 36192508, *Am J Clin Nutr*): iron supplements averted **0.0039 (95% CI 0.0030–0.0048) DALYs/child** at incremental cost **$0.64 ($0.62–$0.67)**, ICER **$1,645 ($1,333–$2,153) per DALY averted** vs no intervention; iron dominated MNPs (cheaper, more DALYs averted, MNP ICER driven by $0.75 cost / 0.0031 DALYs). At the Bangladesh opportunity-cost threshold (~$200) and half-GDP threshold (~$985), universal iron had a **0% probability of being optimal** — authors conclude findings **do not support universal iron supplementation** there.
  - Universal iron-containing MNPs across 78 countries (Pasricha 2020, *Lancet Glob Health*, OpenAlex W3044712618): net benefit in 54/78 countries but **net harm in 24** (malaria/diarrhoea YLLs offsetting anemia YLD gains); where beneficial, median **28.1 DALYs averted per 10,000 children** and median **$3,576 (IQR 2,474–4,918) per DALY averted** — cost-effectiveness highly conditional on high anemia + low infection prevalence and on coverage.
  - Fortified infant cereals, Egypt (OpenAlex W4412427279): **ICER −4.14** (dominant: more effective and less costly than no intervention).
  Bottom line: iron delivery is cost-effective **only in high-anemia, low-malaria settings with good coverage**; untargeted universal supplementation was not cost-effective in the one direct-supplementation trial CEA in the bundle. Hence **Moderate**, not Very High.

- **Government scaling pathway:** Multiple platform fits are documented in-corpus. Antenatal-care platforms deliver iron/IFA to pregnant women (PMID 34444903: 4+ ANC visits associated with lower anemia). Home fortification (MNPs) and fortified complementary foods reach infants at 6 mo (Pasricha 2020; Egypt cereals CEA). Staple-food and social-safety-net fortification is an existing government channel (PMID 22624295: fortified wheat flour delivered through India's Public Distribution System, ICDS, and Mid-Day Meal — rated "highly cost-effective" by WHO criteria). Direct child supplementation would run through primary-care/child-health platforms but requires targeting infrastructure to identify iron-deficient children and to avoid supplementing in malaria-endemic areas — real added investment. Classified **Requires investment** because effectiveness and cost-effectiveness are conditional on targeting + malaria context and no record demonstrates proven national-scale iron-supplementation impact for under-5s.

- **Caveats:**
  - *Corpus composition:* the bundle is dominated by anemia **prevalence** reviews/surveys (7 of 12 records), not iron-intervention efficacy. The strongest efficacy record (PMID 17158406) reports directions but **no pooled effect sizes with 95% CIs** (pooled MD/RR not in corpus), so the evidence grade is **B**, not A.
  - *Anemia ≠ iron deficiency:* several records show iron deficiency explains **less than half** of anemia in some regions (~37% per a cited 23-country meta-analysis, DOI 10.3390/ijerph18052449; IDA 13.6% [95% CI 8.0–19.2] vs total anemia 46.8% [36.0–57.6] in Bangladesh, PMID 36767153) — iron interventions address only the iron-deficient fraction.
  - *Safety heterogeneity / underpowered pathways:* the malaria adverse-event signal (Zanzibar) and adverse weight effect in iron-replete children (PMID 17158406) mean untargeted universal supplementation carries harm; morbidity/mortality outcomes are underpowered across the trial base.
  - *Heterogeneity:* iron-cookware effects are highly heterogeneous (meta-analysis precluded; PMID 31479458) and compliance-dependent (26.7–71.4% for pots).
  - *Version/overlap:* no records share a `cochrane_id`; no double-counting of review versions in this bundle.

## Antenatal Iron-Folic Acid (IFA) Supplementation  (Women of reproductive age / pregnant women)
**Evidence: B  |  Cost-effectiveness: High  |  Scalability: Proven national  |  Tier 2**

- **Evidence base:** The bundle holds 11 records for this intervention: 5 systematic reviews & meta-analyses, 4 systematic reviews (one an umbrella review), 1 Cochrane review, 1 narrative programme review, and 1 cross-sectional study (tiers reported as meta_analysis=5, systematic_review=4, review_other=1, observational=1). Only one is a Cochrane review — *Intermittent oral iron supplementation during pregnancy* (PMID 26482110, cochrane_id CD009997, "The Cochrane database of systematic reviews"); no other record should be called Cochrane. The evidence is characterised as **B (mixed/conditional)** rather than A: the meta-analyses consistently show IFA improves maternal haematological status and reduces anaemia, but much of the corpus addresses **regimen comparisons** (intermittent vs daily) and **observational determinants of anaemia** rather than IFA-vs-placebo mortality/birth-outcome RCTs, and GRADE certainty is low/very low where stated. There is no IFA-vs-placebo Cochrane review in this bundle.

- **Effect sizes** (measure + 95% CI + corpus PMID/key; all-cause vs cause-specific / regimen comparisons kept separate):

  *Anaemia reduction (IFA vs placebo/no supplement):*
  - Preconception IFA vs placebo, anaemia: **RR 0.66 (95% CI 0.53–0.81)**, 6 studies, n=3,430, random-effect (PMID 37131925, Campbell systematic review). Weekly IFA subgroup: **RR 0.70 (0.55–0.88)**, 6 studies, n=2,661 (PMID 37131925).
  - Neural-tube defects, periconceptional folic acid vs placebo: **RR 0.53 (0.41–0.77)**, 2 studies, n=248,056, random-effect (PMID 37131925) — cause-specific benefit driven by the folic-acid component.

  *Haematological status (IFA vs comparator):*
  - Pooled mean haemoglobin, iron vs control in WRA: **SMD −0.71 (95% CI −1.27 to −0.14)**, 19 studies, n=4,421, random-effects (PMID 37069552). Serum ferritin: **SMD −0.76 (−1.56 to 0.04)**, 15 studies, n=3,648 — CI crosses null (PMID 37069552).

  *Regimen comparison — intermittent vs daily (NOT IFA vs placebo; report separately):*
  - Cochrane CD009997 (PMID 26482110), 21 trials contributing data, n=5,490: no clear difference between intermittent and daily for low birthweight **RR 0.82 (0.55–1.22)**, infant birthweight **MD 5.13 g (−29.46 to 39.72)**, premature birth **RR 1.03 (0.76–1.39)**, neonatal death **RR 0.49 (0.04–5.42)**, maternal anaemia at term **RR 1.22 (0.84–1.80)**; intermittent had **fewer maternal side effects RR 0.56 (0.37–0.84)**. GRADE: **low** for infant outcomes, **very low** for maternal outcomes.
  - Newer intermittent-vs-daily MA (PMID 39780191, "Reproductive health"): end-of-supplementation maternal haemoglobin **MD −0.24 g/dl (−0.35 to −0.12)**, 15 studies, n=2,231; incidence of anaemia **RR 1.09 (0.77–1.54)** (null); fewer side effects **RR 0.27 (0.11–0.69)**; better adherence **RR 1.60 (1.34–1.91)**.

  *Neonatal-mortality context (prenatal-care umbrella meta-analysis; single-study RRs cited, not IFA-specific pooled):*
  - PMID 40361853 ("Healthcare (Basel)") overall pooled **RR 0.85 (0.76–0.94)**, 14 studies; nutritional supplementation (folic acid/iron) subgroup cited from Black et al. 2013 as **RR 0.60 (0.54–0.68)** and Bhutta et al. 2013 as **RR 0.85 (0.76–0.94)** — these are single-source citations within the review, not this review's own pooled IFA estimate.

  *Observational determinants of anaemia (harm direction; not intervention effects):* no-IFAS vs IFAS anaemia OR 1.82 (1.22–2.70) (PMID 34861892); no iron-supplementation OR 2.59 (1.19–5.66) (PMID 39810098); low dietary diversity RR 2.61 (1.97–3.48) (PMID 41327070). Cross-sectional: IFA ≥90 days associated with fewer pre-eclampsia/eclampsia symptoms, adjusted **OR 0.64 (0.47–0.88)**, n=39,657 (PLoS ONE, no PMID in record).

- **Mechanism of action:** Iron corrects/prevents iron-deficiency anaemia by supplying substrate for haemoglobin synthesis and replenishing maternal iron stores against the expanded plasma volume and fetal demand of pregnancy; folic acid supports one-carbon metabolism and neural-tube closure in the periconceptional window (reflected in the NTD RR 0.53, PMID 37131925). Benefit is greatest in iron-deficient/anaemic women; in iron-replete women marginal benefit falls and side effects/high-Hb risk rise (rationale for the intermittent regimen, PMID 26482110).

- **Cost-effectiveness:** cea_rating_allowed = **true** (107 CEA papers retrieved, 0 registry matches). The most directly relevant record, a dynamic microsimulation in India, Pakistan, Mali and Tanzania (PMID 35192606, *PLoS Medicine*-style analysis), uses **antenatal IFA as the baseline standard-of-care comparator**: universal MMS vs baseline IFA cost **$52 (95% UI $28–78)/DALY averted in Pakistan, $70 ($43–104) in India, $72 ($37–118) in Mali, $253 ($112–481) in Tanzania**. IFA itself is treated as the low-cost reference against which more expensive regimens are judged, consistent with a **High** cost-effectiveness rating for IFA. Corroborating iron-intervention CEAs in the bundle report ICERs in US$/DALY averted for iron supplements/MNPs in children (BRISC trial, PMID 36192508) and MINIMat (PMID 26018633). Rating: **High** (grounded in cea_record; no single IFA-specific ICER for pregnant women is stated in-corpus, so not "Very High").

- **Government scaling pathway:** IFA is delivered through routine antenatal care (ANC) contacts and is already a WHO-recommended standard of pregnancy care, giving strong platform fit. The Nepal programme review (PMID not in record; "Maternal and Child Nutrition", 2021) documents a **proven national scale-up**: any-IFA consumption rose from 23% (2001) to **91% (2016)**, ≥90-day consumption from 6% to **71%**, alongside anaemia prevalence falling from 75% (1998) to **46% (2016)**, delivered partly via Female Community Health Volunteer community-based distribution. This is the clearest national-scale delivery model in the bundle.

- **Caveats:**
  - **Version/overlap:** the two intermittent-vs-daily analyses (PMID 26482110 CD009997; PMID 39780191) overlap heavily in included trials and address the same regimen question — do not treat as independent evidence generations. They are distinct records (different cochrane_id / none) but count as one body of regimen evidence.
  - **Outcome mismatch:** much of the corpus is anaemia-prevalence and determinant epidemiology (harm-direction ORs), not IFA intervention effects — these should not be read as efficacy estimates.
  - **Underpowered / imprecise pathways:** neonatal death in the Cochrane review rests on a single study (RR 0.49, CI 0.04–5.42); serum ferritin SMD crosses null (PMID 37069552); the fully adjusted pre-eclampsia association is cross-sectional (residual confounding).
  - **Heterogeneity:** haemoglobin SMD −0.71 has a wide CI (−1.27 to −0.14) reflecting substantial between-study heterogeneity (PMID 37069552); GRADE certainty is low/very low in the Cochrane review.
  - **CEA framing:** the strongest CEA evidence positions IFA as the *comparator baseline* rather than reporting a standalone IFA ICER, so the "High" rating is inferred from IFA being the low-cost reference, not from a direct IFA cost-per-DALY figure in corpus.

## Multiple Micronutrient Powders (MNP) — home / point-of-use fortification  (children under 5, esp. 6–23 months)

**Evidence: B  |  Cost-effectiveness: Moderate  |  Scalability: Growing  |  Tier 2**

- **Evidence base:** Three on-topic records in the bundle (all under-5, all China/LMIC): one Cochrane meta-analysis, one cluster-RCT, and one prevalence systematic review.
  - **Cochrane review** (Suchdev/Das update, *The Cochrane Database of Systematic Reviews* 2020, PMID 32107773, CD008959.pub3): 29 RCTs / 33,147 children in LMICs; the anchor evidence. GRADE certainty is graded per-outcome: **high** (iron deficiency), **moderate** (anaemia, ferritin/iron status, weight-for-age), **low** (haemoglobin, MNP vs daily iron).
  - **Cluster-RCT** in rural Shaanxi, China (*BMC Public Health* 2017, key oa_W2757071974, DOI 10.1186/s12889-017-4755-0; ISRCTN44149146): n=1,802 children enrolled at 6–11 months, followed to 24–29 months.
  - **Systematic review** of anaemia prevalence & associated factors, Western China (*BMJ Paediatrics Open* 2022, PMID 36053597) — descriptive/observational, **not** an intervention trial; contributes real-world program (Ying Yang Bao) signal only.
  The direct efficacy evidence (anaemia, iron status) is consistent and comes from a single high-quality meta-analysis rather than "multiple consistent meta-analyses"; the survival/developmental and durability signals are mixed. This supports an Evidence grade of **B**, not A.

- **Effect sizes** (all vs no intervention/placebo unless noted; all from the Cochrane meta-analysis PMID 32107773 unless keyed otherwise):
  - Anaemia: **RR 0.82 (95% CI 0.76–0.90)**, 16 studies, 9,927 children — 18% risk reduction (moderate certainty). *(PMID 32107773)*
  - Iron deficiency: **RR 0.47 (95% CI 0.39–0.56)**, 7 studies, 1,634 children — 53% reduction (high certainty). *(PMID 32107773)*
  - Haemoglobin: **MD +2.74 g/L (95% CI 1.95–3.53)**, 20 studies, 10,509 children (low certainty). *(PMID 32107773)*
  - Iron status (ferritin): **MD +12.93 µg/L (95% CI 7.41–18.45)**, 7 studies, 2,612 children (moderate certainty). *(PMID 32107773)*
  - Weight-for-age: **MD +0.02 z-score (95% CI −0.03–0.07)**, 10 studies, 9,287 children — **null** (moderate certainty). *(PMID 32107773)*
  - MNP vs **daily iron supplementation** (head-to-head): anaemia **RR 0.89 (95% CI 0.58–1.39)**, 1 study, 145 children — no difference (low certainty); i.e. MNP is comparable to, not superior to, iron drops. *(PMID 32107773)*
  - **Durability signal (single RCT, oa_W2757071974):** benefits were modest and **transient**. Haemoglobin improved at 6 months (**MD +1.77 g/L, 95% CI 0.02–3.52**) but was null at 12 months (MD −0.12, 95% CI −2.19–1.96) and 18 months (MD +0.13, 95% CI −1.85–2.11). Bayley MDI (cognitive) improved at 6 months (**MD +2.23 points, 95% CI 0.06–4.40**) but not at 12–18 months (MD +0.83, 95% CI −1.79–3.44); Bayley PDI (psychomotor) null at all timepoints (MD −0.27, 95% CI −3.33–2.80). The authors attribute the non-persistence partly to a low iron dose (6 mg vs the typical 12.5 mg). *(oa_W2757071974)*
  - **No dominant-trial / all-cause-vs-cause-specific mortality issue applies here:** the Cochrane review reports **no mortality outcome** (death reporting was infrequent, no deaths attributable to the intervention). The primary outcomes are haematological, not survival. No `dominant_trial` is set on any record and no fixed/random split is reported in the bundle.
  - **Program-level (observational, not causal):** Ying Yang Bao national anaemia decline from **32.9% to 17.6%** (2012–2017), all 8 studies protective — but observational, so cannot be read as an effect size. Background anaemia burden remains high: median **42.54%** (IQR 25.62–52.56) in under-5s in Western China, up to **67.8%** in Qinghai and **50.09%** at 6–12 months. *(PMID 36053597)*

- **Mechanism of action:** Single-dose sachets of vitamins and minerals (at least iron, zinc, vitamin A) mixed into semi-solid complementary food at the point of use. Iron and ferritin repletion corrects iron-deficiency anaemia; the effect operates through improved micronutrient intake without requiring a change in the food supply chain. Consistent with the biology, effects concentrate on iron/anaemia outcomes and not on anthropometry (weight-for-age null).

- **Cost-effectiveness (Moderate — CEA records present; cea_rating_allowed = true):** 147 CEA papers retrieved, 0 registry matches.
  - MNP-specific modelling in Pakistan ("Sprinkles", PMID 16512321): **~$12.2 per DALY averted** ($8–$97), ~$406 per death averted, and $37 earnings gain per $1 spent — very favourable, but a single-country model in a high-burden setting (anaemia 93%, IMR 83/1000).
  - Trial-based CEA in rural Bangladesh (BRISC, PMID 36192508): MNP averted 0.0031 DALYs/child at incremental cost $0.75/child; **iron supplementation dominated MNP** (cheaper, more DALYs averted, ICER ~$1,645/DALY), and **neither** MNP nor iron was cost-effective at the Bangladesh opportunity-cost threshold ($200/DALY) or half-GDP threshold ($985/DALY). Conclusion: does not support universal MNP as cost-effective in that setting.
  The two anchor CEAs **disagree sharply** (highly cost-effective in high-burden Pakistan vs not cost-effective in lower-burden Bangladesh), and MNP can be dominated by cheaper iron-only supplementation. Cost-effectiveness is therefore context-dependent (rises with baseline anaemia/mortality burden) — rated **Moderate**, not Very High.

- **Government scaling pathway:** Strong platform fit. MNP is delivered through existing complementary-feeding and IYCF platforms, requires no cold chain, and is caregiver-administered at home. Real-world national deployment exists: WHO-cited 43 countries reached >3 million children by 2014 (per PMID 32107773 background), and China's Ying Yang Bao program scaled nationally (PMID 36053597). Rated **Growing** — proven at national scale in at least one large country, with wide sub-national/pilot rollout elsewhere, but not yet universal standard of care.

- **Caveats:**
  - **Version/overlap:** the Cochrane review (CD008959.pub3) is one review counted once; the 2017 China RCT is an independent primary trial, not a version of it. No double-counting.
  - **Underpowered / unclear pathways:** child survival and developmental outcomes are explicitly "unclear" in the Cochrane review; the only developmental signal (single RCT) was transient. Morbidity outcomes (diarrhoea, malaria, respiratory) reported by few studies (3–5 each) — safety reassuring but underpowered.
  - **Durability & dose:** benefits may not persist post-intervention; low-iron formulations (6 mg) may underperform.
  - **Comparator matters:** MNP is comparable to — not better than — daily iron drops, and can be economically dominated by iron-only supplementation (BRISC).
  - **Heterogeneity:** trials span 2–44 months and 5–22 nutrients; the CEA conclusion is highly sensitive to baseline anaemia/mortality burden.
  - **Program evidence is observational:** the Ying Yang Bao national decline is not causal RCT evidence.


# Tier 3 — Promising or indirect, plausible pathway

## Nutrition-Sensitive Agriculture & Food Systems  (children under 5 & women of reproductive age, LMIC)
**Evidence: B  |  Cost-effectiveness: Unknown  |  Scalability: Requires investment  |  Tier 3**

Nutrition-sensitive agriculture (NSA) covers homestead/home-garden food production, biofortified crops (chiefly orange-fleshed sweet potato, OFSP), livestock and dairy, aquaculture/small-fish, crop diversification, and agricultural policy/value-chain reforms designed to carry explicit nutrition objectives.

- **Evidence base:** The bundle holds **30 records**: 4 systematic reviews, 1 cluster-RCT, 2 global modeling studies, 9 observational studies (cohort/cross-sectional/non-randomised), 11 narrative/conceptual reviews, and 3 implementation/qualitative studies. The two most authoritative records are systematic reviews indexed in PubMed:
  - *Nutrition-Sensitive Agriculture: A Systematic Review of Impact Pathways to Nutrition Outcomes* (PMID 32970116, `Advances in Nutrition` 2021, study type "Systematic Review", 43 studies, 18 LMICs, PROSPERO CRD42018108308) — **narrative/vote-counting synthesis, no pooled meta-analytic effect sizes**.
  - *The impact of gender equity in agriculture on nutritional status, diets, and household food security* (PMID 32337083, `BMJ Global Health` 2020, "Systematic Review", 34 studies / 42,809 households, PROSPERO CRD42018093987) — contains the **only pooled random-effects estimates in the bundle**, all for exposure–outcome associations rather than intervention trials.
  - Two further reviews are relevant but limited: a scoping "review of reviews" (key `oa_W4385550334`, `Food Security` 2023, 196 reviews, AMSTAR-2 quality 7 high / 36 moderate / 72 low / 81 critically low, "meta-analysis not possible due to heterogeneity"); and a systematic review of poverty-reduction/development interventions (key `oa_W2792567257`, `PLoS ONE` 2018, 29 studies, author-rated certainty **Low**, "narrative synthesis only — meta-analysis not possible").
  - **Consistency:** direction of effect is consistent for *intermediate* outcomes (dietary diversity, micronutrient/vitamin-A intake improve) but **weak and inconsistent for anthropometric status** across every review. No GRADE ratings are reported; the highest-quality within-bundle certainty statements are "Low."

- **Effect sizes** (all with corpus key; intermediate diet outcomes vs anthropometric/status outcomes kept separate):
  - *Child dietary diversity (RCT, strongest single estimate).* UPAVAN cluster-RCT, Odisha India (key `oa_W3144573952`, `Lancet Planetary Health` 2021, ISRCTN65922679): child minimum dietary diversity RR **1.19 (95% CI 1.03–1.37)** for AGRI-NUT vs control and RR **1.27 (95% CI 1.11–1.46)** for AGRI-NUT+PLA vs control; the agriculture-only arm was null (RR **1.06, 95% CI 0.91–1.23**). Maternal minimum dietary diversity RR **1.30 (95% CI 1.10–1.53)** (AGRI-NUT+PLA vs control).
  - *Child dietary diversity (quasi-experimental).* Participatory farm diversification + nutrition education, Western Kenya (key `oa_W2920187978`, `Maternal & Child Nutrition` 2019, non-randomised difference-in-difference, n=444): children's mean dietary-diversity score MD **+0.683 (95% CI 0.363–1.004)**; proportion reaching minimum dietary diversity difference-in-difference **+0.234 (95% CI 0.105–0.363)**.
  - *Anthropometric / nutritional status (null or unpooled).* UPAVAN found **no effect** on child wasting (RR **0.96, 95% CI 0.73–1.26**, AGRI-NUT+PLA) or maternal BMI (MD **-0.05 kg/m², 95% CI -0.34 to 0.24**, AGRI arm) (key `oa_W3144573952`). In the impact-pathways SR (PMID 32970116) only vote-counts exist: improvement in child anthropometric status in **7 of 21** studies, HAZ/stunting improvement in **4 of 17**, wasting/WHZ in only **1 of 15**; micronutrient status improved in **8 of 12** studies (child anaemia/haemoglobin/serum retinol) — i.e. the diet/micronutrient signal is much stronger than the growth signal.
  - *Pooled meta-analytic estimates (all null).* The gender-equity SR (PMID 32337083) reports women's income share vs household food share MD **0.32 percentage points (95% CI -4.22 to 4.86)** and women's land share vs food share MD **2.72 (95% CI -0.52 to 5.96)** (unstandardised, random-effects); standardised estimates also null (income -0.32, 95% CI -1.99 to 1.35; land 0.96, 95% CI -0.69 to 2.61). 22 of 25 quantitative studies were high risk of bias (adapted ROBINS-I).
  - *Biofortification signal (within-review, single-study, low certainty).* From the poverty-reduction SR (key `oa_W2792567257`): OFSP biofortification reduced child vitamin-A deficiency from ~60% to ~38% over 2 years (Mozambique pilot, n=733, p<0.01), and cash-plus-food combinations outperformed cash alone for acute malnutrition (moderate acute malnutrition HR **2.3, 95% CI 1.6–3.29**; severe acute malnutrition HR **3.13, 95% CI 1.65–5.94**; Niger, n=4,176) — these are individual included-trial results cited by the review, not pooled estimates.
  - *Modeling (background, not intervention effect sizes).* Aquatic-food scenarios project global reductions in inadequate iron (8.1M), calcium (49.3M) but an **increase** in inadequate vitamin A (10.1M) by 2030 (key `oa_W3199565759`, `Nature` 2021); small-scale fisheries supply ~20% of six key micronutrients for 2.3 billion people (key `oa_W4406385601`, `Nature` 2025). These are model projections of nutrient-inadequacy risk, not measured child/WRA outcomes.
  - Contextual burden figures (e.g. "159 million" or "165 million" children stunted, "250 million" children with vitamin-A deficiency; keys `oa_W2593227714`, `oa_W2056001884`) are attributed **within those records to external sources**, not derived by them, and are not corpus intervention effects.

- **Mechanism of action:** PMID 32970116 maps NSA to nutrition through **five impact pathways** — (1) food production improving availability/access to nutrient-rich foods, (2) agricultural income raising purchasing power, (3) nutrition/WASH/health knowledge (behaviour-change communication) improving dietary and care practices, (4) women's empowerment, and (5) strengthening of local institutions. The review's central finding is a **disconnect between long-term (dietary) outcomes and impact on nutritional status**: interventions reliably improve production, knowledge, income and diet, but this does not consistently translate to stunting/wasting reduction (attributed to under-addressed non-food determinants, short program duration, and underpowered growth-outcome designs). The knowledge/BCC pathway is the component the review flags as essential for converting agricultural output into diet change (consistent with UPAVAN, where only the arms *adding* nutrition content, not agriculture alone, improved dietary diversity).

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is **false** and `cea_record` is **null**; no ICER, cost-per-DALY, or cost-per-case-averted for any NSA intervention is present in the corpus. Per the CEA guard, no cost-effectiveness rating is assigned.

- **Government scaling pathway:** NSA fits **agriculture-extension, women's-group / self-help-group, and social-protection platforms** rather than the health system. UPAVAN (key `oa_W3144573952`) delivered through existing women's self-help groups with participatory video — a channel that maps onto India's SHG and ICDS infrastructure — and the Kenya program (`oa_W2920187978`) used community sublocations. Implementation studies show feasibility of grafting nutrition BCC onto existing agricultural video-extension platforms (`oa_W2530043146`, India) and onto integrated group-based maternal-child programs (`oa_W3125291048`, RINEW Bangladesh), but both flag attendance/childcare/gender-norm barriers and note nutrition content needs more time and technical support than agriculture content. Bangladesh's stunting decline is attributed largely to broad nutrition-sensitive drivers — income growth, women's education, family planning, health access — rather than direct programs (`oa_W2590504932`), underscoring that NSA works as a multi-sectoral enabler requiring cross-ministry coordination and sustained investment, not a standalone deliverable. **Rating: Requires investment.**

- **Caveats:**
  - **No pooled anthropometric evidence.** The two systematic reviews on NSA per se (PMID 32970116; scoping review `oa_W4385550334`) are narrative/vote-counting; the only pooled random-effects estimates in the bundle (PMID 32337083) are for gender-equity→food-security associations and are **all null**. Evidence for growth/status outcomes is limited and indirect.
  - **Intermediate vs. status split.** Benefits concentrate on dietary diversity and micronutrient (especially vitamin-A/OFSP) status; effects on stunting and wasting are weak and inconsistent — the genuine evidence gap is anthropometric impact, not diet.
  - **Study-type accuracy.** The strongest causal estimate (UPAVAN) is a single cluster-RCT, not a Cochrane review; the "biofortification" and "cash-plus-food" figures are individual included-trial results cited inside reviews, not meta-analytic pooled effects. The PROTOCOL record `oa_W2973104680` (`Campbell Systematic Reviews`) reports **no original results** — its two effect sizes are secondary citations from a prior review (Lewin 2010) and must not be counted as completed-review evidence.
  - **Version/overlap:** no shared `cochrane_id` across records; no double-counting of review versions detected. No single dominant trial is flagged in any record.
  - **Heterogeneity & bias:** methodological quality is uniformly rated Low / high-risk-of-bias where assessed (AMSTAR-2 mostly low/critically low; 22/25 gender-equity studies high risk; poverty-reduction SR certainty Low). Some observational records show **counter-intuitive or harmful associations** (e.g. Rwanda: garden/livestock ownership positively associated with stunting, `oa_W2954944474`; aquatic-food scenario increasing inadequate vitamin-A intake, `oa_W3199565759`), reinforcing that NSA effects are context-dependent and not automatically protective.

## Water, Sanitation and Hygiene (WASH) interventions for child nutrition  (children under 5; some maternal/WRA evidence)

**Evidence: B  |  Cost-effectiveness: Moderate  |  Scalability: Requires investment  |  Tier 3**

- **Evidence base:** The bundle holds 5 records, none of them a randomized trial of WASH *as delivered here*, and none a Cochrane review (no record has `journal` = "Cochrane Database of Systematic Reviews"; no `cochrane_id` is set on any record). Composition: 3 records tagged `study_design` "Systematic review" / "Systematic review & meta-analysis" (pmid_41177769, pmid_41062239, pmid_31902390), 1 "Modeling study" (oa_W3071879207), and 1 "Narrative/other review" — a WHO/BMGF consensus statement (oa_W2960401104). Critically, the single record that directly evaluates household WASH as an intervention for growth is the consensus statement, which synthesizes three large factorial cluster-RCTs (WASH-Benefits Bangladesh NCT01590095, WASH-Benefits Kenya NCT01704105, SHINE Zimbabwe NCT01824940). The remaining records are exposure–outcome / association reviews (EED biomarkers; intestinal protozoa) or a geospatial burden model — WASH is invoked as a mitigation, not tested. No GRADE/certainty rating is recorded in any bundle record (`certainty` empty throughout); the consensus statement self-describes the three trials as "high internal validity."

- **Effect sizes:**
  - **Linear growth / stunting (all-cause nutrition outcome) — null.** Across all three factorial RCTs, basic household WASH (point-of-use chlorination, improved pit latrines, handwashing stations with soap) had **no effect on childhood linear growth (length-for-age Z-score) in any of the three trials**, and the combined WASH + lipid-based nutrient supplement arm showed **no additive benefit over nutrient supplementation alone** (oa_W2960401104, consensus statement, full text). The bundle carries no pooled HAZ/LAZ point estimate or 95% CI for this outcome — the consensus statement reports it as consistently null across sites rather than as a meta-analytic pooled figure (exact pooled MD *not in corpus*).
  - **Diarrhoea (cause-specific) — mixed, one positive site.** No effect in Kenya or Zimbabwe; a **40% relative reduction** in diarrhoeal prevalence in the Bangladesh combined arm, but against a low baseline — an absolute reduction of ~2 percentage points off a 1-week control-arm prevalence of 5.9% (oa_W2960401104, full text; no 95% CI reported for the 40% figure in corpus). Supporting environmental-contamination endpoints from the same trials: stored-water *E. coli* prevalence fell in the Bangladesh combined WASH arm (PR 0.38, 95% CI 0.32–0.44) and in the later water-treatment arm (PR 0.62, 95% CI 0.53–0.72) and combined arm (PR 0.75, 95% CI 0.69–0.81); *E. coli* in food fell in the water-treatment (PR 0.70, 95% CI 0.57–0.86) and handwashing (PR 0.68, 95% CI 0.56–0.83) arms (oa_W2960401104, full text).
  - **Mortality burden (modeling, not intervention effect).** In sub-Saharan Africa in 2017, unsafe water was attributable to an estimated **143,300 under-5 deaths (95% UI 126,100–163,000)** and unsafe sanitation to **182,300 (159,900–208,200)**; access gains over 2000–2017 averted an estimated **18,100 (15,700–21,200)** and **10,100 (8,970–11,400)** under-5 deaths respectively (oa_W3071879207). LMIC piped-water access rose from 40.0% (39.4–40.7) in 2000 to 50.3% (50.0–50.5) in 2017; sewer/septic sanitation from 28.7% (28.5–29.0) to 46.3% (46.1–46.5) (oa_W3071879207). These are burden-attribution estimates, **not** measured effects of a delivered intervention.
  - **Enteric-pathway associations (observational, underpowered / no pooled effect).** Intestinal protozoa: stunting AOR 2.38 (95% CI 1.55–3.64) for *Cryptosporidium* and 1.70 (1.12–2.58) for *Giardia*; HAZ difference −0.42 (−0.53 to −0.30) with *Giardia* (pmid_41062239, cross-sectional pooling — association, not causal/intervention). EED biomarkers (pmid_41177769) show consistent negative associations with linear growth (lactulose:mannitol ratio 9/19 measurements significantly negative; sCD14 7/11) but the review is a **narrative synthesis with no pooled effect sizes or CIs** (effect estimates *not in corpus*).

- **Mechanism of action:** WASH is a **nutrition-sensitive** intervention. Reducing faecal–oral exposure to enteric pathogens is hypothesized to lower diarrhoeal disease and subclinical environmental enteric dysfunction (gut inflammation, increased permeability, impaired nutrient absorption), thereby protecting linear growth (pmid_41177769; oa_W2960401104). The RCT evidence indicates that *basic, single-pathway, household-level* WASH is insufficient to interrupt exposure enough to move growth in heavily contaminated settings — chlorination in particular fails against chlorine-resistant *Cryptosporidium* and *Giardia* (oa_W2960401104). This points mechanistically to a need for "transformative"/multi-pathway WASH rather than the minimal packages that were tested.

- **Cost-effectiveness:** `cea_rating_allowed` is **true** (132 CEA papers retrieved; 0 registry matches, registry unavailable), so a rating is permitted — but the CEA corpus is heterogeneous and **not** a clean WASH-for-child-growth cost-per-DALY set. Grounded figures from the bundle's CEA record: global **benefit–cost ratios of 5.5 for sanitation, 2.0 for water supply, and 4.3 combined** (PMID 23428544), with universal-coverage costs of US$35 billion/yr (sanitation) and US$17.5 billion/yr (water) over 2010–2015. Community-led total sanitation program cost was US$30.34–81.56 per household in Ghana and US$14.15–19.21 in Ethiopia (bottom-up costing; DOI 10.1016/j.scitotenv.2017.05.279). India's open-defecation burden was estimated at US$54 billion/yr in losses (PMID 29949730). These support WASH being economically attractive **for its own diarrhoeal/mortality and time-saving benefits**, but no retrieved CEA isolates an incremental cost per DALY or per unit of *linear-growth/nutrition* gain — and the RCT evidence that basic WASH does not reduce stunting means cost-effectiveness *for the nutrition outcome specifically* is unproven. Net rating: **Moderate**, with the caveat that it is favourable for health-sector outcomes and Unknown for the growth outcome.

- **Government scaling pathway:** WASH sits on infrastructure, local-government, and health/behaviour-change delivery platforms rather than the nutrition service platform. National-scale programs exist and are proven deliverable (India's Clean India Mission / Swachh Bharat as a national campaign, PMID 29949730; CLTS operationalized at district scale in Ghana/Ethiopia, DOI 10.1016/j.scitotenv.2017.05.279). But moving from "basic" to the "safely managed"/transformative services implied by the null trials requires substantial capital investment in piped water and sewer/septic infrastructure — access still under ~50% across LMICs in 2017 (oa_W3071879207) — hence **Requires investment**.

- **Caveats:**
  - **Version/overlap:** no double-counting risk here — no shared `cochrane_id`, and the three RCTs are counted once via the single consensus record; do not treat the modeling and association reviews as independent efficacy evidence.
  - **All-cause vs cause-specific split:** the growth/stunting (nutrition) outcome is null; the diarrhoea (cause-specific) outcome is mixed and positive at only 1 of 3 sites and against a low baseline. These must not be merged into a single "WASH works" claim.
  - **Underpowered / indirect pathways:** the EED-biomarker and protozoa reviews are observational associations with **no pooled effect sizes** (pmid_41177769) or cross-sectional pooling only (pmid_41062239); they establish a plausible mechanism, not intervention efficacy.
  - **Heterogeneity:** large between-site divergence in the diarrhoea effect is attributed to differing baseline WASH conditions, local pathogen etiology (chlorine-resistant protozoa), and transmission pathways (oa_W2960401104) — effects are setting-dependent, limiting generalization.
  - **Evidence rated B (not A):** genuinely strong, consistent RCT evidence exists, but it points to a **null** effect on the target nutrition outcome; the positive evidence (diarrhoea, mortality burden, mechanism) is mixed, modelled, or observational rather than multiple consistent meta-analyses of a growth benefit.

## Growth Monitoring and Promotion (GMP)  (children under 5)
**Evidence: C  |  Cost-effectiveness: Unknown  |  Scalability: Growing  |  Tier 3**

- **Evidence base:** The bundle holds 4 papers, but only one is an outcome-focused
  evidence synthesis of the intervention itself: a 2023 **Cochrane review** (journal:
  "The Cochrane database of systematic reviews"; cochrane_id CD014785; PMID 37823471).
  It included 6 studies in 8 publications (mostly cluster-RCTs: Alderman 2009, Fink
  2017, George 1993, Marsh 2002; one cohort Laurie 2008; one controlled before-after
  Viraviadyha 1989), **all judged at overall high risk of bias**. **No meta-analysis
  was possible** — findings were synthesised narratively (SWiM guideline). GRADE
  certainty was **very low to low** for every prioritised outcome (downgraded for high
  risk of bias, imprecision, and indirectness). The second synthesis-tier paper is an
  older **Systematic review** (journal: "Tropical medicine & international health";
  PMID 17875018), but it reviews *caregiver comprehension of growth charts*, not the
  health-outcome effect of GMP. The remaining two are observational: a **Cross-sectional**
  measurement/methods paper on stunting catch-up (BMC Pediatrics, DOI 10.1186/s12887-015-0458-9)
  and a **Cross-sectional** machine-learning prediction study (J Prev Med Public Health,
  DOI 10.3961/jpmph.22.388) — neither tests an intervention. There is **no consistent
  body of pooled trial evidence**; hence Evidence grade C.

- **Effect sizes** (all from the Cochrane review CD014785 / PMID 37823471 full text;
  these are single-study estimates, NOT pooled — meta-analysis was not possible):
  - **Anthropometry (GMP with supplementary feeding vs standard care):** height-for-age
    z-score at 12 months **MD -0.15 (95% CI -0.34 to 0.04)**, 1 study (Fink 2017), 337
    participants, low certainty — null. Weight-for-age z-score at 12 months **MD -0.07
    (95% CI -0.19 to 0.06)**, 1 study (Fink 2017), 337 participants, very low certainty
    — null. (A companion home-based-GMP arm of Fink 2017 showed a small WAZ benefit,
    MD 0.183, 95% CI 0.037 to 0.328, 336 participants — the only nominally positive
    anthropometric signal, from a single arm.)
  - **Anthropometry (GMP without supplementary feeding vs standard care):** proportion
    with normal nutritional status at 6 months **RR 1.11 (95% CI 0.95 to 1.30)**, 1
    study (Viraviadyha 1989), 665 participants — null.
  - **Feeding practice:** energy intake at 12 months **MD +108.50 kcal (95% CI 23.37 to
    193.63)**, 1 study (Marsh 2002), 227 participants — favours GMP (the one CI that
    excludes null).
  - **Health-service usage (Alderman 2009, ~4296 observations, no relative effect
    calculable — proportions only):** vitamin A receipt in last 6 months rose to
    **72.5% vs 62.9%** (GMP vs standard care); deworming receipt **29.2% vs 14.6%**.
    Direction favours GMP but no CI and very low certainty.
  - **Mortality: not in corpus** — mortality was a secondary outcome but **no included
    study reported it**; keep this all-cause / cause-specific pathway explicitly
    unevidenced (underpowered/unreported, not null).
  - Supporting descriptive context (not GMP effect estimates): overall stunting
    prevalence 33.35% in Rwanda DHS (n=3814; DOI 10.3961/jpmph.22.388); absolute
    height-for-age difference *worsened* through ages 2-5 (e.g. HAD change -6.1 cm in
    the Peru Young Lives cohort, n=393; DOI 10.1186/s12887-015-0458-9), arguing that
    linear-growth deficits accrue before GMP contact points. On caregiver tools, "a
    third to three-fourths of carers do not understand the growth charts," with
    comprehension improving after training in 5 of 6 intervention trials (PMID 17875018).

- **Mechanism of action:** GMP is a *complex* intervention — regular measurement and
  charting of a child's growth (weight/height → WAZ/HAZ/WHZ plotted against reference)
  combined with promotion (counselling, feeding education, referral, sometimes
  supplementary feeding) triggered by faltering growth. The theorised pathway is:
  earlier detection of growth faltering → caregiver behaviour change and health-service
  contact → improved feeding and anthropometry. The bundle shows the chain breaks at
  two links: caregivers frequently cannot interpret charts (PMID 17875018), and
  measured anthropometric benefit is null (CD014785).

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's
  `cea_rating_allowed` is false and `cea_record` is null; no ICER or cost-per-DALY is
  in the corpus. Per the CEA guard, cost-effectiveness must be recorded as Unknown and
  is not assigned.

- **Government scaling pathway:** GMP already has strong *platform fit* — it is embedded
  in routine child-health / community-health-worker services and national nutrition
  programmes across LMICs (the included studies compared GMP against "usual services
  provided by the government as part of the national programme"). So the delivery
  infrastructure largely exists (rating: Growing — widely fielded, but its added value
  over promotion/education alone is unproven). The actionable investment is not new
  reach but quality: the comprehension gap (PMID 17875018) means scaling should pair
  charting with health-worker communication training and responsive-parenting support
  rather than measurement alone.

- **Caveats:**
  - **No pooled evidence / high risk of bias:** every effect above is a *single-study*
    estimate; all 6 included studies were high risk of bias; certainty very low to low
    throughout (CD014785).
  - **Indirectness/heterogeneity:** estimates come from single countries (Senegal,
    Zambia, Vietnam, Thailand, India, South Africa), all rural — the review explicitly
    downgraded for limited generalisability; heterogeneity in intervention content
    prevented meta-analysis.
  - **Added-value question unresolved:** the review's central debate — whether growth
    *monitoring* adds anything beyond *promotion*/education alone — remains unanswered
    (George 1993 was the only head-to-head, MD in length gain -0.02 cm/month, 95% CI
    -0.08 to 0.04).
  - **Mortality and cause-specific outcomes unevidenced,** not null (no included study
    reported mortality).
  - **Version/overlap:** only one Cochrane record (CD014785) is present; no superseded
    duplicate to collapse. The two observational papers and the comprehension review
    describe different constructs and must not be counted as intervention evidence.
  - **Three RCTs are ongoing** (Indonesia NCT04222998, Malaysia Chek 2022, Zambia
    NCT05120427), so this grade may move as they report.

## School Feeding / Publicly Procured School Meals  (children under 5 via intergenerational pathway; school-age children 5–18; women of reproductive age as future mothers)

**Evidence: C  |  Cost-effectiveness: Unknown  |  Scalability: Proven national  |  Tier 3**

- **Evidence base:** Three records in the bundle, none of them a meta-analysis and none reporting a pooled effect estimate:
  1. **Cohort / econometric study** (study_design "Cohort"; journal *Nature Communications*, 2021) — intergenerational analysis of India's Mid-Day Meal (MDM) scheme [oa_W3182946627 / DOI 10.1038/s41467-021-24433-w].
  2. **Systematic review** (study_design "Systematic review"; journal *Public Health Nutrition*, 2024) — mixed-methods review of publicly procured school meals in sub-Saharan Africa; **not** a Cochrane review [PMID 39422072 / DOI 10.1017/S1368980024001939].
  3. **Narrative/other review** (study_design "Narrative/other review"; journal *Public Health Nutrition*, 2012) — policy description of Brazil's PNAE, no quantitative outcomes [oa_W1966655996 / DOI 10.1017/s1368980012005101].

  There is one systematic review, one observational cohort, and one narrative policy review — no RCT-level meta-analysis and no pooled effect size anywhere in the corpus. The systematic review [PMID 39422072] explicitly did **not** pool: "Due to the small number and methodological heterogeneity of quantitative studies, data were synthesised descriptively." Its own included RCTs are internally mixed. This is limited/indirect evidence for the target populations (most direct outcomes are in school-age 5–18-year-olds, not under-5 or WRA), which fixes the grade at **C**.

- **Effect sizes:** All numbers are anthropometric / intermediate outcomes; there are **no all-cause or cause-specific mortality outcomes in this corpus** (the all-cause vs cause-specific split does not apply — no mortality pathway was measured).

  **India MDM, intergenerational HAZ [oa_W3182946627]:**
  - Child height-for-age z-score (HAZ) among children of mothers with full (100%) MDM coverage was **+0.40 SD** higher than children of non-exposed mothers (p < 0.05) [oa_W3182946627, fulltext]. 95% CI not given as a number in the excerpt (shown only as whiskers in Fig. 4a) → **(exact CI not in corpus)**.
  - Dose/robustness variants of the same estimate: **+0.166 SD** (raw-data model), **+0.261 SD** (log-linear smoothed), **+0.115 SD** (2004 district-SES model) — all p < 0.05 [oa_W3182946627, fulltext]. This is a genuine model-dependence, analogous to a fixed-vs-random split: the headline +0.40 SD is the birth-cohort-fixed-effects estimate; the raw-data model attenuates to +0.166 SD. No single dominant trial (this is one national dataset, not a pool), so `dominant_trial` is empty.
  - Subgroup: effect largest in poorest households, **+0.5 SD** (p < 0.05) vs +0.33 SD middle SES [oa_W3182946627].
  - Mediating (WRA) pathways, regression coefficients per 100% MDM exposure (Table 1) [oa_W3182946627]: maternal education **+3.95 years** (SE 0.46, p < 0.001); age at first birth **+1.62 years** (p < 0.001); number of children **−0.80** (SE 0.07, p < 0.001); ≥4 antenatal-care visits **+0.22** (SE 0.03, p < 0.001); institutional birth **+0.28** (p < 0.001); adult maternal height **+0.51 cm** (SE 0.36) — **not statistically significant (p = 0.163)** [oa_W3182946627]. The height pathway is underpowered/null; the education and fertility pathways carry the signal.
  - Attributable share: MDM associated with **13.3–32.1%** of India's national HAZ improvement from 2006–2016 [oa_W3182946627].

  **Sub-Saharan Africa systematic review [PMID 39422072]** — reported as **vote counts, not effect sizes**: 6 of 7 quantitative studies showed positive impact on some nutritional outcome; positive impact on stunting in 3 studies, wasting in 1, underweight in 1, vitamin A intake in 1, dietary diversity in 1 [PMID 39422072, abstract]. Full-text detail on the two RCTs is discordant:
  - Ghana cluster RCT (Gelli 2019): **no effect** on HAZ or BAZ in children 5–15 y overall; subgroup effect +0.22 SD HAZ in below-poverty-line children and +0.12 SD in northern girls [PMID 39422072, fulltext Table 1].
  - South Africa RCT (Van der Hoeven 2015): subclinical vitamin A deficiency fell from **7.0% to 1.3%** in the intervention arm vs no change in control (p = 0.015); no effect on iron or zinc [PMID 39422072, fulltext].
  - Ethiopia cohort (Desalegn 2022): **no significant effect** on HAZ/BAZ/anaemia [PMID 39422072, fulltext].
  - Two "positive" observational studies (Nigeria, Kenya) had large baseline imbalances the review flags as bias concerns (e.g. baseline stunting 22% vs 44% intervention vs control) [PMID 39422072, fulltext].

  **Brazil PNAE [oa_W1966655996]:** no quantitative nutrition effect sizes reported (policy review only) — **(no effect sizes in corpus)**.

- **Mechanism of action:** Two distinct mechanisms. (1) *Direct*: a free cooked school meal (India MDM mandates ≥450 kcal and 12 g protein per meal [oa_W3182946627]) supplies energy, protein and micronutrients to school-age children, plus attendance/enrolment incentives. (2) *Intergenerational / nutrition-sensitive*: girls exposed to school meals attain more education, marry/give birth later, have fewer children, and use more antenatal and institutional-delivery care — all upstream determinants of their future children's linear growth [oa_W3182946627]. Note the direct maternal-height pathway was **not** significant (p = 0.163), so the intergenerational effect runs mainly through education and fertility/health-service pathways, not maternal stature.

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is **false** and `cea_record` is **null**; no ICER, cost-per-DALY, or cost-per-child figure exists in the corpus for this intervention. Per the CEA guard, no cost-effectiveness rating is assigned. (Any "school meals cost $X per child" figure would be background knowledge and is deliberately excluded — not in corpus.)

- **Government scaling pathway:** Strong platform fit — school feeding is already delivered at national scale by governments in the exact settings studied. India's MDM served **97.8 million children/day** in 2016–17, the world's largest such program, mandated by the Supreme Court and centrally funded [oa_W3182946627]. Brazil's PNAE is a national, legislated, intersectoral program linked to family-farming procurement [oa_W1966655996]. All nine SSA countries in the systematic review "reported having national SMP" [PMID 39422072]. Delivery rides on existing school infrastructure, so the pathway is **Proven national**. The binding constraints are implementation quality, not existence: the SSA review catalogued **53 implementation challenges** (food preparation, distribution to students, funding, monitoring, coordination) against 37 facilitators [PMID 39422072].

- **Caveats:**
  - **Study type (population).** The direct-nutrition evidence is overwhelmingly in **school-age children (5–18 y)**, outside the under-5/WRA target window. The link to under-5s is *indirect* — the intergenerational MDM finding — and to WRA is via the education/fertility mediators. This indirectness is the primary reason for Grade C.
  - **Design.** No meta-analysis; the strongest under-5-relevant result [oa_W3182946627] is an observational econometric analysis (birth-cohort fixed effects / controlled interrupted time series), explicitly acknowledged by its authors as not a randomized design; it estimates intent-to-treat associations, not causal RCT effects.
  - **Heterogeneity / no pooling.** The SSA systematic review [PMID 39422072] could not pool and its included RCTs are directly contradictory (Ghana RCT null on HAZ overall; benefits only in subgroups). Two "positive" studies carry serious baseline-imbalance bias flagged in the review.
  - **Underpowered/null pathways.** Direct maternal adult height (+0.51 cm, p = 0.163) and several anthropometric outcomes (wasting, overall HAZ/BAZ in the Ghana and Ethiopia studies) are null or non-significant. Report these separately from the positive HAZ signal.
  - **Version/overlap:** none — no shared `cochrane_id`, no shared included trials across the three records; each is counted once.
  - **Model dependence:** the headline +0.40 SD attenuates to +0.115–0.261 SD in raw/alternative specifications [oa_W3182946627]; cite the range, not the single figure, when characterizing effect magnitude.

  **Tier rationale:** promising and highly scalable (already national in the study settings) but evidence for the target populations is indirect/observational with no meta-analysis and no CEA → **Tier 3**.

## Vitamin D supplementation for children under 5 (and status in WRA)  (children under 5; women of reproductive age)
**Evidence: C  |  Cost-effectiveness: Unknown  |  Scalability: Requires investment  |  Tier 3**

- **Evidence base:** The bundle contains 3 meta-analysis-tier records, but only **one** tests supplementation as an intervention: the Cochrane review *"Vitamin D supplementation for preventing infections in children under five years of age"* (PMID 27826955, cochrane_id CD008824; journal = *The Cochrane database of systematic reviews*; study_design = Cochrane review). It pooled just **4 RCTs / 3,198 children** (Afghanistan, Spain, USA), with GRADE certainty ranging from **very low to moderate** across outcomes (downgraded for imprecision and indirectness). The other two records are **prevalence/burden meta-analyses, not intervention trials**: a systematic review & meta-analysis of vitamin D deficiency in Africa (PMID 31786117, *The Lancet Global Health*, 129 studies) and a systematic review & meta-analysis of vitamin D insufficiency in South Asian pregnant women (PMID 34725002, *The British Journal of Nutrition*, 20 studies / 7,804 participants). Because only one intervention review exists — and it found no benefit — the intervention evidence is rated **C (limited)**.

- **Effect sizes (intervention — infection prevention, children under 5; PMID 27826955):**
  - *All-cause mortality:* **RR 1.43 (95% CI 0.54–3.74)**, 1 trial, 3,046 participants, low-quality evidence — underpowered (few events); direction null, cannot conclude either way.
  - *Cause-specific mortality (pneumonia/septicaemia):* **RR 1.50 (95% CI 0.42–5.30)**, 1 trial, 3,046 participants — an **underpowered cause-specific pathway** reported by a single trial; no TB, diarrhoea, or malaria cause-specific mortality reported by any trial.
  - *Pneumonia incidence (radiologically confirmed, first/only episode):* **rate ratio 1.06 (95% CI 0.89–1.26)**, 2 trials, 3,134 participants, moderate-quality — null.
  - *Repeat episodes of pneumonia (radiologically confirmed):* **RR 1.69 (95% CI 1.28–2.21)**, 1 trial, 3,046 participants — a statistically significant signal of **harm**, but confined to the single Afghanistan trial and judged by the review authors to be likely a chance finding (not reflected in confirmed-or-unconfirmed pneumonia, RR 1.06, 95% CI 1.00–1.13).
  - *Hospital admission (any):* **RR 0.86 (95% CI 0.20–3.62)**, 1 trial, 88 participants, very low-quality — null.
  - *Mean serum 25(OH)D at end of supplementation:* **MD +7.72 ng/mL (95% CI 0.50–14.93)**, 4 trials, 266 participants, low-quality — the biomarker moved, but the effect was driven by two small trials (Greer 1981, Greer 1989); in the two larger trials concentrations were not sustained to end of supplementation.
  - **Dominant trial:** the Afghanistan trial **Manaseki-Holland 2012** (3,046 participants) carries the dominant weight for pneumonia, diarrhoea, and mortality outcomes — essentially all clinically meaningful conclusions rest on this single trial.
  - *All-cause vs cause-specific:* the all-cause mortality finding (null, underpowered) and the cause-specific pneumonia/septicaemia finding (null, single trial) are both **too underpowered to support any conclusion**; TB and malaria — the two outcomes the review was designed to assess — had **zero** eligible trials.

- **Status/burden context (not intervention effects):**
  - *Africa deficiency prevalence (PMID 31786117, random-effect):* **18.46% (95% CI 10.66–27.78) below 30 nmol/L**, **34.22% (95% CI 26.22–43.68) below 50 nmol/L**, **59.54% (95% CI 51.32–67.50) below 75 nmol/L**; heterogeneity I² 98–99%. Lowest mean 25(OH)D in newborns (50.6 nmol/L, 95% CI 38.91–62.29) and pregnant women/new mothers (65.73 nmol/L, 95% CI 45.65–85.81).
  - *South Asian pregnant-women insufficiency (PMID 34725002):* pooled **65% (95% CI 51–78%)**; Pakistan 76%, India 67%, Bangladesh 64%, Nepal 14% (subgroup CIs not in corpus); heterogeneity I² 99.37%.
  - These establish a substantial deficiency burden in exactly the target populations, but say nothing about whether supplementation prevents disease.

- **Mechanism of action:** Vitamin D (25(OH)D → active 1,25(OH)D via the vitamin D receptor) supports calcium homeostasis and bone growth (deficiency → rickets) and modulates innate immunity — inducing antimicrobial peptides (cathelicidin, defensins) and altering macrophage/T-cell activity, the basis for the hypothesised anti-infective effect against pneumonia, TB, diarrhoea, and malaria (PMID 27826955, full text).

- **Cost-effectiveness:** **Unknown — no CEA record retrieved.** The bundle's `cea_rating_allowed` is false and `cea_record` is null, so per the CEA guard no cost-effectiveness rating is assigned. (The Cochrane full text mentions a single small UK costing study, Zipitis 2006, but this is background narrative, not a corpus CEA record, and is not a figure this synthesis can rely on.)

- **Government scaling pathway:** Vitamin D drops/dosing are cheap, oral, and administrable through routine infant health-facility and immunisation contacts (dosing schedules from 400 IU/day daily to quarterly 100,000 IU boluses appear in the included trials). Platform fit is therefore good in principle. However, given the **absence of demonstrated morbidity/mortality benefit** and no CEA record, there is currently **no evidence base to justify national scaling for infection prevention** — hence "Requires investment": additional adequately powered trials in high-deficiency LMIC settings are the prerequisite, not roll-out.

- **Caveats:**
  - *Thin, single-trial-dominated evidence:* nearly all conclusions rest on one Afghanistan trial (Manaseki-Holland 2012); only 4 RCTs total met inclusion.
  - *Underpowered pathways:* all-cause mortality and cause-specific (pneumonia/septicaemia) mortality are underpowered; **TB and malaria had no trials at all** despite being primary review objectives.
  - *Possible harm signal:* a significant increase in repeat radiologically-confirmed pneumonia (RR 1.69) in the supplemented group — flagged by the review as a likely chance finding but not dismissable.
  - *Version/overlap:* CD008824 is a single Cochrane review (`pub2`); counted once. No trial overlap with the two prevalence meta-analyses, which are burden studies, not intervention evidence and must not be counted toward intervention effect.
  - *Heterogeneity:* the two prevalence meta-analyses show extreme, unexplained heterogeneity (I² 98–99%), so their pooled prevalences are indicative burden figures only.


# Cross-cutting findings

Six patterns recur across the 23 interventions. Each is grounded in the corpus;
effect sizes carry the corpus PMID/key that reported them.

**1. Micronutrient *status* moves reliably; *growth* and *mortality* do not.**
The most consistent, highest-certainty effects in the whole corpus are on anaemia
and micronutrient deficiency: staple/condiment fortification cuts anaemia ~43%
(RR 0.57, 95% CI 0.39–0.82; PMID 35753314), double-fortified salt RR 0.59
(0.46–0.77; PMID 29767699), antenatal IFA RR 0.66 (0.53–0.81; PMID 37131925),
and MMS-vs-IFA cuts low birth weight (RR 0.88, 0.85–0.91, high certainty; PMID
30480324). Anthropometric endpoints are far stickier — fortification growth
effects are "consistently null," and cash transfers move linear growth only
slightly (HAZ +0.024, 95% CI 0.004–0.044) with null weight-for-height. Programmes
should be justified on the outcome the evidence actually supports (usually
status/anaemia), not assumed to reduce stunting or mortality.

**2. Diet-quality gains do not reliably become anthropometric gains.**
Interventions acting through household economics or food access improve dietary
diversity but stall on growth: nutrition-sensitive agriculture raises child
minimum dietary diversity (RR 1.19–1.27, UPAVAN RCT; PMID 32970116) yet leaves
wasting unchanged (RR 0.96, 95% CI 0.73–1.26); cash transfers and social
protection show the same diet-up / anthropometry-flat split. This
diet-to-growth disconnect is the single most repeated null in the corpus.

**3. All-cause signals are robust; cause-specific pathways are underpowered.**
The VAS pattern generalises. Vitamin A cuts all-cause under-5 mortality
(random-effect RR 0.76, 0.69–0.83; PMID 21868478) but its measles-, pneumonia-,
and meningitis-specific estimates all cross 1; the integrated home-visit
breastfeeding package cuts all-cause neonatal mortality (RR 0.76, 0.62–0.92;
PMID 31852432) while single-pathway effects are weaker. Reading only the headline
all-cause number overstates mechanistic certainty.

**4. The cost-effectiveness blind spot is structural — and the two-phase guard
caught it.** Every *direct* nutrition intervention carries a grounded ICER from
the corpus: CMAM US$23–53/DALY, food fortification <$150/DALY in 58% of analyses
(PMID 41620176), complementary feeding $23–242/DALY, breastfeeding $103–11,353/DALY,
vitamin A $220–860/DALY (PMID 35390077). Every *nutrition-sensitive / policy*
intervention — nutrition-sensitive agriculture, social protection, multisectoral
packages, maternal-nutrition counselling, growth monitoring, school feeding —
returned **no** nutrition-specific CEA and is therefore rated **Unknown**, never
guessed. This is the exact failure the pipeline was rebuilt to prevent (VAS was
once rated "Very High" with zero CEAs in scope).

**5. Delivery platform — not efficacy — gates scalability.** "Proven national"
tracks the existence of a government carrier: Child Health Days (vitamin A),
antenatal care (IFA, MMS), MCH/CHW/BFHI (breastfeeding), the salt and staple
industries (fortification), national CMAM protocols. Interventions with equally
strong or stronger evidence but no built delivery/financing platform — SQ-LNS,
the MMS transition — are "requires investment." Evidence strength and
scalability are decoupled; the binding constraint is usually the platform.

**6. Benefit is bounded by age, deficiency, and co-exposure — blanket delivery
erodes it.** Vitamin A works at 6–59 months but is null in neonates with a harm
signal (bulging fontanelle RR 1.53, 1.12–2.09; PMID 37133295); iron/MNP benefit
is conditional on anaemia burden and can be **net-harmful in high-malaria
settings** (MNPs modelled net-harmful in 24/78 countries; OpenAlex W3044712618);
fortification helps anaemia but not growth. Targeting to the deficient population
and setting is not an implementation detail — it determines whether the
intervention helps or harms.

**A note on the evidence base itself.** The tiering also exposes an uneven
evidence frontier: Tier-1/2 direct interventions rest on multiple RCTs and
meta-analyses, whereas the nutrition-sensitive tail (social protection,
nutrition-sensitive agriculture, multisectoral packages) rests on observational
and quasi-experimental studies with no completed meta-analyses or RCTs in the
corpus. Their lower tier reflects **evidence maturity**, not established
ineffectiveness — several are biologically plausible and nationally scalable and
would move up with better trials and dedicated cost-effectiveness studies.


# Appendix A — Full-corpus re-shortlist delta

Interventions that earned a full section here but were **not** in the original 15-item (top-200-derived) shortlist — i.e. surfaced only by reading deeper into the corpus:

- **multisectoral** — 43 papers (cost-effectiveness Unknown — no CEA record)
- **maternal_nutrition_other** — 42 papers (cost-effectiveness Unknown — no CEA record)
- **nutrition_sensitive_ag** — 30 papers (cost-effectiveness Unknown — no CEA record)
- **social_protection** — 17 papers (cost-effectiveness Unknown — no CEA record)
- **multiple_micronutrient_children** — 9 papers (cost-effectiveness Unknown — no CEA record)
- **growth_monitoring** — 4 papers (cost-effectiveness Unknown — no CEA record)
- **vitamin_d_children** — 3 papers (cost-effectiveness Unknown — no CEA record)
- **school_feeding** — 3 papers (cost-effectiveness Unknown — no CEA record)

A further 91 categories appeared below the evidence threshold (mostly observational determinant/surveillance studies and health-systems topics rather than discrete nutrition interventions); they are recorded in the evidence database but not given sections.
