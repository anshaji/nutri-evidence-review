"""Full-corpus full-text retrieval (Stage 3.5, scaled to all papers).

Extends the top-200-only Stage 3.5 to the WHOLE corpus (PubMed + OpenAlex),
using two routes:

  1. PMC (primary) — resolve every paper's PMID *or DOI* to a PMCID via the
     NCBI ID Converter (which accepts DOIs, not just PMIDs), then reuse the
     proven `09_fulltext_client` efetch+JATS-parse path. This reaches most
     open-access papers, including publisher content that blocks PDF scraping
     (Lancet, Campbell, BMC, MDPI, …) because PMC hosts a clean JATS copy.
  2. Unpaywall PDF (fallback) — for papers with no PMCID or a restricted
     (body-less) PMC record, resolve a best open-access PDF via Unpaywall,
     preferring *repository* copies over publisher copies (repositories rarely
     403 a bot), download it, and extract text with PyMuPDF.

Design choices:
  - Full text is written **per paper** to `data/fulltext/{key}.json` so the
    downstream extraction workflow can Read one paper at a time, and so the
    master `papers_database.json` stays lean (annotated with flags only, not
    the multi-MB text blobs).
  - Every network step is cached, so re-runs are cheap and the job is
    resumable after interruption.

stdlib + PyMuPDF (installed via pip; the "stdlib-only" note in CLAUDE.md is
stale — pip works on this machine).
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.request
import urllib.parse

from .config import (
    NCBI_EMAIL,
    NCBI_TOOL,
    OUTPUT_DIR,
    PUBMED_DELAY,
    RAW_RESPONSE_DIR,
)
from .fulltext_client import fetch_pmc_batch, parse_pmc_fulltext

# ── Paths ─────────────────────────────────────────────────────────────────────
DB_PATH = os.path.join(OUTPUT_DIR, "papers_database.json")
FULLTEXT_DIR = os.path.join(OUTPUT_DIR, "fulltext")
PDF_DIR = os.path.join(RAW_RESPONSE_DIR, "pdf")
IDCONV_CACHE = os.path.join(RAW_RESPONSE_DIR, "idconv_cache.json")
UNPAYWALL_CACHE = os.path.join(RAW_RESPONSE_DIR, "unpaywall_cache.json")

IDCONV_URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
UNPAYWALL_URL = "https://api.unpaywall.org/v2/"
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


# ── Small helpers ─────────────────────────────────────────────────────────────

def paper_key(p: dict) -> str:
    """Stable, filesystem-safe key for a paper (PMID > OpenAlex id > DOI)."""
    if p.get("pmid"):
        return f"pmid_{p['pmid']}"
    oa = p.get("openalex_id") or p.get("id") or ""
    m = re.search(r"(W\d+)", oa)
    if m:
        return f"oa_{m.group(1)}"
    doi = p.get("doi") or ""
    return "doi_" + re.sub(r"[^A-Za-z0-9]+", "_", doi).strip("_") or "unknown"


def _load_json(path, default):
    if os.path.isfile(path):
        try:
            with open(path) as f:
                return json.load(f)
        except Exception:
            return default
    return default


def _save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False)
    os.replace(tmp, path)


def _chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# ── Step 1: resolve PMCIDs (PMID or DOI → PMCID) ──────────────────────────────

def resolve_pmcids(id_batch: list[str], batch_size: int) -> dict[str, str]:
    """Resolve a list of PMIDs or DOIs to PMCIDs via the NCBI ID Converter.

    Cached across runs in IDCONV_CACHE. Long DOIs blow the GET URL length at
    batch=200, so DOI batches must be small (~40).
    """
    cache: dict[str, str] = _load_json(IDCONV_CACHE, {})
    todo = [i for i in id_batch if i not in cache]
    if todo:
        print(f"    resolving {len(todo)} new ids (batch {batch_size}) ...")
    for bi, batch in enumerate(_chunks(todo, batch_size)):
        params = urllib.parse.urlencode({
            "ids": ",".join(batch), "format": "json",
            "tool": NCBI_TOOL, "email": NCBI_EMAIL,
        })
        url = f"{IDCONV_URL}?{params}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": NCBI_TOOL})
            with urllib.request.urlopen(req, timeout=45) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            for rec in data.get("records", []):
                # the converter echoes back whichever id it matched
                echoed = str(rec.get("pmid") or "") if rec.get("pmid") else ""
                doi = rec.get("doi")
                pmcid = rec.get("pmcid") or ""
                # map every id in this batch that matches this record
                for ident in batch:
                    if pmcid and (ident == echoed or (doi and ident.lower() == doi.lower())):
                        cache[ident] = pmcid
            # anything unresolved in this batch → cache empty so we don't retry
            for ident in batch:
                cache.setdefault(ident, "")
        except Exception as e:
            print(f"      [warn] idconv batch {bi} failed: {e}")
        if bi % 10 == 0:
            _save_json(IDCONV_CACHE, cache)
        time.sleep(PUBMED_DELAY)
    _save_json(IDCONV_CACHE, cache)
    return {i: cache[i] for i in id_batch if cache.get(i)}


# ── Step 2: Unpaywall → OA PDF (repository-preferred) → PyMuPDF ────────────────

def unpaywall_pdf_url(doi: str) -> str | None:
    """Return a best OA PDF URL for a DOI, preferring repository over publisher.

    Repository copies (Europe PMC, institutional repos) rarely 403 a scraper,
    unlike publisher sites (Wiley/Elsevier).
    """
    cache: dict = _load_json(UNPAYWALL_CACHE, {})
    if doi in cache:
        return cache[doi] or None
    url = f"{UNPAYWALL_URL}{urllib.parse.quote(doi)}?email={NCBI_EMAIL}"
    chosen = ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": NCBI_TOOL})
        with urllib.request.urlopen(req, timeout=30) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        locs = [l for l in (d.get("oa_locations") or []) if l.get("url_for_pdf")]
        repo = [l for l in locs if l.get("host_type") == "repository"]
        pick = (repo or locs)
        if pick:
            chosen = pick[0]["url_for_pdf"]
    except Exception as e:
        print(f"      [warn] unpaywall {doi}: {e}")
    cache[doi] = chosen
    _save_json(UNPAYWALL_CACHE, cache)
    time.sleep(0.1)
    return chosen or None


def fetch_and_parse_pdf(url: str, cache_path: str) -> dict | None:
    """Download a PDF (cached) and extract structured text with PyMuPDF."""
    import fitz  # PyMuPDF

    data = None
    if os.path.isfile(cache_path):
        with open(cache_path, "rb") as f:
            data = f.read()
    else:
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": BROWSER_UA, "Accept": "application/pdf,*/*"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
        except Exception as e:
            print(f"      [warn] pdf fetch {url[:60]}: {type(e).__name__}")
            return None
        if not data or data[:5] != b"%PDF-":
            return None
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, "wb") as f:
            f.write(data)

    try:
        doc = fitz.open(stream=data, filetype="pdf")
        pages = [pg.get_text("text") for pg in doc]
        full = "\n".join(pages).strip()
        npages = doc.page_count
        doc.close()
    except Exception as e:
        print(f"      [warn] pdf parse: {type(e).__name__}")
        return None

    # Heuristic: scanned/image PDFs yield almost no text → treat as failure.
    if len(full) < 500 or (npages and len(full) / npages < 100):
        return None

    return {
        "sections": [{"title": "Body", "text": full}],
        "tables": [],
        "full_text": full,
    }


# ── Orchestrator ──────────────────────────────────────────────────────────────

def run(limit: int | None = None, db_path: str | None = None):
    """Retrieve full text for every paper in `db_path` (defaults to the main
    papers_database.json). FULLTEXT_DIR + the network caches stay SHARED across
    corpora (keyed by paper identity), so the deep-dive corpus reuses anything
    the main run already fetched. Annotations are written back to `db_path`.
    """
    db_path = db_path or DB_PATH
    papers = _load_json(db_path, [])
    if not papers:
        raise SystemExit(f"No papers in {db_path}")
    if limit:
        papers = papers[:limit]
    os.makedirs(FULLTEXT_DIR, exist_ok=True)

    print("=" * 66)
    print(f"FULL-TEXT RETRIEVAL — {len(papers)} papers  [{db_path}]")
    print("=" * 66)

    # Which papers already have a per-paper fulltext file? (resumability)
    def ft_path(p):
        return os.path.join(FULLTEXT_DIR, paper_key(p) + ".json")

    # ── Step 1: PMCID resolution (split PMID vs DOI batches) ──────────────────
    pmid_ids, doi_ids = [], []
    key_to_pmid, key_to_doi = {}, {}
    for p in papers:
        if p.get("pmid"):
            pmid_ids.append(str(p["pmid"]))
            key_to_pmid[str(p["pmid"])] = p
        elif p.get("doi"):
            doi_ids.append(p["doi"])
            key_to_doi[p["doi"]] = p

    print(f"\n[1/3] Resolving PMCIDs — {len(pmid_ids)} via PMID, {len(doi_ids)} via DOI")
    resolved = {}
    resolved.update(resolve_pmcids(pmid_ids, batch_size=200))
    resolved.update(resolve_pmcids(doi_ids, batch_size=40))

    # attach pmcid to papers
    n_pmcid = 0
    for ident, pmcid in resolved.items():
        p = key_to_pmid.get(ident) or key_to_doi.get(ident)
        if p is not None:
            p["pmcid"] = pmcid
            n_pmcid += 1
    print(f"      PMCIDs resolved: {n_pmcid} / {len(papers)}")

    # ── Step 2: PMC full text (reuse proven path) ────────────────────────────
    need_pmc = [p for p in papers if p.get("pmcid") and not os.path.isfile(ft_path(p))]
    pmcids = list({p["pmcid"] for p in need_pmc})
    print(f"\n[2/3] Fetching PMC full text for {len(pmcids)} PMCIDs "
          f"({len(papers) - len(need_pmc)} already done/cached) ...")
    raw_xmls = fetch_pmc_batch(pmcids, save_raw=True) if pmcids else {}

    pmc_ok = 0
    pmc_nobody = []  # papers whose PMC record had no <body> → try PDF fallback
    for p in need_pmc:
        xml = raw_xmls.get(p["pmcid"])
        parsed = parse_pmc_fulltext(xml) if xml else None
        if parsed:
            _write_ft(p, parsed, "pmc", ft_path(p))
            pmc_ok += 1
        else:
            pmc_nobody.append(p)
    print(f"      PMC full text written: {pmc_ok}; body-less/restricted: {len(pmc_nobody)}")

    # ── Step 3: Unpaywall PDF fallback ───────────────────────────────────────
    # candidates: OA papers with a DOI, no fulltext file yet
    fallback = [
        p for p in papers
        if not os.path.isfile(ft_path(p)) and p.get("doi") and p.get("is_open_access")
    ]
    print(f"\n[3/3] Unpaywall PDF fallback for {len(fallback)} candidates ...")
    pdf_ok = 0
    for i, p in enumerate(fallback):
        if i % 50 == 0:
            print(f"      {i}/{len(fallback)} (pdf ok so far: {pdf_ok})")
        url = unpaywall_pdf_url(p["doi"])
        if not url:
            continue
        parsed = fetch_and_parse_pdf(url, os.path.join(PDF_DIR, paper_key(p) + ".pdf"))
        if parsed:
            _write_ft(p, parsed, "pdf", ft_path(p))
            pdf_ok += 1
    print(f"      PDF full text written: {pdf_ok}")

    # ── Annotate master DB (flags only; text lives in per-paper files) ───────
    full_db = _load_json(db_path, [])
    by_key = {paper_key(p): p for p in full_db}
    n_ft = 0
    for p in full_db:
        fp = os.path.join(FULLTEXT_DIR, paper_key(p) + ".json")
        if os.path.isfile(fp):
            meta = _load_json(fp, {})
            p["fulltext_source"] = meta.get("fulltext_source", "abstract_only")
            p["fulltext_chars"] = len(meta.get("full_text", "") or "")
            p["fulltext_path"] = os.path.relpath(fp, ".")
            p.pop("fulltext", None)  # keep DB lean — blob lives in per-paper file
            if p["fulltext_source"] in ("pmc", "pdf"):
                n_ft += 1
        else:
            p.setdefault("fulltext_source", "abstract_only")
            p["fulltext_chars"] = 0
    _save_json(db_path, full_db)

    print("\n" + "=" * 66)
    print(f"DONE. Full text for {n_ft}/{len(full_db)} papers "
          f"({100*n_ft/len(full_db):.0f}%).")
    print(f"  per-paper files: {FULLTEXT_DIR}/")
    print(f"  master DB annotated (lean): {db_path}")
    print("=" * 66)


def _write_ft(paper: dict, parsed: dict, source: str, path: str):
    rec = {
        "key": paper_key(paper),
        "pmid": paper.get("pmid"),
        "doi": paper.get("doi"),
        "pmcid": paper.get("pmcid"),
        "title": paper.get("title"),
        "journal": paper.get("journal"),
        "publication_year": paper.get("publication_year"),
        "fulltext_source": source,
        "full_text": parsed["full_text"],
        "sections": parsed["sections"],
        "tables": parsed.get("tables", []),
    }
    _save_json(path, rec)


if __name__ == "__main__":
    import sys
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run(limit=lim)
