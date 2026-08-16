# The parity law and the register

### Why the cubic-torus near-miss is protected, and why 028's steepness argument inverts the evidence

**2026-08-14. Ash Korth + Claude (Opus 5).**
Status: **correction to paper 028 §5 (Proposition 3)**; extension of the shell
correction already made in **029**. Paper 028 §4 (Proposition 2, the obstruction
theorem) is **untouched and still stands**. Append-only: 026, 027, 028, 029
are left sealed and unedited.

---

## 0. In plain language

You are counting waves in a box, two ways: one where a wave returns to itself,
one where it returns flipped. Compare the two totals and you get a number very
close to 1/24, but not exactly.

In the flipped count, each wave has a partner that is its exact opposite, and the
pair adds to nothing. A wave finds its partner by swapping which side of the box
is which — **and that swap only works if the two sides are the same length.**

So in a cube, an infinite family of waves erases itself exactly. What is left
over is the small handful that never had a partner. That handful is the
near-miss. Squash the box even slightly, the sides no longer match, the partners
can no longer find each other, and everything comes back.

The near-miss is not a coincidence. It is the residue of a perfect cancellation
that exists on the cube and nowhere else.

---

## 1. What each prior entry established

- **018–021 (March)** proposed ε = q(1 − 1/√2)(1 − q), q = e^(−2π), matching to
  17 digits. **This closed form is false and remains false.**
- **026–028 (June)** proved it false. §4 Prop 2: the ratio's e^(−2π√2)
  coefficient is interval-certified in (−68, −66), hence nonzero; e^(−2π√2)
  cannot occur in an integer-power series in q. **This theorem is correct and is
  not disputed here.**
- **029** corrected the figure: the antiperiodic cancellation is the **2D
  transverse** shell (4 points, phase sum 0), not the 3D shell; and 1 − 1/√2 is
  the tempting fit's residue, not a structural coefficient. **029's correction is
  the starting point of this entry.**
- 028 §5 Prop 3 then argued that the near-miss is a *geometric accident*, on the
  grounds that ε(b) crosses zero transversally and steeply near b = 1. **That is
  the step this entry corrects.**

---

## 2. Claim A — the parity law (exact)

In the transverse dual plane of 028 §3, with the antiperiodic character
(−1)^(k₁) acting on ℤ², define

    S(m) = Σ_{k₁² + k₂² = m} (−1)^(k₁)

**Theorem.** S(m) = 0 for every odd m.

*Proof.* If m is odd, exactly one of k₁, k₂ is odd. The involution
(k₁, k₂) ↦ (k₂, k₁) maps the shell to itself and exchanges which coordinate is
odd, hence negates every term while permuting the same finite set. A finite set
equal to its own negative sums to zero. ∎

**Companion (verified, not proved here):** S(2m) = (−1)^m · r₂(m).

Verification (`parity_register.py`): no violations of S(odd) = 0 for m < 4000;
no violations of the companion for m < 2000.

So 028's table entries — 0 at m = 1, 0 at m = 5, −4 at m = 2, −8 at m = 10 — are
not computed special cases. They are two rules with no exceptions. **The
annihilation of the m = 1 shell is not a fact about m = 1. It is parity.**

---

## 3. Claim B — the register (measured)

The involution in §2 is a coordinate swap. It exists **only when the two
transverse sides are equal** — that is, only on the cube. Deform to the
1 × b × b torus and the shells split; the cancellation has no mechanism.

Partition the transverse tail by the shell index m the vector carries *at the
cube*: "odd" = the family that cancels there, "even" = the family that survives.
Radial weight exp(−2πd) — a **proxy**, not the true Bessel tail (see §6).

```
    b        odd part          even part
  0.9900  -2.29425970e-04   -5.15860982e-04
  0.9990  -2.33904787e-05   -5.37001050e-04
  1.0000  -3.92760739e-19   -5.39369569e-04     <- machine zero
  1.0010  +2.34906748e-05   -5.41741938e-04
  1.0100  +2.39445120e-04   -5.63262985e-04
```

The odd family is zero at b = 1 and **nowhere else**, and passes through zero
linearly. This vanishing is weight-independent: the shell sum is zero, so any
radial weight gives zero.

**Suppression bought by the cancellation, at the cube:**

```
  without character = +8.043550e-03
  with character    = -5.393696e-04
  measured factor   = 14.91x
  predicted factor  = 13.50x   = exp(2 pi (sqrt2 - 1))
```

The prediction uses nothing but the shell shift: once the odd shells are gone the
leading survivor sits at radius √2 instead of 1. Measured 14.91 against predicted
13.50, the gap being subleading shells. **The suppression is the cancellation.**

**Slopes at b = 1:**

