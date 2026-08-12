#!/usr/bin/env bash
# Assemble the CARE deep-dive report from its sections and render to .docx.
#
# Markdown is the source of truth: the verifier (code/17_verify_synthesis.py)
# reads markdown, and it is what produces the "0 not-in-corpus" guarantee. The
# .docx is generated from it, never hand-edited — edit report/*.md and re-run.
#
# Usage:  bash CARE_review/code/render_report.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CARE="$ROOT/CARE_review"
SECTIONS="$CARE/report"
MD="$CARE/CARE_DEEPDIVE_REPORT.md"
DOCX="$CARE/CARE_DEEPDIVE_REPORT.docx"
REFERENCE="$CARE/code/assets/reference.docx"

if [ ! -f "$REFERENCE" ]; then
  echo "reference.docx missing — building it"
  python3 "$CARE/code/build_reference_docx.py"
fi

echo "assembling sections -> $(basename "$MD")"
# Join with a blank line between files. Without this, a section file that does
# not end in a blank line lets the next file's "# Chapter" title be swallowed
# as a lazy continuation of the preceding paragraph — it then renders as body
# text rather than a heading, silently and only in the .docx.
: > "$MD"
for section in "$SECTIONS"/0*.md; do
  cat "$section" >> "$MD"
  printf '\n\n' >> "$MD"
done

echo "rendering -> $(basename "$DOCX")"
pandoc "$MD" \
  --from=markdown+pipe_tables+yaml_metadata_block+footnotes \
  --to=docx \
  --reference-doc="$REFERENCE" \
  --toc --toc-depth=2 \
  --standalone \
  --output="$DOCX"

echo
echo "verifying every numeric claim against the corpus"
python3 "$ROOT/code/17_verify_synthesis.py" "$MD" \
  "$CARE/data/deepdive_corpus.json" \
  "$CARE/data/evidence_db.json" 2>/dev/null \
  | grep -E "Cited claims|Unsourced" || true

# ---------------------------------------------------------------- short version
BRIEF_SRC="$CARE/brief"
BRIEF_MD="$CARE/CARE_DEEPDIVE_SUMMARY.md"
BRIEF_DOCX="$CARE/CARE_DEEPDIVE_SUMMARY.docx"

if [ -d "$BRIEF_SRC" ]; then
  echo
  echo "assembling summary -> $(basename "$BRIEF_MD")"
  : > "$BRIEF_MD"
  for section in "$BRIEF_SRC"/0*.md; do
    cat "$section" >> "$BRIEF_MD"
    printf '\n\n' >> "$BRIEF_MD"
  done

  echo "rendering -> $(basename "$BRIEF_DOCX")"
  pandoc "$BRIEF_MD" \
    --from=markdown+pipe_tables+yaml_metadata_block+footnotes \
    --to=docx \
    --reference-doc="$REFERENCE" \
    --standalone \
    --output="$BRIEF_DOCX"

  echo "verifying summary"
  python3 "$ROOT/code/17_verify_synthesis.py" "$BRIEF_MD" \
    "$CARE/data/deepdive_corpus.json" \
    "$CARE/data/evidence_db.json" 2>/dev/null \
    | grep -E "Cited claims|Unsourced" || true
fi

echo
ls -lh "$MD" "$DOCX" "$BRIEF_MD" "$BRIEF_DOCX" 2>/dev/null | awk '{print "  " $9 "  " $5}'
