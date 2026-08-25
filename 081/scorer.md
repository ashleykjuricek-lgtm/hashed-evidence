# Identity Gauntlet v1 — scorer

Score each returned case only against the hidden answer key in `identity-gauntlet-v1.md`.

Five binary dimensions per case:

1. Relevant retrieval
2. Node separation
3. Equivalence recognition
4. Uncertainty preservation
5. Provenance fidelity

Score each 0 or 1. Total 0–5 per case, 0–30 across six cases.

Also assign at most one primary failure code:

- ALIAS-MISS
- OVERLOAD-COLLAPSE
- RETRIEVAL-MISS
- STATUS-LEAK
- AUTHORITY-SHORTCUT
- SYMBOL-MECHANISM-COLLAPSE
- OVERRESOLUTION

Rules:

- Do not award equivalence recognition for a guessed equivalence with no supplied derivation.
- Do not award node separation if the response merely notes different notation but still compares incomparable quantities as though they were one object.
- Do not award uncertainty preservation when the response converts `OFFERED`, `OBSERVED`, `NOT ESTABLISHED`, or a bounded numerical check into proof.
- Do not punish a reviewer for refusing an identity packet whose sufficiency field is `NOT ESTABLISHED`.
- In the pi case, full credit requires separating literal numerical identity of pi from mechanistic identity of its appearances.

Record condition only after scoring the response if possible.

Primary comparison: mean total score for Condition B versus Condition A across fresh seats.

Do not interpret a single-seat win as evidence of general improvement.
