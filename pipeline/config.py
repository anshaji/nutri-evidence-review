"""Pipeline configuration — API keys, rate limits, output paths."""

import os

# ── NCBI E-Utilities ────────────────────────────────────────────────────────
NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")  # Set via: export NCBI_API_KEY=...
NCBI_TOOL = "nutri-evidence-review"
NCBI_EMAIL = "anshaji06@gmail.com"

# Rate limiting: 10 req/s with key, 3 req/s without
PUBMED_DELAY = 0.11 if NCBI_API_KEY else 0.34

# ── OpenAlex ────────────────────────────────────────────────────────────────
OPENALEX_BASE = "https://api.openalex.org/works"
OPENALEX_MAILTO = "anshaji06@gmail.com"
OPENALEX_DELAY = 0.3

# ── Output ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = "."
RAW_RESPONSE_DIR = "./raw_responses"
TOP_N_FOR_REVIEW = 100  # Number of top papers saved for LLM review

# ── PubMed retrieval ────────────────────────────────────────────────────────
PUBMED_RETMAX = 500  # Max results per query
PUBMED_BATCH_SIZE = 200  # PMIDs per efetch request
