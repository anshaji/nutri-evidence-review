# Methods Paper Plan — LLM-Assisted Rapid Evidence Review

**Working title (option A, method-forward):**
*Query, Extract, Ground, Verify: A Reproducible Architecture for LLM-Assisted Rapid Evidence Review*

**Working title (option B, contrast-forward):**
*Rapid Reviews Without the Shortcuts: Replacing Scope Restriction with Machine-Scale Screening and Claim-Level Verification*

**Status:** plan only. Nothing drafted. Read alongside `PROCESS_deepdive.md`
(the method as actually run) and `../../docs/PROCESS_main_pipeline.md`.

---

## 1. The core argument

Traditional rapid reviews buy speed by **restricting scope**: fewer databases,
single-reviewer screening, no dual extraction, narrower date windows, grey
literature dropped. Every one of those is a deliberate, documented reduction in
rigour, and the resulting reviews are explicitly positioned as weaker than a
full systematic review.

Our approach buys speed differently. It does **not** narrow the corpus — it
screens and extracts at a scale a human team could not, then spends the saved
effort on a step traditional reviews cannot afford: **claim-level verification
of every number in the synthesis against its source**.

> **The thesis in one sentence.** Where a traditional rapid review trades
> *coverage* for speed, an LLM-assisted review can hold coverage constant and
> instead trade *human reading* for speed — provided the loss of human reading is
> compensated by structured extraction and automated claim verification.

That proviso is the paper. An LLM synthesis without grounding and verification
is *worse* than a rapid review, because it fails silently and fluently. The
contribution is not "we used an LLM" — it is the **architecture that makes an LLM
synthesis auditable**.

---

## 2. What is genuinely novel (and what is not)

**Be honest in the paper about this split — reviewers will probe it.**

| Claim | Novelty | Notes |
|---|---|---|
| Using LLMs for screening/extraction | ❌ Not novel | Active literature since ~2023. We must cite and position against it. |
| Query-driven retrieval with MeSH/population chokepoints | ❌ Not novel | Standard IR practice. |
| **Per-study structured extraction into a typed evidence DB, then synthesis *only* from that DB** | ⚠️ Partly novel | The discipline of never letting the model synthesise from raw text is the point. |
| **Automated claim-level verification with a `NOT_IN_CORPUS` flag** | ✅ Novel contribution | Every numeric claim is linted against the retrieved corpus + full text + extracted outcomes. This is the falsifiable safety property. |
| **A retrieval pass targeted at implementation outcomes, with its own study-type filter** | ✅ Novel contribution | Implementation evidence lives in program evaluations and qualitative work, which efficacy-shaped queries and design-hierarchy ranking systematically bury. |
| **Documented failure taxonomy from a real audit (the VAS case)** | ✅ Contribution | Empirically grounded, not hypothetical. |
| The specific nutrition findings | ❌ Out of scope | This is a methods paper. Findings are illustration only. |

---

## 3. How this differs from a traditional rapid review — the paper's central table

This table is the spine of the paper. Draft it early.

| Dimension | Traditional rapid review | This method |
|---|---|---|
| **Speed mechanism** | Restrict scope (fewer databases, dates, languages, grey lit) | Restrict *human reading*, not corpus |
| **Screening** | Single reviewer, often title/abstract only | Every retrieved record screened by LLM against explicit criteria; `on_topic` flag on every record |
| **Corpus size** | Typically 10²; deliberately capped | 10³ routinely (1,636 here); cap is compute, not attention |
| **Full text** | Often abstract-only for speed | Retrieved for every record where legally available (981/1,636 = 60% here) |
| **Extraction** | Single extractor, no duplication | One agent per token-balanced batch, typed schema, validated against JSON Schema |
| **Synthesis input** | Reviewer's reading + notes | **Only** the structured evidence DB — never raw text |
| **Claim provenance** | Narrative citation; spot-checked at best | Every number linted against corpus/full text/extracted outcomes |
| **Failure mode** | Missed studies (visible gap) | Fabricated or misattributed numbers (**invisible** without verification) ← the risk this architecture exists to close |
| **Reproducibility** | Search strategy reported; screening judgments not recoverable | Queries, cached API responses, per-paper cards, per-batch outputs, prompts all persisted |
| **Wall-clock** | Weeks to months | Days |
| **What is *worse*** | — | No dual human extraction; extraction fidelity bounded by model; language limits persist |

**The honest framing:** this is not "better than a systematic review." It is a
*different trade*, with a *different failure mode*, and the failure mode is
dangerous precisely because it is fluent. The verification layer is the price of
admission.

---

## 4. The architecture as the unit of contribution

Present it as a pipeline with named, separable stages so others can adopt parts:

