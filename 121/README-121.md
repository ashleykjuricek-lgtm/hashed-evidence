# 121 — What if it's attraction: the twist's sign across dimension

**2026-10-19.** Drafted by Claude (Opus seat) at Ash's word ("yeah and … try to
expound on something I can't see"). Not yet sealed. Nothing earlier is edited.

## The question

Read the Casimir-type energy by its sign. Negative means the box wants to shrink
(attraction). Positive means it wants to grow (repulsion). Both readings, vacuum
energy and Jaffe's charge-to-charge force, agree on the sign. So this entry needs
no decision about what the vacuum is.

## Dimension as a dial

Θ(t) = θ(t)^d, using 1-D theta functions raised to a real power, and the same Mellin
split at t = 1 as 120. At integer d this reproduces the lattice sums: d = 3 gives
R = 0.0416894146, matching the canonical R (`attraction-dimension.out`). Between
integers it is a **definition**, not physics.

| d | plain (PPP) | twisted (APP) | R |
|---|---|---|---|
| 1 | −0.1667 | +0.0833 (push) | −1/2 |
| 2 | −0.2288 | +0.0237 (push) | −0.10355 |
| **2.639069** | | **0, balance** | 0 |
| **2.999782** | | | **exactly 1/24** |
| 3 | −0.2666 | −0.0111 (pull) | 0.0416894 |
| 4 | −0.2967 | −0.0377 (pull) | 0.12696 |

The plain energy is attractive at every d. Only the twisted one changes sign.

## Scar on 120-era chat (not sealed anywhere)

In chat I said three dimensions "sits just past the crossover". **Wrong as stated.**
The balance point is d* = 2.639, about 0.36 below 3. That isn't close. 3-D is
well inside the attraction side.

## What the dial does show

R(d) is smooth and rises steadily, by about 0.1 per unit of d near 3. It passes
1/24 at d = 2.99978, which is 2.2×10⁻⁴ below 3. That nearness is not new
information: it is the same small gap (24R − 1 = 5.5×10⁻⁴) divided by the slope.
**So the dial confirms that nothing structural pins 1/24 to d = 3.** The curve is
just passing through. Grade: OBSERVED.

## The thing you can't see (Claude's reading, marked mine)

The ledger has treated "R ≈ 1/24" as a property of the cube. The dial suggests
that's the wrong frame. 1/24 is not special to R(d) at all. The curve crosses 1/24
the same way it crosses 0.04 or 0.05.

1/24 *is* special in 1-D, though: ζ(−1,½) = +1/24 (120 C5). That's the twisted
1-D energy itself, not a ratio. So there are two candidate stories:
- **(a) coincidence:** a smooth curve lands near a famous number at an integer.
- **(b) inheritance:** the 3-D ratio remembers the 1-D twisted energy, because the
  twist lives on one axis. If so, the leading 1/24 would come from the twisted
  axis's own 1-D energy, normalised by the plain 3-D one. The leftover 5.5×10⁻⁴
  would then be the cross-talk between that axis and the other two.

(b) is testable. Compute the 3-D ratio with the two untwisted axes made very long
or very short (the (1,b,b) family at extreme b), and see whether the leading 1/24
separates cleanly from a term that dies off. If R tends to a limit built from
1/24, (b) has teeth. If not, (a) wins.

**Tested the same day (`inheritance-test.py`):**

| b | 0.25 | 0.5 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| R | 0.855 | 0.550 | 0.0417 | −0.475 | −0.704 |

- **b → 0** (the twisted axis is relatively long): R → 1. The twist stops mattering.
- **b → ∞** (the twisted axis is relatively short, a slab): R heads toward −7/8.
  That is the slab ratio −(1 − 2⁻³), the 1-D twisted-to-plain ratio at the slab's
  exponent. This is an expectation, not computed at large b here.

R sweeps from +1 to about −7/8, and the cube sits partway along the way. Neither
end is built from 1/24. **Story (b), as stated, fails.** The twisted axis's 1-D
energy does not set the cube's value. What's left is (a), or something not yet
named.

**Where the question goes now.** R(b) is a smooth sweep from +1 to −7/8 that passes
almost exactly 1/24 at the one shape with full symmetry. The sharp version of the
mystery: *why does the cube, the symmetric point, land within 5.5×10⁻⁴ of 1/24 on a
curve whose range is about 2?* That is a 1-in-~3,600 coincidence if nothing pins
it. It's suggestive, not compelling. **Grade: OPEN.**

## Files

- `attraction-dimension.py` / `.out`: the dial, integer checks, d*, d(R = 1/24).
- `inheritance-test.py` / `.out`: R at extreme box shapes (test of story b).
  Needs mpmath (bundled in `.pylib/`).

## Correction beside (2026-10-19, found while writing the Claude Code packet)

The b → 0 / b → ∞ parentheticals above are **swapped**. Here "b" scales the *dual*
(momentum) lattice, |k|² = k₁² + b²(k₂²+k₃²), so the actual box is (1, 1/b, 1/b).
- b → 0: a slab that is thin along the **twisted** axis. R → 1.
- b → ∞: a thin tube along the twisted axis. Only k₂ = k₃ = 0 survives, so
  R → Σ(−1)^k k⁻⁴ / Σ k⁻⁴ = −7/8.
Values unchanged; checked independently in direct-box form: R(sides 1, ¼, ¼) = −0.7937,
R(sides 1, 4, 4) = +0.8548. The verdict on story (b) is unaffected.
