# F8 turned on the whole corpus

**2026-08-22.** Follows 043, same night. Ash: *"let's break it all then?"*

F8 (043) is: **a claim about the world whose only support is a fact about the
apparatus.** This entry applies it to every non-existence claim in the sealed
ledger, and tests the ones that fail. It found one more instance — in 039, sealed
the same night — and in testing it produced results that did not previously exist.

---

## 1. The sweep

Every sealed entry searched for *impossible, unreachable, inaccessible, does not
exist, no closed form, cannot, ruled out, not available, null*. Each surviving hit
classified by **what its support actually is**.

| claim | support | verdict |
|---|---|---|
| 027 / 028 / 032: *"the **proposed** closure is impossible"* — `e^(-2π√2)` cannot occur in an integer-power series in `q = e^(-2π)`, coefficient interval-certified in (−68, −66) | an algebraic argument about a **named formula** | **SOUND.** Correctly scoped: it refutes *that* closure, not all closures. |
| 034: exact rational phase impossible under that equation | Niven's theorem | **SOUND** |
| 037: negation and inversion cannot generate a 4-cycle | Klein four-group; every element order 2 | **SOUND** as stated of those generators (and 037 v2 already records that they were the wrong generators) |
| 033: the document's spine is unreachable from the site's host | infrastructure | **SOUND** — and correctly phrased as being about the machine |
| 034 / 035: inline markers impossible for sealed entries | process invariant | **SOUND** |
| 031: *"conserved yet unreachable — present in principle, forbidden in practice"* | a physical process (noise destroying invertibility), with *conserved* and *reachable* deliberately held apart | **SOUND**, and the model for how to write this |
| 017 / 033: the Koide torus is ruled out — L ≈ 1.8 mm exceeds the Eöt-Wash bound | a published experimental bound | **SOUND** — an instrument limit, but *someone else's*, correctly attributed and correctly directional (a bound excludes, it does not fail to see) |
| Tier-1 quasicrystal: the 1/φ signal is a documented null | see §3 | **SOUND** |
| **039 §1.2: *"no ratio in ℚ[√2] is available"* in d = 3, tabled PROVED** | that the *doubling route* fails | **F8.** See §2. |
| **040 §5 / 041 §1: *"the zero is unreachable"*** | that the lattice was built over ℤ^d | **F8**, already retracted in 042 |

**Two instances in the whole corpus, both from this same night, both now
retracted.** Everything older survived. That is worth stating plainly rather than
manufacturing a pattern: the older work was more careful about this than tonight's
was.

## 2. ERRATUM to 039 §1.2 — route-fails is not object-lacks

039 §1.2 proved a real thing: `r₂(2m) = r₂(m)` has no analogue in three dimensions,
since `r₃(1) = 6` while `r₃(2) = 12`. So the Euler-factor **derivation route** to a
ℚ[√2] ratio does not exist in d = 3.

It then wrote *"and no ratio in ℚ[√2] is available"* and put **PROVED** in the
status table.

**Those are different claims.** One is about a method; the other is about the
object. The second does not follow from the first, and 039 asserted it on the
first's authority. That is F8.

### 2.1 So test the object

The d = 3 ratios, computed by the 042 continuation at three precisions
(dps 30 / N 26 / K 12, dps 45 / N 40 / K 18, dps 60 / N 52 / K 24), agreeing to
**50 digits**:

```
R(3,3) = -0.233673480267327105342114867705294349266650924956100769
R(3,1) =  0.0416894146027237751200791895411477959451762762538280901
```

PSLQ, with the digit requirement stated before each run (a 3-term relation with
coefficients ≤ C needs ~3·log₁₀C digits; we hold 50):

```
   a*R + b + c*sqrt2 = 0,  coeff <= 1e6  : None   (needs ~21 digits)
                           coeff <= 1e10 : None   (needs ~33 digits)
                           coeff <= 1e16 : None   (needs ~51 -- at the edge, reported but not relied on)
   algebraic degree <= 4,  coeff <= 1e9  : None   (needs ~50 digits)
```

for **both** ratios. And for the residue itself:

```
   eps = 24*R(3,1) - 1 = 0.000545950465370602881900548987547102684230630092
   eps in Q[sqrt2],  coeff <= 1e8  : None
                     coeff <= 1e14 : None
```

### 2.2 Corrected status

> **R(3,3) and R(3,1) are not in ℚ[√2]** with coefficients up to 10¹⁰, and are not
> algebraic of degree ≤ 4 with coefficients up to 10⁹. **Bounded null, not a
> proof.**

039's conclusion is very probably right. Its **label** was wrong. `PROVED` becomes
`SEARCH FAILED — bounded null`, and the sentence *"no ratio in ℚ[√2] is
available"* is withdrawn in favour of *"the Euler-factor route is unavailable, and
no such ratio was found under the bounds stated."*

