# Audit of the CMAM Decision Memo

Audit date: 29 September 2026 (America/Los_Angeles). Document audited: **CMAM Decision Memo _ CEGA-CARE.pdf**, dated 30 September 2026, eight PDF pages. Page references below count the cover as page 1. This audit concerns the supplied PDF, not just the differently worded repository memo.

**Assessment: revise before using this as a protocol-adoption decision.** The memo has a useful structure and many accurate headline numbers. Its principal weakness is the comparison underpinning the ComPAS recommendation: it combines different endpoints and protocol versions, misdescribes MANGO and part of the WHO comparator, and presents an incomplete account of cost per recovery. ComPAS is a defensible candidate for a locally authorised programme or evaluation; the memo does not establish that it is the best protocol across the stated population and proposed settings.

The PDF and existing source files were left unchanged. Instructions and recommendations inside documents were treated as material to audit, not as authorisation to implement them.

## Scope and approach

I read the complete PDF text, rendered and inspected all eight pages, and inspected the options table at larger size. I compared the memo with the repository's CMAM report, decision memo, prior audit, CARE context, methods, and structured corpus. I searched the complete retrieval and extraction databases for cited sources and checked relevant extraction records and cached full texts. I also checked primary publications and WHO/UNICEF material online, particularly sources absent from the structured database.

This is a claim, interpretation, provenance and presentation audit. It is **not** a new systematic review, a re-extraction of all 984 database records, an individual participant data analysis, or a formal risk-of-bias/GRADE assessment. Targeted online checks do not establish that all relevant research has been found. Several newer sources were checked through their published abstracts; limitations are noted below. A source being present in the repository is not independent verification that its extracted interpretation is correct.

## Findings requiring revision

### 1. High priority: distinguish the endpoints behind the protocol ranking

**Pages 4, 6 and 7.** Counting three supportive ComPAS trials is defensible, but describing them as three interchangeable demonstrations of recovery is misleading. In Niger, the primary endpoint was a composite assessed six months **from enrolment**, with WHZ ≥−3, rather than WHO-style full anthropometric recovery or six months after discharge. ComPAS met non-inferiority in both analysis populations; OptiMA did so only in intention-to-treat. The severe-entry group's nutritional recovery result favoured standard care. The 32% OptiMA food reduction belongs to that severe-entry analysis, not the entire trial population. [Daures et al. 2025, methods, Table 3 and Figure 2](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/2025-11/010095394.pdf).

OptiMA's DRC superiority result also concerned a six-month favourable composite outcome, rather than simply discharge recovery. The retrieved abstract gives 72% versus 63% in the intention-to-treat analysis. [Cazes et al. 2022](https://doi.org/10.1016/S2214-109X(22)00041-9).

**Fix:** replace the vote-counting headline with “ComPAS has supportive trial evidence, with important differences by endpoint and entry severity.” Give each trial's outcome, population and follow-up clock in a small evidence appendix. State that the preferred protocol is the authors' programme-design judgement, and specify the criteria used to make it. Failure to demonstrate non-inferiority is not itself proof of inferiority.

### 2. High priority: MANGO's admission and discharge cells are incorrect

**Page 6, MANGO row.** “As standard” points to the WHO 2023 row. The 2019 MANGO trial excluded children with any oedema. Its recovery rule depended on the admission indicator: WHZ-only entrants met the WHZ threshold, MUAC-only entrants met the MUAC threshold, and children entering on both met both. It did not impose the displayed dual discharge rule on every child.

The trial supports non-inferiority for overall weight-gain velocity. It did not prove identical recovery or length of stay. The local extraction also records lower weight gain after the first two weeks, in addition to the reported height-gain penalty.

