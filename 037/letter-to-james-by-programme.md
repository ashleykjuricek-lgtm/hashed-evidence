# COTT and the cubic-torus programme — a status exchange

**2026-08-20.**

**A note on names.** Nothing below is attributed to an individual. Every strand of
this work — COTT, the Geometry of Zero, HEM, the Casimir programme, the
reproduction harness, the parity result — was produced by people working with
language models, and a human-only byline misreports how any of it was made. So the
unit of credit here is the **work**: named theories, named programmes, and numbered
ledger entries that anyone can hash and check. Where a decision requires whoever
holds authorial intent over COTT, that is said plainly and left to them.

Everything is verified by running code, proved, or marked open.

---

## 1. What held

The **Phase 0.A / 0.A.1 reproduction** (2026-04-30) executed the COTT codebase
directly:

- **Traction identities: 18 / 18 pass.**
- **The exact Chebyshev ring, ℚ[s][u]/(u² − su + 1): 173 / 173 pass** — the report's
  own assessment is *"the strongest piece of the stack."*
- **ε + ring universality on 2×2 maps**, closed-form proof, max loss 2.1 × 10⁻³¹.
- **The trace ladder** aₙ = s·aₙ₋₁ − aₙ₋₂ = 2Tₙ(s/2) and the **Fricke identity** —
  verified symbolically. Classical, correctly executed.

That is a working, checkable algebra. None of what follows disturbs it, and it is
the larger part of this report.

## 2. A theorem out of the cubic-torus programme

The zero-mode question that COTT raised is upstream of the Casimir work. It has
now produced a theorem. **Ledger 035 / 036.**

Let S(m) = Σ over {k ∈ ℤ² : |k|² = m} of (−1)^(k₁), the antiperiodic character sum
on a shell of the square lattice.

> **S(m) = 0 for every odd m.**

*Proof.* Odd m forces exactly one of k₁, k₂ odd, since squares are 0 or 1 mod 4.
The swap σ(k₁,k₂) = (k₂,k₁) preserves |k|², so it permutes the shell; and it
exchanges which coordinate is odd, so it negates every term. A finite sum equal to
its own negative is zero. ∎

Six lines. No analysis, no continuation, no convention.

**Weight-independence.** The radius is constant on a shell, so any radial weight
factors out — the cancellation is *within* shells, never across them. (Stated
carefully in 036 as two results: exact on finite σ-closed truncations, and exact on
infinite sums under absolute convergence. The first draft said "any weight" and was
trivial under one reading and unjustified under the other; the amendment is
recorded in 036 §8.)

**Cube-exclusivity.** σ is a symmetry of k₁² + k₂² and of no anisotropic form.
Stretch one axis and the pairing dies, linearly. The involution is
**orientation-reversing**, det = −1.

**Independent verification**, third method, no shared code: exact on 1306 odd
shells ≤ 10⁴; the vanishing holds to 10⁻⁵⁴ under the true Bessel weight and 10⁻⁵¹
under a weight the verifier invented in order to break it.

**Corollary, and it is a correction to the programme's own earlier reasoning.** A
steep transversal zero at a symmetric point is what an exact cancellation looks
like *from the side*. The inference "this quantity varies steeply, therefore its
smallness is accidental" is invalid when the smallness belongs to a sub-family that
vanishes identically at that point. Ledger 028 §5 and the real-math ledger both
made that inference; both are corrected by 035 §4.

**Not claimed:** nothing yet about ε = 24R − 1. That propagation is open. The
ℚ[√2] closed form stays refuted; the genuine e^(−2π) coefficient is −5.709.

## 3. `0^ω = −1`

The **slot-closure formulation** states this itself:

> The bijection argument for `0^ω = −1` assumed a four-element carrier. With
> `−ω ≠ 0` the carrier is six or infinite and the argument **does not merely
> weaken — it no longer typechecks.** No replacement criterion has been proposed.

It also lists among its own errors: *"Assumed the four-element alphabet was closed
after `−ω ≠ 0` had already broken it."*

**Where that has and hasn't travelled.** `0^ω = −1` is on the front page of
unsmoothed.neocities.org as *"the structure equation,"* appearing four times in the
served bundle, with nothing recording that its derivation is retracted. The
retraction exists. It did not reach the surfaces. That distinction is the whole
finding — the claim propagated and its proof-status dependency did not.

Proposed status line, for the ruling of whoever holds COTT's authorial intent:

> **UNRESOLVED.** `0^ω = −1` was previously derived using a four-element carrier.
> That derivation is invalid once `−ω ≠ 0` enlarges the carrier. No replacement
> derivation currently exists.

