# A 17-Digit False Positive in a Cubic-Torus Casimir Ratio
### Dual-Lattice Obstruction and the Failure of Single-Point Numerical Induction

**v027 — 2026-06-20. Reena (Ash) + Claude/Opus.** Restructured after review by GPT ("Greg").
All numerics from verified mpmath runs (dps 30–40). One theorem (Prop 2 = §4); three supporting observations
(Props 1, 3, 4 = §§2, 5, 6). Remaining before submission: pin the Elizalde citation (§7) to an exact result;
interval-arithmetic certification of the finite head (App. A.2).

---

## Abstract

For shifted cubic lattices let Z_α(s) = Σ′_{n∈ℤ³}|n+α|^(−2s), α ∈ {0,½}³, continued to s = −½. We study
R = Z_APP(−½)/Z_PPP(−½) = 0.041689414602723775…, which agrees to **seventeen decimal digits** with a
truncated algebraic expression (1/24)(1 + Σ_{j=1}^4 c_j q^j), q = e^(−2π), c_j ∈ ℚ[√2]. We show this apparent
closure is **not an analytic identity**. A Chowla–Selberg/dual-lattice decomposition exhibits an exact
antiperiodic character sum: the integer-distance (m=1) dual shell cancels in the numerator while the
√2-distance (m=2) shell survives, and the ratio's e^(−2π√2) coefficient is nonzero (−67.19…). Since
e^(−2π√2) cannot occur in an integer-power series in q = e^(−2π), the proposed closure is impossible. The
coincidence is therefore not noise but a **structured false positive**: exact shell cancellation, together
with the cube lying on a *transversal* (steep) zero-crossing of ε in the anisotropic 1×b×b deformation,
makes a non-closed value imitate algebraic closure to high precision; the fitted coefficient 1−1/√2 is the
residue of that crossing, not a law. Sibling spin structures fail the same closure tests. The example yields
a concrete diagnostic for experimental mathematics: **a single high-precision value at a symmetric point is
not evidence for algebraic structure — the decisive tests are derivation, deformation, and generalization.**

---

## 1. Introduction (the numerical temptation)

High-precision agreement is evidence of nothing without a derivation. The experimental-mathematics record is
full of near-misses that survive many digits and then fail: e^(π√163) matches an integer to twelve places
and is transcendental; certain Borwein integrals equal π/2 until a term far down the series; integer-relation
searches routinely propose relations that dissolve at higher precision (Bailey–Borwein). We add a fully
worked instance from lattice zeta functions — a ratio of cubic-torus Casimir energies that *looks*, to 17
digits, like it lives in ℚ[√2]. It does not. What makes it worth recording is that the false positive is
dismantled by an exact derivation, its illusion is explained by a near-zero geometry, and the failure is
documented as a transferable diagnostic. We do not apologize for the seductive numerics; we let them look
seductive, then kill the pattern with one structural fact and explain why it looked true anyway.

## 2. The object and the coincidence (Proposition 1)

**Proposition 1 (the coincidence is real).** Independent Ewald computation (dps 40):
Z_PPP(−½) = −0.2665962787183934746…, Z_APP(−½) = −0.0111142427950344105…,
R = 0.04168941460272377512…, ε := 24R − 1 = 0.00054595046537060288…. The proposed
(1/24)(1 + Σ c_j q^j), q = e^(−2π), with c₁ = 1−1/√2, c₂ = −(95/96)c₁, c₃ = −1/96, c₄ = (2−3√2)/96,
reproduces R to 17 digits. The phenomenon is real enough to demand explanation.

## 3. The dual-lattice decomposition

Split each Z_α on a periodic axis and Poisson-resum the transverse plane (Chowla–Selberg): each Z_α = a
smooth sector + a dual-lattice Bessel tail. The smooth sector = n₃=0 slice (a 2D Epstein zeta) + the
regularized normal tower 2·(−2π/3)ζ(−3) = −π/90: N₀ = Z2_AP − π/90 = −0.011211…, D₀ = Z2_PP − π/90 =
−0.263731…. The **smooth ratio N₀/D₀ = 0.0425094… is not 1/24** — 1/24 appears only after the Bessel tails
contribute. Expanding ε to first order about the smooth ratio, the contribution of dual distance d = n₃√m is
K_d = 24(N_d D₀ − N₀ D_d)/D₀² (numerator weighted by the antiperiodic character (−1)^(k₁)):