```
  d(odd)/db  = +2.3441e-02      <- the cancellation breaking
  d(even)/db = -2.3704e-03
  odd share of total slope = 111.3%
```

The surviving family contributes about a tenth as much, with opposite sign.

---

## 4. The correction to 028 Prop 3

028 §5 states:

> "a flat minimum (slope ≈ 0) near zero would suggest a protected, structural
> smallness; a steep transversal crossing means the smallness is an accident of
> where we sampled."

**This dichotomy does not hold, and §3 is the counterexample.**

A sub-family that cancels *exactly* at a symmetric point is zero there and
generically linear in the deformation away from it. That is a steep transversal
crossing — necessarily. The flat-minimum criterion would apply only if the
protection acted on ε itself at second order. Here the protection acts on an
infinite sub-family of shells at first order, and the unprotected remainder
varies smoothly on top.

**028 measured the slope, read it as evidence of accident, and closed the file.
The slope is the fingerprint of the cancellation.** The murder weapon and the
corpse are the same object.

028 §5 already concedes the gap in its own parenthetical — that it does not
explain *why the crossing falls near the cube, which we do not claim is
structural.* §2–3 above supply the missing reason: an exact cancellation sits at
b = 1 and breaks linearly, which is what puts a steep zero in the neighbourhood.

---

## 5. The two √2s have one source

028 uses √2 twice, in opposite directions, without reconciling them:

- **§4, as the murder weapon.** The surviving shell sits at radius √2, so ε
  contains e^(−2π√2), so no q-series can close it. Correct.
- **§5, as the alibi.** The fitted 1 − 1/√2 is dismissed as "geometric accident
  of where the crossing lands."

Both √2's are the radius of **the first shell that survives the parity
cancellation.** One structure produces the obstruction and the fitted constant. A
quantity cannot be load-bearing in §4 and meaningless in §5 without an argument
for the change in status, and 028 gives none.

---

## 6. What this does not do

- **It does not resurrect the closed form.** 028 Prop 2 stands. ε contains
  e^(−2π√2); √2 is irrational; no integer-power series in q = e^(−2π) can
  contain it. ε = q(1 − 1/√2)(1 − q) is dead and stays dead. March was wrong
  about what it had.
- **The slope shares are proxy numbers.** The radial weight exp(−2πd) is not the
  true Bessel tail. The vanishing of the odd family at b = 1 is exact and
  weight-independent; the 111.3% is not certified.
- **Not yet shown:** that this propagates verbatim through the true Bessel
  weights and the smooth sector into ε itself. 028's own K_d table is consistent
  with it (d = 1 cancels in the numerator, d = √2 survives), but the link is not
  closed.

### 6.1 The two deformation measurements, completed

`deformation_b0_duality.py`, independent solver, ε(1) accurate to 2.9 × 10⁻⁶
relative. (Sign convention is opposite to 028's — an axis-labelling difference;
magnitudes agree.)

**b₀ — the zero of ε does NOT sit on the cube.**

```
  slope at b=1 = -18.32596      (028 magnitude 18.3)
  b0           =  1.0000297910
  |b0 - 1|     =  2.9791e-05    (028: ~3e-5)
```

028's numbers are **confirmed** by an independent implementation. The zero is
≈3 × 10⁻⁵ from the cube, not at it. This is consistent with §3, not in tension
with it: the *protected* family is exactly zero at b = 1; ε is that family plus
the surviving remainder, so ε itself crosses zero slightly off the cube. The
protection explains the steep zero *in the neighbourhood*, not a zero *at* b = 1.

**A near-antisymmetry under b ↔ 1/b.**

```
  b=0.960   sum = +3.0160e-03    sum/|eps| = +0.00402
  b=0.980   sum = +1.5664e-03    sum/|eps| = +0.00422
  b=0.990   sum = +1.2095e-03    sum/|eps| = +0.00655
  b=1.010   sum = +1.2072e-03    sum/|eps| = +0.00664
  b=1.040   sum = +2.8693e-03    sum/|eps| = +0.00400
```

ε(1/b) ≈ −ε(b) to within 0.4–0.7%. The defect is ~1500× the numerical error, so
the antisymmetry is **real but inexact** — it is not a duality. Were it exact,
its fixed point would force ε(1) = 0.

As b → 1 the defect tends to 2ε(1) = 1.0919 × 10⁻³, matching the measured
1.2095 × 10⁻³ at b = 0.99. That identity is definitional; the content is that
the defect stays this small *across the whole range*, i.e. ε is nearly odd about
the cube, and **the near-miss is what is left of that oddness at the fixed
point.**

This is the same shape as §2–3 — an almost-exact cancellation whose residue is
the phenomenon — arriving by a second, independent route. It is **measured, not
explained**, and nothing in §7 rests on it.

