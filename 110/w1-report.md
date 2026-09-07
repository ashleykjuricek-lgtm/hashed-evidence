# W1 — the arrow attempt: Burgers name DENIED, coboundary structure AWARDED

**Registered:** round-4 memo, work item W1: construct the explicit loop, transport
law, and target group whose composed transport yields the surviving residual ε₀ —
earn or deny the Burgers name; either outcome filed.
**Status:** RESOLVED 2026-09-06. The Burgers name is **denied**, for a provable
reason; what the construction actually yields is sharper — the first fully worked
physics instance of the paper's coboundary test (v2 §12), drawn from the sealed
corpus, with an 8-digit closing identity.
**Receipts:** `w1_arrow_check.py` (this folder), run 2026-09-06, OVERALL PASS.

---

## 1. The construction, as registered

- **Cover space:** the shape line x = ln b of the 1×b×b torus family (charts
  distinguished).
- **Quotient:** the fold x ~ −x — the sealed b ↔ 1/b chart swap, which is the
  S-transform (053), realized exactly by the shift↔character functional equation
  (sealed 097: the involution acts on triples (shift, s, b) ↔ (character, 3/2−s,
  1/b), never at fixed s).
- **Transport law:** carry the energy comparison by that involution. It is an exact
  identity, verified in the sealed record to 25–32 digits.
- **Target group:** displacements of the shape dial, (ℝ, +) in x — abelian, so any
  residual would be basepoint-free.

## 2. Why the Burgers name fails — provably, not rhetorically

A Burgers vector is the residual of **composing** exact local transports around a
loop: the walk itself fails to close. Here the candidate transport is an involution
satisfying σ² = identity **exactly** — 097 is an identity, not an approximation.
Every loop built from it closes perfectly; the holonomy of this connection is
trivial; there is no composition residual for ε₀ to be. (The sealed 55-digit
agreement of the two R-routes — 097-mirror partners per 098 — is precisely this
trivial holonomy, functioning as the two-method seal.)

What fails to close is not the loop. It is the **section**: the energy comparison
ε(x) is not invariant under the fold. That failure is a different mathematical
object, and the paper already has its name.

## 3. What the corpus actually holds: the coboundary test, instantiated

Decompose ε under the fold, ε = even + odd. Then, with fresh receipts:

- **The odd part is the coboundary** — the removable discrepancy. Its slope is
  s_odd = −18.325965 (measured today; the sealed ±18.3 of 054/096), and 097 sealed
  its status: a **chart artifact**, removable by re-description. In §12's language:
  r ↦ r + δa kills it; [r_odd] = 0.
- **ε₀ is the class** — the part no recalibration removes: the even residue at the
  fixed point, ε₀ = 5.4595046537×10⁻⁴, chart-invariant, the load-bearing miss.
- **The "arrow" is the class's chart-shadow.** In any one chart the zero of ε sits
  displaced from the mirror. Measured fresh today: exactly **one** zero in this
  chart, at

      x* = 2.9791118229×10⁻⁵    (b* = 1.0000297916)

  and the displacement obeys the **arrow identity** to all eight displayed digits:

      x* · |s_odd| / ε₀ = 1.00000095 = 1 + c₂·x*/|s_odd|   (c₂ = 0.58260865, sealed 096)

  Magnitude: the invariant class over the chart slope, with the measured well
  supplying the correction. Direction: **chart-dependent** — and this resolves a
  sealed loose end: 054 recorded *two* zeros, b* = 1.0000298 and b₀ = 0.99997.
  Today's computation finds only one zero per chart and 1/b* = 0.9999702093 —
  **b₀ = 1/b\* to every recorded digit.** The two sealed zeros are one zero seen
  from the two charts: the arrow flips sign with the chart, exactly as a
  chart-covariant shadow must and exactly as a Burgers vector must not.

## 4. Receipts (two implementations, one verdict)

Fresh float64 Ewald implementation (closed-form incomplete-gamma tails, no
quadrature), cross-checked against the sealed mpmath instrument (v_landscape.py,
dps 25) run today in parallel:

- eps(cube): fast 5.459504653862e-4 vs instrument 5.459504653706e-4 vs sealed
  5.4595046537e-4 — relative agreement 3×10⁻¹¹.
- Three sealed CSV rows reproduced to ~10⁻¹⁴.
- No sign change anywhere in the left half of this chart (the b₀ zero is not here —
  it lives in the mirror chart, as §3 says).
- **Independent-implementation confirmation of the measured well (096):** the even
  curvature recovered today = 0.582608, vs registry DRAIN_V_C2 = 0.58260865 —
  6-digit agreement from different code at different precision. (Honesty note: same
  Ewald mathematics, different implementation — a code-independence check, not a
  method-independence one.)

## 5. Disposition

- W1 is **closed as a denial that strengthens the paper**: item 7 of the round-4
  memo does not upgrade to "Burgers instance" — it upgrades to **"coboundary-test
  instance"**: the paper's central §12 distinction (removable discrepancy vs
  invariant class) now has a fully worked, sealed-corpus, 8-digit physics example:
  odd slope = the coboundary, ε₀ = the class, x* = the chart-shadow, b₀·b* = 1 the
  covariance witness.
- v2 edit implied (small): §16 item 15's W1 entry gets this resolution; the §12
  coboundary test gains the worked example.
- The 054 loose end (two zeros, one object) deserves a one-line note when next
  sealing: today's receipts identify them as chart partners.

**Attribution:** construction target and denial criterion — the round-4 memo
(Greg's demand, accepted); the fold/chart structure and its exactness — sealed
053/097/098 and 054's recorded zeros (Ash's corpus); fresh implementation,
receipts, the denial proof, and the coboundary identification — Claude (Fable
seat), 2026-09-06, at Ash's word ("the arrow attempt — W1").
