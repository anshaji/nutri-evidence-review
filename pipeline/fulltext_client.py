"""Full-text retrieval from PubMed Central (PMC) for open-access papers.

Stage 3.5: After scoring, before LLM review.
Retrieves structured full text (sections, tables) for top papers that have
a PMC open-access version. Papers without PMC availability retain abstract-only.
"""

from __future__ import annotations

import json
import os
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Any

from pipeline.config import (
    NCBI_API_KEY,
    NCBI_BASE,
    NCBI_EMAIL,
    NCBI_TOOL,
    PUBMED_DELAY,
    RAW_RESPONSE_DIR,
)


# ── PMID → PMCID Conversion ───────────────────────────────────────────────

def get_pmcids(pmids: list[str]) -> dict[str, str]:
    """Batch-convert PMIDs to PMCIDs using NCBI ID Converter API.

    Returns dict mapping PMID → PMCID for papers that have a PMC version.
    Papers without PMC availability are simply omitted from the result.
    """
    if not pmids:
        return {}

    converter_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
    pmid_to_pmcid: dict[str, str] = {}

    # Batch in groups of 200 (API limit)
    batch_size = 200
    for i in range(0, len(pmids), batch_size):
        batch = pmids[i:i + batch_size]
        params = urllib.parse.urlencode({
            "ids": ",".join(batch),
            "format": "json",
            "tool": NCBI_TOOL,
            "email": NCBI_EMAIL,
        })
        url = f"{converter_url}?{params}"

        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            for record in data.get("records", []):
                pmid = str(record.get("pmid", ""))
                pmcid = record.get("pmcid", "")
                if pmid and pmcid:
                    pmid_to_pmcid[pmid] = pmcid

        except Exception as e:
            print(f"  [warn] ID converter batch failed: {e}")

        time.sleep(PUBMED_DELAY)

    return pmid_to_pmcid


# ── PMC Full-Text Fetch ────────────────────────────────────────────────────

def fetch_pmc_xml(pmcid: str) -> str | None:
    """Fetch full-text XML from PMC for a single article.

    Returns raw XML string or None if unavailable.
    """
    params = {
        "db": "pmc",
        "id": pmcid,
        "rettype": "xml",
        "retmode": "xml",
        "tool": NCBI_TOOL,
        "email": NCBI_EMAIL,
    }
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    url = f"{NCBI_BASE}/efetch.fcgi?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  [warn] PMC fetch failed for {pmcid}: {e}")
        return None


def fetch_pmc_batch(pmcids: list[str], save_raw: bool = True) -> dict[str, str]:
    """Fetch full-text XML for multiple PMCIDs.

    Returns dict mapping PMCID → raw XML string.
    Saves raw XML to raw_responses/pmc/ for reproducibility.
    """
    if save_raw:
        pmc_dir = os.path.join(RAW_RESPONSE_DIR, "pmc")
        os.makedirs(pmc_dir, exist_ok=True)

    results: dict[str, str] = {}

    for i, pmcid in enumerate(pmcids):
        print(f"  Fetching full text {i+1}/{len(pmcids)}: {pmcid}", end="\r")

        # Check if we already have it cached
        if save_raw:
            cache_path = os.path.join(RAW_RESPONSE_DIR, "pmc", f"{pmcid}.xml")
            if os.path.isfile(cache_path):
                with open(cache_path) as f:
                    results[pmcid] = f.read()
                continue

        xml_text = fetch_pmc_xml(pmcid)
        if xml_text:
            results[pmcid] = xml_text
            if save_raw:
                with open(cache_path, "w") as f:
                    f.write(xml_text)

        time.sleep(PUBMED_DELAY)

    print()  # Clear the \r line
    return results


# ── PMC XML Parsing ────────────────────────────────────────────────────────

def _get_text_recursive(elem: ET.Element) -> str:
    """Extract all text from an element and its children, stripping tags."""
    parts = []
    if elem.text:
        parts.append(elem.text)
    for child in elem:
        parts.append(_get_text_recursive(child))
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def _parse_section(sec_elem: ET.Element) -> dict[str, str]:
    """Parse a <sec> element into title + body text."""
    title_elem = sec_elem.find("title")
    title = _get_text_recursive(title_elem).strip() if title_elem is not None else ""

    paragraphs = []
    for p in sec_elem.findall(".//p"):
        text = _get_text_recursive(p).strip()
        if text:
            paragraphs.append(text)

    return {"title": title, "text": "\n\n".join(paragraphs)}


