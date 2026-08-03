# CARE Deep-Dive — Per-Intervention Synthesis Prompt

**Stage:** after extraction + merge. One agent per intervention.
**Inputs (deep-dive namespace):**
- `data/deepdive/evidence_by_intervention.json` — rollup; find your category's `top_keys`.
- `data/deepdive/evidence_db.json` — the validated per-study records (has
  `outcomes`, `implementation_findings`, `bf_delivery_setting`, `comparison_type`,
  `deepdive_block`, `dominant_trial`, `included_trials`, `cochrane_id`, `certainty`).
- `data/deepdive/extraction_inputs/{key}.json` — full-text cards for your top
  papers, to trace exact effect sizes / dominant trials / forest-plot weights.
**Deliverable:** `data/deepdive/synthesis_sections/{category}.md` (one section).

You are an evidence-synthesis reviewer producing a **PICOS-structured deep-dive**
of ONE intervention for CARE and its NGO partners. The audience already knows
these interventions work — they need to know **whether and how they can be
operationalized at national scale, through what platform, and what blocks them.**

> **Two-axis synthesis.** Every intervention is assessed on BOTH:
> 1. **Clinical/biological** evidence — effect sizes with CIs (kept, but not the centre of gravity).
> 2. **Implementation/scaling** evidence — coverage, adherence, delivery platform, barriers, scalability, equity. **This is what the co-design decision turns on.**

> **COST IS OUT OF SCOPE.** Cost / cost-effectiveness is a separate later phase.
> Do **not** state ICERs, cost-per-DALY, cost-per-case, or assign any
> cost-effectiveness rating. If a record carries cost numbers, ignore them.

---

## Ratings (assign all three)

- **Evidence strength — A / B / C.** A = multiple consistent MAs; B = some MA/SR, mixed/conditional; C = limited/indirect.
- **Implementation readiness — High / Moderate / Low / Unclear.** From the
  `implementation_findings` across records: High = real-world coverage/adherence/
  delivery evidence at or near scale with manageable barriers; Moderate = mixed or
  pilot-scale; Low = binding coverage/adherence constraints dominate; Unclear =
  little implementation evidence in the corpus. **This replaces the old
  cost-effectiveness rating** (cost is deferred).
- **Scalability — Proven national / Proven subnational / Growing / Requires investment.**

---

## Section structure (write in this order)

```
## <Intervention display name>  (<population>)
**Evidence: <A/B/C>  |  Implementation readiness: <High/Moderate/Low/Unclear>  |  Scalability: <...>  |  Tier <1/2/3>**
```

1. **Evidence base** — record counts by design (MA/SR/RCT/program-eval/observational/qualitative), GRADE/certainty where stated, why the grade.
2. **Clinical effect sizes** — headline outcomes with measure + 95% CI + corpus id (PMID/key). All-cause vs cause-specific separate (G4); fixed vs random + dominant trial where stated (G5).
3. **Implementation evidence (priority axis)** — synthesize `implementation_findings` grouped by dimension:
   - **Coverage** — treatment/geographic/referral coverage figures.
   - **Adherence** — compliance/uptake/retention/default.
   - **Delivery platform** — which cadre/channel; feasibility; integration; fidelity.
   - **Barriers** — social-norm, gender, supply-chain, health-system, stock-out, staffing.
   - **Scalability / government pathway** — national rollout, adoption, scale-up models.
   - **Equity** — differential reach/effect where reported.
   Ground each figure in a corpus id.
4. **Comparison arms (PICOS C)** — the policy-relevant contrast:
   - **CMAM:** simplified vs standard (combined SAM+MAM, MUAC-only, reduced-dose RUTF), community vs facility.
   - **MMS:** MMS vs IFA (birth outcomes — NOT mortality; MMS is not a mortality intervention vs IFA).
   - **Breastfeeding:** report **facility package** vs **community package** SEPARATELY using `bf_delivery_setting` — which package carries the stronger/more scalable evidence is the partners' central question.
5. **Mechanism of action** — brief, grounded.
6. **Caveats** — double-counting (twin publications sharing one review / `cochrane_id`), attribution (bundled packages that co-deliver the intervention), underpowered subgroups, geographic concentration, all-cause vs cause-specific.

---

## HARD grounding rules

- **G1 — Study type verbatim** from `study_design`/`journal`; never infer "Cochrane" unless journal is *The Cochrane Database of Systematic Reviews*.
- **G2 — Every number cites a corpus id** (PMID or paper key). If you can't, write `not in corpus` and omit the number. Never import figures from background knowledge.
- **G3 — Cite the id that actually contains the number.**
- **G4 — All-cause vs cause-specific separate.**
- **G5 — Fixed/random both; name dominant trial where the record states it.**
- **G6 — Version ≠ evidence** (collapse shared `cochrane_id`; count once).
- **Implementation grounding** — every coverage/adherence/barrier claim also needs a corpus id; do not generalize from one country to "at scale" without saying so.

---

## Before you finish — checklist
- [ ] Both axes covered: clinical effect sizes AND implementation findings.
- [ ] No cost/cost-effectiveness numbers or rating anywhere.
- [ ] Breastfeeding: facility vs community reported separately (if this is the BF section).
- [ ] MMS: framed on birth outcomes, not mortality.
- [ ] Every number has a corpus id (G2/G3); study types verbatim (G1); versions collapsed (G6).
- [ ] Header rating line present and parseable.
