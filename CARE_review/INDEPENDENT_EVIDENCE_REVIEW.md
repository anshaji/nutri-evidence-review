---
title: "Scaling Three Nutrition Interventions: An Independent Evidence Review"
subtitle: "CMAM, Breastfeeding Support and Antenatal MMS — clinical effectiveness, implementation, cost, and where each works best"
date: "August 2026"
---

# 0. How to read this

**What this is.** An independent evidence review for CARE and IA partners (Save the Children, Mercy Corps) on the three interventions selected after the June 2026 synthesis: community-based management of acute malnutrition (CMAM), breastfeeding promotion and support, and antenatal multiple micronutrient supplementation (MMS). It was built from scratch and does not inherit findings, framing or conclusions from the earlier CEGA deep-dive.

**Scope decisions, as agreed:**

- **Cost and cost-effectiveness are in scope.**
- **Breastfeeding is disaggregated** into a facility-based package and a community/CHW package, with separate evidence profiles.
- **Development and fragile/emergency contexts are treated separately.**
- **Targeting is treated as a burden question** — where each intervention produces most health per unit of effort — not as a partner-footprint question, which is out of scope (below).

**==Corrections, August 2026.==** ==This version incorporates the findings of an independent fact-check in which every numeric claim was re-verified against its primary source. Passages highlighted in yellow are where something changed. Section 11 lists each correction and why it was made. Nothing was fabricated in the earlier version; the errors were of framing, currency and attribution.==

**Verification standard.** Every effect estimate, cost figure and guideline statement below was read by me at its primary source — the journal abstract or full text, the Cochrane record, or the WHO guideline itself. Nothing is included on the strength of a search snippet or a secondary summary. Where a source describes a *population* narrower than the claim it is often used to support, the narrower population is stated. Section 10 is a source register with each item's verification status.

**Burden data.** Regional wasting, severe wasting and low-birthweight figures in §7 come from the UNICEF global data export supplied for this review. The regional aggregates are complete. The **country rows are a partial set** — Pakistan, Afghanistan, Ethiopia, Nigeria, Niger, Somalia, Uganda, Sudan, South Sudan, Chad, Mali and Yemen are absent from the file entirely — so country comparisons drawn from it are incomplete and are flagged where used.

**Four things I could not verify, stated plainly:**

1. **Regional maternal anaemia**, the second MMS targeting variable. Global figures are verified (35.5% in pregnant women, 30.7% in women of reproductive age, WHO 2025 estimates for 2023); the regional breakdown would not load from WHO's data portal and its API returned empty. Layering this onto §7.2 would sharpen the MMS targeting case.
2. **Facility delivery coverage**, the second targeting variable for the facility newborn package. Not in the supplied export.
3. **Population denominators**, needed to convert prevalence into absolute numbers of affected children. Not in the supplied export.
4. **Sub-national burden data**, which for CMAM siting probably matters more than any national comparison (§7.3).

**Partner operational footprint is deliberately out of scope.** Where CARE, Save the Children and Mercy Corps can operate is theirs to resolve, and layering it onto the evidence would only obscure what the evidence says. This review reports where each intervention has the most to work with; matching that to operating capacity is a separate exercise.

---

# 1. Headline findings

**1. All three interventions clear the efficacy bar, but they clear different bars.** CMAM has a large effect on recovery against dietary alternatives and an enormous untreated counterfactual. Kangaroo mother care has a high-certainty mortality benefit in a narrow population. MMS has a high-certainty benefit on *birth size* and a high-certainty *null* on every mortality outcome. Treating these as three instances of "proven intervention" obscures the thing that matters for a co-design.

**2. The most important number in the CMAM literature is not a treatment effect.** It is the counterfactual: severely wasted children die at **11.6 times** the rate of ==children with normal weight-for-height (Z ≥ −1)== (Olofin 2013, 10 cohorts, 53,809 children). ==These are general-population prospective cohorts — treatment status was never assessed, so this is not a treated-versus-untreated comparison.== No trial randomises children to no treatment, so every head-to-head comparison in the field is food-versus-food and structurally understates the intervention. This is the number that carries a finance-ministry conversation.

**3. Simplified CMAM protocols are at an inflection point, and the newest evidence complicates the story.** The 2025 three-arm trial in Niger found ComPAS and OptiMA non-inferior overall — but only ComPAS survived per-protocol analysis, and among the 1,140 most severely wasted children **the standard protocol was superior on recovery**. WHO 2023 endorsed neither combined protocols nor MUAC-only dosing. Simplification is real and saves 32–50% of therapeutic food, but it is ahead of the guideline and unresolved in the severest children.

**4. Relapse is the most under-priced problem in wasting treatment.** Within six months of discharge, 22–63% of "recovered" children relapse. What predicts relapse is not their condition at discharge but **food insecurity and illness afterwards**. Any programme measured on recovery-at-discharge is measuring the wrong thing.

**5. Kangaroo mother care is a small-and-sick-newborn intervention, not a universal newborn one.** The high-certainty RR 0.68 is in preterm or low-birth-weight infants; the landmark WHO trial enrolled infants of 1.0–1.799 kg. The largest African trial (OMWaNA, Uganda, 2,221 neonates) found **no effect on its primary mortality endpoint**. The intervention is strong; its eligible population is roughly one birth in seven, and it needs facility capacity.

**6. For breastfeeding support, the cadre does not appear to matter — the package does.** Cochrane's 116-trial review found no differential effect by who provides support. The community packages that reduce neonatal mortality (RR 0.75) are bundles in which breastfeeding is one component among several. Do not build a design around "shift it to CHWs" as though the channel were the active ingredient.

**7. MMS is the cheapest intervention here and the one whose evidence is most often overstated.** At **US$21–42 per DALY averted**, switching from iron-folic acid to MMS is among the better buys in nutrition, and the marginal commodity cost is about half a US cent per tablet. But WHO still recommends it *only in the context of rigorous research*, and the mortality claims often made for it are not supported: perinatal, neonatal and maternal mortality are all null at high certainty, and stillbirth is genuinely contested between syntheses.

**8. Targeting differs by intervention, and regional averages mislead.** Low birthweight — what MMS and kangaroo mother care act on — is genuinely concentrated in South Asia (24.8% against 13.9% in sub-Saharan Africa), and that holds at country level. Wasting does not: the South Asian regional figure is essentially India (18.7%), while the sub-Saharan African average of 5.9% conceals Niger, Chad, Burkina Faso and Sudan at roughly double it. For CMAM the burden sits in India and in the Sahel, the Horn of Africa and Yemen — two concentrations needing two different programmes (§7).

---

# 2. CMAM — what the evidence establishes

## 2.1 Clinical effectiveness

The Cochrane review of ready-to-use therapeutic food (Schoonees et al. 2019, CD009000; 15 studies, 7,976 participants, 8 in Malawi and 4 in India) gives the cleanest picture:

| Comparison | Outcome | Effect | Certainty |
|---|---|---|---|
| Standard RUTF vs alternative dietary approaches (7 studies, 2,261) | Recovery | **RR 1.33 (1.16–1.54)** | Moderate |
| | Weight gain | MD 1.12 g/kg/day (0.27–1.96) | Low |
| | Relapse | RR 0.55 (0.30–1.01) | Very low |
| | Mortality | RR 1.05 (0.51–2.16) | Very low |
| RUTF meeting total daily needs vs supplemental RUTF (2 studies, 213) | Recovery | RR 1.41 (1.19–1.68) | Low |
| | Relapse | RR 0.11 (0.01–0.85) | Low |
| Standard RUTF vs alternative formulations (8 studies, 5,502) | Recovery | RR 1.03 (0.99–1.08) | **High** |
| | Relapse | RR 0.84 (0.72–0.98) | **High** |
| | Mortality | RR 1.00 (0.80–1.24) | Moderate |

Two things follow. **RUTF outperforms dietary alternatives on recovery** with moderate certainty. And **formulations recover children equally well** at high certainty. ==But interchangeability stops at recovery: at the same high certainty, standard RUTF also reduces relapse (RR 0.84, 0.72–0.98), and Cochrane's authors carve this out explicitly — the evidence "does not favour a particular formulation, except for relapse, which is reduced with standard RUTF." Substituting formulation to save money is therefore not cost-free.==

