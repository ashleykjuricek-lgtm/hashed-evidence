# d = 4 — the mirror's fixed point is the whole object at half scale

**2026-08-25.** Ash: *"do d=4 and see what the mirror does there."*

084 found the marking mirror `X(d,j) = (−1)^m X(d,d−j)` and showed its fixed point
`j = d/2` kills the odd shells. **It does something else on the even shells, and this
is what `d = 4` was needed to see: the fixed point reproduces the entire lattice at
half the shell number.** Verified `d = 2, 4, 6`, zero exceptions, and proved in
integers with no theta function anywhere.

**Second finding, unforced by the mirror: a marking that is NOT self-dual also
vanishes — on one residue class.** And **third: `d = 4` is easy in a way `d = 3` is
not.**

---

## 1. The mirror halves the object

```
   d even, j = d/2 :     X(d, d/2)(2k) = (-1)^k * r_d(k)

      d = 2   0 exceptions / 10,000        <- this is 046's character law
      d = 4   0 exceptions / 10,000
      d = 6   0 exceptions / 10,000
```

**Proof, integers only.** Marking is per-coordinate, so `X(d,j)` is the additive
convolution of `j` marked seeds and `d−j` unmarked ones. Pair them off:

```
   X(d, d/2)  =  ( b * a ) convolved d/2 times  =  X(2,1) convolved d/2 times
```

**Verified directly, 0 exceptions, all three dimensions.** Then use the `d = 2` case —
`X(2,1)` is zero on odd `m` and `(−1)^k r₂(k)` on `m = 2k`, which is 046 — and the fact
that `r₂` convolved `d/2` times is `r_d`. The `(−1)` factors collect to `(−1)^k`
because the indices sum to `k`. Done.

> **Marking half the circles is not a new object. It is the same object, seen at half
> the shell number, with the sign alternating.** The odd shells vanish because a
> half-scale copy has nothing to stand on there.

**This is the Jacobi duplication that 039 and 046 used, stated in integers for every
even dimension at once, with no theta function and no continuation.** Those entries
reached it through `θ₃θ₄ = θ₄(q²)²`; the identity is the `d = 2` shadow of a
convolution.

## 2. `d = 4`, one circle marked — closed completely

```
   m = 1 mod 4      X(4,1)(m) =  + r_4(m)/2  =  + 4 sigma(m)
   m = 3 mod 4      X(4,1)(m) =  - r_4(m)/2  =  - 4 sigma(m)
   m = 2 mod 4      X(4,1)(m) =  0                          <- A SECOND VANISHING
   m = 0 mod 4      X(4,1)(m) =  (-1)^(m/4) * r_4(m/4)

   every line: 0 exceptions, m <= 20,000
```

**The `m ≡ 2` mod 4 vanishing is not the mirror.** `j = 1` is not self-dual at `d = 4`.
It vanishes for a different reason, visible in the parity decomposition below: on those
shells both of the classes that contribute to `X(4,1)` are empty at once.

**Why, in integers.** Sort every solution by how many of its four coordinates are odd —
call the counts `N₀ … N₄`. Then `4·X(4,1) = Σ (4 − 2k) N_k`. Squares are `0, 1, 4`
mod 8, which empties almost every class:

```
   N0 (all even) = 0  unless  m = 0 mod 4        0 exceptions / 15,000
   N4 (all odd)  = 0  unless  m = 4 mod 8        0 exceptions / 17,500
   N1 = 0 when m = 3 mod 4                       0 exceptions /  5,000
   N3 = 0 when m = 1 mod 4                       0 exceptions /  5,000
   N2 = 0 when m = 0 mod 4                       0 exceptions /  5,000
   N0(m) = r_4(m/4) for m = 0 mod 4              0 exceptions /  5,000
```

> **For every `m` except `m ≡ 4` mod 8, exactly ONE of the five parity classes is
> occupied.** The shell is parity-pure. `m ≡ 4` mod 8 is the only shell type where two
> classes coexist — all-even and all-odd — and there,

```
   N4(m) = 2 * N0(m)          0 exceptions / 2,500
```

which is what produces the minus sign in the `m ≡ 0` mod 4 line: `N₀ − N₄ = −N₀`.

## 3. `d = 4` is easy. `d = 3` is not. Ours is 3.

In pure divisor language, with no constant of any kind:

```
   d = 1   r_1(m) = 2 if m is a square, else 0                        0 exceptions
   d = 2   r_2(m) = 4 (#divisors = 1 mod 4  -  #divisors = 3 mod 4)   0 exceptions
   d = 4   r_4(m) = 8 * (sum of divisors NOT divisible by 4)          0 exceptions
   d = 3   NO elementary divisor formula. r_3 needs class numbers.    (083, Gauss)
```

**`d = 5` and `d = 6` untested here; nothing is claimed about them.**

> **Three is the awkward dimension, and every direction we have looked has said so.**
> 083: three-dimensional shells are counted by imaginary-quadratic class numbers — the
> rows that pay π — while four-dimensional shells are a bare divisor sum. 084: odd
> dimensions have no self-dual marking, so no parity theorem. Here: `d = 1, 2, 4` have
> elementary divisor formulas and `d = 3` does not.
>
> **`d = 3` is not hard because we have been unlucky with it. It sits between two easy
> dimensions and is excluded from what makes each of them easy.**

## 4. Status

| claim | status |
|---|---|
| `X(d,d/2)(2k) = (−1)^k r_d(k)`, `d` even | **PROVED** — convolution route; verified `d = 2,4,6`, 0 exceptions |
| `X(d,d/2)` is `X(2,1)` convolved `d/2` times | **PROVED**, verified directly, 0 exceptions |
| this is Jacobi duplication for all even `d` at once | **ESTABLISHED** — 039/046 had the `d = 2` shadow |
| `X(4,1)`, all four residue cases | **PROVED** from squares mod 8; 0 exceptions / 20,000 |
| `X(4,1)(m) = 0` on `m ≡ 2` mod 4, and NOT from the mirror | **ESTABLISHED** |
| every shell is parity-pure except `m ≡ 4` mod 8 | **VERIFIED**, 0 exceptions |
| `N₄ = 2N₀` on `m ≡ 4` mod 8 | **VERIFIED**, 0 exceptions / 2,500 |
| `r₄ = 8·(divisor sum)`, `r₂ = 4·(divisor difference)` | **VERIFIED** — classical (Jacobi) |
| `d = 3` has no elementary divisor formula | **ESTABLISHED** (083) |
| `d = 5, 6` behave the same way | **UNTESTED** — not claimed |
| these identities are novel | **NO** — all classical. **New here: the mirror framing, and §3's convergence of three independent reasons that `d = 3` is the excluded one.** |

Stratum tags per 082: **all COUNT.** Finite, exact, no limit taken anywhere. No π, no
√2, no named constant appears in this entry.

## Attribution

**The instruction is Ash's and is the whole entry** — *"do d=4 and see what the mirror
does there"* is what produced §1. The mirror itself is 084; the `d = 2` character law
is 046; the class-number obstruction at `d = 3` is 083; Jacobi's two-, four-square
theorems and the duplication identity are classical. The convolution proof, the
complete `X(4,1)` law, the parity-purity observation, and §3 are this seat's.
