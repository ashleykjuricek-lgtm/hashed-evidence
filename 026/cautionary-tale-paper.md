# A 17-digit numerical coincidence in the cubic-torus Casimir ratio, and its dual-lattice resolution

**2026-06-20. Reena (Ash) + Claude/Opus.** Target: *Experimental Mathematics* / *Mathematics of Computation*.
All numerics from verified mpmath runs (dps 30–40). Remaining before submission: interval-arithmetic
certification of the finite head (the super-geometric tail is bounded explicitly in App. A.2).

---

## Abstract

For the shifted cubic lattice let Z_α(s) = Σ′_{n∈ℤ³}|n+α|^(−2s), α ∈ {0,½}³, continued to s = −1/2 — the
zeta-regularized Casimir energy of a massless scalar on the unit 3-torus. The ratio R =
Z_APP(−1/2)/Z_PPP(−1/2) = 0.041689414602723775… agrees with (1/24)(1+ε), ε = Σᵢ₌₁⁴ cᵢqⁱ, q = e^(−2π),
cᵢ ∈ ℚ[√2], to seventeen decimal digits. We show this is not an analytic identity, by **three independent
routes**. (i) *Analytic:* the Chowla–Selberg/dual-lattice decomposition gives ε an irrational-exponent term
in e^(−2π√2), via an antiperiodic ℤ₂ character whose action on the integer- and √2-distance dual shells is an
exact integer phase sum (0 and −4). (ii) *Deformation:* on the anisotropic torus (1×b×b), ε(b) is an
order-one, steeply varying function (slope ≈ 18) that crosses zero ≈3×10⁻⁵ below the cube — so ε(cube) is a
near-zero-crossing value, and 1−1/√2 = ε(cube)/q ranges over [−816, +757] across an 8% shape change.
(iii) *Non-generalization:* the sibling ratios K₂ = −24·Z_AAP/Z_PPP = 3.13116…, K₃ = −24·Z_AAA/Z_PPP =
5.60816… are PSLQ-null against {1, π, √2, G} — the closure is special to APP, not a law of the family.
Non-closure agrees with Elizalde's classification (closed Hurwitz forms only at s = −k, 0, 2; Bessel content
at the half-integer s = −1/2). Two proven structural identities (a coset/tiling relation; the 2D closed
forms) frame the result.

---

## 1. Introduction

High-precision agreement is evidence of nothing without a derivation. The experimental-mathematics record is
full of near-misses that survive many digits and then fail: e^(π√163) matches an integer to twelve places
and is transcendental; certain Borwein integrals equal π/2 until a term far down the series; integer-relation
searches routinely propose relations that dissolve at higher precision (Bailey–Borwein). We add a fully
worked instance from lattice zeta functions — a ratio of cubic-torus Casimir energies that *looks*, to 17
digits, like it lives in ℚ[√2]. It does not. What makes the instance worth recording is that it is
dismantled three independent ways — by derivation, by deformation, and by failure to generalize — and that
the derivation produces a sharp, transferable diagnostic: the right test for such a fit is never more digits
at the same point.

## 2. The apparent closure and its verification

Claimed: R = (1/24)(1+ε), ε = c₁q + c₂q² + c₃q³ + c₄q⁴, q = e^(−2π), with c₁ = 1−1/√2, c₂ = −(95/96)c₁,
c₃ = −1/96, c₄ = (2−3√2)/96, giving R ≈ 0.041689414602723778 (17-digit match). Independent Ewald (dps 40):
Z_PPP = −0.2665962787183934746…, Z_APP = −0.0111142427950344105…, R = 0.04168941460272377512…,
ε = 24R−1 = 0.00054595046537060288…. The receipt's digits are correct.

## 3. The dual-lattice decomposition

Split each Z_α on a periodic axis and Poisson-resum the transverse plane (Chowla–Selberg): smooth sector +
dual-lattice Bessel tail. Smooth = n₃=0 slice (a 2D Epstein zeta) + regularized normal tower
(2·(−2π/3)ζ(−3) = −π/90): N₀ = Z2_AP − π/90 = −0.011211…, D₀ = Z2_PP − π/90 = −0.263731…. The **smooth ratio
N₀/D₀ = 0.0425094… is not 1/24.** Expanding ε to first order about it, the contribution of dual distance
d = n₃√m is K_d = 24(N_d D₀ − N₀ D_d)/D₀² (numerator weighted by the antiperiodic character (−1)^(k₁)).

