# One curve — and two errata against 047

**2026-08-23.** Follows 050. Ash: *"let's do it all."*

047 §B.2 noticed that a crossing appears when you vary the dimension and again when
you vary the shape, and flagged it **NOT ESTABLISHED** and **not investigated**. It
has now been investigated. The observation was right in spirit, **wrong in the
objects it compared**, and the corrected version is true — verified to sixteen
digits by two independent computations.

---

## 1. ERRATUM — 047 §B.2 compared zeros of two different functions

047 set side by side:

```
vary the DIMENSION :  zero at  d* = 2.6390688716830038646...
vary the SHAPE     :  zero at  b* = 1.0000297915619869892
```

and wrote *"the cube sits near a zero it is not on, in two independent
directions."*

**Those are zeros of different functions.**

- `d* = 2.639…` is where **`Z(d,1) = 0`** — the sign-change crossing of 042.
- `b* = 1.00003` is where **`24·R(3,b) − 1 = 0`**, i.e. where `R = 1/24`.

They are not two views of one phenomenon; they are two unrelated level sets. Worse,
`24R − 1` is not even defined away from three dimensions — the **24 is a
three-dimensional artefact**, so the quantity whose zero `b*` is cannot be
continued in `d` at all.

**Retracted.** Presenting two different functions' zeros as one object is the same
class of error as F8 and as KESTREL's `a₁`: a true statement about one thing read
as evidence about another.

## 2. The well-posed question, and its answer

Hold **one** function — `R(d,b) − 1/24` — and vary two things:

```
   dimension :  d'  with  R(d', 1) = 1/24        never computed before
   shape     :  b'  with  R(3, b') = 1/24        = 1.0000297915619869892  (047)
```

### 2.1 The merged solver

The 042 real-dimension continuation and the 047 anisotropic sum turn out to be the
same factorised theta with a different argument. On the `d`-torus with sides
`(1, b, b, …, b)` and the length-1 axis marked:

    Theta_A(t) = theta_A(t) * theta_P(t/b^2)^(d-1)          V = b^(d-1)
    Theta_P(t) = theta_P(t) * theta_P(t/b^2)^(d-1)

Real `d`, real `b`. Validated against **both** parents:

```
R(3, b=1) =  0.0416894146027238      042 ref  0.0416894146027238
R(2, b=1) = -0.103553390593274       042 ref -0.103553390593274
R(5, b=1) =  0.191188548061399       042 ref  0.191188548061399
R(1, b=1) = -0.5                     042 ref -0.5
24R(3,1)-1 = 0.000545950465370603    047 ref  0.000545950465371
24R(3,b*)-1 = -3.6e-19               047 b* is a zero here too
```

### 2.2 The new number

```
   d' = 2.99978241968328574
   3 - d' = 0.0002175803167
```

The dimension at which the ratio hits `1/24` exactly. Three dimensions overshoots
it by two parts in ten thousand.

### 2.3 The level set is one smooth curve

Tracing `R(d,b) = 1/24`:

```
      d              b on the curve            b - 1
   2.97            0.9958837751343122      -0.0041162249
   2.98            0.9972744132660724      -0.0027255867
   2.99            0.9986563945749757      -0.0013436054
   2.995           0.9993441616143225      -0.00065583839
   2.99978241968   1.0                      3.2e-27        <- (d', 1)
   3.00            1.000029791561987        2.9791562e-5   <- (3, b')
```

**The endpoint agrees with 047's independently computed `b*` to sixteen digits:**

```
047, dedicated anisotropic solver :  1.0000297915619869892
051, tracing the level set        :  1.000029791561987
```

Two different programs, two different parameterisations, same number.

> **Result. `(d', 1)` and `(3, b')` are two points on one smooth curve.**
> The cube's near-miss is a single geometric fact — the point `(3, 1)` lies off the
> curve `R = 1/24`, and `d'` and `b'` are that curve's two axis-intercepts near it.

The curve's slope at the cube, from five interior points:

```
   db/dd  ≈  0.13906, 0.13820, 0.13756, 0.13713, 0.13692   (approaching d = 3)
```

Smooth and slowly decreasing. And the ratio of the two misses **is** that slope:

    (b' - 1) / (3 - d')  =  2.979e-5 / 2.1758e-4  =  0.13692

which is not an extra fact — it is the same fact, which is exactly what "one curve"
means. **No closed form for the slope was sought and none is claimed.**

## 3. What this does and does not settle

**Does:** the "two independent directions" language is gone. There is one curve, one
distance from the cube to it, and two ways of measuring that distance. It also
means the March target `R = 1/24` is *reachable* — just not at three whole
dimensions with equal sides.

**Does not:** it says nothing about `d* = 2.639`, the zero of `Z(d,1)`. That is a
genuinely different level set and its relation to this curve, if any, is
**untested**. 042's result stands unchanged; only its pairing with `b*` in 047 is
withdrawn.

**Not claimed:** any interpretation of `d'` or `b'` as physical. They are where a
ratio meets a target, on a continuation whose uniqueness is still **NOT
ESTABLISHED** (042 §2).


