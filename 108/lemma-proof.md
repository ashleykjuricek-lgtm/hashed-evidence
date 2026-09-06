# The open lemma of 107, proved — and it closes the whole chain

**Status:** B1 is now PROVED (below, elementary and complete), upgrading every
"verified" in sealed 107 to "proved." The proof also yields a second, independent
one-paragraph derivation of the sealed two-shell law itself (two-method rule satisfied
at the level of proof, pending comparison with 093's original route).
**Companion receipts:** the numeric check of the key congruence (d = 8, all rings to
200: zero violations; occupied sectors on rings divisible by 4 are exactly {0, 4, 8})
run 2026-09-06; sealed 107's bolt_check output remains the consequence-level receipt.

---

## The congruence lemma (the whole proof lives here)

**Lemma.** For any point of ℤᵈ with squared length m and exactly k odd coordinates:

    m ≡ k (mod 4).

*Proof.* An odd square is 4j² + 4j + 1 ≡ 1 (mod 4); an even square is 4j² ≡ 0
(mod 4). Summing d squares, the remainder of m on division by 4 is the number of odd
coordinates. ∎

**Consequence.** On a ring divisible by 4, the only sectors that can be inhabited are
those whose k is itself divisible by 4. In dimension 8 that means k ∈ {0, 4, 8} — and
in every dimension below 8 it means k ∈ {0, 4}.

## B1, proved

**Claim (B1 of sealed 107).** In dimension 8, for every ring m divisible by 4:

    sum over k = 1..7 of (4 − k) · N_k(m) = 0.

*Proof.* By the lemma, N_k(m) = 0 for every k in 1..7 except possibly k = 4; and the
k = 4 term carries the coefficient 4 − 4 = 0. Every term vanishes individually. ∎

The balance does not hold because seven families cancel each other. It holds because
**six of the seven seats are empty and the seventh sits exactly on the pivot** — the
one interior sector that can be inhabited has no vote. And the pivot's position is no
accident: the law pivots at four because four is the modulus of odd squares. The same
4 twice.

(Note B1 as proved is stronger than 107 needed: it holds in every dimension, not just
d = 8, since sectors 1,2,3,5,6,7 are empty on 4-divisible rings in any ℤᵈ.)

## The chain, now proved end to end

With B1 proved, sealed 107's B2 and B3 upgrade from verified to proved:

- **The extension identity** (all d ≤ 8, rings divisible by 4):
  d·X(d,1)(m) = 8·r_d(m/4) − (8−d)·r_d(m) − 8·N₈(m),
  where the correction term N₈ is empty below dimension 8.
- **The failure scope**, proved not observed: an all-odd point in d = 8 has m ≡ 8 ≡ 0
  (mod 8) — the mod-8 refinement of the lemma (odd squares are 1 mod 8) — so the
  correction vanishes on rings ≡ 4 (mod 8) and the sealed law still holds there.
- **The E8 identification** (via sealed 106): defect(8n) = −16·(240σ₃(n) − r_D8(2n)).

## Bonus: an independent one-paragraph proof of the sealed law itself

For d ≤ 7 on rings divisible by 4, the lemma leaves only sectors k = 0 and k = 4.
Writing the marked count sector-wise, d·X(d,1)(m) = d·N₀(m) + (d−8)·N₄(m); and since
N₀(m) = r_d(m/4) (halving all-even points) while r_d(m) = N₀(m) + N₄(m), the
right-hand side 8·r_d(m/4) − (8−d)·r_d(m) equals d·N₀(m) + (d−8)·N₄(m) identically.
The two sides agree term by term. ∎ — This is a second, independent route to 093's
law (the original proof's method not compared here; if it differs, the two-method
rule is satisfied for the law itself).

## Plain version, one held image

Every odd coordinate tithes exactly one grain to the ring's remainder-of-four; even
coordinates tithe nothing. So a ring divisible by four can only host points whose odd
coordinates come in fours: no odds, four odds, or eight odds. The law's weights were
tuned — before anyone knew why — so the four-odds family stands exactly on the silent
pivot. Which leaves precisely one voice that can ever break the silence: the
eight-odds family, which cannot exist below dimension eight, arrives only on rings
divisible by eight, and is (sealed 106) the glue that builds E8. The law is quiet
everywhere it can be, and the only thing that can make it speak is E8 being born.

**Attribution:** lemma, B1 proof, extension identity, and the independent law proof —
Claude (Fable seat), 2026-09-06, at Ash's word ("the lemma — prove it"). The sealed
law is 093's (the two-shell program, Ash's corpus / SZE golden tests); the sector
frame and defect formula are sealed 107; the glue theorem is sealed 106.