def _parse_table(table_wrap: ET.Element) -> dict[str, str]:
    """Parse a <table-wrap> element into label + caption + simplified content."""
    label_elem = table_wrap.find("label")
    label = _get_text_recursive(label_elem).strip() if label_elem is not None else ""

    caption_elem = table_wrap.find("caption")
    caption = ""
    if caption_elem is not None:
        caption_parts = []
        for p in caption_elem.findall(".//p"):
            caption_parts.append(_get_text_recursive(p).strip())
        if not caption_parts:
            caption_parts.append(_get_text_recursive(caption_elem).strip())
        caption = " ".join(caption_parts)

    # Extract table content as plain text (simplified)
    table_elem = table_wrap.find(".//table") or table_wrap.find(".//{http://www.w3.org/1999/xhtml}table")
    table_text = ""
    if table_elem is not None:
        rows = []
        for tr in table_elem.findall(".//{http://www.w3.org/1999/xhtml}tr") or table_elem.findall(".//tr"):
            cells = []
            for cell in list(tr):
                cells.append(_get_text_recursive(cell).strip())
            if cells:
                rows.append(" | ".join(cells))
        table_text = "\n".join(rows)

    return {"label": label, "caption": caption, "content": table_text}


def parse_pmc_fulltext(xml_text: str) -> dict[str, Any] | None:
    """Parse PMC XML into structured full-text content.

    Returns dict with keys:
        - sections: list of {title, text} dicts
        - tables: list of {label, caption, content} dicts
        - full_text: concatenated plain text of all sections
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None

    # Find the article body — try multiple paths
    body = root.find(".//body")
    if body is None:
        return None

    sections = []
    for sec in body.findall("sec"):
        parsed = _parse_section(sec)
        if parsed["text"]:
            sections.append(parsed)

    # If no <sec> elements, get all paragraphs directly
    if not sections:
        paragraphs = []
        for p in body.findall(".//p"):
            text = _get_text_recursive(p).strip()
            if text:
                paragraphs.append(text)
        if paragraphs:
            sections.append({"title": "Body", "text": "\n\n".join(paragraphs)})

    # Parse tables
    tables = []
    for table_wrap in root.findall(".//table-wrap"):
        parsed = _parse_table(table_wrap)
        if parsed["caption"] or parsed["content"]:
            tables.append(parsed)

    # Build concatenated full text
    full_text_parts = []
    for sec in sections:
        if sec["title"]:
            full_text_parts.append(f"## {sec['title']}")
        full_text_parts.append(sec["text"])
        full_text_parts.append("")  # blank line between sections

    full_text = "\n".join(full_text_parts).strip()

    if not full_text:
        return None

    return {
        "sections": sections,
        "tables": tables,
        "full_text": full_text,
    }


# ── Main Coordinator ───────────────────────────────────────────────────────

def retrieve_fulltext(papers: list[dict]) -> list[dict]:
    """Retrieve PMC full text for top papers that have open-access PMC versions.

    Mutates papers in-place, adding:
        - fulltext_source: "pmc" | "abstract_only"
        - fulltext: structured dict (sections, tables, full_text) or None
        - pmcid: PMC ID if available

    Returns the same list with fulltext fields populated.
    """
    # Get PMIDs from papers that have them
    pmid_papers: dict[str, dict] = {}
    for paper in papers:
        pmid = paper.get("pmid", "")
        if pmid:
            pmid_papers[pmid] = paper

    print(f"\n{'='*60}")
    print(f"STAGE 3.5: Full-Text Retrieval (PMC Open Access)")
    print(f"{'='*60}")
    print(f"  Papers with PMIDs: {len(pmid_papers)}")

    # Step 1: Convert PMIDs to PMCIDs
    print("  Converting PMIDs → PMCIDs...")
    pmid_list = list(pmid_papers.keys())
    pmid_to_pmcid = get_pmcids(pmid_list)
    print(f"  PMC-available papers: {len(pmid_to_pmcid)} / {len(pmid_list)}")

    # Step 2: Fetch full text for available PMCIDs
    pmcids = list(pmid_to_pmcid.values())
    if pmcids:
        print(f"  Fetching full text from PMC...")
        raw_xmls = fetch_pmc_batch(pmcids, save_raw=True)
        print(f"  Successfully fetched: {len(raw_xmls)} full-text articles")
    else:
        raw_xmls = {}

    # Step 3: Parse and attach to papers
    fulltext_count = 0
    pmcid_to_pmid = {v: k for k, v in pmid_to_pmcid.items()}

    for pmcid, xml_text in raw_xmls.items():
        parsed = parse_pmc_fulltext(xml_text)
        if parsed and pmcid in pmcid_to_pmid:
            pmid = pmcid_to_pmid[pmcid]
            if pmid in pmid_papers:
                pmid_papers[pmid]["fulltext"] = parsed
                pmid_papers[pmid]["fulltext_source"] = "pmc"
                pmid_papers[pmid]["pmcid"] = pmcid
                fulltext_count += 1

    # Mark remaining papers as abstract-only
    for paper in papers:
        if "fulltext_source" not in paper:
            paper["fulltext_source"] = "abstract_only"
            paper["fulltext"] = None
            # Still note PMCID if we found it (even if fetch failed)
            pmid = paper.get("pmid", "")
            if pmid in pmid_to_pmcid:
                paper["pmcid"] = pmid_to_pmcid[pmid]

    print(f"\n  Results:")
    print(f"    Full text retrieved: {fulltext_count}")
    print(f"    Abstract only:      {len(papers) - fulltext_count}")
    print(f"{'='*60}\n")

    return papers
