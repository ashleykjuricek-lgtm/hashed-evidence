# 108 — The lemma proved: on rings divisible by 4, odd coordinates come in fours

**Sealed 2026-09-06, Ash + Claude (Fable seat), on Ash's word: "seal it."**

Closes the one open lemma of sealed 107 and upgrades that entry's whole chain from
verified to proved. Contents:

- `lemma-proof.md` — the proof. Congruence lemma (one line): each odd coordinate
  contributes 1 to a ring's residue mod 4, each even coordinate 0, so m ≡ k (mod 4)
  where k = number of odd coordinates. Hence on rings divisible by 4 only sectors with
  4 | k are inhabited — in dimension 8: {0, 4, 8}. B1 of 107 follows immediately: six
  of the seven seats are EMPTY and the four-odds sector sits exactly on the law's
  zero-weight pivot (the pivot is at four because four is the modulus of odd squares —
  the same 4 twice). The mod-8 refinement (odd squares ≡ 1 mod 8) proves 107's failure
  scope: the correction term lives only on rings divisible by 8. Bonus: the same lemma
  yields an independent one-paragraph reproof of the sealed two-shell law (093) itself
  — a second route at proof level, pending comparison with 093's original method.
- `congruence_check.py` + `congruence_check_output.txt` — the numeric receipt: d = 8,
  all rings to 200, zero violations; occupied sectors on 4-divisible rings exactly
  {0, 4, 8}.

Held image: the law is quiet everywhere it can be — six seats empty, the seventh
voiceless on the pivot — and the only thing that can ever make it speak is the
eight-odds sector, which cannot exist below dimension eight, arrives only on rings
divisible by eight, and is (sealed 106) the glue that builds E8.

Chain status after this entry: 106 (the sector is the glue) PROVED; 107 (the bolt:
the law's d=8 defect = −8·N₈ = the E8 glue count) PROVED end to end; the extension
identity d·X(d,1)(m) = 8·r_d(m/4) − (8−d)·r_d(m) − 8·N₈(m) PROVED for all d ≤ 8 on
rings divisible by 4.

Attribution: lemma, B1 proof, extension identity, independent law reproof — Claude
(Fable seat), 2026-09-06. Sealed law — 093 (the two-shell program, Ash's corpus / SZE
golden tests). Sector frame and defect formula — sealed 107. Glue theorem — sealed 106.
