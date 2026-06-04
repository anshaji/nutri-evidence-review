"""Main orchestrator for the evidence synthesis pipeline.

Runs all tracks, deduplicates, enriches citations, scores, and exports.
"""

import os
import sys
import json
import csv
from datetime import datetime

from .config import OUTPUT_DIR, RAW_RESPONSE_DIR, TOP_N_FOR_REVIEW, NCBI_API_KEY
from .queries import (
    TRACK_A_QUERIES, TRACK_C_QUERIES,
    MA_FILTER, SR_FILTER, build_openalex_search,
)
from .pubmed_client import fetch_pubmed_track
from .openalex_client import fetch_openalex_query
from .citation_enrichment import enrich_citations
from .dedup import (
    deduplicate_pubmed, deduplicate_cochrane,
    deduplicate_openalex, deduplicate_cross_source,
)
from .scoring import score_paper
from .fulltext_client import retrieve_fulltext


def run_phase1():
    """Execute Phase 1 of the pipeline: evidence retrieval, ranking, full text.

    Phase 1 finds strong evidence for nutrition interventions in children under
    5 and women of reproductive age (PubMed Track A + OpenAlex Track C). Cost-
    effectiveness is deliberately excluded here — it is handled per shortlisted
    intervention in Phase 2 (see pipeline/cea_main.py).
    """
    print("=" * 70)
    print("NUTRITION EVIDENCE SYNTHESIS PIPELINE v3.0 — PHASE 1 (EVIDENCE)")
    print(f"PubMed + OpenAlex | under-5 + WRA | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    if NCBI_API_KEY:
        print(f"NCBI API key: configured (10 req/s)")
    else:
        print(f"NCBI API key: NOT SET (3 req/s — set NCBI_API_KEY env var for faster runs)")

    os.makedirs(RAW_RESPONSE_DIR, exist_ok=True)

    # ── Track A Pass 1: Meta-Analyses ───────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("TRACK A — PASS 1: Meta-Analyses (PubMed)")
    print(f"{'─' * 70}")

    pubmed_primary = []
    for i, qdef in enumerate(TRACK_A_QUERIES, 1):
        print(f"\n  [{i}/{len(TRACK_A_QUERIES)}] {qdef['name']}")
        papers = fetch_pubmed_track(qdef, MA_FILTER, tier="primary")
        pubmed_primary.extend(papers)
        print(f"    → {len(papers)} papers")

    print(f"\n  Track A Pass 1 total: {len(pubmed_primary)} papers")

    # ── Track A Pass 2: Systematic Reviews ──────────────────────────────────
    print(f"\n{'─' * 70}")
    print("TRACK A — PASS 2: Systematic Reviews (PubMed)")
    print(f"{'─' * 70}")

    pubmed_supplementary = []
    for i, qdef in enumerate(TRACK_A_QUERIES, 1):
        print(f"\n  [{i}/{len(TRACK_A_QUERIES)}] {qdef['name']}")
        papers = fetch_pubmed_track(qdef, SR_FILTER, tier="supplementary")
        pubmed_supplementary.extend(papers)
        print(f"    → {len(papers)} papers")

    print(f"\n  Track A Pass 2 total: {len(pubmed_supplementary)} papers")

    # ── Track C: Non-Biomedical (OpenAlex) ──────────────────────────────────
    # (Cost-effectiveness is NOT searched in Phase 1 — see Phase 2.)
    print(f"\n{'─' * 70}")
    print("TRACK C: Nutrition-Sensitive (OpenAlex)")
    print(f"{'─' * 70}")

    openalex_papers = []
    for i, qdef in enumerate(TRACK_C_QUERIES, 1):
        print(f"\n  [{i}/{len(TRACK_C_QUERIES)}] {qdef['name']}")
        # AND the population clause (under-5 / WRA) into the free-text search
        scoped = {"name": qdef["name"], "search": build_openalex_search(qdef["search"])}
        papers = fetch_openalex_query(scoped)
        openalex_papers.extend(papers)
        print(f"    → {len(papers)} papers")

    print(f"\n  Track C total: {len(openalex_papers)} papers")

    # ── Deduplication ───────────────────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("DEDUPLICATION")
    print(f"{'─' * 70}")

    # Phase 1: Within PubMed (by PMID), then collapse Cochrane review versions
    all_pubmed = pubmed_primary + pubmed_supplementary
    print(f"\n  PubMed before dedup: {len(all_pubmed)}")
    all_pubmed = deduplicate_pubmed(all_pubmed)
    all_pubmed = deduplicate_cochrane(all_pubmed)
    print(f"  PubMed after dedup: {len(all_pubmed)}")

    # Phase 2: Within OpenAlex
    print(f"\n  OpenAlex before dedup: {len(openalex_papers)}")
    openalex_papers = deduplicate_openalex(openalex_papers)
    print(f"  OpenAlex after dedup: {len(openalex_papers)}")

    # Phase 3: Cross-source
    print(f"\n  Cross-source deduplication...")
    all_papers = deduplicate_cross_source(all_pubmed, openalex_papers)
    print(f"  Final merged set: {len(all_papers)} papers")

    # ── Citation Enrichment ──────────────────────────────────────────────���──
    print(f"\n{'─' * 70}")
    print("CITATION ENRICHMENT (OpenAlex cross-reference)")
    print(f"{'─' * 70}\n")

    all_papers = enrich_citations(all_papers)

    # ── Scoring ─────────────────────────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("SCORING")
    print(f"{'─' * 70}\n")

    for paper in all_papers:
        paper["relevance_score"] = score_paper(paper)

    all_papers.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
    print(f"  Scored {len(all_papers)} papers. Score range: "
          f"{all_papers[-1]['relevance_score']:.1f} – {all_papers[0]['relevance_score']:.1f}")

    # ── Full-Text Retrieval (Stage 3.5) ───────────────────────────────────
    top_n = min(TOP_N_FOR_REVIEW, len(all_papers))
    top_papers = all_papers[:top_n]
    top_papers = retrieve_fulltext(top_papers)

    # ── Export ──────────────────────────────────────────────────────────────
    print(f"\n{'─' * 70}")
    print("EXPORT")
    print(f"{'─' * 70}\n")

    # Full JSON database (without fulltext to keep size manageable)
    json_path = os.path.join(OUTPUT_DIR, "papers_database.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False, default=str)
    print(f"  {json_path}: {len(all_papers)} papers")

    # Ranked CSV
    csv_path = os.path.join(OUTPUT_DIR, "papers_ranked.csv")
    fieldnames = [
        "rank", "relevance_score", "tier", "title", "publication_year",
        "study_type", "publication_type", "cited_by_count", "journal",
        "doi", "pmid", "source_db", "mesh_terms", "is_open_access",
        "query_origin", "abstract",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for rank, paper in enumerate(all_papers, 1):
            row = {**paper}
            row["rank"] = rank
            # Flatten lists for CSV
            row["publication_type"] = "; ".join(paper.get("publication_type", []))
            row["mesh_terms"] = "; ".join(paper.get("mesh_terms", []))
            writer.writerow(row)
    print(f"  {csv_path}: {len(all_papers)} rows")

    # Top N for review (WITH full text)
    top_path = os.path.join(OUTPUT_DIR, "top_papers_for_review.json")
    with open(top_path, "w", encoding="utf-8") as f:
        json.dump(top_papers, f, indent=2, ensure_ascii=False, default=str)
    ft_count = sum(1 for p in top_papers if p.get("fulltext_source") == "pmc")
    print(f"  {top_path}: top {top_n} papers ({ft_count} with full text, "
          f"{top_n - ft_count} abstract-only)")

    # ── Summary ─────────────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("TOP 20 PAPERS BY RELEVANCE SCORE")
    print(f"{'=' * 70}")

    for i, p in enumerate(all_papers[:20], 1):
        print(f"\n{i:2d}. [Score: {p['relevance_score']:5.1f}] [{p['tier']}] "
              f"({p.get('publication_year', '?')}) {p['study_type']}")
        print(f"    {p['title']}")
        print(f"    Cited: {p.get('cited_by_count', 0)} | {p.get('journal', '')}")
        doi = p.get('doi', '')
        if doi:
            print(f"    https://doi.org/{doi}")

    # Score distribution
    print(f"\n{'=' * 70}")
    print("SCORE DISTRIBUTION")
    brackets = [(80, 999), (70, 80), (60, 70), (50, 60), (40, 50), (30, 40), (20, 30), (0, 20)]
    for lo, hi in brackets:
        count = sum(1 for p in all_papers if lo <= p.get("relevance_score", 0) < hi)
        label = f"{lo}+" if hi >= 999 else f"{lo}-{hi}"
        print(f"  Score {label:>6s}: {count:4d} papers")

    # Tier breakdown
    print(f"\n{'=' * 70}")
    print("TIER BREAKDOWN")
    tier_counts: dict[str, int] = {}
    for p in all_papers:
        t = p.get("tier", "unknown")
        tier_counts[t] = tier_counts.get(t, 0) + 1
    for t, c in sorted(tier_counts.items(), key=lambda x: -x[1]):
        print(f"  {t:<20s}: {c:4d}")

    # Study type breakdown
    print(f"\n{'=' * 70}")
    print("STUDY TYPE BREAKDOWN")
    type_counts: dict[str, int] = {}
    for p in all_papers:
        t = p.get("study_type", "Unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t:<40s}: {c:4d}")

    # Source breakdown
    print(f"\n{'=' * 70}")
    print("SOURCE BREAKDOWN")
    source_counts: dict[str, int] = {}
    for p in all_papers:
        s = p.get("source_db", "unknown")
        source_counts[s] = source_counts.get(s, 0) + 1
    for s, c in sorted(source_counts.items(), key=lambda x: -x[1]):
        print(f"  {s:<20s}: {c:4d}")

    print(f"\n{'=' * 70}")
    print(f"DONE (Phase 1). Files saved in {os.path.abspath(OUTPUT_DIR)}/")
    print("Next: review top_papers_for_review.json, author shortlist.json, then run run_cea.py (Phase 2).")
    print(f"{'=' * 70}")

    return all_papers


# Backwards-compatible alias
run_pipeline = run_phase1
