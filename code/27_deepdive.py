"""CARE deep-dive orchestrator — PICOS-targeted evidence retrieval (Phase 1).

Runs a focused retrieval for the 3 partner-selected interventions, split into
4 PICOS blocks (breastfeeding disaggregated facility vs community). For each
block it runs three passes — meta-analysis, systematic review, and an
IMPLEMENTATION pass (program evaluations / trials / cohorts / qualitative that
carry coverage/adherence/delivery/barrier signal) — plus an OpenAlex arm.

This is EVIDENCE ONLY. Cost is not searched here; cost is Phase 2
(code/15_run_cea.py), run later per the partners' "evidence now, cost later"
steer. Output is a ranked per-block evidence set under data/deepdive/ that we
validate for relevance before committing to full-text + extraction + synthesis.

Reuses the main pipeline's clients, dedup, enrichment, and scoring unchanged —
only the query layer (deep-dive blocks) and the ranking (deepdive_score, which
adds an implementation-relevance component) are new.
"""

import os
import re
import sys
import json
import csv
from datetime import datetime

from .config import (
    DEEPDIVE_DIR, DEEPDIVE_OPENALEX_MAX_PAGES, RAW_RESPONSE_DIR, NCBI_API_KEY,
)
from .queries import (
    DEEPDIVE_BLOCKS, MA_FILTER, SR_FILTER, IMPL_TYPE_FILTER,
    build_deepdive_terms, build_deepdive_openalex, build_openalex_search,
)
from .pubmed_client import fetch_pubmed_track
from .openalex_client import fetch_openalex_query
from .citation_enrichment import enrich_citations
from .dedup import (
    deduplicate_pubmed, deduplicate_cochrane,
    deduplicate_openalex, deduplicate_cross_source,
)
from .scoring import deepdive_score, score_implementation_relevance


def _run_block(block: dict) -> list[dict]:
    """Retrieve, dedup, enrich, and score one PICOS block."""
    key, label = block["key"], block["label"]
    print(f"\n{'─' * 70}\n  BLOCK: {label}\n{'─' * 70}")

    pubmed_papers: list[dict] = []

    # Pass 1 — Meta-analyses (clinical)
    ma_def = {"name": f"{key}_ma", "terms": build_deepdive_terms(block, include_impl=False)}
    ma = fetch_pubmed_track(ma_def, MA_FILTER, tier="primary")
    print(f"    MA pass:   {len(ma)} papers")
    pubmed_papers.extend(ma)

    # Pass 2 — Systematic reviews (clinical)
    sr_def = {"name": f"{key}_sr", "terms": build_deepdive_terms(block, include_impl=False)}
    sr = fetch_pubmed_track(sr_def, SR_FILTER, tier="supplementary")
    print(f"    SR pass:   {len(sr)} papers")
    pubmed_papers.extend(sr)

    # Pass 3 — Implementation (program evaluations / trials / cohorts / qualitative)
    impl_def = {"name": f"{key}_impl", "terms": build_deepdive_terms(block, include_impl=True)}
    impl = fetch_pubmed_track(impl_def, IMPL_TYPE_FILTER, tier="implementation")
    print(f"    IMPL pass: {len(impl)} papers")
    pubmed_papers.extend(impl)

    # OpenAlex arm — clinical + implementation free-text
    oa_clin = {"name": f"{key}_oa",
               "search": build_openalex_search(build_deepdive_openalex(block, include_impl=False))}
    oa_impl = {"name": f"{key}_oa_impl",
               "search": build_openalex_search(build_deepdive_openalex(block, include_impl=True))}
    openalex_papers = fetch_openalex_query(oa_clin, max_pages=DEEPDIVE_OPENALEX_MAX_PAGES)
    openalex_papers += fetch_openalex_query(oa_impl, max_pages=DEEPDIVE_OPENALEX_MAX_PAGES)
    print(f"    OpenAlex:  {len(openalex_papers)} papers")

    # Optional title anchor: PubMed papers already passed a precise query (e.g.
    # BF [Majr]/[ti]) and are trusted; OpenAlex papers (no MeSH) are gated on a
    # title regex to kill topically-loose bleed-in.
    anchor = block.get("title_anchor")
    if anchor:
        rx = re.compile(anchor, re.I)
        before = len(openalex_papers)
        openalex_papers = [p for p in openalex_papers if rx.search(p.get("title") or "")]
        print(f"    title-anchor: OpenAlex {before} → {len(openalex_papers)} kept")

    # Dedup: within PubMed (PMID → Cochrane-version collapse), within OpenAlex,
    # then cross-source.
    pubmed_papers = deduplicate_cochrane(deduplicate_pubmed(pubmed_papers))
    openalex_papers = deduplicate_openalex(openalex_papers)
    merged = deduplicate_cross_source(pubmed_papers, openalex_papers)
    print(f"    → {len(merged)} unique after dedup")

    # Enrich citations, then score with the implementation-aware ranker.
    merged = enrich_citations(merged)
    for p in merged:
        p["deepdive_block"] = key
        p["implementation_score"] = score_implementation_relevance(p)
        p["relevance_score"] = deepdive_score(p)
    merged.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
    return merged