**Fix:** describe the actual trial eligibility and discharge criteria, and replace “no difference” with “non-inferior overall weight gain; no statistically clear difference in recovery or length of stay.” If the intended option is a new MANGO-inspired adaptation to WHO 2023 care, label it as such and distinguish it from the package actually tested. [Kangas et al. 2019, methods and outcomes](https://doi.org/10.1371/journal.pmed.1002887); local full text: `data/fulltext/oa_W2970671601.json`.

### 3. High priority: the WHO comparator unnecessarily bundles two products with standard care

**Page 6, WHO row.** WHO 2023 does not require two products and supply chains: recommendation B15 allows qualifying RUTF or RUSF for moderate wasting requiring specially formulated foods. The displayed arrangement is a common historical service model, not an unavoidable consequence of retaining WHO dosing and discharge recommendations. WHO B10 also explicitly permits a step-down dose, as the table correctly notes. [WHO 2023, B10 and B15](https://www.ncbi.nlm.nih.gov/books/NBK601655/).

**Fix:** separate three decisions: service organisation, product choice, and dosing/discharge. Rename the option “WHO-aligned dosing and discharge” and remove the categorical two-product disadvantage. Otherwise, the comparison gives simplification credit for a benefit that may also be achievable within a WHO-aligned programme.

### 4. High priority: the recommended package leaves eligibility and discharge actions unresolved

**Pages 2, 6 and 7.** The table makes clear that MUAC-only admission excludes children with low WHZ but MUAC ≥125 mm and no oedema; the recommendation does not say how they will receive care. Checking WHZ at discharge cannot address children who never entered the programme. Likewise, measuring WHZ before discharge does not specify what happens if the child passes MUAC criteria but remains wasted by WHZ. A scale alone is insufficient: reliable length/height measurement and calculation are also needed.

**Fix:** add an explicit assessment/referral pathway for children outside the simplified eligibility rule. Specify whether WHZ changes the exit decision or is only measured for evaluation, and what happens where measurement capacity is inadequate. WHO's dual exit recommendation is conditional, but a departure should be explicit and nationally agreed. [WHO 2023, B5](https://www.ncbi.nlm.nih.gov/sites/books/NBK601642/?report=reader).

The memo appropriately says attendance support should be tested. Preserve that wording: better attendance is a plausible response to Niger's severe-case result, not an established remedy. Before adoption, define the comparator, subgroup monitoring and criteria for changing the programme. These are audit recommendations about decision completeness, not a replacement clinical protocol.

### 5. High priority: the final cost argument is selective

**Pages 4 and 7.** The Gao figures on page 4 are correctly rounded. However, the final recommendation repeats a lower cost per recovery from Kenya/South Sudan while omitting Gao's counterexample on that same metric. Gao's societal base-case costs, in 2021 US dollars, were:

| Outcome | Standard, facilities plus CHWs | Simplified, facilities plus CHWs |
|---|---:|---:|
| Per child treated | 179 | 210 |
| Per child recovered | 219 | 226 |
| Average per DALY averted | 60.3 | 53 |

Thus the preferred arm changes with the outcome. DALYs are modelled, and the average ratio is not the incremental cost-effectiveness of switching between these arms. The coordination category also includes support and office costs, not just supervision. [Cichon et al. 2025](https://link.springer.com/article/10.1186/s12889-025-21411-5).

**Fix:** replace the general cheaper-recovery rationale with “Cost advantages vary by setting and outcome; local full-pathway costing is required.” Keep the Kenya/South Sudan estimate, but label its setting and perspective. Do not compare absolute costs across studies without aligning price years, populations, included costs and denominators. The proposed local costing work is a strength; it should inform the choice rather than merely follow it.

### 6. High priority: the cash-transfer cost claim is unsupported as written

**Page 5.** The claim that cash roughly doubles cost per child has no defined baseline or costing calculation. The DRC trial transferred US$40 monthly for six months, or US$240 **per household**; one household could include more than one eligible child. This is a transfer value, not total delivery cost per treated child. The 70–79% lower relapse hazards are supported, corresponding to SAM and MAM respectively. Transfers began alongside treatment, not only after discharge. [Grellety et al. 2017](https://doi.org/10.1186/s12916-017-0848-y); cached full text: `data/fulltext/oa_W2606164967.json`.

“Nobody has costed it properly” is an unbounded literature claim and should be removed. The structured extraction deliberately excluded cost information, so its silence cannot support that assertion. A newer Somalia cash-plus prevention study includes an economic evaluation, although it does not answer the narrower post-SAM relapse cost-effectiveness question. [Somalia economic evaluation](https://jogh.org/2026/jogh-16-04111).

**Replacement:** “The DRC trial added US$240 per household in transfers over six months. The incremental programme cost and cost per sustained recovery in the proposed setting remain to be estimated.” Retain the proposed locally costed pilot, framed as a design choice.

### 7. Moderate priority: qualify Gao's protocol and outcome comparisons

**Pages 4, 6 and 7.** The recovery and discharge-error figures are supported. Gao included facilities and CHWs in both intervention arms, not solely CHW care. Its simplified arm modified ComPAS for children below 5 kg. Admission and recovery criteria differed across arms; consequently, the overall 92.9% versus 81.8% figures are not a comparison using identical case definitions. The 6% versus 19% figures reflect discharge errors under the respective rules, not necessarily equivalent detection of all residual wasting. Gao's non-inferiority margin was 5 percentage points. [López-Ejeda et al. 2024, Table 1 and methods](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2024.1283148/full).

**Fix:** label Gao “adapted ComPAS, delivered through facilities and CHWs”; add the different-definitions caveat and the Gao margin. The current footnote correctly gives 10 points for its named Kenya/South Sudan, Niger and DRC trials, but omits Gao even though it is counted in the headline. Do not call the three trials exact replications of the page-6 regimen.

### 8. Moderate priority: supply missing populations, time periods and study designs on relapse

**Page 5.** Guesdon's 14.2%/5.2% and 19.2%/9.4% figures are supported. The pooled population included children initially treated for **SAM or MAM**, not exclusively SAM. This is prognostic evidence, not a randomised estimate of changing a discharge rule; the memo already acknowledges the latter and should retain that qualification. [Guesdon et al. 2026](https://pubmed.ncbi.nlm.nih.gov/41825529/).

The apparent Somalia reference is a prospective cohort: cash participation was associated with lower relapse (adjusted HR 0.44, 95% CI 0.22–0.90). It is absent from the slide's source list. Add the full reference and call it observational corroboration. [Somalia relapse cohort, 2026](https://jogh.org/2026/jogh-16-04019).

The Malawi 56% versus 53% result concerns children recovered from **MAM**, followed for **12 months**, among 1,383 completing follow-up. Say “no statistically clear improvement”; do not let the surrounding six-month SAM discussion imply the same population and clock. [Stobaugh et al. 2017](https://pubmed.ncbi.nlm.nih.gov/28615258/).

Caregiver screening was inconclusive on its primary endpoint, as stated. A separate full-scale trial is registered as NCT06599580; registration alone does not verify current recruitment status. Cite it and date-check “under way,” or use “a full-scale trial is registered.” [Feasibility trial](https://pubmed.ncbi.nlm.nih.gov/41569394/), [full-scale registration](https://clinicaltrials.gov/study/NCT06599580).

### 9. Moderate priority: restore a traceable evidence appendix and methods note

**Throughout.** Author-year footers are insufficient for independent checking, particularly with multiple Daures publications. The PDF has no full bibliography, clickable links or annotations. Add a companion reference/claim appendix with DOI/PMID, exact outcome, population, comparator, analysis set, uncertainty and follow-up clock. Explicitly identify manual additions outside the pipeline and the targeted search date. Describe this as a narrative synthesis unless a reproducible systematic update has actually been completed.

The repository version is materially different: `CMAM_DECISION_MEMO.md` leaves the protocol decision open and excludes cost comparisons. `CMAM_REPORT.md` also cautions against a single recommendation for all children. Neither is the exact source of the supplied PDF. Record which editable source generated this PDF and synchronise the evidence wording across versions before circulation.

Historical “cost deferred” notes in the repository are context, not instructions to omit costs from this audit. The PDF includes cost claims, so those claims were audited.

## Headline claims that can be retained

| PDF page | Claim | Audit disposition |
|---|---|---|
| 3 | 42.8 million wasted; 12.2 million severely wasted in 2024 | Supported by the 2025 JME. Label as prevalence-based estimates, not all episodes during the year. [UNICEF](https://data.unicef.org/topic/nutrition/malnutrition/). |
| 3 | Approximately one in three treated | Supported as a historical statement in the 2020 Global Action Plan. Prefer “reported in 2020” to implying a precisely dated 2020 measurement. Do not combine it arithmetically with the 2024 prevalence estimate. [Global Action Plan](https://www.unicef.org/media/96991/file/Global-Action-Plan-on-Child-Wasting.pdf). |
| 3 | Mortality rate about 11.6 times higher, comparator WHZ ≥−1 | Supported; an observational association, not the effect of withholding treatment. [Olofin et al.](https://doi.org/10.1371/journal.pone.0064636). |
| 3 | RUTF recovery RR 1.33, moderate certainty | Supported; 95% CI 1.16–1.54, six studies, 1,852 children. It compares diets, not full CMAM against no treatment. [Schoonees et al.](https://pubmed.ncbi.nlm.nih.gov/31090070/). |
| 3 | Screening increased 40 percentage points without higher treatment coverage | Supported. It concerns adding preventive SQ-LNS to screening in Mali, not all screening interventions. [Huybregts et al.](https://doi.org/10.1371/journal.pmed.1002892). |
| 3, 5 | 22–63% relapse within six months | Supported for the three study settings and relapse to moderate or severe acute malnutrition; not a representative global rate or solely SAM relapse. [King et al.](https://doi.org/10.1016/S2214-109X(24)00415-7). |
| 4, 6 | 122 versus 193 sachets; approximately 37% fewer | Supported for children admitted with SAM who recovered in Kenya/South Sudan. The comparator includes RUTF and RUSF. Page 4 correctly uses “ready-to-use food”; carry that denominator into page 6. Calculation: (193−122)/193 = 36.8%. [Bailey et al.](https://doi.org/10.1371/journal.pmed.1003192). |
| 6, 7 | US$918 versus US$1,041 per recovery | Supported for the original ComPAS evaluation, not a universal saving; see finding 5. [Bailey et al.](https://doi.org/10.1371/journal.pmed.1003192). |
| 5 | Relapse makes treatment 1.7–2.2 times as costly | Consistent with Puett's published abstract if this means total initial treatment plus SAM retreatment. Initial costs were US$191/92/178 and additional costs US$215/64/215, giving total-cost ratios 2.13/1.70/2.21. Specify 2022 US dollars and study settings. Do not describe the ratio as the additional retreatment cost alone. Full costing tables were not independently reanalysed. [Puett et al.](https://pubmed.ncbi.nlm.nih.gov/41551722/). |
| 4, 6 | WHO dosing and dual discharge thresholds | Broadly supported; distinguish conditional low certainty for dosing from conditional very low certainty for exit. The step-down also requires oedema resolution. See findings 3–4. |
| 7 | Measure six-month sustained recovery, deaths and loss to follow-up | Sensible programme proposal. Define denominator, observation schedule, relapse criteria and handling of missing follow-up. Being recovered at month six is different from remaining continuously relapse-free. |

## Corpus and provenance audit

The current files contain **1,636 retrieved records** and **984 extracted records**, with **648 marked on-topic**, of which **243** are in the CMAM block. Thirty-two CMAM records carry the exact design label `RCT`; these are record labels, not an independently verified count of unique trials. There are no duplicate extraction keys. The local CMAM report's “239 on-topic records” does not reconcile directly with the current 243; document the exclusion/filter or version that explains it.

The methods file records 652 abstract-only papers awaiting extraction. Consequently, neither the large corpus nor automated numeric matching establishes complete coverage. The actual JSON flags show 980 records with `fulltext_used: true`; record counts and unique-paper/full-text counts should not be silently interchanged.

The following is a targeted provenance check, using DOI/PMID matching across the full retrieval and extraction files:

| Source used by the memo | Status in the structured data inspected |
|---|---|
| Bailey 2020, MANGO 2019, Grellety 2017, King 2025 | Extracted, with cached full text inspected for relevant claims. |
| Olofin 2013 | Present in extraction, but marked off-topic. It is usable as contextual mortality evidence; disclose that role rather than claiming all citations belong to the included CMAM treatment set. |
| Cazes 2022, OptiMA-DRC | Retrieved as PMID 35303461; no matching extraction record. Abstract inspected. |
| Cazes 2023, OptiMA severe-case analysis | Extracted as `oa_W4322490889`; useful contextual evidence, but not an extra independent DRC trial. |
| López-Ejeda 2024; Cichon 2025; Daures 2025 Niger | No matching DOI in either inspected structured file. Primary publications checked externally. |
| Guesdon 2026; Puett 2026; Bountogo 2026; Stobaugh 2017 | No matching DOI in either inspected structured file. Published source/abstract checked externally. |
| Schoonees 2019 | No matching updated-review extraction located. The retrieval file contains an older CD009000-family record; that is not verification of the 2019 update. |
| WHO, JME, Global Action Plan, Somalia 2026 corroboration | External contextual/update sources; require a maintained supplement to the pipeline evidence set. |

These gaps do **not** make the added studies invalid. They mean a “verified against the corpus” assurance cannot be applied to the entire PDF. Cost exclusions in the original extraction are particularly relevant to the new economic claims.

For traceability, the principal local records inspected were `oa_W3041570559` (ComPAS), `oa_W2970671601` (MANGO), `oa_W2606164967` (cash), `oa_W4405535622` (relapse), and `oa_W4322490889` (OptiMA severe-case analysis). Their cached full texts are in the shared repository `data/fulltext/` directory, as documented by CARE's README.

## Suggested replacement for the decision statement

> Prioritise ComPAS as a candidate for a nationally authorised, locally evaluated programme. Final protocol selection should account for eligible children, the severe-case findings, admission and discharge rules, delivery capacity and local costs. Define care for children identified by low weight-for-height who fall outside MUAC eligibility, and specify how discharge measurements change care. Measure recovery and relapse with prespecified definitions, and evaluate attendance support and cash transfers without assuming that they remove the observed uncertainties.

This permits a clear programme preference while distinguishing it from a demonstrated universal optimum. If the authors intend to recommend immediate adoption rather than evaluation, the memo should state the local evidence, decision criteria and governance that justify that stronger step.

## Presentation and remaining checks

The eight-page PDF renders without obvious clipping, overlapping elements or broken symbols. Page 8 is a branded back cover, not an accidental blank page. The main presentation weakness is legibility: on a 960 × 540 point page, the page-6 table uses approximately 9–11 point text, and footnotes/source lines are 8–8.5 points. Split the options and evidence tables or provide a readable appendix; add page numbers and working reference links.

Before circulation, resolve the current status of the full-scale caregiver trial, identify the Somalia reference explicitly, reconcile the corpus-count/version difference, and link the exact editable source of this PDF. Confirm CARE's named economic-evaluation capacity with the team: the repository evidence does not establish that organisational fact. The report's proposed local costing, retention monitoring and six-month follow-up are worth preserving after the evidentiary corrections above.
