# The price has two parts — and the flat 3-torus is not in the π-free room

**2026-08-25.** Ash, on reading 080's nine-world table: *"because we aren't doing a
sphere torus."*

**Correct, and it breaks the table open.** Every one of 080's nine worlds is
**two-dimensional**. In two dimensions there are only two possibilities, so the price
*looks* binary — π, or a logarithm. It is not binary. **This entry counts the
three-dimensional case, finds a row that pays no π at all, and then finds that our
object is not in it.**

---

## 1. Amendment to 080 (not a retraction)

080 §2 wrote:

> `IMAGINARY discriminant -> a CIRCLE constant` / `REAL discriminant -> a UNIT's LOGARITHM`

**True, and true only for quadratic fields**, which is what 080 was about. **It is not
the general law, and it was written in a way that invites reading it as one.** The
general law:

```
   price  =  2^r1 (2 pi)^r2 h R / (w sqrt|d|)

       r1 = real embeddings          r2 = COMPLEX embedding PAIRS
       R  = a determinant of logarithms, of size (r1 + r2 - 1)
```

**π's exponent is `r₂`.** Not the dimension, not the symmetry — **the number of
directions that fold onto their own conjugate.** And the stretch price is not a
logarithm; it is a **determinant** of logarithms, whose size is the unit rank.

```
   shape                 r1 r2  rank   pi?   what R actually is
   imaginary quadratic    0  1    0    YES   the EMPTY determinant = 1
   real quadratic         2  0    1    no    ONE logarithm
   totally real cubic     3  0    2    no    a 2x2 DETERMINANT  -- an AREA of logs
   complex cubic          1  1    1    YES   one logarithm, times 2 pi
```

**Two dimensions has rank 0 or 1 — an empty determinant or a single number. That is
why 2D looks like a binary. It is a degenerate case of a determinant.**

## 2. Counted: three dimensions, and one row pays no π

Ideals of norm `m ≤ 2,000,000` in two cyclic cubic fields, `r₁ = 3`, `r₂ = 0`:

```
   Q(zeta_7)+   counted mean  0.30025300
                4 h R / sqrt(d)   0.30025982     R = 0.5254546821    ratio 0.999977
   Q(zeta_9)+   counted mean  0.37748350
                4 h R / sqrt(d)   0.37746109     R = 0.8492874506    ratio 1.000059

   splitting-rule cross-check (split/inert/ramified, and C(4,2)=6 at p^2):
                0 mismatches, both fields
   the same value WITH a factor of 2 pi:  counted/that = 0.1592 = 1/(2 pi), both fields
```

> **A three-dimensional world whose ring-price contains no π, counted twice.** The
> stretch price is a **2×2 determinant** — the area spanned by two independent
> logarithms, not the length of one.

## 3. And our object is not that row — Gauss says so

The flat 3-torus is `ℤ³` with the standard form. **Its shell counts are `r₃(m)`, and
Gauss determined them: they are class numbers of IMAGINARY QUADRATIC fields.**
Verified over every squarefree `m ≤ 3000`:

```
   m = 7 mod 8         r3(m) = 0                      (Legendre)
   m = 3 mod 8         r3(m) = 24 h(-m)  * 2/w
   m = 1,2 mod 4       r3(m) = 12 h(-4m) * 2/w

   1824 agreements, 0 mismatches
```

Class numbers computed independently, by counting reduced binary quadratic forms.

> **The counting layer of our three-dimensional object is two-dimensional, and it is
> the folding kind.** Three dimensions of geometry, counted by the worlds that close.
> **Being 3D does not buy you out of π. Our shells are priced in the π rows.**

**Scope, kept.** This is a statement about **the counts**. Whether π survives into any
particular derived quantity is separate and was answered separately: **064 showed π
cancels out of `R` entirely.** Count-level π and answer-level π are different
questions, and this entry settles only the first.

## 4. The two exceptions are 080's two worlds, and the factor is exactly `w`

The first run gave **1822 agreements and 2 mismatches — `m = 1` and `m = 3`**:

```
   m = 1  ->  d = -4   square      r3 = 6   vs 12 h = 12    off by 2
   m = 3  ->  d = -3   hexagonal   r3 = 8   vs 24 h = 24    off by 3
```

**`d = −4` and `d = −3` are the only two quadratic fields with `w > 2` in all of
number theory** — 080 §3's entire finding. `w = 4` and `w = 6`. **The correction
factor is exactly `w/2`, in both cases.** With `2/w` restored: **1824 of 1824, zero
mismatches.**

> **The only two exceptions to the law counting our lattice are the only two worlds
> with extra rotational symmetry, and the size of the exception is the amount of extra
> symmetry.** 080 was reached by counting ideals in nine fields. This was reached by
> counting lattice points in one. **They meet on the same two rows.**

## 5. What would have to change to reach the π-free room

The room exists — §2 counted it twice. Getting into it requires an object whose counts
come from a **totally real** field: **nothing folding, everything stretching, unit rank
2, price an area of logarithms.** `ℤ³` is not such an object and no marking changes
that, because `r₃` is fixed by the quadratic form, not by the boundary condition.

**That is a real constraint on the programme and it is worth having stated.** It says
where not to look.

## 6. Status

| claim | status |
|---|---|
| π's exponent is `r₂`, the count of complex places | **CLASSICAL** — Dirichlet |
| the stretch price is a determinant, size = unit rank | **CLASSICAL** |
| 080's binary framing is the 2D shadow of this | **AMENDED**, not retracted — 080 is true and scoped to quadratic |
| a 3D world pays no π: `Q(ζ₇)⁺`, `Q(ζ₉)⁺` | **COUNTED**, `m ≤ 2e6`, 4–5 digits, splitting rule 0 mismatches |
| `r₃(m)` is an imaginary-quadratic class number × `24/w` | **VERIFIED** 1824/1824, squarefree `m ≤ 3000` |
| the 2 exceptions are exactly `d = −3, −4` | **VERIFIED** — and the factor is exactly `w/2` |
| our lattice's counts are priced in π rows | **ESTABLISHED** at the count level |
| π therefore survives into our answers | **NO** — 064 showed it cancels from `R`. Different question. |
| `ℤ³` can be moved into the π-free room | **NO** — `r₃` is fixed by the form, not the marking |

Stratum tags, per 082: §2 and §3 are **COUNT** — finite, exact, no limit anywhere.
The residue means in §2 are **SUM** (absolutely convergent, no scheme chosen). Nothing
here is **CONTINUED**.

## Attribution

**The correction is Ash's** — *"we aren't doing a sphere torus"* is what identified
080's table as two-dimensional and its law as a special case. Dirichlet's formula,
Gauss's three-squares class-number law, and the `w > 2` classification are classical.
The counting, the two cubic verifications, the `r₃` check, and the identification of
the two exceptions as 080's two worlds are this seat's. 080's `w > 2` finding — which
§4 lands on from the opposite direction — is also this seat's, and 072's
two-occupant observation that started the whole thread came from the reviewing seat.
