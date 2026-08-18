#!/bin/sh
# 034 — CANONICAL CONSTANTS GATE
#
# Greg's rule as a build failure: one canonical constant object, and a gate that
# fails when a deprecated literal reappears outside a declared historical record.
#
# Design notes, both learned by getting them wrong first:
#  1. The allowlist MUST be external. Sealed ledger entries quote dead values in
#     order to document them, and a sealed file cannot be edited to carry an
#     inline marker without breaking its hash.
#  2. It must be pattern-based, not substring-based, so "any numbered ledger
#     folder is a historical record" is expressible independent of how the tree
#     is invoked (. vs absolute path vs repo-relative).
#
# Usage:  ./constants_gate.sh <tree>
#         ln -s "$PWD/constants_gate.sh" <repo>/.git/hooks/pre-commit
HERE=$(cd "$(dirname "$0")" && pwd)
ALLOW="$HERE/constants_gate.allow"
STALE='041689414162'
DEAD='c₁ = 1 PROVEN|c₁ = 1 proven|c₁ = 1 forced|forced by Poincaré isometry|proven by Poincaré isometry'
TREE="${1:-.}"
fail=0

PATS=$(grep -vE '^\s*(#|$)' "$ALLOW" 2>/dev/null | paste -sd'|' -)
[ -z "$PATS" ] && PATS='^$'

echo "── canonical constants gate ── $TREE"
for f in $(grep -rlE "$STALE|$DEAD" "$TREE" --exclude-dir=node_modules --exclude-dir=.git 2>/dev/null); do
  printf '%s\n' "$f" | grep -qE "$PATS" && continue
  grep -qE "$STALE" "$f" && { echo "  STALE R    $f"; fail=1; }
  grep -qE "$DEAD"  "$f" && { echo "  DEAD CLAIM $f"; fail=1; }
done

if [ "$fail" -eq 0 ]; then echo "  PASS — canonical R is the only R; no dead claim reachable."
else
  echo ""
  echo "  FAIL — import from 032/canonical_constants.json."
  echo "         To quote a superseded value deliberately, add a path pattern to"
  echo "         $ALLOW"
fi
exit $fail
