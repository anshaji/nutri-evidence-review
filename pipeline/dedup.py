"""Deduplication: within-source and cross-source.

Phase 1: Within PubMed by PMID (across all Track A + B queries)
Phase 2: Within OpenAlex by OpenAlex ID (across Track C queries)
Phase 3: Cross-source by DOI (prefer PubMed record, merge citation count from OpenAlex)
"""

import sys
from .models import Paper, normalize_doi


def deduplicate_pubmed(papers: list[Paper]) -> list[Paper]:
    """
    Deduplicate PubMed papers by PMID.
    When duplicates exist (from overlapping queries), keep the one with
    the higher-priority tier: primary > supplementary > cea.
    """
    tier_priority = {"primary": 0, "supplementary": 1, "cea": 2}
    seen: dict[str, Paper] = {}

    for paper in papers:
        pmid = paper.get("pmid")
        if not pmid:
            continue

        if pmid not in seen:
            seen[pmid] = paper
        else:
            # Keep the one from the higher-priority tier
            existing_priority = tier_priority.get(seen[pmid].get("tier", ""), 99)
            new_priority = tier_priority.get(paper.get("tier", ""), 99)
            if new_priority < existing_priority:
                seen[pmid] = paper

    deduped = list(seen.values())
    removed = len(papers) - len(deduped)
    if removed:
        print(f"  PubMed dedup: {len(papers)} → {len(deduped)} ({removed} duplicates removed)",
              file=sys.stderr)
    return deduped


def deduplicate_openalex(papers: list[Paper]) -> list[Paper]:
    """Deduplicate OpenAlex papers by OpenAlex ID."""
    seen: dict[str, Paper] = {}
    for paper in papers:
        oa_id = paper.get("openalex_id") or paper.get("id", "")
        if oa_id and oa_id not in seen:
            seen[oa_id] = paper
    deduped = list(seen.values())
    removed = len(papers) - len(deduped)
    if removed:
        print(f"  OpenAlex dedup: {len(papers)} → {len(deduped)} ({removed} duplicates removed)",
              file=sys.stderr)
    return deduped


def deduplicate_cross_source(
    pubmed_papers: list[Paper],
    openalex_papers: list[Paper],
) -> list[Paper]:
    """
    Cross-source deduplication by DOI.

    When a paper exists in both PubMed and OpenAlex:
    - Keep the PubMed record (richer metadata: MeSH, publication_type)
    - Merge cited_by_count and open_access from OpenAlex
    - Set openalex_id on the PubMed record

    Returns the merged, deduplicated list.
    """
    # Index PubMed papers by normalized DOI
    pubmed_by_doi: dict[str, int] = {}
    for i, paper in enumerate(pubmed_papers):
        ndoi = normalize_doi(paper.get("doi"))
        if ndoi:
            pubmed_by_doi[ndoi] = i

    # Check each OpenAlex paper against PubMed
    unique_openalex = []
    merged_count = 0

    for oa_paper in openalex_papers:
        ndoi = normalize_doi(oa_paper.get("doi"))
        if ndoi and ndoi in pubmed_by_doi:
            # Merge: enrich PubMed record with OpenAlex data
            pm_idx = pubmed_by_doi[ndoi]
            pm_paper = pubmed_papers[pm_idx]
            # Take citation count (OpenAlex has this, PubMed doesn't)
            if oa_paper.get("cited_by_count", 0) > pm_paper.get("cited_by_count", 0):
                pm_paper["cited_by_count"] = oa_paper["cited_by_count"]
            # Take open access status
            if oa_paper.get("is_open_access"):
                pm_paper["is_open_access"] = True
            # Record OpenAlex ID
            pm_paper["openalex_id"] = oa_paper.get("openalex_id")
            merged_count += 1
        else:
            # No match in PubMed — keep as unique OpenAlex paper
            unique_openalex.append(oa_paper)

    if merged_count:
        print(f"  Cross-source merge: {merged_count} papers matched by DOI "
              f"(PubMed records enriched)", file=sys.stderr)
    print(f"  Unique OpenAlex papers (no PubMed match): {len(unique_openalex)}", file=sys.stderr)

    return pubmed_papers + unique_openalex
