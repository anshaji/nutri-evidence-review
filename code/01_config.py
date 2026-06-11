"""Pipeline configuration — API keys, rate limits, output paths."""

import os


def _load_dotenv():
    """Load .env file from project root if it exists (stdlib-only)."""
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.isfile(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key, value = key.strip(), value.strip()
                # Don't override existing env vars
                if key not in os.environ:
                    os.environ[key] = value


_load_dotenv()

# ── NCBI E-Utilities ────────────────────────────────────────────────────────
NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")  # Loaded from .env or environment
NCBI_TOOL = "nutri-evidence-review"
NCBI_EMAIL = "anshaji06@gmail.com"

# Rate limiting: 10 req/s with key, 3 req/s without
PUBMED_DELAY = 0.11 if NCBI_API_KEY else 0.34

# ── OpenAlex ────────────────────────────────────────────────────────────────
OPENALEX_BASE = "https://api.openalex.org/works"
OPENALEX_MAILTO = "anshaji06@gmail.com"
OPENALEX_DELAY = 0.3

# ── Output ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = "./data"
RAW_RESPONSE_DIR = "./data/raw_responses"
TOP_N_FOR_REVIEW = 200  # Number of top papers saved for LLM review (Phase 1)

# ── PubMed retrieval ────────────────────────────────────────────────────────
PUBMED_RETMAX = 500  # Max results per query
PUBMED_BATCH_SIZE = 200  # PMIDs per efetch request

# ── Scoring ─────────────────────────────────────────────────────────────────
POPULATION_SCORE_MAX = 10  # Component 8: under-5 / women-of-reproductive-age relevance

# ── Phase 2: Cost-Effectiveness (per shortlisted intervention) ──────────────
CEA_PER_INTERVENTION_RETMAX = 100  # Max PubMed results per intervention CEA search
CEA_OPENALEX_MAX_PAGES = 2  # Keep Phase 2 OpenAlex targeted/small
SHORTLIST_PATH = "./data/shortlist.json"  # Phase 1 → Phase 2 handoff (human-authored)
CEA_OUTPUT_PATH = "./data/cea_by_intervention.json"  # Phase 2 output
GHCEA_LOCAL_PATH = "./data/ghcea_registry.csv"  # Manual one-time CEA registry download
DCP3_LOCAL_PATH = "./data/dcp3_annex7a.csv"  # Optional DCP3 Annex 7A extract
