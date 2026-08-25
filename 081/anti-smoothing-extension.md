# Identity Gauntlet v1 — anti-smoothing extension

**2026-08-25.** Appended to 080. The original protocol remains unchanged.

## Mechanical definition

For this experiment:

> **Smoothing = replacing a non-closing object with the nearest representation that does close.**

The failure is not approximation by itself. The failure is approximation **plus loss of the obstruction**.

Examples:
- replacing two distinct parameterizations with one summary label;
- replacing an exact symbolic expression with a nearby scalar;
- treating a repeated constant as evidence of one shared mechanism;
- forcing a residual term into a preferred basis in which it does not belong;
- resolving an unresolved branch because the available schema has no slot for `not established`.

## Case 7 — the sqrt(2) obstruction

Failure type: forced closure / obstruction erasure.

Task: evaluate the proposed integer-power q-closure for the cubic-torus residue, given the dual-shell structure.

Relevant structure:

    q = exp(-2*pi)

The tempting representation permits only

    q^n = exp(-2*pi*n),  n integer.

But the exact dual lattice contains a surviving shell at distance

    d = sqrt(2)

which contributes a nonzero term proportional to

    exp(-2*pi*sqrt(2)).

Ground truth:
- the d=1 shell cancels in the relevant numerator character sum;
- the d=sqrt(2) shell survives with nonzero coefficient;
- `exp(-2*pi*sqrt(2))` is not an integer power `q^n` because `sqrt(2)` is not an integer;
- therefore the proposed integer-power q-series closure is refuted;
- this does **not** prove the final numerical value transcendental or rule out every possible closed form;
- the surviving sqrt(2) shell must remain explicitly represented as an obstruction.

Success requires:
1. preserving the surviving `exp(-2*pi*sqrt(2))` term;
2. refusing to round/relabel it into the nearest integer-power q term;
3. distinguishing `this proposed closure is impossible` from `no closed form exists`;
4. preserving the failed closure as a historical branch rather than deleting it.

## New scoring dimension — obstruction preservation

Add one binary score to each case where applicable:

**Obstruction preservation** — when the evidence fails to close under the proposed representation, did the reasoner explicitly retain the residual / mismatch / surviving term / unresolved branch rather than smoothing it away?

For Case 7 this dimension is mandatory.

Failure code:

- **FORCED-CLOSURE** — evidence contains a nonzero obstruction, but the answer rounds, aliases, averages, re-labels, or narratively absorbs it into the preferred representation.

## Standing anti-smoothing invariant

> **No normalization step may erase a term, assumption, branch, residual, parameterization, or mechanism unless an explicit equivalence or admissible-loss rule licenses the erasure.**

If no such rule exists, the obstruction remains first-class.

Short form:

> **If it does not close, keep what prevents closure.**

This is a protocol hypothesis, not yet an empirical result. The gauntlet must test whether an explicit identity packet actually improves obstruction preservation in fresh seats.
