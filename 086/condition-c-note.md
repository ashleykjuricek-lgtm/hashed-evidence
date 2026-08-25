# Condition C — why COTT is being tested

**2026-08-25.** This note adds a third intervention to Identity Gauntlet v1. It does not claim COTT already solves claim identity or smoothing.

## The testable COTT residue

The early COTT bridge states totality and reversibility / no information loss as core principles. Later corrected COTT work records a direct carrier-closure failure: the assumed four-element carrier `{1,0,-1,omega}` does not remain closed once `-omega != 0`. The earlier derivation depending on four-element closure no longer typechecks; the carrier may need to be larger finite or infinite.

That history supplies a concrete anti-smoothing principle without relying on the retracted four-cycle story:

> **when exact operation leaves the assumed carrier, enlarge the carrier rather than coerce the output into an existing slot.**

This is the intervention tested as Condition C.

## Comparison

- **A — ordinary:** source materials + task.
- **B — identity packet:** A + `(witness, predicate, class, sufficiency)` packet.
- **C — closure by extension:** source materials + task + operational rule to preserve derivation path, extend the carrier/type when closure fails, and collapse only under licensed equivalence.

Condition C is intentionally separable from the rest of COTT. A positive result would support the closure-by-extension rule, not the full COTT programme.

## Primary COTT question

Does closure-by-extension improve **obstruction preservation** — especially on Case 7, where the exact surviving `exp(-2*pi*sqrt(2))` term does not belong to the preferred integer-power q carrier?

A successful C response should represent the failure as something like:

    carrier C_q = {q^n : n integer}
    operation / derivation produces x = exp(-2*pi*sqrt(2))
    x not in C_q
    obstruction = sqrt(2) not in Z
    action = extend carrier to include x
    forbidden action = coerce x to q^1, q^2, or an integer-power surrogate

## Interpretation

If C beats A and B on obstruction preservation, that is evidence for the intervention `closure by extension` in this corpus.

If it does not, COTT does not get credit merely because its vocabulary sounds appropriate.

Status: **READY, UNRUN.**