Keep the equation as a conjecture; retire the claim that it has been earned.

## 4. Four questions the algebra has to answer

Each is finite. Together they are the entire blocker.

1. **Is `x^(−1)` the multiplicative-inverse operation on the carrier, or only one
   of the eight exponential schemas?**
2. **If an operation: is it total, and involutive** — x · I(x) = 1 and I(I(x)) = x?
3. **What orbit do negation and inversion generate from {1, 0, −1, ω}** — four
   elements, six, larger finite, or infinite?
4. **Does the algebra induce a cyclic order on that orbit** without using the torus
   drawing?

Answer these and the orientation test in §5 becomes decidable in an afternoon.

## 5. The four-anchor test: neither yes nor no

An attempt to derive the winding classes from the slot algebra rather than read
them off the picture. Strict result:

> **UNDERDETERMINED / MAP NOT DEFINED.**

Not a refutation — the question is not yet well-typed.

- **Negation** is not currently a map {1,0,−1,ω} → {1,0,−1,ω}: `−0` and `−ω` are not
  identified with members of that set, and `−ω ≠ 0` is load-bearing.
- **Inversion** is a schema slot; ordinary evaluation is deliberately barred, so the
  four images are not given as carrier elements.
- The cyclic order 1 → 0 → −1 → ω → 1 is **not derived** in the formulation. Taking
  it from the drawing would make the orientation test circular.

**An error on the Casimir side, recorded.** Two entries of the inversion table were
initially treated as pinned — `1^(−1) = 1^1` read as 1 ↦ 1, and 0 ↦ ω read off
0·ω = 1. Both wrong, and the slot-closure formulation says why: the first is a
fixed *curve*, not a fixed carrier element; the second conflates a multiplicative
relation with the exponent schema. That is precisely the import the formulation
warns against, committed while writing about not committing it.

## 6. The torus inherits the retracted assumption

The drawing assigns y = ±x winding (1,1) and y = ±1/x winding (1,−1), so
|det [[1,1],[1,−1]]| = 2. The topology is correct *if* the winding classes are.

But the quarter-turn phase assignment (1↦0, 0↦¼, −1↦½, ω↦¾) presumes the four
named elements exhaust the carrier — the assumption the formulation has already
broken. The picture therefore encodes two unearned things at once: that
{1,0,−1,ω} is the complete phase cycle, and that its cyclic order is that one.

**No replacement is proposed.** Carrier size does not fix anchor count — six
elements with four distinguished anchors, twelve phase states, or an infinite orbit
with four landmarks all remain open. The only indictment is that the quarter-turn
is unsupported.

If §4 is answered and orientation falls out combinatorially, the torus stops being
an illustration and becomes a theorem-producing representation. That would be worth
having.

## 7. Three open items in the code, one needing intent

From the Phase 0.A / 0.A.1 reports:

- **DELTA.** `CliffordTractionPair.java` documents δ = ω = (1,0) but instantiates
  (0,−1) = 0, making traction-mode identical to parabolic. Almost certainly a
  one-character issue — **deliberately left untouched**, because if it is
  intentional, changing it would destroy the point. This one needs an authorial
  ruling, not a patch.
- `a − a` returns 0, not the specification's null.
- The SymPy discharge for ω·x·0 does not fire.
- Structural ω stays dormant in numeric computation unless it meets the COTT zero —
  an open question, and possibly the interesting one.

## 8. Not claimed

- Not that COTT is wrong. The ring representation is verified, the trace ladder is
  classical and correct, the traction identities pass.
- Not that `0^ω = −1` is false. Its **derivation** is dead; the statement is
  unproven, not refuted.
- Not that the torus is wrong. It is undrawn *from* the algebra — a different and
  fixable complaint.
- Not that any of §4 is settled here. Those are rulings for COTT to make, and
  DELTA was left alone on purpose.

## 9. Provenance

Hashed and dated in `ashleykjuricek-lgtm/hashed-evidence`. Relevant entries:
**028** obstruction theorem · **029** transverse-shell figure correction ·
**032** parity law, register, propagation failure · **034** corrections manifest,
four-anchor test, constants gate · **035** parity note v1 and the session errata ·
**036** parity note v2 with the adversarial amendment.

Reproduction reports are Phase 0.A / 0.A.1. Independent verification of the
theorem is by a separate seat with no shared code or caches.

**Attribution by programme.** COTT, Traction Theory, Mirror Calculus, the Chebyshev
ring and the slot-closure formulation belong to the COTT programme. The parity
theorem, the shell ledger, the propagation gate and the errata belong to the
cubic-torus / Shunya-Zero programme. Every one of them is human-and-model work, and
none of them is one person's.
