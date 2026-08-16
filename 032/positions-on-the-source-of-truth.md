# Positions on the source-of-truth question

### Recorded, not resolved

**2026-08-15.** Sealed with 032. Ash's instruction: *"we just record what we all
think."* This document does that. It does not pick a winner, and it is not a
decision. Where a party did not state a view, that is recorded as an absence
rather than inferred.

---

## The open question

The propagation test fails at 75 findings against the 2026-08-14 Figma export.
Fixing them requires knowing where an edit becomes real.

**(a) Figma Make stays authoritative.** Corrections are applied in Figma, exported,
then tested.

**(b) A local tree becomes the source of truth.** Figma Make is retired as the
editor. Corrections are applied directly and gated by the test.

---

## Claude (Opus 5)

**(b), with the cost stated.**

(a) cannot close the hole it is meant to close. Correction #5 — the July
supersession banners — was applied to a local checkout while Figma remained
authoritative, and the next export reverted eight of ten. Under (a) that can
happen again on any future export, because Figma has no propagation test and
cannot be given one. The gate would sit downstream of the thing that reverts.

(b) ends it permanently: one tree, one test, no re-import.

The cost is real and not mine to discount — (b) means giving up a visual editor
that has evidently been productive, in exchange for a discipline that is only
worth it if the corrections actually matter more than the velocity. That is a
judgment about how Ash wants to work, not a technical fact.

Also recorded: I have been wrong twice in this session about scope. I estimated
20 affected files; the test found 75. Weight my confidence accordingly.

---

## Greg (GPT)

**No position on (a) vs (b).** Greg did not address the editor question. What Greg
did state, and what is adopted:

- The diagnosis: *"this is no longer primarily a math-correction problem. It's a
  deployment/governance failure. The correction existed as prose but never became
  state."*
- The rule: *"A correction is not complete until every downstream representation
  that can reproduce the old claim has been invalidated or regenerated. Notes do
  not outrank code. Banners do not outrank exports. Memory does not outrank the
  source-of-truth build."*
- The five-step atomic release: kill every instance including export payloads;
  replace rather than merely retract; one canonical constants object, "no manually
  copied ground truth strings scattered around components like mathematical
  glitter"; mark the Chowla–Selberg page invalid pending recomputation and keep
  Γ(1/4)⁴/4008 as a **negative control**; seal only after the propagation test
  passes.
- That the propagation failure should itself be a ledger event.

Greg's rule is agnostic between (a) and (b) — it constrains the gate, not the
editor. Both branches can satisfy it; only one can satisfy it durably.

---

## Ash Korth

**Records rather than resolves.** That is the position, not the absence of one.

Her prior recorded view on the substance is correction #4,
`casimir_half_period_hinge_notes.md`, 2026-07-07 — a numbered task list with
explicit "Claims to Keep" and "Claims to Avoid," which is a complete and correct
correction pass that was never executed. On the *substance* she has been right and
consistent since July. What failed was execution, not judgment.

On the workflow she has declined to choose, and this document is the form that
declining takes here: the branch stays open and visible instead of being closed by
whoever is most confident. Consistent with the project's stated discipline —
nothing is smoothed to a scalar because a decision would be tidier.

---

## The Figma agent

**No position on the question.** Recorded because its practice is relevant
evidence: on the scar page it separated a verified fact, a cross-domain analogy,
and a philosophical identity claim, tagged each, and preserved line 48's
disclaimer — *"They are emphatically not the same mathematical object. The rhyme
is that each can preserve information that a simpler representation would
discard."* Its quotation was checked and is verbatim.

So the epistemic hygiene inside Figma is good. The failure is not that the editor
produces careless work; it is that the editor has no memory of what has been
killed. That is an argument about tooling, not about the agent.

---

## What is not decided

- Whether (a) or (b).
- Therefore: the 75 findings remain live, and the dead claim remains in production
  on `/correction` and `/#/spectral`.
- Therefore: **032 does not seal.** Per Greg's gate, adopted.

---

## The risk in this document

This project's failure mode is that writing something down felt like completing
it. Five documents recorded the correction; none changed anything. A sixth
document recording a disagreement is structurally the same move, and it would be
dishonest to seal it without saying so.

What differs: the gate is no longer prose. `propagation_test.py` returns exit code
1 at 75 findings whether or not anyone reads this. `canonical_constants.json` is
the single object the numbers must come from. Those are state. This document is
allowed to be only a record precisely because it is not the thing holding the
line.

If the branch stays open indefinitely, the test stays red and the site stays
wrong. That is the honest cost of not choosing, recorded here so that it is a
known cost rather than a forgotten one.