```
PICOS spec (human)
   → Retrieval          queries at chokepoints; clinical + IMPLEMENTATION passes
   → Relevance check    HUMAN-IN-THE-LOOP checkpoint (§5 — this earned its keep)
   → Corpus assembly    dedup incl. version-collapse
   → Full text          PMC + OA fallback
   → Cards + batching   token-balanced, one self-contained card per paper
   → Extraction         1 agent/batch → typed records (idempotent, resumable)
   → Merge + validate   schema conformance, coverage cross-check
   → Synthesis          from the evidence DB ONLY, under grounding rules
   → Verification       lint every number → NOT_IN_CORPUS / unsupported / unsourced
   → Assembly
```

**Four design principles worth naming as such** (these generalise beyond nutrition):

1. **Synthesis reads the database, not the papers.** Forces every claim through a
   typed, inspectable intermediate.
2. **Grounding rules are explicit and testable** — study design verbatim from
   metadata; all-cause vs cause-specific separated; fixed *and* random reported;
   version ≠ evidence (shared accession = one review).
3. **Verification is adversarial and automated** — the reviewer does not have to
   trust the model; the linter checks it.
4. **Agent tasks are idempotent and file-writing** — what made a 112-batch,
   session-limited extraction recoverable. A practical contribution for anyone
   running LLM pipelines at scale.

---

## 5. Empirical evidence we already have

| Evidence | What it demonstrates | Where |
|---|---|---|
| **VAS audit** — a naive single-phase LLM synthesis produced a CEA rating with zero CEAs in corpus; imported "823,000 deaths" from training data (actually a *Breastfeeding* series figure); mislabelled a *BMC Public Health* MA as Cochrane; double-counted two versions of one Cochrane review | **The failure taxonomy.** Every fix in the architecture maps to one of these. This is the paper's motivating case. | `docs/PROCESS_main_pipeline.md` |
| **DEVTA detection** — pipeline surfaced that DEVTA held 65.2% of pooled weight, fixed RR 0.88 vs random 0.76, without being asked | Structured extraction recovers dominant-trial/heterogeneity signals a rapid review would miss | full-corpus run |
| **WHO technical correction catch** — full-text extraction surfaced that a widely-cited MMS neonatal-mortality safety signal had been *overturned* (corrected RR 1.05 vs original 1.22); an abstract-only review would have propagated the stale caveat | Full-text extraction changes conclusions, not just confidence | `CARE_DEEPDIVE_REVIEW.md` |
| **Twin-publication detection** — two 2020 papers with identical estimates identified as one evidence base | Automated double-counting control | same |
| **Verifier outcomes** — 639 claims / 0 not-in-corpus (full corpus); 130 claims / 0 not-in-corpus (deep-dive) | The safety property holds in practice | both runs |
| **Implementation-pass yield** — 630/648 on-topic records (97%) carried implementation findings | The targeted pass works; these records exist and are retrievable | deep-dive |
| **The BF facility/community finding** — two supposedly distinct queries returned near-identical top-lists, showing the distinction is *not retrievable* and must be extracted per study | A transferable methodological result about what queries can and cannot separate | §2.2 of `PROCESS_deepdive.md` |

---

## 6. What we do NOT yet have — and must, before submission

This is the gap between "interesting write-up" and "publishable methods paper."
**A reviewer's first question will be: how do you know the extraction is right?**

| Gap | Why it matters | Proposed study |
|---|---|---|
| **No gold-standard benchmark** | The central validity question | Take 2–3 published Cochrane/Campbell reviews in scope. Run the pipeline on the *same* question. Compare: study inclusion (sensitivity/specificity vs their included list), extracted effect sizes (exact agreement on point estimate + CI), conclusions. **This is the single most important missing piece.** |
| **No human dual-extraction comparison** | Traditional reviews' quality anchor | Sample ~50 papers; have 2 humans extract independently; compute agreement (κ / ICC) human-vs-human and human-vs-LLM. If LLM-vs-human ≈ human-vs-human, that is a headline result. |
| **No inter-run reliability** | LLMs are stochastic | Re-run extraction on the same 100 papers ≥3×. Report field-level agreement. Stability of `on_topic`, effect sizes, and the new implementation fields. |
| **Verifier false-negative rate unknown** | We report 0 not-in-corpus — but what does the linter *miss*? | Adversarial injection: deliberately plant N fabricated/misattributed numbers into a synthesis; measure detection rate. **Without this the "0 not-in-corpus" claim is weak.** |
| **No cost/time accounting** | "Rapid" is a claim about resources | Log wall-clock, token cost, human-hours per stage. Compare with published rapid-review resourcing. |
| **Single domain** | Generalisability | At minimum discuss; ideally one out-of-domain pilot (e.g. an education or WASH question). |

