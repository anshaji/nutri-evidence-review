"""Revised scoring algorithm using authoritative PubMed metadata.

For PubMed papers: uses publication_type field and MeSH terms for classification.
For OpenAlex papers: falls back to keyword heuristics (capped at lower scores).

Components:
1. Study Design Authority (0-20) — from publication_type
2. Topic Relevance (0-25) — from MeSH terms
3. Setting Relevance (0-10) — MeSH geographic terms
4. Recency (0-10) — publication year decay
5. Citation Impact (0-12) — cited_by_count brackets
6. Open Access (0-3) — accessibility bonus
7. Tier Bonus (0-5) — confirmed meta-analyses from Pass 1
8. Population Relevance (0-10) — under-5 / women-of-reproductive-age targeting

Max ≈ 95.
"""

from datetime import datetime
from .config import POPULATION_SCORE_MAX
from .models import Paper

CURRENT_YEAR = datetime.now().year


# ── Component 1: Study Design ─────���─────────────────────────────────────────

# Authoritative scores from PubMed publication_type field
PUBTYPE_SCORES = {
    "Meta-Analysis": 20,
    "Systematic Review": 17,
    "Randomized Controlled Trial": 14,
    "Review": 10,
    "Practice Guideline": 10,
    "Guideline": 10,
    "Clinical Trial": 8,
    "Comparative Study": 6,
    "Evaluation Study": 6,
    "Observational Study": 5,
}

# Keyword fallback for OpenAlex papers (capped lower)
KEYWORD_TYPE_SCORES = {
    "meta-analysis": 15,
    "umbrella review": 15,
    "cochrane": 14,
    "systematic review": 12,
    "cost-effectiveness": 10,
    "cost-effective": 10,
    "cost-benefit": 10,
    "randomized controlled trial": 8,
    "randomised controlled trial": 8,
    "evidence review": 7,
}


def score_study_design(paper: Paper) -> float:
    """Score based on publication_type (PubMed) or keyword fallback (OpenAlex)."""
    if paper.get("source_db") == "pubmed" and paper.get("publication_type"):
        # Use authoritative publication type — take the highest-scoring type
        return max(
            (PUBTYPE_SCORES.get(pt, 0) for pt in paper["publication_type"]),
            default=0,
        )
    else:
        # Keyword fallback for OpenAlex papers
        combined = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
        return max(
            (pts for kw, pts in KEYWORD_TYPE_SCORES.items() if kw in combined),
            default=0,
        )


# ── Component 2: Topic Relevance (MeSH-based) ──────────────────────────────

# Curated MeSH term sets for nutrition interventions
INTERVENTION_MESH = {
    "Micronutrients", "Dietary Supplements", "Food, Fortified",
    "Iron", "Zinc", "Vitamin A", "Folic Acid", "Iodine",
    "Breast Feeding", "Infant Nutritional Physiological Phenomena",
    "Child Nutrition Sciences", "Maternal Nutritional Physiological Phenomena",
    "Prenatal Nutritional Physiological Phenomena",
    "Nutritional Support", "Food Supply",
    "Anthelmintics", "Deworming",
    "Agriculture", "Food Assistance",
    "Nutrition Programs and Policies", "Nutrition Therapy",
    "Malnutrition", "Child Nutrition Disorders",
    "Infant Food", "Complementary Feeding",
}

OUTCOME_MESH = {
    "Nutritional Status", "Growth Disorders", "Malnutrition",
    "Wasting Syndrome", "Anemia", "Anemia, Iron-Deficiency",
    "Child Development", "Birth Weight", "Infant, Low Birth Weight",
    "Growth", "Body Height", "Body Weight",
    "Mortality", "Child Mortality", "Infant Mortality",
    "Diarrhea", "Respiratory Tract Infections",
    "Vitamin A Deficiency", "Iron Deficiencies",
    "Stunting",
}

# Keyword fallback for topic relevance (OpenAlex)
KEYWORD_TOPIC_SCORES = {
    "stunting": 4, "wasting": 4, "undernutrition": 4,
    "child nutrition": 4, "maternal nutrition": 4,
    "complementary feeding": 4, "micronutrient": 4,
    "malnutrition": 3, "anemia": 3, "anaemia": 3,
    "breastfeeding": 3, "supplementation": 3,
    "fortification": 3, "food security": 3,
}


def score_topic_relevance(paper: Paper) -> float:
    """Score based on MeSH terms (PubMed) or keyword fallback (OpenAlex)."""
    mesh = set(paper.get("mesh_terms", []))

    if mesh:
        score = 0.0
        # Intervention MeSH match
        intervention_matches = mesh & INTERVENTION_MESH
        if intervention_matches:
            score += min(len(intervention_matches) * 4, 12)
        # Outcome MeSH match
        outcome_matches = mesh & OUTCOME_MESH
        if outcome_matches:
            score += min(len(outcome_matches) * 3, 9)
        # Bonus for having both intervention AND outcome terms
        if intervention_matches and outcome_matches:
            score += 4
        return min(score, 25)
    else:
        # Keyword fallback for OpenAlex
        combined = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
        score = sum(pts for kw, pts in KEYWORD_TOPIC_SCORES.items() if kw in combined)
        return min(score, 20)  # Capped lower than MeSH-based