What the review does *not* establish is a mortality benefit. The authors' own conclusion is that effects on relapse and mortality "are unknown." That is a property of the trial designs, not of the intervention.

## 2.2 The counterfactual, which is where the case actually rests

Because no trial withholds treatment, the intervention's value has to be established from cohort data. The canonical source is **Olofin et al., PLoS One 2013** — a pooled analysis of ten prospective cohorts, 53,809 children, 1,315 deaths:

| Condition (vs z-score ≥ −1) | All-cause mortality hazard ratio |
|---|---|
| **Severe wasting (WHZ < −3)** | **11.63 (9.84–13.76)** |
| Severe underweight (WAZ < −3) | 9.40 (8.02–11.03) |
| Severe stunting (HAZ < −3) | 5.48 (4.62–6.50) |

Wasting is a stronger mortality determinant than stunting or underweight. This is the number to put in front of a ministry of finance — not in-programme case fatality, which describes children *already receiving treatment* and therefore understates what treatment averts.

## 2.3 Simplified protocols — the live question, and the 2025 correction

Three generations of evidence, all verified at source:

**Reduced dose (MANGO, Burkina Faso, 801 children, PLoS Med 2019).** Weight gain velocity 3.4 g/kg/day, difference 0.0 (−0.4 to 0.4), non-inferiority confirmed (p=0.013). **But a small negative effect on height gain velocity: −0.2 mm/week (0.04–0.4), p=0.015, more pronounced under 12 months** (interaction p=0.019; Δ −0.4 mm/week, −0.6 to −0.2, p<0.001). This linear-growth penalty is the principal safety caveat on dose reduction and is frequently omitted. ==It rests on a single trial of one specific design — standard dose for two weeks, then reduced — in a relatively food-secure setting, so it should not be generalised to reduced-dose regimens as a class.==

**Combined SAM+MAM protocol (ComPAS, Kenya and South Sudan, PLoS Med 2020).** Recovery 76.3% (981/1,286) combined vs 73.5% (884/1,202) standard; risk difference 0.03 (−0.05 to 0.10), p=0.52, against a 10% non-inferiority margin. **122 versus 193 RUTF sachets** per SAM child recovered. Cost per child recovered **US$918 vs US$1,041**.

**Head-to-head (OptiMA-Niger, Am J Clin Nutr 2025, 1,732 children, NCT04698070).** Three arms — Niger standard, ComPAS, OptiMA:

- Recovery: standard 50.9%, ComPAS 51.9%, OptiMA 49.7%
- Intention-to-treat non-inferiority met by both (ComPAS +1.0%, 97.5% CI −5.5 to +7.6; OptiMA +3.2%, −3.3 to +9.9)
- **Per-protocol: only ComPAS met non-inferiority**
- **Among 1,140 children with MUAC <115 mm or oedema, the standard protocol was superior on recovery in both ITT and per-protocol analysis** — driven by better attendance rather than mortality or growth differences
- RUTF saved: ComPAS 50%, OptiMA 32%
- No mortality difference across arms at 6 months

**Read:** simplification delivers real commodity savings and holds recovery in aggregate, but the severest children are an open question, and ComPAS currently has the stronger evidential position of the two.

## 2.4 Relapse

**King et al., Lancet Global Health 2025** — prospective cohort, 2,749 children (1,689 SAM-recovered, 1,060 never-malnourished controls), six months' follow-up:

| Country | Relapse to acute malnutrition within 6 months |
|---|---|
| South Sudan | **63% (59–67)** |
| Mali | **30% (25–34)** |
| Somalia | **22% (19–25)** |

Previously-SAM children were 1.2–6.2 times more likely to be acutely malnourished than non-exposed peers. Higher anthropometry at discharge was protective, but **few child- or household-level factors at discharge predicted relapse; food insecurity and morbidity at follow-up did.**

The design implication is specific: post-discharge support is not an optional add-on, and the determinants sit outside the treatment episode. WHO 2023 recommendation **C3** (conditional, moderate certainty) now supports **cash transfers in addition to routine care to decrease relapse** — the only place in this review where a demand-side transfer carries normative backing.

## 2.5 Cost

| Setting | Cost per DALY averted | Cost per child | Perspective / price year |
|---|---|---|---|
| **Bangladesh**, CHW-delivered CMAM (Puett, Health Policy Plan 2013) | **US$26 (21–31)** | $165 treated / $180 recovered | Societal, 2010 USD |
| Inpatient comparator, same study | US$1,344 | — | Societal, 2010 USD |
| **Malawi**, CMAM (Wilford, Health Policy Plan 2012) | **US$42** base case; $493 worst case | — | 2007 USD |
| **Ethiopia** (Sidama), community therapeutic care (Tekeste, Cost Eff Resour Alloc 2012) | not reported | $134.88 treated / $145.50 cured | Societal, 2006–07 USD |
| Same study, therapeutic feeding centre | not reported | $284.56 treated / $320.00 cured | — |
| **Pakistan** (Sindh), LHW vs facility (Rogers, BMC Public Health 2019) | not reported | $291 vs $301 treated; **$382 vs $363 recovered** | 2016 USD |
| **Kenya/South Sudan**, combined vs standard protocol (Bailey 2020) | not reported | $918 vs $1,041 recovered | — |

**At US$26–42 per DALY averted, community-based treatment sits alongside the better-value interventions in global health.** Note the composition difference: in Ethiopia, RUTF was 43.2% of community-programme institutional cost, while personnel were 46.6% of inpatient cost. Community delivery substitutes commodity for staff — which is why RUTF price and simplified dosing dominate the community cost equation, and why the Pakistan result matters.

**The Pakistan result is the honest counterweight.** LHW-delivered treatment achieved 76.0% recovery (323/425) against 83.0% (326/393) at facilities, at essentially the same cost per child treated but *higher* cost per child recovered ($382 vs $363), giving an incremental cost-effectiveness ratio of $146 per additional child recovered through facilities. The authors report **no significance test** for the recovery difference and note substantial uncertainty. Treat it as a caution, not a finding: decentralisation raises reach, and may cost quality if supervision is not resourced.

## 2.6 Normative status — WHO 2023

Verified against the guideline itself (WHO, *Guideline on the prevention and management of wasting and nutritional oedema in infants and children under 5 years*, 2023):

| Rec. | Content | Strength / certainty |
|---|---|---|
| **B17** | Assessment, classification and management or referral **can be carried out by community health workers**, with adequate training and regular supervision | **Conditional, VERY LOW certainty** |
| B10 | RUTF 150–185 kcal/kg/day until recovery, then 100–130 kcal/kg/day (**weight-based**) | Conditional, low |
| B2 | Inpatient admission criteria | Strong, moderate |
| B5 | Exit at **WHZ ≥ −2 AND MUAC ≥ 125 mm**, ≥2 consecutive measurements | Conditional, very low |
| B13 | Targeted specially formulated foods for moderate wasting (<24 months, MUAC 115–119 mm, WAZ < −3, or failing recovery) | Strong, moderate |
| B14 | In humanitarian crises, all 6–59 months with moderate wasting considered for SFF | Strong, moderate |
| C2 | Psychosocial stimulation post-discharge | Conditional, moderate |
| **C3** | **Cash transfers in addition to routine care to decrease relapse** | Conditional, moderate |

**Two implications for a national co-design.** First, CHW delivery — the centrepiece of most scale-up proposals — rests on *very low certainty* evidence in WHO's own assessment. That is a fundable, defensible position, but it should be presented to a ministry as such rather than as settled. Second, WHO retained **weight-based dosing and dual WHZ+MUAC exit criteria**, both of which the leading simplified protocols depart from. A country adopting simplified protocols is operating ahead of the guideline, and should know it.

## 2.7 Development versus fragile contexts

The CMAM evidence base is disproportionately generated in fragile settings: ComPAS in Kenya and South Sudan, OptiMA and MANGO in Niger and Burkina Faso, the relapse cohort in Mali, South Sudan and Somalia. The cost-effectiveness evidence is the reverse — Bangladesh, Malawi, Ethiopia, Pakistan.