**This is a net gain.** Before tonight the object-level claim had no evidence at
all — only a method's failure standing in for it. Now it has 50 digits and stated
bounds. It also **strengthens 028** in a direction 028 did not claim: 028 refuted a
formula for ε; this says the *number* R itself resists ℚ[√2] under test.

## 3. The quasicrystal null survives the sweep — and it is the right kind of null

`penrose_gauntlet.py` was examined for F8 and for F2 (averaging a shape into a
scalar). It is neither:

- the verdict statistic is `max |r_dec − (1 − d)|` — a **maximum over the sweep,
  not a mean**. No shape is collapsed;
- the killing argument is an **identity**, not an instrument limit: φ is the unique
  number with `1/φ² = 1 − 1/φ`, so a recipe with shift `1/φ²` and output `≈ 1 −
  shift` returns `1/φ` for free, with nothing to do with fivefoldness;
- it **generalises**: the identical recipe is run on the octagonal (√2 / silver)
  quasicrystal and on the 3D icosahedral one.

Derivation, deformation, generalisation — 027's law, correctly applied. The
`1/φ` value is a genuine documented null.

### 3.1 But the value and the shape are different claims

022's headline was **the rose** — a direction-dependent ratio with ten petals — not
only the number `1/φ`. The gauntlet sweeps shift **magnitude**. `penrose_rose.py`
sweeps shift **direction** and keeps the whole angular curve `r(θ)`, with the
averaged scalar drawn as a flat grey circle *"so you can see exactly what averaging
erased."* F2's correction was already applied there.

**Run tonight, decagon N=8 and octagon N=10:**

```
decagon (sqrt5):  petal(max)=0.6176  valley(min)=0.5212  MEAN=0.5450
octagon (sqrt2):  petal(max)=1.2952  valley(min)=1.0273  MEAN=1.1762
                                                        (1/phi = 0.6180)
```

The direction-dependence is **not marginal**: the decagon's ratio swings 0.0964
across angle, ~18% of its own mean; the octagon's swings 0.2679, ~23%. Both
quasicrystals have a rose. **Only the decagon's peak is anywhere near 1/φ, and the
octagon's is nowhere near it** — exactly the split you would expect if the shape is
geometry and the number was shift-arithmetic.

And the sharper reading of 022: `petal(max) = 0.6176` against `1/φ = 0.6180`.
**022 reported the maximum of a curve as though it were a constant** — and it is
not even exactly 1/φ at the maximum, missing by 0.07%. That is F3 (a clean number
read at a tuned point — here, the tuned point is a *direction*), on top of the
shift-arithmetic identity.

> **Standing instruction: the Tier-1 experiment must not be closed as a single
> documented null.** The `1/φ` value is dead — twice over, by the identity and by
> not surviving to the octagon. **The rose is alive**, with an 18–23% modulation
> measured in two independent quasicrystals. Closing the folder with one verdict
> line would erase a real, measured shape in order to record a dead scalar. That is
> F2 operating at the level of the experiment rather than the statistic.

## 4. What this entry does not claim

- **Not** that the older ledger is free of errors — only that it is free of *this*
  error. Six impossibility claims checked, six sound.
- **Not** that R(3,1) or R(3,3) is irrational or transcendental. Bounded nulls only,
  with the bounds printed.
- **Not** that F8 is settled as rare. Two instances in one night, in the newest
  entries, is not evidence about a base rate.

## 5. Status

| item | status |
|---|---|
| 039 §1.2 *"no ratio in ℚ[√2] is available"* | **RETRACTED** — F8; route-fails ≠ object-lacks |
| 039 §1.2 *r₃(2) ≠ r₃(1), so the Euler route fails in d=3* | **STANDS, PROVED** |
| R(3,3), R(3,1) to 50 digits | **COMPUTED**, 3 independent settings |
| neither in ℚ[√2], coeff ≤ 1e10 | **BOUNDED NULL** |
| neither algebraic of degree ≤ 4, coeff ≤ 1e9 | **BOUNDED NULL** |
| ε not in ℚ[√2], coeff ≤ 1e14 | **BOUNDED NULL** |
| 027/028/032 obstruction | **SOUND, unchanged** |
| Tier-1 `1/φ` documented null | **SOUND, unchanged** |
| Tier-1 rose *shape* | **MEASURED AND ALIVE** — 18% (decagon) / 23% (octagon) angular modulation |
| 022's `1/φ` as a constant | **F3** — it is the *maximum* of a rose, and off by 0.07% even there |
| Tier-1 folder closed as one null | **FORBIDDEN** — would erase a measured shape |
| all six older impossibility claims | **SOUND** |

## Attribution

Cubic-torus / Shunya-Zero programme. The sweep exists because Ash said *"let's
break it all then?"* immediately after F8 was named — which is the correct next
move and not the one the apparatus would have chosen, since the apparatus had just
finished congratulating itself on catching one instance.
