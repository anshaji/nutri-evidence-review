# 2. Scope, method, and how to read this report

## 2.1 Scope

**In scope:** three partner-selected interventions — CMAM, breastfeeding promotion and support (facility and community), and antenatal MMS — assessed on both clinical and implementation outcomes, in low- and middle-income settings, with development contexts as primary and emergency settings tagged as a sub-analysis.

**Deliberately out of scope:** cost and cost-effectiveness. This is a decision on record rather than an oversight. Cost terms were excluded from search queries, from extraction, and from synthesis, so that no cost claim could enter the report informally. Cost is the subject of a separate later phase, and §8.1 flags the findings in this report that should seed it.

**Also out of scope:** general complementary feeding (raised by both CARE technical experts and flagged for a decision in §8), and country-specific retrieval — searches were run country-agnostically so that the evidence base would not be biased toward a pre-selected shortlist, with country fit layered on at synthesis.

## 2.2 The PICOS frame

Each intervention was specified before searching, following the standard template. The distinguishing feature of this review is the **dual outcome axis**: alongside clinical endpoints, every intervention was assessed on implementation outcomes — coverage, adherence, delivery platform, barriers, scalability and equity. This was a direct response to the partner steer that adherence and coverage, not efficacy, are the binding constraint.

| | |
|---|---|
| **Population** | Children 6–59 months with severe or moderate acute malnutrition (SAM, MAM) for CMAM; mothers and infants 0–6 months for breastfeeding; pregnant women for MMS |
| **Intervention** | As specified per chapter |
| **Comparison** | Includes simplified-versus-standard protocols (CMAM), facility-versus-community delivery (breastfeeding), and MMS versus iron-folic acid, IFA (the transition question) |
| **Outcomes** | Clinical endpoints **and** implementation outcomes across six dimensions |
| **Study design** | Meta-analyses and systematic reviews, trials, cohorts, and program evaluations — the last being essential, since implementation evidence rarely appears in trials |

Full specification: `docs/PICOS_specification.md`.

## 2.3 How the evidence was assembled

| Stage | Result |
|---|---|
| Retrieval — 3 intervention blocks × meta-analysis, systematic-review and implementation passes | 1,671 papers (CMAM 500, breastfeeding 640, MMS 531) |
| Deduplication and merge | **1,636 papers** |
| Full-text acquisition | 981 papers with full text retrieved and parsed |
| Structured per-study extraction | **984 records**, of which 980 used full text |
| On-topic after screening | **648 records** (CMAM 243, breastfeeding 193, MMS 212) |
| Implementation findings extracted | **2,470 findings** across six dimensions; 630 records (97%) carry at least one |

Three design choices are worth noting because they shaped what the review can say.

**A dedicated implementation retrieval pass.** Beyond the standard meta-analysis and systematic-review passes, a third pass searched explicitly for coverage, adherence, delivery-platform and barrier outcomes across program-evaluation, trial and cohort designs — with no cost terms. This is why program evaluations make up a substantial share of the corpus (48 for CMAM alone) and why the implementation axis is directly evidenced rather than inferred.

**Breastfeeding was retrieved as one block, not two.** Separate facility and community searches returned near-identical top-lists, because broad breastfeeding reviews genuinely cover both channels. The facility-versus-community distinction is therefore a per-study judgment made at **extraction** (`bf_delivery_setting`), not a retrieval split. This was a finding, not a convenience.

**Version is not new evidence.** Where a review has been updated (two editions of the same Cochrane review, for instance), the versions are collapsed and only the newest retained. An earlier synthesis had counted two editions of one review as two independent generations of evidence.

## 2.4 Verification

Every numeric claim in this report carries a citation to a specific record, and an automated verifier checks each one against the corpus. Its load-bearing output is the count of claims that cannot be traced to any corpus record — the signature of a number imported from background knowledge rather than from the evidence. **That count is zero.**

This check exists because an audit of an earlier synthesis found exactly that failure: a widely-quoted mortality statistic that was plausible, well-known, and not from the corpus. The same audit produced the other grounding rules used here — study design quoted verbatim from the source record rather than inferred, all-cause and cause-specific mortality kept separate, fixed- and random-effects estimates reported with the dominant trial named, and review versions collapsed.

A separate manual fact-check audited 268 numeric values against their specific cited record — not merely against corpus presence — confirming record counts and source descriptions and tracing interpretive claims to record text.

**What verification does not do.** It confirms that a number appears in the cited source. It does not confirm that the source is correct, that the pooled estimate is well-constructed, or that the interpretation drawn is the only reasonable one. Section 8 sets out those limits.

## 2.5 Why this report does not grade the interventions

An earlier draft carried summary grades — evidence strength A/B/C, implementation readiness High/Moderate/Low, and a "Tier 1" band. **They have been removed.**

The reason is that a single letter compressed several genuinely different things into one symbol and then invited comparison across them. "Evidence strength B" for CMAM was doing at least three jobs at once: describing a structural feature of its literature (treatments are only ever compared against other treatments), describing the proportion of the corpus that is synthesis-tier, and implying a verdict on the intervention. Readers reasonably took it as the third. A grade that has to be explained in a paragraph is not helping.

The three interventions also differ in ways a common scale cannot hold. They are measured on different outcomes, against different comparators, in literatures at different stages of maturity. Placing them on one axis creates an impression of commensurability the evidence does not support.

**What replaces it.** Each chapter states plainly what its evidence base contains, what it establishes, where it is thin, and what it cannot answer. Where a source reports formal certainty using **GRADE** — the standard instrument, applied by review authors to a specific outcome — we quote it as they stated it ("high certainty", "low-to-moderate"). That is a real assessment made by the people closest to the data, and it is reported rather than replaced by a judgment of our own.

Readers who want a one-line summary per intervention will find it at the head of each chapter, in sentences rather than letters.

## 2.6 A note on the statistics

For readers who do not work with trial data daily: **RR — risk ratio, also called relative risk — compares treated to untreated, and 1.00 means no difference.** RR 0.85 means the outcome occurred 15% less often; RR 1.51 means 51% more often. The direction that counts as good depends on the outcome — for deaths and low birthweight you want a number below 1; for recovery and breastfeeding rates you want it above 1.

The bracketed range, such as (0.77–0.93), is the confidence interval. **If it crosses 1.00, the result is not statistically significant.**

| Measure | How to read it |
|---|---|
| **RR** (risk ratio / relative risk) | Ratio of rates. 1.00 = no difference |
| **OR** (odds ratio), **HR** (hazard ratio) | Read like RR |
| **RD** (risk difference) | The **absolute** difference between the two groups, in percentage points — not a ratio. RD 0.03 means three percentage points apart. **0 means no difference** |
| **MD / SMD** (mean difference) | Compares averages rather than rates. **0**, not 1, means no difference |

**One term that is easy to misread: "non-inferior".** A non-inferiority trial does not claim the new option is *better*. It asks whether the new option is **not worse by more than a margin agreed before the trial began** — the point being that if it performs about as well while costing less or being simpler to deliver, that is a win. So when a simplified protocol is reported as non-inferior with a risk difference of 0.03, the finding is "**as good as** standard care," not "3% better." The small positive number is not the claim; the *absence of a meaningful shortfall* is.