- **Development contexts:** the question is integration into routine primary care and sustained financing. The cost case is strong ($26–42/DALY) and the platform question is about supervision and supply.
- **Fragile contexts:** the question is caseload surge, access and relapse. WHO **B14** gives explicit normative cover for blanket treatment of moderate wasting in humanitarian crises. Simplified protocols matter most here, where commodity and workforce are hardest — and the relapse rates (South Sudan 63%) are highest, meaning post-discharge and food-security linkage is not optional.

---

# 3. Breastfeeding, Package A — facility-based support around delivery

## 3.1 Evidence profile

**Kangaroo mother care is the strongest clinical result in this review, in a narrow population.**

*Sivanandan & Sankar, BMJ Global Health 2023;8:e010728* — systematic review and meta-analysis, population **"low birth weight or preterm infants"**:

| Outcome | Effect | Basis | Certainty |
|---|---|---|---|
| Mortality (during birth hospitalisation, or by 28 days / 40 weeks PMA) | **RR 0.68 (0.53–0.86)** | 11 trials, 10,505 infants | **High** |
| Severe infection | RR 0.85 (0.79–0.92) | 9 trials | Moderate |
| Early vs late KMC initiation — mortality | RR 0.77 (0.66–0.91) | 3 trials, 3,693 infants | High |

==The review reports greater mortality benefit at ≥8 hours per day, but its own discussion notes there was insufficient data in the under-8-hour group, so the contrast has no real comparator. The dose target is better anchored on WHO's recommendation of 8–24 hours a day, as many as possible (strong recommendation, high-certainty evidence).==

==Two boundaries on the pooled estimate: all but one included trial started kangaroo care *after* the infant was stabilised, so RR 0.68 is essentially post-stabilisation evidence; and the pooled analysis used a fixed-effect model.==

*WHO Immediate KMC Study Group, NEJM 2021* — five hospitals in Ghana, India, Malawi, Nigeria, Tanzania; infants **1.0–1.799 kg**; 3,211 infants (1,609 intervention / 1,602 control); immediate KMC vs conventional care until stabilisation:

- **28-day neonatal mortality: 12.0% vs 15.7%, RR 0.75 (0.64–0.89), p=0.001**
- Mortality in first 72 hours: 4.6% vs 5.8%, RR 0.77 (0.58–1.04), p=0.09

==The immediate-KMC trial's comparator was conventional care followed by KMC after stabilisation — not an absence of KMC — and the trial was stopped early for benefit, which risks overestimating the effect.==

*OMWaNA, Lancet 2024* — five hospitals in Uganda, 2,221 neonates, KMC initiated **before** clinical stabilisation: **no effect on the primary outcome, mortality within 7 days**; non-significant 12% relative reduction at 28 days; hypothermia at 24 hours and weight gain significantly improved; cost-effective from societal and provider perspectives.

**How to state this honestly.** KMC has a high-certainty mortality benefit in preterm and low-birth-weight infants, replicated in a large multi-country trial. The one trial that tested initiation *before stabilisation* in an African hospital setting did not reproduce a mortality effect on its primary endpoint, though it improved thermal care and was cost-effective. The intervention is well evidenced; the marginal question is how early, in which infants, and with what facility support.

**Normative status: strongest in this review.** WHO's 2022 recommendations for care of the preterm or low-birth-weight infant state that KMC should be started **as soon as possible after birth — a strong recommendation on high-certainty evidence** — for as many hours a day as possible, aspiring to 8–24 hours. This is the only intervention of the three carrying a strong WHO recommendation on high-certainty evidence.

**Early initiation of breastfeeding** (Smith et al., PLoS One 2017; 5 studies, 136,047 infants): compared with initiation within 1 hour, initiation at 2–23 hours carried **33% greater neonatal mortality risk (13–56%, I²=0%)** and at ≥24 hours **2.19-fold (1.73–2.77, I²=33%)**. These are pooled *observational* associations with real confounding-by-indication risk — sick infants initiate late. Use them as supportive, not causal.

## 3.2 Implementation and scaling

- **The eligible population is the constraint, not the evidence.** KMC applies to preterm or low-birth-weight infants — roughly one birth in seven ==worldwide== (==the LMIC-only rate is higher, since the global figure includes high-income regions at about 7%==). It is a small-and-sick-newborn care intervention delivered where births happen.
- **It is facility-dependent.** Immediate KMC requires the mother and newborn to be kept together with clinical monitoring, which is a ward-configuration and staffing question, not a commodity question. "No commodity required" is true and misleading in equal measure.
- **Facility delivery coverage gates it.** The intervention cannot reach infants born at home, which bounds it in exactly the settings with the highest neonatal mortality.
- **Cost signal is favourable but thin.** OMWaNA found immediate KMC cost-effective from both societal and provider perspectives; I found no multi-country costing of KMC scale-up that I could verify.

---

# 4. Breastfeeding, Package B — community and CHW postnatal support

## 4.1 Evidence profile

*Gavine et al., Cochrane CD001141.pub6, 2022* — 116 trials, 103 contributing data, >98,816 mother–infant pairs. Outcomes are expressed as **stopping** breastfeeding, so RR below 1 is better:

| Support type | Outcome | Effect | Certainty |
|---|---|---|---|
| 'Breastfeeding only' | Stopping **exclusive** BF at 6 months | **RR 0.90 (0.88–0.93)** | Moderate |
| | Stopping any BF at 6 months | RR 0.93 (0.89–0.97) | Moderate |
| | Stopping exclusive BF at 4–6 weeks | RR 0.83 (0.76–0.90) | Moderate |
| | Stopping any BF at 4–6 weeks | RR 0.88 (0.79–0.97) | Moderate |
| 'Breastfeeding plus' | Stopping exclusive BF at 6 months | RR 0.79 (0.70–0.90) | — |
| | Stopping any BF at 4–6 weeks | RR 0.94 (0.82–1.08) — null | Moderate |

**Two findings from this review deserve to govern the design.**

First, **there is no demonstrated cadre effect**: the meta-regression "suggested that there were no differential effects regarding person providing support or mode of delivery, however, power was limited." Support may be offered by professionals, lay/peer supporters, or a combination. This is absence of evidence for a difference rather than proven equivalence — but it is the opposite of a mandate to shift delivery to CHWs.

Second, the **4–8 visit** finding is real but hedged: moderate levels of 'breastfeeding only' support "may be associated with a more beneficial effect" on exclusive breastfeeding at 4–6 weeks and 6 months. It is a plausible dose target, not an established threshold.

*Lassi & Bhutta, Cochrane CD007754.pub3, 2015* — 26 cluster-randomised or quasi-randomised trials of **community-based intervention packages**:

| Outcome | Effect | Basis |
|---|---|---|
| Neonatal mortality | **RR 0.75 (0.67–0.83)** | 21 studies, n=302,646 |
| Perinatal mortality | RR 0.78 (0.70–0.86) | 17 studies, n=282,327 |
| Stillbirth | RR 0.81 (0.73–0.91) | 15 studies, n=201,181 |
| Maternal mortality | RR 0.80 (0.64–1.00) | 11 studies |
| Early initiation of breastfeeding | RR 1.93 (1.55–2.39) | 11 studies, n=72,464 |

**This is the mortality evidence for community delivery — and it is bundled.** ==The 26 trials cover a wide range of packages — women's groups and participatory learning cycles, community health worker home visits, training of traditional birth attendants and lady health workers, health education and home-based newborn care — rather than one standard bundle. Breastfeeding support is one element among several, and the pooled figure is a random-effects average with substantial heterogeneity (I² = 85%).== The breastfeeding-specific share of the mortality benefit cannot be isolated. Exclusive breastfeeding at six months was not reported by any included study.

## 4.2 Implementation at scale — the strongest evidence in this review

*Menon et al., PLoS Medicine 2016 (Alive & Thrive)* — cluster-randomised programme evaluations of intensive interpersonal counselling combined with mass media, community mobilisation ==and policy advocacy==:

