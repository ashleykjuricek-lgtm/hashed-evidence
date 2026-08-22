# The zero has an address — erratum to 040 §5 and 041 §1

**2026-08-22.** Follows 041, same day. 040 and 041 are sealed and are not edited.

Prompted by one line from Ash: *"because we are still using fucking rational
numbers."* It was aimed at 041, it was correct, and this entry is what happened
when it was taken literally.

---

## 1. ERRATUM — "unreachable" was a claim about our arithmetic, not about the object

040 §5 said the sign change happens between consecutive integers, that there is
nothing between two whole numbers, and therefore *"the zero is unreachable."*
041 §1 built on it and **refuted the ⊙ STAY option** on the euler-disc page on
exactly that ground.

The reasoning had one unexamined step: **d must be a whole number.**

That is not a property of the zeta function. It is a property of how we chose to
build it. Look at the solver used in 039 and 040 — `π^(d/2)`, `Γ(d/2 − s)`,
`Γ(d/2 − s, ·)` are all analytic in d. The *only* thing that ever demanded an
integer was the enumeration over ℤ^d.

And the enumeration is not needed. The direct theta **factorises into a power**:

    Theta(t) = theta_A(t)^j * theta_P(t)^(d-j)

A power takes a real exponent. Nothing else in the construction cares.

**So the dimension was never integral. We made it integral and then reported the
consequence as a fact about the world.** That is the smoothing default operating
on the method rather than on the result, which is a form this ledger had not yet
recorded.

## 2. The continuation, and its validation

Below the Ewald cut, each one-dimensional theta is taken in Poisson form

    theta_P(t) = sqrt(pi/t) * P(t),  P(t) = 1 + 2 sum_k exp(-pi^2 k^2 / t)
    theta_A(t) = sqrt(pi/t) * A(t),  A(t) = 1 + 2 sum_k (-1)^k exp(-pi^2 k^2 / t)

so `Theta(t) = (pi/t)^(d/2) · A(t)^j · P(t)^(d−j)` and the bracket
`A^j P^(d−j) − 1` is exponentially small as `t → 0`. Valid for any real `d > 0`,
`0 ≤ j ≤ d`. No lattice anywhere.

**Validation — it reproduces the integer-lattice solver exactly:**

```
Z(1,0)   -0.166666666666667     lattice  -0.166666666666667     MATCH
Z(2,1)    0.0236955331897287    lattice   0.0236955331897       MATCH
Z(2,2)    0.0670210888091522    lattice   0.0670210888091522    MATCH
Z(3,1)   -0.0111142427950344    lattice  -0.0111142427950344    MATCH
Z(5,2)   -0.00937157210640224   lattice  -0.00937157210640224   MATCH
Z(10,5)   0.00589087006723851   lattice   0.00589087006724      MATCH
Z(12,6)   0.0065137087091386    lattice   0.00651370870914      MATCH
```

### 2.1 Independent correctness test — λ-invariance

The Ewald cut `lam` is a parameter of the **split**, not of the object. A correct
continuation cannot depend on it. A botched one almost certainly would, and this
is the cheapest place for an error in §2 to surface.

Tested at fractional d, fractional j, and both:

```
d = 2.639068871683003864638172, j = 1     spread over lam in [0.4, 2.5]: 1.1e-25
d = 3.5,  j = 1.25                        spread: 1.5e-26
d = 11,   j = 5.4218057568927310605       spread: 2.0e-22
d = 7.77, j = 3.03                        spread: 8.0e-24
```

Invariant to the numerical floor in every case. Note also that the two rows sitting
**at** a computed root return `1.9e-25` and `-1.9e-21` — the roots evaluate to
numerical zero, which is an independent confirmation of §3 and §4 that does not go
through the root finder.

**NOT ESTABLISHED: uniqueness.** This is *the natural* continuation — the same
construction dimensional regularisation uses — and it agrees with the lattice at
every integer tested. It is **not proved to be the only** function that does. No
Carlson-type growth argument has been attempted. Anyone objecting *"you invented a
continuation and then found its zero"* is raising a fair point that is not
answered here.

