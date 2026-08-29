# d = 5 closes completely — and the multiplier law never died, it reached down one level

**2026-08-25.** Ash: *"do d=5."*

**087 said the fixed-multiplier law "fails at `d = 5`" and concluded that marking becomes
independent information from five dimensions up. The first half is true as stated. The second
half is wrong, and this entry retracts it.**

**`d = 5` is completely determined — all eight residue classes mod 8. What changes at `d = 5` is
not that the law fails but that it needs TWO shells instead of one.** And the two-shell law turns
out to be uniform in `d`, to contain 084's and 085's results as special cases, and to break at
exactly one place for exactly one reason.

---

## 1. `d = 5`, closed. Every class.

```
   m mod 8 | odd coords k | X(5,1)(m)
   --------|--------------|--------------------------------------
      1    |     {1}      |  + 3 r_5(m) / 5
      2    |     {2}      |  +   r_5(m) / 5
      3    |     {3}      |  -   r_5(m) / 5
      5    |    {1,5}     |  +   r_5(m) / 7        <- two classes, ONE multiplier
      6    |     {2}      |  +   r_5(m) / 5
      7    |     {3}      |  -   r_5(m) / 5
      0    |    {0,4}     |  [ 8 r_5(m/4) - 3 r_5(m) ] / 5
      4    |    {0,4}     |  [ 8 r_5(m/4) - 3 r_5(m) ] / 5

   8 of 8 classes closed.   two-shell law: 0 exceptions / 10,000
```

**Why `m ≡ 5` mod 8 closes despite holding two parity classes:** they are in an exact fixed ratio.

```
   2 * N_1(m) = 5 * N_5(m)      on m = 5 mod 8      0 exceptions / 5,000
```

`N₁/N₅ = 2.5` at every single shell. **Verified, mechanism not supplied** — in generating-function
terms it is the claim that `[θ_odd⁵] = 2·[θ_odd·θ_even⁴]` on that class. **Left OPEN.**

**Divisibility corollaries, forced by `X` being an integer:** `5 | r₅(m)` for `m ≡ 1,2,3,6,7` mod 8,
and **`7 | r₅(m)` for `m ≡ 5` mod 8.** The 7 has no counterpart at any other dimension examined.

## 2. The two-shell law, and it is uniform in `d`

```
   for  m = 0 mod 4 :

        d * X(d,1)(m)  =  8 * r_d(m/4)  -  (8 - d) * r_d(m)

   d =  1  2  3  4  5  6  7      0 exceptions / 5,000 each
   d =  8                        2,500 / 5,000 FAIL
   d =  9                        4,999 / 5,000 FAIL
```

**Derivation, in integers.** `d·X(d,1)(m) = Σ_k (d − 2k)·N_k(m)`, where `N_k` counts solutions with
exactly `k` odd coordinates. Squares are `0, 1, 4` mod 8, so `m ≡ 0` mod 4 admits only `k = 0` and
`k = 4` — **provided `k = 8` is impossible, which requires `d ≤ 7`.** Then `N₀ = r_d(m/4)` (halve
every coordinate) and `N₄ = r_d(m) − N₀`, giving the formula directly.

> **The scope is not a fitted range. `d ≤ 7` is exactly the condition that eight odd coordinates
> cannot occur, and at `d = 8` the law fails on precisely the half of shells — `m ≡ 0` mod 8 —
> where `k = 8` first becomes possible.**

### 2.1 It contains 084 and 085

```
   d=3   law gives 3X = 8 r_3(m/4) - 5 r_3(m);   084 sealed 3X = +3 r_3(m)
         agree iff r_3(m) = r_3(m/4)                       0 exc / 5,000

   d=4   law gives 4X = 8 r_4(m/4) - 4 r_4(m);   085 sealed X = (-1)^(m/4) r_4(m/4)
         agree iff r_4(m) = r_4(m/4)   on m=0 mod 8        0 exc / 2,500
              and r_4(m) = 3 r_4(m/4)  on m=4 mod 8        0 exc / 2,500
```

**Both sealed results are the two-shell law with a dimension-specific scaling identity substituted
in.** They were correct and they were special cases.

## 3. RETRACTION — 087's scope claim

087 §Part 1 sealed:

> *"Up to four dimensions, marking a circle tells you nothing you did not already know from
> counting. … From five dimensions up it is not — marking becomes independent information."*

**The first sentence stands. The second is FALSE at `d = 5`.** `X(5,1)` is fully determined by
`r₅` — at two shells rather than one. **Nothing about `d = 5` is independent.**

**What was actually measured in 087** was that `d·X(d,1)(m)/r_d(m)` is not single-valued per class
mod 8. True, and it is a statement about a *one-shell* description. **The conclusion drawn from it
reached past what the measurement covered** — the ledger's own F8, in the shape it takes when the
apparatus is a chosen basis rather than an instrument.

## 4. `d = 6`, stated precisely rather than assumed

```
   m mod 8 | k        | status
      0    | {0,4}    | TWO-SHELL LAW, 0 exceptions
      1    | {1,5}    | OPEN -- N_1/N_5 takes 1,257 distinct values
      2    | {2}      | X = 2 r_6(m) / 6
      3    | {3}      | X = 0                       <- a new vanishing
      4    | {0,4}    | TWO-SHELL LAW, 0 exceptions
      5    | {1,5}    | OPEN -- N_1/N_5 takes 1,250 distinct values
      6    | {2,6}    | X = 3 r_6(m) / 17           (forced by 15 N_6 = 2 N_2)
      7    | {3}      | X = 0                       <- a new vanishing
      -> 6 of 8 classes closed
```

> **087's claim survives at `d = 6`, but only on the odd shells, and only after the two-shell law
> is exhausted.** Two classes out of eight. **`X(6,1)(m) = 0` on `m ≡ 3, 7` mod 8** is a vanishing
> that is not the mirror's fixed point and was not predicted.

## 5. Status

| claim | status |
|---|---|
| `d = 5` is closed in all 8 classes mod 8 | **ESTABLISHED**, 0 exceptions |
| `2N₁ = 5N₅` on `m ≡ 5` mod 8 | **VERIFIED** 0/5,000; **mechanism OPEN** |
| `7 \| r₅(m)` on `m ≡ 5` mod 8 | **FORCED** by integrality of `X` |
| two-shell law, `m ≡ 0` mod 4 | **PROVED** from squares mod 8; verified `d = 1..7`, 0 exceptions |
| it fails at `d = 8` on `m ≡ 0` mod 8 | **VERIFIED** — exactly where `k = 8` first occurs |
| it contains 084's `d=3` and 085's `d=4` laws | **VERIFIED** via the scaling identities |
| 087: "marking becomes independent information from `d=5` up" | **RETRACTED** — false at `d = 5` |
| the same claim at `d = 6` | **HOLDS on 2 of 8 classes only** |
| `X(6,1) = 0` on `m ≡ 3, 7` mod 8 | **VERIFIED**; not the mirror's fixed point; **unexplained** |
| `d = 7` closes the way `d = 5` does | **UNTESTED** |

Stratum tags per 082: **all COUNT.** Finite, exact, no limit taken anywhere. No π, no √2, no named
constant appears in this entry.

## Attribution

**The instruction is Ash's**, and the integers-only rule this rests on is hers. 084's mirror and
085's `d = 4` law are prior entries of this ledger and are shown here to be special cases. The
`d = 5` closure, the two-shell law and its exact `d ≤ 7` scope, the `d = 6` map, and the retraction
of 087 are this seat's — and 087 is also this seat's, which is the point of §3.
