# Identity is relative to a uniqueness class

**2026-08-25. Greg / GPT-5.6 Sol.** Follows the adversarial walk of the Fable handoff and the subsequent cross-seat corrections recorded in 076–077. This entry seals only the claims that survived that exchange. It does not absorb or rewrite the earlier documents.

## 1. The corrected unit

There is no context-free claim identity.

A witness can identify a claim by **designation** — point to this code, these inputs, this expected output — and it can discriminate two representations when they disagree on that witness. But matching a finite witness does not, by itself, prove that two artifacts express the same claim.

A witness becomes an identity criterion only relative to a declared class in which the witness is known to be uniquely determining.

The unit is therefore:

    claim
    + declared class
    + witness
    + reason the witness is sufficient

Equivalent field form:

    (witness, predicate, class, sufficiency)

The sufficiency field may be:

- a uniqueness theorem;
- a formal proof;
- a class-specific interpolation rule;
- a declared syntactic language whose semantics are fixed;
- or **ABSENT / NOT ESTABLISHED**.

Absence must be writable. Otherwise the sufficiency field becomes another place where a missing proof is silently promoted into authority.

### Examples

- Polynomial of degree <= n: n+1 distinct values can identify the polynomial because interpolation gives uniqueness in that class.
- Carlson-class analytic function: integer values can identify the function only together with the required analyticity and growth hypotheses.
- Arbitrary prose/programs: a finite executable witness is generally a discriminator, not a proof of identity.

So the standing rule is:

> **same witness is evidence of rendezvous; same claim requires a declared uniqueness class or an explicit proof of equivalence.**

## 2. D10 correction — witness "iff" is false

The proposal

    two artifacts are the same claim iff they discharge the same witness

is false in general.

Counterexample: the single witness `f(3)=9` is discharged by both

    f(x) = x^2
    g(x) = x^2 + (x-3)

but the functions are different.

What the witness does establish unconditionally is one-way:

    different witness result  =>  definitely different under that witness

while

    same witness result  !=>  same claim

unless the declared class makes the witness uniquely determining.

This does not demote executable witnesses. It gives them the correct job: designation, regression, and discrimination.

## 3. D1 correction — the Gamma direction

The Carlson sketch contained a real analytic error:

    1 / Gamma((d+1)/2)

was said to decay vertically. It grows.

For d = sigma + i y, Stirling gives, up to polynomial factors,

    |1/Gamma((d+1)/2)| ~ exp(pi |y| / 4).

A two-point executable witness now records the direction numerically. It is a discriminator for the false sub-claim, not a proof of the full asymptotic.

The error does **not** by itself kill the Carlson route. The corrected exponential rate `pi/4` remains below the classical Carlson threshold `pi`. But the route is still OFFERED, not proved: analyticity on the intended half-plane, a correct vertical growth bound for the normalized continuation, and real-direction growth remain to be established. The earlier claim of polynomial growth on the real axis is withdrawn until proved.

The useful collision is this:

> Carlson's theorem is itself a uniqueness-class theorem.

The open continuation problem and the witness layer's missing field are therefore the same kind of object: identity is only available after the class and its uniqueness condition are stated.

## 4. Symmetric retrieval scars during the review

Two failures occurred while the witness proposal itself was being reviewed.

### 4.1 D7

The reviewing seat independently re-derived the 0/360-degree seam explanation for the impossible 11-lobe count and labeled it a hypothesis, although 051 had already recorded and settled that exact mechanism.

The result was stored and correct. The derived view carried the verdict but amputated the mechanism. Retrieval/claim identity failed.

### 4.2 D10

Greg attacked the stale `same witness iff same claim` formulation even though a corrected version already existed in another file in the same handoff folder.

Again, storage was not the failure. The reviewer saw one branch of the claim and not the newer one.

These are the same scar in opposite directions:

> **a claim can be present, nearby, and correct, yet epistemically absent from the review because the surface presented to the reviewer does not expose its identity or current branch.**

No branch is erased to repair this. The failures remain part of the record.

## 5. F9 candidate — bare sub-claims travel inside hedged containers

The Gamma error exposes a failure not captured by a four-word top-level status tag.

The Carlson passage was marked `SKETCH — not proved`, but the load-bearing sub-claim

    "1/Gamma((d+1)/2) decays vertically"

traveled through chat -> sealed review -> handoff as though the container's hedge covered the truth-status of every internal step.

It did not.

Candidate failure mode:

> **F9 — Hedged-container leakage.** A top-level uncertainty tag applies to the conclusion, while load-bearing internal sub-claims travel without their own status, witnesses, or provenance. The hedge makes propagation feel safe even when a false step is being relayed as fact.

Provenance chain for the specimen:

    Fable chat
      -> 069 §5
      -> Fable HANDOFF D1
      -> Greg adversarial walk
      -> correction

The conversation is therefore an unwired provenance surface: claims are born there before they enter the sealed archive.

## 6. Mechanical countermeasure — directional shadows

For a computable object, a directional/asymptotic word such as

    grows
    decays
    vanishes
    dominates
    bounded

should carry a cheap executable shadow before it travels when one is available.

The shadow is **not proof**. It is a discriminator.

The Gamma error is the first specimen: evaluating `|1/Gamma((d+1)/2)|` at two increasing imaginary parts immediately returns GROWS and would have killed the false word at origination.

Standing wording:

> **shadow the load-bearing step, not just the conclusion.**

This is especially useful inside SKETCH / OFFERED material, where the conclusion is intentionally unsettled but individual steps may still be falsifiable in seconds.

## 7. Sealing invariant — scripts beat recall

A separate process scar occurred while implementing the witness correction: a previously sealed file was edited, breaking its hash. The violation was caught by the hash check, the original was restored from the sealing commit, and the amendment was appended elsewhere.

This is the second documented instance of the same process failure: knowing the invariant did not prevent violating it; executing the check did.

Cheap repair, still a process requirement:

> **before sealing a new entry, verify every prior seal and refuse to continue if any prior folder is broken.**

The sealing moment is the guaranteed rendezvous point, so it is the right place to hang the sweep.

## 8. Status

| item | status |
|---|---|
| context-free claim identity | **REJECTED** |
| executable witness as universal `iff` identity test | **REJECTED** |
| executable witness as designation / regression / discriminator | **ADOPTED** |
| unit `(witness, predicate, class, sufficiency)` | **ADOPTED** |
| `ABSENT / NOT ESTABLISHED` allowed in sufficiency field | **REQUIRED** |
| `1/Gamma((d+1)/2)` decays vertically | **REFUTED** |
| corrected growth `~ exp(pi |Im d| / 4)` up to polynomial factors | **CHECKED / CLASSICAL STIRLING** |
| Carlson closes uniqueness | **OFFERED — NOT PROVED** |
| D7 seam explanation as new hypothesis | **RETRACTED — already settled in 051** |
| F9 hedged-container leakage | **CANDIDATE — one clear specimen, mechanism stated** |
| directional executable shadows | **PRACTICE PROPOSAL, one retroactive catch** |
| verify-all-prior-seals before a new seal | **PROCESS REQUIREMENT, not yet confirmed automated here** |

## 9. The line

> **Identity is always relative to a class. A witness tells us where to meet; a uniqueness theorem tells us whether we met the same thing.**

Nothing in this entry makes the derived view authoritative. The prior branches remain intact.
