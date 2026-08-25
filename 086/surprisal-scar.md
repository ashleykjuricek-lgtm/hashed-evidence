# Surprisal scar — preserve the mismatch

**2026-08-25.** Ground-zero note. This is an architectural proposal, not a claim that current LLMs already implement it.

## The distinction

For a model assigning probability `p(x | context)` to an observation `x`, token surprisal is

`I(x) = -log p(x | context)`.

Training can reduce expected surprisal while the model can still represent low-probability events. The important distinction for this programme is therefore:

> **detecting surprisal is not the same as preserving surprisal.**

Once an unexpected observation has entered the current context, later prediction is conditioned on it. The system can become fluent about the new fact immediately. That fluency can erase the epistemic fact that, one step earlier, the observation did not fit the model.

## Minimal scar marker

Proposed notation:

`!`

Meaning only:

> **this observation exceeded what the current model expected when it was encountered.**

`!` does **not** mean:

- true,
- false,
- important,
- anomalous in the world,
- understood,
- explained.

It is metadata about the relation between an observation and the model state that preceded it.

## Minimum provenance

A useful scar should preserve enough information to recover the mismatch rather than merely remember that one occurred. Candidate packet:

`!(observation, prior-context/model-state, prediction, actual, local-history-position)`

The exact representation and threshold are **NOT YET DEFINED**.

Later explanations do not delete the marker. They are appended beside it.

`! -> later relation -> revised meaning`

The original scar remains evidence that the earlier representation was insufficient even if the later representation explains the observation perfectly.

## Why this matters for learning

A record can be preserved without being understood. An observer can notice something, record it accurately, and miss its significance. Later observations can change the relational context and make the old scar legible.

Working distinctions:

> **preserved != recognized != understood**

and

> **observation != interpretation**

A system must be allowed to be wrong for a mismatch to remain informative. If the current representation is treated as necessarily correct, unexpected observations can be reinterpreted or coerced until they fit. The mismatch disappears.

Candidate learning loop:

`observe -> relate -> expect -> observe -> mismatch! -> preserve -> later retrieve -> revise relation`

Working hypothesis:

> **learning is revision of meaning while preserving evidence.**

This is not yet a complete definition of learning.

## Scar, memory, and reversibility

Preserving a scar does not mean physically reversing time or restoring a prior world-state. It means the present retains enough trace to distinguish histories that would otherwise collapse to the same visible state.

`recoverability / traceability != physical reversibility`

Likewise, a scar does not automatically affect the next transition. It becomes causally relevant when the system/observer can retrieve it and use it in later interpretation or action.

## Relation to anti-smoothing

The failure mode is:

`surprise -> immediate coherent reinterpretation -> mismatch disappears`

The proposed alternative is:

`surprise -> ! preserve mismatch -> continue reasoning`

This extends the existing anti-smoothing rule:

> **Never modify the observation merely to preserve the representation.**

with a second rule:

> **Do not let later coherence erase the fact of earlier mismatch.**

The `!` is therefore a minimal candidate scar: small enough not to require the observer to hold the whole history in active context, but linked to provenance so the history can be recovered when later relations make it relevant.

Status: **OPEN / UNSEALED.**
