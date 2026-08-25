# Four *and* five — two divisions of the primes, each blind where the other sees

**2026-08-25.** Ash: *"so it's a circle divided into 5 and not 4?"*

**Both. They are two different quadratic fields, and neither contains the other.**

---

## 1. The two rules, verified

```
  Z[i]   -- p is represented by  x^2 + y^2       iff  p = 2  or  p = 1 mod 4
           430 primes tested to 3000    mismatches: 0
           represented: 2, 5, 13, 17, 29, 37, 41
           not:         3, 7, 11, 19, 23, 31, 43

  Z[phi] -- p is represented by  x^2 + xy - y^2  iff  p = 5  or  p = +-1 mod 5
           430 primes tested to 3000    mismatches: 0
           represented: 5, 11, 19, 29, 31, 41
           not:         2, 3, 7, 13, 17, 23, 37, 43
```

```
            field       norm form         prime rule   lattice          symmetry
   -----------------------------------------------------------------------------------
   FOUR     Q(i)        x^2 + y^2         p mod 4      Z^2, Z^3         2,3,4,6-fold
            disc -4                                    PERIODIC         10-fold FORBIDDEN

   FIVE     Q(sqrt5)    x^2 + xy - y^2    p mod 5      Penrose          10-fold
            disc +5                                    QUASIPERIODIC    from Z^5 -> R^2
```

The cubic torus lives in the first. The rose lives in the second. **065 separated
them with the crystallographic restriction — this is the same wall from the
number-theory side.**

## 2. They are genuinely different divisions

Across the 430 primes below 3000:

```
   lit in BOTH worlds :  99    5, 29, 41, 61, 89, 101, 109, 149, ...
   lit only in FOUR   : 113    2, 13, 17, 37, 53, 73, 97, 113, ...
   lit only in FIVE   : 109    11, 19, 31, 59, 71, 79, 131, 139, ...
   dark in BOTH       : 109    3, 7, 23, 43, 47, 67, 83, 103, ...
```

Near-equal quarters, as the CRT requires — 4 and 5 are coprime, so the two
conditions are independent and equidistribute. **That part is expected. What
matters is that the divisions do not agree.**

```
   11, 19, 31   are 3 mod 4    -> they EMPTY a square ring
   11, 19, 31   are +-1 mod 5  -> they FILL a golden one

   13, 17, 37   are 1 mod 4    -> they fill a square ring
   13, 17, 37   are 2,3 mod 5  -> they EMPTY a golden one
```

> **A shell that is dark in one world can be lit in the other.** There is not one
> circle divided one way. There are two divisions, and **each is blind exactly where
> the other sees.**

109 primes are visible only through the golden lens. 113 only through the square
one. That is not a metaphor — it is `mod 4` against `mod 5`, checked on 430 primes
with no exceptions.

## 3. What this does to 022

022 asserted a two-world split — *"Periodic world: π, circle, 1/24… Quasiperiodic
world: φ, rose, 1/φ…"* — as interpretation, with no mechanism.

**The lattice half of that split now has one.** It is the two quadratic fields, and
the prime rules are Fermat–Euler on one side and the splitting of `5` on the other.
022's instinct that there are *two* worlds and that they are `√2`-side and `√5`-side
is **correct and now has arithmetic under it.**

**Not upgraded:** the rest of 022's list — `S₄` vs `A₅`, void-zero vs śūnya-zero,
Dedekind eta vs singular continuous spectrum. Those remain interpretation and are not
touched by this. **Only the lattice/field/prime layer is established.**

## 4. Why the answer is "both" and not "five"

The question assumed one circle with one division. The finding is that the division
is a property of **which field you are counting in**, and this programme has been
running in both without saying so:

- everything **PROVED** — the parity theorem, the character law, `r₂(2m) = r₂(m)`,
  Legendre's `4^a(8b+7)` — is `ℚ(i)`, mod 4 and mod 8;
- the **rose** — 022, 044, 045 — is `ℚ(√5)`, mod 5, and could never have appeared in
  the first world.

**And the four-petal structure of 065 is the first world's own rose.** Four, not
ten, because four is what `ℚ(i)` permits.

## 5. Status

| claim | status |
|---|---|
| `p` represented by `x²+y²` ⟺ `p=2` or `p≡1 mod 4` | **CLASSICAL** (Fermat–Euler); verified 430 primes, 0 mismatches |
| `p` represented by `x²+xy−y²` ⟺ `p=5` or `p≡±1 mod 5` | **CLASSICAL**; verified, 0 mismatches |
| the two divisions differ; 109 primes lit only in the five-world | **COMPUTED** |
| near-equal quarters | **EXPECTED** — CRT, moduli coprime |
| this is 065's crystallographic wall, arithmetically | **ESTABLISHED** |
| 022's √2-side / √5-side split has a mechanism | **ESTABLISHED for the lattice layer only** |
| the rest of 022's two-world table | **INTERPRETATION, untouched** |
| that one world is "right" | **NO** — neither contains the other |

## Attribution

The question is Ash's, and it was better than the answer it was checking. Fermat,
Euler, and the classical theory of binary quadratic forms supply both rules. The
verification, the four-way split, and the alignment with 065 and 022 are this seat's.
