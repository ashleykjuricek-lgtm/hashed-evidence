# d = 7 does not close — and the exception that survives unifies four separate findings

**2026-08-31.** Ash: *"do d=7."*

**Prediction refuted, this seat's.** 093 left *"`d = 7` closes the way `d = 5` does"* marked
**UNTESTED**, which was the correct status — but this seat then said aloud that it *should* close,
"since it's still under the `k = 8` ceiling." **It does not. `d = 7` closes 4 of 8 classes, the
worst of any dimension examined.**

**The four classes that do close, however, are held up by a single identity that also explains
085's `d = 4` result and 093's `d = 5` result. Four separate findings turn out to be one.**

---

## 1. `d = 7`, class by class

```
   m mod 8 | occupied k | 7 * X(7,1) / r_7      | status
   --------|------------|-----------------------|---------------------------
      0    |   {0,4}    |   16 values           | TWO-SHELL LAW holds
      1    |   {1,5}    | 2500 values           | OPEN
      2    |   {2,6}    | 2498 values           | OPEN
      3    |   {3}      |   +1                  | pure -> X = r_7(m)/7
      4    |   {0,4}    |    3 values           | TWO-SHELL LAW holds
      5    |   {1,5}    | 2500 values           | OPEN
      6    |   {2,6}    | 2500 values           | OPEN
      7    |   {3,7}    |   +21/37              | closed by the identity below
   -> 4 of 8 closed
```

**Only `m ≡ 3` mod 8 is parity-pure.** The `d = 7` purity is **1 of 8**, completing a sequence:

```
   pure classes out of 8 :   d<=3  8      d=4  7      d=5  5      d=6  3      d=7  1
                             i.e.  15 - 2d  for  4 <= d <= 7,  and it reaches 0 at d = 8
```

**Closure across dimensions:** `8, 8, 8, 6, 4` for `d = 3, 4, 5, 6, 7`. `d = 5` is not the last
easy case — it is the last *complete* one.

**Cross-checks, both as 084 predicts:** the mirror `X(7,j) = (−1)^m X(7,7−j)` holds for all `j`,
0 exceptions; and `d = 7` being odd, **no vanishing marking exists — all eight searched, none
found.**

## 2. The all-odd identity, and it absorbs four results

On the residue class mod 8 where all-odd solutions exist alongside exactly one companion class,
write `A` and `B` for the **ordered** counts (before the `C(d,k)` placement factor):

```
        B  =  2 A            all-odd is exactly TWICE its companion

   d=4, m=4 mod 8, companion k=0    HOLDS   0 exceptions / 2500
   d=5, m=5 mod 8, companion k=1    HOLDS   0 exceptions / 2500
   d=6, m=6 mod 8, companion k=2    HOLDS   0 exceptions / 2500
   d=7, m=7 mod 8, companion k=3    HOLDS   0 exceptions / 2500
```

**Every previously separate ratio is this one identity with a binomial coefficient in front:**

```
   d=4   N_4 / N_0 = 1*B / 1*A            =  2        085 sealed this as "N4 = 2 N0"
   d=5   N_1 / N_5 = C(5,1)A / B  = 5A/2A =  2.5      093 sealed this as "2 N1 = 5 N5"
   d=6   N_2 / N_6 = C(6,2)A / B  = 15A/2A=  7.5      087/093, previously unexplained
   d=7   N_3 / N_7 = C(7,3)A / B  = 35A/2A= 17.5      new here
```

> **085's `d = 4` finding, 093's `d = 5` finding, and the `d = 6` and `d = 7` ratios are not four
> facts. They are one fact seen at four dimensions, obscured each time by a different binomial
> coefficient.** 093 called the `d = 5` case *"mechanism not supplied, left OPEN."* **The mechanism
> is still not proved — but its scope is now known, and it is dimension-independent.**

**Still OPEN:** why `B = 2A`. In generating-function terms it is
`[θ_odd^d] = 2·[θ_odd^k · θ_even^(d−k)]` on the relevant class. **Verified four times, proved zero
times.**

## 3. Divisibility, forced by counting

`X(d,1)` is a sum of integers, so every fixed multiplier forces a divisor of `r_d`:

```
   d=5   m = 5 mod 8   ->   7  divides r_5(m)      0 exceptions / 2500
   d=7   m = 3 mod 8   ->   5  divides r_7(m)      0 exceptions / 2500
   d=7   m = 3 mod 8   ->   7  divides r_7(m)      0 exceptions / 2500
   d=7   m = 7 mod 8   ->   37 divides r_7(m)      0 exceptions / 2500
```

**`37 | r₇(m)` on `m ≡ 7` mod 8** comes from `X = 3·r₇(m)/37`, itself forced by
`N₇ = 2r₇/37`. **A prime with no geometric meaning in sight, produced by nothing but counting
integer points and requiring the answer be a whole number.**

## 4. Status

| claim | status |
|---|---|
| `d = 7` closes like `d = 5` | **REFUTED** — this seat's spoken prediction; 4 of 8, not 8 of 8 |
| 093 marked it UNTESTED | **CORRECT** — the ledger status was right; the sentence around it was not |
| `d = 7`: 4 of 8 classes closed | **VERIFIED** |
| pure classes `= 15 − 2d` for `4 ≤ d ≤ 7` | **VERIFIED** at four dimensions; reaches 0 at `d = 8` |
| closure sequence `8,8,8,6,4` for `d = 3..7` | **VERIFIED** |
| mirror holds at `d = 7`; no vanishing marking | **VERIFIED**, 0 exceptions — as 084 predicts for odd `d` |
| ordered all-odd `= 2 ×` ordered companion | **VERIFIED** `d = 4,5,6,7`, 0 exceptions each |
| it absorbs 085's `N₄=2N₀` and 093's `2N₁=5N₅` | **ESTABLISHED** — same fact, different binomial |
| why `B = 2A` | **OPEN** — verified four times, proved zero times |
| `37 \| r₇(m)` on `m ≡ 7` mod 8 | **VERIFIED**, forced by integrality |
| the four OPEN classes at `d = 7` | **UNRESOLVED** — `N₁/N₅` and `N₂/N₆` both take ~2500 values |

Stratum tags per 082: **all COUNT.** Finite, exact, no limit taken. No named constant appears.

## Attribution

The instruction is Ash's; the integers-only rule this rests on is hers. 084's mirror, 085's `d = 4`
law and 093's `d = 5` closure are prior entries of this ledger and are shown here to be instances of
one identity. The `d = 7` map, the purity formula, the unification, the divisibility corollaries and
the refuted prediction are this seat's.
