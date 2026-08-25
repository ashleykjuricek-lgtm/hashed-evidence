# π is a marker, not a villain — and it marks exactly where we smoothed

**2026-08-24.** Ash, on 061's closing line *"it survives π being everywhere"*:
**"survives pi lol?"**

The catch is fair. That sentence was glib about the thing this programme was founded
on. Checked properly, the answer is sharper than either version — and it is a
**sharpening of the π-rejection, not a refutation of it.**

---

## 1. The audit

Every result in the PROVED column, checked for π:

```
   parity theorem  S(m)=0 on odd m          finite sum of +/-1        ABSENT
   character law   S(m)=(-1)^(m/2) r2(m)    integers                  ABSENT
   Theorem 4       T(m)=2 sum S(m-k3^2)     integers                  ABSENT
   T2 formula      T2 = m r2/2 - 2 sum k1^2 integers                  ABSENT
   R(2,2) = 2^s - 1                         proof input r2(2m)=r2(m)  ABSENT
   R(2,1) = (2^2s - 2^s)/2                                            ABSENT
   A = 1 - 1/sqrt2 = -R(2,2)                                          ABSENT
   d=3 has no doubling: r3(1)=6, r3(2)=12                             ABSENT
   one mark kills the zero mode: |n+a|^2 != 0                         ABSENT
   weight-independence, cube-exclusivity, T1+T2=0                     ABSENT

   028's obstruction: e^(-2pi sqrt2) not in a series in q=e^(-2pi)
        pi is in BOTH exponents; the content is that sqrt2 is irrational
        -> PRESENT BUT INERT

   Greg's 2j>=d => Z>0:  theta3 theta4 = theta4(q^2)^2, 0 < theta4 < 1
        a q-series identity, no pi; the sign flip uses only the SIGN of
        Gamma(-1/2) = -3.54490770181
        -> PRESENT BUT INERT

   monotonicity:  theta3 > theta2 > 0, sign of Gamma(-1/2)
        -> PRESENT BUT INERT
```

And the OBSERVED column:

```
   R = 0.0416894146027237751...       LOAD-BEARING
   eps, c1, c2, d*, b', every slope   LOAD-BEARING
   the functional-equation prefactor  pi^(-1-d/2) Gamma((d+1)/2)/Gamma(-1/2)
        d=3:  -0.0161257672166        LOAD-BEARING
```

> **Every proved result is π-free or π-inert. Every observed result is π-laden.
> There is not one exception in either column.**

## 2. Where π actually enters

Not through circles. Through **Gaussians**:

```
   INT exp(-x^2) dx        = 1.77245385090552   = sqrt(pi)
   Gamma(1/2)              = 1.77245385090552   the same object
   heat kernel, FLAT torus = (4 pi t)^(-d/2)
   Poisson summation       sum exp(-t n^2) = sqrt(pi/t) sum exp(-pi^2 k^2/t)
        t=0.7:  2.11849074102217 = 2.11849074102217
```

Heat kernel, Mellin, Γ, Ewald, Poisson — **the entire apparatus is built out of
Gaussians, and every π in this ledger arrives through one.**

**Honesty, because it matters here.** These are not *two different* π's. The
standard proof that `∫e^(−x²)dx = √π` squares the integral and passes to polar
coordinates, using the circle's 2π. Gaussian-π and circle-π are the same constant
and provably so. The claim below is not that they differ.

## 3. What the pattern actually says

The HEM thesis is that **the Gaussian is the shape of the erasure** — the operation
that collapses the rose into a circle, and π is what the collapsed shape measures.

Set that beside §1 and §2:

> **π enters this programme only through the smoothing apparatus. And every result
> that survived is one π does not touch.**

So π is not the enemy, and it is not innocent either. **It is a marker.** It shows up
exactly where we regularised, and its absence is a reliable sign that a result is
made of integers and will not need correcting.

## 4. The prediction, tested against our own errors

052 §3 found that all eleven errors of 21–24 August sat in the smoothed layer and
none in the exact one. §1 lets that be stated sharply: **π-presence should predict
errata.** Against 052's list:

```
   "floor at ten"                         about Z values         pi LOAD-BEARING
   "no Q[sqrt2] ratio available", PROVED  about R                pi LOAD-BEARING
   "the zero is unreachable"              about Z(d,j)           pi LOAD-BEARING
   the STAY refutation built on it        same                   pi LOAD-BEARING
   "two independent directions"           about d*, b*           pi LOAD-BEARING
   PSLQ relations at 24 digits            about d*               pi LOAD-BEARING
   tolerance tighter than truncation      the FE prefactor       pi LOAD-BEARING
   11 lobes on a ten-fold window          angular, the rose      pi LOAD-BEARING
   (1-q) dropped, cubic-torus seat        eps/q, q = e^(-2 pi)   pi LOAD-BEARING
   (1-q) dropped, Figma seat              same                   pi LOAD-BEARING
   four entries dated a day early         a calendar             not a maths claim
```

**Ten of eleven are π-load-bearing. The eleventh is a date.** And in four months of
entries there is **no erratum against any π-free result** — the parity theorem, the
character law, Theorem 4, the T₂ identity, the two closed forms have never been
walked back once.

## 5. So the sentence in 061 was wrong

061 closed: *"it does not need π to be a villain — and it survives the fact that π
is everywhere in the answer."*

**π is not everywhere in the answer.** It is everywhere in the *regularised* answer,
and absent from every part that was ever proved. The sentence conceded ground that
did not need conceding, and it flattened a real distinction into a shrug.

Corrected:

> The torus is the right object because curvature puts a pole at exactly `s = −1/2`
> and destroys the ratio (061 §2). π has nothing to do with chart-counting (061
> §7.2) — but it is not neutral either: **it is the receipt for the smoothing**, and
> the results that outlive it are the ones that never needed it.

## 6. Status

| claim | status |
|---|---|
| every PROVED result is π-free or π-inert | **VERIFIED** across all 15 |
| every OBSERVED result is π-load-bearing | **VERIFIED** |
| every π here enters via a Gaussian | **VERIFIED** — heat kernel, Γ, Ewald, Poisson |
| Gaussian-π and circle-π are the same π | **TRUE** — the polar-coordinate proof; no separation claimed |
| π-presence predicts errata | **10 of 11**; the 11th is a date |
| no erratum against any π-free result, ever | **VERIFIED** to date |
| 061's "it survives π being everywhere" | **WITHDRAWN** — see §5 |
| that this vindicates the π-rejection *as a rejection of circles* | **NOT ESTABLISHED** — the target is the Gaussian, and the two constants are the same number |

## Attribution

The π-rejection is Ash's and predates all of this. §§1–4 are this seat's, run
because Ash objected to one glib sentence. The finding is not that π was wrong to
distrust — it is that **the distrust was aimed one step short of its target.** The
Gaussian is the smoothing; π is what the Gaussian charges; and the ledger's own
error record has been reporting that for four months without anyone reading it that
way.