# ── Component 3: Setting Relevance ──��───────────────────────────────────────

SETTING_MESH = {
    "Developing Countries",
    "Africa South of the Sahara", "Africa, Eastern", "Africa, Western",
    "Asia, Southeastern", "Asia, Southern", "India",
    "Bangladesh", "Pakistan", "Nepal", "Ethiopia", "Nigeria",
    "Tanzania", "Kenya", "Uganda", "Mozambique", "Malawi",
    "Latin America", "Haiti",
}

SETTING_KEYWORDS = {
    "lmic": 5, "low-income": 4, "middle-income": 4,
    "developing countr": 4, "sub-saharan africa": 4,
    "south asia": 4, "southeast asia": 3,
}


def score_setting_relevance(paper: Paper) -> float:
    """Score LMIC setting relevance from MeSH or keywords."""
    mesh = set(paper.get("mesh_terms", []))

    if mesh:
        setting_matches = mesh & SETTING_MESH
        if setting_matches:
            return min(len(setting_matches) * 4, 10)
        return 0
    else:
        # Keyword fallback
        combined = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
        score = sum(pts for kw, pts in SETTING_KEYWORDS.items() if kw in combined)
        return min(score, 10)


# ── Component 4: Recency ────────────────────────────────────────────────────

def score_recency(paper: Paper) -> float:
    """Step function decay based on publication year."""
    pub_year = paper.get("publication_year")
    if not pub_year:
        return 1  # Unknown year → minimal credit

    age = CURRENT_YEAR - pub_year
    if age <= 5:
        return 10
    elif age <= 10:
        return 7
    elif age <= 15:
        return 4
    elif age <= 20:
        return 2
    else:
        return 0


# ── Component 5: Citation Impact ────────────────────────────────────────────

def score_citations(paper: Paper) -> float:
    """Log-scaled citation brackets."""
    cited = paper.get("cited_by_count", 0)
    if cited > 500:
        return 12
    elif cited > 200:
        return 10
    elif cited > 100:
        return 8
    elif cited > 50:
        return 6
    elif cited > 20:
        return 4
    elif cited > 5:
        return 2
    return 0


# ── Component 6: Open Access ────────────────────────────────────────────────

def score_open_access(paper: Paper) -> float:
    """Bonus for open access papers."""
    return 3.0 if paper.get("is_open_access") else 0.0


# ── Component 7: Tier Bonus ─────────────────────────────────────────────────

def score_tier_bonus(paper: Paper) -> float:
    """Bonus for confirmed meta-analyses from Track A Pass 1."""
    return 5.0 if paper.get("tier") == "primary" else 0.0


# ── Component 8: Population Relevance ────────────────────────────────────────
# Targets children under 5 OR women of reproductive age. A paper on EITHER
# population scores; this is a first-class ranking signal so under-5 / WRA
# evidence rises into the top 200.

POPULATION_MESH = {
    "Infant", "Infant, Newborn", "Child, Preschool",
    "Infant Nutritional Physiological Phenomena",
    "Pregnant Women", "Pregnancy",
    "Maternal Nutritional Physiological Phenomena",
    "Prenatal Nutritional Physiological Phenomena",
    "Reproductive Health", "Women",
}

POPULATION_KEYWORDS = {
    "under-five": 5, "under 5": 5, "preschool": 4, "infant": 4,
    "young child": 4, "neonatal": 3,
    "women of reproductive age": 5, "reproductive age": 4,
    "pregnant": 4, "pregnancy": 4, "maternal": 4,
    "antenatal": 3, "prenatal": 3,
}


def score_population_relevance(paper: Paper) -> float:
    """Score under-5 / women-of-reproductive-age relevance (MeSH or keywords)."""
    mesh = set(paper.get("mesh_terms", []))
    if mesh:
        matches = mesh & POPULATION_MESH
        return min(len(matches) * 4, POPULATION_SCORE_MAX) if matches else 0
    # Keyword fallback for OpenAlex (no MeSH)
    combined = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
    score = sum(pts for kw, pts in POPULATION_KEYWORDS.items() if kw in combined)
    return min(score, POPULATION_SCORE_MAX)


# ── Composite Score ─────────────────────────────────────────────────────────

def score_paper(paper: Paper) -> float:
    """Compute composite relevance score for a paper."""
    total = (
        score_study_design(paper) +
        score_topic_relevance(paper) +
        score_setting_relevance(paper) +
        score_recency(paper) +
        score_citations(paper) +
        score_open_access(paper) +
        score_tier_bonus(paper) +
        score_population_relevance(paper)
    )
    return round(total, 1)
