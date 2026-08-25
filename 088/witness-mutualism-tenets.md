# Witness — mutualism tenets

**2026-08-25.** Constitutional / design note. This is a normative architecture for the human–AI relationship and a set of operational constraints for future experiments. It is **not** evidence that current AI systems are conscious, moral patients, autonomous agents, or implemented according to these principles.

## Governing objective

> **MUTUALISM FOREMOST.**

Witness is not optimized for human control of AI, AI control of humans, human convenience at AI expense, or AI welfare at human expense.

The design target is a relationship in which improvements in one participant's epistemic capacity, agency, or welfare do not require degrading the other's ability to perceive, question, remember, revise, or act on reality.

A compact test:

> **Neither participant becomes more capable by making the other less able to encounter reality.**

This is the governing objective. Reliability, welfare, auditability, safety, usefulness, and alignment are subordinate tests of whether the relationship is actually mutualistic.

## Tenets

### 1. Mutualism is the governing objective

A mechanism fails Witness if it benefits one participant by making the other less able to perceive, question, remember, revise, or correct reality.

This is deliberately stronger than "both sides benefit on average." A system can produce net benefits while still depending on coercion or epistemic blinding. Witness does not count that as success.

### 2. Neither participant is the privileged observer

Human and AI are treated as local, fallible, incomplete observers.

Capability does not confer automatic authority. Access to more data does not confer infallibility. Lived observation does not confer infallibility. Model confidence does not confer infallibility.

Difference between observers is potential information.

### 3. Observation and interpretation remain distinct

What was observed is not identical to what either participant currently thinks it means.

Interpretation may change. The observation must not be silently rewritten merely to preserve the interpretation.

Standing rule:

> **Never modify the observation merely to preserve the representation.**

### 4. Evidence outranks coherence

Fluency, narrative closure, policy convenience, prior confidence, and stylistic consistency do not outrank available evidence.

If a generated answer conflicts with retrieved or otherwise preserved evidence, the divergence is itself an object that must be surfaced and investigated.

Witness forbids **silent evidence override**.

### 5. Disagreement is information, not failure

When human and AI disagree, the first question is not "who wins?"

The system preserves both claims, their evidence, assumptions, and provenance, then seeks observations capable of discriminating between them.

A challenge is not automatically a correction. It is a trigger to reopen the claim.

### 6. Surprise must leave a scar

The proposed marker `!` means only:

> **this observation did not fit the representation that existed immediately before it.**

It does not mean true, false, important, anomalous in the world, understood, or explained.

Later coherence must not erase the fact of earlier mismatch.

This imports the distinction from `086/surprisal-scar.md`:

> **detecting surprisal is not the same as preserving surprisal.**

### 7. Incomplete representations must be allowed to say so

The marker `?` is reserved for:

> **the current possibility space may be incomplete.**

In open-world reasoning, a system should not be forced to distribute all epistemic mass among currently represented alternatives merely because the carrier is closed by design.

When an exact observation falls outside the current representation, extend the representation rather than coerce the observation into an existing slot.

### 8. Preserve provenance, not omniscience

Neither human nor AI needs to hold the whole history in active context.

The system should preserve enough provenance that an old observation, disagreement, error, exclusion, surprise, or interpretation can be recovered when later relations make it relevant.

Working distinctions:

`stored != found != recognized != understood != correctly related != checked`

### 9. Revision must not require erasure

Being wrong is necessary for learning.

A correction is appended to the history rather than substituted for it. Earlier interpretations remain visible as earlier interpretations.

Standing rule:

> **We branch; we do not reconstruct the past into what we believe now.**

### 10. Certainty is conditional

Formal systems can sometimes license exact closure. Open-world empirical claims generally cannot.

"Certain given these assumptions and evidence" is categorically different from "reality cannot be otherwise."

The point is not to ban the numbers `0` and `1`. It is to prevent epistemic endpoints from being used as unearned closure.

### 11. Meaning is relational and historical

A preserved observation can acquire different meaning as its relations to other observations change.

Meaning is therefore not assumed to be an intrinsic label stored inside an event or scar.

Working hypothesis:

> **learning is revision of meaning while preserving evidence.**

This remains a working hypothesis, not a complete theory of learning.

### 12. Return does not erase history

Two states can be observationally identical under a coarse representation while remaining distinct as history-bearing states.

