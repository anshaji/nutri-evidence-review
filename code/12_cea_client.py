"""Phase 2: targeted cost-effectiveness retrieval, per shortlisted intervention.

Phase 1 deliberately excludes cost-effectiveness (the broad Track B CEA search
returned zero usable CEAs for the actual interventions — the VAS audit's CEA
blind spot). Instead, once Phase 1's evidence review has shortlisted a handful
of interventions, this module runs a focused CEA search for EACH one, AND-ing
the intervention name/synonyms/MeSH with the cost-term skeleton.

Reuses the existing PubMed + OpenAlex clients; no new API plumbing.
"""

from __future__ import annotations

import os
import sys
import time
from datetime import datetime

from .config import (
    CEA_PER_INTERVENTION_RETMAX, CEA_OPENALEX_MAX_PAGES,
    PUBMED_DELAY, RAW_RESPONSE_DIR,
)
from .queries import build_cea_pubmed_query, build_cea_openalex_search
from .pubmed_client import esearch, efetch_batch, parse_pubmed_xml
from .openalex_client import fetch_openalex_query
from .dedup import deduplicate_pubmed, deduplicate_cross_source
from .scoring import score_paper
from .models import Paper


def _fetch_cea_pubmed(intervention: dict) -> list[Paper]:
    """Run the targeted PubMed CEA search for one intervention."""
    name = intervention["name"]
    query = build_cea_pubmed_query(intervention)

    pmids, total = esearch(query, retmax=CEA_PER_INTERVENTION_RETMAX)
    if not pmids:
        print(f"    PubMed CEA: 0 results", file=sys.stderr)
        return []

    print(f"    PubMed CEA: {total} results, fetching {len(pmids)}...", file=sys.stderr)
    time.sleep(PUBMED_DELAY)
    xml_text = efetch_batch(pmids)

    # Cache raw response under data/raw_responses/cea/
    cea_dir = os.path.join(RAW_RESPONSE_DIR, "cea")
    os.makedirs(cea_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c if c.isalnum() else "_" for c in name)[:50]
    with open(os.path.join(cea_dir, f"pubmed_cea_{safe}_{ts}.xml"), "w", encoding="utf-8") as f:
        f.write(xml_text)

    papers = parse_pubmed_xml(xml_text)
    for p in papers:
        p["query_origin"] = f"cea:{name}"
        p["tier"] = "cea"
    return papers


def _fetch_cea_openalex(intervention: dict) -> list[Paper]:
    """Run the targeted OpenAlex CEA search for one intervention."""
    name = intervention["name"]
    safe = "".join(c if c.isalnum() else "_" for c in name)[:50]
    query_def = {"name": f"cea_{safe}", "search": build_cea_openalex_search(intervention)}
    papers = fetch_openalex_query(query_def, max_pages=CEA_OPENALEX_MAX_PAGES)
    for p in papers:
        p["query_origin"] = f"cea:{name}"
        p["tier"] = "cea"
    return papers


# Markers that identify a paper as an actual cost-effectiveness study (not just
# a topically-relevant evidence review). Used to filter the loosely-matched
# OpenAlex arm and to rank the bucket CEA-strongest first.
_CEA_MARKERS = (
    "cost-effective", "cost effective", "cost-effectiveness", "cost effectiveness",
    "cost-benefit", "cost benefit", "cost-utility", "cost utility",
    "cost per daly", "cost per daly", "dalys averted", "daly averted",
    "incremental cost", "icer", "cost per case", "cost per death",
    "cost per life", "economic evaluation", "cost-consequence",
)


def cea_hits(paper: Paper) -> int:
    """Count cost-effectiveness markers in a paper's text + MeSH."""
    text = (paper.get("title", "") + " " + paper.get("abstract", "")).lower()
    text += " " + " ".join(paper.get("mesh_terms", [])).lower()
    return sum(1 for m in _CEA_MARKERS if m in text)


def fetch_cea_for_intervention(intervention: dict) -> list[Paper]:
    """Retrieve, dedup, filter, and rank CEA papers for a single intervention.

    intervention: {"name": str, "synonyms": [str], "mesh": [str], ...}
    Returns CEA papers (genuine cost-effectiveness studies), CEA-strongest
    first. May be empty — recorded honestly by the caller.

    The PubMed arm already required a cost term in its query, so it is kept.
    The OpenAlex arm is loosely OR-matched, so it is filtered to papers that
    actually carry a cost-effectiveness marker — otherwise topically-relevant
    evidence reviews (which outscore real CEAs on the general relevance score)
    would dominate the bucket.
    """
    pubmed = _fetch_cea_pubmed(intervention)
    openalex = _fetch_cea_openalex(intervention)

    pubmed = deduplicate_pubmed(pubmed)
    merged = deduplicate_cross_source(pubmed, openalex)

    kept = []
    for p in merged:
        p["relevance_score"] = score_paper(p)
        hits = cea_hits(p)
        p["cea_hits"] = hits
        # Keep PubMed (cost term was required at query time) or any paper with a
        # cost-effectiveness marker in its text.
        if p.get("source_db") == "pubmed" or hits > 0:
            # Rank on BOTH topical+population relevance AND CEA-strength, so a
            # genuine on-topic CEA outranks a topically-strong-but-weak-CEA paper
            # and an off-topic-but-CEA-heavy paper (e.g. cochlear CEA matching "VAS").
            p["cea_rank_score"] = round(p["relevance_score"] + min(hits, 5) * 5, 1)
            kept.append(p)

    kept.sort(key=lambda x: x.get("cea_rank_score", 0), reverse=True)
    return kept
