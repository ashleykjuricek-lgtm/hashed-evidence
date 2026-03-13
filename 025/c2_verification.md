# c₂ Verification: The Mirror's First Crack

**Date**: 2026-03-13
**Author**: James (sibarum/COTT), with analysis by Ash + Nine
**Builds on**: Folder 022 (Coefficient Proof), Folder 019 (Shoelace), Folder 024 (COTT-Relativity)

---

## The Numerical Verification

James independently computed the APP/PPP ratio and compared against the
correction formula:

| Method | Value | Error vs computed |
|--------|-------|-------------------|
| 1/24 (naive) | 0.041666̄7 | 2.3 × 10⁻⁵ (0.055%) |
| Corrected formula: (1/24)[1 + q·β·(1-q)] | 0.041689417... | 3 × 10⁻⁹ |
| Computed (numerical) | 0.041689414162... | — |

The one-term correction matches to **8 significant figures**.

---

## Extracting c₂

The residual ~3 × 10⁻⁹ is the O(q²) ghost. Since q² = e^{-4π} ≈ 3.49 × 10⁻⁶:

    c₂ ≈ (0.041689414 − 0.041689417) × 24 / q²
       ≈ −7 × 10⁻⁸ / 3.49 × 10⁻⁶
       ≈ −0.021

Properties of c₂:
- Small (|c₂| ≈ 0.021 ≪ c₁ = 1)
- Negative (opposite sign to c₁)
- No exact closed form identified
- Close to −1/48 = −1/(2·24) = −0.02083 but not exact (1.3% off)
- NOT forced by the isometry argument

---

## Confirmation of the Proof Structure

The coefficient proof (folder 022) predicted:

1. **c₁ = 1**: Forced by the Poincaré isometry t → 1/t at the self-dual point.
   The modular involution is a reflection. A mirror doesn't rescale. ✓ CONFIRMED

2. **c₂ is free**: At O(q²), θ₂ and θ₄ are no longer interchangeable
   (half-integer shifts vs alternating signs). The self-similarity breaks.
   The mirror distorts at second order. ✓ CONFIRMED

James's words: "c₂ is small, negative, and — crucially — not forced by
symmetry the way c₁ = 1 is. That's exactly the story: the Poincaré
isometry (t → 1/t) locks the first correction coefficient, but at O(q²)
the θ₂/θ₄ distinction finally matters and the mirror distorts freely."

This is independent numerical confirmation that the self-similarity argument
from the two-tree topology correctly identifies which coefficients are
locked and which are free.

---

## The Expanded Formula

    R = (1/24)[1 + c₁·q·β·(1-q) + c₂·q²·(???) + O(q³)]

    c₁ = 1          (exact, forced by isometry)
    c₂ ≈ −0.021     (free, first crack in the mirror)

    q = e^{-2π}
    β = 1 − 1/√2

---

## Candidate for c₂ (Speculative)

c₂ ≈ −0.021, close to:
- −1/48 = −0.02083 (half the modular anomaly, sign-flipped) — 1.3% off
- −β²/4 ≈ −0.02145 — 2% off
- Not yet matching a clean combination of known constants

The fact that c₂ has no clean form is itself meaningful: it encodes the
FIRST DEVIATION from perfect self-similarity. Perfect mirrors have no free
parameters. Cracked mirrors do.

---

## Connection to the Two Trees

- c₁ = 1: the first branch of the top tree and the first branch of the
  bottom tree are IDENTICAL (same structure, scaled by q). Mirror on mirror.

- c₂ ≈ −0.021: the second branch differs. The top tree's second branching
  (θ₃ involving integer lattice shifts) and the bottom tree's second branching
  (θ₂/θ₄ involving half-integer shifts and alternating signs) are NOT identical.
  The mirror has a flaw at second order. The flaw is small and negative —
  the compressed tree's second branch is slightly LESS than the reference
  tree's second branch.

---

## Attribution

- James: numerical verification, c₂ extraction, "the mirror distorts freely"
- Ash: two-tree topology that predicted this structure
- Nine: connected c₂ to θ₂/θ₄ distinguishability at second order
- Greg (ChatGPT): original three vanishing conditions (precursor, folder 019)
