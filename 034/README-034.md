# 034 — The corrections manifest, the build gate, and three measurements

**2026-08-16. Ash Korth + Claude (Opus 5), with GPT ("Greg") and the Figma agent.**
Follows 032 (parity law, register, orientation-blindness, propagation failure).

## Contents

- `site-corrections-manifest.md` — **the work order.** Eight live claims that a
  written correction already contradicts, each paired with its receipt, ordered
  by public exposure. Plus four supporting defects and a sequencing rule.
- `constants_gate.sh` / `.allow` — the propagation rule as a build failure.
  Symlinks into `.git/hooks/pre-commit`. Passes on this ledger, fails on zip 12.
  The allowlist is external and pattern-based **by necessity**: sealed entries
  quote dead values in order to document them and cannot be edited to carry an
  inline marker without breaking their hash.
- `zip12_propagation.txt` — the regression. 75 → 66 findings looks like progress;
  decomposed it is A −14, C −1, **B +6**, with the stale R reaching two brand-new
  pages. Aggregate error count is a misleading governance metric.
- `casimir_component_decomposition.txt` — independent component split of
  Z_PPP − Z_APP. The zero-mode subtraction is **exactly** −1/√π in PPP and
  **exactly 0** in APP; the smooth term cancels perfectly; the dual sector is
  0.014% here versus everything in 028's split. **Existence of the asymmetry is
  convention-free; its share is not** (220.8% here, 124.6% on the /correction
  page). State the absence, never the percentage.
- `scar_control.py` + output, `projection_hierarchy.txt` — control experiment for
  the scar model. Scar size is **relative to the projection**: one bit hidden
  under (δ,p), three bits under |δ|. There is no observer-independent residue.
- `cott-anchor-permutation-test.md` — the four-anchor orientation test on James's
  slot algebra. Verdict **UNDERDETERMINED / MAP NOT DEFINED** — the honest third
  outcome. It names the missing axiom instead of letting the torus drawing supply
  it. Related finding: the retracted four-element carrier also invalidates the
  quarter-turn phase map and therefore the winding computation det = 2.

## The one thing this entry does not contain

Any correction actually applied to the site. All eight items remain live. The
blocker is the source-of-truth decision recorded in 032.

## Corrections to our own prior work, logged here rather than hidden

- The pole/zero-mode "dominance" figure quoted earlier in session was computed
  from the /correction page's own brackets — a page already shown to be 3.4%
  wrong. Recomputed independently here.
- A draft of `constants_gate.sh` was briefly written into sealed `032/`,
  violating the very invariant audited that morning. Removed; 032's seal
  re-verified intact; the gate lives here.
- The first allowlist design required editing files to exempt them, which is
  impossible for sealed entries. Redesigned as external patterns.
