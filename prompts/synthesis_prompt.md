# Stage 4 Synthesis Prompt & Grounding Checklist

This is the contract for the manual, in-conversation evidence synthesis. It
encodes the hardening rules from the VAS validation audit. Follow every rule;
when reviewing the synthesis, run `verify_synthesis.py` as the automated check
of rules G2/G3.

## Inputs
- `top_papers_for_review.json` — Phase 1 top 200 (metadata, MeSH, full text where available)
- `cea_by_intervention.json` — Phase 2 CEA evidence, per shortlisted intervention

## Task
1. Identify distinct interventions for **children under 5** and **women of reproductive age** in LMICs; group variants under one heading.
2. Rate each on three dimensions:
   - **Evidence strength (A/B/C)** — number/quality of meta-analyses, consistency, study-type hierarchy.
   - **Cost-effectiveness** — *only* from Phase 2 CEA data (see CEA-rating guard below).
   - **Scalability** — evidence of national/subnational implementation, platform fit.
3. Rank into Tier 1 / 2 / 3.
4. For each intervention: evidence rating + justification, effect sizes with CIs, mechanism, government scaling pathway, key supporting PMIDs.
5. Cross-cutting findings (4–6 patterns).
6. Summary table.

## Grounding rules (HARD — from the VAS audit)

**G1 — Study type is verbatim, never inferred.**
State each paper's study type and source from its `journal` + `publication_type`
fields *exactly*. Never call something a "Cochrane review" unless
`journal == "Cochrane Database of Systematic Reviews"`. (Imdad 2011 is a *BMC
Public Health* CHERG meta-analysis — not Cochrane.)

**G2 — Every numeric claim needs a corpus PMID.**
Any effect size, percentage, cost, or count must cite a PMID that exists in the
provided corpus. If you cannot point to a corpus PMID, write `not in corpus`
and do not state the number. Do **not** import figures from background knowledge
(e.g. "$1–3 per child", "823,000 deaths" — the latter is the Lancet
*Breastfeeding* series, PMID 26869575, not vitamin A).

**G3 — Cite the PMID that actually contains the number.**
The cited paper's own abstract/full text must support the specific value. Don't
pin a real figure onto a plausible-but-wrong PMID.

**G4 — Separate all-cause from cause-specific evidence.**
Report all-cause outcomes separately from cause-specific ones (diarrhoea,
measles, etc.). Flag cause-specific pathways that are underpowered or
inconsistent rather than blending them into the headline.

**G5 — Report both fixed/random estimates and name the dominant trial.**
When a meta-analysis reports diverging fixed- vs random-effect estimates, give
both and name the trial driving the divergence and its weight if the review
identifies it (e.g. DEVTA holds ~62% of the fixed-effect weight in the VAS
all-cause estimate).

**G6 — Version is not evidence.**
Cochrane review updates sharing one accession (e.g. CD008524, 2017 & 2022) are
the **same review**, not independent evidence generations. Phase 1's Cochrane
dedup collapses these; do not re-inflate robustness by counting versions.

## CEA-rating guard (#2b — HARD)

Assign a cost-effectiveness rating **only** if that intervention's record in
`cea_by_intervention.json` has `cea_rating_allowed == true` (i.e. ≥1 `cea_papers`
or ≥1 `registry_matches`). Otherwise the rating is **`Unknown`** — state that
explicitly. Never rate cost-effectiveness from background knowledge or from the
evidence (Phase 1) corpus, which contains no CEAs by design.

## Output
- `INTERVENTION_SYNTHESIS.md` — abstract-only synthesis
- `FULL_INTERVENTION_SYNTH.md` — full-text-enhanced synthesis (effect sizes, subgroups)

After writing, run `python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md`
and resolve every `NOT_IN_CORPUS` / `NEEDS_REVIEW` / unsourced flag.