## 4. The lobe width dissolves — it was a chosen parameter

045 listed *"what sets the lobe width — 8 deg of 36 for the decagon, 28 of 45 for
the octagon. No account of either"* as an open item, phrased as though the number
were a property of the tiling. It is not.

The shift magnitude `MAG` is a free parameter of the 022 recipe (022 chose
`1/phi^2 = 0.38197`). Sweeping it:

```
DECAGON (10-fold window)
    mag      lobes   width(deg)   duty      swing
   0.0500     10      28.750     0.7986   0.08336
   0.1000     10      31.250     0.8681   0.08336
   0.2000     10      15.250     0.4236   0.08363
   0.3820     10       8.250     0.2292   0.09639   <- 022
   0.5000     10       6.250     0.1736   0.10062
   0.7000     10      33.750     0.9375   0.56448
   0.9000     10      28.750     0.7986   0.64142

OCTAGON (8-fold window)
   0.0500      8      43.250     0.9611   0.00332
   0.3820      8      28.250     0.6278   0.26791   <- 022
   0.9000      8      10.250     0.2278   3.29023
```

> **The lobe COUNT is invariant** — exactly 10 and exactly 8 at every magnitude
> tested. **The lobe WIDTH is not** — it swings from 6.25 deg to 33.75 deg on the
> decagon, non-monotonically, a factor of five.

**045's open item is dissolved rather than answered.** There was nothing to
explain: the 8 deg is a fact about `MAG = 1/phi^2`, not about the Penrose tiling.
Anyone reading tile geometry off that number would have been reading back a
parameter someone chose in April.

What survives from 045 is the part that was tested against a control: the
direction-dependence itself is in the point set (it survives a **round** window),
and the ten-fold and eight-fold counts are stable under every deformation tried.

**Two caveats, stated rather than buried.**

- The "width" statistic is the extent above half-max, which only describes a
  *two-level* curve. At `MAG = 1/phi^2` the curve is cleanly two-level (045). Away
  from there it may not be, so the widths at other magnitudes may be describing a
  different shape rather than a wider lobe. **Not investigated.**
- There is a **regime change at `MAG` around 0.7**: the swing jumps from 0.10 to
  0.56 on the decagon and from 0.30 to 3.00 on the octagon, where the shifted
  window substantially leaves the original. Rows across that boundary should not be
  compared.

**Erratum on the instrument.** A first pass reported **11 lobes on a ten-fold
window**, which is impossible — the run detector split a lobe across the 0/360
seam. Its verdict was discarded rather than patched, and the sweep rerun with wrap
handling at 045's resolution. Every row above now reports the correct fold count,
which is what makes the width numbers usable at all.

## 5. ERRATUM — four sealed entries carry the wrong date

The day rolled over mid-session and was not noticed. Local seal times, from git:

```
   045   02:19  2026-08-22      header says 2026-08-22    ok
   046   02:51  2026-08-22      header says 2026-08-22    ok
   047   02:39  2026-08-23      header says 2026-08-22    WRONG
   048   04:30  2026-08-23      header says 2026-08-22    WRONG
   049   05:09  2026-08-23      header says 2026-08-22    WRONG
   050   05:52  2026-08-23      header says 2026-08-22    WRONG
```

The `hashes.txt` files are unaffected — the sealing script stamps real UTC — so the
**provenance chain is intact**. Only the human-readable dates in the prose of
047–050 are off by one day. Recorded here rather than edited there.

In a ledger whose entire function is *when did we know this*, the date is not
decoration. Noted also because it was found the same way as everything else useful
tonight: by checking instead of assuming.

## 6. Status

| claim | status |
|---|---|
| 047 §B.2 "two independent directions" | **RETRACTED** — different functions |
| merged (d,b) solver reproduces 042 and 047 | **VERIFIED**, both parents |
| `d' = 2.99978241968328574` | **COMPUTED**, new |
| `R(d,b) = 1/24` is one smooth curve through `(d',1)` and `(3,b')` | **COMPUTED** — endpoint agrees with 047 to 16 digits |
| slope `db/dd ≈ 0.1369` at the cube | **COMPUTED**; no closed form sought |
| relation of this curve to `Z(d,1) = 0` at `d* = 2.639` | **UNTESTED** |
| dates in 047–050 | **ERRATUM** — off by one day; hashes unaffected |
| lobe COUNT (10 and 8) | **INVARIANT** under every MAG tested |
| lobe WIDTH | **NOT INTRINSIC** — varies 6.25°–33.75° with a chosen parameter |
| 045's "what sets the lobe width" | **DISSOLVED**, not answered |
| whether the curve stays two-level away from MAG = 1/φ² | **NOT INVESTIGATED** |

## Attribution

Cubic-torus / Shunya-Zero programme. The question was asked by Ash — *"what do YOU
want to look at?"* — and the honest answer was the thing this seat had flagged as
not-investigated four hours earlier and walked past. Investigating it produced both
the result and the erratum against the entry that raised it.