**Recommendation:** the benchmark study (row 1) and the adversarial verifier test
(row 4) are non-negotiable. The rest can be limitations.

---

## 7. Proposed paper structure

1. **Introduction** — rapid reviews trade rigour for speed; LLMs promise speed but
   introduce a *fluent* failure mode; the open question is whether the trade can
   be restructured rather than merely accelerated.
2. **Background** — rapid review methodology (Tricco, Cochrane RR guidance,
   PRISMA); prior LLM-for-evidence-synthesis work; the gap: adoption is
   outpacing verification.
3. **Methods — the architecture** — the stage pipeline; the four design
   principles; grounding rules; the verification layer; the implementation pass.
4. **Validation** — the benchmark study; extraction agreement; inter-run
   reliability; adversarial verifier test; resource accounting.
5. **Worked application** — the CARE deep-dive as illustration (three
   interventions, dual outcome axis). Kept short; it is a demonstration, not the
   contribution.
6. **Failure taxonomy** — the VAS audit, each failure mapped to its structural
   fix. Strong, concrete, memorable section.
7. **What this cannot do** — no dual human extraction; extraction bounded by
   model capability; English-only; full-text availability ceiling (60% here);
   requires a human relevance checkpoint; not a systematic-review replacement.
8. **Reporting standard proposal** — a short PRISMA-style checklist extension for
   LLM-assisted reviews: model + version, prompts, verification results,
   inter-run reliability, human checkpoints. **Potentially the most-cited part.**
9. **Discussion / conclusion.**

---

## 8. Target venues

| Venue | Fit | Note |
|---|---|---|
| *Research Synthesis Methods* | **Best fit** | Methods-forward, receptive to synthesis innovation |
| *Systematic Reviews* (BMC) | Strong | Broad readership among review practitioners |
| *BMC Medical Research Methodology* | Good | Solid methods home |
| *Campbell Systematic Reviews* | Good | Social-policy angle fits the CARE application |
| *JMIR / npj Digital Medicine* | Alternative | If we lean harder on the AI-systems framing |

**Sequence:** CEGA working paper / SSRN preprint first (fast, citable, gets
feedback from the ScaleWorks partners), then journal submission.

---

## 9. Authorship + roles (to confirm)

- **Akash Shaji** — pipeline design and implementation, runs, drafting
- **Liz** — senior review, methodological framing
- CARE / Save the Children / Mercy Corps technical experts — acknowledgement, or
  co-authorship if they contribute to the validation design
- Confirm CEGA affiliation/attribution requirements early

---

## 10. Risks and how to handle them

| Risk | Handling |
|---|---|
| **"You just used ChatGPT to write a review"** | Lead with verification, not with the model. The `NOT_IN_CORPUS` linter and the failure taxonomy are the defence. Report model versions and prompts in full. |
| **Reproducibility challenge** (models change) | Persist everything: queries, cached API responses, cards, per-batch outputs, prompts. Report model + version. Acknowledge that exact reproduction is bounded by model availability — this is an honest limitation of *all* LLM-based methods and worth stating plainly. |
| **Benchmark shows poor agreement** | Then that is the finding, and it is publishable and useful. Do not design the validation to flatter the method. |
| **Ethics / conflict** | Method developed under a client engagement (CARE). Disclose. Keep the methods claims separable from the client findings. |
| **Scooped** | Field is moving fast. Preprint early. |

---

## 11. Immediate next steps

1. **Confirm scope with Liz** — methods paper vs application paper vs both.
2. **Choose the benchmark reviews** (2–3 Cochrane/Campbell in nutrition). This
   gates the whole validation.
3. **Run the adversarial verifier test** — cheapest high-value experiment; can be
   done now on the existing corpus.
4. **Instrument resource accounting** into the pipeline (wall-clock + tokens per
   stage) before any further runs.
5. **Draft §3's comparison table and §6's failure taxonomy** — both are already
   evidenced and will clarify the argument for everyone.
6. Decide whether the CARE deep-dive is the worked example, or whether a cleaner
   purpose-built demonstration is needed.

---

## Appendix — quantitative material already available

- **Deep-dive funnel:** 1,671 retrieved → 1,636 unique → 981 full text (60%) →
  1,636 cards / 156 batches → 984 records → 648 on-topic → 130 verified claims.
- **Full-corpus run:** ~2,000 papers, 1,378 full text (69%), 23 interventions
  tiered, 639 claims / 0 not-in-corpus.
- **Schema conformance:** 1,000 records validated, 0 violations.
- **Implementation-pass yield:** 97% of on-topic records carry implementation findings.
- **Extraction throughput:** 112 batches, ~16 concurrent, ~10.6M input tokens.
- **Operational failure modes documented:** silent empty fan-out (args type
  coercion), session-limit fragmentation, batch-order vs evidence-value mismatch.
