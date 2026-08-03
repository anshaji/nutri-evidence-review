"""Query definitions for all tracks.

Track A: PubMed meta-analyses and systematic reviews (two passes)
Track B: PubMed cost-effectiveness analyses
Track C: OpenAlex non-biomedical literature (cash transfers, social protection)
"""

# ── Shared PubMed Filters ───────────────────────────────────────────────────

LMIC_FILTER = (
    '("developing countries"[MeSH] OR "low income"[tiab] OR "middle income"[tiab] '
    'OR "LMIC"[tiab] OR "sub-saharan africa"[tiab] OR "south asia"[tiab] '
    'OR "southeast asia"[tiab])'
)

# Population filter: target children under 5 OR women of reproductive age.
# OR logic — a paper on EITHER population qualifies. Applied to every Track A
# sub-query via build_pubmed_query (Phase 1 evidence search).
POPULATION_FILTER = (
    '("infant"[MeSH] OR "child, preschool"[MeSH] '
    'OR "infant nutritional physiological phenomena"[MeSH] '
    'OR "pregnant women"[MeSH] OR "pregnancy"[MeSH] '
    'OR "maternal nutritional physiological phenomena"[MeSH] '
    'OR "reproductive health"[MeSH] '
    'OR "under-five"[tiab] OR "under 5"[tiab] OR "preschool"[tiab] '
    'OR "infant"[tiab] OR "neonatal"[tiab] OR "young child"[tiab] '
    'OR "women of reproductive age"[tiab] OR "reproductive age"[tiab] '
    'OR "pregnant"[tiab] OR "pregnancy"[tiab] OR "maternal"[tiab] '
    'OR "antenatal"[tiab] OR "prenatal"[tiab])'
)

# OpenAlex free-text equivalent of POPULATION_FILTER (Track C).
OPENALEX_POPULATION = (
    '("infant" OR "child" OR "preschool" OR "under-five" OR "young child" '
    'OR "pregnant" OR "pregnancy" OR "maternal" OR "antenatal" '
    'OR "women of reproductive age")'
)

# Pass 1: meta-analyses only
MA_FILTER = '(meta-analysis[pt] OR "Cochrane Database Syst Rev"[Journal])'

# Pass 2: systematic reviews (broader)
SR_FILTER = '(systematic review[pt] OR "systematic review"[tiab])'


# ── Track A: Intervention Queries (PubMed) ──────────────────────────────────

TRACK_A_QUERIES = [
    {
        "name": "micronutrient_supplementation",
        "terms": (
            '("micronutrients"[MeSH] OR "dietary supplements"[MeSH] '
            'OR "iron"[tiab] OR "zinc"[tiab] OR "vitamin a"[tiab] '
            'OR "folic acid"[tiab] OR "multiple micronutrient"[tiab])'
        ),
    },
    {
        "name": "food_fortification",
        "terms": (
            '("food, fortified"[MeSH] OR "flour fortification"[tiab] '
            'OR "salt iodization"[tiab] OR "biofortification"[tiab] '
            'OR "rice fortification"[tiab] OR "oil fortification"[tiab])'
        ),
    },
    {
        "name": "complementary_feeding",
        "terms": (
            '("infant nutritional physiological phenomena"[MeSH] '
            'OR "complementary feeding"[tiab] OR "weaning"[tiab] '
            'OR "infant food"[tiab])'
        ),
    },
    {
        "name": "breastfeeding_promotion",
        "terms": (
            '("breast feeding"[MeSH] OR "lactation"[MeSH] '
            'OR "kangaroo mother care"[tiab] OR "exclusive breastfeeding"[tiab] '
            'OR "breastfeeding promotion"[tiab])'
        ),
    },
    {
        "name": "acute_malnutrition_management",
        "terms": (
            '("severe acute malnutrition"[tiab] OR "moderate acute malnutrition"[tiab] '
            'OR "ready-to-use therapeutic food"[tiab] OR "RUTF"[tiab] '
            'OR "CMAM"[tiab] OR "community-based management"[tiab] AND "malnutrition"[tiab])'
        ),
    },
    {
        "name": "maternal_nutrition",
        "terms": (
            '("prenatal nutritional physiological phenomena"[MeSH] '
            'OR "maternal nutrition"[tiab] OR ("antenatal"[tiab] AND '
            '("nutrition"[tiab] OR "supplementation"[tiab])) '
            'OR "pregnancy supplementation"[tiab])'
        ),
    },
    {
        "name": "wash_nutrition",
        "terms": (
            '(("water purification"[MeSH] OR "hygiene"[MeSH] OR "sanitation"[MeSH] '
            'OR "WASH"[tiab]) AND ("nutrition"[tiab] OR "stunting"[tiab] '
            'OR "growth"[tiab] OR "undernutrition"[tiab]))'
        ),
    },
    {
        "name": "school_feeding",
        "terms": (
            '("school feeding"[tiab] OR "school meal"[tiab] '
            'OR "school nutrition"[tiab] OR "school food program"[tiab])'
        ),
    },
    {
        "name": "growth_monitoring",
        "terms": (
            '("growth monitoring"[tiab] OR "growth promotion"[tiab] '
            'OR "nutrition surveillance"[MeSH] OR "nutrition screening"[tiab])'
        ),
    },
    {
        "name": "deworming",
        "terms": (
            '(("anthelmintics"[MeSH] OR "deworming"[tiab] OR "albendazole"[tiab]) '
            'AND ("nutrition"[tiab] OR "growth"[tiab] OR "anemia"[tiab] '
            'OR "anaemia"[tiab]))'
        ),
    },
    {
        "name": "nutrition_sensitive_agriculture",
        "terms": (
            '(("agriculture"[MeSH] OR "homestead food production"[tiab] '
            'OR "nutrition-sensitive agriculture"[tiab]) AND '
            '("nutrition"[tiab] OR "diet"[tiab] OR "dietary diversity"[tiab]))'
        ),
    },
    {
        "name": "integrated_multisectoral",
        "terms": (
            '("nutrition programs and policies"[MeSH] OR "integrated intervention"[tiab] '
            'OR "multisectoral"[tiab] OR "nutrition-sensitive"[tiab] '
            'OR "nutrition-specific"[tiab])'
        ),
    },
]


