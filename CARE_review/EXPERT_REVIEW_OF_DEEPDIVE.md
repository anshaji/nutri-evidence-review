# Expert review — CARE/IA deep-dive report and summary

Reviewer brief: read as a malnutrition-intervention specialist, fact-check heavily, assess
what significant literature is missing. Every claim below was checked against the cited
source. Statements about what a paper says are quoted or paraphrased from that paper.

---

## 1. Verdict

**The full report is good work.** Several of its structural choices are ones I would
defend against a sceptical technical reviewer: refusing to grade three interventions
measured on different outcomes against different comparators; separating case-finding
from conversion-to-treatment as two distinct coverage failures; naming the active-control
ceiling on CMAM instead of quietly benefiting from it; catching a twin publication of one
42-study evidence base; stating that recovery-at-discharge overstates durable effect
because relapse is high. The implementation axis is real rather than decorative. The body
text is appropriately hedged.

**The summary is where it goes wrong, and it goes wrong in one consistent way.**
Correct numbers, drawn from the right papers, are re-attached to broader populations,
interventions, or claims than the source supports. I found:

- **1 pair of numbers I could not locate in the cited source at all** (West Africa breastfeeding);
- **1 population error that overstates the eligible population roughly sevenfold** (KMC);
- **1 intervention descriptor that does not appear in the source** ("continuous" KMC);
- **1 policy target that is both the wrong number and the wrong indicator** (70% EBF);
- **1 causal claim the source does not make** (Ethiopia recovery "fell as the programme matured");
- **1 circular counterfactual** (~11% case fatality used to justify treatment's mortality benefit);
- **1 claim of independent replication that is a duplicated analysis** (MMS stillbirth).

**Every one of these passed the automated verifier.** That is the most important finding
here, and it is a finding about the method, not just this report.

The report's own §8.3 says verification establishes "that a cited number appears in the
record cited." The West Africa case shows that even this is not established. What the
verifier actually establishes is that a number is *traceable to a record in the corpus* —
not that the record contains it in that form, and not that the population, comparator or
certainty attached to it survived the trip into prose. The four most consequential errors
in this report are all of the latter kind. If the methods paper claims verification as its
distinctive contribution, this gap is the thing to characterise honestly, because a
reviewer will find it.

**Bottom line for the partner deliverable:** do not send the summary as it stands. The KMC
population error alone would be caught by any CARE newborn-health advisor within a minute,
and it sits under the heading "the strongest single result in the review."

---

## 2. Tier 1 — fix before this goes to CARE

### 2.1 Kangaroo Mother Care is a preterm/low-birth-weight intervention, not a newborn intervention

Source: Sivanandan S, Sankar MJ. **"Kangaroo mother care for preterm or low birth weight
infants: a systematic review and meta-analysis."** *BMJ Glob Health* 2023;8:e010728
(PMID 37277198). Eligibility, verbatim: *"All randomised trials comparing KMC vs
conventional care or early vs late initiation of KMC in low birth weight or preterm
infants were included."*

The report says *"continuous skin-to-skin holding of **the newborn** cuts neonatal mortality
by 32%,"* and the glossary defines KMC as applying to "the newborn." The strings "low birth
weight" and "birthweight" never appear anywhere in the report in connection with KMC.

This matters programmatically, not pedantically. Low birth weight is roughly 14–15% of
births in LMICs. Presenting RR 0.68 as a general newborn effect overstates the eligible
population by about sevenfold, and it converts a **facility-based small-and-sick-newborn
care intervention** — which needs beds, staff, warmth, feeding support and maternal
presence — into something that sounds like a universal behavioural practice. That directly
inflates Option A's apparent reach. The claim "requires no commodity and no equipment"
compounds it: KMC at scale requires facility capacity, which the report elsewhere correctly
names as Option A's binding constraint.

**Four further defects in the same claim:**

| Element | Report | Source |
|---|---|---|
| Intervention | "continuous" skin-to-skin | Review's subgroup was **≥8 h/day vs <8 h/day**. "Intermittent" appears zero times in the full text. The paper's own recommendation is *"initiated within 24 hours of birth and provided for at least 8 hours daily."* |
| CI | 0.53–0.87 | **0.53–0.86** |
| Trials | 12 | Abstract says 11 (the paper is internally inconsistent between abstract and results) |
| Outcome label | "neonatal mortality" | *"mortality during birth hospitalisation or by 28 days after birth or 40 weeks of postmenstrual age"* |

**And one that should worry you specifically.** The pooled estimate is fixed-effect
(I²=0%), and the paper's text notes one trial (Mazumder) carrying **65.4% of the weight**.
That is structurally the DEVTA problem the pipeline was built to detect — a single trial
holding the pooled estimate, unnamed in the synthesis. It went undetected here.
*(I was unable to re-open the full text to confirm the weight figure directly because of a
tool outage; confirm against the forest plot before quoting it.)*

**Suggested rewrite:** "Among preterm or low-birth-weight infants, kangaroo mother care of
at least 8 hours a day reduces mortality to 28 days by 32% (RR 0.68, 0.53–0.86; 10,505
infants; high certainty). This is a small-and-sick-newborn care intervention, not a
universal newborn practice; the eligible population is roughly the 14–15% of births that
are low birth weight."

### 2.2 The largest African KMC trial found no mortality effect, and it is not in the corpus

**OMWaNA** — *"Effectiveness of kangaroo mother care before clinical stabilisation versus
standard care among neonates at five hospitals in Uganda: a parallel-group, individually
randomised controlled trial and economic evaluation."* *Lancet* 2024
(doi:10.1016/S0140-6736(24)00064-3). 2,221 neonates. **KMC initiated before stabilisation
had no effect on the primary outcome, early neonatal mortality (<7 days)**, with a
non-significant 12% relative reduction at 28 days. Secondary outcomes (hypothermia at 24 h,
weight gain) improved, and it was cost-effective. The authors' own pooled analysis with
prior trials gives a 19% relative reduction in 28-day mortality overall, 14% across
sub-Saharan African sites.

The report anchors KMC on the WHO immediate-KMC trial (NEJM 2021), which it does cite. It
does not cite the trial that tried to replicate that result in an African hospital setting
and did not reproduce it on the primary endpoint. For a report recommending Option A in
African contexts, that is the single most relevant qualifier available, and its absence
makes the evidence look more settled than it is.

### 2.3 The West Africa breastfeeding percentages are not in the cited paper

Source: Lewis-Koku MO et al., *Matern Child Nutr* 2025 (PMID 39764605). The review reports
**no combined West Africa estimate**. It reports a language-bloc split:

| | Report states | Anglophone | Francophone |
|---|---|---|---|
| Exclusive breastfeeding | 36.5% | **41.2% (36.9–45.5)** | **30.1% (26.7–33.5)** |
| Early initiation | 48.7% | **51.7% (48.8–54.6)** | **45.5% (42.0–48.9)** |

The report's figures are close to the *unweighted arithmetic means* of the two blocs
(35.65% and 48.6%) — an estimate the authors did not compute and which ignores population
weighting. This is the clearest instance of a number being derived rather than read, and
it is the one that most directly contradicts what the verifier is claimed to establish.

### 2.4 The 70% breastfeeding target is the wrong number and the wrong indicator

- The WHA global nutrition target for **exclusive breastfeeding** was ≥50% by 2025,
  extended by the 78th World Health Assembly (2025) to **≥60% by 2030**.
- **70% by 2030 is the Global Breastfeeding Collective target for *early initiation*** —
  breastfeeding within the first hour — not for exclusive breastfeeding.

So "below the 70% global target" is wrong twice over. It also changes the story: Anglophone
West Africa at 41.2% EBF against a 60% target is a materially different gap from what the
summary implies, while both blocs genuinely do fall short of the 70% early-initiation target.

### 2.5 Ethiopia's recovery did not "fall as the programme matured"

Source: Bitew et al., *BMC Pediatrics* 2020 (PMID 32631260) — a **meta-analysis of 19
studies (23,395 children)**, not a programme time series. Pooled recovery 70% (64–76).

The 72% and 69% are real, but they are a **subgroup split by publication year of the
included studies**: pre-2015 = 72% (62–82), 6 studies; post-2015 = 69% (62–76), 13 studies.
The confidence intervals overlap almost completely. There is no demonstrable decline, and
publication year of heterogeneous studies across different regions and service levels is
not a measure of programme maturity.

This is presented in the summary as one of three headline quantifications of the
operationalization gap, and as the marquee cautionary finding about Ethiopia — the country
the report otherwise leans toward. It cannot carry that weight. Either drop it or restate
it as "subgroup estimates by publication year were 72% and 69%, with overlapping intervals."

**Related:** *"the only country running it at national scale"* appears nowhere in that
paper, and is not true as a general claim. Malawi and Niger integrated CMAM into government
systems in the same post-emergency generation (documented in the FANTA-2 review of CMAM
integration, which covers Ethiopia, Malawi and Niger together). The full report is careful
— it says "the only country in the corpus" and sources the narrower CHW-managed-treatment
claim to a specific review — but the summary drops the qualifier and states it flatly.
Ethiopia's real and more useful distinction is that it **issued a national guideline on
simplified and combined approaches to acute malnutrition treatment (FMOH, 2023)** — it has
already made the policy move the report is contemplating. That is a far stronger basis for
selecting it, and it survives partner review.

### 2.6 The ~11% case fatality is the treated rate, used as the untreated counterfactual

Source: *Systematic Reviews* 2025 (PMID 39885605), "Prevalence and risk factors of
under-five mortality due to severe acute malnutrition in Africa," pooling 52 of 82 studies
published 2014–2024. The included populations are overwhelmingly children **admitted to**
inpatient nutrition wards, stabilisation centres and therapeutic feeding centres, many
specifying complicated SAM.

The summary uses this to justify Option B's mortality benefit: *"treats a condition with
~11% case fatality."* That inverts the logic. 11% is mortality **with** treatment, skewed
toward the most severe inpatient cases. The benefit of treatment is (untreated CFR −
treated CFR); the report supplies only the second term and presents it as the first.

**Use these instead:**

- **Olofin I et al., *PLoS One* 2013;8:e64636** (PMID 23734210) — pooled analysis of ten
  prospective cohorts, 53,809 children. Severe wasting (WHZ < −3): all-cause mortality
  **HR 11.63 (9.84–13.76)**. This is the canonical relative-risk anchor and populates the
  Lives Saved Tool that a ministry's own modellers will use.
- **Schwinger C et al., *PLoS One* 2019** (doi:10.1371/journal.pone.0219745) — community
  cohorts from DRC, Senegal and Nepal; MUAC <115 mm = 5.08 deaths/10,000 children/day
  (≈18%/year), both criteria = 9.60 (≈30%/year), against a reference of 1.31. The cleanest
  untreated counterfactual available.
- Avoid the widely circulated "30–50% of untreated SAM dies." It derives from pre-CMAM
  hospital case series, not from these cohorts, and is frequently mis-attributed.

The honest counterfactual is roughly 2–4× the 11% figure.

### 2.7 MMS and stillbirth: "four of five independent syntheses" is not accurate

This is the report's most significant scientific problem, and it is worth setting out fully
because §7.4 is otherwise one of the best-argued sections in the document.

The report presents stillbirth RR 0.91 as replicated across four of five large syntheses,
against a single dissenter. What the sources actually show:

| Source | Stillbirth | Independent? |
|---|---|---|
| Oh, Keats, Bhutta — *Nutrients* 2020 (PMID 32075071) | 0.91 (0.86–0.98) | Bhutta group |
| Keats, Oh, … Bhutta — *Campbell Syst Rev* 2021 (PMID 37051178) | 0.91 (0.86–0.98), 22 studies, N=96,772 | Bhutta group — same overlapping analysis |
| **Keats, Haider, Tam, Bhutta — Cochrane CD004905, 2019 (PMID 30873598)** | **0.95 (0.86–1.04), HIGH certainty** | flagship; **absent from the corpus** |
| Hunter et al. — *Am J Clin Nutr* 2023 (PMID 37331760) | 0.95 (0.86–1.04) | independent (Tampere/UCL) |
| WHO GDG evidence table | 0.98 (0.87–1.10) | independent |

Three problems follow:

1. **The 0.91 is one analysis published twice, not two replications.** This is exactly the
   twin-publication pattern the report itself catches in §5.3 for CMAM — *the same journal
   pair, Campbell and Nutrients*. It was caught in Chapter 5 and missed in Chapter 7.
2. **The stillbirth and perinatal-mortality numbers come from the same paper.** *Nutrients*
   2020 reports stillbirth 0.91 and perinatal mortality 1.00 side by side. The report splits
   them across two citations, so they read as two independent sources corroborating a
   nuanced story. They are one internally consistent analysis.
3. **"A well-powered null" inverts the precision ordering.** Perinatal mortality rests on
   ~64,000 participants; stillbirth on ~97,000. The stillbirth analysis has more data, not
   less. And the arithmetic incoherence the report notices but does not resolve is real:
   perinatal mortality = stillbirth + early neonatal death, and neonatal mortality is also
   flatly null (1.00, 0.89–1.12, high certainty). A genuine 9% stillbirth reduction should
   move perinatal mortality. It does not.

**Defensible reframing:** MMS versus IFA shows consistent benefit on **fetal growth and
size** — low birthweight and small-for-gestational-age — across every synthesis. Effects on
**mortality** (stillbirth, perinatal, neonatal, maternal) are null or unstable, with
stillbirth reaching significance only in the LMIC-restricted Bhutta-group analysis.

### 2.8 "The only finding here carrying a formal high-certainty rating" is false

Cochrane CD004905 assigns **high certainty** to four MMS outcomes: low birthweight
0.88 (0.85–0.91), stillbirth 0.95 (0.86–1.04), perinatal mortality 1.00 (0.90–1.11),
neonatal mortality 1.00 (0.89–1.12). MMS therefore has a **high-certainty benefit on low
birthweight**.

The correct statement is narrower: *KMC is the only high-certainty **mortality** benefit in
the review.* As written, the claim is wrong, and it is load-bearing — it is the stated
reason Option A outranks Option C in the summary's closing observations. Note that the
statement is only "true within the corpus" because the flagship Cochrane review is missing
from the corpus, which is not a defence.

---

## 3. Tier 2 — misframings that change the reading

| # | Claim | What the source shows |
|---|---|---|
| 1 | "MMS birth outcomes settled (RR 0.73–0.85)" | 0.73 (0.64–0.84) is **preterm SGA with low birthweight** — one of six small-vulnerable-newborn phenotypes, the rarest and most severe (Wang et al., *Lancet Glob Health* 2025, PMID 39890230, 14 trials, n=42,618). That paper reports **no overall LBW estimate**, so it cannot support "RR 0.85" either. Presenting 0.73–0.85 as a range implies a consistent effect band; it splices the most extreme subtype from one IPD meta-analysis onto a pooled estimate from a different review. "Settled" also overstates: preterm birth is null in Cochrane (0.95, 0.90–1.01). |
| 2 | "Support works via professionals or peers" and "CHW counselling at 4–8 postnatal contacts" | Gavine et al., Cochrane CD001141.pub6 (PMID 36282618) — correctly cited. But the review found *"no differential effects regarding person providing support or mode of delivery"*, and concludes support *"may be offered either by professional or lay/peer supporters, or a combination of both."* The 4–8 visit finding is real but hedged — *"It is possible that…"* — from a meta-regression where *"heterogeneity remains largely unexplained."* Nothing in it compares facility-initiated versus community-only sequencing, so "the best-evidenced configuration" overstates it. |
| 3 | Home visits: CHW RR 0.69, professionals "showed no benefit" RR 1.26 | Tiruneh et al. 2019 (PMID 31852432). Both numbers exact. But RR 1.26 has CI **0.37–4.30** from only 3 studies — that is no evidence either way, not evidence of no benefit. More importantly, the same table shows the effect tracks the **package, not the cadre**: home visits with community mobilisation RR 0.69 (0.54–0.88) versus **home visits alone RR 0.97 (0.90–1.05)**. It is also confounded by publication era (pre-2008 0.58 vs post-2008 0.94, p<0.01). |
| 4 | CMAM "recovers about 71% of children treated" | Desyibelew et al. 2020 (PMID 32187182): 71.2% (68.5–73.8), I²=98.9%, 54 studies, n=140,148 — **sub-Saharan Africa only, and 35 of 53 studies are inpatient care**. The full report handles this correctly (inpatient 70.4%, outpatient 71.1%); the summary presents it as community-programme performance. |
| 5 | Cash transfers "cut relapse sharply (HR 0.21)" | Grellety et al., *BMC Medicine* 2017 (PMID 28441944), **DRC**, cluster-RCT, US$40/month × 6 months. HR 0.21 (0.11–0.41) is relapse to **moderate** acute malnutrition. Relapse to **SAM** was HR 0.30 (0.16–0.58). Recovery HR 1.35 (1.10–1.69) confirmed. Name the country — it is a single-country trial. |
| 6 | Nepal women's groups + cash raised consumption "2.5–4.6 fold" | Harris-Fry et al., *J Nutr* 2018 (PMID 30053188), 4-arm cluster-RCT. It is **odds** of consuming supplements, not consumption levels; it is **iron-folate**, not MMS; and the range spans **all three intervention arms**, so it cannot be attributed to "women's groups plus cash." Cash's distinctive result was dietary diversity (+0.4 food groups). |
| 7 | Adherence "41–46% of women took them as recommended" | Both sources are **iron-folic acid**, not MMS (Sendeku 2020, PMID 32131751, 41.4%, adherence = ≥4 tablets/week in the prior month; Desta 2019, PMID 31864397, 46.2%, adherence = ≥90 days or 4 days/week). The two definitions differ, so 41–46% is not a like-for-like band. The full report says IFA correctly; the summary says "antenatal supplements" and files it under MMS. |
| 8 | "77–82% in parts of north India" | One facility: Ballabgarh sub-district hospital, Haryana, n=484 ANC attendees, 77.1% compliant (≥80% of tablets); **82.1% is the lower-SES subgroup of that same study**. Facility ANC attendees with a laxer definition, against Ethiopian population meta-analyses — not a valid contrast, and "parts" (plural) is not supported. |
| 9 | Mali screening: "treatment coverage stayed at 7.6%" | PROMIS trial, *PLoS Med* 2019: *"Only 7.6% of AM cases in the two study arms combined received appropriate treatment."* It is a pooled endline cross-sectional figure across **both arms**, not a value that stayed flat in the intervention arm over time. The intervention was SQ-LNS integrated into screening, not screening alone. |
| 10 | Dairy reduction "measurably worsens recovery" | *Advances in Nutrition* 2021 (PMID 33838044): recovery RR 0.93 (0.87–**1.00**), p=0.046, GRADE moderate. The upper bound is exactly 1.00. Mortality, time to recovery, default and non-response did not differ. "Main cost driver" is stronger than the paper, which says milk "is a costly ingredient." |
| 11 | Design qualifiers that should travel | Mali CHW coverage (PMID 36271427) is **before-after SQUEAC, not controlled**. Pakistan (PMID 30654780, *BMC Public Health* **2019**) is a cost-effectiveness analysis alongside a cluster-RCT in which the intervention arm was LHW care **complemented with NGO outpatient facility care**, and **no significance test is reported** for the 76.0% vs 82.95% gap. OptiMA demonstrated non-inferiority properly, but recovery was **97–98% in both arms** under trial supervision, against ~70% in routine programmes. The Rogers 2015 coverage paper carries its own caveat of *"selection bias towards favouring higher performing programmes"* — which biases 38.3% **upward**. |

---

## 4. The strategic problem: the CHW lever is the least well-supported part

The summary's organising claim is that *"moving delivery from facilities to community health
workers appears in all three interventions… the closest thing to a transferable finding in
this review."* Three things cut against it, two of which are already inside the report:

1. **Cochrane's breastfeeding review found no provider effect** — explicitly, in the paper
   the report cites for the 4–8 contacts figure.
2. **The home-visit mortality benefit tracks the package, not the cadre** — home visits
   alone RR 0.97 (0.90–1.05), in the same table as the RR 0.69 the report quotes.
3. **The report's own §7.6 finds facility adherence (47.3%) exceeds community adherence
   (37.2%)** for supplements. The full report calls this "a useful counterweight to the
   CHW-decentralisation finding." The summary omits it entirely.

The evidence that *does* survive is narrower and worth stating precisely: **decentralising
acute malnutrition *treatment* to CHWs raises treatment coverage** (Mali, Tanzania — both
uncontrolled or quasi-experimental), with the report's own three qualifications intact
(Pakistan quality, Mali conversion, cadre overload). That is a CMAM finding, not a
cross-cutting one. Presenting it as the transferable lever is the summary's weakest
inference, and it is the one a Save the Children technical advisor is most likely to
challenge — particularly since it also collides with WHO 2023, which makes CHW-delivered
wasting treatment a **conditional recommendation on very low certainty evidence** (below).

---

## 5. Significant literature that is missing

Verified absent from the full report. Ranked by how much the absence changes a conclusion.
(I confirmed that ComPAS's primary result, the RISE relapse cohort, the Gavine Cochrane
breastfeeding review and the WHO immediate-KMC trial *are* present — the report is better
covered than a quick scan suggests.)

**1. WHO guideline on the prevention and management of wasting and nutritional oedema in
infants and children under 5 (WHO, 2023).** The normative document that determines what a
ministry can adopt. Directly decisive here: recommendation **B17** says assessment,
classification and management "can be carried out by community health workers" with
training and supervision — but as a **conditional recommendation on very low certainty
evidence**, which a scaling review must convey rather than assert. **B5a** retains dual
WHZ ≥ −2 *and* MUAC ≥ 125 mm exit criteria; **B10** retains weight-based RUTF dosing. Both
are in tension with the MUAC-only, tapered-dose simplified protocols the report favours.
**C3** recommends cash transfers to reduce relapse — which retroactively validates the DRC
trial the report already cites. Without this, the report cannot state its most useful
finding: that simplified protocols are credibly non-inferior in aggregate but **not yet
normatively adopted**.

**2. Cochrane review of MMS — Keats EC, Haider BA, Tam E, Bhutta ZA, CD004905 (2019),
PMID 30873598.** The flagship synthesis, with GRADE ratings, absent while the report leans
on the same group's *Nutrients* and *Campbell* versions. Its absence produces §2.7 and §2.8
above. This is the most consequential single missing citation in the report.

**3. OMWaNA — *Lancet* 2024, doi:10.1016/S0140-6736(24)00064-3.** See §2.2. The largest
African KMC trial; null on its primary mortality endpoint.

**4. Smith ER et al., *Lancet Glob Health* 2017 (PMID 29025632)** — IPD meta-analysis,
17 trials, 112,953 women, 14 countries. MMS produced **greater** reductions in low
birthweight, SGA and 6-month mortality in **anaemic** women; greater neonatal mortality
reduction in **female** neonates; greater preterm effect in **underweight** women. This is
the targeting evidence, and it is exactly what a "where should we scale this" review needs:
it says MMS's advantage over IFA is concentrated in populations with high maternal anaemia
and undernutrition. The report cites the NYAS republication of the task-force IPD data but
not the effect-modifier findings, which are the operationally useful part.

**5. Alive & Thrive — Menon P et al., *PLoS Med* 2016;13(10):e1002159 (PMID 27780198).**
Cluster-randomised evaluations of at-scale breastfeeding programming in Bangladesh and Viet
Nam, combining intensive interpersonal counselling, mass media and community mobilisation.
Exclusive breastfeeding in Bangladesh rose from 48.5% to 87.6% in intensive areas; in Viet
Nam counselling was integrated into government health facilities. This is the strongest
"can breastfeeding promotion be delivered at national scale through government and mass
media" evidence that exists, and the report's central question is scalability. Its absence
also distorts the country section: Bangladesh is described as having the weakest CMAM
platform readiness, without noting that it hosts the best-documented at-scale breastfeeding
programme in the world. Companion: the sustainability evaluation, *BMC Public Health*
2020;20:1361.

**6. OptiMA-Niger — Daures M et al., *Am J Clin Nutr* 2025;122(4):972–985 (PMID 41043877).**
The first three-arm head-to-head of ComPAS and OptiMA against a national standard protocol,
1,732 children. Non-inferiority met on ITT for both, but **only ComPAS held per-protocol**,
and among the 1,140 children with MUAC <115 mm or oedema **the standard protocol achieved
higher recovery** (mortality did not differ). ComPAS used 50% less RUTF, OptiMA 32% less.
A report whose simplified-protocol case rests on OptiMA-DRC 2023 is one generation out of
date, and this trial is the first credible signal that simplification underperforms in the
most severe children — precisely the risk a government adopting at scale needs costed.

**7. Olofin I et al., *PLoS One* 2013;8:e64636 (PMID 23734210).** See §2.6 — the
counterfactual that justifies the entire intervention, and the source of the LiST
parameters a ministry's modellers will use.

**8. MANGO — Kangas ST et al., *PLoS Med* 2019;16(8):e1002887 (PMID 31454351).** 801
children, Burkina Faso; reduced-dose RUTF non-inferior on weight gain, **but with a small
negative effect on height gain velocity (0.2 mm/week, 0.04–0.4, p=0.015), more pronounced
under 12 months**. The key safety caveat on reduced-dose protocols. Its omission makes the
simplified-protocol case look cleaner than it is.

**9. Alé FGB et al., *Arch Public Health* 2016;74:38 (PMID 27602207)** — mother-led MUAC
screening non-inferior to CHWs, 12,893 trained mothers versus 36 CHWs; MUAC agreement 75.4%
vs 40.1%; hospitalisation at admission 0.70% vs 7.75%; annual cost US$8,600 vs US$21,980.
The cheapest and most scalable case-finding innovation in the field, and a direct answer to
"through what platform." Conspicuous given CARE's community-mobilisation comparative
advantage. The report mentions Family-MUAC's COVID-era scale-up but not the trial.

**10. Schoonees A et al., Cochrane CD009000 (2019), PMID 31090070** — the Cochrane anchor
for RUTF itself, with deliberately cautious conclusions that are a useful corrective
against over-claiming to partners.

**Also worth adding, lower priority:** the Lancet 2016 Breastfeeding Series (Victora et al.,
*Lancet* 2016;387:475–90; Rollins et al., 387:491–504) — the canonical framing document for
any partner-facing breastfeeding case, and the standard source for the burden and
investment argument. And on coverage (§6 below), the Global Action Plan on Child Wasting
and UNICEF's current reporting.

---

## 6. Two further points on evidence currency

**The coverage figure is a decade old and biased upward.** The 38.3% is correctly
transcribed from Rogers et al. 2015, but it is a 2012–13 survey whose own authors flag
"selection bias towards favouring higher performing programmes." A review whose central
question is coverage should not rest on it alone. The current citable position is the
**Global Action Plan on Child Wasting** framing that roughly one in three severely wasted
children receives treatment (lower outside humanitarian settings), plus UNICEF's annual
reporting. Do **not** compute coverage as admissions ÷ prevalence: that conflates point
prevalence with annual caseload. The correction is **Isanaka S et al., *BMJ Glob Health*
2021;6:e004342 (PMID 33653730)**, which puts the incidence correction factor at **3.6
(3.4–3.9)**, not the conventionally applied 1.6. Applied, true coverage is nearer one in
four or five. That there is **no rigorous current peer-reviewed global coverage estimate**
is itself a finding worth stating.

**WHO's MMS position is unchanged as of 2026** — antenatal MMS containing iron and folic
acid is *"recommended in the context of rigorous research"*; daily IFA remains standard of
care. The report states this correctly. Worth adding for the partner conversation: WHO's own
GDG evidence table gives a **third**, more conservative set of numbers (LBW 0.88, stillbirth
0.98, SGA 0.98, preterm 0.94) than either Cochrane or the Bhutta LMIC review. The report's
figure set matches the Micronutrient Forum / MMS-advocacy framing, which sources from the
Bhutta review. If those numbers are retained, disclose the provenance — a CARE technical
advisor will recognise them.

---

## 7. What I would do

**Before this goes to CARE:**

1. Fix §2.1–2.8. The KMC population error, the West Africa numbers and the 70% target are
   non-negotiable; the Ethiopia trend claim and the 11% counterfactual should be rewritten
   or dropped.
2. Add WHO 2023 and Cochrane CD004905 to the corpus and re-run the affected sections. These
   two citations change conclusions, not just references.
3. Rewrite §2 of the summary ("the one lever that recurs") to the narrower CMAM-specific
   claim the evidence supports, and restore the facility-versus-community adherence
   counterweight from §7.6.
4. Add a currency note wherever a figure predates 2020 (coverage, RUTF reach).

**For the pipeline, and for the methods paper:**

5. The verifier's guarantee needs restating precisely. It establishes traceability to a
   corpus record. It does not check that the number appears in the record in that form, nor
   that population, comparator, certainty rating and intervention descriptor survived into
   prose. **Population fidelity is the highest-yield thing to add** — a check that the
   population attached to an effect estimate in the synthesis matches the population field
   in the extraction record would have caught the KMC error, the 71%-inpatient framing, and
   the IFA-versus-MMS adherence slippage in one pass.
6. **Cross-review overlap detection is no longer optional.** The Campbell/Nutrients twin
   publication was caught in Chapter 5 and missed in Chapter 7 — same journal pair, same
   author group. It is listed as open work; this report is the concrete cost of deferring
   it, and it produced the report's largest scientific error.
7. **Dominant-trial detection did not fire on KMC**, where one trial appears to hold ~65% of
   a fixed-effect pooled weight. The extraction schema already captures `dominant_trial`;
   this looks like a gap in either extraction coverage for that record or in the synthesis
   prompt's use of the field.
8. **Guideline documents are not optional grey literature for a scaling review.** WHO
   guidelines are the binding constraint on what a ministry can adopt. Consider a small
   curated normative-documents layer (WHO, UNICEF/WHO JME, Global Action Plan) that sits
   alongside the PubMed/OpenAlex corpus, since none of them are reachable through it.

**One thing not to change.** The decision not to grade the three interventions against one
another is correct and worth defending explicitly if partners push back. So is the
separation of case-finding from treatment conversion — it is the most useful original
framing in the report and I would lead the partner conversation with it.
