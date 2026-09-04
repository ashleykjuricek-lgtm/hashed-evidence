# W3 — The sector is the glue

**Registered:** round-4 memo, work item W3 (candidate claim, stated before checking)
**Status:** PROVED (short exact proof below) + verified numerically on 12 rings by two
independent methods (`w3_check.py`, output reproduced at the end; ALL CHECKS PASS)
**Content note:** every ingredient is classical lattice theory (the D8→E8 glue
construction and Θ_E8 = E4 are textbook — Conway & Sloane, *Sphere Packings, Lattices
and Groups*, ch. 4). What is new here is the **identification**: the sector that the
sealed two-shell counting law watches open at dimension 8 *is* the classical glue.
This answers the working brief's Question 14 for one exact statement: shared theorem,
not analogy.

---

## Theorem (the sector is the glue)

Work in ℤ⁸. Let A(n) be the number of points with **all eight coordinates odd** and
squared length n — the sector the two-shell decomposition watches open at dimension 8.

**(a)** A(n) = 0 unless n is divisible by 8.

**(b)** Halving every coordinate maps the all-odd points of squared length 8m
bijectively onto the half-integer points of squared length 2m; and the half-integer
points split into exactly two families — coordinate sum ≡ 0 (mod 4) versus ≡ 2 (mod 4)
before halving — which are precisely the two glue cosets D₈ + g and D₈ + g′
(g = the vector of eight halves, g′ = g with one sign flipped). Each family, glued to
the checkerboard lattice D₈, produces a copy of E₈ (the two copies are mirror images,
swapped by flipping one coordinate's sign; hence the families are equal in size on
every ring).

**(c)** Consequently, for every m ≥ 1:

    A(8m) = 2 · ( r_E8(2m) − r_D8(2m) ) = 2 · ( 240·σ₃(m) − r_D8(2m) )

— the all-odd count on ring 8m is exactly twice the number of glue vectors E₈ adds to
the checkerboard at norm 2m, and 240·σ₃(m) is E₈'s classical shell count (sum of cubes
of the divisors of m, times 240).

## Proof

**(a)** Every odd square leaves remainder 1 on division by 8. Eight of them sum to
remainder 8, i.e. 0. ∎

**(b)** A point has all coordinates odd exactly when half of it has all coordinates in
ℤ + ½; squared lengths divide by 4. Every half-integer point is uniquely g + v with v
integral; sorting by the parity of v's coordinate sum splits the half-integer points
into D₈ + g (sum even) and D₈ + g′ (sum odd, since g′ = g − e₈ shifts the parity by
one). The construction E₈ = D₈ ∪ (D₈ + g) is the standard index-2 glue extension: the
coset's squared lengths |g+v|² = 2 + Σvᵢ + |v|² are even because Σvᵢ and |v|² always
share parity, and the extension is even and unimodular. Negating the last coordinate is
an isometry of ℤ⁸ that fixes D₈, carries g to g′ (hence one glued copy to the other),
and preserves every ring — so the two families are isometric copies of the same glue
and have equal counts on every ring. The sum-mod-4 bookkeeping: unhalved, the
coordinate sum is 8 + 2·(Σvᵢ), which is ≡ 0 (mod 4) exactly when Σvᵢ is even. ∎

**(c)** E₈ is the disjoint union of D₈ and its glue coset, so on every even ring the
glue count is r_E8 − r_D8; there are two such families in the all-odd sector, and
Θ_E8 = E₄ gives r_E8(2m) = 240·σ₃(m) (classical). ∎

## Corollary (both "why eight"s are the same remainder computation)

In dimension d, the all-odd sector of ℤᵈ lives on rings with remainder d mod 8 (d odd
squares, each remainder 1). It lands on rings divisible by 8 **exactly when d is a
multiple of 8**. On the lattice side, the glue vector of d halves has squared length
d/4, and the glued lattice D_d ∪ (D_d + g) is an *even* lattice exactly when d/4 is
even — again d ≡ 0 (mod 8). So:

- the two-shell law's sector opening at d = 8 on rings divisible by 8, and
- the existence of an even unimodular lattice (E₈) first at dimension 8,

are the **same residue-mod-8 fact** read on two sides of the halving bijection.
"Seven is before the loop closes" and "E₈ cannot exist below dimension eight" are one
sentence. Eight odd squares, each leaving remainder one, complete a turn of eight.

## Plain-language statement (the held image)

The checkerboard lattice is the grid points whose coordinates sum to an even number.
E₈ is that checkerboard **plus a ghost population** living at the half-steps between
grid points. Our all-odd sector — the new species of solution that appears for the
first time in dimension 8 — is that ghost population, seen at double scale. And the
ghosts come in two equal mirror families (chirality: flip one sign and the families
swap — the cancellation-powered-by-a-mirror motif, again). Below dimension eight the
ghosts land on odd-length rings and no even crystal can absorb them; at eight, for the
first time, they land on even rings — and E₈ snaps into existence. The sector didn't
just open *at* dimension 8. The sector opening **is** E₈ becoming possible.

## Numeric receipts (two methods, 12 rings, all pass)

Method 1: direct enumeration of all-odd points (with the chirality split and an
independent half-integer-side enumeration of the cosets). Method 2: the classical
closed form 2·(240σ₃(m) − r_D8(2m)) with r_D8 enumerated separately.

```
 m | ring 8m | A(8m) all-odd | per coset | 240*sigma3(m) | r_D8(2m) | 2*(E8-D8) | match
 1 |      8 |          256 |       128 |          240 |      112 |       256 | YES
 2 |     16 |         2048 |      1024 |         2160 |     1136 |      2048 | YES
 3 |     24 |         7168 |      3584 |         6720 |     3136 |      7168 | YES
 4 |     32 |        16384 |      8192 |        17520 |     9328 |     16384 | YES
 5 |     40 |        32256 |     16128 |        30240 |    14112 |     32256 | YES
 6 |     48 |        57344 |     28672 |        60480 |    31808 |     57344 | YES
 7 |     56 |        88064 |     44032 |        82560 |    38528 |     88064 | YES
 8 |     64 |       131072 |     65536 |       140400 |    74864 |    131072 | YES
 9 |     72 |       193792 |     96896 |       181680 |    84784 |    193792 | YES
10 |     80 |       258048 |    129024 |       272160 |   143136 |    258048 | YES
11 |     88 |       340992 |    170496 |       319680 |   149184 |    340992 | YES
12 |     96 |       458752 |    229376 |       490560 |   261184 |    458752 | YES
ALL CHECKS PASS
```

Sanity anchors: ring 8 gives 256 (the ±1 hypercube corners) = 2 × 128, and 128 is
exactly the glue's contribution to E₈'s 240 roots (112 from the checkerboard + 128
ghosts = 240, the number on everyone's E₈ poster).

## What this upgrades, and what it does not

**Upgrades:** the brief's §10 comparison ("E₈ = clean self-dual closure vs. our
imperfect closure") acquires its first exact shared statement; E₈'s theta series now
computes a sealed counting object of this project (the d = 8 sector), and the sector's
counting function is 2·(240σ₃(m) − r_D8(2m)) in closed form.

**Does not claim:** any novelty in lattice theory (all classical); any statement about
the sealed two-shell identity's precise algebraic form, which is not restated here —
wiring this theorem into that identity verbatim is the natural follow-up. And it makes
no physical claim of any kind.

**Attribution:** sector and its d = 8 opening — the sealed two-shell program (Ash's
corpus / the SZE golden tests); identification with the glue, proof, corollary, and
verification — Claude (this seat), 2026-09-04; classical ingredients — Conway–Sloane.
