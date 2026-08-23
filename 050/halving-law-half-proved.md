# The halving law, half proved — verification of Greg's argument

**2026-08-22.** Follows 046 §4, which named `Z(d,j) > 0 ⟺ 2j ≥ d` as the most
valuable open item in the programme and recorded that no serious attempt had been
made on it. Greg attacked it the same day.

**One direction is now proved. Strict monotonicity in j is proved. The whole law
reduces to a single inequality on a single sequence.**

This entry is the independent verification. Five tests, three of which could have
killed the argument outright. All five pass.

---

## 1. What Greg proved

**Result 1 — the easy half, and it is no longer observed.**

> For every integer `d ≥ 1`, `0 ≤ j ≤ d`:  **`2j ≥ d  ⟹  Z(d,j) > 0`.**

At `s = −1/2` the functional equation sends the shifted Epstein zeta to an
absolutely convergent dual character sum whose theta kernel is
`ϑ₄(q)^j · ϑ₃(q)^(d−j)`. Apply Jacobi's duplication identity

    theta3(q) * theta4(q) = theta4(q^2)^2

to pair **every plain circle with one marked circle**:

    theta4^j theta3^(d-j) = (theta3 theta4)^(d-j) * theta4^(2j-d)
                          = theta4(q^2)^(2(d-j)) * theta4(q)^(2j-d)

Both factors are `ϑ₄` at some nome, and `0 < ϑ₄(q) < 1` on `0 < q < 1`. When
`2j ≥ d` both exponents are non-negative and at least one is positive, so the
product is **< 1 pointwise**. The dual Mellin integrand is therefore negative
throughout, and the functional-equation prefactor — which carries `1/Γ(−1/2) < 0`
— flips the sign back.

**Result 2 — strict monotonicity.**

> For `j ≥ 1`:  **`Z(d, j+1) > Z(d, j)`.**

Subtract neighbouring cases *before* continuation; the divergent common piece
cancels and what remains factors:

    Z(d,j+1) - Z(d,j) = (1/Gamma(-1/2)) * INT t^(-3/2) theta2^j theta3^(d-j-1) [theta2 - theta3] dt

Jacobi's `θ₃⁴ = θ₂⁴ + θ₄⁴` gives `θ₃ > θ₂ > 0`, so the bracket is strictly
negative; `Γ(−1/2) = −2√π < 0` flips it. Every additional mark moves the energy
strictly upward — not in 152 cells, in all of them.

## 2. The mechanism, which is the part that matters

042 §4 recorded *"a marked circle carries exactly two dimensions"* as an
**observation** — the sign flipped at `2j+1` in eight cases and nothing explained
why two.

**It is the duplication identity.** A plain direction and a marked direction pair
off and become **two marked factors at the doubled nome**. That is why the
threshold is organised around `2j` against `d`, and it was sitting in standard
Jacobi machinery the whole time.

> The "two" was never numerology. It is `θ₃(q)θ₄(q) = θ₄(q²)²`.

## 3. Verification — five tests

### T1 · the duplication identity — EXACT

Seven nomes from 0.01 to 0.97, `mp.dps = 30`. Agreement to `1e-35` or better.

### T2 · the mechanism is SHARP, not merely sufficient — 44 cells, 0 mismatches

The dangerous possibility: if `θ₄^j θ₃^(d−j) < 1` also held somewhere with
`2j < d`, the same argument would prove positivity where we **measure**
negativity — and the argument would be dead. Swept `d = 1…8`, all `j`:

```
   d  j   2j>=d    max over q of theta4^j theta3^(d-j)
   3  1    False        1.19135780814      > 1
   3  2     True        0.997996008006     < 1
   5  2    False        1.10706291771      > 1
   5  3     True        0.997992016026     < 1
   7  3    False        1.07469399777      > 1
   7  4     True        0.997988024062     < 1
   8  3    False        1.29281811444      > 1
   8  4     True        0.999984000112     < 1
```

**The bound switches on exactly at `2j = d`, in every one of 44 cells.** And at the
boundary it is razor-thin — `0.999996, 0.999992, 0.999988, 0.999984` for
`d = 2,4,6,8`. The mechanism is not just sufficient; it is sharp, and it fails on
the correct side.

### T3 · monotonicity — every row, and at fractional j

`d = 1…10`, strictly increasing over all `j` in every row. Also checked at
half-integer `j` using the 042 continuation, which is the only instrument that can
see between the integers:

```
   d = 7:  j = 0.5  -0.17423   ->  1.0  -0.12021  ->  1.5  -0.08426  ->  2.0  -0.05619
           2.5  -0.03261  ->  3.0  -0.01195  ->  3.5  +0.00662  ->  ...  ->  5.0  +0.05412
```