def run_deepdive(only: list[str] | None = None):
    """Execute the CARE deep-dive Phase-1 retrieval.

    only: optional list of block keys to run (e.g. ["breastfeeding"]) — lets us
    re-run a single block without re-fetching the others. None runs all blocks.
    """
    blocks = [b for b in DEEPDIVE_BLOCKS if not only or b["key"] in only]
    print("=" * 70)
    print("CARE DEEP-DIVE — PHASE 1 (EVIDENCE ONLY, PICOS-TARGETED)")
    print(f"{len(blocks)} block(s): {', '.join(b['key'] for b in blocks)} | "
          f"implementation-weighted | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)
    print(f"NCBI API key: {'configured (10 req/s)' if NCBI_API_KEY else 'NOT SET (3 req/s)'}")

    os.makedirs(DEEPDIVE_DIR, exist_ok=True)
    os.makedirs(RAW_RESPONSE_DIR, exist_ok=True)

    all_rows: list[dict] = []
    summary: list[tuple[str, int, int]] = []

    for block in blocks:
        papers = _run_block(block)

        # Per-block JSON (full records, ranked)
        out_path = os.path.join(DEEPDIVE_DIR, f"{block['key']}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(papers, f, indent=2, ensure_ascii=False, default=str)

        impl_heavy = sum(1 for p in papers if p.get("implementation_score", 0) >= 6)
        summary.append((block["key"], len(papers), impl_heavy))

        print(f"    saved {out_path} ({len(papers)} papers, {impl_heavy} implementation-heavy)")

    # Combined CSV — rebuilt from ALL per-block JSON on disk (so re-running one
    # block doesn't drop the others from the combined view).
    csv_path = os.path.join(DEEPDIVE_DIR, "deepdive_combined.csv")
    fieldnames = [
        "deepdive_block", "relevance_score", "implementation_score", "tier",
        "study_type", "publication_year", "title", "journal", "cited_by_count",
        "doi", "pmid", "source_db", "query_origin",
    ]
    all_rows = []
    for b in DEEPDIVE_BLOCKS:
        bpath = os.path.join(DEEPDIVE_DIR, f"{b['key']}.json")
        if os.path.isfile(bpath):
            all_rows.extend(json.load(open(bpath, encoding="utf-8")))
    all_rows.sort(key=lambda x: (x.get("deepdive_block", ""), -x.get("relevance_score", 0)))
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for p in all_rows:
            writer.writerow(p)

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"\n{'=' * 70}\nDEEP-DIVE SUMMARY\n{'=' * 70}")
    print(f"  {'block':<28s}{'papers':>8s}{'impl-heavy':>12s}")
    for key, n, impl in summary:
        print(f"  {key:<28s}{n:>8d}{impl:>12d}")
    print(f"\n  Combined CSV: {csv_path} ({len(all_rows)} rows)")
    print(f"  Per-block JSON in {os.path.abspath(DEEPDIVE_DIR)}/")
    print("  Next: review per-block relevance, then run full-text + extraction + synthesis.")
    print("=" * 70)

    return all_rows