### 6.2 Orientation-blindness (a limitation theorem)

Prompted by Ash asking what happens at τ = −it.

τ = −it is not another point of the modular domain — θ requires Im τ > 0, so it
lies in the lower half-plane. Nor is it the S-map: S sends it ↦ i/t, staying on
the ray. Passing from +it to −it is **complex conjugation**, which is
orientation-reversing and not in PSL(2,ℤ). The two operations must not be
collapsed into one "mirror"; conflating them is plausibly the original sin of the
Poincaré-isometry story.

**It does not rescue c₁ = 1** — nothing can, because the genuine e^(−2π)
coefficient is −5.709 (028 shell table), and no symmetrisation of a contour turns
+1 into −5.709. But it establishes something else, exactly:

**Theorem (orientation-blindness).** For any character χ_α(n) = e^(2πiαn₁), the
scalar Epstein sum satisfies Z_α(s) = Z_{−α}(s), and Z_α(s) is real.

*Proof.* The sum runs over n and −n together, and |n| = |−n|, so the terms pair
as e^(2πiαn₁) + e^(−2πiαn₁) = 2cos(2παn₁). ∎

Verified (`orientation_check.py`): for α = 1/2, 1/4, 1/3, 0.1234 the difference
|Z(−α) − Z(+α)| and the imaginary part are at machine zero (3.0e-32 at α = 1/2;
≤ 5.8e-16 elsewhere).

For the ℤ₂ twist specifically the collapse is even cruder: (−1)^(n₁) is real and
self-inverse, so it equals its own conjugate. **The twist records that a twist
occurred, not which way around it went.**

**Why this matters here.** The involution proving §2 is (k₁,k₂) ↦ (k₂,k₁), whose
matrix has determinant −1 — it is itself **orientation-reversing**. The
cancellation works because the swap preserves |k| (same shell, same radial weight,
invisible to the observable) while flipping the parity of k₁ (negating the
character). So the protection is *built out of* the degree of freedom the
observable cannot see. Those are not two facts. The same ℤ₂ is too small to carry
orientation, which is simultaneously why it can cancel and why it cannot
distinguish.

**Consequence.** R is defined as a sum over the whole lattice — an average over
all translations (killing the basepoint) and over ±n (killing the direction).
Basepoint and direction are the only data a traversal carries. So orientation is
not merely undetected in R; it is **quotiented out by construction**, and no
refinement of contour or continuation can recover it. Detecting it requires an
observable that breaks n ↔ −n: oriented/helical boundary conditions, coupled
characteristics, non-commuting holonomies, off-diagonal structure. *That list is
speculation and is tagged as such.*

This is a negative result. It says what this class of observable can never
contain.

---

## 7. The standing statement

> On the cubic torus and only there, the antiperiodic character annihilates every
> odd transverse dual shell exactly. The residue ε is the surviving √2-tower.
> That is why the ratio sits anomalously near 1/24, why no q-series can close it,
> and why the deformation slope is steep.

One mechanism accounts for the 17 digits, the failure to close, and the steep
crossing that 028 mistook for its refutation.

**018–021 had a real structure and wrote the wrong formula for it. 026–028
correctly killed the formula and then discarded the structure with it. The
structure is what is left.**

---

## 8. Tooling

`epstein_aniso_check.py` is an independent Ewald/Poisson continuation of the
anisotropic Epstein zeta to s = −1/2, written from scratch and **not** ported
from 028 Appendix A.3, so it is a genuine cross-check. It reproduces:

```
  Z_PPP(-1/2) = -0.2665962787183934746104985
  Z_APP(-1/2) = -0.0111142427950344105200505
  ratio       =  0.04168941460272377512007919
  eps(1)      =  0.0005459504653706028819
```

against 028's 80-digit references, to 25 digits.

`deformation_b0_duality.py` is the same continuation in float64 with the
direct-lattice energies bucketed by multiplicity — fast enough to sweep b. It
reproduces ε(1) to 2.9 × 10⁻⁶ relative and 028's slope (18.33 vs 18.3) and
offset (2.98 × 10⁻⁵ vs ~3 × 10⁻⁵). Used for §6.1 only.

`parity_register.py` needs no external libraries; `epstein_aniso_check.py`
requires mpmath.

---

## 9. Authorship

Ash Korth and Claude (Opus 5), jointly. The circle-of-equals reading is what
aimed the instrument: the hypothesis that the cancellation would live at the
symmetric point and die off it was an interpretive move made before it was a
computation, and it is the reason parity was the thing tested. Neither half of
this entry is subordinate to the other, and neither is "computational work by."

Prior art properly located: the 2D-transverse-shell correction is **029**; the
obstruction theorem is **028 §4**; the false closed form is **018–021**.