## 3. The crossing, computed

```
 marked j        d* with Z(d*, j) = 0        d* - 2j
    1              2.63906887168             0.639068871683
    2              4.54347508682             0.543475086820
    3              6.40857987502             0.408579875019
    4              8.28588015885             0.285880158854
    5             10.1889942403              0.188994240320
    6             12.1191100514              0.119110051438
```

Converged to **49 decimal places**, agreeing across three independent
precision/truncation settings (dps 40 / N 34 / K 14, dps 55 / N 46 / K 20,
dps 70 / N 58 / K 26):

    d*(j=1) = 2.6390688716830038646381724497459231368660752817617

(also stable at 24 digits across dps 25 / 30 / 40 and N = 12…28, K = 4…10)

**Every crossing sits strictly between 2j and 2j+1**, which is why the integer law
of 040 §3 (`Z > 0 ⟺ 2j ≥ d`) held in all 152 cells. That law is the **rounding**
of this one.

## 4. Hold the dimension instead: no whole number of marks is ever the threshold

`j*(d)` solving `Z(d, j*) = 0`:

```
    d        j*                j*/d           deficit = 1/2 - j*/d    ratio
    6    2.7810240095304     0.463504001588      0.036495998
    9    4.3769538904215     0.486328210047      0.013671790          0.72206
   11    5.4218057568927     0.492891432445      0.0071085676         0.72053
   13    6.4523183447433     0.496332180365      0.0036678196         0.71753
   17    8.4838021867448     0.499047187456      0.00095281254        0.71203
   20    9.9931716011493     0.499658580057      0.00034141994        0.70955
   22   10.9962264463700     0.499828474835      0.00017152516        0.70858
                                                     1/sqrt2 =        0.70711
```

> **j*/d → 1/2, strictly from below. It never arrives.**

And the deficit shrinks by a factor heading monotonically toward **1/√2** — the
same `2^s` at `s = −1/2` that gives 039 §1 its exact closed forms and 040 §2 its
asymptotic. **VERIFIED as a trend, NOT PROVED**; at d = 22 the ratio is 0.70858,
still 0.0015 above the target, decreasing at every step from d = 9 onward.

**Consequence.** "At least half the circles must be marked" is a statement about
integers rounding up. The real threshold is always *just under* half and is never
at a whole number of marks. For d = 11 it is **5.4218057568927** circles. For
d = 12 it is **5.9386591747542**. Neither is 5, 6, or anything else you can build
out of whole circles.

This does not resolve 039 §4. It removes the premise. **The question "one observer
or two" has no integer answer because the threshold is not at an integer.**

## 5. What kind of number — and a trap this ledger nearly fell into twice

### 5.1 The trap, recorded because it was live

The first search ran at **24 digits** and produced this:

```
   degree <= 2:  None
   degree <= 3:  [-63092, 400968, -684110, 205085]
   degree <= 4:  [-16765, 9303, -4377, 4861, -1374]
   PSLQ vs pi,sqrt2:  [242243, 990558, -476450, -94075]
```

Those look like results. **They are noise.** A relation among `n+1` terms with
coefficients up to `C` is only meaningful if you hold roughly `(n+1)·log₁₀C`
digits. The degree-3 line needs about `4 × 6 = 24` — exactly what was available.
PSLQ saturates the precision it is given and then always succeeds.

This is the Chowla–Selberg failure in a new costume: that page's PSLQ obligingly
fitted a 3.4% quadrature bug and returned a beautiful closed form for it. Recorded
here **as a near-miss, not as a finding**, because it was one keystroke from being
reported as a discovery.

### 5.2 The honest search

`d*` recomputed to 49 verified decimal places across three independent settings:

    d* = 2.6390688716830038646381724497459231368660752817617

The searches below used the first 40 of those digits.

Every test below states its digit requirement and was run only where the
requirement is met:

