"""Unified paper data model."""

from __future__ import annotations
from typing import TypedDict


class Paper(TypedDict, total=False):
    """Unified representation of a paper from any source."""

    # Identity
    id: str  # Canonical: "pmid:12345678" or OpenAlex ID
    title: str
    abstract: str

    # Bibliographic
    publication_year: int | None
    authors: list[str]  # First 5 authors
    journal: str
    doi: str | None
    pmid: str | None
    openalex_id: str | None

    # Source tracking
    source_db: str  # "pubmed" | "openalex"
    query_origin: str  # Which query found this paper

    # Classification (authoritative from PubMed, inferred for OpenAlex)
    study_type: str  # Human-readable classification
    publication_type: list[str]  # Raw from PubMed indexing
    mesh_terms: list[str]  # MeSH descriptor names

    # Impact
    cited_by_count: int
    is_open_access: bool

    # Scoring
    relevance_score: float
    tier: str  # "primary" (meta-analysis) | "supplementary" (SR) | "cea" | "nutrition-sensitive"


def normalize_doi(doi: str | None) -> str | None:
    """Normalize DOI for deduplication: lowercase, strip prefix."""
    if not doi:
        return None
    doi = doi.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi.rstrip("/")
