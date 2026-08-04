"""Deep-dive query layer — PICOS-targeted retrieval for the CARE workstream.

Owns the three intervention blocks and the implementation-pass filters. Reuses
the core pipeline's query chokepoints (build_pubmed_query / build_openalex_search)
so the population and LMIC filters are applied identically to the main pipeline.

Cost terms are deliberately absent — cost is Phase 2 (code/15_run_cea.py).
"""

from code.queries import (  # core pipeline primitives
    MA_FILTER, SR_FILTER, build_pubmed_query, build_openalex_search,
)

# ── CARE Deep-Dive: PICOS-targeted retrieval (Phase 1, EVIDENCE ONLY) ───────
#
# A focused retrieval for the 3 partner-selected interventions, disaggregated
# into 4 PICOS blocks (breastfeeding split facility vs community). This layer
# is SEPARATE from the broad 12-domain Track A above (which reproduces the
# original synthesis) — it does not replace it.
#
# Cost is deliberately NOT searched here: cost is Phase 2 (see build_cea_*).
# The novelty vs the original run is the IMPLEMENTATION axis — coverage,
# adherence, delivery platform, barriers — because partners told us
# adherence/coverage, not efficacy, is the binding constraint.
#
# Each block runs three passes through the SAME build_pubmed_query chokepoint:
#   - MA   pass:  intervention [AND setting]                      × MA_FILTER
#   - SR   pass:  intervention [AND setting]                      × SR_FILTER
#   - IMPL pass:  intervention [AND setting] AND IMPL_OUTCOMES    × IMPL_TYPE_FILTER
# so population + LMIC filters are applied identically to the main pipeline.

# Implementation OUTCOME vocabulary (content filter — NO cost terms; cost = Phase 2).
IMPL_OUTCOME_FILTER = (
    '("coverage"[tiab] OR "adherence"[tiab] OR "compliance"[tiab] '
    'OR "uptake"[tiab] OR "retention"[tiab] OR "default"[tiab] '
    'OR "implementation"[tiab] OR "scale-up"[tiab] OR "scale up"[tiab] '
    'OR "scaling up"[tiab] OR "delivery platform"[tiab] OR "feasibility"[tiab] '
    'OR "program evaluation"[tiab] OR "programme evaluation"[tiab] '
    'OR "process evaluation"[tiab] OR "barriers"[tiab] OR "facilitators"[tiab] '
    'OR "fidelity"[tiab] OR "health system"[tiab] '
    'OR "community health worker"[tiab])'
)

# Implementation STUDY-TYPE filter — widens beyond MA/SR to admit program
# evaluations, trials, cohorts, and qualitative barrier studies (the designs
# implementation evidence actually lives in).
IMPL_TYPE_FILTER = (
    '(randomized controlled trial[pt] OR "controlled clinical trial"[pt] '
    'OR clinical trial[pt] OR evaluation study[pt] OR comparative study[pt] '
    'OR multicenter study[pt] OR observational study[pt] '
    'OR "cluster randomi*"[tiab] OR "program evaluation"[tiab] '
    'OR "programme evaluation"[tiab] OR "implementation"[tiab] '
    'OR "process evaluation"[tiab] OR "mixed methods"[tiab] '
    'OR "qualitative"[tiab] OR "cohort"[tiab] OR "feasibility"[tiab] '
    'OR "cross-sectional"[tiab] OR "coverage survey"[tiab])'
)

