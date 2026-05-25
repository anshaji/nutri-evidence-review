"""Citation enrichment: cross-reference PubMed papers with OpenAlex for citation counts.

PubMed doesn't provide citation counts. OpenAlex does.
This module looks up PubMed papers by DOI in OpenAlex to fill cited_by_count.
"""

import sys
import time
import json
import urllib.request
import urllib.parse

from .config import OPENALEX_BASE, OPENALEX_MAILTO, OPENALEX_DELAY
from .models import Paper, normalize_doi


def enrich_citations(papers: list[Paper], batch_size: int = 50) -> list[Paper]:
    """
    For papers with DOIs that lack citation data, look them up in OpenAlex.
    Modifies papers in-place and returns them.

    Uses OpenAlex filter API to batch lookups:
    /works?filter=doi:10.xxx|10.yyy|10.zzz
    """
    # Collect papers needing enrichment (have DOI, no citations yet)
    needs_enrichment = [
        (i, p) for i, p in enumerate(papers)
        if p.get("doi") and p.get("cited_by_count", 0) == 0
    ]

    if not needs_enrichment:
        print("  No papers need citation enrichment.", file=sys.stderr)
        return papers

    print(f"  Enriching citations for {len(needs_enrichment)} papers...", file=sys.stderr)

    # Build DOI → paper index mapping
    doi_to_indices: dict[str, list[int]] = {}
    for idx, paper in needs_enrichment:
        ndoi = normalize_doi(paper.get("doi"))
        if ndoi:
            doi_to_indices.setdefault(ndoi, []).append(idx)

    all_dois = list(doi_to_indices.keys())
    enriched_count = 0

    # Batch lookup
    for batch_start in range(0, len(all_dois), batch_size):
        batch_dois = all_dois[batch_start:batch_start + batch_size]
        doi_filter = "|".join(batch_dois)

        params = urllib.parse.urlencode({
            "filter": f"doi:{doi_filter}",
            "per_page": batch_size,
            "select": "doi,cited_by_count,open_access",
            "mailto": OPENALEX_MAILTO,
        })
        url = f"{OPENALEX_BASE}?{params}"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NutriEvidenceBot/2.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                results = data.get("results", [])

                for work in results:
                    work_doi = work.get("doi", "")
                    ndoi = normalize_doi(work_doi)
                    if ndoi and ndoi in doi_to_indices:
                        cited = work.get("cited_by_count", 0)
                        is_oa = work.get("open_access", {}).get("is_oa", False)
                        for idx in doi_to_indices[ndoi]:
                            papers[idx]["cited_by_count"] = cited
                            if is_oa:
                                papers[idx]["is_open_access"] = True
                            enriched_count += 1

        except Exception as e:
            print(f"    [Citation enrichment ERROR] batch {batch_start//batch_size + 1}: {e}",
                  file=sys.stderr)

        time.sleep(OPENALEX_DELAY)

        # Progress
        done = min(batch_start + batch_size, len(all_dois))
        print(f"    Processed {done}/{len(all_dois)} DOIs...", file=sys.stderr)

    print(f"  Enriched {enriched_count} papers with citation counts.", file=sys.stderr)
    return papers
