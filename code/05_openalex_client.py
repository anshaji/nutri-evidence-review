"""OpenAlex client for Track C (non-biomedical literature).

Used only for nutrition-sensitive interventions in economics/development
literature that PubMed covers poorly: cash transfers, social protection,
food subsidies.
"""

from __future__ import annotations

import os
import sys
import time
import json
import urllib.request
import urllib.parse
from datetime import datetime

from .config import OPENALEX_BASE, OPENALEX_MAILTO, OPENALEX_DELAY, RAW_RESPONSE_DIR
from .models import Paper


def extract_abstract(work: dict) -> str:
    """Reconstruct abstract from OpenAlex inverted index format."""
    inv = work.get("abstract_inverted_index")
    if not inv:
        return ""
    word_positions = []
    for word, positions in inv.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort()
    return " ".join(w for _, w in word_positions)


def _get_source_name(work: dict) -> str:
    """Extract journal/source name."""
    loc = work.get("primary_location", {})
    if loc:
        source = loc.get("source", {})
        if source:
            return source.get("display_name", "")
    return ""


def _get_doi(work: dict) -> str | None:
    """Extract DOI from OpenAlex work."""
    doi = work.get("doi")
    if doi:
        # OpenAlex returns full URL: https://doi.org/10.xxxx
        return doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return None


def _get_authors(work: dict) -> list[str]:
    """Extract first 5 author names."""
    authors = []
    for authorship in work.get("authorships", [])[:5]:
        author = authorship.get("author", {})
        name = author.get("display_name", "")
        if name:
            authors.append(name)
    return authors


def _classify_study_type(title: str, abstract: str) -> str:
    """Classify paper into study type based on text (fallback for OpenAlex)."""
    combined = (title + " " + abstract).lower()
    if "umbrella review" in combined:
        return "Umbrella Review"
    if "meta-analysis" in combined and "systematic review" in combined:
        return "Systematic Review & Meta-Analysis"
    if "meta-analysis" in combined:
        return "Meta-Analysis"
    if "cochrane" in combined:
        return "Cochrane Review"
    if "systematic review" in combined:
        return "Systematic Review"
    if "scoping review" in combined:
        return "Scoping Review"
    if "randomized controlled" in combined or "randomised controlled" in combined:
        return "RCT"
    if "review" in combined:
        return "Review"
    return "Article"


def fetch_openalex_query(query_def: dict, per_page: int = 100, max_pages: int = 5) -> list[Paper]:
    """
    Fetch works from OpenAlex for a Track C query.
    Returns unified Paper dicts.
    """
    search_text = query_def["search"]
    name = query_def["name"]
    all_papers = []
    raw_results = []

    for page in range(1, max_pages + 1):
        params = urllib.parse.urlencode({
            "search": search_text,
            "filter": "type:article|review",
            "per_page": per_page,
            "page": page,
            "mailto": OPENALEX_MAILTO,
        })
        url = f"{OPENALEX_BASE}?{params}"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NutriEvidenceBot/2.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                results = data.get("results", [])
                if not results:
                    break
                raw_results.extend(results)
                total = data.get("meta", {}).get("count", 0)
                if page * per_page >= total:
                    break
        except Exception as e:
            print(f"    [OpenAlex ERROR] page {page}: {e}", file=sys.stderr)
            break

        time.sleep(OPENALEX_DELAY)

    # Save raw response
    os.makedirs(RAW_RESPONSE_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = os.path.join(RAW_RESPONSE_DIR, f"openalex_{name}_{ts}.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(raw_results, f, ensure_ascii=False)

    # Convert to Paper format
    for work in raw_results:
        wid = work.get("id", "")
        title = work.get("title") or ""
        abstract = extract_abstract(work)
        doi = _get_doi(work)

        paper = Paper(
            id=wid,
            title=title,
            abstract=abstract,
            publication_year=work.get("publication_year"),
            authors=_get_authors(work),
            journal=_get_source_name(work),
            doi=doi,
            pmid=None,
            openalex_id=wid,
            source_db="openalex",
            query_origin=name,
            study_type=_classify_study_type(title, abstract),
            publication_type=[],  # Not available from OpenAlex
            mesh_terms=[],  # Not available from OpenAlex
            cited_by_count=work.get("cited_by_count", 0),
            is_open_access=work.get("open_access", {}).get("is_oa", False),
            relevance_score=0.0,
            tier="nutrition-sensitive",
        )
        all_papers.append(paper)

    return all_papers
