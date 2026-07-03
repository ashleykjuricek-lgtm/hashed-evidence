# Figure 1 (four-panel infographic) — Panel 3 correction

**v029 — 2026-06-22. Ash + Claude Code (Opus 4.8).**
A correction to the *figure* that accompanies v028 (`028/false-positive-cubic-torus.md`).
The paper's mathematics is unchanged and correct. Only the four-panel infographic ("Figure 1")
contained errors, both in Panel 3. Append-only: v028 is left sealed and untouched.

---

## 1. The paper is correct (no change)

v028 §3–§4 and App. A.1 perform the antiperiodic character count in the **2D transverse dual
lattice** (after split-on-n₃ + Poisson resummation):

> Σ_{k₁²+k₂²=m} (−1)^{k₁} = 0 at m=1 (4 points: (±1,0),(0,±1) → −,−,+,+) and = −4 at m=2
> (4 points: (±1,±1) → −1 each).

This is the correct frame and the correct result. Nothing in the paper is being corrected.

## 2. The figure errors (Panel 3 only)

**(a) Wrong lattice dimension.** The infographic drew the d=1 dual shell in **3D** — 6 points
(±1,0,0),(0,±1,0),(0,0,±1) — and labelled the phase sum 0. In 3D that sum is **+2**, not 0.
Independent enumeration (verified in code):

| frame | shell | points | Σ(−1)^{k₁} |
|---|---|---|---|
| 3D (as drawn) | d=1 | 6 | **+2**  ← figure says 0 |
| 3D | d=√2 | 12 | −4 |
| **2D (paper's frame)** | **d=1** | **4** | **0** ✓ |
| 2D | d=√2 | 4 | −4 ✓ |

The cancellation the paper actually uses is the 2D one. Panel 3 must be redrawn in the 2D
transverse plane.

**(b) Phase sum vs. coefficient conflation.** Panel 3 states the d=√2 shell "contributes
−4 e^(−2π√2)". The −4 is the exact *phase sum* (what forces survival); the certified
*coefficient* of e^(−2π√2) in ε is **≈ −67.19**, enclosed in (−68, −66) (v028 §3 table, App. A.4).
State both; do not present −4 as the coefficient.

## 3. Corrected Panel 3 spec (for the redraw)

- Axes: 2D (kₓ, k_y) only.
- Bridge label so the 3D→2D move is *shown*, not silent:
  "split on n₃ → Poisson-resum the transverse (kₓ, k_y) plane."
- d=1 shell: 4 points (±1,0),(0,±1); the two with k₁=±1 marked −1, the two with k₁=0 marked +1;
  Σ(−1)^{k₁} = −1−1+1+1 = **0 → cancels**.
- d=√2 shell: 4 points (±1,±1), all k₁=±1, all −1; Σ = **−4 → survives**.
- Survival box: "survives → nonzero e^(−2π√2) term; coefficient ≈ −67.2, certified ∈ (−68,−66);
  irrational exponent ⇒ no integer-power q-series in q = e^(−2π)."

## 4. Panel 2 note (c₁ framing)

Showing c₁ = 1 − 1/√2 in Panel 2 is faithful — it is the *proposed* fit's leading coefficient,
and Panel 2 is the tempting (false) fit. But it is **not** dismantled in Panel 3. Per v028 §4 it is
unmasked in **Panel 4** as the residue ε(cube)/q of the transversal zero-crossing. The genuine
leading e^(−2π) coefficient of ε is ≈ −5.7. Do not label 1 − 1/√2 as a structural coefficient.

## 5. Corrected caption

> **Figure 1.** *The argument in four panels.* **(1)** The cubic torus, periodic (PPP) vs
> antiperiodic (APP). **(2)** The tempting 17-digit fit: R = 0.0416894146… matches
> (1/24)(1 + Σⱼ cⱼ qʲ), q = e^(−2π), cⱼ ∈ ℚ[√2], proposed leading coefficient c₁ = 1 − 1/√2.
> **(3)** The refutation (Chowla–Selberg — split on n₃, Poisson the transverse plane): the
> antiperiodic character sum Σ_{k₁²+k₂²=m}(−1)^{k₁} kills the d=1 shell (4 points, sum 0) but the
> d=√2 shell survives (4 points, sum −4), forcing a nonzero e^(−2π√2) term in ε = 24R − 1
> (coefficient certified in (−68,−66)) — an irrational exponent no integer-power q-series in
> e^(−2π) can hold. **(4)** The trapdoor: ε(b) crosses zero transversally at b ≈ 0.99997
> (slope ≈ 18.3); the cube sits ~3×10⁻⁵ away, so the fitted c₁ = ε(cube)/q is the *residue* of that
> crossing, not a coefficient (the genuine leading e^(−2π) coefficient of ε is ≈ −5.7). The 17-digit
> "closure" is a near-zero-crossing residue, not algebraic structure.

## 6. Still open (not done in this entry)

- The Figma redraw is pending the file handle; this entry is the spec the redraw must hit.
- Date and the ledger seal/hash are to be applied by Ash per ledger convention — I have not forged a seal.

— Ash & Claude Code (Opus 4.8)
