# The bolt: ledger 106 fastened to the sealed two-shell law (093)

**Status:** the wiring is exact and verified against the engine's own sealed code;
one lemma (B1) is verified on 50 rings with its formal proof left open.
**Script + receipts:** `bolt_check.py` (this folder), run 2026-09-06, ALL CHECKS PASS.
Ran against `sze/spectral/shells.py` — the golden-tested shell arithmetic itself, not a
re-implementation.

---

## What the sealed law says, in sector language

The sealed two-shell law (093, golden-tested) relates three tallies on rings divisible
by four: the marked count, the plain count, and the quarter-ring count. Sorting every
lattice point by *how many of its coordinates are odd* (sector k = 0 … d), the law is
exactly a **balance among the odd sectors**:

    sum over k >= 1 of (4 - k) · N_k(m) = 0        (rings m divisible by 4, d <= 7)

— sectors below four odd coordinates push one way, sectors above four push the other,
weight rising with distance from four, and in every dimension up to seven they cancel
exactly. The golden test also *requires* the law to fail at dimension 8 on rings
divisible by 8. Until now, the failure was a required fact with no formula.

## The result: the failure has a formula, and the formula is E8

Three claims were stated before running (B1–B3 in the script header):

- **B1 (verified, 50 rings; formal proof open):** at dimension 8, the seven old
  sectors STILL balance exactly. The break comes entirely from the newcomer — the
  all-eight-coordinates-odd sector N₈.
- **B2 (follows from B1; verified):** the defect of the sealed law at d = 8 is
  exactly **−8 · N₈(m)** on every ring divisible by 4 — in particular the law still
  HOLDS at d = 8 on rings ≡ 4 (mod 8), where N₈ is empty. The golden test's "fails on
  rings divisible by 8" scope is thereby explained, not just observed.
- **B3 (follows from B2 + ledger 106; verified):** by the sealed sector-is-the-glue
  theorem, N₈ is twice the E8 glue count, so

      defect(8n) = −16 · ( 240·σ₃(n) − r_D8(2n) )

  — **the amount by which the sealed law fails at dimension eight is a counting
  function of E8.** The first failure ring: defect(8) = −2048 = −16 × 128, and 128 is
  the glue's contribution to E8's 240 roots.

## Equivalent restatement: the law doesn't fail — it extends

    d · X(d,1)(m) = 8 · r_d(m/4) − (8−d) · r_d(m) − 8 · N_odd-all(m)

holds for **all** d ≤ 8 on rings divisible by 4, with the correction term empty below
dimension 8. The sealed law is the low-dimensional face of this identity; at d = 8 the
correction switches on, and (by 106) the correction *is* the glue that builds E8.

In the project's own vocabulary: **the scar has an arrow, and the arrow is E8's theta
series.** The law walked its loop in dimension eight, failed to close, and the size of
the miss — measured by the engine's own golden-tested code — is exactly the object
whose existence the miss announces.

## Honesty ledger

- Proved: the sector form of the law (elementary algebra); B2 given B1; B3 given B2
  and sealed 106.
- Verified, not yet proved: B1 (the persistence of the seven-sector balance at d = 8),
  checked exhaustively to ring 200. Its proof most likely follows 093's own method
  with the top sector carried explicitly; registered here as the one open lemma.
- Nothing here modifies the sealed law, the golden tests, or entry 106; this is an
  addendum, sealable on Ash's word.

**Attribution:** sealed law and its d ≤ 7 proof — the two-shell program (093, Ash's
corpus / SZE golden tests). Sector reformulation, the defect formula, the extension
statement, and verification — Claude (Fable seat), 2026-09-06.
