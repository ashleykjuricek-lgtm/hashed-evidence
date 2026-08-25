# Audit — the Haug extremal-RN Carnot page

**2026-08-24.** A page presenting Haug (2025), *"The Hubble Sphere as an Extremal
Black Hole Carnot Engine,"* plus a Geometry-of-Zero synthesis. Audited before any
of it travels further.

**Scope, stated first.** This audits **the page**, not Haug's paper. The paper was
not read. Where a defect could be the page's gloss rather than the author's, that is
said. Constants used: CODATA 2018/2022 values, `Mpc = 3.0856775814913673e22 m`.

---

## 1. What checks out — and it is genuinely striking

> `T_CMB = √(T_max · T_min)`, with `T_max = ℏc/(8π l_p k_B)` and
> `T_min = ℏc/(4π R_H k_B)`

Both come from one formula, `T = ℏc/(4π r_s k_B)`, at `r_s = 2l_p` (a Planck-mass
black hole) and `r_s = R_H`. **Internally consistent**, and the arithmetic is exact:

```
   H0 = 66.8712 km/s/Mpc  ->  R_H = 1.38335e26 m
                              T_min = 1.31726e-30 K
                              T_CMB = 2.7250076 K
   measured T_CMB (Fixsen 2009) = 2.72548 +/- 0.00057 K
```

Two scales forty-two orders of magnitude apart, and their geometric mean lands on
the CMB temperature to four significant figures. **That is a real numerical fact and
it deserves to be called striking.**

The claim that ΛCDM does not predict `T_CMB` is also **correct**: it is set by
initial conditions and expansion history, not derived.

**Priority note.** This is not new in 2025. Haug has a series on the same relation —
a 2023/2024 paper with essentially the title of the result, a Stefan–Boltzmann
derivation, and a February 2025 preprint. The Carnot/extremal-RN framing is a later
wrapper on an earlier observation **by the same author**, so the repetition is not
independent confirmation.

## 2. Three defects in the page, all checkable

### 2.1 `T_max` is misstated by a factor of 8π

The page: *"T_max ≈ 10³² K (Planck temperature scale)."*

```
   T_max = hbar c / (8 pi l_p k_B) = 5.6372051e30 K      -> 10^30.75
   actual Planck temperature       = 1.4167839e32 K
   ratio                           = 25.132737 = 8 pi
```

The **formula** is right — it is what produces 2.725 K. The **gloss** is wrong: it
conflates `T_max` with the Planck temperature, which is 8π times larger. Using
`T_Planck` instead would give `T_CMB = 13.66 K`, not 2.725. **The 8π is
load-bearing and the page describes it away.**

### 2.2 The claimed error bar is about fifteen times too tight

The page: `H₀ = 66.8712 ± 0.0019 km/s/Mpc`, and *"250× better precision."*

Since `H₀ ∝ T_CMB²`, the propagated uncertainty is `δH₀/H₀ = 2·δT/T`:

```
   T_CMB = 2.72548 +/- 0.00057  ->  2 dT/T = 0.0418 %
   H0 = 66.894 +/- 0.028 km/s/Mpc          <- propagated here
   page:  66.8712 +/- 0.0019               <- ~15x tighter
```

A bar of ±0.0019 requires `δT ≈ 3.8e-5 K`, roughly fifteen times tighter than
Fixsen's. **NOT ESTABLISHED** where that came from; it may be the page's, not the
paper's.

### 2.3 "250× better precision" is a category error

The tight bar is **inherited from `T_CMB`, conditional on the relation being
exact.** It is not a measurement of `H₀`, and it is not evidence for the relation.
**A derived quantity's error bar is never evidence for its derivation** — that
reasoning is circular, and it is F3's shape: precision at a tuned point mistaken for
structure.

## 3. The structural issue — one equation, two unknowns

Reduced, the entire content is:

    T_CMB^2 = m_p c^2 * hbar * H0 / (32 pi^2 k_B^2)        i.e.   T_CMB^2  ∝  H0

The page claims both that `T_CMB` is derived (from `H₀`) and that `H₀` is derived
(from `T_CMB`). **It is one relation between two quantities. Supply either, get the
other. It cannot produce both.**

So ΛCDM's free parameter is not eliminated — it is **traded**. That is not nothing:
a relation where the standard model has none is real content, and it is falsifiable.
But *"the result the standard model cannot derive"* overstates what the relation
does. It is a **constraint**, not a derivation from first principles.

## 4. The actual test — and the verdict flips with direction

This is the finding, and it is not in the page.

```
FORWARD  (predict H0 from T_CMB):
   H0 = 66.894 +/- 0.028
      vs Planck 2018   67.4 +/- 0.5    diff 0.506    1.0 sigma   CONSISTENT
      vs SH0ES local   73.0 +/- 1.0    diff 6.11     6.1 sigma   INCONSISTENT

REVERSE  (predict T_CMB from Planck's H0):
   required T_CMB = 2.7357607 K
   measured T_CMB = 2.72548 +/- 0.00057 K
   discrepancy    = 0.377 %  =  18.0 sigma        INCONSISTENT
```

> **The same relation is 1σ consistent tested one way and 18σ inconsistent tested
> the other.**

