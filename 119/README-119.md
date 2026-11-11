# 119 — The bowl and the two inputs: what A is, and 028's last outside number closed

**2026-10-10.** Drafted by Claude (Opus seat) in the Figma Make session, at Ash's
word ("add all this to the ledger — not append, but add a new entry"). Not yet
sealed. Nothing earlier is edited; this entry stands beside them.

## Part 1 — What A is

Squash the cube: keep one side at 1, set the other two to b (the (1, b, b) family).
Write x = ln b and ε = 24R − 1. Near the cube:

    ε(x) ≈ ε₀ + s·x + A·x² + …

| | value | grade |
|---|---|---|
| ε₀ | 5.4595046537…×10⁻⁴ | CONFIRMED (c2-highprec.py; well-curvature-A.py agrees to ~11 digits) |
| s (odd slope) | −18.3259647 | sealed, 098 |
| A | 0.58260865319173… | CONFIRMED; `well-curvature-A.py` here gives 0.582608650241 (8 digits, float) |

Definition: A = ½(ε′(1) + ε″(1)) in derivatives with respect to b. That is the same
as ½ d²ε/dx² at x = 0, because changing variables to ln b produces ε′ + ε″.

Consequence (098): the slope is large and the gap is small, so the ratio hits exactly
1/24 a hair off the cube, at ln b* ≈ ε₀/|s| ≈ 3×10⁻⁵. A gives the correction to that
estimate. No closed form for A is known.

**Naming clash, recorded rather than fixed:** 096 calls this number "c₂". On the
site, c₂ is the q² fit residual 0.0030314…, a different number. Read "c₂" by context.

## Part 2 — 028 App. A.4 input, closed

028 certified the e^(−2π√2) coefficient (−67.193…) but listed one input it did not
certify itself: ζ(−½) and β(−½) ("routine"). `certify-zeta-beta.py` does it:

- reflection: ζ(−½) = −ζ(3/2)/(4π), β(−½) = β(3/2)/π,
  β(3/2) = 4^(−3/2)[ζ(3/2,¼) − ζ(3/2,¾)]
- Hurwitz values by Euler–Maclaurin (N = 60, P = 30), remainder bounded and added
  as an interval, all in mpmath.iv
- widths 9.6×10⁻⁷⁶ and 1.6×10⁻⁷⁵ (028 used 1e-45); mpmath's values lie inside

    ζ(−½) = −0.2078862249773545660173067253970493022262685312876725376101…
    β(−½) =  0.2751797412288202501166651676562889559119469647154551964909…

Grade: CERTIFIED, conditional on mpmath.iv being correct (the same trust 028 places in it).

## Part 3 — Scars placed on the site (correction-beside, per 052)

Ten "[CORRECTION · ledger NNN]" notes in 7 files of the Geometry of Zero site. Each
sits next to an old "c₁ = 1", "1 − 1/√2 proved in 3-D", or old-R claim. Nothing was
deleted. The EEAAO I–IV pages carry an audit banner, plus a new EEAAO V and an
"In Memoriam" page for the dead claims. c2-highprec.py has an appended note: its
"residual 8e-62" is true by construction, since c₂ is defined as the leftover.

## What this does NOT do

- It does not certify R itself. The 50 digits are converged, not enclosed.
- It does not give a formula for A or for c₂.
- It does not derive the 1/24 or the ratio equality (098 "derivable, not yet derived").

## Plain version (for Ash)

There are three kinds of number here.
- **R** is the ratio.
- **The gap** is how far R misses 1/24.
- **A** is how the miss changes if you squash the box.

A is the shape of the bowl. This entry also finishes a chore 028 left open: two
numbers it had borrowed from a library are now pinned down by our own code with a
guaranteed error box. Nothing new is explained. Things we already had are now
better nailed down.

## Files

- `well-curvature-A.py` / `.out`: A and ε₀ from the definition
- `certify-zeta-beta.py` / `.out`: the interval enclosures (needs mpmath)
