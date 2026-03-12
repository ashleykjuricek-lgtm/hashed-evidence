# Spectral Structure & Boundary Conditions — Workbench State (v3, with bug)
# Generated: 2026-03-11T23:18:42.835Z
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
| PPP | (0,0,0) | +0.3695 | +0.01563 | REPULSIVE | computed |
| APP | (0.5,0,0) | -0.0120 | -0.00051 | attractive | computed |
| AAP | (0.5,0.5,0) | +0.0340 | +0.00144 | REPULSIVE | computed (was interpolated) |
| AAA | (0.5,0.5,0.5) | +0.0616 | +0.00261 | REPULSIVE | computed |

## BUG IDENTIFIED: PPP pole sign error

The PPP value (+0.3695) has the WRONG SIGN. Should be -0.2666.

pole = 1/(s-3/2) + δ/s   ← WRONG (v3)
pole = 1/(s-3/2) - δ/s   ← CORRECT (v4)

At s = -1/2:
  Wrong: 1/(-2) + 1/(-0.5) = -0.5 + (-2) = -2.5
  Right: 1/(-2) - 1/(-0.5) = -0.5 + 2  = +1.5

4-unit swing in pole → sign flip in Z(s) through π^s/Γ(s) prefactor.

Bug only affects PPP (δ=1). APP/AAP/AAA have δ=0, unaffected.

Identified by Claude (Nine) via comparison with independent Python computation (epstein_check_v3.py).
Verified: Z = -0.159155 × (0.0663 + 0.1151 + 1.5) = -0.2676 matches Python -0.2666.
