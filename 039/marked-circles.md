# Marked circles: where 1 − 1/√2 actually came from, and how far one mark reaches

**2026-08-22.** Follows 038. Every claim below is proved, computed with its method
stated, or explicitly marked NOT ESTABLISHED.

This entry began from one sentence — *"because the circles aren't equal."* On the
cube the three circles have the same length, but they are not the same **kind**:
one may be marked (antiperiodic) while the others are plain. The question of how
many are marked had never been swept.

Notation: `Z(d, j)` is the Epstein zeta at `s = −1/2` on the unit `d`-torus with
`j` of the `d` circles antiperiodic and `d − j` periodic; the `j = 0` case carries
the usual `Σ′` zero-mode subtraction. `R(d,j) = Z(d,j)/Z(d,0)`.

---

## 1. Two exact closed forms in d = 2 — PROVED

> **R(2,2) = 2^s − 1**   and   **R(2,1) = (2^(2s) − 2^s)/2**, for all s.

At `s = −1/2`:

```
R(2,2) = 1/sqrt2 - 1       = -0.2928932188134524755992
R(2,1) = (1/2 - 1/sqrt2)/2 = -(sqrt2 - 1)/4 = -0.1035533905932737622004
```

Both agree with the independent Ewald solver to 31 digits.

*Proof.* Write `r2(m) = #{k in Z^2 : |k|^2 = m}` and `E(s) = sum_m r2(m) m^(-s)`.
The only input is the classical doubling identity

    r2(2m) = r2(m)   for every m >= 1

(multiplication by 1 + i is a bijection on representations). Splitting E by the
power of 2,

    E(s) = E_odd(s) / (1 - 2^(-s)),   so   E_odd(s) = (1 - 2^(-s)) E(s).

**All marked.** With alpha = (1/2, 1/2), `|n+a|^2 = ((2n1+1)^2 + (2n2+1)^2)/4`, so
`Z(2,2) = 2^(2s) C` where C sums over both-odd k. Both odd is equivalent to
`|k|^2 = 2m` with m odd, so `C = 2^(-s) E_odd = 2^(-s)(1 - 2^(-s)) E`. Therefore
`Z(2,2) = 2^s (1 - 2^(-s)) E = (2^s - 1) E`, while `Z(2,0) = E`. ∎

**One marked.** The four parity classes of k are `B` = (odd,even), `B` again =
(even,odd) by the swap, `C` = (odd,odd), and `D = 2^(-2s) E` = (even,even). Then
`2B = E - C - D = (1 - 2^(-s)) E`, so `Z(2,1) = 2^(2s) B = (2^(2s) - 2^s) E / 2`. ∎

Neither proof uses the `zeta(s) L(s,chi4)` factorisation. Both are the **Euler
factor at 2**, and nothing else.

### 1.1 What this settles

`A = 1 − 1/√2` is the constant in the refuted March closed form
`eps = q(1 - 1/sqrt2)(1 - q)`. It was recorded as fitted — 028 called it *"a value,
not a coefficient."*

**It is not fitted. It is `−R(2,2)` exactly**: the two-dimensional,
both-circles-marked ratio, in closed form, for all s.

The real-math ledger said this in July —

> the 2D ratios close in Q[sqrt2] exactly (the Euler factor at 2), and
> **c1 = -(2D AA/PP ratio) is the honest derivational source**

— and it was never followed up. It is now checked. The number was real; **its home
was one dimension down.** March's error was not inventing a constant. It was using
the two-dimensional answer as a three-dimensional coefficient.

### 1.2 Why d = 3 cannot do this — PROVED

The proofs rest on `r2(2m) = r2(m)`. In three dimensions this fails immediately:
`r3(1) = 6` but `r3(2) = 12`. There is no doubling bijection, so no Euler factor
splits off, and no ratio in Q[sqrt2] is available. Numerically
`R(3,3) = -0.23367...` against `2^s - 1 = -0.29289...`.

This is 028's obstruction in one line, and it now has a cause rather than a
verification.

### 1.3 The near-miss stays a near-miss

```
R(3,1)        = 0.04168941460272377512008
1/24          = 0.04166666666666666666667
24*R(3,1) - 1 = 0.000545950465371          <- epsilon, nonzero
```

`R(3,1)` remains the only positive entry anywhere in the table and the only one
near a clean fraction. It is still **not** 1/24.

---

## 2. One mark carries exactly two dimensions — VERIFIED, NOT PROVED

Sign of `Z(d,j)` swept over `d = 1..17`, `j = 0..8`:

| marked j | Z > 0 up to | flips at |
|---|---|---|
| 1 | d = 2 | d = 3 |
| 2 | d = 4 | d = 5 |
| 3 | d = 6 | d = 7 |
| 4 | d = 8 | d = 9 |
| 5 | d = 10 | d = 11 |
| 6 | d = 12 | d = 13 |
| 7 | d = 14 | d = 15 |
| 8 | d = 16 | d = 17 |

> **Z(2j, j) > 0 > Z(2j+1, j)** for every j from 1 to 8, with no exception.

