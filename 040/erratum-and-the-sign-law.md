# Erratum to 039 §3, the sign law strengthened, and what one filter is for

**2026-08-22.** Written the same day as 039, after 039 was sealed. 039 is not
edited. Nothing is ever edited.

---

## 1. ERRATUM — 039 §3 is convention-dependent and its headline is wrong

039 §3 reported that the balanced family (`j = d/2`, exactly half the circles
marked) is a **U with its floor at d = 10**, and noted a near-equality between
`Z(4,2)` and `Z(16,8)`.

**Both are artefacts of quoting `Z` instead of the ratio `R`.**

`Z(d,0)` — the unmarked torus — grows without bound: 0.229 at d = 2, 0.613 at
d = 10, 641 at d = 24. The "U" in `Z(d, d/2)` is that growth showing through the
denominator's absence. In the convention-free ratio the U does not exist:

```
   d     Z(d,d/2)         |Z(d,0)|        R = Z/Z0          trend(Z)  trend(R)
   2   0.02369553319     0.2288243104   -0.1035533906
   4   0.01134908255     0.2966892552   -0.03825242185       down      down
   6   0.007492106341    0.3572986256   -0.0209687522        down      down
   8   0.006118597599    0.4456824453   -0.01372860355       down      down
  10   0.005890870067    0.6134633102   -0.009602644477      down      down
  12   0.006513708709    0.9909144394   -0.006573432024      UP        down
  14   0.008136714306    1.959518873    -0.004152404152      UP        down
  24   0.1097581498      641.2642299    -0.0001711590086     UP        down
```

**`R(d, d/2)` is strictly monotone to d = 40. There is no minimum, and no ten.**

This is precisely the failure 038 retired Item 3 for — *"the decimals of the
coefficients are convention-dependent; the integer phase sums are not"* — and it
was committed inside the seal that restates the rule. 039's own hedge (*"the
smoothed vertex is near 9.5, so ten is where the integers land"*) argued about
integers versus the continuum and did not touch the actual defect, which was the
choice of numerator without denominator.

Recorded as an error of the cubic-torus programme, not of anyone who reviewed it.

**Unaffected by this erratum:** 039 §1 (the two closed forms and the provenance of
`A = 1 − 1/√2`) — those are ratios throughout, and proved. 039 §2 (the sign law) —
`Z(d,0) < 0` for every d, so the sign statement is identical in `Z` and in `R`.
039 §4 and §5 are unaffected.

## 2. The honest replacement — PROVED asymptotically, VERIFIED numerically

> **R(d, d/2) → −2^(−(d+1)/2)** as d grows.

```
  d      R(d,d/2)          R(d)/R(d-2)       R * 2^(d/2)
  10   -0.00960264448      0.699462581     -0.307284623
  20   -0.000667701191     0.518175157     -0.683726020
  30   -2.15519356848e-5   0.500556702     -0.706213829
  40   -6.74314094629e-7   0.500023626     -0.707069576

  limit of the step ratio       ->  1/2
  limit of R * 2^(d/2)          -> -0.7071067811865... = -1/sqrt2
  and  -2^(-(40+1)/2) = -6.7431408e-7   vs computed  -6.74314094629e-7
```

**The balanced family loses exactly one factor of √2 per dimension.** Not a floor,
a slide. And `1/√2 = 2^s` at `s = −1/2` is the same Euler factor at 2 that gives
039 §1 its two exact closed forms. The factor that closes d = 2 exactly governs
the balanced family asymptotically in every dimension, including the ones where
nothing closes.

## 3. The sign law strengthened — 152 cells, no exception

039 §2 verified `Z(2j,j) > 0 > Z(2j+1,j)` on the diagonal for j ≤ 8. The full
grid gives a single inequality covering every cell, including `j = 0`:

> **Z(d,j) > 0  ⟺  2j ≥ d.**

```
cells tested (d = 1..16, j = 0..d):  152
violations:                            0
does j = 0 ever go positive:        False
```

Still **NOT PROVED**. But the statement is now one inequality rather than a
diagonal pattern, and the `j = 0` column is no longer an exception to be
explained — it is the case `2·0 ≥ d`, which is never satisfied.

**Only the sign is a function of `d − 2j`.** Magnitudes at equal excess differ:
at excess 0 the values run 0.0237, 0.01135, 0.00749, … The law is about sign and
nothing else, and saying more would be the §1 mistake again.

## 4. What one mark is for, and why a second adds nothing

