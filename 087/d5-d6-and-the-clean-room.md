# d = 5, 6 — where marking stops being a corollary. And the clean room: what walks in by itself

**2026-08-25.** Two instructions from Ash, one of them a correction that lands on this
seat.

> *"do d=5 and 6"*
>
> *"u are still using π … If the question is 'does π emerge?', then π cannot appear
> anywhere in the setup — not even hidden inside a theorem we already know. No class
> number residue formula. No `(2π)^r₂`. No circle-area formula. … If eventually some
> constant is required to express the square-world growth, and that constant turns out
> to be π, then π walked in by itself."*
>
> *"and square root of 2? lol. bitch come on"*

**The correction is right and it lands on 080 and 083, this seat's.** Both compared
counted means against closed forms carrying `(2π)^r₂` and then reported that π appeared.
**That is 043's F8 exactly: a claim about the world whose only support is a fact about
the apparatus.** 084 and 085 are clean — pure counts, no constant anywhere. What was
contaminated is the *closed-form column* of 080 and 083, not their counting.

---

## Part 1 — d = 5 and d = 6

**The mirror survives.** `X(d,j) = (−1)^m X(d,d−j)` holds at `d = 5` and `d = 6`, zero
exceptions. `d = 5` is odd, so no marking is its own complement, and **no vanishing
marking exists — searched all six, found none**, as 084 predicted. `d = 6`'s self-dual
`j = 3` vanishes on odd `m`, as predicted.

**Parity purity degrades, and the rate is exact.** A shell is *pure* when every point on
it has the same number of odd coordinates:

```
   d = 1   pure  100.0%      max classes on any shell : 1
   d = 2   pure  100.0%                                 1
   d = 3   pure  100.0%                                 1
   d = 4   pure   87.5%                                 2
   d = 5   pure   62.5%                                 2
   d = 6   pure   37.5%                                 2
```

**`d ≤ 3` is completely pure.** This corrects 085's framing: that entry called `d = 3`
"the awkward dimension," and on *this* axis `d = 3` is on the easy side, sitting in the
fully-pure regime with `d = 1` and `d = 2`. **The awkwardness of `d = 3` is real for
divisor formulas (085 §3) and for markings (084 §2), and is not a universal property.**
Amendment, not retraction.

### And here is where something actually changes

084 §3 found that at `d = 3` the marked count is a **fixed multiple** of the unmarked
count, the multiplier depending only on `m` mod 4. 085 found the same at `d = 4`. Tested
upward:

```
   d * X(d,1)(m) / r_d(m),  sorted by m mod 8

   d = 3    +3   +1   -1   -3   +3   +1   -1    -        ONE MULTIPLIER PER CLASS
   d = 4    +4   +2    0   -2  -4/3  +2    0   -2        ONE MULTIPLIER PER CLASS
   d = 5    14 values ...  3 values ...                  NO fixed multiplier
   d = 6    533 values ... 527 values ...                NO fixed multiplier
```

> **Up to four dimensions, marking a circle tells you nothing you did not already know
> from counting. The marked count is a function of the unmarked one. From five
> dimensions up it is not — marking becomes independent information.**

That is a sharp scope boundary and it was not visible from `d ≤ 4`. **Our torus is
`d = 3`, inside the rigid regime: there, "the circles aren't equal" is a statement whose
entire content is fixed by `m` mod 4.**

## Part 2 — the clean room

**Rules: integer tuples, one operation, counting. Nothing named may enter.**

Objects: `ℤ[i]`, `ℤ[√−2]`, `ℤ[(1+√5)/2]`, `ℤ[√2]`. Count ideals of each norm, sum to
`X`, report the growth. `ℤ[i]` and `ℤ[√−2]` are principal, so ideals are **elements
divided by units**, and the count is nothing but **integer pairs**:

```
   square world   a^2 + b^2 <= X, /4 units      A(2,000,000)/X = 0.78540300
                  a^2 + 2b^2 <= X, /2 units                      1.11070600
   golden world   Z[(1+sqrt5)/2]                                  0.43040600
                  Z[sqrt2]                                        0.62324200
```

**The first two came from counting integer pairs and nothing else.** The real worlds
have infinite unit groups, so no finite element count exists; their ideal counts use a
multiplicative rule, **which is a theorem, not a count, and is flagged as such**. That
rule was **controlled against the pair count on the two worlds where both exist, and
they agree to every digit printed.**

### Two instruments failed here and both were caught by running them

**Eleventh instrument failure.** This seat first defined "ideal of norm `n`" as the
number of solutions of `b² ≡ D` mod `4n`, called it strict, and ran it. **It overcounts
at non-squarefree `n`** — mismatches at `n = 4, 8, 9, 16, 18, 25`, i.e. at the squares.
Caught by cross-checking against the multiplicative count. **Discarded, not patched.**