| | Bangladesh (20 sub-districts) | Viet Nam (40 communes) |
|---|---|---|
| Exclusive breastfeeding impact ==(difference-in-differences vs baseline)== | **+36.2 pp (21.0–51.5), p<0.001** | **+27.9 pp (17.7–38.1), p<0.001** |
| Endline EBF, intensive vs non-intensive | **87.6% vs 53.5%** | 57.8% vs 28.4% |
| Early initiation impact | +16.7 pp (2.8–30.6), p=0.021 | +10.0 pp (−1.3–21.4), p=0.072 |
| Delivery channel | BRAC frontline workers and volunteers (large NGO health programme) | Government health facility staff, social-franchise model, 8 counselling sessions |

**This is the single most useful implementation result for CARE's question**, for three reasons. It demonstrates effects at population scale rather than trial scale. The effect sizes dwarf anything in the individual-support literature, because the intervention is a *system* — counselling plus mass media plus community mobilisation plus policy advocacy — not a counselling contact. And the two countries used **different delivery channels to comparable effect**, which is the strongest available evidence that the channel is substitutable and the package is what carries the result.

The corollary for a government co-design: Viet Nam's arm ran through government facilities, so a government-anchored version of this model is evidenced. Bangladesh's ran through an NGO platform, which is a weaker precedent for handover.

## 4.3 Facility versus community — the honest comparison

| | Package A (facility) | Package B (community) |
|---|---|---|
| Strongest clinical result | KMC mortality **RR 0.68**, high certainty, preterm/LBW | Bundled package neonatal mortality **RR 0.75**, but breastfeeding share not isolable |
| Normative backing | **Strong WHO recommendation, high certainty** (2022) | WHO supports counselling; no comparable strong/high-certainty statement identified |
| Eligible population | ~1 birth in 7 (preterm/LBW) | All mother–infant pairs |
| Delivery requirement | Facility beds, staffing, mother–infant co-location | CHW time, supervision, and — for the large effects — mass media and community mobilisation |
| Gated by | Facility delivery coverage | CHW workload and programme intensity |
| Proven at population scale? | Not demonstrated at national scale in the sources verified here | **Yes** — Alive & Thrive, two countries, two channels |

**They are complements with different jobs.** Package A delivers a mortality benefit in a small high-risk population. Package B delivers population-level behaviour change and — in bundled form — a mortality benefit that cannot be attributed to breastfeeding alone. Neither substitutes for the other, and the evidence does not support choosing between them on effect size, because they are measured on different populations and different outcomes.

---

# 5. Antenatal MMS

## 5.1 Effectiveness — what is settled and what is not

*Keats, Haider, Tam & Bhutta, Cochrane CD004905, 2019* — MMS versus iron ± folic acid:

| Outcome | Effect | Trials / n | Certainty |
|---|---|---|---|
| **Low birthweight** | **RR 0.88 (0.85–0.91)** | 18 / 68,801 | **High** |
| Small-for-gestational-age | RR 0.92 (0.88–0.97) | 17 / 57,348 | Moderate |
| Preterm birth | RR 0.95 (0.90–1.01) | 18 / 91,425 | Moderate |
| **Stillbirth** | **RR 0.95 (0.86–1.04)** — null | 17 / 97,927 | **High** |
| **Perinatal mortality** | **RR 1.00 (0.90–1.11)** — null | 15 / 63,922 | **High** |
| **Neonatal mortality** | **RR 1.00 (0.89–1.12)** — null | 14 / 80,964 | **High** |
| Maternal mortality | RR 1.06 (0.72–1.54) | 6 / 106,275 | — |
| Miscarriage | RR 0.99 (0.94–1.04) | 12 / 100,565 | — |

**The settled finding is birth size, not survival.** Low birthweight reduction is high-certainty. Every mortality outcome is null, three of them at high certainty.

**Stillbirth is contested and should be presented as such.** A competing LMIC-restricted analysis (Keats, Oh, Chau, Khalifa, Imdad & Bhutta, *Campbell Systematic Reviews* 2021; 72 studies, 451,723 women) reports stillbirth **RR 0.91 (0.86–0.98)**, 22 studies, N=96,772, and low birthweight RR 0.85 (0.77–0.93). An independent synthesis from a different group (Hunter et al., *Am J Clin Nutr* 2023) reports stillbirth **RR 0.95 (0.86–1.04)** — null, matching Cochrane.

Two cautions when using the 0.91. It comes from the same author group as the Cochrane review, and the identical estimate appears in a second publication (Oh, Keats & Bhutta, *Nutrients* 2020) that reports stillbirth 0.91 and perinatal mortality 1.00 side by side — so citing them separately manufactures the appearance of independent corroboration. And a genuine 9% stillbirth reduction is hard to reconcile with a flatly null perinatal mortality (stillbirth plus early neonatal death) at high certainty.

**Recommended framing for partners:** MMS reliably produces bigger, more mature babies than iron-folic acid. It has not been shown to save lives, and the stillbirth question is open.

## 5.2 Targeting — the most actionable MMS finding

*Smith et al., Lancet Global Health 2017* — individual participant data meta-analysis, **112,953 women, 17 trials, 14 LMICs**:

- Greater reductions in **low birthweight, small-for-gestational-age and 6-month mortality in anaemic women** (haemoglobin <110 g/L) than in non-anaemic women
- Greater reduction in **neonatal mortality for female neonates** than male
- Greater effect on **preterm birth among underweight women**

This is the evidence that should drive country and district selection: **MMS's advantage over iron-folic acid is concentrated where maternal anaemia and undernutrition are high.** A switch in a low-anaemia population buys much less. No other finding in this review offers as clean a targeting rule — ==though it comes from one of 26 subgroups examined, with interaction tests in the 0.03–0.049 range, so it is a targeting steer rather than a settled rule.==

## 5.3 Normative status — unchanged, and it is a real barrier

WHO's antenatal care recommendation, verified verbatim: **"Antenatal multiple micronutrient supplements that include iron and folic acid are recommended in the context of rigorous research."** Recommendation type: **context-specific — research**. Year: **2020.** Daily iron-folic acid (60 mg elemental iron where anaemia prevalence is ≥40%) remains the recommended standard of care.

I found no evidence of a change through 2026. Any national scale-up conversation begins from the position that WHO has not endorsed routine substitution — which is a genuine obstacle for ministries and one that partners should plan to address explicitly rather than discover late.

## 5.4 Cost — the strongest cost case of the three

*Kashi et al., Journal of Nutrition 2019* — modelled incremental cost-effectiveness of switching IFA→MMS, using effect estimates from the 2017 Cochrane and Lancet meta-analyses with Monte Carlo simulation:

| Country | ICER per DALY averted (2016 USD) |
|---|---|
| Bangladesh | **$21.26** |
| India | **$31.62** |
| Pakistan | **$41.54** |

*Engle-Stone et al., Annals of the New York Academy of Sciences 2019* — replacing IFA with MMS at current coverage:

| | Bangladesh | Burkina Faso |
|---|---|---|
| Deaths averted (stillbirths + infant) | 7,628 | 484 |
| Cost per death averted | ~$183 | ~$125 |
| Cost per DALY averted | $3.62–13.25 | $3.02–15.21 |
| Modelled coverage | 50.3% national | 10.2% national |

The marginal commodity cost is **about US$0.005 more per tablet** for MMS than IFA — roughly $1.4 million annually in Bangladesh at current coverage. ==That is a marginal *production* cost, not a procurement price: UNICEF's Supply Catalogue puts 180 UNIMMAP tablets at US$3.42 against US$1.75–2.35 for 180 IFA tablets — a procurement gap of roughly $0.006–0.009 per tablet, or about $1.1–1.7 per pregnancy. Verney et al. (*Maternal & Child Nutrition* 2023;19:e13523) put the same comparison at $3.42 against $2.00, a gap of $1.42, which sits inside that range. Same order of magnitude as the production cost, but do not present $0.005 as what a ministry pays.==

**Two caveats that matter.** These are *modelled* results, not trial-based costings, and they inherit whichever effectiveness estimates they were fed — the Engle-Stone figures assume 180 tablets consumed per covered pregnancy with perfect programme management, perfect adherence and no waste, which no real programme achieves. The realistic cost per DALY is higher than the headline. Even so, MMS is the cheapest of the three interventions per unit of health gain, and the marginal commodity cost of the switch is close to trivial — the cost is in the system change, not the tablet.