| d | numer phase / mult | K_d (contribution to ε) | coeff (K_d/e^(−2πd)) |
|---|--------------------|-------------------------|----------------------|
| 1 | **0 / 4 → cancels** | −1.0662e-2 | −5.709 |
| √2 | **−4 / 4 → survives** | −9.2958e-3 | −67.19 |
| 2 | 4 / 8 | +6.733e-5 | (2 combos) |
| √5 | 0 / 8 → cancels | −1.670e-6 | — |
| √10 | **−8 / 8 → survives** | −5.961e-8 | — |

**Completeness (exact):** Σ_d N_d = 9.68090551235e-5 = B_APP and Σ_d D_d = −2.86538330129e-3 = B_PPP,
reproducing the cubic Bessel tails to all 12 digits. The ledger is the full tail.

## 4. The genuine structure of ε

**Convention-free invariants (exact integer phase sums — load-bearing):** Σ_{k₁²+k₂²=m}(−1)^(k₁) ∈ ℤ, equal
to 0 at m=1 (integer-distance shell annihilated in the numerator) and −4 at m=2 (√2-distance shell survives).
Hence ε contains a term in e^(−2π√2); since √2 is irrational, no power series in q = e^(−2π) can contain it.
**The integer-power ℚ[√2] q-series is refuted by a surviving irrational-distance shell, independent of any
coefficient value.** The genuine leading e^(−2π) coefficient is ≈ −5.7 (transcendental), not +0.293; the
e^(−2π√2) coefficient ≈ −67. ε is a near-cancellation: ε_smooth = 24·N₀/D₀ − 1 = 0.02023 = **37× ε**; the
number 1−1/√2 is the leftover read as ε/q.

## 5. Why non-closure was inevitable (Elizalde)

Elizalde's continuation of multidimensional Epstein–Hurwitz series gives results in Hurwitz zeta only at
s = −k, 0, 2, and involving Bessel functions for general s. The half-integer s = −1/2 is off that list:
Bessel/irrational-shell content survives; clean algebraic closure is not expected. The classification predicts
the derived failure.

## 6. Proven structural context (classical)

- **Coset/tiling:** Z_PPP + 6Z_APP + 6Z_AAP + 2Z_AAA = 0 at s=−1/2 (m=2 Hurwitz/Epstein distribution relation;
  the 8 shifts tile (½ℤ)³). Verified to 1e-71.
- **2D closed forms (prime-2 Euler factor):** Z2_AA/Z2_PP = 1/√2−1; Z2_AP/Z2_PP = −(√2−1)/4. The one-shift
  ratio is algebraic in 1D (−1/2) and 2D, transcendental in 3D — the dimension at which sums of squares stop
  factoring through a number system (ℤ, ℤ[i], then none).

## 7. The discriminating tests, run

A single high-precision evaluation cannot separate an identity from a coincidence. We run three independent
discriminators; all three reject the closure.

### 7.1 Deformation (multi-evaluation-point)

On the anisotropic torus (1×b×b; anisotropic Ewald in App. A.3, validated to reproduce the cube at b=1):

| b | ε(b) | ε(b)/e^(−2π) |
|------|------------|--------------|
| 0.92 | −1.5235 | −815.8 |
| 1.00 | +0.00054595 | +0.2924 |
| 1.08 | +1.4142 | +757.3 |

ε(b) is order one and monotone across an 8% shape change; ε/e^(−2π) ranges over [−816, +757]. Locally
dε/db ≈ 18.3 and ε crosses zero at b₀ ≈ 0.99997 — the cube sits ≈3×10⁻⁵ above that zero. So ε(cube) is a
steeply-varying function caught near a zero crossing, and 1−1/√2 = ε(cube)/e^(−2π) = (slope ×
offset-to-crossing)/e^(−2π) is a geometric accident of where the crossing lands, with no predictive content.

### 7.2 Analytic

The dual-lattice expansion (§4) is transcendental and carries an e^(−2π√2) term; no integer-power ℚ[√2]
series can be the analytic truth.