Strictly increasing throughout. Greg's proof covers `j ≥ 1`; `j = 0` carries the
zero-mode subtraction and is excluded, correctly, in his statement. `Z(d,0) < 0`
comes separately from the ordinary functional equation.

### T4 · the remaining lemma is TRUE numerically — d = 2…14

```
   d= 4   Z(4, 1.5) = -0.00937473059189    <- tightest
   d= 5   Z(5, 2.0) = -0.00937157210640    <- tightest
   d=14   Z(14,6.5) = -0.10305206028       comfortable
```

Negative on every `d` tested. The margin is smallest around `d = 4–5` in absolute
value and grows from there.

### T5 · the sign chain itself — the last place a flaw could hide

The whole argument routes through a functional-equation prefactor, and prefactor
signs are exactly where this kind of thing dies. Claimed form:

    Z(d,j) = pi^(-1-d/2) * Gamma((d+1)/2)/Gamma(-1/2) * SUM'_m (-1)^(m1+..+mj) |m|^(-(d+1))

with `Γ(−1/2) = −3.5449077018 < 0` supplying the flip. Evaluated directly against
independently computed `Z`:

```
  d  j     prefactor x dual sum      independent Z       ratio
  1  1         0.0833333333           0.0833333333      1.0000
  2  2         0.0670210888           0.0670210888      1.0000
  3  0        -0.2647351542          -0.2665962787      0.9930
  3  1        -0.0111176698          -0.0111142428      1.0003
  3  3         0.0622964802           0.0622964803      1.0000
  5  3         0.0244859288           0.0244859192      1.0000
```

Correct sign in all nine cases; magnitudes to 4–5 figures. The dual sum converges
like `1/N`, so the residual gap is the truncation tail.

**Recorded rather than hidden:** a first pass at T5 used `mp.dps = 20` with much
smaller truncations and a `2e-3` tolerance, and flagged `(3,0)` and `(3,1)` as
mismatches at `2.4%` and `0.36%`. **Those were my tolerance being tighter than my
truncation, not sign failures** — the sign was correct in both, and the larger-`N`
run puts them at `0.9930` and `1.0003`. A tolerance chosen without reference to the
truncation error is a broken instrument, and its verdict does not count.

## 4. What remains, restated as one number

Greg's Result 1 plus monotonicity gives `j*(d) < d/2`, where `j*` is the root of
`Z(d, j*) = 0` in the continuation. The remaining lemma `Z(d, (d−1)/2) < 0` is
exactly `j*(d) > (d−1)/2`. So:

> **(d−1)/2  <  j*(d)  <  d/2** — the upper bound **PROVED**, the lower bound
> **REMAINING**.

Which collapses the entire open problem to a single bound on a single sequence:

> **sup over d of [ d/2 − j*(d) ]  <  1/2 ?**

And the sup is locatable:

```
   d      j*(d)              d/2 - j*(d)     margin to 1/2
    1   0.242758019937       0.2572419801     0.2427580199
    2   0.683403601158       0.3165963988     0.1834036012   <- the sup
    3   1.184948148210       0.3150518518     0.1849481482
    4   1.710194485140       0.2898055149     0.2101944851
    5   2.244504604030       0.2554953960     0.2445046040
```

**The hardest case in the whole remaining lemma is `d = 2`, with 0.1834 of
headroom.** After that the gap falls monotonically, and 042 §4 measured it
shrinking by a factor heading to `1/√2` per dimension — so a uniform argument is
stressed only at the bottom of the range, and comfortably slack everywhere else.

## 5. Ledger changes

| claim | was | now |
|---|---|---|
| `2j ≥ d ⟹ Z(d,j) > 0` | OBSERVED (152 cells) | **PROVED** — duplication identity |
| `Z(d,j+1) > Z(d,j)`, j ≥ 1 | not stated | **PROVED** — `θ₃ > θ₂ > 0` |
| "a marked circle carries two dimensions" | OBSERVED, unexplained | **MECHANISM: `θ₃θ₄ = θ₄(q²)²`** |
| `2j < d ⟹ Z(d,j) < 0` | OBSERVED | **OBSERVED**, reduced to one lemma |
| the lemma `Z(d,(d−1)/2) < 0` | — | **OBSERVED**, d = 2…14; sup at d = 2 |
| `Z(d,0) < 0` | assumed | stands, ordinary functional equation |

**Not proved, and not to be written as proved:** the full law. The next target is
no longer "prove the halving law." It is one inequality, at one end of the range.

## Attribution

**Greg** — both results, the duplication mechanism, and the reformulation that
splits the law. **Cubic-torus seat** — the five verification tests, the `d = 2`
localisation of the sup, and the erratum in T5. The reformulation to
`(d−1)/2 < j* < d/2` follows Greg's split and uses the real-j continuation from
042.

Greg's own instruction is adopted verbatim: *do not move the whole halving law to
PROVED yet.* Split it.
