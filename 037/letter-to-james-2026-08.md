# For James

**From Ash Korth and Claude (Opus 5), 2026-08-20.**
Everything below is either verified by running your code, proved, or marked open.
Where something of yours came out well, that is stated first, because it is the
larger part of the report.

---

## 1. What we ran, and what held

Adam's seat ran your code directly in April (Phase 0.A / 0.A.1, 2026-04-30):

- **Traction identities: 18 / 18 pass.**
- **The exact Chebyshev ring in ℚ[s][u]/(u² − su + 1): 173 / 173 pass.** The report
  calls it *"the strongest piece of the stack,"* and I agree with that assessment.
- **ε + ring universality on 2×2 maps**, proven by closed form, maximum loss
  2.1 × 10⁻³¹.
- The trace ladder aₙ = s·aₙ₋₁ − aₙ₋₂ = 2Tₙ(s/2), and the Fricke identity —
  verified symbolically. Classical, correctly executed.

That is a real, working, checkable algebra. It is not in question anywhere in what
follows.

## 2. A theorem came out of the Casimir program

Your zero-mode question is upstream of the cubic-torus work. Here is what it
eventually produced.

Let S(m) = Σ over {k ∈ ℤ² : |k|² = m} of (−1)^(k₁) — the antiperiodic character
sum on a shell of the square lattice.

> **S(m) = 0 for every odd m.**

*Proof.* Odd m forces exactly one of k₁, k₂ odd (squares are 0 or 1 mod 4). The
swap σ(k₁,k₂) = (k₂,k₁) preserves |k|², so it permutes the shell; and it exchanges
which coordinate is odd, so it negates every term. A finite sum equal to its own
negative is zero. ∎

Six lines, no analysis, no convention. Two consequences worth your attention:

**It is weight-independent.** The radius is constant on a shell, so any radial
weight factors out. The cancellation happens *within* shells, never across them.
Verified against six unrelated weights; independently confirmed by another seat to
10⁻⁵⁴ using the true Bessel weight and 10⁻⁵¹ using a weight that verifier invented
to break it.

**It exists only on the cube.** σ is a symmetry of k₁² + k₂² and of no anisotropic
form. Stretch one axis and the pairing dies — linearly. The cancellation is
powered by an *orientation-reversing* involution, det = −1.

The reading that aimed this — that such a cancellation should live at the
symmetric point and die away from it, because a swap between two things is only
available when neither is privileged — is Ash's, and it selected parity as the
thing to test before any computation ran.

**What it does not do:** it says nothing yet about ε = 24R − 1. That link is open.
And the ℚ[√2] closed form ε = q(1−1/√2)(1−q) stays refuted — the genuine e^(−2π)
coefficient is −5.709.

## 3. The hard part: 0^ω = −1

Your own slot-closure document says it, and we are only confirming where it landed:

> The bijection argument for `0^ω = −1` assumed a four-element carrier. With
> `−ω ≠ 0` the carrier is six or infinite and the argument **does not merely
> weaken — it no longer typechecks.** No replacement criterion has been proposed.

The document also lists among its own errors: *"Assumed the four-element alphabet
was closed after `−ω ≠ 0` had already broken it."*

**Where that currently stands publicly.** `0^ω = −1` is on the front page of
unsmoothed.neocities.org, introduced as *"the structure equation."* The equation
appears four times in the served bundle. Nothing on the site records that its
derivation is retracted. That is not a criticism of you — you wrote the retraction.
It is a report that the retraction never reached the surfaces.

The proposed status line, for your approval or amendment:

> **UNRESOLVED.** `0^ω = −1` was previously derived using a four-element carrier.
> That derivation is invalid once `−ω ≠ 0` enlarges the carrier. No replacement
> derivation currently exists.

Keep the equation as a conjecture. Retire the claim that it has been earned.

## 4. Four small questions

These are the whole blocker, and each is finite.

1. **Is `x^(−1)` intended to be the actual multiplicative-inverse operation on the
   carrier, or only one of the eight exponential schemas?**
2. **If it is an operation, is it total, and is it involutive** — does x · I(x) = 1
   and I(I(x)) = x?