def build_pubmed_query(query_def: dict, type_filter: str) -> str:
    """Construct full PubMed query string from components.

    Single chokepoint for all 24 Track A sub-queries: ANDs in the population
    filter (under-5 / women of reproductive age) and the LMIC filter.
    """
    return (f'{query_def["terms"]} AND {POPULATION_FILTER} '
            f'AND {LMIC_FILTER} AND {type_filter}')


def build_openalex_search(search_text: str) -> str:
    """AND the population clause into an OpenAlex free-text search (Track C)."""
    return f'({search_text}) AND {OPENALEX_POPULATION}'


# ── Phase 2: Cost-Effectiveness (PubMed, per shortlisted intervention) ──────
#
# Phase 1 deliberately excludes cost-effectiveness. In Phase 2 the CEA search
# is run targeted *per shortlisted intervention* — the intervention name (plus
# synonyms/MeSH from the shortlist) replaces the broad nutrition-noun half of
# the old Track B query, AND-ed with this cost-term skeleton.

CEA_TERM_SKELETON = (
    '("cost-benefit analysis"[MeSH] OR "cost-effectiveness"[tiab] '
    'OR "cost per DALY"[tiab] OR "cost-benefit"[tiab] '
    'OR "cost effective"[tiab] OR "incremental cost"[tiab] '
    'OR "cost-utility"[tiab])'
)


def build_cea_pubmed_query(intervention: dict) -> str:
    """Build a targeted PubMed CEA query for one shortlisted intervention.

    intervention: {"name": str, "synonyms": [str], "mesh": [str], ...}
    """
    name = intervention["name"]
    syns = intervention.get("synonyms", [])
    mesh = intervention.get("mesh", [])
    tiab_terms = [f'"{t}"[tiab]' for t in [name] + syns]
    mesh_terms = [f'"{m}"[MeSH]' for m in mesh]
    intervention_clause = "(" + " OR ".join(tiab_terms + mesh_terms) + ")"
    return f'{CEA_TERM_SKELETON} AND {intervention_clause} AND {LMIC_FILTER}'


def build_cea_openalex_search(intervention: dict) -> str:
    """Build a targeted OpenAlex CEA free-text search for one intervention."""
    name = intervention["name"]
    syns = intervention.get("synonyms", [])
    names = " OR ".join(f'"{t}"' for t in [name] + syns)
    return (
        '("cost-effectiveness" OR "cost per DALY" OR "cost-benefit" '
        'OR "cost-utility" OR "incremental cost") '
        f'AND ({names}) '
        'AND ("low-income" OR "LMIC" OR "developing")'
    )


# ── Track C: Non-Biomedical (OpenAlex) ─────────────────────────────────────

TRACK_C_QUERIES = [
    {
        "name": "cash_transfers_nutrition",
        "search": (
            '"cash transfer" AND ("nutrition" OR "child growth" OR '
            '"food security" OR "dietary diversity") AND '
            '("low-income" OR "LMIC" OR "developing countries") AND '
            '("meta-analysis" OR "systematic review" OR "evidence")'
        ),
    },
    {
        "name": "social_protection_nutrition",
        "search": (
            '"social protection" AND ("child nutrition" OR "food security" '
            'OR "malnutrition" OR "stunting") AND '
            '("low-income" OR "LMIC" OR "developing") AND '
            '("review" OR "meta-analysis" OR "evidence")'
        ),
    },
    {
        "name": "food_subsidies_pds",
        "search": (
            '("food subsidy" OR "public distribution system" OR '
            '"food assistance" OR "food voucher") AND '
            '("nutrition" OR "food security" OR "dietary") AND '
            '("low-income" OR "LMIC" OR "developing") AND '
            '("review" OR "evidence" OR "evaluation")'
        ),
    },
    {
        "name": "conditional_transfers_health",
        "search": (
            '("conditional cash transfer" OR "CCT") AND '
            '("nutrition" OR "child health" OR "growth" OR "anemia") AND '
            '("low-income" OR "LMIC" OR "developing") AND '
            '("meta-analysis" OR "systematic review" OR "impact evaluation")'
        ),
    },
]
