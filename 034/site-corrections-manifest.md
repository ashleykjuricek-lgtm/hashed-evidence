# Site corrections manifest

### Every live claim that a written correction already contradicts

**2026-08-16. Ash Korth + Claude (Opus 5), with GPT ("Greg") and the Figma agent.**
Status: **work order.** Not a finding. Each row is a thing currently readable by a
visitor, paired with the sealed document that already refutes it.

Ordered by exposure: what a stranger hits first, and how wrong it is.

---

## The list

| # | live claim | where | correction exists in | state |
|---|---|---|---|---|
| 1 | `0^ω = −1` — "the structure equation" | **homepage**, `/origins`; `0^ω` ×4 in the index bundle | `cott-slot-closure.md` §246 | **argument no longer typechecks**; no replacement proposed |
| 2 | `c₁ = 1 PROVEN`, forced by Poincaré isometry | `/#/spectral` (served bundle), `/correction` | 026–028; real-math ledger line 76; 032 | genuine e^(−2π) coefficient is **−5.709** |
| 3 | ε = q(1−1/√2)(1−q) as an identity | `/correction`, badged **7/7 PASSED** | 028 Prop 2 (interval-certified) | dead since 2026-06-20 |
| 4 | R = `0.041689414162238` | 24 files in zip 12 | 032/`canonical_constants.json` | stale at the 10th figure; warned by the July note, item 10 |
| 5 | Chowla–Selberg PSLQ "hit" Γ(1/4)⁴/4008 | `ChowlaSelbergPage` (new) | this session | fits a **3.4% quadrature error**, not R |
| 6 | §7.6 conj: Σ_APP = 0 when D² ≡ 1,2 mod 4 | paper draft | 032 parity law | **falsified by its own table** (D²=2 → −4) |
| 7 | Figure 1 Panel 3 (shell diagram) | figure / new lattice image | **029 §3**, a complete redraw spec | spec never followed; no phase sums drawn |
| 8 | Oscillator page's four pillars | `/oscillator` — **not yet live** | this session | no K_ij, no learning law, TComplex vs Niven |

## Supporting defects

| | |
|---|---|
| **48 rooms missing** | live site serves 29 of 75 routes; deploy predates 2026-05-04 |
| **`llms.txt` / `llms-full.txt`** | built, sealed in 033, still **404** on the live site |
| **supersession banners** | applied to 10 files in July; **2 survived** the next Figma export |
| **no build gate** | 034/`constants_gate.sh` exists and has nowhere to run |

---

## Per-item correction, stated once

**1 — `0^ω = −1`.** The bijection argument assumed a four-element carrier
`{0,1,−1,ω}`. With `−ω ≠ 0` the carrier is six or infinite, and the slot document
says the argument *"does not merely weaken — it no longer typechecks."* Downgrade
from *structure equation* to **conjecture pending a replacement criterion**. This
also invalidates the quarter-turn phase assignment and therefore the torus
winding computation `det[[1,1],[1,−1]] = 2`, which inherits the same assumption.

**2 — `c₁ = 1`.** Lead with the number, not the argument: the genuine e^(−2π)
coefficient of ε is **−5.709**, wrong sign and ~20× wrong magnitude versus 1. The
mirror argument fails independently because the Mellin integral samples the whole
`it` ray, not only the fixed point `i`. Replace with the mechanism, do not merely
delete: half-shift α=(½,0,0) Poisson-dualises to the character (−1)^(k₁); the
character annihilates **every odd** transverse dual shell exactly, by the
orientation-reversing swap (k₁,k₂)→(k₂,k₁), which exists only on the cube.

**3 — the closed form.** Keep the page as a dated record; add a supersession
banner. Its own q² table and η-product table already argue against it — both get
*worse* when extended. Reframe them as evidence, not as loose ends.

**4 — the stale R.** Stop fixing occurrences. Import from
`canonical_constants.json` and gate the literal at build time.

**5 — Chowla–Selberg.** Sections 01–02 are **correct and worth keeping** —
independently verified: `Z_PPP(2) = 16.5323159598` from the functional equation
against `16.5323159181` by direct summation. The identity R = Z*_APP(2)/Z_PPP(2)
holds. Recompute §03 at high precision; record Γ(1/4)⁴/4008 as a **negative
control**; the honest §04 result is that no single-term CM closed form matches R
(best is 6.0×10⁻⁵, which the page's own criterion calls noise). Delete step 5 of
§06 — it targets the dead formula.

**6 — §7.6.** Replace the conjecture with the theorem: Σ_APP(m) = 0 ⟺ m odd.

**7 — Figure 1.** Follow 029 §3 verbatim, plus one addition: draw the swap
(k₁,k₂)→(k₂,k₁) as an arrow between paired points, so the cancellation reads as a
reflection rather than an arithmetic accident.

**8 — oscillator.** Not live. Fix before it ships: the demo is mean-field
Kuramoto (K_ij = K/N), which Ott–Antonsen collapses to two macroscopic degrees of
freedom regardless of N; the σ demo is a leaky integrator relaxing to a constant;
and exact rational phase is impossible under this equation by Niven's theorem.

---

## Sequencing

1. **Do not rebuild and upload** until items 1–4 are corrected in the source of
   truth. Zip 12 still carries 66 findings; a deploy takes the dead claim from
   2 live pages to ~20.
2. Corrections must land where the build comes from. Local edits to an exported
   tree evaporate — that is documented, not hypothetical.
3. Then install `constants_gate.sh` so item 4 cannot recur.
4. Then deploy, and the 48 missing rooms arrive with the corrections already in
   them rather than needing a second pass.

## The blocker

Every item above is written, sealed, and unapplied. The single unresolved
decision is whether Figma Make stays authoritative or a local tree becomes the
source of truth. Recorded, not settled, in `032/positions-on-the-source-of-truth.md`.
