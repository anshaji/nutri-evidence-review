#!/usr/bin/env bash
# Render the CMAM policy report. CMAM_REPORT.md is the single source of truth.
set -euo pipefail
cd "$(dirname "$0")"
report_python="${CMAM_PYTHON:-$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3}"
"$report_python" build_report.py
