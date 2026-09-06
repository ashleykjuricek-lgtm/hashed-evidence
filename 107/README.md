# 107 — The bolt: the sealed law's failure at d=8 IS the E8 glue count

**Sealed 2026-09-06, Ash + Claude (Fable seat), on Ash's word: "seal the bolt."**

This entry fastens sealed 106 ("the sector is the glue") onto sealed 093 (the two-shell
law) exactly. Contents:

- `bolt-report.md` — the result. In sector language the two-shell law is a balance
  among the odd-coordinate families, Σ_{k≥1}(4−k)·N_k(m) = 0 on rings divisible by 4.
  At dimension 8 the seven old families STILL balance (B1 — verified to ring 200,
  formal proof the one open lemma); the entire defect is the newcomer:
  defect(m) = −8·N₈(m), so the law still holds at d=8 on rings ≡ 4 (mod 8) — the
  golden test's failure scope explained, not just observed. Via 106,
  defect(8n) = −16·(240σ₃(n) − r_D8(2n)): **the amount by which the sealed law fails
  at dimension eight is a counting function of E8.** First failure ring: −2048 =
  −16 × 128, the glue's share of E8's 240 roots. Equivalent restatement: the law
  doesn't fail — it extends to all d ≤ 8 with correction term −8·N_all-odd.
- `bolt_check.py` — the verification, run against the engine's OWN golden-tested
  shell arithmetic (sze/spectral/shells.py), not a re-implementation. Claims B1–B3
  stated in the header before running.
- `bolt_check_output.txt` — the fresh run at sealing time: 25 rings printed, 50
  checked, ALL CHECKS PASS.

Honesty ledger: proved — the sector form (elementary), B2 given B1, B3 given B2 + 106.
Verified-not-proved — B1, exhaustively to ring 200; proof registered as the open lemma.
Nothing modifies 093, 106, or the golden tests; this is an addendum.

Attribution: sealed law and its d ≤ 7 proof — the two-shell program (093, Ash's corpus /
SZE golden tests). Sector reformulation, defect formula, extension statement, and
verification — Claude (Fable seat), 2026-09-06.
