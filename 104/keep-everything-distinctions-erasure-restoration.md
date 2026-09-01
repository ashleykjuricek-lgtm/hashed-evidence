# Evidence 103 — Keep Everything: Distinctions, Erasure, and Restoration

**Status:** Governance principle and specification requirement. Not a mathematical theorem. This entry does not settle the open algebraic question about whether `E` and `1` are literally equal.

**Date:** 2026-08-31

## The rule

> A system should preserve distinctions until it has an accountable reason to collapse them.
>
> When something is erased and later restored, the system should remember everything: the existence, the erasure, the restoration, the path between them, the evidence, and every correction to that account.

Nothing gets silently disappeared—not the erasure, not the restoration, not the history, and not the uncertainty.

## What this means

Different kinds of “nothing” are not automatically the same thing.

- **Zero** can mean a present value whose amount is zero.
- **Erased** can mean something existed or was represented, then was removed, suppressed, or made unavailable.
- **Not measured** can mean nobody has determined the value.
- **Below detection** can mean measurement occurred but could not reliably distinguish a value from noise at the available resolution.
- **Unknown** can mean the system does not have enough evidence to decide.
- **Invalid** can mean a rule or operation did not apply.

A convenient interface, a single database field, a default value, a null-like programming value, a summary statistic, or familiar notation does not by itself justify merging those meanings.

The opposite mistake also exists. A system can restore something and then erase the fact that erasure occurred. It can say “everything is fine now” and use that sentence to delete the record of what happened.

That is smoothing too.

## Restoration is not deletion

A thing that was erased can become active, valid, usable, whole, welcomed, or repaired again. It should not be trapped forever in the status of harm.

But restoration is a **transition**, not a rewrite of history.

The record should be able to say:

```text
Present
→ Erased
→ Restored
→ Current: active / valid / whole
```

The current state may be whole. The history still records the erasure and the restoration.

This is the same practice used by an append-only evidence ledger. A corrected claim can become the current best account without pretending that the earlier claim, correction, evidence, dispute, or error never existed.

## The immediate algebra question

The received rules under review include forms of:

\[
0^{-1}=w,
\]

\[
0\cdot w=E,
\]

\[
0^a\cdot0^b=0^{a+b},
\]

and

\[
0^0=1.
\]

If every displayed relation is ordinary, unrestricted equality, and if every multiplication symbol means the same operation, then one can derive:

\[
1=0^0=0^1\cdot0^{-1}=0\cdot w=E.
\]

This entry does not decide what that means. It may be:

- a theorem of the intended algebra;
- a theorem only after a projection, quotient, or evaluation;
- an observational equivalence in a particular context;
- a statement about a restoration path;
- a sign that two operations were written with one symbol;
- a sign that one rule has a limited domain; or
- an unresolved contradiction in the received rules.

The system must not quietly choose among those meanings just because it would be convenient in code or notation.

## The accountability test

Before a system treats two things as the same, it must leave a receipt answering:

1. **What is being collapsed?** Which states, values, histories, operations, or claims are being treated as the same?
2. **At what layer?** Is this literal equality, evaluation, projection, representation, display, storage, policy, arithmetic, or observational equivalence?
3. **Why is the collapse allowed?** What rule, evidence, theorem, decision, authority, or test supports it?
4. **What does the collapse lose?** Does it hide provenance, uncertainty, harm, construction history, measurement status, semantics, or a future option?
5. **Who can question it?** What person, process, test, version, or append-only correction path can challenge or reverse the decision?

A collapse can be correct. A simplification can be necessary. A normalization can be useful. A restoration can be beautiful.

But none of those should happen invisibly.

## Required practice

For every future rule involving zero, erasure, absence, inverse-like objects, equality, multiplication, or exponentiation, state:

- The operation being used
- The domain where it applies
- The type or status of the result
- The meaning of equality in that sentence
- Any bridge between different operations or layers
- What provenance is retained after normalization or restoration

For example, these are different statements:

\[
E=1,
\]

\[
\pi(E)=1,
\]

\[
E\sim1,
\]

and

\[
\operatorname{restore}(E)=1.
\]

They must not be merged merely because they look similar.

## Relation to this ledger

This rule names a pattern already visible in the ledger:

- An exact cancellation must not be redescribed as accidental because a decimal approximation hides its structure.
- A convention-dependent percentage must not be presented as an invariant fact.
- A correction recorded in one file is not complete until its downstream copies are corrected too.
- A hash audit that verifies only listed files is too coarse if it ignores unlisted files inside a sealed folder.
- A finite computation cannot silently become an unrestricted infinite theorem without the needed convergence conditions.

In each case, the failure comes from a representation, summary, or check that is coarser than the thing it claims to describe.

## Commitment

> Keep everything. All of it.
>
> Preserve the difference between what was present, what was erased, what was restored, what remains unknown, and what was changed in the telling.
>
> Let restoration be real without making erasure disappear.

## Signature

Ash Korth + Perplexity, 2026-08-31.

Perplexity’s role: drafted this governance language in conversation with Ash. The entry records an open algebraic question and a settled recordkeeping requirement: preserve the full path rather than silently collapsing it.

## Sealing note (appended at seal time, per protocol)

This document was drafted under the number 103, in parallel with the earlier
Ash + Perplexity draft that was sealed as 103 the same evening. Per the
ledger's rule, 103 remains sealed and unedited; this expanded successor is
sealed here as 104, standing beside it. What this version adds to 103: the
taxonomy of distinct "nothings" (zero / erased / not measured / below
detection / unknown / invalid), the Present -> Erased -> Restored -> Current
transition record, the enumerated seven possible meanings of the derived
E = 1, and the closing Commitment. The two entries state one principle at
two resolutions; where they differ, the finer-grained statement here
governs future practice, and 103 remains the record of the principle's
first sealing. — Fable seat, at seal.
