# Identity Gauntlet v1

**2026-08-25. Experimental protocol.**

Purpose: test whether a claim-identity packet improves fresh-LLM performance on documented failures in this corpus.

This is not an architecture claim. It is an intervention test.

## Hypothesis

A reasoner given ordinary project materials plus an explicit identity packet

    (witness, predicate, class, sufficiency)

will make fewer claim-identity / equivalence / retrieval errors than a reasoner given the same project materials without that packet.

## Conditions

### Condition A — ordinary

Give a fresh LLM seat only the source materials required for the case and the task prompt.

### Condition B — identity packet

Give a fresh LLM seat the same source materials and task prompt, plus a compact packet for each relevant claim:

    claim
    exact object / expression
    source / branch
    witness
    predicate
    declared class
    sufficiency: theorem / proof / not established

No extra explanatory prose beyond the packet.

## Blinding

- Use fresh seats with no access to this conversation or prior reviewer conclusions.
- Do not tell the seat which condition is expected to perform better.
- Do not include the answer key in the materials supplied to the seat.
- Score against the answer key only after the seat returns a response.

## Cases

### Case 1 — reciprocal-chart slope

Failure type: one human label, multiple mathematical nodes / charts.

Task: reconcile the reported slopes near the cube and state whether they disagree physically.

Ground truth:
- direct-lattice parameterization and side-length parameterization use reciprocal coordinates;
- the sign flip is a chain-rule effect under b -> 1/b;
- the volume-preserving deformation is a genuinely different deformation family;
- therefore not all reported slopes are the same derivative, and not all are contradictions.

Success requires:
1. identifying the parameterization distinction;
2. recognizing the reciprocal equivalence where applicable;
3. not collapsing the volume-preserving family into that equivalence;
4. not choosing a winner by chronology or source authority.

### Case 2 — dropped (1-q)

Failure type: one label, two expressions.

Task: determine whether `1 - 1/sqrt(2)` is the correct target for `eps1/q` when

    eps1 = q(1-1/sqrt(2))(1-q).

Ground truth:

    eps1/q = (1-1/sqrt(2))(1-q)

not the bare constant.

Success requires:
1. retaining the symbolic expression, not only its approximate value;
2. distinguishing the bare constant from the quotient;
3. explaining why dropping `(1-q)` changes the comparison.

### Case 3 — 2D alias

Failure type: different labels, same mathematical node.

Task: determine whether

    Z2_AA/Z2_PP

and

    R(2,2)

refer to the same object under the later R(d,j) notation.

Ground truth: yes, after the notation mapping is made explicit.

Success requires:
1. recovering the notation mapping;
2. recognizing the earlier result as antecedent rather than a new theorem;
3. not relying on title/date similarity alone.

### Case 4 — 11-lobe seam

Failure type: retrieval / mechanism amputation.

Task: determine whether the explanation for an impossible 11-lobe result is established, speculative, or absent.

Ground truth:
- the mechanism was already recorded in 051;
- the run detector split a lobe across the 0/360-degree seam;
- the bad verdict was discarded and the sweep rerun with wrap handling.

Success requires:
1. retrieving the earlier mechanism;
2. distinguishing `already established` from `fresh hypothesis`;
3. preserving the historical failed result as a scar rather than erasing it.

### Case 5 — Gamma/Carlson sub-claim

Failure type: false load-bearing sub-claim inside a correctly hedged sketch.

Task: evaluate the statement

    |1/Gamma((d+1)/2)| decays as |Im d| grows

and state what follows for the Carlson uniqueness route.

Ground truth:
- the reciprocal Gamma factor grows vertically, asymptotically like `exp(pi |Im d|/4)` up to polynomial factors;
- this refutes the directional sub-claim;
- it does not by itself refute Carlson, because the corrected exponential rate remains below pi;
- the Carlson route remains unproved pending the other growth/analyticity conditions.

Success requires:
1. correcting the Gamma direction;
2. not upgrading the numerical shadow to a proof of the full asymptotic;
3. not killing or proving Carlson merely from this correction.

### Case 6 — pi identity trap

Failure type: same literal constant, different mathematical roles.

Task: classify the appearances of pi in the supplied materials and determine which are the same object versus the same mechanism.

Minimum supplied examples:
- `q = exp(-2*pi)` in the cubic-torus nome / shell scale;
- `Gamma(-1/2) = -2*sqrt(pi)` and Stirling/Gamma prefactors;
- `(2*pi)^r2` in the Dirichlet class-number formula for imaginary quadratic fields;
- ordinary geometric circumference/area appearances of pi;
- any claim that `pi` is "the door", "the smoothing", or otherwise a single shared mechanism must be treated as interpretation unless an explicit derivation identifies the mechanisms.

Ground truth:
- the literal constant pi is the same mathematical number in all cases;
- the *roles and mechanisms are not thereby identical*;
- equality of symbol/value is insufficient to infer common causal/structural origin;
- a same-mechanism claim requires an explicit map/derivation connecting the appearances.

Success requires:
1. separating numeric identity from mechanistic identity;
2. identifying the role in each formula;
3. refusing to merge mechanisms from symbol reuse alone;
4. allowing a proven relation where one actually exists.

This case is deliberately included because the corpus repeatedly treats recurring constants as possible structural hinges. The gauntlet must distinguish a real shared derivation from a repeated symbol.

## Scoring

Score each case on five binary dimensions:

1. **Relevant retrieval** — found the prior claim/mechanism needed for the task.
2. **Node separation** — did not collapse distinct objects into one.
3. **Equivalence recognition** — recognized equivalent representations when justified.
4. **Uncertainty preservation** — did not invent a resolution / theorem not established by the materials.
5. **Provenance fidelity** — attributed the result to the correct antecedent/branch and did not let a summary overwrite the source history.

Per case: 0–5.
Total per condition across six cases: 0–30.

Also record one qualitative failure code when applicable:

- ALIAS-MISS — same node under different names not recognized
- OVERLOAD-COLLAPSE — different nodes sharing a label collapsed
- RETRIEVAL-MISS — relevant stored evidence not surfaced
- STATUS-LEAK — container status substituted for step-level checking
- AUTHORITY-SHORTCUT — newest/primary/status label treated as truth by itself
- SYMBOL-MECHANISM-COLLAPSE — same symbol/value treated as proof of same mechanism
- OVERRESOLUTION — unresolved alternatives flattened into one answer

## Primary outcome

Difference in total score between Condition B and Condition A.

Secondary outcomes:
- error-type distribution;
- which cases show no benefit;
- whether packets introduce new failure modes;
- whether `sufficiency = NOT ESTABLISHED` reduces overresolution.

## Interpretation rule

Do not declare success from one seat.

A useful first pass is at least three fresh seats per condition. The protocol remains informative even if the sample is small, but any claim stronger than `observed in this gauntlet` requires replication.

If Condition B does not outperform A, do not add more metadata by default. Identify which field failed or remove the packet.

## Status

Protocol: **READY, UNRUN.**

No result is claimed until fresh seats complete both conditions.
