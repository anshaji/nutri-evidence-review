"""Deep-dive ranking — adds an implementation-relevance component.

Partners identified adherence/coverage (not efficacy) as the binding constraint,
so implementation evidence must be a first-class ranking signal rather than
something buried under study-design weighting.

`deepdive_score` is ADDITIVE over the core `score_paper`, so a paper strong on
both clinical and implementation grounds ranks highest. The core scorer is left
untouched — the main pipeline's ranking is unchanged.
"""

from code.models import Paper
from code.scoring import score_paper

# ── Implementation Relevance (0–12) ────────────────────
# Used ONLY by the CARE deep-dive (deepdive_score). Partners told us the
# binding constraint is adherence/coverage, not efficacy — so implementation
# evidence (program evaluations, coverage surveys, CHW-delivery studies) must
# be a first-class ranking signal, not buried under the study-design weighting
# that favours meta-analyses. This does NOT touch score_paper, so the original
# pipeline's ranking is unchanged. Cost terms are excluded (cost = Phase 2).

IMPLEMENTATION_MESH = {
    "Health Services Accessibility", "Patient Compliance", "Medication Adherence",
    "Program Evaluation", "Health Plan Implementation", "Community Health Workers",
    "Delivery of Health Care", "Health Care Reform", "Quality of Health Care",
    "Feasibility Studies", "National Health Programs",
}

IMPLEMENTATION_KEYWORDS = {
    "coverage": 3, "adherence": 3, "compliance": 3, "uptake": 2, "retention": 2,
    "default rate": 2, "implementation": 3, "scale-up": 3, "scale up": 3,
    "scaling up": 2, "delivery platform": 3, "feasibility": 2,
    "program evaluation": 3, "programme evaluation": 3, "process evaluation": 2,
    "barriers": 2, "facilitators": 2, "fidelity": 2, "health system": 2,
    "community health worker": 3, "operational": 2, "real-world": 2,
}


def score_implementation_relevance(paper: Paper) -> float:
    """Score how much a paper carries implementation/scaling signal (0–12)."""
    mesh = set(paper.get("mesh_terms", []))
    score = 0.0
    mesh_matches = mesh & IMPLEMENTATION_MESH
    if mesh_matches:
        score += min(len(mesh_matches) * 3, 6)
    text = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
    score += sum(pts for kw, pts in IMPLEMENTATION_KEYWORDS.items() if kw in text)
    return min(score, 12)


def deepdive_score(paper: Paper) -> float:
    """Deep-dive composite: base relevance + implementation relevance.

    Additive over score_paper so clinical strength and implementation strength
    both lift a paper — matching the dual-outcome PICOS (clinical + scaling).
    """
    return round(score_paper(paper) + score_implementation_relevance(paper), 1)
