"""Unified paper data model."""

from __future__ import annotations
import re
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

    # Cochrane versioning (for version-aware dedup)
    cochrane_id: str | None  # Cochrane accession, e.g. "CD008524" (version-independent)
    superseded_by: str | None  # If this record was collapsed: id of the kept (newer) version

    # Phase 2 (cost-effectiveness)
    cea_hits: int  # Count of cost-effectiveness markers in title/abstract/MeSH
    cea_rank_score: float  # relevance_score + CEA-strength bonus (Phase 2 ranking)


def normalize_doi(doi: str | None) -> str | None:
    """Normalize DOI for deduplication: lowercase, strip prefix."""
    if not doi:
        return None
    doi = doi.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi.rstrip("/")


_COCHRANE_RE = re.compile(r"(CD\d{6,})", re.IGNORECASE)


def extract_cochrane_id(doi: str | None, journal: str | None = None) -> str | None:
    """Extract the version-independent Cochrane accession (e.g. 'CD008524').

    Cochrane Reviews carry DOIs like 10.1002/14651858.CD008524.pub3 — the
    .pubN suffix marks the version; the CDxxxxxx accession identifies the
    review itself, so a 2017 and 2022 update share one accession.
    """
    if not doi:
        return None
    m = _COCHRANE_RE.search(doi)
    if m:
        return m.group(1).upper()
    return None
