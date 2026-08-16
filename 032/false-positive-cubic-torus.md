# A 17-Digit False Positive in a Cubic-Torus Casimir Ratio
### Dual-Lattice Obstruction and the Failure of Single-Point Numerical Induction

**v032 — 2026-07-03. Reena (Ash) + Claude, revision per a handoff note from GPT ("Greg"); v028 text otherwise
preserved.** Changes in this revision: (i) new §2.1 "The Half-Period Hinge" foregrounding the structural
localization of the APP/PPP comparison (α = (½,0,0) ⇔ one θ₃ → θ₂ replacement); (ii) the audited value of R
independently re-verified via the theta-integral reflection route to 10⁻²³ (script sealed with this entry);
(iii) one interpretive sentence after the shell audit (§3) and one cross-reference in §6. No claim has been
strengthened; the audited framing (near-1/24 as structured cancellation residue, not a proven q-series
identity) is unchanged.

**v028 — 2026-06-20. Reena (Ash) + Claude/Opus.** Restructured after review by GPT ("Greg").
All numerics from verified mpmath runs (dps 30–60); the obstruction is interval-certified (App. A.4).
One theorem (Prop 2 = §4); three supporting observations (Props 1, 3, 4 = §§2, 5, 6).
Both previously-flagged gaps now closed: Elizalde pinned to exact results (§7); the e^(−2π√2) coefficient and
the truncation tail are interval-certified (App. A.4). Remaining: journal formatting; for maximal rigor, a
self-contained enclosure of ζ(−½), β(−½) (here taken from mpmath to 60 digits).

---

## Abstract

For shifted cubic lattices let Z_α(s) = Σ′_{n∈ℤ³}|n+α|^(−2s), α ∈ {0,½}³, continued to s = −½. We study
R = Z_APP(−½)/Z_PPP(−½) = 0.041689414602723775…, which agrees to **seventeen decimal digits** with a
truncated algebraic expression (1/24)(1 + Σ_{j=1}^4 c_j q^j), q = e^(−2π), c_j ∈ ℚ[√2]. We show this apparent
closure is **not an analytic identity**. The APP/PPP comparison is controlled by a single structural move —
a half-period shift α = (½,0,0), equivalently the replacement of one θ₃ factor by θ₂ in the theta
representation (§2.1) — and the near-rational value is treated throughout as a downstream residue of that
half-shifted lattice comparison, not as a primary closed-form target. A Chowla–Selberg/dual-lattice
decomposition exhibits an exact antiperiodic character sum: the integer-distance (m=1) dual shell cancels in
the numerator while the √2-distance (m=2) shell survives, and the ratio's e^(−2π√2) coefficient is
**interval-certified** nonzero, enclosed in (−68, −66). Since e^(−2π√2) cannot occur in an integer-power
series in q = e^(−2π), the proposed closure is impossible. The coincidence is therefore not noise but a
**structured false positive**: exact shell cancellation, together with the cube lying on a *transversal*
(steep) zero-crossing of ε in the anisotropic 1×b×b deformation, makes a non-closed value imitate algebraic
closure to high precision; the fitted coefficient 1−1/√2 is the residue of that crossing, not a law. Sibling
spin structures fail the same closure tests. The example yields a concrete diagnostic for experimental
mathematics: **a single high-precision value at a symmetric point is not evidence for algebraic structure —
the decisive tests are derivation, deformation, and generalization.**

---

## 1. Introduction (the numerical temptation)

High-precision agreement is evidence of nothing without a derivation. The experimental-mathematics record is
full of near-misses that survive many digits and then fail: e^(π√163) matches an integer to twelve places
and is transcendental; certain Borwein integrals equal π/2 until a term far down the series; integer-relation
searches routinely propose relations that dissolve at higher precision (Bailey–Borwein). We add a fully
worked instance from lattice zeta functions — a ratio of cubic-torus Casimir energies that *looks*, to 17
digits, like it lives in ℚ[√2]. It does not. What makes it worth recording is that the false positive is
dismantled by an exact, interval-certified derivation, its illusion is explained by a near-zero geometry, and
the failure is documented as a transferable diagnostic. We let the numerics look seductive, then kill the
pattern with one structural fact and explain why it looked true anyway.

## 2. The object and the coincidence (Proposition 1)

**Proposition 1 (the coincidence is real).** Independent Ewald computation (dps 40):
Z_PPP(−½) = −0.2665962787183934746…, Z_APP(−½) = −0.0111142427950344105…,
R = 0.04168941460272377512…, ε := 24R − 1 = 0.00054595046537060288…. The proposed
(1/24)(1 + Σ c_j q^j), q = e^(−2π), with c₁ = 1−1/√2, c₂ = −(95/96)c₁, c₃ = −1/96, c₄ = (2−3√2)/96,
reproduces R to 17 digits. The phenomenon is real enough to demand explanation. *(Re-verified for this
revision by a second, independent route — the theta-integral reflection representation of §2.1 — giving
R = 0.04168941460272377512… in agreement to 10⁻²³; the script is sealed with this entry.)*