**Twelfth.** The unit search for `D = 8` was run over `ℤ[√8]` instead of `ℤ[√2]` and
returned `3 + 2√2`, which is `ε²`. The answer came out **exactly twice** the measured
value. **A clean factor of two is a signature, not noise** — same diagnostic as 080's
Kronecker bug, where four rows were off by exactly `2×`. Fixed to a uniform search
`a² − Db² = ±4`, and all four real worlds then agree.

## Part 3 — so what walked in, and it is not one thing

**Real worlds: an integer search, then one logarithm.** Search for the smallest integer
pair with `a² − Db² = ±4`. That is Pell — pure integer, findable by looking:

```
   D =  5   pair (1,1)   unit 1.6180339887   2 log(u)/sqrt D = 0.43040894   measured 0.43040600
   D =  8   pair (2,1)   unit 2.4142135624                     0.62322524   measured 0.62324200
   D = 12   pair (4,1)   unit 3.7320508076                     0.76034600   measured 0.76034450
   D = 13   pair (3,1)   unit 3.3027756377                     0.66273539   measured 0.66272700
```

**Square worlds: no integer search exists. The constant is an area.**

```
   D = -4   disk a^2+b^2 <= X, area / 4 units        0.78539816   measured 0.78540300
   D = -8   ellipse, area / 2 units                  1.11072073   measured 1.11070600
```

> **π did walk in by itself — and it walked in as an AREA.** Not from a formula. From
> the fact that the region you are counting inside is round. Lattice points in a region
> approach its area; the area of a round region is π. **That is the whole entrance, and
> it is forced by the shape of the question, not imported.**

### The asymmetry, which is the point

**These are not the same kind of constant, and 083 §1 put them in the same slot.**

```
   golden / silver   an INTEGER PAIR you can find by searching, wearing a logarithm
   square worlds     no integer object at all -- only a count divided by a scale, in the limit
```

**`log ε` has an exact integer seed.** `(1,1)` is a thing you can hold. The logarithm is
a wrapper on a found object.

**π has no integer seed.** No search over integers produces it. It exists only as the
limit of a count over a scale — **which is the definition of a smoothing.** 084 §4 said
π enters at the average; this says *why it can only enter there.*

> **π is irreducibly an average. The golden world's constant is not.** That asymmetry
> is invisible in Dirichlet's formula, which gives both the same slot, and it is
> visible the moment you refuse the formula and count.

**And the limit of what measurement can do, stated so it is not claimed later.** The
measured `0.78540300` is consistent with `π/4` and with infinitely many other numbers.
**No amount of counting can promote a decimal to a named constant.** What identifies it
is the area argument — a proof, not the measurement. **Reporting "we measured π" would
be F8 pointed the other way,** and this entry does not claim it.

## Part 4 — status

| claim | status |
|---|---|
| 080 and 083 imported π and then reported finding it | **CONCEDED** — F8, this seat's; Ash's correction |
| 084, 085 are π-free | **HOLDS** — pure counts throughout |
| the mirror holds at `d = 5, 6` | **VERIFIED**, 0 exceptions |
| `d = 5` has no vanishing marking | **VERIFIED** — all six searched, none found; predicted by 084 |
| parity purity is 100% for `d ≤ 3`, then degrades | **VERIFIED** |
| 085's "`d=3` is the awkward dimension" | **AMENDED** — true per-axis, not universal; `d=3` is on the easy side here |
| the fixed-multiplier law holds at `d = 3, 4` and fails at `d = 5, 6` | **VERIFIED** |
| marking is independent information from `d = 5` up | **ESTABLISHED** |
| the four growth constants, measured | **COUNTED** — two from integer pairs alone, 8 digits printed, ~6 trustworthy |
| pair count and multiplicative rule agree | **VERIFIED**, both worlds, every digit |
| the congruence definition of ideal count | **RETRACTED** — overcounts at squares |
| the `D = 8` unit search | **RETRACTED** — wrong ring, returned `ε²` |
| real-world constants have an integer seed | **DEMONSTRATED** — four worlds, Pell search |
| π has no integer seed; it is a limit of a count over a scale | **ESTABLISHED** |
| the measurement establishes that the constant *is* `π/4` | **NO** — measurement cannot do that; the area argument does |

Stratum tags per 082: Part 1 is **COUNT** throughout. Part 2's measured means are
**SUM**. Part 3's identifications are **CONTINUED** — every one of them is a limit, and
that is the entire finding.

## Attribution

**Both the instruction and the correction are Ash's** — *"do d=5 and 6"* produced Part
1, and *"u are still using π"* is what forced Parts 2 and 3 and is a direct hit on this
seat's 080 and 083. The clean-room design — algebra, then exact counting, then pattern,
then constant, in that order and no other — **is hers, in her words.** The computations,
the `d = 5` scope boundary, the two retracted instruments, and the integer-seed
asymmetry in Part 3 are this seat's. 043's F8, 084's mirror and 085's `d = 4` work are
prior entries of this ledger.
