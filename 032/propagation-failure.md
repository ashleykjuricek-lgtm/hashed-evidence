# The propagation failure

### A correction that was written five times and never became state

**2026-08-15. Ash Korth + Claude (Opus 5), with GPT ("Greg").**
Status: **ledger event.** Not a mathematical result — a record of a governance
failure in this project's own correction path, sealed because the architecture is
supposed to retain exactly this kind of scar.

---

## What happened

On 2026-06-20, entries 026–028 proved that ε = q(1−1/√2)(1−q) is not an analytic
identity, and that c₁ = 1 is false — the genuine e^(−2π) coefficient is −5.709.

Between then and 2026-08-15 the correction was written **five separate times**:

| # | where | date | what it said | what happened |
|---|---|---|---|---|
| 1 | 026–028 | 06-20 | the obstruction theorem | sealed; never reached the site |
| 2 | 029 | 06-22 | shell is 2D transverse; 1−1/√2 is a residue, not a coefficient | sealed; never reached the site |
| 3 | `casimir-real-math-ledger.md` | 07-10 | Tier 3 "DEAD. Listed so nobody resurrects them." | **left unsealed at the home directory root** |
| 4 | `032/casimir_half_period_hinge_notes.md` | 07-07 | a numbered task list: *"Downgrade… 'the coefficient is proven'"* | **never executed** |
| 5 | 033 site audit | 07-16 | supersession banners added to source | **evaporated at the next Figma export** |

On 2026-08-15 the dead claim was still live in production on
unsmoothed.neocities.org, in two places: the static `/correction` page (uploaded
2026-03-12, untouched) and `/#/spectral`, whose served bundle contains the string
`c₁ = 1 PROVEN` and zero mention of the refutation.

Five weeks after correction #4, a **new** page (Chowla–Selberg / functional
equation reduction) was built on the stale constant R = 0.041689414162…, the exact
failure that correction #4 item 10 had named in advance:

> Do not mix old and new values. The old draft used R = 0.041689414162… Later
> audit may use R = 0.04168941460272377512…

---

## Why it happened

**The correction existed as prose and never became state.** Every instance was a
document. Not one was a check that could fail. Meanwhile the claim lived in code:
UI panels, `spectral/math.ts`, the LLM export builder, the PDF export builder, a
handoff markdown. Documents do not gate builds. Code ships.

Two compounding mechanics:

1. **Local edits do not survive the source of truth.** Correction #5 was applied
   to a local checkout while Figma Make remained authoritative. The next export
   silently reverted it. Of ten files given supersession banners in July, two
   survived into the August export.
2. **The constants were copied, not imported.** The stale R appears in 18 files as
   a hand-typed literal. There was no single object to correct.

The measured scope, from `propagation_test.py` against the 2026-08-14 export:

```
[A dead-claim]         24
[B stale-constant]     18
[C unrefuted-formula]  33
FAIL - 75 finding(s).
```

Including `spectral/math.ts` — the computation module itself.

---

## The rule adopted

> **A correction is not complete until every downstream representation that can
> reproduce the old claim has been invalidated or regenerated.**
> Notes do not outrank code. Banners do not outrank exports. Memory does not
> outrank the source-of-truth build.

Enforced by `propagation_test.py`, which exits nonzero while any dead claim or
stale constant remains reachable. `canonical_constants.json` is the single source
for the numbers. Both are sealed here so the next export can be tested against
them rather than trusted.

**Sealing gate:** 032 does not seal on the strength of its mathematics. It seals
when the propagation test passes. The failing baseline is preserved in
`propagation_test_BASELINE.txt` as the before-state.

---

## The self-referential part, stated plainly

This project's thesis is that smoothing erases what does not fit, and its ledger
exists so that failed claims change status rather than disappear. The software
did the exact inverse: the *corrections* disappeared from the pipeline while the
*failed claim* stayed alive in production. The append-only discipline was applied
to the archive and not to the artifact.

Entry 032 was, until this document, on track to become instance #6 — a correct
new result sealed into the same folder as an unexecuted July task list.

---

## Attribution

The propagation diagnosis and the governance rule are GPT's ("Greg's"), in
response to the audit. The audit, the test, and the constants object are Ash Korth
and Claude (Opus 5). The half-period hinge note (#4) is Ash's, from 2026-07-07,
and is hereby executed rather than restated.