| d | numer phase / mult | K_d (contribution to ε) | coeff (K_d/e^(−2πd)) |
|---|--------------------|-------------------------|----------------------|
| 1 | **0 / 4 → cancels** | −1.0662e-2 | −5.709 |
| √2 | **−4 / 4 → survives** | −9.2958e-3 | −67.19 |
| 2 | 4 / 8 | +6.733e-5 | (2 combos) |
| √5 | 0 / 8 → cancels | −1.670e-6 | — |
| √10 | **−8 / 8 → survives** | −5.961e-8 | — |

**Completeness (exact):** Σ_d N_d = 9.68090551235e-5 = B_APP and Σ_d D_d = −2.86538330129e-3 = B_PPP,
reproducing the cubic Bessel tails to all 12 digits computed. The ledger is the full tail, not a truncation.

## 4. The analytic obstruction (Proposition 2 — THEOREM, the murder weapon)

**Theorem.** ε = 24R − 1 contains a nonzero e^(−2π√2) term; hence no integer-power series in q = e^(−2π) with
coefficients in ℚ[√2] can be the exact analytic structure of R.

*Proof (each step exact or computed).*
1. By §3, Z_α = smooth + dual-lattice Bessel tail, the numerator (APP) weighted by the antiperiodic character
   (−1)^(k₁) on the transverse dual lattice.
2. The character sum over the shell |k|² = m is an **exact integer**: Σ_{k₁²+k₂²=m}(−1)^(k₁) = 0 at m=1
   (vectors (±1,0),(0,±1) carry signs −,−,+,+) and = −4 at m=2 (all four (±1,±1) carry −1). So the
   integer-distance shell is annihilated in the numerator; the √2-distance shell survives.
