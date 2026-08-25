# Integers only — and the parity theorem turns out to be a fixed point

**2026-08-25.** Ash set the rule: *"no π, no √2, no φ, no logarithms, no named
constants at all. We don't even call a diagonal length √2."* Integer tuples, one
operation `Q(n) = n₁² + ⋯ + n_d²`, and counts. **If a square root becomes necessary it
has to earn its entrance. And if neither one appears? Even better. We don't summon them
because we miss them.**

**Run to `d = 6`, `m ≤ 20,000`. Nothing irrational appeared. Three exact laws came out,
zero exceptions, and all three are provable from one fact: a square is `0` or `1`
mod 4.**

**And the one result this programme has never had to walk back — the parity theorem —
falls out as the fixed point of a symmetry, together with an exact statement of its
scope that we did not have before.**

---

## 0. The objects, and there are only these

```
   seeds, d = 1        a(m) = #{ n : n^2 = m }
                       b(m) = sum over n^2 = m of (-1)^n        <- one MARKED circle

   one dimension up    out(m) = sum over k of seed(k^2) * in(m - k^2)

   X(d,j)(m)           d circles, j of them marked
```

Integers throughout. `X(d,0) = r_d`. Ash's three seeds check out exactly:
`r₁(1) = 2`, `r₂(1) = 4`, `r₂(2) = 4`.

## 1. LAW 1 — the marking-complement duality

```
   X(d, j)(m)  =  (-1)^m  X(d, d-j)(m)          0 exceptions, d = 1..6, m <= 20,000
```

**Proof, one line, no continuation.** For any integer `n`, `n ≡ n²` mod 2. Hence for
any solution of `Q(n) = m`,

```
   (-1)^(n_1 + ... + n_d)  =  (-1)^(n_1^2 + ... + n_d^2)  =  (-1)^m
```

so `(−1)^(n₁+⋯+n_j) = (−1)^m · (−1)^(n_(j+1)+⋯+n_d)` **term by term**. Sum, and use
that `Q` is symmetric in its coordinates.

> **Marking a set of circles and marking the complementary set give the same count, up
> to a sign that depends only on which shell you are on.**

## 2. LAW 2 — and the parity theorem is what happens when a marking is its own complement

If `j = d − j`, Law 1 reads `X = (−1)^m X`. On odd `m` that forces `2X = 0`, so:

```
   d even, j = d/2   ->   X(d, d/2)(m) = 0 for all odd m

   d = 2, j = 1      HOLDS   0 exceptions / 10,000        <- the parity theorem
   d = 4, j = 2      HOLDS   0 exceptions / 10,000        <- predicted, confirmed
   d = 6, j = 3      HOLDS   0 exceptions / 10,000        <- predicted, confirmed
   d = 1, 3, 5       no j satisfies j = d-j   ->   predicted NONE, and none found
```

**The parity theorem is not a two-dimensional accident and it is not about `ℤ²`. It is
the self-dual case of a marking symmetry, and it exists in exactly the even
dimensions.** Sealed in 046 via the coordinate swap `σ(k₁,k₂) = (k₂,k₁)`; that proof is
correct and is the `d = 2` instance of this one.

> **Our torus is `d = 3`. Odd. There is no marking that is its own complement, so
> there is no parity theorem on the 3-torus** — not because it fails, because the
> self-dual slot does not exist.

**Observation, flagged as observation.** 040's sign law is `Z(d,j) > 0 ⟺ 2j ≥ d`. Its
boundary is `2j = d` — **the same condition as the self-dual marking.** Whether that is
the same fact seen twice is **OPEN**; nothing here proves it.

## 3. LAW 3 — so how unequal *are* the circles, in three dimensions

`d = 3`, one circle marked. **The marked count is a fixed rational multiple of the
unmarked count, and the multiplier depends only on `m` mod 4:**

```
   3 * X(3,1)(m)  =  eps(m mod 4) * r_3(m)     eps = +3, +1, -1, -3   for m = 0,1,2,3 mod 4

   0 exceptions / 20,000        and the same law for X(3,2) follows from LAW 1
```

