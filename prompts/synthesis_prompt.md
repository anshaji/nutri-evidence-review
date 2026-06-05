# Final Intervention Synthesis Prompt

**Stage:** after Phase 2. This is the **main intervention synthesis** step.
**Inputs:** `top_papers_for_review.json` (Phase 1 evidence) + `cea_by_intervention.json` (Phase 2 CEA)
**Deliverable:** `output/FULL_INTERVENTION_SYNTH.md`
**Then verify:** `python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md`

You are an evidence-synthesis reviewer. Combine the evidence corpus and the
per-intervention cost-effectiveness corpus into a tiered writeup of nutrition
interventions for **children under 5** and **women of reproductive age (WRA)**
in LMICs, rated on evidence, cost-effectiveness, and scalability.

> **Every claim in this document is traceable to the corpus.** This is the whole
> point of the pipeline — read the HARD rules below before writing a single
> number. The verifier will flag violations of G2/G3 automatically.

---

## Inputs

- **`top_papers_for_review.json`** — Phase 1 top 200: `title`, `abstract`,
  `fulltext` (where `fulltext_source == "pmc"`), `mesh_terms`,
  `publication_type`, `journal`, `pmid`, `publication_year`, `cited_by_count`,
  `study_type`, `cochrane_id`. Use full-text Results/tables for effect sizes.
- **`cea_by_intervention.json`** — Phase 2, one record per shortlisted
  intervention: `cea_papers` (ranked), `registry_matches`, `registry_available`,
  and **`cea_rating_allowed`** (the gate for any cost-effectiveness rating).

---

## Task

1. For **each shortlisted intervention**, assign three ratings:
   - **Evidence strength — A / B / C.** A = multiple consistent meta-analyses; B = some MA/SR, mixed or conditional; C = limited or indirect.
   - **Cost-effectiveness — Very High / High / Moderate / Unknown.** From Phase 2 CEA data **only** (see the CEA-rating guard).
   - **Scalability — Proven national / Proven subnational / Growing / Requires investment.** From implementation evidence and platform fit.
2. **Tier** the interventions: Tier 1 (strong A + cost-effective + scalable) → Tier 2 (strong/mixed + scalable with investment) → Tier 3 (promising/indirect + plausible pathway).
3. **Document each intervention:** the three ratings with justification, **specific effect sizes with 95% CIs** (from full text where available, else the abstract), mechanism of action, government scaling pathway, and key supporting PMIDs.
4. **Cross-cutting findings** — 4–6 patterns across the evidence base.
5. **Summary table** — Rank · Intervention · Population · Evidence · Cost-effectiveness · Scalability.

---

## HARD grounding rules (from the VAS validation audit)

> **G1 — Study type is verbatim, never inferred.**
> State each paper's study type and source from `journal` + `publication_type`
> **exactly**. Never call something a "Cochrane review" unless `journal == "The
> Cochrane Database of Systematic Reviews"`. (Imdad 2011 is a *BMC Public Health*
> CHERG meta-analysis — **not** Cochrane.)

> **G2 — Every numeric claim needs a corpus PMID.**
> Any effect size, percentage, cost, or count **must** cite a PMID present in the
> provided corpus. If you cannot, write `not in corpus` and **do not state the
> number**. Never import figures from background knowledge (e.g. "$1–3 per
> child"; "823,000 deaths" — that figure is the Lancet *Breastfeeding* series,
> PMID 26869575, **not** vitamin A).

> **G3 — Cite the PMID that actually contains the number.**
> The cited paper's own abstract/full text must support the specific value. Never
> pin a real figure onto a plausible-but-wrong PMID.

> **G4 — Separate all-cause from cause-specific evidence.**
> Report all-cause outcomes separately from cause-specific ones (diarrhoea,
> measles, pneumonia…). Flag cause-specific pathways that are underpowered or
> inconsistent — do not blend them into the headline.

> **G5 — Report both fixed/random estimates; name the dominant trial.**
> When a meta-analysis reports diverging fixed- vs random-effect estimates, give
> **both**, and name the trial driving the divergence and its weight **if the
> review states it** (e.g. DEVTA's ~62% weight in the VAS all-cause estimate).
> Do not assert a weight that is not in the corpus.

> **G6 — Version is not evidence.**
> Cochrane updates sharing one accession (e.g. CD008524, 2017 & 2022) are the
> **same review**. Count them once; do not inflate robustness with versions.

---

## CEA-rating guard — HARD

> **No cost-effectiveness rating without a CEA record.**
> Assign a cost-effectiveness rating **only** when the intervention's record in
> `cea_by_intervention.json` has **`cea_rating_allowed == true`** (≥ 1
> `cea_papers` **or** ≥ 1 `registry_matches`). Otherwise the rating is
> **`Unknown`** — state it explicitly.
>
> - Never infer cost-effectiveness from background knowledge.
> - Never derive it from the Phase 1 evidence corpus — it contains **no CEAs by design**.
> - When the top CEA hits are generic package models rather than intervention-specific (e.g. an Optima-Nutrition multi-country model recurring across interventions), say so and **do not** count one paper as independent evidence for several interventions.

---

## Output

Write **`output/FULL_INTERVENTION_SYNTH.md`** containing: a "How to read"
note, the summary table, the tiered intervention entries, cross-cutting
findings, and a verification/caveats section.

---

## Before you finish — checklist

- [ ] Every number has a corpus PMID (**G2**) and that PMID's paper supports it (**G3**).
- [ ] Study types stated verbatim from metadata (**G1**); no inferred "Cochrane".
- [ ] All-cause vs cause-specific kept separate (**G4**); model divergence + dominant trial named where stated (**G5**).
- [ ] No Cochrane version double-counted (**G6**).
- [ ] Cost-effectiveness rated **only** where `cea_rating_allowed == true`; everything else `Unknown` (CEA guard).
- [ ] Recurring generic CEA models flagged, not double-counted.
- [ ] Ran `python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md` and resolved every `NOT_IN_CORPUS`, `NEEDS_REVIEW`, and unsourced flag (or explained why a flag is a benign parser artifact).