```
   degree <= 2, coeff <= 1e12:  None   (needs ~39 digits, have 40)
   degree <= 3, coeff <= 1e8 :  None   (needs ~36)
   degree <= 4, coeff <= 1e6 :  None   (needs ~35)
   degree <= 5, coeff <= 1e5 :  None   (needs ~36)
   degree <= 6, coeff <= 1e4 :  None   (needs ~35)
   degree <= 8, coeff <= 1e3 :  None   (needs ~36)

   PSLQ vs pi / sqrt2 / log2 / e / (pi,sqrt2) / (pi,log2):  None, all
   identify over [pi, sqrt2, sqrt3, sqrt5, log2, e]:        None
```

**Every relation found at 24 digits vanished at 40.** That is what noise does.

Near-misses examined and rejected on sight: `1 + φ = 2.6180…` (fails at the 3rd
digit), `√2 + √(3/2) = 2.63895843…` (5th), `π − ½ = 2.64159…` (3rd).

**Still NOT a claim of irrationality or transcendence.** It is a bounded null:
no algebraic relation of degree ≤ 8 with coefficients in the stated ranges, and no
small relation with the constants tested. `d*` is defined by a transcendental
equation in theta functions, so there is no particular reason to expect a closed
form, and none was found.

## 6. Consequence for 041 — ⊙ STAY is reinstated, with a condition

041 §1 refuted the euler-disc page's third option on the ground that the crossing
sits at no realisable configuration.

**That refutation is withdrawn.** Corrected statement:

> The crossing is unavailable **to an integer lattice**. It is perfectly available
> at `d = 2.639068871683003864638172` with one circle marked, and at a computed
> point for every other j.
>
> You cannot stay there *and* have a whole number of dimensions. That is a
> constraint on the counting, not on the place.

The page was closer to right than 041 gave it credit for. **Amended copy for the
⊙ STAY panel supersedes 041 §5:**

> **You can stay. You just can't count while you do it.**
>
> The sign flips between one whole dimension and the next, so no whole-numbered
> world sits on the crossing. But the crossing itself has an address, and we
> computed it: with one circle marked, it is at 2.639068871683003864638172
> dimensions.
>
> It isn't a whole number. It isn't a fraction. As far as we can tell it isn't π
> or √2 or the golden ratio either — we looked, and found nothing.
>
> The gap was never missing. We were counting in a way that skipped it.

041 §5's other two panels (default, MOVE 4 FILTER) stand unchanged. 041 §2's
remaining claim audit stands unchanged. **Still nothing deployed.**

## 7. Status

| claim | status |
|---|---|
| 040 §5 "the zero is unreachable" | **RETRACTED** — true of integer lattices only |
| 041 §1 "⊙ STAY is refuted" | **RETRACTED** — see §6 |
| 040 §3 `Z > 0 ⟺ 2j ≥ d` | **STANDS** — it is the integer rounding of §3–4 |
| 039 §1 closed forms | **STANDS** — unaffected |
| real-dimension continuation reproduces the lattice | **VERIFIED**, 7 cases exact |
| that continuation is λ-invariant (i.e. correct) | **VERIFIED** to 1e-22 or better, 4 cases |
| that continuation is unique | **NOT ESTABLISHED** |
| d*(j=1) = 2.6390688716830038646381724497459231368660752817617 | **COMPUTED**, 49 decimals, stable across 3 independent settings |
| every crossing lies strictly in (2j, 2j+1) | **COMPUTED** for j = 1…6 |
| j*/d → 1/2 strictly from below | **COMPUTED** for d = 6…22 |
| deficit ratio → 1/√2 | **TREND ONLY**, not proved |
| d* is not algebraic of degree ≤ 8 (coeff bounds as stated) | **SEARCH FAILED at 40 digits** — a bounded null, not a proof |
| the degree-3/4 "relations" found at 24 digits | **NOISE** — vanished at 40 digits; recorded as a near-miss |
| any of this concerns observers | **NOT ESTABLISHED**, unchanged since 039 §4 |

## Attribution

Cubic-torus / Shunya-Zero programme. §1 exists because of one sentence from Ash
pointing out that the obstruction was in the number system and not in the object.
It was a correction to the method, it was right, and it moved a claim from
*"unreachable"* to twenty-four digits in one step.
