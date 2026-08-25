# What we use instead of π

**2026-08-25.** Ash: *"what do we use instead of pi?"*

064 showed π cancels out of `R` — it is in the method, not the object. That leaves
the question this project was founded on, and now it has a concrete answer.

> **We use `r₂(m)` and `r₃(m)`: the number of lattice points at distance `√m`.
> π is their average. That is all π is.**

---

## 1. The identity

`r₂(m)` is the number of `(x,y) ∈ ℤ²` with `x² + y² = m`. The counts:

```
   m:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
  r2:  4  4  0  4  8  0  0  4  4  8  0  0  8  0  0  4  8  4  0  8  0  0  0  0
```

Integers. Wildly irregular. **Often zero.**

Now average them:

```
   mean of r2(m) over m <=     100 : 3.16000000
   mean of r2(m) over m <=  10,000 : 3.14160000
   mean of r2(m) over m <= 500,000 : 3.14160800
   mean of r2(m) over m <= 2,000,000: 3.14161200

                                pi = 3.14159265
```

**That is not an approximation to π. It is π.** The number of lattice points inside
a circle of area `X` is `πX + O(X^(1/3))` — the Gauss circle problem — so the mean of
`r₂` converges to π exactly, with error `O(X^(−2/3))`. At `X = 2×10⁶` the observed
residual is `1.9e-5` against a predicted `6.3e-5`. Consistent.

Same in three dimensions: `r₃(m)` averages `2π√m`, because the ball of radius `√X`
holds `(4/3)πX^(3/2)` points.

```
   sum r3(m), m <=   1,000 :    132,450   vs (4/3) pi X^(3/2) =    132,461   ratio 0.999916
   sum r3(m), m <=  50,000 : 46,832,034   vs                  = 46,832,098   ratio 0.999999
   sum r3(m), m <= 200,000 : 374,656,122  vs                  = 374,656,786  ratio 0.999998
```

> **π is the mean of the number of ways to write `m` as a sum of two squares.**
> Nothing else. It is a summary statistic of an arithmetic function.

## 2. What the average cannot see

```
   r2(m) = 0 for m = 3, 6, 7, 11, 12, 14, 15, 19, 21, 22, 23, 24, 27, 28, ...
   79.0% of all shells below 2,000,000 are EMPTY.

   r3(m) = 0 for m = 7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71, 79, ...
   Legendre's three-square theorem: exactly when m = 4^a (8b + 7).
```

**Four shells in five are empty, and π never is.**

Every empty shell is a place where the count is `0` and the average says `3.14159…`.
That is the erasure, with a number on it: **not a metaphor about smoothing, a
measured 79%.**

And the empty shells are not noise. Legendre's theorem says exactly which they are:
`4^a(8b+7)`. **The structure the average destroys is a theorem.**

## 3. Why every proof in this ledger is π-free

Look at what the PROVED column is actually made of:

```
   the parity theorem     a character sum over the ACTUAL points on a shell
   the character law      r2(m), with a sign
   Theorem 4             a sum of S over ACTUAL sub-shells
   the T2 identity        r2(m) and a second moment over ACTUAL points
   R(2,2) = 2^s - 1       from r2(2m) = r2(m)
   d=3 fails             from r3(1) = 6, r3(2) = 12
```

**Every one is a statement about counts. Not one is about an average.** That is why
they are exact, why they are π-free, and — per 062 — why not one of them has ever
needed correcting.

The OBSERVED column is what you get when the counts are pushed through Gaussian
machinery that replaces them with their smooth envelope. π appears there, and so do
all eleven errata.

## 4. The answer, stated plainly

**Instead of π, use the counts.**

- In two dimensions: `r₂(m) = 4(d₁(m) − d₃(m))` — four times the excess of divisors
  `≡ 1 mod 4` over those `≡ 3 mod 4`. Integers, from divisors. Jacobi, classical.
- In three: `r₃(m)`, zero exactly on `4^a(8b+7)`, Legendre, classical.
- The object we care about: `R = Σ′ χ(m)|m|^(−4) / Σ′ |m|^(−4)`, both sums over
  counts, no π (064).

This is not a new number system and it is not an alternative to π. **It is the thing
π is the average of.** Choosing counts over π is choosing the shape over its mean —
which is the project's founding move, now stated as an identity rather than a
preference.

## 5. What this does NOT claim

- **π is not wrong, and not avoidable in practice.** It is the correct average, it
  makes the computation converge geometrically instead of like `M^(−1/2)`, and the
  Gaussian road is why any of these numbers are known to 50 digits (064 §5).
- **Circle-π and Gaussian-π remain the same constant** (062). Nothing here separates
  them; this identifies a *third* place the same number appears — as the density of a
  lattice — and it is the same π again.
- **"Use counts instead of π" is not a method.** It is a statement about where the
  information is. The counts are what the proofs are about; the average is what the
  computations run on. Both are needed.
- **None of this makes `R` identifiable.** 044's bounded nulls stand.

## 6. Erratum, same document

The script's closing text says *"r2 vanishes on 76% of shells"* while its own
computation prints **79.0%**. The computed figure is correct; the 76% was written by
hand and not checked against the run three lines above it.

Trivial, and recorded because it is the same failure as everything else in this
ledger: **a summary sentence drifting from the number it summarises.**

## 7. Status

| claim | status |
|---|---|
| mean of `r₂(m)` → π exactly | **CLASSICAL** (Gauss circle problem); verified to `1.9e-5` at `X = 2e6` |
| `r₃(m)` averages `2π√m` | **CLASSICAL**; verified, ratio `0.999998` at `X = 2e5` |
| 79.0% of shells below 2e6 have `r₂ = 0` | **COMPUTED** |
| `r₃(m) = 0` ⟺ `m = 4^a(8b+7)` | **CLASSICAL** — Legendre |
| every PROVED result is a statement about counts, not averages | **VERIFIED** across all 15 |
| π is "the average of the counts" and nothing more | **TRUE in this precise sense**; it is also the circle constant and the Gaussian constant, and they are one number |
| this gives a practical alternative to π | **NO** — see §5 |

## Attribution

The question is Ash's and predates the programme. The identity in §1 is classical —
Gauss, Jacobi, Legendre. What is new here is only the alignment: that this ledger's
proved column is made entirely of counts, its observed column entirely of averages,
and its entire error record sits in the second. 062 found the correlation; 064 found
π was in the road; this names what is on the road instead.
