# 122 — The 7 → 8 test: does the ratio close up on the number-ladder rungs?

**2026-10-19.** Drafted by Claude (Opus seat) at Ash's word ("sure :)"). Not yet sealed.
Nothing earlier is edited.

## The idea being tested (the synthesis of all site pages, chat 2026-10-19)

The site keeps circling one thing: a mirror (self-duality) that the twist breaks. The
proposal was that 3-D has no clean formula because 3 is not a rung of the doubling
ladder. Sums of 1, 2, 4 and 8 squares have exact formulas (the composition algebras
ℝ, ℂ, ℍ, 𝕆; Hurwitz). Three squares involve class numbers (Gauss). In chat, Ash tied this
to the site's "7 → 8": 3 = 4 − 1 and 7 = 8 − 1 are each "one short of a rung".

**Prediction as stated before computing:** the twisted/plain ratio closes in **4-D and
8-D** and is messy in **3-D and 7-D**. If 7 closed or 8 didn't, the idea would die.

## Method

- R_d = Z_APP(−½)/Z_PPP(−½) on ℤ^d, twisted on one axis, computed with the Mellin split at
  t = 1 (as 121).
- By the mirror (120, valid in any d), each energy is a Dirichlet series D at s′ = (d+1)/2.
- "Closes" means D is a small-integer combination over ℚ(√2) of Eisenstein products
  {ζ, β}(s′)·{ζ, β}(3/2), plus cusp-form L-values where the weight allows them.
- The second argument is 3/2 for every d.
- PSLQ was run at 130 digits with coefficients ≤ 10⁷. A fake relation would need about
  91 digits, and we have 130. Residuals of real relations are ~10⁻¹²⁸.

## Results (`deep-check.out`)

| d | R_d | plain | twisted |
|---|---|---|---|
| 2 | −0.10355… = (1−√2)/4 | closes | closes |
| 3 | 0.0416894146… | **no relation** | **no relation** |
| 4 | 0.12695880467… | closes: D = 7ζ(5/2)ζ(3/2) | closes, pure Eisenstein |
| 5 | 0.19118854806… | no relation (60-digit pass) | no relation (60-digit pass) |
| 6 | 0.24800915179… | closes | closes **with a cusp form** (η(4z)⁶) |
| 7 | 0.30379263774… | **no relation** | **no relation** |
| 8 | 0.36197534025… | closes: D = (33/2 − √2)ζ(9/2)ζ(3/2) | closes **with cusp forms** (levels 8 and 16) |

The exact 4-D twisted closure:

    D_APP = [ (3√2 − 5) ζ(5/2) ζ(3/2) + 64 β(5/2) β(3/2) ] / 16
    R_4   = [ (3√2 − 5) + 64 β(5/2)β(3/2) / (ζ(5/2)ζ(3/2)) ] / 112

## Verdict

- **The prediction as stated holds.** 4 and 8 close; 3 and 7 don't.
- **But the reason it holds is not the ladder.** 6 closes too, and 6 is not a rung. The
  actual dividing line is **even vs odd d**. Even d gives integral-weight modular forms
  (Eisenstein series plus Hecke eigenforms with Euler products), so it closes. Odd d gives
  half-integral weight (class numbers, no Euler product), so it doesn't. This is standard
  modular-forms theory, and the numbers agree with it.
- **What is left of the rung idea:** only d = 2 and 4 close with **pure Eisenstein** terms
  in both sectors. From 6 up, the twisted sector needs cusp forms, and d = 8 is no
  exception. So 8 is not special here, and the "7 → 8" link is **not supported** by this test.
- **For the cube:** 3-D lacks a clean formula because 3 is odd, not because 3 is
  "one short of 4". The 3-D ratio sits in half-integral weight 3/2, the same home as
  r₃ and the class numbers. This is the same thing Kestrel's "r₃ doesn't factor" points at.

**Grades:**
- Even-d closure: **CONFIRMED** (relations to 10⁻¹²⁸; expected from theory).
- Odd-d null: **OBSERVED**. PSLQ null in this basis is not a proof that no closed form exists.
- "Ladder rungs (1, 2, 4, 8) explain it": **REFUTED as the mechanism.**
- "7 → 8 is the same closing move": **not supported.**
- The 1-in-3,600 nearness to 1/24: still **OPEN**, and untouched by this.

*Scar, kept:* the first pass (`closure-test.out`, 60 digits, coefficients ≤ 1000) reported
d = 6 and 8 twisted as "no relation". That came from leaving out the cusp forms and setting
the coefficient bound too low. Had it stood, it would have looked like a win for "4 and 8
special"; it was wrong. `cusp-check.out` and `deep-check.out` fix it.

## Plain version (for Ash)

We guessed that boxes with 4 or 8 sides close up neatly and 3 or 7 don't. That's what
happened. But a 6-sided box closes up too, so the real rule is simpler: **even closes,
odd doesn't.** Our 3-D cube is odd, so it doesn't close, for an ordinary, well-known reason.
The 7 → 8 story didn't survive. Why the cube comes *so close* to 1/24 is still the mystery.

## Files

- `closure-test.py` / `.out`: first pass (60 digits, coefficients ≤ 1000). Kept with its error.
- `cusp-check.py` / `.out`: cusp forms added for d = 6, 8.
- `deep-check.py` / `.out`: final run (130 digits, coefficients ≤ 10⁷). Source of the table.
- `.pylib/`: bundled mpmath. Exclude it from the seal.