### 2.1 The Half-Period Hinge

Periodic and antiperiodic boundary conditions differ by a half-period shift in one lattice direction. In the
Epstein-zeta representation, the periodic sector is indexed by

```math
\alpha_{PPP}=(0,0,0),
```

with the zero mode excluded from the primed sum, while the singly antiperiodic sector is indexed by

```math
\alpha_{APP}=\left(\frac12,0,0\right),
```

which possesses no zero mode. Thus APP is not merely PPP with one mode removed or one sign changed. It is a
different spectral lattice: one coordinate has been shifted by half a period before the regularized sum is
formed.

Equivalently, in the theta representation on the cubic torus, the boundary-condition change appears as a
single theta-factor replacement:

```math
\Theta_{PPP}(t)=\theta_3(it)^3,
```

```math
\Theta_{APP}(t)=\theta_2(it)\,\theta_3(it)^2.
```

The APP/PPP comparison is localized to the replacement of one θ₃ factor by θ₂. This replacement is the
structural hinge of the calculation.

Geometrically, periodicity says that after one circuit of the torus, the field returns to itself:

```math
\phi(x+L)=\phi(x).
```

Antiperiodicity says that after one circuit, the field returns with opposite sign:

```math
\phi(x+L)=-\phi(x).
```

The half-shift is the spectral expression of this sign reversal. It changes the allowed modes, removes the
ordinary zero-mode channel, and alters the cancellation pattern shell by shell.

The direct-space and dual-space descriptions are the same hinge seen from the two sides of the modular
transform: θ₂(i/t) = √t·θ₄(it), so under t → 1/t the half-shifted factor becomes the alternating-sign
factor, and the antiperiodic character weight (−1)^(k₁) on the transverse dual lattice used in §§3–4 is the
Poisson-resummed image of the α = (½,0,0) shift.

For this reason, the near-1/24 behavior should not be treated as a primary numerological target. The more
precise statement is that the observed ratio is downstream of a half-period spectral obstruction: the APP
lattice differs from PPP by a phase inversion in one direction, and the resulting quotient records the
residual effect of that obstruction after analytic continuation. In the audited formulation, the
near-rational value is therefore interpreted not as evidence for a simple closed-form identity, but as a
structured residue of the half-shifted lattice comparison.

*Numerical check.* The theta representation above was used directly (completed-zeta integrals with the
reflection t → 1/t) to recompute both zeta values at s = −½ at 40-digit working precision; the result agrees
with the audited Ewald values to 10⁻²³, confirming that the hinge representation and the audited numerics
describe the same object.

## 3. The dual-lattice decomposition

Split each Z_α on a periodic axis and Poisson-resum the transverse plane (Chowla–Selberg): each Z_α = a
smooth sector + a dual-lattice Bessel tail. Smooth = n₃=0 slice (a 2D Epstein zeta) + the regularized normal
tower 2·(−2π/3)ζ(−3) = −π/90: N₀ = Z2_AP − π/90 = −0.011211…, D₀ = Z2_PP − π/90 = −0.263731…. The **smooth
ratio N₀/D₀ = 0.0425094… is not 1/24** — 1/24 appears only after the Bessel tails contribute. Expanding ε to
first order about the smooth ratio, the contribution of dual distance d = n₃√m is K_d = 24(N_d D₀ − N₀ D_d)/D₀²
(numerator weighted by the antiperiodic character (−1)^(k₁)):

| d | numer phase / mult | K_d (contribution to ε) | coeff (K_d/e^(−2πd)) |
|---|--------------------|-------------------------|----------------------|
| 1 | **0 / 4 → cancels** | −1.0662e-2 | −5.709 |
| √2 | **−4 / 4 → survives** | −9.29579884827e-3 | −67.1932743663 |
| 2 | 4 / 8 | +6.733e-5 | (2 combos) |
| √5 | 0 / 8 → cancels | −1.670e-6 | — |
| √10 | **−8 / 8 → survives** | −5.961e-8 | — |

**Completeness (exact):** Σ_d N_d = 9.68090551235e-5 = B_APP and Σ_d D_d = −2.86538330129e-3 = B_PPP,
reproducing the cubic Bessel tails to all 12 digits computed. The ledger is the full tail.

The shell audit supports the interpretation that the near-rational behavior is a residue of the half-shifted
APP lattice (§2.1), not an analytic q-series identity.