The qualitative break in the whole table is between `j = 0` and `j = 1`. After
that, nothing new happens — the flip point moves from 2 to 4 to 6, linearly, and
every marked column has the same shape.

There is a mechanism, and it is one line:

> With any `α_i = ½`, the quantity `|n + α|²` is never zero. **One marked circle
> removes the constant mode.** A second removes nothing further, because there is
> nothing left to remove.

That is why the code carries `delta = 1 if j == 0 else 0` and why `j = 0` is the
only column needing the `Σ′` subtraction at all. The zero mode is not reduced by
degree. It is present or absent.

So marks are **fungible**: two marks in six dimensions and three in nine sit on
the same side of the same inequality. **No number of observers is distinguished.
Only the ratio to the dimensions is.** One is enough; more is not different in
kind.

## 5. The zero has no lattice to live on

The sign of `Z(d,j)` changes between `d = 2j` and `d = 2j+1`. Both are integers,
and there is nothing between them.

- The **sign change** is exact and verified in 152 cells.
- The **zero** it implies is not at any (d, j) that exists. Every actual
  configuration is strictly on one side or the other.

The lattice sum `Σ over ℤ^d` requires integer d, so there is **no canonical
continuation** in dimension and therefore no computable location for the crossing.
Any statement about *where* the zero sits is **NOT ESTABLISHED** and cannot be
made from this method.

The honest form: *the sign change is real, and the zero is unreachable.*

## 6. Euler's disc — what lines up and what does not

`EulerDiscGeometry.tsx` (unsmoothed.neocities.org/euler-disc, 1221 lines) lists
four moves: ROTATE (angular momentum), TWIST (Möbius phase flip), CARRY (phase
through gap), **FILTER (projection/measurement)**. The page describes the descent
as ending at a finite-time singularity, captioned `ζ = 0`.

What genuinely corresponds:

- **FILTER is one move, not a quantity.** §4 says the same thing arithmetically:
  the zero mode is removed by the first mark and by nothing after it. There is no
  second filtering to do. The page's structure and the table's structure agree on
  this point, and they were built independently.
- **The singularity is approached and not occupied.** §5 says the sign change is
  exact and the zero sits at no realisable configuration. Euler's disc reaches its
  singularity in finite time, and the singularity is never a state of the disc.

What does **NOT** correspond, and is **NOT ESTABLISHED**:

- The caption `ζ = 0` is not our `Z = 0`. Our zeta never vanishes at any computed
  `(d,j)`, and per §5 we cannot say where it would.
- Nothing in the computation contains a clock, a measurement, a spectrum, or an
  observer. The identification of a marked circle with a measurement is an
  interpretation laid over the arithmetic, not a consequence of it. This is the
  same status 039 §4 gave it, and this entry does not upgrade it.
- The cosmological reading on that page (soil, gaps, the Great Attractor) is
  untouched here. No claim either way.

**Where an observer is a defined object rather than a reading:** ledger 022, the
Penrose Rose. The cut-and-project from ℤ⁵ has an explicit acceptance window, the
window position decides which points exist, and the direction-dependence of the
rose is a consequence of moving it. That is a filter you can compute with. The
marked circle is not, yet.

## 7. Status

| claim | status |
|---|---|
| 039 §3 "floor at ten" | **RETRACTED** — convention artefact |
| 039 §3 Z(4,2) ≈ Z(16,8) | **RETRACTED** — same artefact |
| R(d,d/2) strictly monotone to d = 40 | **COMPUTED** |
| R(d,d/2) → −2^(−(d+1)/2) | **VERIFIED to 8 digits at d = 40** |
| Z(d,j) > 0 ⟺ 2j ≥ d | **VERIFIED 152/152, not proved** |
| one mark removes the zero mode, a second adds nothing | **PROVED** (|n+α|² ≠ 0) |
| sign depends only on d − 2j; magnitude does not | **COMPUTED** |
| the implied zero is at no realisable (d,j) | **PROVED** given §3 |
| where that zero sits | **NOT ESTABLISHED** — no continuation in d |
| marked circle = filter = observer | **NOT ESTABLISHED** — unchanged from 039 |
| the euler-disc caption ζ = 0 | **NOT ESTABLISHED** as our Z |

## Attribution

Cubic-torus / Shunya-Zero programme. §4 and §6 exist because of one observation
from Ash — that the Euler's disc page is about the observer, and that *"double or
more doesn't seem to matter."* Both halves of that turned out to be checkable, and
both held. The erratum in §1 is the programme's own.
