# Evidence Atlas — country profiles for child wasting

**Status:** plan + probe results, no code yet · **Written:** 2026-09-24 · **Owner:** Akash
**Folder name is provisional** (`atlas/`); rename before the first commit if you prefer.

---

## 1. What we are building

A catalogue of country profiles for one nutrition problem at a time, starting with
**wasting in children under 5**. Each profile joins three things that today live in
different places:

| Layer | Question it answers | Where it comes from |
|---|---|---|
| **Evidence** | What works to treat and prevent wasting, with what effect, in which setting? | The existing pipeline corpus (`data/evidence_db.json`, `CARE_review/data/evidence_db.json`) plus a dedicated wasting retrieval block later |
| **Country context** | How big is the problem, who is at risk, what can the health system and social-protection system carry? | Public APIs: World Bank WDI, UNICEF/WHO/WB Joint Malnutrition Estimates (JME), WHO GHO, DHS |
| **Delivery landscape** | Which government and NGO programmes already deliver, through which platform, at what coverage? | Curated registry with a source URL per claim (no API exists) |

On top of the profiles sit two tools:

1. **Analogue finder.** For a country with a wasting problem but thin evidence (the
   user's Ecuador example), find the evidence-rich countries whose profile is closest,
   so their evidence can be read across with eyes open.
2. **Later: effect transport.** Combine experimental effects from analogue settings
   with precise-but-biased local observational effects into a bias-adjusted weighted
   effect, and eventually a simulation layer that helps policymakers compare options.

It builds directly on the existing repo: same stdlib-first style, same grounding rule
(every number carries a source), same verifier philosophy, and the CARE deep-dive's
`country_analysis.py` already solved country-tag normalisation and the
"multi-country review is not evidence about one country" problem.

---

## 2. Probe results (2026-09-24)

Everything below was tested live from this machine with plain `curl`/`urllib`.

### 2.1 Country-context data sources

| Source | Reachable | What it gives us | Notes |
|---|---|---|---|
| **World Bank WDI API** (`api.worldbank.org/v2`) | Yes, JSON | Wasting and severe wasting prevalence (JME survey values), under-5 population, health expenditure, physicians/nurses/beds density, UHC index, skilled birth attendance, immunisation, WASH, poverty, Gini, rural share, female literacy, fertility, and **social-protection coverage** (ASPIRE `per_allsp.cov_pop_tot`, needs `source=25`) | One indicator per call; `mrnev=1` returns latest non-empty value. Country metadata endpoint gives region, income group and lending type for the standardised LMIC list (an item already on the repo's open-work list). |
| **UNICEF JME via SDMX** (`sdmx.data.unicef.org`) | Yes, CSV | Wasting and severe wasting **disaggregated by wealth quintile, residence, sex, age band, maternal education**, with CI, SE and weighted sample size, and the source survey named | Ethiopia returned 94 rows for one indicator. This is the best single burden source. |
| **WHO GHO OData** (`ghoapi.azureedge.net`) | Yes, JSON | Survey-based wasting with CI and survey citation; **model-based numbers affected** (`NUTWASTINGNUM`, `NUTSEVWASTINGNUM`, millions); **community health worker density** (`HRH_29`) and counts (`HWF_0024`) | CHW density is the platform indicator CMAM scaling hinges on. |
| **DHS Program API** (`api.dhsprogram.com`) | Yes, JSON, no key | Wasting by **subnational region**, wealth, residence, age, mother's education, birth size; 92 countries; multiple survey rounds so a within-country trend exists | Ethiopia 2016: Somali region 22.7% vs SNNPR 6.0%. This is the "where inside the country" layer. |
| INFORM Risk index API | Reachable, needs an integer workflow id | Fragility / hazard / coping-capacity scores | Fix the query later; not needed for PoC. |
| WHO GINA (policies and programmes) | HTTP 301, HTML app | Nutrition policies and programme actions by country | Not machine-readable. Treat as a manual source for the registry. |
| acutemalnutrition.org country pages | HTTP 200, HTML | CMAM admissions and coverage narratives | Candidate for careful scraping later; manual for PoC. |
| Global Nutrition Report country profiles | HTTP 200, HTML | Consolidated indicators and policy commitments | Manual cross-check source. |
| childwasting.org (Global Action Plan) | HTTP 403 | Country operational roadmaps | Download by hand if needed. |

### 2.2 Size of the country pool

From the WDI wasting series, latest value per country, joined to income group:

| Pool | Count |
|---|---|
| Countries with any wasting estimate | 164 |
| Low, lower-middle and upper-middle income with an estimate | 126 |
| Of those, wasting ≥ 10% (WHO "high" or "very high") | 17 |
| 5–10% ("medium") | 37 |
| < 5% | 72 |

**Vintage warning.** Of the 126 LMIC estimates, 18 are from before 2015 and several
high-burden ones are very old (South Sudan 2010, Somalia 2009, Papua New Guinea 2010).
Wasting has no modelled national trend in JME because prevalence is seasonal, so the
profile must carry the survey year on every burden number and flag anything older than
a threshold.

### 2.3 What the existing corpus already holds on wasting

Union of both evidence databases, on-topic records that are CMAM-tagged or mention
wasting, acute malnutrition, SAM/MAM, RUTF/RUSF, WHZ or MUAC:

| Measure | Value |
|---|---|
| Unique wasting-related records | 315 |
| By tier | observational 101 · programme evaluation 49 · RCT 42 · other review 41 · systematic review 32 · meta-analysis 23 · modelling 13 · qualitative 11 |
| Treatment vs prevention (heuristic on intervention label) | treatment 209 · prevention 38 · other 68 |
| Numeric effect rows with a CI on a wasting-relevant outcome | 436 (observational 237, MA 58, RCT 56, programme eval 51, SR 22) |
| Countries with country-specific primary evidence (≤ 3 country tags) | 30 |
| Countries with at least one RCT | 21 |

Top country-specific primary evidence: Ethiopia 30, Malawi 15, Kenya 9, India 9,
Mali 7, Zambia 7, Uganda 6, Nepal 5, Pakistan 5, Niger 5. RCTs cluster in Malawi 8,
Kenya 5, Burkina Faso 4, Mali 3, Pakistan 3.

Two gaps this reveals: the corpus is **treatment-heavy** (the CARE block was CMAM), so
prevention evidence (SQ-LNS, MAM supplementary feeding, cash, IYCF, WASH) needs its own
retrieval block; and country tags come from LLM extraction, so the atlas must reuse the
`normalise_country` logic from `CARE_review/code/country_analysis.py` rather than trust
raw strings.

---

## 3. Architecture

```
atlas/
  PLAN.md                    this file
  README.md                  (PoC) how to run, what each output is
  docs/
    PROFILE_SCHEMA.md        field-by-field definition of a country profile
    INDICATORS.md            the indicator catalogue: code, source, unit, definition, why it is in
    METHODS_transport.md     (later) effect-transport and simulation design
  code/
    config.py                paths, API endpoints, rate limits; reuses ../code/01_config.py .env loader
    countries.py             standardised country list from the WB metadata endpoint (ISO3, region, income)
    indicators.py            the indicator catalogue as data, not code
    fetch_wdi.py             World Bank WDI client (cached per indicator, resumable)
    fetch_jme.py             UNICEF SDMX client (national + disaggregated wasting)
    fetch_gho.py             WHO GHO client (numbers affected, CHW density)
    fetch_dhs.py             DHS client (subnational + equity breakdowns)
    evidence_link.py         corpus → per-country evidence cards (reuses CARE normalisation rules)
    registry.py              loads + validates the curated programme registry
    profile.py               assembles data/profiles/{ISO3}.json with provenance on every value
    similarity.py            Gower-style distance over the profile, weighted by domain; analogue finder
    build_atlas.py           orchestrator: fetch → link → assemble → similarity → render
    render.py                Markdown (and later HTML) profile pages
  data/                      gitignored; raw API cache, profiles, similarity matrix
  registry/                  tracked; curated programme entries, one YAML/JSON per country, each claim with a URL
```

Design rules carried over from the main pipeline:

- **Provenance on every value.** Each profile number is stored as
  `{value, year, source, indicator_code, retrieved, note}`. The verifier can then lint a
  written country brief against the profile the same way it lints a synthesis against the
  corpus.
- **Cache everything, resume anything.** Raw API responses under `atlas/data/raw/`.
- **Evidence attribution follows the CARE rule.** A record counts as evidence *about*
  a country only if it carries ≤ 3 clean single-country tags; pooled reviews count toward
  breadth, never toward country-specific effects.
- **The registry is curated, not generated.** No programme claim without a source URL
  and a `verification_status`. LLM assistance is allowed for drafting entries from the
  corpus's `implementation_findings`, but a human marks them verified.

### 3.1 Profile schema (draft, to be finalised in `docs/PROFILE_SCHEMA.md`)

| Section | Contents |
|---|---|
| `identity` | ISO3, name, WB region, income group, lending type, fragility flag |
| `burden` | wasting and severe wasting prevalence with CI, survey year and source; numbers affected (model-based); disaggregation by wealth, residence, sex, age; subnational regions with prevalence; prevalence category (WHO thresholds); data-vintage flag |
| `at_risk` | under-5 population; estimated wasted children; stunting and underweight as co-burden; low birth weight; food insecurity / undernourishment |
| `health_system` | physicians, nurses, CHW density; beds; current health expenditure per capita and share of GDP; government share and out-of-pocket share; UHC service coverage index |
| `platform_reach` | skilled birth attendance, ANC 4+, DTP3 and measles coverage, ORS use, care-seeking for ARI: proxies for how far the routine system reaches |
| `social_protection` | ASPIRE coverage of social protection and social assistance |
| `wash_and_environment` | basic water, basic sanitation, open defecation |
| `socioeconomic` | GDP per capita PPP, poverty headcount, Gini, rural share, female literacy, fertility |
| `programmes` | registry entries: name, type (government / NGO / donor), intervention (CMAM, SQ-LNS, cash, IYCF...), delivery platform, scale (national / subnational / pilot), coverage if reported, source URL, verification status |
| `evidence` | per intervention: count of records by tier; country-specific effect estimates (design verbatim, outcome, measure, value, CI, year, key); pooled reviews that include the country; implementation findings by dimension (coverage, adherence, delivery platform, barriers) |
| `evidence_summary` | evidence-richness score per intervention, so the analogue finder can require "has evidence" |
| `_provenance` | retrieval dates, API versions, cache paths |

### 3.2 Similarity and the analogue finder

- Distance: Gower-style so mixed types and missing values are handled without imputation
  (a missing indicator drops out of that pair's distance and lowers a coverage weight).
- Domain weights, exposed and editable: burden, at-risk, health system, platform reach,
  social protection, socioeconomic, fragility. Default equal weights for the PoC.
- **Similarity is purpose-specific.** The right analogue for scaling CMAM (CHW density,
  facility reach) is not the right analogue for cash transfers (social-protection
  coverage). The PoC ships one default weight set and one alternative
  ("delivery-platform similarity") to show the difference.
- Query: `find_analogues(target, intervention, min_evidence=k)` returns the nearest
  countries that clear the evidence threshold for that intervention, with the per-domain
  distance breakdown so the user can see *why* they are close.

---

## 4. Proof of concept

Goal: prove the join works end to end on a small, deliberately mixed set of countries,
and let you and Liz judge whether the profiles and analogues are credible before we
scale to 126 countries or spend on new retrieval.

### 4.1 Country set (12)

| Role | Countries | Why |
|---|---|---|
| Evidence-rich, high burden | Ethiopia, Malawi, Kenya, India, Niger, Pakistan | Most country-specific primary and RCT evidence in the corpus |
| Evidence-poor, high burden | Yemen, Mauritania, Djibouti, Laos, Papua New Guinea | Wasting ≥ 10% with little or no corpus evidence: the analogue finder's real use case |
| Sanity case | Ecuador | Your example; low prevalence (0.7%), tests that the tool does not over-claim |

Six of these are also on the WHO/UNICEF Global Action Plan front-runner list, which
gives the registry an obvious first source.

### 4.2 Phases and checkpoints

| Phase | Deliverable | Checkpoint |
|---|---|---|
| **P0 · Scope** (now) | This plan; your answers to the decisions in §6 | You approve the PoC scope |
| **P1 · Country data layer** | `countries.py`, four fetch clients, indicator catalogue, `profile.py`; 12 profile JSON files with provenance; one rendered Markdown profile (India) | Every number in the India profile traceable to an API response in the cache |
| **P2 · Evidence + registry** | `evidence_link.py` producing per-country evidence cards from the existing corpus; registry seeded for the 12 countries with source URLs, status `unverified` unless checked | Evidence cards for Ethiopia and Malawi read correctly against the CARE synthesis |
| **P3 · Analogue finder** | `similarity.py`, default + platform weight sets; a table "target → top-3 analogues with domain breakdown" for the five evidence-poor countries | Face-validity review with Liz: do the analogues make sense to someone who knows these programmes? |
| **P4 · Decide** | Short write-up of what worked, what the profiles got wrong, cost of scaling | Go / no-go on: full 126-country build; dedicated wasting retrieval block; starting the transport methods |

Rough effort: P1 and P2 are one working session each; P3 is half a session. Nothing in
the PoC calls PubMed or OpenAlex, so it is cheap and fast to re-run.

### 4.3 Success criteria

- Reproducible: `python3 atlas/code/build_atlas.py --poc` rebuilds all 12 profiles from cache in under a minute.
- Grounded: every numeric field has source, indicator code, year and retrieval date; a spot-check of 20 random values against the source API matches.
- Honest about gaps: missing indicators appear as explicit nulls with a reason, never as imputed values; old survey years are flagged.
- Useful: for at least three of the five evidence-poor countries, the top analogue is one a domain expert would also have picked, and the domain breakdown explains why.
- Does not over-claim: Ecuador's profile shows low burden and the finder says so rather than forcing analogues.

### 4.4 Explicitly out of scope for the PoC

- New literature retrieval (the wasting prevention block) — decided at P4.
- Effect transport, bias adjustment, simulation — design note only (§5).
- Scraping programme sources; the registry is hand-seeded.
- A web UI. Markdown profiles are enough to judge the content; an HTML atlas can come once the content is trusted.

---

## 5. Later stages: effect transport and simulation (design sketch)

This is the part with real methodological risk, so it stays a design note until the
profiles exist. Three ideas, in the order I would try them.

**5.1 Setting-aware meta-regression (most feasible, uses only what we have).**
Each corpus effect estimate is tagged with a country and a year; the atlas gives that
country-year a covariate vector (baseline prevalence, CHW density, UHC index, and so
on). A meta-regression of effect size on setting covariates then *predicts* the effect
at a target country's covariates, with a prediction interval that widens as the target
moves away from the studied settings. This turns "similar profile" from a qualitative
match into a quantitative extrapolation, and it makes explicit when a target is outside
the support of the evidence.

**5.2 Combining trial and observational effects with a bias variance.**
The failure mode to avoid: a large local observational study looks precise, so naive
inverse-variance weighting hands it almost all the weight. The fix is to inflate its
variance with a bias term before weighting:

```
w_rct ∝ 1 / se_rct²
w_obs ∝ 1 / (se_obs² + τ_bias²)
θ̂     = (w_rct · θ_rct_transported + w_obs · (θ_obs − b̂)) / (w_rct + w_obs)
```

`τ_bias²` and the bias correction `b̂` are not guessed: they are estimated on the
country-intervention pairs where the corpus holds *both* a trial and an observational
estimate (a calibration set), then applied where only one exists. This is the logic of
the shrinkage and calibration estimators in the recent data-integration literature
(Rosenman et al.; Kallus, Puli and Shalit; Yang et al.; the Colnet et al. review), kept
simple enough to run in the standard library. The corpus already has 56 RCT and 237
observational effect rows on wasting outcomes, so a calibration set is plausible.

**5.3 LLM-integrated simulation.**
A small cohort model of the wasting pathway (incidence → detection → admission →
recovery / default / death, in the style of the Lives Saved Tool) does the arithmetic.
The language model's job is bounded: turn a profile plus a policy scenario into a
structured, cited set of assumptions (coverage ramp, platform constraint, commodity
cost), never to produce the outputs. The verifier lints every assumption back to the
profile or the corpus, exactly as it lints a synthesis today. This keeps the "no number
without a source" guarantee intact even in a forward-looking tool.

**Risks to state up front.** Matching on observed covariates says nothing about
unobserved effect modifiers, so similarity is a screening aid, not a transport
guarantee. Prevalence is a stock and wasting is a flow, so any burden-to-caseload
conversion needs an incidence correction that must itself be sourced. And the programme
registry will go stale unless someone owns it.

---

## 6. Decisions needed from you (recommended defaults in bold)

1. **Project name and folder.** **`atlas/`**, product name "Evidence Atlas". Alternatives: `country_profiles/`, `wasting_atlas/`.
2. **Country pool for the full build after the PoC.** **All 126 LMICs with a wasting estimate**, with burden category as a filter. Alternative: only the 54 at ≥ 5%.
3. **Evidence source for the PoC.** **Existing corpus only** (315 records); add the dedicated wasting retrieval block (treatment + prevention + implementation passes, mirroring `DEEPDIVE_BLOCKS`) at P4 if the PoC holds up.
4. **Registry seeding.** **Hand-seeded for 12 countries from official sources**, with LLM-drafted entries from corpus implementation findings clearly marked `unverified`. Alternative: skip the registry in the PoC and use the corpus's named-cadre and platform findings only.
5. **Similarity weights.** **Equal domain weights plus one platform-weighted variant** for the PoC; expert-elicited weights later.

Reply with any changes and I will start P1.
