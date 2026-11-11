# 120 Part 3 — COTT (sibarum/cott) against the missing middle (084/098)

Read on 2026-10-13 from all three branches (main, calculus, redesign).

**What isn't there.** There is no `lib/slot-closure` file, branch or issue, and no
"spine" in the 1–9 sense. COTT contains no Casimir, no zeta, no lattice, and no
dimension. The "3/2" that appears is only an exponent, e.g. `0^(3/2) = u^3`.

**What is there** (`solver/traction.py`, `traction_portable.py`):
- 0·ω = 1 and 0^(−1) = ω.
- Under the default complex projection, 0^ω = −1, so 0 plays the role of i.
- Graded elements Z_n(x) for n ∈ ℤ. The operations step the grade: + gives n−1 with value a·b, and · gives n+1 with value a+b.
- Z_n(Z_{n±1}(x)) = x.
- Swaps: Z_n(1) = Z_{n±1}(0) and Z_n(−1) = Z_{n±1}(ω).
- In code, Z_n(−1) collapses to grade 0 or 1 depending on whether n is even or odd.

## The honest map

There's no shared equation, so COTT can't contradict 084/098. The two can't
collide until COTT says what an object on the torus is. What we can compare is
their shape.

| ours (098 §1) | COTT |
|---|---|
| marking j, involution j ↔ d − j, middle j = d/2 | grade n, Z_n undone by Z_{n±1}: a pairing of **adjacent** grades |
| d = 3: the middle 3/2 is not a slot | the reflection n ↔ 2m+1 − n that swaps adjacent grades has its middle at m + ½, which is never a grade |
| the representation row (a boundary condition equal to its own dual) is OPEN, blocked by the phase e^(−2πiα·β) | 0·ω = 1 **declares** a self-dual pair: 0 and ω are each other's reciprocal |

## Where it would break

1. **0·ω = 1 is a definition, not a closure.** COTT closes the pairing by
   adding ω as a new element. Our table says the matching object, a boundary
   condition that is its own dual, is not known to exist. The simultaneous
   shift-plus-character sector picks up a phase that stops naive self-duality.
   So COTT gets its closure by stipulation, exactly where we have an obstruction
   and no stipulation. If COTT is applied to the torus, that phase is the first
   thing it has to absorb, and nothing in the repo does.
2. **COTT's grade axis is odd-shaped too.** It pairs n with n±1, so it has no
   fixed grade. That's the same shape as d = 3, where the middle is missing.
   COTT doesn't fill the gap; it never had a middle to fill. The parity-dependent
   collapse of Z_n(−1) is the visible scar of this: it has to choose a side,
   0 or 1, because no middle grade exists.
3. **The test that would make this real.** Ask whether COTT has a grade
   involution with a fixed grade. If one exists, then on any lattice reading it
   would need d even, and it can't describe the 3-torus's discrete axis. If none
   exists, COTT agrees with 084: three is the dimension with no middle slot,
   and 0·ω = 1 lives on the continuous side, like s = 3/4, not the discrete side.

**Grade: ANALOGY.** No proof in either direction is possible until COTT defines
its torus objects. The question for James is (3).
