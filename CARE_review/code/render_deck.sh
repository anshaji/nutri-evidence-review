#!/usr/bin/env bash
# Build the partner slide deck from code/build_deck.js.
#
# The deck is generated, not hand-edited — edit build_deck.js and re-run.
# Its content tracks brief/01_brief.md (the summary) but is maintained by hand:
# if the summary changes materially, update the deck script to match.
#
# Usage:  bash CARE_review/code/render_deck.sh

set -euo pipefail
CODE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! (cd "$CODE" && node -e "require.resolve('pptxgenjs')" >/dev/null 2>&1); then
  echo "installing pptxgenjs into $CODE"
  (cd "$CODE" && npm install --no-fund --no-audit pptxgenjs >/dev/null 2>&1)
fi

(cd "$CODE" && node build_deck.js)