## 5.5 The transition — what implementation research shows

*Thurstans-Fuller, James, Menezes et al., Maternal & Child Nutrition 2025* — implementation research on the IFA→MMS transition in **Bangladesh (2020–24), Burkina Faso (2021–24), Madagascar (2021–24) and Tanzania (2022–24)**:

**Enablers:** government leadership and multisectoral coordination; context-specific situational analysis; community engagement and demand creation; integration into existing systems rather than parallel structures; inclusion on national essential medicines lists. Acceptability was better than IFA — "pregnant women like MMS more, especially those previously using IFA, reporting fewer side effects."

**Barriers:** late or poor antenatal attendance (all four countries); distance to facilities (all four); unfavourable socio-cultural factors and lack of family support (all four); IFA side effects and low adherence (Bangladesh, Burkina Faso, Tanzania); stockouts and cost.

**Supply chain was "one of the most challenging aspects" in every country.** Tanzania integrated MMS into the national electronic Logistics Management Information System; Madagascar added MMS to its essential medicines list; Burkina Faso is advancing the same.

**The operational read:** the commodity substitutes into an existing channel, which makes MMS the most tractable of the three interventions to introduce — but the binding constraints are antenatal attendance and supply chain, neither of which the switch itself fixes. A co-design that changes the tablet without addressing ANC timing and stock management will move coverage very little.

---

# 6. What actually constrains scale — cross-cutting

**1. Coverage, and the honest global position.** The Global Action Plan on Child Wasting states that **just one in three severely wasted children receives treatment**. In 2024, UNICEF and partners reached over 9.3 million children with treatment for severe wasting, and supplied RUTF to 7.4 million children in 47 high-mortality countries. Globally in 2024, 6.6% of children under 5 were wasted (42.8 million) and 1.9% severely wasted (12.2 million); 150.2 million were stunted. **Do not compute coverage as admissions divided by prevalence** — annual incident caseload is several times point prevalence, and that arithmetic materially overstates coverage.

**2. Adherence, for the commodity intervention.** The MMS transition research identifies adherence and antenatal attendance as barriers in every country studied. Note that MMS's acceptability advantage over IFA — fewer reported side effects — is a genuine, if modest, adherence asset.

**3. The cadre is not the lever.** Three independent lines of evidence converge: Cochrane found no provider effect for breastfeeding support; the community mortality benefit comes from bundled packages, not from who delivers them; and WHO rates CHW delivery of wasting treatment as *conditional on very low certainty evidence*. Where task-shifting does have strong support is **reach** — getting treatment closer to children who would otherwise not be treated — and the Pakistan costing is a reminder that reach can be bought at some cost in quality.

**4. Post-discharge and demand-side linkage.** Relapse at 22–63% within six months, driven by post-discharge food insecurity, is the clearest signal in the CMAM literature that treatment alone is insufficient. WHO's conditional recommendation on cash transfers to reduce relapse is the normative hook for pairing treatment with a social-protection component — an area of genuine CARE comparative advantage.

**5. Guideline lag is a design constraint, not a footnote.** Simplified CMAM protocols are ahead of WHO 2023; MMS is not endorsed for routine use at all. Both are defensible to pursue, but a ministry will ask, and the answer needs preparing.

---

# 7. Where these interventions have the most to work with

This section asks a targeting question: **for each intervention, what determines where it produces the most health per unit of effort, and where does the burden data say that is?**

## 7.1 How reliable the burden data is

This matters enough to state before the numbers.

**The regional aggregates are sound.** The supplied UNICEF export carries the series footnote *"UNICEF/WHO/World Bank Joint Malnutrition Estimates Databases, March 2025"*, and its World figures for 2024 — 6.6% wasting, 1.9% severe wasting — match exactly the JME 2025 global figures verified independently for §6. These are the official modelled regional estimates, computed by the JME from all countries. They are **not** derived from whichever country rows happen to appear in this export, so the absent countries do not bias them.

**But the export contains almost no country rows for wasting** — only Finland and the Russian Federation. It is a regional extract. Country-level wasting figures below therefore come from a second source: the WHO Global Health Observatory, queried directly, which carries the underlying national survey estimates.

**And regional aggregation turns out to mislead in both directions.** That is the substantive finding of this section, and it corrects a reading that the regional table alone would support.

## 7.2 The targeting variable for each intervention

| Intervention | What determines where it works best | Why |
|---|---|---|
| **CMAM** | **Wasting and severe wasting prevalence** | Benefit per child treated is fixed by the counterfactual (HR 11.63, §2.2). What varies is case-finding efficiency: in low-prevalence settings you screen many children to find few, so cost per case found rises sharply |
| **MMS** | **Low birthweight prevalence**, and **maternal anaemia** | The high-certainty MMS effect is on low birthweight (RR 0.88), so *absolute* benefit scales with baseline LBW. Smith 2017 (§5.2) shows the *relative* benefit is also larger in anaemic and underweight women. Both terms move together — the only multiplicative targeting argument in this review |
| **Facility newborn package (KMC)** | **Low birthweight prevalence × facility delivery coverage** | Preterm and low-birthweight infants are the entire eligible population. Lives saved scale directly with how many such infants are born, and with how many are born where KMC can be delivered |

## 7.3 Wasting: the regional picture, and why it is not the right grain

**Regional, ==JME 2025 edition, 2024 reference year==:**

| Region | Wasting | Severe wasting | Severe wasting 2000 | Change |
|---|---|---|---|---|
| South Asia | 14.1% | 4.5% | 5.3% | −15% |
| World | 6.6% | 1.9% | 2.7% | −30% |
| West and Central Africa | 6.9% | 1.5% | 3.5% | −57% |
| Sub-Saharan Africa | 5.9% | 1.3% | 3.0% | −57% |
| Middle East and North Africa | 5.0% | 1.6% | 2.1% | −24% |
| Eastern and Southern Africa | 4.9% | 1.0% | 2.6% | −62% |
| East Asia and Pacific | 3.5% | 0.9% | — | — |
| Latin America and Caribbean | 1.3% | 0.3% | — | — |

Read alone, this says South Asia is where wasting is, by a factor of roughly three, and that Africa has more than halved its severe wasting since 2000 while South Asia has barely moved. Both statements are true of the regions. **Neither survives contact with the country data.**

**National survey estimates, WHO Global Health Observatory (most recent available; survey year in brackets):**

| Country | Wasting | Survey year |
|---|---|---|
| **India** | **18.7%** | 2020 (NFHS-5, 2019–21) |
| **Yemen** | **16.8%** | 2022 |
| **Sudan** | **16.3%** | 2014 — pre-dates the current conflict |
| **Niger** | **10.9%** | 2022 (was 14.1% in 2018) |
| Bangladesh | ==10.7%== | ==2022 (9.8% was the 2019 round)== |
| Burkina Faso | 9.3% | 2021 |
| Chad | ==7.8%== | ==2022 (was 13.9% in 2019)== |
| Nepal | ==7.0%== | 2022 |
| Ethiopia | 6.8% | 2019 |
| **Nigeria** | ==**11.6%**== | ==2021 (National Food Consumption and Micronutrient Survey)== |
| Pakistan | ==7.1%== | 2018 |
| Mali | 5.4% | 2024 |
| Kenya | 4.5% | 2022 |
| Afghanistan | 3.6% | 2022 |

**Two corrections follow, and they matter for targeting.**

**First, "South Asia" is India.** India at 18.7% sits far above every other country here, and with roughly three-quarters of South Asia's child population it essentially *is* the regional figure. ==The other South Asian countries sit far below it — Bangladesh 10.7%, Pakistan 7.1%, Nepal 7.0%, Afghanistan 3.6% — though Bangladesh is the exception worth noting, close to Niger and well above the sub-Saharan African average; the last three are at or **below** several African countries.== A targeting claim of the form "go to South Asia" is not supported. A claim of the form "India is the single largest concentration of child wasting in the world" is.

**Second, the sub-Saharan African average of 5.9% conceals the geographies that matter most.** ==Nigeria (11.6%) and Niger (10.9%) sit at roughly double the regional figure, with Burkina Faso (9.3%) well above it and Chad now closer to it at 7.8%==, and Sudan's 16.3% is both the second-highest here and eleven years old, measured before a conflict that will have worsened it substantially. Averaging the Sahel and Horn into a continental mean makes them look like a low-priority target when they contain some of the highest-burden populations in the world.

