# 028 — ALTERNATE DRAFT, as produced by Ash on 2026-08-24

**This is NOT the sealed 028.** The vault's `028/false-positive-cubic-torus.md`
(194 lines) is a different document with the same date and title. Both are
preserved. Which is later is **NOT ESTABLISHED** — see 057 README.

**Difference that matters.** The sealed version carries a caveat this draft lacks,
on exactly the point that later went wrong:

> *"The load-bearing point is the **slope, not the proximity**: a flat minimum
> (slope ≈ 0) near zero would suggest a protected, structural smallness; a steep
> transversal crossing means the smallness is an accident of where we sampled.
> …(The trapdoor explains the imitation mechanism — a near-zero residue divided by
> q mimics a coefficient — not why the crossing falls near the cube, which we do
> not claim is structural.)"*

Both drafts contain the `(1 − q)` slip: `1 − 1/√2 = ε(cube)/e^(−2π)`, where
`ε/q = 0.29235192` and `1 − 1/√2 = 0.29289322`. See 053 §4 and 048 §3.

---

# A 17-digit numerical coincidence in the cubic-torus Casimir ratio, and its dual-lattice resolution

**2026-06-20. Reena (Ash) + Claude/Opus.** Target: *Experimental Mathematics* /
*Mathematics of Computation*. All numerics from verified mpmath runs (dps 30–40).
Remaining before submission: interval-arithmetic certification of the finite head
(the super-geometric tail is bounded explicitly in App. A.2).

## Abstract

For the shifted cubic lattice let Z_α(s) = Σ′_{n∈ℤ³}|n+α|^(−2s), α ∈ {0,½}³,
continued to s = −1/2 — the zeta-regularized Casimir energy of a massless scalar on
the unit 3-torus. The ratio R = Z_APP(−1/2)/Z_PPP(−1/2) = 0.041689414602723775…
agrees with (1/24)(1+ε), ε = Σᵢ₌₁⁴ cᵢqⁱ, q = e^(−2π), cᵢ ∈ ℚ[√2], to seventeen
decimal digits. We show this is not an analytic identity, by **three independent
routes**. (i) *Analytic:* the Chowla–Selberg/dual-lattice decomposition gives ε an
irrational-exponent term in e^(−2π√2), via an antiperiodic ℤ₂ character whose action
on the integer- and √2-distance dual shells is an exact integer phase sum (0 and
−4). (ii) *Deformation:* on the anisotropic torus (1×b×b), ε(b) is an order-one,
steeply varying function (slope ≈ 18) that crosses zero ≈3×10⁻⁵ below the cube — so
ε(cube) is a near-zero-crossing value, and 1−1/√2 = ε(cube)/q ranges over [−816,
+757] across an 8% shape change. (iii) *Non-generalization:* the sibling ratios
K₂ = −24·Z_AAP/Z_PPP = 3.13116…, K₃ = −24·Z_AAA/Z_PPP = 5.60816… are PSLQ-null
against {1, π, √2, G} — the closure is special to APP, not a law of the family.
Non-closure agrees with Elizalde's classification (closed Hurwitz forms only at
s = −k, 0, 2; Bessel content at the half-integer s = −1/2). Two proven structural
identities (a coset/tiling relation; the 2D closed forms) frame the result.

## 6. Proven structural context (classical)

- **Coset/tiling:** Z_PPP + 6Z_APP + 6Z_AAP + 2Z_AAA = 0 at s=−1/2 (m=2
  Hurwitz/Epstein distribution relation; the 8 shifts tile (½ℤ)³). Verified to
  1e-71.  [053 §2: re-verified to 9.9e-25.]
- **2D closed forms (prime-2 Euler factor):** Z2_AA/Z2_PP = 1/√2−1;
  Z2_AP/Z2_PP = −(√2−1)/4. The one-shift ratio is algebraic in 1D (−1/2) and 2D,
  transcendental in 3D — the dimension at which sums of squares stop factoring
  through a number system (ℤ, ℤ[i], then none).
  [**053 §3: this is 039 §1's headline, two months earlier. 039 should not have
  presented these as newly established.**]

## 7.1 Deformation (multi-evaluation-point)

On the anisotropic torus (1×b×b; anisotropic Ewald in App. A.3, validated to
reproduce the cube at b=1):

| b | ε(b) | ε(b)/e^(−2π) |
|------|------------|--------------|
| 0.92 | −1.5235 | −815.8 |
| 1.00 | +0.00054595 | +0.2924 |
| 1.08 | +1.4142 | +757.3 |

ε(b) is order one and monotone across an 8% shape change; ε/e^(−2π) ranges over
[−816, +757]. Locally dε/db ≈ 18.3 and ε crosses zero at b₀ ≈ 0.99997 — the cube
sits ≈3×10⁻⁵ above that zero. So ε(cube) is a steeply-varying function caught near
a zero crossing, and 1−1/√2 = ε(cube)/e^(−2π) = (slope × offset-to-crossing)/e^(−2π)
is a geometric accident of where the crossing lands, with no predictive content.

[**053 §1: every number here is correct. Recomputed in this draft's own convention:
ε(0.92) = −1.523464467, ε(1.00) = 0.0005459505, ε(1.08) = 1.414162348,
dε/db = 18.3259647484, b₀ = 0.999970209325523736 = 1/b*(047) exactly.**]

[**053 §4: the sentence "1−1/√2 = ε(cube)/e^(−2π)" is 0.185% off. The table's
+0.2924 is right — it is ε/q. The prose equates it to 0.29289. This is the earliest
of three instances of the dropped (1−q) factor.**]

## A.3 Anisotropic Ewald

For box (1,b,b), s=−1/2: Z(−1/2) = [S₁ + S₂ + B]/(−2√π),
S₁ = Σ′ 2[e^(−πQ)/√π − √π√Q·erfc(√(πQ))], **Q = (n₁+a₁)² + b²((n₂+a₂)²+(n₃+a₃)²)**;
S₂ = b^(−2)π^(−5/2) Σ_{k≠0} χ(k)(1+πQ*)e^(−πQ*)/Q*², Q* = k₁² + (k₂²+k₃²)/b²,
χ(k) = ∏ over shifted axes (−1)^(kᵢ); B = (−1/(2b²) + 2δ)/√π, δ = [α=0].
Validated: at b=1 reproduces Z_PPP, Z_APP to all digits.

[**THE DECISIVE LINE. The b² on the transverse axes is what makes this draft's b
the reciprocal of 047's. Present in the sealed draft too, at line 167, and never
read.**]

---

*Sections 1–5, 7.2, 7.3, 8, A.1, A.2 and the references are materially the same as
the sealed draft and are not duplicated here. The sealed 028 remains the reference
copy.*
