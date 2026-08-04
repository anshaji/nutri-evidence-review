#!/usr/bin/env python3
"""Build per-paper extraction cards + token-balanced batches (Stage 3.6 prep).

Reads papers_database.json (metadata) + data/fulltext/{key}.json (full text
where retrieved) and writes one self-contained card per paper to
data/extraction_inputs/{key}.json. Each card is everything an extraction
subagent needs from a single Read: metadata, abstract, and a length-capped
full-text excerpt (Methods/Results-biased, since that is where effect sizes
live).

Also writes data/extraction_inputs/batches.json — a greedy bin-packing of all
cards into ~token-balanced batches so each extraction subagent gets a bounded
context.

Usage: python3 code/21_build_extraction_inputs.py
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.fulltext_all import paper_key  # reuse the same key scheme

OUTPUT_DIR = "./data"
DB_PATH = os.path.join(OUTPUT_DIR, "papers_database.json")
FULLTEXT_DIR = os.path.join(OUTPUT_DIR, "fulltext")  # SHARED across corpora
INPUT_DIR = os.path.join(OUTPUT_DIR, "extraction_inputs")

MAX_FULLTEXT_WORDS = 9000        # cap per card (~12k tokens)
BATCH_TOKEN_TARGET = 70_000      # aim per batch
BATCH_MAX_PAPERS = 18            # hard cap per batch

# Sections most worth keeping when we must truncate (effect sizes / design).
PRIORITY_SECS = ("result", "method", "finding", "outcome", "abstract",
                 "discussion", "conclusion")


def _est_tokens(words: int) -> int:
    return int(words * 1.3)


def _trim_fulltext(ft: dict) -> tuple[str, list, bool]:
    """Return (excerpt_text, tables, truncated) capped at MAX_FULLTEXT_WORDS."""
    secs = ft.get("sections") or []
    tables = ft.get("tables") or []

    # order sections: priority sections first (keep original order within tier)
    def prio(s):
        t = (s.get("title") or "").lower()
        for i, kw in enumerate(PRIORITY_SECS):
            if kw in t:
                return i
        return len(PRIORITY_SECS)

    ordered = sorted(range(len(secs)), key=lambda i: (prio(secs[i]), i))
    kept, used, truncated = [], 0, False
    for i in ordered:
        s = secs[i]
        w = len((s.get("text") or "").split())
        if used + w > MAX_FULLTEXT_WORDS and kept:
            truncated = True
            break
        kept.append(i)
        used += w
    # re-emit in original document order
    kept.sort()
    parts = []
    for i in kept:
        s = secs[i]
        if s.get("title"):
            parts.append(f"## {s['title']}")
        parts.append(s.get("text", ""))
    text = "\n\n".join(p for p in parts if p).strip()

    # keep table captions (compact, effect-size rich) — drop huge bodies
    slim_tables = []
    for t in tables[:12]:
        slim_tables.append({
            "label": t.get("label", ""),
            "caption": t.get("caption", ""),
            "content": (t.get("content", "") or "")[:2000],
        })
    return text, slim_tables, truncated


def main(db_path: str = DB_PATH, input_dir: str = INPUT_DIR):
    db = json.load(open(db_path))
    os.makedirs(input_dir, exist_ok=True)

    cards = []
    n_ft = 0
    for p in db:
        key = paper_key(p)
        ft_excerpt, tables, truncated = "", [], False
        ftp = os.path.join(FULLTEXT_DIR, key + ".json")
        if os.path.isfile(ftp):
            try:
                ft = json.load(open(ftp))
                ft_excerpt, tables, truncated = _trim_fulltext(ft)
                if ft_excerpt:
                    n_ft += 1
            except Exception:
                pass

        card = {
            "key": key,
            "pmid": p.get("pmid"),
            "doi": p.get("doi"),
            "openalex_id": p.get("openalex_id"),
            "title": p.get("title", ""),
            "journal": p.get("journal", ""),
            "publication_year": p.get("publication_year"),
            "source_db": p.get("source_db"),
            "study_type": p.get("study_type", ""),
            "publication_type": p.get("publication_type", []),
            "mesh_terms": p.get("mesh_terms", []),
            "cochrane_id": p.get("cochrane_id"),
            "is_open_access": p.get("is_open_access", False),
            "query_origin": p.get("query_origin", ""),
            "relevance_score": p.get("relevance_score", 0),
            # Deep-dive fields (empty/absent for the main pipeline — harmless):
            "deepdive_blocks": p.get("deepdive_blocks", []),
            "implementation_score": p.get("implementation_score", 0),
            "abstract": p.get("abstract", ""),
            "fulltext_source": p.get("fulltext_source", "abstract_only"),
            "fulltext_truncated": truncated,
            "fulltext_excerpt": ft_excerpt,
            "tables": tables,
        }
        with open(os.path.join(input_dir, key + ".json"), "w", encoding="utf-8") as f:
            json.dump(card, f, ensure_ascii=False)

        words = len((card["abstract"] or "").split()) + len(ft_excerpt.split()) + 200
        cards.append({"key": key, "tokens": _est_tokens(words),
                      "has_fulltext": bool(ft_excerpt)})

    # ── greedy bin-pack into batches ─────────────────────────────────────────
    cards.sort(key=lambda c: -c["tokens"])   # big first, then fill
    batches, cur, cur_tok = [], [], 0
    for c in cards:
        if cur and (cur_tok + c["tokens"] > BATCH_TOKEN_TARGET or len(cur) >= BATCH_MAX_PAPERS):
            batches.append(cur); cur, cur_tok = [], 0
        cur.append(c["key"]); cur_tok += c["tokens"]
    if cur:
        batches.append(cur)

    manifest = {
        "n_papers": len(cards),
        "n_with_fulltext": n_ft,
        "n_batches": len(batches),
        "batches": [{"batch_index": i, "keys": b} for i, b in enumerate(batches)],
    }
    with open(os.path.join(input_dir, "batches.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    sizes = [len(b) for b in batches]
    print(f"Cards written:      {len(cards)}  ({n_ft} with full-text excerpt)")
    print(f"Batches:            {len(batches)}  "
          f"(papers/batch min={min(sizes)} max={max(sizes)} avg={sum(sizes)/len(sizes):.1f})")
    print(f"Manifest:           {os.path.join(input_dir, 'batches.json')}")


if __name__ == "__main__":
    db = sys.argv[1] if len(sys.argv) > 1 else DB_PATH
    inp = sys.argv[2] if len(sys.argv) > 2 else INPUT_DIR
    main(db_path=db, input_dir=inp)