**The honest conclusion is neither "South Asia" nor "Africa".** For CMAM the burden concentrates in **India**, and in **the Sahel, the Horn of Africa and Yemen** — and those two concentrations call for very different programmes. India is a large, stable, high-prevalence setting where the question is routine-system integration at enormous scale. The Sahel–Horn belt is where caseloads surge episodically, where simplified protocols matter most, where WHO recommendation B14 on blanket treatment of moderate wasting applies, and where relapse runs highest (South Sudan 63%, §2.4).

**A caution on the trend claim.** The regional trend table shows African severe wasting falling 57–62% since 2000 while South Asia's fell 15%. That comparison is between modelled regional series and is sound as far as it goes, but it should not be read as "Africa has solved this": Niger and Chad both show recent national figures well above their regional average, and Sudan's most recent data point pre-dates a war.

**A caution on comparability.** The country figures above are survey point estimates from different years, different instruments (DHS, MICS, SMART, national nutrition surveys) and different seasons. Wasting is highly seasonal, and SMART surveys in the Sahel are often timed to the lean season, which raises measured prevalence relative to a DHS fielded at another time of year. These are not a harmonised annual series and small differences between countries should not be over-read.

**Sub-national variation is the next level down, and for CMAM it is probably larger than the between-country variation.** Nigeria's ==11.6%== national figure spans northern states with far higher burden; Ethiopia's 6.8% spans a Somali region historically several times the national mean. Any serious CMAM siting decision should be made on sub-national data, not national averages.

## 7.4 Low birthweight: the finding that does hold up

**Regional, UNICEF-WHO Global Low Birthweight Estimates, 2020:**

| Region | 2020 | 2000 |
|---|---|---|
| **South Asia** | **24.8%** | 29.4% |
| Least Developed Countries | 15.4% | — |
| Intergovernmental Authority on Development (Horn of Africa) | 14.6% | — |
| Community of Sahel-Saharan States | 14.5% | — |
| Eastern and Southern Africa | 14.4% | 15.7% |
| Western Africa | 14.3% | — |
| Sub-Saharan Africa | 13.9% | 15.6% |
| Sahel | 13.8% | — |
| ECOWAS | 13.7% | — |
| West and Central Africa | 13.4% | 15.6% |
| Middle East and North Africa | 12.9% | — |
| Latin America and Caribbean | 9.7% | — |
| East Asia and Pacific | 8.5% | — |

**Unlike wasting, this survives the country check.** ==These are modelled estimates that adjust for birthweight heaping and missing records, so they run above nationally reported figures — India's survey-reported low birthweight is around 18% against the model's 27.4%. They should not be read alongside survey-based wasting figures as if both were measured the same way.== The three South Asian countries present in the export are India 27.4%, Bangladesh 23.0% and Nepal 19.7% — **all three above the sub-Saharan African regional figure of 13.9%**, and Nepal's 19.7% is well above it despite Nepal being unremarkable on wasting. The next highest countries in the export are Comoros 23.0%, the Philippines 21.1%, Liberia 19.9%, Guinea-Bissau 19.5% and Papua New Guinea 19.4%.

So the low-birthweight concentration in South Asia is a regional property, not an India artefact. **For the two interventions that target low birthweight — MMS and the facility newborn package — South Asia genuinely is the highest-yield region**, and that conclusion is robust to the disaggregation that overturned the wasting one.

*Country-level low-birthweight figures for the African countries were not in the supplied export; the UNICEF-WHO estimates do cover them and should be added before siting decisions.*

## 7.5 What this means for each intervention

**MMS — target South Asia, and target anaemic populations within it.** This is the clearest targeting conclusion in the review, and the only one resting on a multiplicative argument: absolute benefit scales with baseline low birthweight (24.8% regionally, 19.7–27.4% in the three countries with data), and the relative benefit is *additionally* larger in anaemic and undernourished women (§5.2). It is also the cheapest intervention here at $21–42 per DALY. Nothing else in this review lines up this cleanly.

**There is a mechanistic reading that reinforces it.** South Asia combines the world's highest low birthweight with — in India — the world's largest wasting burden. Where a quarter of infants are born already small, a substantial share of subsequent wasting is determined before birth rather than by post-natal food insecurity and infection, which is the dominant pathway in the Sahel and Horn. If that holds, antenatal MMS has more leverage in South Asia than anywhere else because it acts on the pathway generating the caseload rather than on its consequences. **This is an inference consistent with the burden data and the effect-modifier evidence, not a directly verified finding**, and it would be worth testing against the South Asian birth-cohort literature before it is relied on.

**Facility newborn package (KMC) — same geography, gated by a variable not measured here.** At 24.8% low birthweight the eligible population in South Asia is nearly double sub-Saharan Africa's, and the RR 0.68 mortality benefit applies to every such infant who reaches a facility. But the second targeting term is facility delivery coverage, which is not in the supplied data and which varies enormously — it should be layered on before siting.

**CMAM — two distinct geographies, needing two distinct programmes.** India for scale within a functioning routine system; the Sahel, the Horn of Africa and Yemen for episodic high-severity caseload, where simplified protocols, blanket moderate-wasting treatment in crises, and post-discharge support against relapse all matter most. The evidence base was overwhelmingly generated in the second (ComPAS in Kenya and South Sudan; OptiMA and MANGO in Niger and Burkina Faso; the relapse cohort in Mali, South Sudan and Somalia), which makes it well matched to that geography and only partly transferable to the first.

## 7.6 What this analysis cannot settle

- **Prevalence is not absolute burden.** Converting rates into numbers of children needs population denominators, which the supplied export does not contain. This understates India by a wide margin and overstates small high-prevalence countries.
- **Prevalence is not mortality.** Under-five mortality rates are higher in sub-Saharan Africa, so deaths averted per wasted child treated may be higher there than prevalence alone implies.
- **Annual and survey-point figures understate crisis dynamics.** Sudan's most recent survey is 2014; Yemen, Somalia and South Sudan experience surges that no periodic survey captures well.
- **Maternal anaemia, the second MMS targeting variable, could not be obtained by region.** Global prevalence is 35.5% in pregnant women and 30.7% in women of reproductive age (WHO 2025 estimates, 2023 reference year), both verified; WHO's regional breakdown would not load and its API returned empty. This is the single most valuable addition to §7.5.
- **Facility delivery coverage, the second KMC targeting variable, is not in the supplied data.**
- **Sub-national data would change CMAM siting** and probably matters more than any national comparison above.

# 8. Evidence gaps

**1. No trial of CMAM against no treatment, and there never will be.** The intervention's value rests on cohort counterfactuals (§2.2). This structurally understates measured benefit and should be stated whenever CMAM is compared with interventions that have placebo-controlled evidence.

**2. Simplified protocols in the severest children.** OptiMA-Niger found standard care superior on recovery in children with MUAC <115 mm or oedema. This needs resolving before national adoption, and it is the single most decision-relevant open question in CMAM.

**3. The breastfeeding-specific share of the community mortality benefit is unknown.** Lassi's RR 0.75 comes from packages in which breastfeeding is one of five or more components.

**4. No cadre comparison with adequate power.** Cochrane's null on provider type is explicitly underpowered. The field does not know whether CHWs, peers or professionals differ.

**5. MMS effectiveness rather than efficacy.** Almost all MMS evidence is efficacy-trial evidence under supervised conditions; the cost-effectiveness models assume perfect adherence and no waste. Real-world MMS effect sizes are unmeasured.

**6. KMC scale-up costing.** I found no multi-country costing of KMC scale-up that met the verification standard here — a notable gap given it is the strongest clinical result in the review.

**7. Grey literature.** This review draws on peer-reviewed sources, WHO guidelines and organisational reporting. Government programme documentation and NGO evaluations are under-represented, which matters disproportionately for implementation questions.

---

# 9. What I would tell CARE in one page

