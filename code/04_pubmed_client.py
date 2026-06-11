"""PubMed E-Utilities client for Tracks A and B.

Handles esearch (query → PMIDs) and efetch (PMIDs → full article metadata).
Parses PubMed XML into unified Paper format.
"""

from __future__ import annotations

import os
import sys
import time
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

from .config import (
    NCBI_BASE, NCBI_API_KEY, NCBI_TOOL, NCBI_EMAIL,
    PUBMED_DELAY, PUBMED_RETMAX, PUBMED_BATCH_SIZE, RAW_RESPONSE_DIR,
)
from .models import Paper, extract_cochrane_id


def _ncbi_params() -> dict:
    """Common parameters for all NCBI requests."""
    params = {"tool": NCBI_TOOL, "email": NCBI_EMAIL}
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    return params


def esearch(query: str, retmax: int = PUBMED_RETMAX) -> tuple[list[str], int]:
    """
    Submit a PubMed search and return (list of PMIDs, total count).
    """
    params = {
        **_ncbi_params(),
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
        "usehistory": "n",
    }
    url = f"{NCBI_BASE}/esearch.fcgi?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NutriEvidenceBot/2.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            result = data.get("esearchresult", {})
            pmids = result.get("idlist", [])
            total = int(result.get("count", 0))
            return pmids, total
    except Exception as e:
        print(f"  [esearch ERROR] {e}", file=sys.stderr)
        return [], 0


def efetch_batch(pmids: list[str]) -> str:
    """
    Fetch full article XML for a batch of PMIDs.
    Batches in groups of PUBMED_BATCH_SIZE to avoid URL length limits.
    Returns concatenated XML text.
    """
    all_xml_parts = []

    for i in range(0, len(pmids), PUBMED_BATCH_SIZE):
        batch = pmids[i:i + PUBMED_BATCH_SIZE]
        params = {
            **_ncbi_params(),
            "db": "pubmed",
            "id": ",".join(batch),
            "rettype": "xml",
            "retmode": "xml",
        }
        url = f"{NCBI_BASE}/efetch.fcgi?{urllib.parse.urlencode(params)}"

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "NutriEvidenceBot/2.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                xml_text = resp.read().decode()
                all_xml_parts.append(xml_text)
        except Exception as e:
            print(f"  [efetch ERROR] batch {i//PUBMED_BATCH_SIZE + 1}: {e}", file=sys.stderr)

        time.sleep(PUBMED_DELAY)

    return "\n".join(all_xml_parts)


def parse_pubmed_xml(xml_text: str) -> list[Paper]:
    """
    Parse PubmedArticleSet XML into list of Paper dicts.
    Handles structured abstracts, multiple MeSH headings, and missing fields.
    """
    papers = []

    # Handle multiple XML documents from batch concatenation
    # Wrap in a root if needed
    if xml_text.count("<?xml") > 1:
        # Multiple XML docs concatenated — extract PubmedArticle elements
        articles_xml = []
        for part in xml_text.split("<?xml"):
            if "PubmedArticle" in part:
                articles_xml.append("<?xml" + part if not part.startswith("<?xml") else part)
        # Re-wrap
        combined = "<PubmedArticleSet>"
        for part in articles_xml:
            try:
                root = ET.fromstring(part)
                for article in root.iter("PubmedArticle"):
                    combined += ET.tostring(article, encoding="unicode")
            except ET.ParseError:
                continue
        combined += "</PubmedArticleSet>"
        xml_text = combined

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"  [XML PARSE ERROR] {e}", file=sys.stderr)
        return papers

    for article in root.iter("PubmedArticle"):
        paper = _parse_article(article)
        if paper:
            papers.append(paper)

    return papers


