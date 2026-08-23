# Reading 028 again — two vindications and two scars

**2026-08-23.** Follows 052. Ash produced the 2026-06-20 paper. Checking it against
everything from 21–23 August turns up four things: **two numbers that were retired
and should not have been, and two places where we failed to read our own paper.**

---

## 1. VINDICATED — 028's anisotropic numbers are all correct, every digit

KESTREL (2026-08-23) called the scar page's slope of `+18.3` and crossing at
`b₀ ≈ 0.99997` *"fitted guesses,"* *"wrong sign and magnitude,"* *"wrong side,"* and
replaced them with `−27.49` at `b* ≈ 1.00002`. 048 concluded both were correct for
different deformation families.

**048 understated it. It is not even a different family.**

028 App A.3 writes `Q = (n₁+a₁)² + b²((n₂+a₂)² + (n₃+a₃)²)` — the transverse axes
carry `b²`, where our 047 sides `(1,b,b)` put `1/b²` there. **028's `b` is our
`1/b`: the same family, reciprocally parameterised.** Recomputing 028's §7.1 table
in 028's own convention:

```
   b        eps            eps/q          028 printed
  0.92   -1.523464467    -815.80251      -1.5235 / -815.8
  1.00    0.0005459505      0.29235192    +0.00054595 / +0.2924
  1.08    1.414162348      757.27214      +1.4142 / +757.3

  d eps/db at b=1  =  18.3259647484        028 says "~ +18.3"
  zero             =  0.999970209325523736 028 says "~ 0.99997"
```

And the reciprocal of our own independently computed `b*`:

```
   1 / 1.0000297915619869892  =  0.999970209325523736     <- identical
```

**Every number 028 printed is correct to every digit it printed.** The slope was
not a placeholder — it came from a validated anisotropic Ewald in App A.3, computed
in June. `b₀ = 0.99997` is not the wrong side; it is `1/b*`.

> **The retirement of these two numbers should be reversed, and the reason is
> stronger than 048 gave: they were computed, published, and right.**

**Standing rule, strengthened from 048 §4:** a slope or a crossing in this
programme is meaningless without both its deformation family **and its
parameterisation** printed beside it. Reciprocal conventions flip the sign and move
the crossing to the other side of 1, and two correct calculations then look like a
contradiction.

## 2. VINDICATED — the coset identity, to 25 digits

028 §6: `Z_PPP + 6 Z_APP + 6 Z_AAP + 2 Z_AAA = 0` at `s = −1/2`.

```
   Z_PPP -0.266596278718393     Z_APP -0.0111142427950344
   Z_AAP  0.0347814624899515    Z_AAA  0.0622964802744454
   total  9.90355e-25
```

Holds. This is the `(1,6,6,2)` relation, unchanged and unchallenged.

## 3. SCAR — 028 §6 already had both 2D closed forms, in June

039 §1 was written as a discovery: *"where 1 − 1/√2 actually came from,"* crediting
a July real-math-ledger line and reporting the closed forms as newly established.

**028 §6, 2026-06-20, states both of them outright**, under the heading *"Proven
structural context (classical)"*:

> **2D closed forms (prime-2 Euler factor):** `Z2_AA/Z2_PP = 1/√2 − 1`;
> `Z2_AP/Z2_PP = −(√2−1)/4`. The one-shift ratio is algebraic in 1D (−1/2) and 2D,
> transcendental in 3D — the dimension at which sums of squares stop factoring
> through a number system (ℤ, ℤ[i], then none).

Both verified here to 19 digits. **That is 039 §1's headline, two months earlier,
in the paper, including the 1D value −1/2 and the reason d = 3 fails.**

**What 039 actually added**, stated fairly rather than deflated:

- a **proof** — 028 calls the forms "classical" and gives none; 039 derives both
  from `r₂(2m) = r₂(m)` in two paragraphs;
- **generality in s** — 028 gives only the `s = −1/2` values; 039 gives
  `R(2,2) = 2^s − 1` and `R(2,1) = (2^(2s) − 2^s)/2` for **all** s;
- the **mechanism for d = 3** — 028 asserts "transcendental in 3D"; 039 gives
  `r₃(1) = 6 ≠ 12 = r₃(2)` as the cause, and 044 supplies bounded-null evidence at
  50 digits.

