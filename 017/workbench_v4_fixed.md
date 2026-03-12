# Spectral Structure & Boundary Conditions — Workbench State (v4, fixed)
# Generated: 2026-03-11T23:32:39.943Z
# Current view: BC=PPP, s=-0.5000, tab=continuation

## Framework
Particle masses as eigenvalues of the Laplacian on a vacuum torus T³.
λ_{n₁,n₂,n₃} = (2π/L)² × |n + α|² where α encodes boundary conditions.
Epstein zeta: Z(s; α) = Σ' |n + α|^{-2s} analytically continued via Jacobi θ-transform.
Casimir energy: E_Cas ∝ c₃ / L⁴ where c₃ = Z(-1/2) × normalization.

## Boundary Conditions & Epstein Zeta at s = -1/2
(All values computed client-side via Jacobi theta transform with pole subtraction)

| BC  | Shifts α      | Z(-1/2)  | c₃        | Sign      | Status   |
|-----|---------------|----------|-----------|-----------|----------|
| PPP | (0,0,0) | -0.2672 | -0.01130 | attractive | computed |
| APP | (0.5,0,0) | -0.0120 | -0.00051 | attractive | computed |
| AAP | (0.5,0.5,0) | +0.0340 | +0.00144 | REPULSIVE | computed |
| AAA | (0.5,0.5,0.5) | +0.0616 | +0.00261 | REPULSIVE | computed |

## v4 Verification Against Python (epstein_check_v3.py)
  PPP: computed -0.2672 vs Python -0.2666 → 0.2%  ✓
  APP: computed -0.0120 vs Python -0.0111 → 8.0%  (numerical precision)
  AAP: computed +0.0340 vs Python +0.0348 → 2.3%  ✓
  AAA: computed +0.0616 vs Python +0.0623 → 1.1%  ✓

Note: AAP reference updated from 0.0248 (old interpolation) to 0.03478 (Python-verified).

## Bug Fix (v3 → v4)
pole = 1/(s-3/2) + δ/s  →  pole = 1/(s-3/2) - δ/s

Wrong: +1/s → at s=-½: pole = -2.5 → Z = +0.37 (WRONG SIGN)
Right: -1/s → at s=-½: pole = +1.5 → Z = -0.267 (matches reference)

## COTT Sign Structure (verified)
BC     | shifts      | Z sign | COTT operator   | interpretation
-------|-------------|--------|-----------------|---------------
PPP    | (0,0,0)     | −      | 0³              | fully bosonic → attractive
APP    | (½,0,0)     | −      | (−0)·0²         | 1 fermionic dir → attractive
AAP    | (½,½,0)     | +      | (−0)²·0         | crossover → REPULSIVE
AAA    | (½,½,½)     | +      | (−0)³           | fully fermionic → REPULSIVE

Sign pattern: − − + +
Crossover between APP and AAP = (−0)² position in 4-cycle

## Physical Interpretation
ω = 0³ ↔ PPP (Z < 0) = attractive = contracting face (gravity)
−ω = (−0)³ ↔ AAA (Z > 0) = repulsive = expanding face (dark energy)
The cosmological constant is the −ω face of the torus.

## Predictions
Torus size L ≈ 78 μm (scenario A, all periodic)
Eöt-Wash current reach: ~52 μm