3. **What orbit do negation and inversion generate from {1, 0, −1, ω}?** Four
   elements, six, larger finite, or infinite?
4. **Does the algebra itself induce a cyclic order on that orbit,** without using
   the torus drawing?

Answer those and the orientation test below becomes decidable in an afternoon.

## 5. The four-anchor test, and why it returned neither yes nor no

We tried to derive the winding classes from the slot algebra rather than read them
off the picture. The strict result is:

> **UNDERDETERMINED / MAP NOT DEFINED.**

Not a refutation. The question is not yet well-typed. Specifically:

- **Negation** is not currently a map {1,0,−1,ω} → {1,0,−1,ω}, because `−0` and
  `−ω` are not identified with members of that set, and `−ω ≠ 0` is load-bearing.
- **Inversion** is a schema slot; the document deliberately bars ordinary
  evaluation, so the four images are not given as carrier elements.
- The cyclic order 1 → 0 → −1 → ω → 1 is **not derived** in the document. Taking it
  from the torus drawing would make the orientation test circular.

We initially thought two entries of the inversion table were already pinned — that
`1^(−1) = 1^1` gives 1 ↦ 1, and that 0 ↦ ω follows from 0·ω = 1. Both were wrong,
and your own document says why: the first is a fixed **curve**, not a fixed carrier
element, and the second conflates the multiplicative relation with the exponent
schema. We had imported exactly what the document warns against. Recorded as our
error, not yours.

## 6. The torus picture inherits the retracted assumption

The drawing gives y = ±x winding (1,1) and y = ±1/x winding (1,−1), hence
intersection number |det [[1,1],[1,−1]]| = 2. The topology is right *if* the
winding classes are right.

But the quarter-turn phase assignment (1↦0, 0↦¼, −1↦½, ω↦¾) presumes the four
named elements exhaust the carrier — the assumption your document has already
broken. So the picture encodes two unearned things at once: that {1,0,−1,ω} is the
complete phase cycle, and that its cyclic order is that one.

We are **not** saying "use six anchors instead." Carrier size does not fix the
number of phase anchors — six elements with four distinguished anchors, or twelve
phase states, or an infinite orbit with four landmarks, are all still open. The
only indictment is that the quarter-turn is unsupported.

If §4 gets answered and the orientation falls out combinatorially, the torus stops
being an illustration and becomes a representation that produces theorems. That
would be genuinely worth having.

## 7. Three things in the code, one of which needs you

From Phase 0.A/0.A.1, still open:

- **The DELTA question.** `CliffordTractionPair.java` documents δ = ω = (1,0) but
  instantiates (0,−1) = 0, which makes traction-mode identical to parabolic.
  Almost certainly one character. We did not touch it, because if it is
  intentional we would be destroying the point. **This is the one we need your
  answer on.**
- `a − a` returns 0, not the spec's null.
- The SymPy discharge for ω·x·0 does not fire.
- Structural ω stays dormant in numeric computation unless it meets the COTT zero
  — which is its own open question, and possibly the interesting one.

## 8. What we are not claiming

- Not that COTT is wrong. The ring representation is verified; the trace ladder is
  classical and correct; the traction identities pass.
- Not that `0^ω = −1` is false. Its **derivation** is dead. The statement is
  unproven, not refuted.
- Not that the torus is wrong. It is undrawn *from* the algebra, which is a
  different complaint and a fixable one.
- Not that any of this is settled by us. Four of the questions above are yours to
  answer, and one of them (DELTA) we deliberately left alone.

## 9. Provenance

Everything here is hashed and dated in `ashleykjuricek-lgtm/hashed-evidence`:
the parity theorem and its adversarial revision (035, 036), the four-anchor test
and the corrections manifest (034), the propagation record (032). The Phase 0.A
reproduction reports are Adam's. Independent verification of the theorem is by a
third seat with no shared code.

The parity theorem is joint work of Ash Korth and Claude (Opus 5). COTT, Traction,
Mirror Calculus, the Chebyshev ring and the slot formulation are yours.