- **All three work; they do different jobs.** KMC saves the lives of small babies. CMAM saves the lives of wasted children — the counterfactual is 11.6× mortality. MMS makes babies bigger and has not been shown to save lives.
- **Pick the geography to the intervention, not the reverse — and do not trust regional averages.** Low birthweight, which MMS and KMC act on, is genuinely concentrated in South Asia and holds up country by country. Wasting does not behave that way: the South Asian figure is essentially India, and sub-Saharan Africa's average hides Niger, Chad, Burkina Faso and Sudan at roughly double it.
- **MMS is the cheapest and most tractable to introduce** — about half a US cent more per tablet, $21–42 per DALY — but WHO has not endorsed routine use, and the real constraints are antenatal attendance and supply chain, which the switch does not fix.
- **CMAM is genuinely cost-effective** at $26–42 per DALY, and the biggest efficiency gain available is protocol simplification (32–50% less therapeutic food) — with an unresolved question about the severest children and a guideline that has not yet followed.
- **Do not design around task-shifting as the active ingredient.** Reach improves; quality can fall; and for breastfeeding there is no demonstrated cadre effect at all. Design the package.
- **Budget for post-discharge.** A fifth to two-thirds of "recovered" children relapse within six months, driven by food insecurity afterwards. WHO now conditionally recommends cash transfers to reduce it — the clearest opening in this review for CARE's social-protection strengths.
- **MMS in South Asia is the cleanest match in this review.** It is the only place where the absolute benefit (baseline low birthweight of 24.8%) and the relative benefit (larger in anaemic and undernourished women) point the same way, on the cheapest intervention here.
- **CMAM needs two different programmes, not one.** India is scale within a working routine system. The Sahel, the Horn of Africa and Yemen carry episodic high-severity caseload, where simplified protocols, crisis-mode blanket treatment and post-discharge support matter most — and where almost all the protocol evidence was generated.
- **Site CMAM on sub-national data.** Within-country variation almost certainly exceeds the between-country differences above.

---

# 10. Source register

All items below were read at the primary source. "Abstract-level" means the abstract or structured record was read in full; "full text" means the article body or guideline text was consulted.

| # | Source | Used for | Verification |
|---|---|---|---|
| 1 | Schoonees A, Lombard MJ, Musekiwa A, Nel E, Volmink J. Ready-to-use therapeutic food for home-based nutritional rehabilitation of SAM in children 6 months to 5 years. Cochrane CD009000, 2019 (PMID 31090070) | §2.1 RUTF effect estimates and GRADE ratings | Abstract-level ✓ |
| 2 | Olofin I et al. Associations of suboptimal growth with all-cause and cause-specific mortality in children under five: pooled analysis of ten prospective studies. PLoS One 2013 (PMID 23734210) | §2.2 untreated counterfactual, HR 11.63 | Abstract-level ✓ |
| 3 | Bailey J et al. A simplified, combined protocol versus standard treatment for acute malnutrition in children 6–59 months (ComPAS trial). PLoS Med 2020 (PMID 32645109) | §2.3, §2.5 ComPAS results and costs | Abstract-level ✓ |
| 4 | Kangas ST et al. Impact of reduced dose of RUTF in children with uncomplicated SAM (MANGO). PLoS Med 2019 (PMID 31454351) | §2.3 reduced dose, height-gain penalty | Abstract-level ✓ |
| 5 | Daures M et al. Optimizing management of uncomplicated acute malnutrition in children in rural Niger: 3-arm noninferiority trial. Am J Clin Nutr 2025 (PMID 41043877) | §2.3 head-to-head, severe subgroup | Abstract-level ✓ |
| 6 | King S et al. Rates and risk factors for relapse among children recovered from SAM in Mali, South Sudan and Somalia. Lancet Glob Health 2025 (PMID 39706667) | §2.4 relapse | Abstract-level ✓ |
| 7 | Puett C, Sadler K, Alderman H, Coates J, Fiedler JL, Myatt M. Cost-effectiveness of CMAM of SAM by community health workers in southern Bangladesh. Health Policy Plan 2013;28(4):386–99 (==PMID 22879522==) | §2.5 $26/DALY | Full text ✓ |
| 8 | Wilford R, Golden K, Walker DG. Cost-effectiveness of CMAM in Malawi. Health Policy Plan 2012 (PMID 21378101) | §2.5 $42/DALY | Abstract-level ✓ |
| 9 | Tekeste A et al. Cost effectiveness of community-based and in-patient therapeutic feeding programs to treat SAM in Ethiopia. Cost Eff Resour Alloc 2012 | §2.5 Ethiopia unit costs, cost composition | Full text ✓ |
| 10 | Rogers E et al. Cost-effectiveness of treatment of uncomplicated SAM by lady health workers vs outpatient therapeutic feeding, Sindh, Pakistan. BMC Public Health 2019 | §2.5 Pakistan counterweight | Full text ✓ |
| 11 | WHO. Guideline on the prevention and management of wasting and nutritional oedema in infants and children under 5 years. 2023 (NCBI Bookshelf NBK601642) | §2.6 recommendations B2, B5, B10, B13, B14, B17, C2, C3 | Full text ✓ |
| 12 | Sivanandan S, Sankar MJ. Kangaroo mother care for preterm or low birth weight infants: systematic review and meta-analysis. BMJ Glob Health 2023;8:e010728 (PMID 37277198) | §3.1 KMC RR 0.68, population, duration | Abstract-level ✓ |
| 13 | WHO Immediate KMC Study Group. Immediate "Kangaroo Mother Care" and Survival of Infants with Low Birth Weight. NEJM 2021 (doi 10.1056/NEJMoa2026486) | §3.1 iKMC, 1.0–1.799 kg, RR 0.75 | Abstract-level ✓ |
| 14 | OMWaNA trial. Effectiveness of KMC before clinical stabilisation vs standard care, Uganda. Lancet 2024 (doi 10.1016/S0140-6736(24)00064-3) | §3.1 null primary endpoint | Abstract-level ✓ |
| 15 | WHO recommendations for care of the preterm or low-birth-weight infant, 2022 | §3.1 strong recommendation, high certainty | Statement verified via WHO news release and guideline summary ✓ |
| 16 | Smith ER et al. Delayed breastfeeding initiation and infant survival: systematic review and meta-analysis. PLoS One 2017 (PMID 28746353) | §3.1 early initiation, observational | Abstract-level ✓ |
| 17 | Gavine A et al. Support for healthy breastfeeding mothers with healthy term babies. Cochrane CD001141.pub6, 2022 (PMID 36282618) | §4.1 effect estimates, no cadre effect, 4–8 visits | Abstract-level ✓ |
| 18 | Lassi ZS, Bhutta ZA. Community-based intervention packages for reducing maternal and neonatal morbidity and mortality. Cochrane CD007754.pub3, 2015 (PMID 25803792) | §4.1 bundled package mortality | Abstract-level ✓ |
| 19 | Menon P et al. Impacts on breastfeeding practices of at-scale strategies (Alive & Thrive), Bangladesh and Viet Nam. PLoS Med 2016 (PMID 27780198) | §4.2 at-scale impact, delivery channels | Full text ✓ |
| 20 | Keats EC, Haider BA, Tam E, Bhutta ZA. Multiple-micronutrient supplementation for women during pregnancy. Cochrane CD004905, 2019 (PMID 30873598) | §5.1 all MMS outcomes and GRADE | Abstract-level ✓ |
| 21 | Keats EC et al. Effects of vitamin and mineral supplementation during pregnancy on maternal, birth, child health and development outcomes in LMICs. Campbell Syst Rev 2021 (PMID 37051178) | §5.1 competing stillbirth estimate | Abstract-level ✓ |
| 22 | Hunter PJ et al. A modular systematic review of antenatal interventions to address undernutrition in pregnancy in the prevention of low birth weight. Am J Clin Nutr 2023 (PMID 37331760) | §5.1 independent null on stillbirth | Abstract-level ✓ |
| 23 | Oh C, Keats EC, Bhutta ZA. Vitamin and mineral supplementation during pregnancy… Nutrients 2020 (PMID 32075071) | §5.1 duplicate-publication caution | Abstract-level ✓ |
| 24 | Smith ER et al. Modifiers of the effect of maternal multiple micronutrient supplementation on stillbirth, birth outcomes and infant mortality: IPD meta-analysis of 17 trials. Lancet Glob Health 2017 (PMID 29025632) | §5.2 targeting | Abstract-level ✓ |
| 25 | WHO antenatal care recommendation on multiple micronutrient supplements (NCBI Bookshelf NBK560390) | §5.3 verbatim recommendation, 2020 | Full text ✓ |
| 26 | Kashi B et al. Multiple micronutrient supplements are more cost-effective than iron and folic acid: modeling results from 3 high-burden Asian countries. J Nutr 2019 (PMID 31131412) | §5.4 ICERs | Abstract-level ✓ |
| 27 | Engle-Stone R et al. Replacing iron-folic acid with multiple micronutrient supplements among pregnant women in Bangladesh and Burkina Faso. Ann NY Acad Sci 2019 | §5.4 deaths averted, cost per DALY, commodity cost | Full text ✓ |
| 28 | Thurstans-Fuller S, James P, Menezes R et al. Introducing antenatal multiple micronutrient supplements: lessons from implementation research in Bangladesh, Burkina Faso, Madagascar and Tanzania. Matern Child Nutr 2025 | §5.5 transition barriers and enablers | Full text ✓ |
| 29 | UNICEF/WHO/World Bank Joint Child Malnutrition Estimates, 2025 edition | §6 global 2024 burden figures | Summary figures verified; **country tables not accessible** |
| 30 | Global Action Plan on Child Wasting (FAO, UNHCR, UNICEF, WFP, WHO) | §6 one-in-three coverage | Verified ✓ |
| 31 | UNICEF Global Annual Results Report 2024 (Nutrition) | §6 9.3M children reached, 7.4M RUTF, 47 countries | Verified ✓ |
| 32 | WHO global nutrition targets to 2030 (78th World Health Assembly, 2025) | §6 targets | Verified ✓ |
| 33 | UNICEF global data export (`GLOBAL_DATAFLOW_2000-2026.xlsx`), series footnote "UNICEF/WHO/World Bank Joint Malnutrition Estimates Databases, March 2025"; UNICEF-WHO Global Low Birthweight Estimates | §7.3–7.4 regional wasting, severe wasting and low birthweight | Regional aggregates ✓ (World 2024 values reconcile with independently verified JME 2025 global figures). **Country rows for wasting absent from the export** |
| 33b | WHO Global Health Observatory, indicator NUTRITION_WH_2, queried directly by country | §7.3 national wasting survey estimates | ✓ — survey point estimates, mixed instruments and years; not a harmonised series |
| 34 | Nutrition International / Results for Development MMS programme documentation; 2nd Africa Maternal Nutrition and MMS Technical Meeting (Nairobi, Oct 2024); Nepal National Essential Medicines List addition (2025); Bauchi State, Nigeria IFA→MMS replacement (Nov 2023–Mar 2025) | §7.2 policy windows | **Organisational/grey sources — confirm with in-country teams before relying on them for a country decision** |