3. The √2 shell survives in the *numerator*; the *ratio* ε inherits an e^(−2π√2) term with coefficient
   24(N_√2 D₀ − N₀ D_√2)/D₀² = **−67.19… ≠ 0**. (The denominator's √2 shell does not cancel it.) Thus ε
   genuinely contains e^(−2π√2).
4. √2 is irrational, so e^(−2π√2) cannot appear in any power series in q = e^(−2π). ∎

The genuine leading e^(−2π) coefficient of ε is ≈ −5.7 (transcendental, π-bearing), not +0.293; and
ε_smooth = 24·N₀/D₀ − 1 = 0.02023 = **37× ε** — ε is a near-cancellation, and 1−1/√2 is the leftover read as
ε/q, not a coefficient. (The exact decimals of the coefficients are convention-dependent — which shells are
"smooth"; the integer phase sums of step 2 are not.)

## 5. The trapdoor: mechanism of the false positive (Proposition 3)

The obstruction proves the closure false; it does not explain why the false formula matched to 17 digits.
That comes from geometry. Deform to the anisotropic torus (1×b×b; anisotropic Ewald in App. A.3, validated to
reproduce the cube at b=1) and let ε(b) = 24 Z_APP(b)/Z_PPP(b) − 1:

| b | ε(b) | ε(b)/e^(−2π) |
|------|------------|--------------|
| 0.92 | −1.5235 | −815.8 |
| 1.00 | +0.00054595 | +0.2924 |
| 1.08 | +1.4142 | +757.3 |

ε(b) is order one and monotone across an 8% shape change; ε/e^(−2π) ranges over [−816, +757]. Locally
dε/db ≈ 18.3 and ε crosses zero **transversally** at b₀ ≈ 0.99997 — the cube sits ≈3×10⁻⁵ (in shape) from a
zero. The load-bearing point is the *slope, not the proximity*: a flat minimum (slope ≈ 0) near zero would
suggest a protected, structural smallness; a steep transversal crossing means the smallness is an accident of
where we sampled. So ε(cube) = 0.000546 is the residue of a steep zero-crossing, and 1−1/√2 = ε(cube)/e^(−2π)
= (slope × offset-to-crossing)/e^(−2π) is a geometric accident of where the crossing lands, with no
predictive content. *(The trapdoor explains the imitation mechanism — a near-zero residue divided by q mimics
a coefficient — not why the crossing falls near the cube, which we do not claim is structural.)*

## 6. Non-generalization across spin structures (Proposition 4)

If "1/24 + small ℚ[√2] series" were a structural law it would recur across spin structures. The siblings
K₂ = −24·Z_AAP/Z_PPP = 3.1311581…, K₃ = −24·Z_AAA/Z_PPP = 5.6081635… are **PSLQ-null** against {1, π, √2},
{1, π, G}, {1, √2, G}, and {1, π, √2, G} (G = Catalan): generic transcendentals with no clean closure.
Structurally, AAP and AAA carry θ₂²θ₃ and θ₂³ heat kernels, with corrections at the e^(−π/2) scale rather
than e^(−2π); the clean appearance is special to APP (single shift + self-duality), not a family law.

## 7. Why non-closure was inevitable (Elizalde context)

Elizalde's continuation of multidimensional Epstein–Hurwitz series yields closed Hurwitz-zeta forms at
s = −k, 0, 2 and forms involving Bessel functions for general s. The half-integer s = −½ is off that list:
Bessel/irrational-shell content survives, so clean algebraic closure is not expected. *(For submission: pin
this to the exact theorem/result, or state it as "consistent with the principle Elizalde established in the
2D case" — the precise multidimensional statement must be cited, not waved.)*

## 8. Diagnostic rule

A single high-precision evaluation at a symmetric point cannot distinguish an algebraic identity from a
structured false positive: a few coefficients from a constrained family fit one number, and a value near a
zero-crossing imitates closure. The decisive tests are **derivation** (the exact obstruction), **deformation**
(transversal vs minimum), and **generalization** (does it recur across siblings). The right test for such a
fit is never more digits at the same point.

## 9. Conclusion

The apparent ℚ[√2] q-series for the APP/PPP cubic-torus Casimir ratio is not an identity. Its mechanism — an
antiperiodic ℤ₂ character annihilating the integer-distance dual shell and preserving the √2-distance shell —
forces an irrational exponent into ε (the proof); independently, the ratio is a steeply-varying function
caught on a transversal zero-crossing at the cube (the illusion); and the closure fails to generalize to the
sibling spin structures (the corroboration). It is a documented failure mode of single-point numerical
induction, not a hidden law in the digits.

---

## Appendix A — Exactness, tail bound, deformation

**A.1 Exactness of the invariants.** The numerator weight at dual distance d with m = |k|² is the finite
integer character sum Σ_{k₁²+k₂²=m}(−1)^(k₁): m=1 → 0, m=2 → −4, m=5 → 0, m=10 → −8. No numerical
certification needed. The vanishing at m=1 and non-vanishing at m=2 alone force the e^(−2π√2) term into ε.

**A.2 Explicit tail bound.** Per term, |K(n₃,k)| ≤ ((1+1/2π)/π)·(n₃/|k|²)·e^(−2πn₃|k|), prefactor
(1+1/2π)/π = 0.36897…. The multiplicity μ(d) = #{(n₃,k): n₃√m = d} is divisor-bounded (μ = 4, 4, 8, 8 for
d = 1, √2, 2, √5), so μ(d) = O(d^(1+ε)) and Σ_{d>D}|K_d| ≤ C·D^(1+ε)·e^(−2πD) — faster than geometric.
**Computed truncation error beyond d = 4: 7.2×10⁻¹²**, consistent with the 12-digit completeness match (§3).
Full rigor needs only certifying the finite head (d ≤ 4) by interval arithmetic.

**A.3 Anisotropic Ewald (deformation).** For box (1,b,b), s = −½: Z(−½) = [S₁ + S₂ + B]/(−2√π),
S₁ = Σ′ 2[e^(−πQ)/√π − √π√Q·erfc(√(πQ))], Q = (n₁+a₁)² + b²((n₂+a₂)²+(n₃+a₃)²);
S₂ = b^(−2)π^(−5/2) Σ_{k≠0} χ(k)(1+πQ*)e^(−πQ*)/Q*², Q* = k₁² + (k₂²+k₃²)/b², χ(k) = ∏_{shifted axes}(−1)^(kᵢ);
B = (−1/(2b²) + 2δ)/√π, δ = [α=0]. Validated: at b=1 reproduces Z_PPP, Z_APP to all digits.

## References

1. J. Ambjørn, S. Wolfram, *Properties of the vacuum. I.*, Ann. Phys. **147** (1983) 1–32.
2. E. Elizalde, *Ten Physical Applications of Spectral Zeta Functions*, 2nd ed., Springer (2012); and the
   multidimensional Epstein–Hurwitz continuation papers (exact result to be cited; see §7).
3. S. Chowla, A. Selberg, *On Epstein's zeta-function*, J. Reine Angew. Math. **227** (1967) 86–110.
4. D. H. Bailey, J. M. Borwein, *Experimental Mathematics: examples, methods and implications*, Notices AMS
   **52** (2005) 502–514; R. E. Crandall, lattice-sum / Ewald methods.
5. N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. **17** (1950) 197–226.
6. B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020) e6.