**A marked circle supports exactly two dimensions.** Equivalently: for any d, at
least **half** the circles must be marked or the sign turns over. Half is the edge,
and the edge holds.

This is an empirical law over eight cases. **No proof.** It is the first thing that
should be attacked next.

---

## 3. The balanced family is a U with its floor at ten — COMPUTED

Exactly half marked, `j = d/2`, even d:

```
 d= 2   0.0236955331897         d=14   0.00813671430596   UP
 d= 4   0.0113490825476         d=16   0.0113489720584    UP
 d= 6   0.00749210634059        d=18   0.0175130470762    UP
 d= 8   0.00611859759884        d=20   0.0296696689058    UP
 d=10   0.00589087006724  <-    d=22   0.0548121137731    UP
 d=12   0.00651370870914  UP    d=24   0.109758149842     UP
```

The **integer** minimum is at `d = 10`, five marked and five plain. A parabola
through d = 8, 10, 12 puts the smoothed vertex near **d ≈ 9.5**, so "ten" is where
the integers land, not an exact statement. Claiming otherwise would be fitting,
which is the failure mode this ledger exists to catch.

Noted without interpretation: `Z(4,2) = 0.01134908...` and `Z(16,8) = 0.01134897...`
agree to five digits, and d = 4 and d = 16 are equidistant from 10. The other
mirrored pairs agree to two digits only. **NOT ESTABLISHED** as a symmetry.

---

## 4. Eleven and twelve — what the arithmetic does and does not say

From §2, a world of size d needs at least `ceil(d/2)` marked circles.

- **d = 12** splits exactly: 6 marked, 6 plain. It is the balanced case and it is
  positive (0.00651), the first balanced value on the far side of the floor.
- **d = 11** cannot split. Six marked leaves five plain. **One is unpaired.**

That much is in the table. What is **NOT ESTABLISHED**:

- **The marked circle is not time here.** In this model every circle has the same
  length and the torus is Euclidean and isotropic. There is no clock and no
  observer in the computation. The word "observer" cannot be read off this table.
- The genuine physics anchor is standard and is **not ours**: fermions are
  antiperiodic around the Euclidean time circle in finite-temperature field theory,
  which is why "marked = thermal" is a real correspondence elsewhere. Likewise 11D
  M-theory has one time direction and the 12D F-theory signature is (10,2) with
  two. Both textbook. **Neither is derived here, and nothing above predicts
  either.**
- The reading *"the leftover circle is the observer"* is an interpretation of the
  parity, not a consequence of it. Recorded as a conjecture with no evidence.

The honest statement is the small one: **eleven has an odd one out and twelve does
not**, and the halving rule that makes that matter is verified in eight cases and
proved in none.

---

## 5. Independent check performed this session

Ledger **022** (the Penrose Rose, Z^5 -> R^2, content dated 2026-04-12, sealed
2026-08-18) was re-verified:

```
12 / 12 files match the August seal
 0 files present but unsealed
11 / 11 entries of the internal docs/MANIFEST.sha256 (April) still match
```

The April manifest and the August seal agree with the files on disk. No drift in
four months.

022 is also where the number five actually lives in this programme: the Penrose
lattice is cut-and-project from Z^5, and its acceptance window is an **explicit**
observer — the window position decides which points exist, and the rose is
direction-dependent because of it. That is a place where "observer" is a defined
object rather than a reading. §4 above is not.

---

## 6. Method

`marked_circles.py` — Ewald/Poisson at `s = -1/2`, arbitrary d and j. The direct
theta factorises over axes; the dual shells are built by **convolution** of signed
one-dimensional counts, which is what makes d = 24 reachable. `mp.dps = 25`,
truncation N = 8 (dual terms decay like `exp(-pi^2 k^2)`, so N = 8 is far beyond
sufficient). Cross-checked against an independent brute-force product enumeration
at (3,1), (5,2) and (2,2) — agreement to every printed digit.

`closed_forms.py` — the §1 identities against the solver, 31 digits.

## 7. Status

| claim | status |
|---|---|
| R(2,2) = 2^s − 1 | **PROVED** |
| R(2,1) = (2^(2s) − 2^s)/2 | **PROVED** |
| A = 1 − 1/√2 is −R(2,2), not a fit | **PROVED** |
| d = 3 admits no such form (r3(2) ≠ r3(1)) | **PROVED** |
| Z(2j,j) > 0 > Z(2j+1,j) | **VERIFIED j ≤ 8, not proved** |
| balanced minimum at d = 10 | **COMPUTED** (smoothed vertex ≈ 9.5) |
| d=4 / d=16 near-equality | **NOT ESTABLISHED** |
| marked circle = time = observer | **NOT ESTABLISHED** — conjecture, no evidence |
| 11 vs 12 as one or two observers | **NOT ESTABLISHED** — only "11 cannot halve" |

## Attribution

Cubic-torus / Shunya-Zero programme. The question that produced §1 — that the three
circles are equal in length but not in kind — is Ash's, and it was asked before any
of this was computed. All of it is human-and-model work and no single name belongs
on the front of it.