DEEPDIVE_BLOCKS = [
    {
        "key": "cmam",
        "label": "Community-based Management of Acute Malnutrition (CMAM)",
        "intervention": (
            '("severe acute malnutrition"[tiab] OR "moderate acute malnutrition"[tiab] '
            'OR "acute malnutrition"[tiab] OR "severe wasting"[tiab] '
            'OR "child wasting"[tiab] OR "ready-to-use therapeutic food"[tiab] '
            'OR "RUTF"[tiab] OR "ready-to-use supplementary food"[tiab] OR "RUSF"[tiab] '
            'OR "lipid-based nutrient supplement"[tiab] OR "CMAM"[tiab] '
            'OR "community-based management of acute malnutrition"[tiab] '
            'OR "community management of acute malnutrition"[tiab] '
            'OR "outpatient therapeutic"[tiab] OR "therapeutic feeding"[tiab] '
            'OR "supplementary feeding"[tiab] OR "simplified approach"[tiab] '
            'OR "combined protocol"[tiab] OR "ComPAS"[tiab] OR "family MUAC"[tiab] '
            'OR "mid-upper arm circumference"[tiab])'
        ),
        "setting": None,
        # Phase-2 handoff (cost): name/synonyms/mesh for build_cea_pubmed_query.
        "synonyms": ["CMAM", "ready-to-use therapeutic food", "acute malnutrition",
                     "RUTF", "severe acute malnutrition"],
        "mesh": ["Malnutrition", "Child Nutrition Disorders"],
    },
    {
        # Single breastfeeding block. Retrieval can't cleanly separate facility
        # vs community (broad reviews cover both), so the facility/community
        # split (partner PICOS) is a per-study DELIVERY-SETTING tag applied at
        # extraction, not two overlapping retrievals. Anchored to BF as a MAJOR
        # topic ([Majr]) or a BF term in the title ([ti]) to kill the generic-
        # MNCH-package dilution seen in the first run.
        "key": "breastfeeding",
        "label": "Breastfeeding promotion & support (facility + community — split tagged at extraction)",
        "intervention": (
            '("breast feeding"[Majr] OR "breastfeeding"[ti] OR "breast feeding"[ti] '
            'OR "breast-feeding"[ti] OR "exclusive breastfeeding"[ti] OR "lactation"[ti] '
            'OR "skin-to-skin"[ti] OR "kangaroo mother care"[ti] OR "baby-friendly"[ti] '
            'OR "baby friendly"[ti] OR "BFHI"[ti])'
        ),
        "setting": None,
        # OpenAlex papers (no MeSH) are gated on this title regex; PubMed papers
        # already passed the precise [Majr]/[ti] query and are trusted.
        "title_anchor": r"breastfeed|breast[ -]?feed|lactation|exclusive breast|skin-to-skin|kangaroo|baby.?friendly|BFHI",
        "synonyms": ["breastfeeding", "exclusive breastfeeding", "breastfeeding counselling",
                     "baby-friendly hospital", "skin-to-skin"],
        "mesh": ["Breast Feeding"],
    },
    {
        "key": "mms",
        "label": "Antenatal Multiple Micronutrient Supplementation (MMS)",
        "intervention": (
            '("multiple micronutrient"[tiab] OR "multiple micronutrients"[tiab] '
            'OR "multiple micronutrient supplementation"[tiab] OR "MMS"[tiab] '
            'OR "UNIMMAP"[tiab] OR "antenatal micronutrient"[tiab] '
            'OR "prenatal micronutrient"[tiab] OR "iron-folic acid"[tiab] '
            'OR "iron and folic acid"[tiab] OR "iron folic acid"[tiab])'
        ),
        "setting": None,
        "synonyms": ["multiple micronutrient supplementation", "MMS", "UNIMMAP",
                     "antenatal micronutrient", "iron-folic acid"],
        "mesh": ["Micronutrients", "Dietary Supplements", "Prenatal Nutritional Physiological Phenomena"],
    },
]


def build_deepdive_terms(block: dict, include_impl: bool) -> str:
    """Assemble the `terms` clause for one deep-dive block.

    Returns intervention [AND setting] [AND IMPL_OUTCOME_FILTER]. The result is
    passed as query_def["terms"] to the existing build_pubmed_query chokepoint,
    which appends the population + LMIC + study-type filters.
    """
    parts = [block["intervention"]]
    if block.get("setting"):
        parts.append(block["setting"])
    if include_impl:
        parts.append(IMPL_OUTCOME_FILTER)
    return " AND ".join(parts)


# OpenAlex free-text equivalents (Track-C-style) for each block.
_BF_OPENALEX = (
    '("breastfeeding" OR "breast feeding" OR "exclusive breastfeeding" '
    'OR "lactation" OR "kangaroo mother care" OR "skin-to-skin")'
)
_DEEPDIVE_OPENALEX_INTERVENTION = {
    "cmam": (
        '("severe acute malnutrition" OR "acute malnutrition" '
        'OR "ready-to-use therapeutic food" OR "RUTF" OR "CMAM" '
        'OR "community-based management of acute malnutrition" '
        'OR "therapeutic feeding" OR "simplified approach")'
    ),
    "breastfeeding": _BF_OPENALEX,
    "mms": (
        '("multiple micronutrient" OR "antenatal micronutrient" '
        'OR "prenatal micronutrient" OR "UNIMMAP" OR "iron-folic acid")'
    ),
}
_DEEPDIVE_OPENALEX_SETTING = {}  # breastfeeding no longer setting-split at retrieval
_IMPL_OPENALEX = (
    '("coverage" OR "adherence" OR "implementation" OR "scale-up" '
    'OR "program evaluation" OR "feasibility" OR "barriers" '
    'OR "community health worker")'
)


def build_deepdive_openalex(block: dict, include_impl: bool) -> str:
    """Assemble the OpenAlex free-text search for one deep-dive block.

    The result is passed to build_openalex_search, which ANDs the population
    clause. No cost terms (cost = Phase 2).
    """
    parts = [_DEEPDIVE_OPENALEX_INTERVENTION[block["key"]]]
    setting = _DEEPDIVE_OPENALEX_SETTING.get(block["key"])
    if setting:
        parts.append(setting)
    if include_impl:
        parts.append(_IMPL_OPENALEX)
    return " AND ".join(parts)