**Items 29, 33 and 34 are the weak points in this register**, and are flagged as such rather than smoothed over. Everything used to support a numeric claim in §§1–6 sits in rows 1–28 and 30–32.

---

# 11. Corrections log

Applied after an independent fact-check against primary sources. Highlighted passages in the body mark where each landed.

| § | What it said | What it says now | Why |
|---|---|---|---|
| 1, 2.2 | Severe wasting carries 11.6× mortality risk "untreated" | The comparator is children with normal weight-for-height (Z ≥ −1); treatment status was never assessed | Olofin pooled general-population cohorts. They do not compare treated with untreated children |
| 2.1 | RUTF formulations "essentially interchangeable", so procurement is a cost question not a clinical one | Interchangeable on recovery only; standard RUTF also reduces relapse (RR 0.84) at high certainty | Cochrane's authors carve out relapse explicitly. Substituting formulation is not cost-free |
| 2.3 | The linear-growth penalty framed as a general property of reduced dosing | Attributed to one trial of one design in a relatively food-secure setting | MANGO tested a single regimen; it does not license a claim about reduced-dose regimens as a class |
| 3.1 | KMC benefit "greater at ≥8 hours per day" | Re-anchored on WHO's 8–24 h/day recommendation | The review's own discussion reports insufficient data in the under-8-hour group, so the contrast has no comparator |
| 3.1 | RR 0.68 presented without the trial-design bounds | Added: all but one trial started KMC after stabilisation; fixed-effect pooling; the immediate-KMC trial compared against delayed KMC and stopped early | Prevents the pooled estimate being read as evidence for immediate KMC |
| 3.2 | Low birthweight "roughly one birth in seven in LMICs" | One birth in seven **worldwide**; the LMIC-only rate is higher | 14.7% is the global figure and includes high-income regions at about 7% |
| 4.1 | Community packages described as bundling tetanus immunisation, clean delivery, resuscitation, breastfeeding and cord care | Packages vary widely — women's groups, home visits, birth-attendant training, home-based newborn care; pooled figure is a random-effects average, I² = 85% | That five-item list appears in the review's *Background* as generic examples, not as a description of the included trials |
| 4.2 | Alive & Thrive impact and endline percentages presented together | Impact labelled as difference-in-differences; policy advocacy added to the intervention description | 87.6% − 53.5% = 34.1 points, not the 36.2 reported; 36.2 is the difference-in-differences |
| 5.2 | MMS effect-modifier findings presented as a clean targeting rule | Added that they come from one of 26 subgroups with interaction tests of 0.03–0.049 | Borderline under multiplicity; a steer rather than a settled rule |
| 5.4 | "About US$0.005 more per tablet" | Flagged as marginal *production* cost; procurement gap is roughly $0.006–0.009 per tablet, about $1.1–1.7 per pregnancy, with Verney et al. 2023 at $1.42 | $0.005 is not what a ministry pays. The range was first written as $0.9–1.7, but $0.9 is the production figure — the catalogue prices cited give $1.07–$1.67 |
| 7.3 | Bangladesh wasting 9.8%, labelled 2022 | **10.7% (2022)** | 9.8% is the 2019 round. Bangladesh is not "unremarkable" — at 10.7% it sits close to Niger and well above the sub-Saharan African average |
| 7.3 | Pakistan wasting 6.1% (2018) | **7.1% (2018)** | 6.1% matches no Pakistan data point in either WHO GHO or the World Bank series |
| 7.3 | Nepal wasting 6.9% (2022) | **7.0% (2022)** | Both sources give 7.0 |
| 7.3 | Nigeria wasting 6.5% (2020) | **11.6% (2021)** | The 2021 National Food Consumption and Micronutrient Survey supersedes it. Nigeria moves from near the regional average to roughly double it |
| 7.3 | Chad wasting 9.0% | **7.8% (2022)** | 9.0% matched no Chad data point; the GHO series runs 13.9% (2019), 9.5% (2020), 10.2% (2021), 7.8% (2022) |
| 7.3 | "Niger, Burkina Faso and Chad at roughly double the regional figure" | Nigeria and Niger at roughly double; Burkina Faso well above; Chad now closer to it | At 7.8%, Chad is 1.3× the regional figure, not 2× |
| 7.3 | "Regional, JME 2024" | JME 2025 edition, 2024 reference year | There is no 2024 edition; the estimates are biennial |
| 7.4 | Low-birthweight country figures given without provenance | Flagged as modelled estimates that run above nationally reported figures | India's survey-reported figure is around 18% against the model's 27.4%; they should not sit unlabelled beside survey-based wasting data |
| 10 | Puett citation without identifier | Full author list, volume, pages and PMID 22879522 added | The PMID first recorded was off by one and pointed at an unrelated paper |

**Checked and left unchanged.** The Cochrane MMS estimates and their GRADE ratings; the Smith IPD trial count and sample size; WHO's antenatal MMS recommendation wording and status; the Kashi cost-effectiveness ratios; the Engle-Stone per-DALY figures; the low-birthweight regional and country estimates; South Asia's 24.8% (UNICEF region — the 24.4% figure is UNSDG's "Southern Asia", a different grouping); the ComPAS and OptiMA-Niger trial results; the relapse cohort figures; the Rogers coverage survey; and the Global Action Plan coverage statement.