## 4. The analytic obstruction (Proposition 2 — THEOREM, the murder weapon)

**Theorem.** ε = 24R − 1 contains a nonzero e^(−2π√2) term; hence no integer-power series in q = e^(−2π) with
coefficients in ℚ[√2] can be the exact analytic structure of R.

*Proof (each step exact, computed, or interval-certified).*
1. By §3, Z_α = smooth + dual-lattice Bessel tail, the numerator (APP) weighted by the antiperiodic character
   (−1)^(k₁) on the transverse dual lattice.
2. The character sum over the shell |k|² = m is an **exact integer**: Σ_{k₁²+k₂²=m}(−1)^(k₁) = 0 at m=1
   (vectors (±1,0),(0,±1): signs −,−,+,+) and = −4 at m=2 (all four (±1,±1): −1 each). The integer-distance
   shell is annihilated in the numerator; the √2-distance shell survives.
3. The √2 shell survives in the numerator; the ratio's e^(−2π√2) coefficient,
   24(N_√2 D₀ − N₀ D_√2)/D₀², is **interval-certified to lie in (−68, −66)** (App. A.4), hence ≠ 0. (The
   denominator's √2 shell does not cancel it.) So ε genuinely contains e^(−2π√2).
4. √2 is irrational, so e^(−2π√2) cannot appear in any power series in q = e^(−2π). ∎

The genuine leading e^(−2π) coefficient of ε is ≈ −5.7 (transcendental, π-bearing), not +0.293; and
ε_smooth = 24·N₀/D₀ − 1 = 0.02023 = **37× ε** — ε is a near-cancellation, and 1−1/√2 is the leftover read as
ε/q, not a coefficient. (The decimals of the coefficients are convention-dependent — which shells are
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
Structurally, AAP and AAA carry θ₂²θ₃ and θ₂³ heat kernels — two and three half-period hinges in the sense of
§2.1 — with corrections at the e^(−π/2) scale rather than e^(−2π); the clean appearance is special to APP
(single shift + self-duality), not a family law.

## 7. Why non-closure was inevitable (Elizalde)

Our dual-lattice decomposition (§§3–4) is the **p = 3 case of Elizalde's multidimensional generalized
Chowla–Selberg formula** [E. Elizalde, *Multidimensional Extension of the Generalized Chowla–Selberg
Formula*, Commun. Math. Phys. **198** (1998) 83–95; hep-th/9707257], which analytically continues the
inhomogeneous Epstein zeta ζ_{A,b,q}(s) = Σ_{n∈ℤ^p}(nᵀAn + bᵀn + q)^(−s) over the whole s-plane by an
exponentially convergent expression in Bessel functions, with explicit residua. Our Z_α is the case A = I,
b = 2α, q = |α|², p = 3. The Bessel terms are precisely the irrational-distance dual shells; they are a
generic feature of the continuation, present for general s. They collapse to closed Hurwitz-zeta forms only
at special arguments — in the 2D classification, s = −k, 0, 2 (k = 1,2,3,…) [E. Elizalde, *On the
zeta-function regularization of a two-dimensional series of Epstein–Hurwitz type*, J. Math. Phys. **31**
(1990) 170–174]. The half-integer s = −½ is not such a point; the Bessel/irrational-shell content therefore
survives — exactly as computed and interval-certified here (App. A.4). The non-closure is the established
generic behavior, not an anomaly.

## 8. Diagnostic rule

A single high-precision evaluation at a symmetric point cannot distinguish an algebraic identity from a
structured false positive: a few coefficients from a constrained family fit one number, and a value near a
transversal zero-crossing imitates closure. The decisive tests are **derivation** (the exact, certified
obstruction), **deformation** (transversal vs minimum), and **generalization** (recurrence across siblings).
The right test for such a fit is never more digits at the same point.

## 9. Conclusion

The apparent ℚ[√2] q-series for the APP/PPP cubic-torus Casimir ratio is not an identity. Its mechanism — an
antiperiodic ℤ₂ character annihilating the integer-distance dual shell and preserving the √2-distance shell —
forces an interval-certified-nonzero e^(−2π√2) term into ε (the proof); independently, the ratio is a
steeply-varying function caught on a transversal zero-crossing at the cube (the illusion); and the closure
fails to generalize to the sibling spin structures (the corroboration). The comparison that produces all of
this is localized in a single half-period hinge (§2.1); the near-rational value is its downstream residue. It
is a documented failure mode of single-point numerical induction, not a hidden law in the digits. The origin
of the dimension-specific closeness to 1/24 remains open.

---

## Appendix A — Exactness, certification, tail bound, deformation

**A.1 Exactness of the invariants.** The numerator weight at dual distance d with m = |k|² is the finite
integer character sum Σ_{k₁²+k₂²=m}(−1)^(k₁): m=1 → 0, m=2 → −4, m=5 → 0, m=10 → −8. No numerical
certification needed. The vanishing at m=1 and non-vanishing at m=2 alone force the e^(−2π√2) term into ε.

**A.2 Tail bound.** Per term, |K(n₃,k)| ≤ ((1+1/2π)/π)·(n₃/|k|²)·e^(−2πn₃|k|), prefactor (1+1/2π)/π =
0.36897…. The multiplicity μ(d) = #{(n₃,k): n₃√m = d} is divisor-bounded (μ = 4, 4, 8, 8 for d = 1, √2, 2, √5),
so μ(d) = O(d^(1+ε)) and Σ_{d>D}|K_d| ≤ C·D^(1+ε)·e^(−2πD) — faster than geometric. See A.4 for the certified
numerical bound.

**A.3 Anisotropic Ewald (deformation).** For box (1,b,b), s = −½: Z(−½) = [S₁ + S₂ + B]/(−2√π),
S₁ = Σ′ 2[e^(−πQ)/√π − √π√Q·erfc(√(πQ))], Q = (n₁+a₁)² + b²((n₂+a₂)²+(n₃+a₃)²);
S₂ = b^(−2)π^(−5/2) Σ_{k≠0} χ(k)(1+πQ*)e^(−πQ*)/Q*², Q* = k₁² + (k₂²+k₃²)/b², χ(k) = ∏_{shifted axes}(−1)^(kᵢ);
B = (−1/(2b²) + 2δ)/√π, δ = [α=0]. Validated: at b=1 reproduces Z_PPP, Z_APP to all digits.

**A.4 Interval-arithmetic certification.** Using mpmath's interval type (iv, dps 40), with ζ(−½) and β(−½)
computed to 60 digits and enclosed in 10⁻⁴⁵-width intervals, propagating through the elementary shell
expressions gives a rigorous enclosure of the √2-shell coefficient of ε:
> e^(−2π√2) coefficient ∈ [−67.193274366287611647…, −67.193274366287611647…] ⊂ (−68, −66),

so 0 is excluded: **the irrational-exponent contribution is certified nonzero**, making Prop 2 rigorous. The
rigorous tail majorant (A.2) evaluates to **Σ_{d>4}|K_d| ≤ 8.06×10⁻¹²**, certifying that truncating the
ledger at d = 4 incurs error < 10⁻¹¹ (consistent with the 12-digit completeness match, §3). The only
non-self-contained input is the 60-digit value of ζ(−½), β(−½) (from mpmath); a fully self-contained proof
would replace these with certified enclosures, which is routine.

**A.5 Theta-route re-verification (this revision).** With Θ_PPP = θ₃³ and Θ_APP = θ₂θ₃² (§2.1), the completed
zetas were evaluated by the reflection representation
π^(−s)Γ(s)Z_PPP(s) = ∫₁^∞ (Θ_PPP−1)(t^(s−1)+t^(½−s))dt + 1/(s−3/2) − 1/s and
π^(−s)Γ(s)Z_APP(s) = ∫₁^∞ Θ_APP·t^(s−1)dt + ∫₁^∞ (θ₄θ₃²−1)·t^(½−s)dt + 1/(s−3/2)
(the θ₄ factor arising from θ₂(i/t) = √t·θ₄(it)), at dps 40. Results: Z_PPP(−½) = −0.26659627871839347461…,
Z_APP(−½) = −0.01111424279503441052…, R = 0.04168941460272377512… — agreeing with the audited Ewald values
to 10⁻²³. Script: `verify_R_theta_route.py`, sealed with this entry. Note the absent −1/s term for APP: the
half-shifted lattice has no zero mode, the spectral trace of the hinge.

## References

1. J. Ambjørn, S. Wolfram, *Properties of the vacuum. I.*, Ann. Phys. **147** (1983) 1–32.
2. E. Elizalde, *Multidimensional extension of the generalized Chowla–Selberg formula*, Commun. Math. Phys.
   **198** (1998) 83–95 (arXiv:hep-th/9707257).
3. E. Elizalde, *On the zeta-function regularization of a two-dimensional series of Epstein–Hurwitz type*,
   J. Math. Phys. **31** (1990) 170–174.
4. S. Chowla, A. Selberg, *On Epstein's zeta-function*, J. Reine Angew. Math. **227** (1967) 86–110.
5. D. H. Bailey, J. M. Borwein, *Experimental Mathematics: examples, methods and implications*, Notices AMS
   **52** (2005) 502–514; R. E. Crandall, lattice-sum / Ewald methods.
6. N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. **17** (1950) 197–226;
   B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi **8** (2020) e6.