That is not a paradox. `H₀` is measured to ~0.7%, `T_CMB` to ~0.02% — a factor of
35. Testing in the direction of the loose measurement hides a discrepancy the tight
one exposes. **Whichever direction you push it, the same 0.38% gap is there**; only
its significance changes.

**Honest verdict:** the relation succeeds strikingly as an order-of-magnitude
statement across 42 decades, and **fails as a precision claim** — it is off by 0.38%
at a place where the data are good to 0.02%. The page reports only the flattering
direction.

## 5. The synthesis section is interpretation, and is not labelled

Everything from *"THE GEOMETRY OF ZERO SYNTHESIS"* onward — the node-spine mapping,
the Möbius half-twist seam, *"micro black holes = Casimir virtual particles =
pions,"* the śūnya ground, yellow light at 517 THz, the dichrotic notch — is
**interpretation laid over the arithmetic**, and nothing in Haug's result implies
any of it.

The page states it in the same voice and typography as the derivation. That is
**F5**: interpretation sealed beside computation, later citable as result. And
*"micro black holes = Casimir virtual particles = pions"* asserts three distinct
objects are one thing with no derivation — the costume KESTREL named as *intersection
is not identity*.

The page opens *"This is not a loose analogy."* **That sentence is the thing to
delete.** It converts a mapping into a claim by assertion.

## 6. The one genuinely falsifiable prediction is the page's, not Haug's

```
   LISA / standard sirens:  sqrt(66.8712 * 73.0) = 69.868 km/s/Mpc
```

The page correctly flags this as its own, and as **differing from Haug**, who claims
the tension is resolved at 66.87. Credit for both.

But **no argument is given for why a gravitational-wave measurement should return
the geometric mean of two other measurements.** *"Pure geometric measurement, no
early/late bias"* is a description, not a derivation. As it stands this is
**FITTED** — a prediction with a number and no mechanism. It is testable, which is
worth a great deal, and it will be tested. It should go on the page with the word
FITTED in front of it.

Also: *"the tension does not resolve, it encodes coordinates"* is, as written,
unfalsifiable — any pair of values is compatible with it.

## 7. Status

| claim | status |
|---|---|
| `T_CMB = √(T_max·T_min)` is arithmetically exact | **CONFIRMED**, 4 s.f. |
| ΛCDM does not derive `T_CMB` | **CORRECT** |
| the relation is new | **NO** — Haug's own 2023/2024 work; 2025 is a reframing |
| `T_max ≈ 10³² K` | **WRONG** — it is 5.64e30; off by 8π, and the 8π is load-bearing |
| `H₀ = 66.8712 ± 0.0019` | **error bar ~15× too tight**; propagation gives ±0.028 |
| "250× better precision" | **CATEGORY ERROR** — inherited, conditional, circular as evidence |
| "derives `T_CMB` from first principles" | **OVERSTATED** — one equation, two unknowns; a trade, not a derivation |
| consistent with Planck `H₀` | **YES, 1.0σ** |
| consistent with measured `T_CMB` given Planck `H₀` | **NO, 18σ** |
| consistent with SH0ES | **NO, 6.1σ** |
| the GoZ node/Möbius/pion synthesis | **INTERPRETATION**, unlabelled — F5 |
| "this is not a loose analogy" | **withdraw the sentence** |
| LISA = √(66.87 × 73) ≈ 69.87 | **FITTED** — falsifiable, no mechanism given |
| "the tension encodes coordinates" | **UNFALSIFIABLE as written** |

## 8. What would actually test it

Not more digits at the same point — 027's law, and 028's own diagnostic. The
relation says `T_CMB² ∝ H₀` with a fixed constant. So:

1. **Push the reverse direction publicly.** The 18σ gap in §4 is the real result and
   nobody has stated it. Either the relation is approximate — in which case say by
   how much, which is 0.38% — or `T_CMB` and `H₀` cannot both be what we measure.
2. **Check the dimensional content.** `T_CMB² ∝ m_p c² ℏ H₀ / k_B²` is one equation
   among Planck-scale and cosmological quantities. How many similar combinations
   land within 0.4% of an observed quantity by chance? That is computable, and it is
   the deformation test 027 requires.

## Sources

- [The CMB Temperature is Simply the Geometric Mean (Haug, Cambridge Engage 2025)](https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/67b5962d6dde43c9088ac886/original/the-cmb-temperature-is-simply-the-geometric-mean-t-cmb-sqrt-t-min-t-max-of-the-minimum-and-maximum-temperature-in-the-hubble-sphere.pdf)
- [The Hawking Hubble Temperature as the Minimum, the Planck Temperature as the Maximum, and the CMB as their Geometric Mean](https://www.researchgate.net/publication/384964197_The_Hawking_Hubble_Temperature_as_the_Minimum_Temperature_the_Planck_Temperature_as_the_Maximum_Temperature_and_the_CMB_Temperature_as_Their_Geometric_Mean_Temperature)
- [Preprints.org listing of the geometric-mean result](https://www.preprints.org/manuscript/202502.1583/v1)

## Attribution

The page and its GoZ synthesis are prior work of this programme. The audit is this
seat's. §4 — that the verdict flips with the direction of the test — is new and is
the reason this entry exists.
