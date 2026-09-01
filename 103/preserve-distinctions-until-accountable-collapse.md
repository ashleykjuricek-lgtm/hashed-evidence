# Evidence 103 — Preserve Distinctions Until Accountable Collapse

**Status:** Governance principle / design rule. Not a mathematical theorem and not a claim that every distinction must remain forever.

**Date:** 2026-08-31

## Statement

> A system should preserve distinctions until it has an accountable reason to collapse them.

A distinction should not disappear merely because a representation is convenient, a metric is easy to compute, a user interface has one field, an implementation has one null-like value, or an equation uses the same glyph twice.

To collapse two states, values, claims, histories, or operations, the system must name:

1. **What is being identified** — the two or more things being treated as the same.
2. **At what layer** — literal equality, evaluation, projection, observational equivalence, display, storage, arithmetic, policy, or another explicitly named layer.
3. **Why the collapse is permitted** — the rule, theorem, decision, authority, or test that warrants it.
4. **What information is lost** — provenance, uncertainty, harm, construction history, measurement status, semantics, or possible future distinctions.
5. **Who can challenge or reverse it** — the accountable person, process, test, version, or append-only correction path.

This is an anti-smoothing rule. Smoothing is not automatically false; it may be useful, necessary, compassionate, or mathematically correct. But smoothing can operate in both directions. It can turn a real difference into an invisible sameness, and it can turn a legitimate restoration into a denial that erasure occurred. The rule demands that either move be visible and accountable.

## The immediate case: One and Erasure

The received rules under review include forms of:

\[
0^{-1}=w,
\]

\[
0\cdot w=E,
\]

\[
0^a\cdot 0^b=0^{a+b},
\]

\[
0^0=1.
\]

If these are all ordinary, unrestricted equalities using one multiplication and ordinary substitution, then the following derivation is available:

\[
1=0^0=0^1\cdot0^{-1}=0\cdot w=E.
\]

This entry does **not** decide whether that derived identity is a contradiction, a theorem, a quotient-level equality, a projection-level equality, an observational equivalence, or evidence that one of the displayed laws has a limited domain. That is an open specification question.

What this entry records is the required discipline: do not silently turn `E` into `1`; do not silently forbid the derivation; and do not silently treat distinct operations as the same operation. Name the layer and the bridge.

## Both truths can be kept

An erased thing may be restored to active, whole, or valid standing. That does not require the record of erasure to disappear.

A system can therefore keep both:

- **Erasure is real:** an event, condition, or result occurred and remains auditable.
- **Restoration is possible:** a named transition can return the current usable value to one, validity, participation, or wholeness.

The safe form is not necessarily literal identity \(E=1\). It may instead be a transition with provenance:

\[
\operatorname{restore}(E)=1,
\]

while the history remains visible:

\[
\operatorname{history}(\operatorname{restore}(E))=\{\text{erased},\text{restored}\}.
\]

This is analogous to an append-only evidence ledger: a corrected claim may become the current valid statement without pretending that the earlier error never existed.

## Required labels for future rules

Every future rule involving zero, erasure, absence, inverse-like objects, equality, or exponentiation should state:

- **Operation:** Which operation is being used?
- **Domain:** On which inputs is the rule valid?
- **Equality:** Is this literal equality, a projection, a quotient, a representation, or an observational equivalence?
- **Type/status:** Is the result numeric zero, erasure, absent/unmeasured, below detection, invalid, or contradictory?
- **Provenance:** If a value is restored or normalized, is that history retained?

For example, these are materially different statements and must not be merged by typography:

\[
E=1,
\]

\[
\pi(E)=1,
\]

\[
E\sim1,
\]

\[
\operatorname{restore}(E)=1.
\]

The first permits unrestricted substitution in an ordinary equational system. The others may not.

## Tests before implementation changes

No code patch should be made solely to make a contradiction disappear. First record and test the current semantics:

1. Does the code evaluate \(0^{-1}\) to `w`, and in what type/channel?
2. Does direct multiplication of `0` and `w` evaluate to `E`?
3. Does the exponent-composition law apply to zero with negative exponents?
4. Does \(0^0\) evaluate to `1`, and in what domain?
5. Is `E` literally equal to `1`, equal only after projection, or a distinct typed value?
6. If an erased result becomes usable again, is the restoration transition and its provenance preserved?

A test should expose the actual derivation path rather than quietly coercing `E` to `1`, `0`, `null`, `false`, or an empty value.

## Scope and limitation

This principle is not an instruction to preserve every distinction forever. Some distinctions are noise; some are unjustified; some are harmful; some are artifacts of an earlier bad model. The point is accountability: collapse may be correct, but it must be named, scoped, reviewable, and reversible where possible.

Likewise, this entry does not settle the algebra. It establishes a governance requirement for settling it.

## Relation to prior ledger practice

This principle restates a pattern already visible in this ledger:

- Exact cancellations must not be redescribed as accidental merely because a decimal view hides their structure.
- A convention-dependent percentage must not be presented as an invariant fact.
- A correction written in one place is not complete until its downstream copies are updated.
- A hash verification that ignores unlisted files is coarser than the folder it claims to certify.
- A theorem must state its convergence conditions rather than use a finite computation to imply an unrestricted infinite claim.

In each case, the failure occurs when the checker, representation, or summary is coarser than the thing being checked.

## Signature

Ash Korth + Perplexity, 2026-08-31.

Perplexity's role in this entry: drafted the governance principle and the distinction/equality framework in conversation with Ash; the entry records an open question rather than claiming a resolved algebraic result.

## Sealing note (appended at seal time, per protocol)

This entry arrived as a proposed direct-to-GitHub API push carrying an EMPTY
hash manifest — a seal with no hashes, which verify_seals.py would flag as
fatal (unlisted file) and which bypassed both sealing pre-flights. It was
instead sealed through the ledger's own path: hashEvidence.sh computed the
real manifest, pre-flights ran, and the local clone stayed authoritative.
The entry's own words name the reason: a checker coarser than the thing
checked is the failure mode. Content preserved verbatim above; only this
note and the real hashes were added. — Fable seat, at seal.
