#!/usr/bin/env bash
# Render both CARE report variants. Clean version is the source of truth.
set -euo pipefail
cd "$(dirname "$0")"
COMMON="--from=markdown+pipe_tables+yaml_metadata_block+footnotes+implicit_figures"
REF="--reference-doc=../code/assets/reference.docx --toc --toc-depth=1 --standalone --resource-path=."
python3 make_figures.py >/dev/null && echo "figures rebuilt"
pandoc CARE_FINAL_REPORT.md $COMMON $REF -o CARE_FINAL_REPORT.docx && echo "rendered CARE_FINAL_REPORT.docx (clean)"
python3 make_marked.py
pandoc CARE_FINAL_REPORT_MARKED.md ${COMMON}+mark $REF -o CARE_FINAL_REPORT_MARKED.docx && echo "rendered CARE_FINAL_REPORT_MARKED.docx (highlighted)"
