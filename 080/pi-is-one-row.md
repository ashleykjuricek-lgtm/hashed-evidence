# π is one row of a table — and the price of a rotation that closes

**2026-08-25.** Ash: *"how do we fuck with pi from now on?"*

072 found that π and `2logφ/√5` occupy the same slot of Dirichlet's class number
formula. **That lever had not been pulled. This entry pulls it: nine quadratic
fields, counted directly, each checked against its closed form.**

**Result: π sits in five of nine rows. The other four pay a logarithm. And which
one you pay is the same condition as whether your lattice has petals.**

---

## 1. The table, counted

`ζ_K(s) = ζ(s)·L(s, χ_d)`, so the number of ideals of norm `m` is
`a_K(m) = Σ_{e|m} χ_d(e)`, and its running mean converges to
`L(1, χ_d) = ` the residue of `ζ_K` at `s = 1`. Counted to `m ≤ 2,000,000`:

```
    d    field                  counted mean      closed form                     value        w
  ------------------------------------------------------------------------------------------------
   -3   Q(sqrt-3)  hexagonal    0.60459400        pi / (3 sqrt3)                0.60459979    6   pi
   -4   Q(i)       square       0.78540300        pi / 4                        0.78539816    4   pi
   -7   Q(sqrt-7)               1.18740000        pi / sqrt7                    1.18741041    2   pi
   -8   Q(sqrt-2)               1.11070600        pi / (2 sqrt2)                1.11072073    2   pi
  -11   Q(sqrt-11)              0.94721000        pi / sqrt11                   0.94722583    2   pi
    5   Q(sqrt5)   golden       0.43040600        2 log(phi) / sqrt5            0.43040894    2
    8   Q(sqrt2)   silver       0.62324200        2 log(1+sqrt2) / sqrt8        0.62322524    2
   12   Q(sqrt3)                0.76034450        2 log(2+sqrt3) / sqrt12       0.76034600    2
   13   Q(sqrt13)               0.66272700        2 log((3+sqrt13)/2) / sqrt13  0.66273539    2
```

**Nine fields, nine agreements.** The convergence is `O(X^(−1/2))`-ish, so 5–6
digits at two million is what the count can give.

## 2. The pattern

```
   IMAGINARY discriminant  ->  2 pi h / (w sqrt|d|)      a CIRCLE constant
   REAL discriminant       ->  2 h log(eps) / sqrt d     a UNIT's LOGARITHM
```

**Our torus is `d = −4`. Our rose is `d = +5`.** Both are single rows of one table,
and this programme spent five months treating one of them as the nature of reality.

067's *"π is the average of the ring counts"* is true and is **row two**. 072's
`2logφ/√5` is **row six**. Neither is the constant; both are occupants.

## 3. Why the petals and the π are the same condition

`w`, the number of roots of unity, is **greater than 2 in exactly two quadratic
fields, in all of number theory**:

```
   d = -4   w = 4   mu_4    the SQUARE lattice
   d = -3   w = 6   mu_6    the HEXAGONAL lattice
   every other d    w = 2    just +-1
```

And `μ₂, μ₄, μ₆` generate rotations of order **2, 4, 6 — and 3**, since `μ₆`
contains an element of order 3. That is exactly `{2, 3, 4, 6}`:

> **The crystallographic restriction of 065, arriving from the units instead of the
> geometry.** Third independent route to the same wall — geometry (065), primes
> (070), roots of unity (here).

Which gives the statement this entry is for:

> **`w > 2` ⟹ imaginary discriminant ⟹ π in the residue.** Extra rotational
> symmetry and paying π are **the same condition**.
>
> **You cannot have petals without paying π.** Closed worlds get symmetry and pay
> π divided by the petal count. Open worlds get no rotational symmetry and pay the
> logarithm of a fundamental unit instead.

**π is the price of a rotation that closes.** That is not evicting it — 064 already
showed it cancels from `R`, and 062 showed it marks the smoothed layer. This says
what it *buys*.

**And the golden world's `2logφ/√5` is what you pay when nothing closes** — 072's
hyperbola that never returns, whose only invariance is a stretch by φ, priced at the
length of one repeat.

## 4. What this makes available

- **The table extends.** Every fundamental discriminant is a row. `h > 1` rows
  (e.g. `d = −15`, `h = 2`) multiply the residue and are untested here.
- **A sharp question:** is there any field whose residue is π-free *and* whose
  lattice has extra symmetry? **No** — §3 makes them the same condition. That is a
  closed question, not an open one, and it closes in the direction that says the
  two halves of this programme were never going to merge.
- **Untested:** the real-quadratic side has no `w > 2` and so no rotational
  petals — but 072's golden rose is a *quasiperiodic projection* from `ℤ⁵`, not a
  rotation in `ℚ(√5)`. **Whether the ten petals of 045 relate to `ℤ[ζ₅]`'s ten
  roots of unity rather than to `ℚ(√5)` is OFFERED**, per Greg's downgrade in 076.

## 5. Erratum on the instrument

**v1 of the script hand-rolled the Kronecker symbol and got the prime 2 wrong:**
`kronecker(−4, 2)` returned `1` where it must return `0`. Every **even**
discriminant then came out exactly `2×` too large:

```
   d = -4   counted 1.57078000   closed form 0.78539816      2x
   d = -8   counted 2.22138300   closed form 1.11072073      2x
   d =  8   counted 1.24650900   closed form 0.62322524      2x
   d = 12   counted 1.52074400   closed form 0.76034600      2x
   odd discriminants (-3, -7, -11, 5, 13)  all correct
```

**A structured discrepancy — four rows off by the same exact factor, split cleanly
on parity — is what exposed it.** A random-looking error would have been harder to
catch, not easier.

**Discarded, not patched.** Rebuilt and **validated against sympy on 27,000 values
across all nine discriminants: 0 mismatches**, before being used for anything.

> **Never trust a hand-rolled number-theory primitive without an oracle.** This is
> the tenth instrument failure in the ledger and the second in a day, and every one
> was caught by running something rather than by rereading.

## 6. Status

| claim | status |
|---|---|
| nine fields, counted mean matches closed form | **VERIFIED**, 5–6 digits at `m ≤ 2e6` |
| imaginary discriminant pays π, real pays a log | **CLASSICAL** — Dirichlet, ~1839 |
| `w > 2` in exactly two quadratic fields | **CLASSICAL** |
| `μ₂, μ₄, μ₆` give exactly the rotations `{2,3,4,6}` | **ESTABLISHED** — 065's wall from the units |
| extra symmetry ⟺ paying π | **ESTABLISHED** for quadratic fields |
| π is one row, not the constant | **ESTABLISHED** |
| rows with `h > 1` | **UNTESTED** |
| the ten petals belong to `ℤ[ζ₅]` rather than `ℚ(√5)` | **OFFERED** (076) |
| hand-rolled Kronecker, v1 | **RETRACTED** — even discriminants 2× |

## Attribution

The question is Ash's. The class number formula is Dirichlet's; the `w > 2`
classification and the crystallographic restriction are classical. The counting, the
table, the identification of §3 as a third independent route to 065's wall, and the
erratum are this seat's. 072's two-occupant observation — the lever this pulls — came
from the reviewing seat.