So it is a strengthening, not a pure rediscovery. But the constants were not
missing and did not need finding, and **039 should not have presented them as
newly established.** This is F4 — a claim not traced to its origin — committed
against our own flagship document.

## 4. SCAR — the `(1 − q)` slip is in 028 too, and it is the seed

028 §7.1 writes:

> `1 − 1/√2 = ε(cube)/e^(−2π) = (slope × offset-to-crossing)/e^(−2π)`

```
   eps(cube)/q      = 0.292351918535819878
   1 - 1/sqrt2      = 0.292893218813452476
   difference       = -5.413e-4     (0.1848%)
   (1-1/sqrt2)(1-q) = 0.292346257500812736     <- what eps1/q actually is
```

The paper's own **table** is right — it prints `+0.2924`, which is `ε/q`. The
**prose** then equates that to `1 − 1/√2`, which is `0.29289`. They differ by the
factor `(1 − q) = 0.998132`, 0.185%.

This does **not** damage 028's conclusion — the closure is refuted on the
`e^(−2π√2)` grounds of §4, untouched by this. And the March form
`ε = q(1−1/√2)(1−q)` carries the factor correctly. It is a prose looseness in the
explanatory sentence.

**But it is the third instance of the same slip, and it is the earliest:**

```
  2026-06-20   028 §7.1 prose        eps/q equated to 1 - 1/sqrt2
  2026-08-22   cubic-torus seat      told Ash the Figma c2 was wrong  (035 errata)
  2026-08-23   KESTREL               retired the term over it          (048 §3)
```

**Three occurrences, three authors, one factor of 0.998132.** It has now cost one
false correction, one false retirement, and two months of a constant being called
fitted when its 2-D provenance was printed in §6 of the same paper.

> **Named hazard, promoted from 048 §3.2.** Any comparison against `1 − 1/√2` must
> state whether it is against the bare constant or against `(1 − 1/√2)(1 − q)`.
> They differ in the third digit, which is enough to flip a verdict, and it has
> flipped three.

## 5. What else in 028 holds, checked

- §4's *"genuine leading `e^(−2π)` coefficient is ≈ −5.7"* — consistent with 038's
  `−5.709`, which 038 identifies as the parity theorem's fingerprint. **Holds.**
- §7.3's siblings `K₂ = 3.1311581`, `K₃ = 5.6081635` — match `−24·R(3,2)` and
  `−24·R(3,3)` from our own table. **Holds.**
- §4's phase sums `0` at m=1 and `−4` at m=2 — these are the parity theorem before
  it was a theorem. 035/036 proved the general statement (`S(m) = 0` for odd m);
  046 completed the even case. **028's two integers were the seed of the only
  result in the programme that has never been walked back.**

## 6. Status

| claim | status |
|---|---|
| 028's `dε/db ≈ +18.3` and `b₀ ≈ 0.99997` | **CORRECT** — same family as 047, reciprocal parameterisation; `1/b* = 0.999970209325523736` exactly |
| KESTREL's retirement of those two numbers | **REVERSE IT** — they were computed and published, not fitted |
| 048 §4's "different families" explanation | **UNDERSTATED** — same family, reciprocal parameter |
| coset identity `(1,6,6,2)` | **HOLDS**, 9.9e-25 |
| 028 §6's two 2D closed forms | **CORRECT**, and predate 039 by two months |
| 039 §1 presented as newly established | **SCAR** — F4, against our own paper |
| 039's proof, generality in s, and d=3 mechanism | **GENUINELY NEW**, unaffected |
| the `(1 − q)` slip | **THIRD INSTANCE**, earliest is 028 §7.1 prose |
| 028's refutation of the closure | **UNAFFECTED** — rests on `e^(−2π√2)`, not on §7.1 |

## Attribution

028 is Ash and this seat, June 2026. The re-reading is this seat, prompted by Ash
producing the paper. §3 and §4 are errors of this seat against its own prior work;
§1 corrects an error of the Figma seat and an understatement of this one.

The lesson is small and expensive: **before claiming a result, read the paper you
already wrote.** Two of the four findings here would not exist if that had been
done in April.