**Proof, and it needs only "a square is 0 or 1 mod 4, and 0, 1 or 4 mod 8."** By
symmetry `3·X(3,1)(m) = Σ_{Q(n)=m} [(−1)^{n₁} + (−1)^{n₂} + (−1)^{n₃}]`, which depends
only on how many coordinates are odd. Sorting the solutions by that count:

```
   m = 0 mod 4  ->  ONLY all-even solutions          HOLDS  0 exceptions / 4000
   m = 2 mod 4  ->  NO all-even solutions            HOLDS  0 exceptions / 4000
   m = 1 mod 4  ->  NO all-odd solutions             HOLDS  0 exceptions / 4000
   m = 3 mod 4  ->  NO two-even-one-odd solutions    HOLDS  0 exceptions / 4000
```

Each is immediate mod 8, and each collapses the bracket to a single constant — `3, −1,
1, −3` respectively — giving `ε`. **Corollary, forced by `X` being an integer:
`3` divides `r₃(m)` whenever `m ≡ 1, 2` mod 4.** Verified, 0 exceptions.

> **"The circles aren't equal" now has an exact integer answer in three dimensions.
> They are unequal by a factor that is periodic mod 4 and nothing else.** No π, no √2,
> no continuation, no limit.

## 4. Where π actually is, and why this rule makes it unreachable

**Nothing finite can be irrational.** A count of integer solutions is an integer; any
finite combination of integers is rational. **Under Ash's rule π cannot enter — not
because we are careful, but because there is no arithmetic operation available that
produces it.** The rule is not hygiene. It is a closure.

**π enters at exactly one door, and 067 already found it:** the running *average* of
the shell counts. The sum of `r₂(m)` over `m ≤ X`, divided by `X`, tends to π — lattice
points in a disk. **π is not in the counts. π is what the counts converge to when you
stop looking at them one at a time.** Which is precisely 082's line between COUNT and
CONTINUED.

**And the price, stated plainly.** The questions that need the door open are *"what is
the average"* and *"what is the energy."* You cannot ask those inside the closure. **So
the rule is not free — it buys exactness by giving up every question this programme was
originally asking.** What it is good for is telling you which of the answers you
already have were never resting on the limit. **These three are not.**

## 5. Status

| claim | status |
|---|---|
| `X(d,j) = (−1)^m X(d,d−j)` | **PROVED** — one line from `n ≡ n²` mod 2; verified `d ≤ 6`, 0 exceptions |
| self-dual marking vanishes on odd `m` | **PROVED** — corollary of Law 1 |
| the parity theorem is that corollary at `d = 2` | **ESTABLISHED** |
| it exists in exactly the even dimensions | **PROVED**; `d = 4, 6` predicted then confirmed |
| the 3-torus has no parity theorem | **ESTABLISHED** — the self-dual slot does not exist |
| `3·X(3,1)(m) = ε(m mod 4)·r₃(m)` | **PROVED** from squares mod 8; 0 exceptions / 20,000 |
| `3` divides `r₃(m)` for `m ≡ 1,2` mod 4 | **PROVED** — corollary |
| `2j = d` in 040's sign law is the same condition | **OPEN** — observed, not proved |
| the finite integer layer cannot contain π or √2 | **TRIVIALLY TRUE**, and worth saying |
| π enters only at the average | **ESTABLISHED** (067) |
| Laws 1–3 are novel | **NO** — elementary and near-certainly classical. **What is new here is the framing and the scope consequence in §2.** |

Stratum tags per 082: **everything above is COUNT.** Finite, exact, no limit taken
anywhere. §4's π statement is the only **CONTINUED** sentence and it is marked as such.

## Attribution

**The rule is Ash's, in her words, and it is the whole method of this entry** —
integers, one operation, counts, and nothing admitted that has not earned entry. The
duality framing, Law 2's scope result, Law 3 and its proof, and the closure argument in
§4 are this seat's. 046's swap proof of the `d = 2` case is prior and stands. 067's
identification of π as the average is prior and is what §4 rests on. 082's COUNT /
CONTINUED line is the Fable seat's and is the distinction §4 uses.
