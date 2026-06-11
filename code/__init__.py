"""Nutrition evidence synthesis pipeline.

Numbered filenames (01_config, 02_models, …) reflect pipeline execution order
but cannot be imported directly in Python. This __init__ registers clean aliases
so that ``from code.config import X`` resolves to ``code/01_config.py``, etc.
"""

import importlib as _il
import sys as _sys

_ALIASES = {
    "config":               "01_config",
    "models":               "02_models",
    "queries":              "03_queries",
    "pubmed_client":        "04_pubmed_client",
    "openalex_client":      "05_openalex_client",
    "dedup":                "06_dedup",
    "citation_enrichment":  "07_citation_enrichment",
    "scoring":              "08_scoring",
    "fulltext_client":      "09_fulltext_client",
    "main":                 "10_main",
    "cea_client":           "12_cea_client",
    "ghcea_registry":       "13_ghcea_registry",
    "cea_main":             "14_cea_main",
    "verify":               "16_verify",
}

for _clean, _numbered in _ALIASES.items():
    _mod = _il.import_module(f".{_numbered}", __name__)
    _sys.modules[f"{__name__}.{_clean}"] = _mod
    setattr(_sys.modules[__name__], _clean, _mod)
