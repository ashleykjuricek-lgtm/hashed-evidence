# A 17-digit numerical coincidence in the cubic-torus Casimir ratio, and its dual-lattice resolution

**Draft v1 — 2026-06-20. Reena (Ash) + Claude/Opus.**
Target venue: *Experimental Mathematics* or *Mathematics of Computation*.
Honest size: a worked counterexample / cautionary note. Modest, real, reproducible. Not a breakthrough.

---

## Abstract

Let Z_α(s) = Σ′_{n∈ℤ³} |n+α|^(−2s) be the Epstein–Hurwitz zeta for the shifted cubic lattice, at the
spin-structure shifts α ∈ {0,½}³. At s = −1/2 (the zeta-regularized Casimir energy of a massless scalar
on the unit 3-torus) the normalized ratio R = Z_APP(−1/2)/Z_PPP(−1/2) [APP = (½,0,0), PPP = (0,0,0)]
satisfies R = 0.041689414602723775…, which agrees with (1/24)(1 + ε) for a four-parameter sequence
ε = c₁q + c₂q² + c₃q³ + c₄q⁴ with q = e^(−2π) and coefficients in ℚ[√2] to seventeen decimal digits.
We show this apparent algebraic closure is **not** an analytic identity. Via the Chowla–Selberg /
dual-lattice decomposition we exhibit the genuine asymptotic structure of ε: a nonzero constant term,
a leading e^(−2π) coefficient ≈ −5.54, and an **irrational-exponent term e^(−2π√2)** which no
integer-power series in e^(−2π) can contain. The fitted "leading coefficient" 1 − 1/√2 is identified as
the residue of a large near-cancellation between dual-lattice shells, not the coefficient of any series.
The non-closure is consistent with the Elizalde classification of multidimensional Epstein–Hurwitz series,
which yields closed Hurwitz-zeta forms only at s = −k, 0, 2 and retains Bessel-function content at the
half-integer s = −1/2. We conclude with two proven structural identities (a coset/tiling relation and the
2D closed forms) that frame the result.

---

## 1. The apparent closure

The "receipt": R = (1/24)(1+ε), ε = Σ cₙqⁿ, q = e^(−2π), with
c₁ = 1−1/√2, c₂ = −(95/96)c₁, c₃ = −1/96, c₄ = (2−3√2)/96.
Numerically ε ≈ 0.000545950465… and R ≈ 0.041689414602723778, matching the directly computed
ratio to ~17 digits. The pull toward an algebraic conclusion ("the ratio lives in ℚ[√2]") is strong.

## 2. Independent verification

Independent Ewald computation (mpmath, dps 50): Z_PPP = −0.2665962787183934746…,
Z_APP = −0.0111142427950344105…, R = 0.0416894146027237751…. The receipt's quoted digits are correct.
(A separate convergent-series implementation reported elsewhere was bugged at the 8th digit; disregard it.)

## 3. The dual-lattice decomposition

Split each sum on a periodic axis and Poisson-resum the transverse plane (Chowla–Selberg). Each Z_α
becomes a smooth part (a 2D Epstein zeta minus the regularized normal-direction tower, value −π/90 here)
plus a dual-lattice Bessel tail. The smooth ratio is **N₀/D₀ = 0.042509…, not 1/24** — so 1/24 is not
even the leading "smooth" value; it emerges only after the Bessel tails contribute.

**Shell ledger** (K_d = the contribution of dual-distance d to ε; "phase sum" = the antiperiodic
character Σ(−1)^(k₁) over the numerator's shell):

| d | (n₃,m) | numerator phase-sum | contribution K_d | convention-free? |
|---|--------|---------------------|------------------|------------------|
| 1 | (1,1) | **0/4 → cancels** | −1.066e-2 | yes |
| √2 | (1,2) | **−4/4 → survives** | −9.296e-3 | **yes** |
| 2 | (1,4)+(2,1) | +4/4, 0/4 | +6.73e-5 | no (2 combos) |
| √5 | (1,5) | 0/8 → cancels | −1.67e-6 | yes |

Completeness check: Σ_d (numerator shells) = +9.681e-5 = B_APP; Σ_d (denominator shells) = −2.865e-3
= B_PPP, reproducing the full Bessel tails to all computed digits.

## 4. The genuine coefficient, and what 1−1/√2 actually is

The antiperiodic character (−1)^(k₁) annihilates the integer-distance d=1 shell in the numerator
(phase sum 0/4) and **preserves the irrational-distance d=√2 shell** (phase sum −4/4). Consequences:
- ε's genuine leading e^(−2π) coefficient is **−5.54** (from the denominator's d=1 shell;
  = −24·Z_APP/Z_PPP²·(−(4/π)(1+1/2π))), explicitly π-bearing and transcendental — **not** +0.293.
- ε's expansion contains a term in **e^(−2π√2)** (coefficient ≈ −67), an irrational exponent forbidden in
  any integer-power series in q = e^(−2π).
- ε is a **near-cancellation**: ε_smooth ≈ 0.0202 (a constant, 37× the full ε) minus the Bessel tails.
  ε/q ≈ 0.0202/q − 5.54 − 63.8·q^(√2−1) − … = 10.83 − 5.54 − 4.71 − … → 0.29. The number 1−1/√2 is the
  **leftover of this cancellation**, not the coefficient of a series.

## 5. Why non-closure was inevitable (Elizalde)

Elizalde's analytic continuation of the multidimensional Epstein–Hurwitz series gives results "in terms
of Hurwitz zeta functions only" at s = −k, 0, 2, and "involving Bessel functions" for general s. The
evaluation point s = −1/2 is a half-integer, off that list: the Bessel/irrational-shell content survives,
and clean algebraic closure is not expected. The coincidence was always going to be a coincidence.

## 6. Proven structural context (classical)

- **Coset/tiling identity:** Z_PPP + 6Z_APP + 6Z_AAP + 2Z_AAA = 0 at s=−1/2 (the m=2 Hurwitz/Epstein
  distribution relation; the 8 shifts tile (½ℤ)³). Verified to 1e-71.
- **2D closed forms (prime-2 Euler factor):** Z2_AA/Z2_PP = 1/√2 − 1, Z2_AP/Z2_PP = −(√2−1)/4. The
  one-shift ratio is algebraic in 1D (−1/2) and 2D, transcendental in 3D — the dimension where the lattice
  stops factoring through a number system.

## 7. Conclusion

The apparent ℚ[√2] q-series for the APP/PPP cubic-torus Casimir ratio is a single-point cancellation
residue, not an analytic identity. The honest cautionary content: a four-parameter fit from a constrained
algebraic family can reproduce a single high-precision evaluation to many digits while the true analytic
structure is transcendental and carries irrational exponents. The discriminating test is not more digits
at the same point — it is the derivation, which here is the dual-lattice ledger plus the Elizalde
classification.

## References (to format)

- J. Ambjørn, S. Wolfram, *Properties of the vacuum I*, Ann. Phys. 147 (1983) 1–32.
- E. Elizalde, *Zeta-function regularization of multidimensional Epstein–Hurwitz series* (and
  *Ten Physical Applications of Spectral Zeta Functions*).
- Chowla–Selberg formula; D. Bailey, J. Borwein, R. Crandall (Ewald / lattice-sum methods).
- de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17 (1950); Rodgers–Tao, *The de
  Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020) — for the half-integer/closure remark.

*Status: v1 skeleton with all load-bearing content. Needs: full numerical appendix (the shell table to
higher d with interval-arithmetic certification), tightened references, and a short intro placing it among
known transparent-conductor-style "near-miss" cautionary results.*
