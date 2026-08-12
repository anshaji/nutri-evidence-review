#!/usr/bin/env python3
"""Derive the highlighted review copy from the clean CARE report.

CARE_FINAL_REPORT.md is the single source of truth. This wraps the passages
that were changed by the August 2026 fact-check in ==...== so pandoc's `mark`
extension renders them as yellow highlight in Word.

Run:  python3 make_marked.py && bash render.sh
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "CARE_FINAL_REPORT.md")
DST = os.path.join(HERE, "CARE_FINAL_REPORT_MARKED.md")

# Passages corrected after the independent fact-check. Order does not matter;
# each must appear verbatim in the clean report exactly once.
CORRECTED = [
    # §2 — at-a-glance table
    "different formulations recover children equally well at high certainty, though standard RUTF reduces relapse (RR 0.84)",
    "Cohort data put severe wasting at **11.6× the mortality hazard** of children with normal weight-for-height",
    "an intermediate contact intensity of four to eight visits may work best",
    "Any reduction in perinatal or neonatal mortality — both null at high certainty. Maternal mortality is also null but imprecise (RR 1.06, 0.72–1.54) and not GRADE-rated",
    # §2 — prose
    "Roughly two in three children with severe wasting go untreated.",
    "children with normal weight-for-height** (pooled analysis of ten general-population cohorts, 53,809 children — these follow children in the community, and do not compare treated with untreated). Ready-to-use therapeutic food probably improves recovery over caregiver-prepared alternatives. Different RUTF formulations recover children equally well at high certainty — but standard RUTF also reduces relapse (RR 0.84, 0.72–0.98), so substituting formulation to save money is not cost-free.",
    "and one of the two leading protocols holds recovery.** In a 2025 three-arm trial in Niger, the combined SAM/MAM protocol (ComPAS, 50% less therapeutic food) met non-inferiority on both intention-to-treat and per-protocol analysis; the tapered-dose protocol (OptiMA, 32% less) met it only on intention-to-treat.",
    "Separately, a reduced-dose trial in Burkina Faso found a small negative effect on height gain velocity, more pronounced under 12 months.",
    "The population is preterm or low-birth-weight infants — roughly one birth in seven worldwide, and closer to one in four in South Asia. Two things bound how far the headline result travels: almost all the pooled trials started kangaroo care *after* the infant was stabilised, and the landmark WHO trial, which tested starting it immediately, enrolled only infants of 1.0–1.799 kg, compared against kangaroo care after stabilisation rather than against none, and was stopped early for benefit. WHO recommends 8–24 hours a day, as many as possible.",
    "The packages that cut neonatal mortality by a quarter vary widely — women's groups and participatory learning, community health worker home visits, training of birth attendants, home-based newborn care — with breastfeeding support one element among several, so that benefit belongs to the package rather than to counselling alone. It is also a random-effects average across heterogeneous trials. Cochrane's 116-trial review **detected no differential effect by who delivers support** — professionals, peers or a combination — though it notes power was limited, so this is absence of evidence rather than demonstrated equivalence. Contact intensity looks like it matters, with four to eight visits the tentative optimum.",
    "These are three of 26 subgroups examined and the interaction tests are borderline, so they indicate where benefit is likely to be greatest rather than settling the question.",
    "a narrower question remains, since MMS formulations often contain less iron than the iron-folic acid they replace",
    # §2 — MMS certainty, corrected in the final fact-check
    "small-for-gestational-age RR 0.92, moderate certainty",
    "Its advantage over iron-folic acid is established on low birthweight at high certainty and on small-for-gestational-age at moderate certainty; no mortality outcome shows a benefit at any certainty.",
    # §3 — cost
    "against **US$1,344** for the inpatient standard of care in the same study — a roughly fiftyfold difference, because that comparison captures health outcomes as well as cost (Puett et al., *Health Policy and Planning* 2013;28(4):386–99)",
    "in the base case of a decision-tree model, rising to $493 under worst-case assumptions",
    "$145.50 per child cured against $320",
    "therapeutic food was 43% of institutional cost in the community programme there, while personnel were 47% of institutional cost inpatient",
    "Producing an MMS tablet costs roughly half a US cent more than an iron-folic acid tablet — about **$0.9 more across the 180 tablets of a pregnancy**. Procurement prices give a gap of the same order, around $1.4.",
    # §4 — targeting
    "of 13.9%",
    "(2019–21 survey)",
    "with northern Nigeria, Niger and Burkina Faso well above the sub-Saharan African average — Nigeria and Niger at roughly double it —",
    "Nigeria's 11.6% national figure",
    # §5 — implementation
    "— a stark contrast, though the community arm rests on a small number of detected cases and a single-NGO comparison",
    "relapse to acute malnutrition, moderate or severe",
    "in children with severe wasting — a conditional recommendation on moderate-certainty evidence, contingent on cost. It",
    "lifted exclusive breastfeeding to **87.6% in intensive areas against 53.5% elsewhere in Bangladesh**, and 57.8% against 28.4% in Viet Nam. Against baseline, that is an impact of 36.2 percentage points (21.0–51.5) and 27.9 points (17.7–38.1) respectively,",
    # §7 — normative status
    "It keeps dosing indexed to body weight — though it lowered the range to 150–185 kcal/kg/day and now endorses stepping down to 100–130 once a child is no longer severely wasted — and it retains dual discharge criteria. The leading simplified protocols dose by severity rather than weight and mostly discharge on MUAC alone,",
]

BANNER = """# 1. What was asked

**==Review copy.==** ==Passages highlighted in yellow were corrected after an independent fact-check against primary sources. This markup is for internal review only — the clean version, `CARE_FINAL_REPORT.docx`, is the one to send to CARE.=="""


def main():
    text = open(SRC).read()
    missing = [c for c in CORRECTED if c not in text]
    if missing:
        for m in missing:
            print(f"  MISSING: {m[:90]}…", file=sys.stderr)
        sys.exit(f"{len(missing)} passage(s) no longer match {os.path.basename(SRC)} — update CORRECTED.")
    for c in CORRECTED:
        text = text.replace(c, f"=={c}==", 1)
    text = text.replace("# 1. What was asked", BANNER, 1)
    open(DST, "w").write(text)
    print(f"wrote {os.path.basename(DST)} — {len(CORRECTED)} passages highlighted")


if __name__ == "__main__":
    main()
