#!/usr/bin/env python3
"""
032 — PROPAGATION TEST.

The governance rule this enforces:

    A correction is not complete until every downstream representation that can
    reproduce the old claim has been invalidated or regenerated.
    Notes do not outrank code. Banners do not outrank exports.
    Memory does not outrank the source-of-truth build.

Five corrections in this project were written and never became state. This script
is the state. Run it against a source tree; it exits nonzero if any dead claim or
stale constant is still reachable.

    python propagation_test.py <path-to-src>

Checks:
  A. dead-claim strings absent from ALL files, including export payload builders
  B. the stale R (0.041689414162...) absent everywhere
  C. every file that states the dead formula also states its refutation
  D. the replacement mechanism is present somewhere (retract-and-replace, not just retract)
"""

import json
import os
import re
import sys

# Windows consoles default to cp1252 and cannot print the subscripts that appear
# in the very strings we are hunting. Force UTF-8 so the report is readable.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, OSError):
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
CONST = json.load(open(os.path.join(HERE, "canonical_constants.json"), encoding="utf-8"))

# --- A. strings that must not survive anywhere -----------------------------
DEAD_STRINGS = [
    "c₁ = 1 PROVEN",
    "c₁ = 1 proven",
    "c₁ = 1 is",
    "c₁ = 1 forced",
    "c1 = 1 PROVEN",
    "The c₁ = 1 Proof",
    "forced by Poincaré isometry",
    "proven by Poincaré isometry",
    "PARTIALLY RESOLVED — c₁ = 1",
]

# --- B. superseded numeric constants ---------------------------------------
STALE = [CONST["SUPERSEDED_DO_NOT_USE"]["R_stale"], "041689414162"]

# --- C. files stating the formula must also state the refutation -----------
FORMULA_RE = re.compile(r"1\s*[-−]\s*1/√2|\(1 - 1/√2\)|1−1/√2")
REFUTED_MARKERS = ["-5.709", "−5.709", "not an analytic identity",
                   "false positive", "SUPERSEDED", "cancellation residue"]

# --- D. the replacement must be present somewhere --------------------------
MECHANISM_MARKERS = ["parity", "odd shell", "half-shift", "half-period",
                     "alternating character", "cancellation residue"]

TEXT_EXT = {".tsx", ".ts", ".js", ".jsx", ".md", ".txt", ".html", ".json"}


def walk(root):
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in
                 {"node_modules", ".git", "dist", "build", "__pycache__"}]
        for f in fn:
            if os.path.splitext(f)[1].lower() in TEXT_EXT:
                yield os.path.join(dp, f)


def main(root):
    fails, mech_seen = [], False
    scanned = 0

    for path in walk(root):
        try:
            txt = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        scanned += 1
        rel = os.path.relpath(path, root)

        for s in DEAD_STRINGS:
            if s in txt:
                fails.append(("A dead-claim", rel, s))

        for s in STALE:
            if s in txt and "SUPERSEDED_DO_NOT_USE" not in txt:
                fails.append(("B stale-constant", rel, s))

        if FORMULA_RE.search(txt) and not any(m in txt for m in REFUTED_MARKERS):
            fails.append(("C unrefuted-formula", rel, "states formula, no refutation"))

        if any(m in txt.lower() for m in MECHANISM_MARKERS):
            mech_seen = True

    if not mech_seen:
        fails.append(("D no-replacement", "(tree)",
                      "retraction without the replacement mechanism"))

    print("=" * 72)
    print("032 PROPAGATION TEST  |  root: %s" % root)
    print("files scanned: %d" % scanned)
    print("=" * 72)
    if not fails:
        print("\nPASS - no dead claim or stale constant is reachable.\n")
        return 0

    by_kind = {}
    for kind, rel, det in fails:
        by_kind.setdefault(kind, []).append((rel, det))
    for kind in sorted(by_kind):
        rows = by_kind[kind]
        print("\n[%s]  %d" % (kind, len(rows)))
        for rel, det in rows[:25]:
            print("    %-52s %s" % (rel[:52], det[:60]))
        if len(rows) > 25:
            print("    ... and %d more" % (len(rows) - 25))
    print("\nFAIL - %d finding(s). Correction is NOT complete. Do not seal.\n"
          % len(fails))
    return 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