def _parse_article(article: ET.Element) -> Paper | None:
    """Parse a single PubmedArticle element into a Paper dict."""
    citation = article.find("MedlineCitation")
    if citation is None:
        return None

    # PMID
    pmid_elem = citation.find("PMID")
    pmid = pmid_elem.text if pmid_elem is not None else None
    if not pmid:
        return None

    art = citation.find("Article")
    if art is None:
        return None

    # Title
    title_elem = art.find("ArticleTitle")
    title = _get_text(title_elem) if title_elem is not None else ""

    # Abstract (handle structured abstracts)
    abstract = ""
    abstract_elem = art.find("Abstract")
    if abstract_elem is not None:
        parts = []
        for text_elem in abstract_elem.findall("AbstractText"):
            label = text_elem.get("Label", "")
            text = _get_text(text_elem)
            if label and text:
                parts.append(f"{label}: {text}")
            elif text:
                parts.append(text)
        abstract = " ".join(parts)

    # Publication year
    pub_year = None
    pub_date = art.find("Journal/JournalIssue/PubDate")
    if pub_date is not None:
        year_elem = pub_date.find("Year")
        if year_elem is not None and year_elem.text:
            try:
                pub_year = int(year_elem.text)
            except ValueError:
                pass
        # Fallback: MedlineDate
        if pub_year is None:
            medline_date = pub_date.find("MedlineDate")
            if medline_date is not None and medline_date.text:
                try:
                    pub_year = int(medline_date.text[:4])
                except (ValueError, IndexError):
                    pass

    # Journal
    journal_elem = art.find("Journal/Title")
    journal = journal_elem.text if journal_elem is not None else ""

    # Authors (first 5)
    authors = []
    author_list = art.find("AuthorList")
    if author_list is not None:
        for author in list(author_list.findall("Author"))[:5]:
            last = author.find("LastName")
            fore = author.find("ForeName")
            if last is not None and last.text:
                name = last.text
                if fore is not None and fore.text:
                    name += f" {fore.text}"
                authors.append(name)

    # DOI
    doi = None
    pubmed_data = article.find("PubmedData")
    if pubmed_data is not None:
        for aid in pubmed_data.findall("ArticleIdList/ArticleId"):
            if aid.get("IdType") == "doi" and aid.text:
                doi = aid.text
                break

    # Publication types
    pub_types = []
    pub_type_list = art.find("PublicationTypeList")
    if pub_type_list is not None:
        for pt in pub_type_list.findall("PublicationType"):
            if pt.text:
                pub_types.append(pt.text)

    # MeSH terms
    mesh_terms = []
    mesh_list = citation.find("MeshHeadingList")
    if mesh_list is not None:
        for heading in mesh_list.findall("MeshHeading"):
            desc = heading.find("DescriptorName")
            if desc is not None and desc.text:
                mesh_terms.append(desc.text)

    # Classify study type from publication types
    study_type = _classify_from_pubtypes(pub_types, title, abstract)

    return Paper(
        id=f"pmid:{pmid}",
        title=title,
        abstract=abstract,
        publication_year=pub_year,
        authors=authors,
        journal=journal,
        doi=doi,
        pmid=pmid,
        openalex_id=None,
        source_db="pubmed",
        query_origin="",  # Set by caller
        study_type=study_type,
        publication_type=pub_types,
        mesh_terms=mesh_terms,
        cited_by_count=0,  # Filled by citation enrichment
        is_open_access=False,  # PubMed doesn't reliably report this
        relevance_score=0.0,
        tier="",  # Set by caller
        cochrane_id=extract_cochrane_id(doi, journal),  # Version-independent accession
        superseded_by=None,
    )


def _get_text(elem: ET.Element) -> str:
    """Extract all text content from an element, including mixed content."""
    return "".join(elem.itertext()).strip()


def _classify_from_pubtypes(pub_types: list[str], title: str, abstract: str) -> str:
    """Classify study type using authoritative PubMed publication types."""
    pt_set = {pt.lower() for pt in pub_types}
    combined = (title + " " + abstract).lower()

    if "meta-analysis" in pt_set:
        if "systematic review" in combined:
            return "Systematic Review & Meta-Analysis"
        return "Meta-Analysis"
    if "systematic review" in pt_set:
        return "Systematic Review"
    if "review" in pt_set:
        if "cochrane" in combined or "cochrane database" in combined:
            return "Cochrane Review"
        if "umbrella review" in combined:
            return "Umbrella Review"
        return "Review"
    if "randomized controlled trial" in pt_set:
        return "RCT"
    if "practice guideline" in pt_set or "guideline" in pt_set:
        return "Practice Guideline"
    if "cost-effectiveness" in combined or "cost-benefit" in combined:
        return "Cost-Effectiveness Analysis"
    return "Article"


def fetch_pubmed_track(query_def: dict, type_filter: str, tier: str) -> list[Paper]:
    """
    Run a single PubMed query end-to-end: esearch → efetch → parse.
    Returns list of Papers with query_origin and tier set.
    """
    from .queries import build_pubmed_query

    full_query = build_pubmed_query(query_def, type_filter)
    name = query_def["name"]

    # Step 1: Search
    pmids, total = esearch(full_query)
    if not pmids:
        return []

    print(f"    Found {total} results, fetching {len(pmids)}...", file=sys.stderr)

    # Step 2: Fetch XML
    time.sleep(PUBMED_DELAY)
    xml_text = efetch_batch(pmids)

    # Save raw response
    os.makedirs(RAW_RESPONSE_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = os.path.join(RAW_RESPONSE_DIR, f"pubmed_{tier}_{name}_{ts}.xml")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(xml_text)

    # Step 3: Parse
    papers = parse_pubmed_xml(xml_text)

    # Set provenance
    for p in papers:
        p["query_origin"] = name
        p["tier"] = tier

    return papers


def fetch_pubmed_cea(query_def: dict) -> list[Paper]:
    """
    Run the cost-effectiveness query (Track B) — no publication type filter.
    """
    query = query_def["query"]
    name = query_def["name"]

    # Step 1: Search
    pmids, total = esearch(query)
    if not pmids:
        return []

    print(f"    Found {total} results, fetching {len(pmids)}...", file=sys.stderr)

    # Step 2: Fetch XML
    time.sleep(PUBMED_DELAY)
    xml_text = efetch_batch(pmids)

    # Save raw response
    os.makedirs(RAW_RESPONSE_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_path = os.path.join(RAW_RESPONSE_DIR, f"pubmed_cea_{name}_{ts}.xml")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(xml_text)

    # Step 3: Parse
    papers = parse_pubmed_xml(xml_text)

    # Set provenance
    for p in papers:
        p["query_origin"] = name
        p["tier"] = "cea"

    return papers
