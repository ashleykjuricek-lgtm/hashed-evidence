# Counting the petals — 022's rose, measured for the first time

**2026-08-22.** Follows 044, same night. Prompted by Ash: **"flat and thin rhombi."**

022 asserted two things about the Penrose rose and neither was ever checked:
**ten petals**, and **`r = |cos(5θ)|`**. 044 established that the rose is real and
must not be closed with the dead `1/φ` value. This entry counts it.

---

## 1. The petals — 022's count is CORRECT

Angular sweep of `r(θ) = Z_shifted(θ)/Z_unshifted`, 1441 samples (0.25° resolution),
shift magnitude `1/φ²` as in 022, `s = 2`, decagon N=8 / octagon N=10.

```
decagon (Penrose P3):  10 lobes   spacing exactly 36.00 deg   width exactly  8.00 deg
octagon (silver)    :   8 lobes   spacing exactly 45.00 deg   width exactly 28.00 deg
```

Lobe centres for the decagon: **0, 36, 72, 108, 144, 180, 216, 252, 288, 324.**

> **Ten petals. Confirmed by counting, for the first time.**

## 2. `r = |cos(5θ)|` — REFUTED

Least-squares fit of `r(θ)` to each basis (amplitude + offset free), residual
normalised by the data's own standard deviation. A good fit is well under 0.15:

```
decagon    |cos(5θ)| : 0.7881
           cos(10θ)  : 0.6965
           cos(20θ)  : 0.8439
octagon    all three : 1.0000
```

Every one is garbage. The curve does not resemble a rose curve.

## 3. What it actually is — a two-level step, not a smooth petal

```
decagon:  min 0.521239   max 0.617630   swing 0.096391  (17.7% of mean)
          most-occupied levels:  0.5225 (30.5% of sweep)   0.6176 (21.6%)
          duty cycle high = 8/36 = 0.2222

octagon:  min 1.027264   max 1.295178   swing 0.267913  (22.8% of mean)
          duty cycle high = 28/45 = 0.6222
```

The curve sits flat at one value, jumps, sits flat at another, jumps back. Sharp
edges. **Two states, not a continuum** — which is what Ash's "flat and thin rhombi"
predicts qualitatively, and what a smooth flower does not.

**But the obvious quantitative version of that idea fails.** The Penrose tiles occur
in ratio φ:1. The two levels are in ratio

    0.617630 / 0.521239 = 1.18492      phi = 1.61803

**NOT ESTABLISHED** that the two levels are the fat and thin rhombi. Two states are
measured; the identification is not.

## 4. The control — the rose is NOT the aperture

Ten lobes for a ten-sided window and eight for an eight-sided window is exactly
what the **window's corners** would produce, with the tiles never involved. Shift
toward a corner and you admit a different count than shifting toward an edge. That
deflation had to be killed before anything else could be said.

So: same ℤ⁵ → ℝ² projection, same shift magnitude, same zeta — **round acceptance
window**, area-matched. A circle has no preferred direction. If the rose is the
aperture, it must go flat.

```
DECAGON   polygon window (10 corners)      swing 17.69% of mean
          ROUND window (R=1.01698)         swing 15.39% of mean     ratio 4.94 (see 4.1)

OCTAGON   polygon window (8 corners)       swing 22.78% of mean
          ROUND window (R=1.02703)         swing 27.08% of mean     ratio 1.22
```

> **The direction-dependence survives a round window. On the octagon it gets
> stronger.** The rose is in the projected point set, not in the shape of the
> aperture.

### 4.1 One anomaly, flagged rather than smoothed

The decagon's round-window ratio runs at **≈ 2.93–3.40** rather than ≈ 1. The
unshifted round window is evidently sitting on a degenerate configuration — most
likely many perp-space points landing exactly on the boundary circle at the
high-symmetry centre — so its **baseline is not trustworthy** and neither are that
row's absolute values.

**The octagon row carries the verdict**: base 1.027, no anomaly, swing 27% with no
corners anywhere. The decagon row is consistent with it but is not independent
evidence until the baseline is understood. **Open item.**

## 5. Where this leaves 022

| 022 claimed | status now |
|---|---|
| ten petals | **CONFIRMED** — counted, spacing exactly 36.00° |
| `r = |cos(5θ)|` | **REFUTED** — residual/std 0.70–0.84; it is a step function |
| ratio = 1/φ at vertex directions | **REFUTED** (044) — it is the *maximum* of a curve, and 0.6176 vs 0.6180 misses even there |
| the shape is direction-dependent and real | **CONFIRMED, and strengthened** — survives a round window |
| the rose is the tiling, not the observer's aperture | **SUPPORTED** by §4, decisively on the octagon |

**022's headline number was wrong and its picture was wrong, and the thing it
noticed was right.** The rose exists, it has ten lobes, it is not the curve anyone
said it was, and it is not an artefact of the window.

## 6. Not established

- That the two levels are the fat and thin rhombi. The population ratio is φ; the
  level ratio is 1.185. **The most obvious test of Ash's idea came back negative.**
  A different pairing (widths? areas? edge counts?) is not ruled out and was not
  tested.
- What sets the lobe width — 8° of 36° for the decagon, 28° of 45° for the octagon.
  No account of either.
- The decagon round-window baseline. See §4.1.
- Whether any of this survives larger N. All of it is N=8 / N=10.

## Attribution

Cubic-torus / Shunya-Zero programme; Tier-1 quasicrystal experiment. The rose was
named by Ash in April 2026 from the structure rather than the numbers (022's own
summary records this). It was counted tonight because Ash said **"flat and thin
rhombi"** — which is why anyone thought to ask whether the petals were all the same
kind, which is the question that produced §1 and §3. The deflationary hypothesis in
§4 was the apparatus's, and the apparatus's own control killed it.
