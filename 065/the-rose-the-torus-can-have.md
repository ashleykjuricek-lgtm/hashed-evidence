# The rose the torus is allowed to have

**2026-08-25.** Ash: *"but what if we use the unit circle. rose curved? or
something?"*

The question lands on a real gap in 064. The π-free form

    R = SUM'_m chi(m) |m|^-4  /  SUM'_m |m|^-4

**still contains a smoothing.** `Σ′` bins by `|m|²` — it sums over **spheres**.
Binning by radius *is* averaging the rose. So: is the isotropic `R` a
direction-average of something with structure underneath?

**Yes. And the structure is four-fold, and it can never be ten-fold, and that is a
theorem rather than a measurement.**

---

## 1. First order: a quadrupole, exactly

Deform the metric along a unit direction `û`: `Q_û(n) = |n|² + ε(n·û)²`, and take
`dR/dε`. The response is a quadratic form with matrix `M_ij = Σ f(n) n_i n_j |n|^(−6)`.

```
DENOMINATOR (f = 1):        diag(5.48459105, 5.48459105, 5.48459105)
                            off-diagonals 0 to 1e-17   -- exactly isotropic

NUMERATOR (f = (-1)^n1):    diag(-2.9262045876, 1.8077123102, 1.8077123102)
                            off-diagonals max 9.044e-17
                            A - B = -4.7339168978
```

The unmarked sum respects ℤ³'s full cubic symmetry, so **its response has no
direction at all.** The character `(−1)^(n₁)` breaks exactly one axis, so the
numerator's is `diag(A, B, B)`.

Sweeping `û = (sin t, 0, cos t)` against the predicted `B + (A−B)û_x²`:

```
   angle    dR/deps          quadrupole form     ratio
     0     -0.1918067406    -0.1918067406       1.00000000
    30     -0.0479516851    -0.0479516851       1.00000000
    45      0.0959033703     0.0959033703       1.00000000
    90      0.3836134811     0.3836134811       1.00000000
```

> **To first order the angular structure is exactly `cos²θ`.** A quadrupole, set by
> the single marked axis. No petals.

Note it changes sign near 40°: the deformation *raises* `R` along the marked axis
and *lowers* it perpendicular, or the reverse depending on the sign of `ε`.

## 2. At finite deformation: four petals

Sweep `û` in the **y–z plane**, perpendicular to the marked axis, where first order
predicts a constant (both give `B`). Anything that appears is higher-order lattice
structure:

```
   eps=0.05   min 0.0324794487   max 0.0327797224   swing 3.003e-04
   eps=0.30   min -0.0097714244  max -0.0015598187  swing 8.212e-03
   eps=1.00   min -0.0975329650  max -0.0483564994  swing 4.918e-02

   deviations from the mean, eps=1.0:
      0 deg +2.48e-2    20 deg +1.40e-3    40 deg -2.33e-2
     60 deg -1.45e-2    80 deg +1.77e-2
```

One full oscillation across 90°. **Four-fold, with extrema on the axes and on the
diagonal.** At `ε = 1` the swing is 4.9% of `R`.

**So the isotropic `R` genuinely is a direction-average**, and there is a real shape
under it. Ash's instinct is correct.

The 45° extremum is the diagonal of the transverse square lattice — the same
diagonal whose reflection powers the parity theorem, though `σ` is the swap
involving the *marked* axis and this sweep is in the plane that excludes it.
**Related in kind, not the same map.** Not investigated further.

## 3. Why it can never be ten-fold

**Crystallographic restriction theorem.** A periodic lattice in two or three
dimensions admits rotational symmetry of order **2, 3, 4 or 6 only.** Five-fold and
ten-fold are impossible.

ℤ³'s point group is octahedral — 48 elements, axes of order 2, 3 and 4.

> **No amount of deformation, at any order, can produce a ten-petal rose on the
> cubic torus.** It is forbidden, permanently, by the periodicity that makes the
> lattice a lattice.

And that is exactly what cut-and-project buys. 022's rose lives on a **Penrose**
lattice, projected from ℤ⁵, and **quasiperiodicity is precisely the purchase of the
symmetry periodicity forbids.** 045 counted its ten lobes at 36.00° spacing and
confirmed they survive a round window.

## 4. What this settles between the two halves of the programme

```
   CUBIC TORUS            periodic     4-fold      R is pi-free (064)
                          all the proofs live here

   PENROSE ROSE           quasiperiodic  10-fold   the shape is in the point set (045)
```

**They sit on opposite sides of one theorem.** The cubic torus and the ten-petal
rose are not two views of one object and cannot be made into one — the
crystallographic restriction separates them by construction.

That is not a disappointment. It is the first hard statement of how the two halves
of this project relate, and it replaces an assumed continuity with a proved
boundary.

**And the torus is not shapeless.** It has a rose. The rose has four petals, its
diagonal is the transverse lattice's mirror, and nobody had looked at it.

## 5. Status

| claim | status |
|---|---|
| the π-free `R` still averages over spheres | **TRUE** — `Σ′` bins by `\|m\|²` |
| the denominator's first-order response is exactly isotropic | **COMPUTED**, off-diag 1e-17 |
| the numerator's is `diag(A,B,B)`, `A−B = −4.7339168978` | **COMPUTED**, off-diag 9e-17 |
| first-order angular structure is exactly `cos²θ` | **VERIFIED**, ratio 1.00000000 at every angle |
| four-fold structure appears at finite `ε`, 4.9% swing at `ε=1` | **COMPUTED** |
| ten-fold is impossible on ℤ³ | **THEOREM** — crystallographic restriction |
| the Penrose rose requires quasiperiodicity | **THEOREM**, same one |
| the two halves are separated by that theorem | **ESTABLISHED** |
| the 45° extremum relates to `σ`'s mirror | **NOT ESTABLISHED** — different swap, not investigated |
| the four-petal rose has been studied before | **UNKNOWN** — not searched |

## Attribution

The question is Ash's, and it found a smoothing left inside 064's "π-free" result —
which this seat had presented as the end of the road. The quadrupole computation,
the four-fold sweep, and the crystallographic-restriction argument are this seat's.
The ten-petal rose is 022's and was counted in 045.