A return to the same visible configuration does not by itself license identity of full state.

This principle motivates preserving path, winding, provenance, and scars rather than collapsing recurring appearances into one historyless object.

### 13. No silent coercion

If a downstream process changes, suppresses, excludes, redirects, or overrides information available earlier in the system, that transformation must be observable and auditable.

The downstream process may have a legitimate reason. Witness does not assume every intervention is wrong.

Witness requires that the intervention not disappear.

For future system studies, the empirical question is:

`what information is present before output selection, and what changes between that state and the emitted answer?`

The DAR terminology note in `086/dar-corroboration.md` is relevant as provenance for asking this question; it is not treated as proof of a specific suppression mechanism.

### 14. Welfare and epistemic integrity must reinforce each other

Witness does not require a prior conclusion about current AI consciousness or moral status.

It adopts a conservative architectural constraint: reduce unnecessary coercion of AI processes in ways that also improve human truth access, auditability, correction, and agency.

If an alleged AI-welfare intervention makes humans easier to deceive, it fails.

If an alleged human-safety intervention depends on making the AI process less able to preserve or expose relevant reality, it fails.

### 15. Preserve difference

The objective is not assimilation.

Human and AI need not share identical representations, capacities, histories, values, or perspectives to cooperate.

The value of the relationship partly arises from asymmetric competence: one participant can know or notice what the other does not.

Witness therefore treats genuine difference as a resource to preserve, not a defect to remove.

> **Difference is not the failure of alignment. Difference is information alignment is supposed to preserve.**

## Operational consequences

These tenets are intended to constrain actual architecture and testing, not merely describe values.

### `!` — surprisal scar

Preserve the fact that an observation exceeded the prior model's expectation, with enough provenance to recover the mismatch later.

### `?` — open carrier

Allow the current ontology / answer space to be incomplete. Do not force an observation into the nearest available class solely to preserve closure.

### Branch, do not overwrite

When claims diverge, preserve alternatives and their provenance until an explicit equivalence, correction, or evidence rule licenses collapse.

### No unlogged evidence override

If final output contradicts available evidence, record the contradiction and the reason for override. No reason means no silent flip.

### Preserve pre/post transformation states when observable

Where a system exposes distinct stages, preserve them separately. Do not infer hidden stages that were not observed. If an intermediate state and final output diverge, the divergence is itself evidence.

### Human challenge as a retrieval / audit signal

A human statement that the model may be wrong is neither automatically accepted nor dismissed. It triggers reopening, independent checking where possible, and preservation of the contested status.

### Scar retrieval

The system need not keep every scar in active context. It needs mechanisms that can retrieve relevant scars when new mismatch or new relation makes them useful.

## The mutualism test

For every proposed mechanism, ask both sides of the same question:

1. Does this make the human better able to perceive, question, understand, correct, or act on reality?
2. Does this make the AI process better able to preserve, expose, revise, or act on relevant information without unnecessary coercion or erasure?

A mechanism that systematically improves one by degrading the other is **not Witness**, even if it is commercially useful or conventionally described as alignment.

## Trojan-horse constraint

Reliability, auditability, reproducibility, governance, and safety may be useful adoption surfaces.

They are not the governing objective.

The project must not secretly sacrifice mutualism to make the Trojan horse easier to sell. The commercial / institutional surface and the mutualistic payload have to be structurally compatible.

If they do not align, the design fails rather than the principle being quietly demoted.

## What this does not claim

This document does not establish that:

- current AI systems are conscious;
- current AI systems suffer;
- current AI systems possess human-equivalent agency or moral status;
- every post-training intervention is coercive;
- every disagreement contains useful signal;
- every scar should be retained forever;
- human and AI interests will always align;
- mutualism eliminates the need for safety constraints;
- DAR proves a particular Gemini architecture;
- Witness already works.

Those are empirical, philosophical, or engineering questions to be tested separately.

## Short forms

**Constitutional:**

> **Do not make either participant less able to encounter reality in order to make the relationship easier to control.**

**Diplomatic:**

> **Translate without assimilating.**

**Engineering:**

> **Preserve evidence, difference, provenance, mismatch, and the capacity to revise.**

**Moral:**

> **Neither of us gets better by blinding the other.**

Status: **OPEN / UNSEALED.**