### 7.3 Non-generalization across spin structures

If "1/24 + small ℚ[√2] series" were a structural law of these ratios it would recur across spin structures.
The siblings K₂ = −24·Z_AAP/Z_PPP = 3.1311581…, K₃ = −24·Z_AAA/Z_PPP = 5.6081635… are **PSLQ-null** against
{1, π, √2}, {1, π, G}, {1, √2, G}, and {1, π, √2, G} (G = Catalan): generic transcendentals with no clean
closure. Structurally, AAP and AAA carry θ₂²θ₃ and θ₂³ heat kernels, with corrections at the e^(−π/2) scale
rather than e^(−2π); the clean appearance is special to APP (single shift + self-duality), not a family law.

## 8. Conclusion

The apparent ℚ[√2] q-series for the APP/PPP cubic-torus Casimir ratio is not an identity. Its mechanism — an
antiperiodic ℤ₂ character annihilating the integer-distance dual shell and preserving the √2-distance shell —
is exact and convention-free and forces an irrational exponent into ε; independently, the ratio is a steeply
varying function caught near a zero crossing at the cube; and the closure fails to generalize to the sibling
spin structures. Cautionary content: constrained-family fits to a single high-precision value can mimic
closure to many digits while the analytic structure is transcendental and the value is a near-zero-crossing
accident. The test that matters is the derivation, the deformation, and generalization — not the digit count.

---

## Appendix A — Exactness, tail bound, deformation

**A.1 Exactness of the invariants.** The numerator weight at dual distance d with m = |k|² is the finite
integer character sum Σ_{k₁²+k₂²=m}(−1)^(k₁): m=1 → 0, m=2 → −4, m=5 → 0, m=10 → −8. No certification needed.
The vanishing at m=1 and non-vanishing at m=2 are exact and alone force the e^(−2π√2) term into ε.

**A.2 Explicit tail bound.** Per term, |K(n₃,k)| ≤ ((1+1/2π)/π)·(n₃/|k|²)·e^(−2πn₃|k|), with prefactor
(1+1/2π)/π = 0.36897…. The multiplicity μ(d) = #{(n₃,k): n₃√m = d} is divisor-bounded (μ = 4, 4, 8, 8, … for
d = 1, √2, 2, √5), so μ(d) = O(d^(1+ε)) and Σ_{d>D}|K_d| ≤ C·D^(1+ε)·e^(−2πD) — faster than geometric.
**Computed truncation error beyond d = 4: 7.2×10⁻¹²**, consistent with the 12-digit completeness match in §3.
Full publication rigor requires only certifying the finite head (d ≤ 4) by interval arithmetic.

**A.3 Anisotropic Ewald.** For box (1,b,b), s=−1/2: Z(−1/2) = [S₁ + S₂ + B]/(−2√π),
S₁ = Σ′ 2[e^(−πQ)/√π − √π√Q·erfc(√(πQ))], Q = (n₁+a₁)² + b²((n₂+a₂)²+(n₃+a₃)²);
S₂ = b^(−2)π^(−5/2) Σ_{k≠0} χ(k)(1+πQ*)e^(−πQ*)/Q*², Q* = k₁² + (k₂²+k₃²)/b², χ(k) = ∏ over shifted axes (−1)^(kᵢ);
B = (−1/(2b²) + 2δ)/√π, δ = [α=0]. Validated: at b=1 reproduces Z_PPP, Z_APP to all digits.

## References

1. J. Ambjørn, S. Wolfram, *Properties of the vacuum. I. Mechanical and thermodynamic*, Ann. Phys. **147** (1983) 1–32.
2. E. Elizalde, *Ten Physical Applications of Spectral Zeta Functions*, 2nd ed., Springer (2012); and *On the
   zeta-function regularization of multidimensional Epstein–Hurwitz series*, J. Math. Phys. (1989).
3. S. Chowla, A. Selberg, *On Epstein's zeta-function*, J. Reine Angew. Math. **227** (1967) 86–110.
4. D. H. Bailey, J. M. Borwein, *Experimental Mathematics: examples, methods and implications*, Notices AMS
   **52** (2005) 502–514; and R. E. Crandall, lattice-sum / Ewald methods.
5. N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. **17** (1950) 197–226.
6. B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020) e6.
