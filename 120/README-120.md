# 120 — The mirror is an identity, and the slope is the normal one

**2026-10-13.** Drafted by Claude (Opus seat) in the Figma Make session, at Ash's
word ("sure look into all of it"). Not yet sealed. Nothing earlier is edited.

## Part 1 — 098's "derivable, not yet derived": derived

Λ_a(s) = π^(−s) Γ(s) Z_a(s), with Z_a(s) = Σ |n+a|^(−2s) over ℤ³. For PPP, a = 0
and n = 0 is dropped. For APP, a = (½,0,0) and nothing is dropped.

Poisson summation gives θ_a(t) = t^(−3/2) Σ_k (−1)^(k₁) e^(−π|k|²/t). The zero-mode
constant terms are:

| | direct side | dual side | poles |
|---|---|---|---|
| PPP | n = 0 | k = 0 | −1/s, +1/(s − 3/2) |
| shift (APP) | none, because ½ ∉ ℤ | k = 0 | +1/(s − 3/2) |
| character | k = 0 | none | −1/s′ |

Split the Mellin integral at t = 1. For the shift this gives
Λ_shift(s) = 1/(s−3/2) + ∫₁^∞[t^(s−1)θ_a + t^(1/2−s)θ̂*_a]dt. For the character at
s′ = 3/2 − s, the same two integrals appear with their roles swapped, and the pole
term is −1/s′ = 1/(s − 3/2). The pole terms are identical, so

    Λ_shift(s) = Λ_char(3/2 − s),   Λ_PPP(s) = Λ_PPP(3/2 − s)

as meromorphic identities. Neither s = −½ nor s′ = 2 is a pole. The prefactors are
π^(1/2)Γ(−½) = −2π and π^(−2)Γ(2) = π^(−2), so both sectors get the same factor:

    Z(−½) = −Z̃(2) / (2π³)   ⇒   R = Σ′(−1)^(k₁)|k|^(−4) / Σ′|k|^(−4).   ∎

The boundary terms live only inside the integral representation. They cancel in
the identity and never reach the evaluation point. 098's 55-digit agreement is this
theorem. **Grade: PROVED** (standard Epstein/Poisson).

Numerical check (`mirror-prefactor-check.py`): Ewald at s = −½ against a direct sum
at s = 2. PPP agrees to 3×10⁻⁶ and APP to 2×10⁻⁵, which is the accuracy of the
direct sum. The Ewald R = 0.04168941460272377512007918954, matching c2-highprec.py
to 30 digits.

## Part 2 — The lopsidedness (038/097/098)

On the (1,b,b) family, the dual lattice has |k|² = k₁² + b²(k₂²+k₃²), and the
volume factor b² cancels in R. Differentiating in x = ln b at the cube, and using
cubic symmetry for the unsigned sum:

    d ln R/dx = 4U/S_χ − 4/3,   U = Σ′(−1)^(k₁) k₁² |k|^(−6),   S_χ = Σ′(−1)^(k₁)|k|^(−4)

Direct sums (`lopsided-slope.py`, |k| ≤ 120):

| quantity | value | cancellation |
|---|---|---|
| S₀ | 16.5323 | none |
| S_χ | 0.6892 | heavy: 1/24 of S₀ |
| U | −2.9262 | light: the k₁ = ±1 shells dominate |

That gives d(24R)/dx = **−18.3260**, matching the sealed −18.3259647, sign included.

*Scar, kept:* the first draft of this entry wrote the dual as k₁² + (k₂²+k₃²)/b².
That is the eigenvalue lattice, not its dual, and it flipped the sign (+18.326).
The Ewald finite-difference check in `battery.py` caught it before sealing.

**Reading.** Written out, d(24R)/dx = 96 U/S₀ − 24R·(4/3) ≈ −16.99 − 1.33. U/S₀ ≈ −0.18
is an ordinary, uncancelled size, so the slope is the natural size. **The
lopsidedness is not a big slope. It is an unnaturally small gap.** The signed sum
cancels down to almost exactly S₀/24. Its first derivative doesn't, because the
weight k₁² breaks the cancellation. So the lopsidedness is the same 1/24 mystery
seen from a different angle, not a second mystery.
**Grade: OBSERVED** (formula derived, numbers ~5 digits).

## Part 3 — COTT bridge (sibarum/cott)

See `cott-bridge.md`.

## Files

- `mirror-prefactor-check.py` / `.out`: needs mpmath
- `lopsided-slope.py` / `.out`: stdlib only
- `battery.py` / `.out`: independent checks of every claim above (needs mpmath); see `CHECKS.md`

## Correction beside (2026-10-19)

The Part 2 "scar" is a convention issue, not an error. k₁² + (k₂²+k₃²)/b² *is* the
dual of the direct box (1, b, b); Laplacian eigenvalues and the dual lattice are the same
thing. The −18.3260 here, which matches 098, holds when b scales the dual lattice,
i.e. the box is (1, 1/b, 1/b). For the direct box (1, b, b) the slope is +18.326. Whoever
seals this should check which convention 098 states.
