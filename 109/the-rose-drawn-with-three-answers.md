# 109 — The rose drawn with three answers, and what π is in it

**2026-09-06.** Ash: *"run it on the quasicrystal rose"* · *"seal it in the ledger and what is pi — in this structure?"*

**Status:** COMPUTED and CHECKED (finite, exact up to a stated float pad; four containment checks, 0 misses). No new theorem. One control run that decides a question left open in 031.

**Depends on (already sealed):** `penrose_gauntlet.py` — sealed in 031 and 044, SHA-256 `92e9a6229f96c53d77bdaa029e6898716c45bf0d329c4265fede0efad7a4816c`, unchanged on disk today. The rose recipe is 022's, reproduced in 031 (`penrose_rose.py`, `ecbe6ebf…`). The control is 031's `round_window_control.py` (`74b48b21…`), re-run here inside the new tool.

---

## 1. What this entry is

The Penrose rose is r(θ) = Z_shifted(θ) / Z_unshifted: a zeta sum over the cut-and-project point set, with the acceptance window in perpendicular space slid by 1/φ² in direction θ. 022 reduced it to a number (1/φ) and 031 caught the reduction: the mean of a rose is not the rose. 031 then drew r(θ) by sampling 721 angles and joining the dots.

Joining the dots is also a smoothing. The rose is a **step function** — lattice points drop in and out of the sliding window one at a time — and a polyline draws a confident diagonal through every step.

This entry draws the rose with a plotter that gives one of three answers for every arc of angle (Tupper's reliable graphing, interval arithmetic): **Bounded** (all values on this arc lie in [lo, hi]), **Unbounded** (a pole or detail finer than the arc), **Undefined** (no value on this arc). The propagation law is written once: Undefined absorbs, Unbounded spills, then the arithmetic runs. A gap is never a pole. The tool is sealed here as source (`threeanswer-0.1.0-src.zip`, 50 tests green in `threeanswer_test_output.txt`).

The rose enters the plotter as its own node. For each arc, every lattice point is sorted three ways — definitely inside the shifted window for the whole arc, definitely outside for the whole arc, or undecided (its boundary crosses inside the arc) — and Z over the arc is bracketed by [Σ definite, Σ definite + Σ undecided]. Where an arc holds a jump the bracket is fat and the picture shows a **bar from the lower level to the upper level**: "the jump is somewhere in here." Nothing is averaged; the mean is not drawn.

**Soundness, stated plainly (ROAD).** The lattice projection, window normals and zeta weights are ordinary floats (as in the sealed gauntlet), each padded outward by a relative 10⁻¹² before use; the arc's cosine and sine are true intervals (mpmath). The claim is: at that tolerance, every value of the original float recipe lies inside its arc's bracket. **Checked: 1440 angles × 4 cases, 0 outside** (`rose_three_answers_output.txt`).

## 2. What the rose is (COUNT — finite exact sums on the N=8 / N=10 grids; the infinite-lattice object is SUM, absolutely convergent at s=2)

| case | lattice pts that can enter | flat arcs / 1440 | jump arcs | distinct flat levels | lowest | highest | swing (% of arc-mean) | largest jump |
|---|---|---|---|---|---|---|---|---|
| decagon, 10-gon window (022) | 8820 | 716 | 724 | 14 | 0.521239 | 0.617632 | 17.71 % | 0.0830 |
| decagon, **round** window, equal area | 8820 | **0** | 1440 | 0 | 2.927638 | 3.403715 | 15.38 % | 0.4609 |
| octagon, 8-gon window | 4856 | 680 | 760 | 22 | 1.027264 | 1.295178 | 22.81 % | 0.2543 |
| octagon, **round** window, equal area | 4856 | 48 | 1392 | 3 | 1.027257 | 1.353773 | 27.13 % | 0.2489 |

**Findings, each checkable in the output file:**

1. **It is a gear, not a flower.** The decagon rose is ten flat-topped tabs, each **8.2° wide**, at **36° spacing** (edges at 4.1/31.9, 40.1/67.9, 76.1/103.9, … 355.9), every tab rising by the same **0.0830** — one heavy lattice point (nearest the origin in physical space, weight |x|⁻⁴) entering the window and leaving it 8° later. This is 045/lobe_width's "8°" seen directly, and it answers `count_the_petals.py`'s question: at this shift and N there are **not** five fat and five thin petals — all ten tabs are identical. (The octagon is the one with two lobe shapes: jumps of 0.254 and 0.086 alternate.)

2. **The tails are the small jumps, and there is a hierarchy.** Decagon: 20 jumps ≥ 10⁻², 92 in [10⁻³,10⁻²), 60 in [10⁻⁴,10⁻³), 224 in [10⁻⁵,10⁻⁴), 236 in [10⁻⁶,10⁻⁵), 92 in [10⁻⁷,10⁻⁶). Far lattice points enter and leave the window all the way down; each is a step of its own height. The polyline turned every one into a slope; the mean turned all of them into one number; this drawing keeps each one.

3. **The three answers all came back "bounded."** No poles, no gaps, in any of the four cases. The plotter's honesty here is not red columns; it is bars where the jumps are instead of diagonals. Reported so the tool is not credited with more than it did.

## 3. The control: take the corners away (decides 031's open question)

031 asked whether the rose is the tiling or the aperture: ten corners on the window → ten lobes is exactly what corners would do. `round_window_control.py` was written to test it and its verdict was never sealed. Run here, inside the three-answer node, with a **round** window of the same area (πR² = 10·tan(π/10)):

- **The rose survives.** Decagon swing 15.38 % of mean with the round window versus 17.71 % with the decagon; octagon 27.13 % versus 22.81 %.
- **The ten tabs are at the same ten angles** (centres 0, 36, 72, …), now **12.8° wide** with a notch in each (edges 6.4/29.6, 42.4/65.6, …), each rising by 0.4609 — the same heavy points, seen through a boundary of a different shape.
- **With the round window there is no flat arc at all** at quarter-degree resolution: the circle's boundary is always crossing some lattice point somewhere. With the polygon, 716 of 1440 arcs are flat.

**Verdict: the rose is in the point set.** The corners are not the rose. (COUNT at N=8 and N=10; one shift magnitude; not size-scaled — see §5.)

## 4. What π is, in this structure

Three different things are called π here, and only one of them erases anything.

**(a) π as apparatus.** The window's normals are cos(π(2k+1)/10); the round window's area is πR². This is π as a *period* — the fact that ten equal angles make a turn. Per 087's clean-room rule this is π declared in the setup, not π discovered, and it is tagged ROAD: it says nothing about the rose.

**(b) π as a shape — the round aperture.** This is the one the control tested. **A circular window does not erase the rose.** The teeth stay at the same ten angles, wider. Roundness of the *observer* is not the smoothing.

**(c) π as an operation — the average over direction.** The number 031 drew as a grey circle (0.545) is r(θ) averaged over θ. That single number is what 022 sealed as 1/φ and what this entry's four pictures replace. Sealed entry 067 says the same thing on the shell side: *π is the mean of the number of ways to write m as a sum of two squares* — an integer-valued, mostly-zero, wildly irregular count whose average is π. Here the count is a ten-toothed gear whose teeth are single lattice points, and its average is a circle.

So, in this structure: **π is not a shape. It is the act of averaging over direction.** The circle is what a gear looks like after that act. (a) is bookkeeping, (b) was tested and acquitted, (c) is the erasure.

**One temptation refused, on the record.** The round-window decagon's arc-mean is 3.0947. That is 1.5 % from π and it is *not* π: it is a ratio of two truncated zeta sums that depends on N, on the shift magnitude and on s, none of which were varied here, and the recipe gives no reason for it to be π. Filed under 027's law and the 49.77 scar (030): a near-miss is a coincidence until it survives changing the arbitrary choices, and this one has not been asked to.

## 5. Scope, and what is not claimed

- Single lattice sizes (N=8 decagon, N=10 octagon), one shift magnitude (1/φ²), one exponent (s=2). The gear's tab width and the level hierarchy are properties of *this* truncation; the round-window survival should be re-run at larger N before it travels.
- The plotter changes how the rose is **drawn**, not what is **computed**. Every number above is 022's recipe.
- No physical claim. No claim about 1/φ (022's claim was already deformed away in 031; untouched here).

## 6. Witness units

| witness | predicate | declared class | sufficiency |
|---|---|---|---|
| containment check | every point-sampled value lies inside its arc's bracket | float recipe, pad 10⁻¹², quarter-degree arcs | 4 × 1440 samples, 0 misses |
| flat-arc count | r constant on the arc to < 10⁻⁹ | same | 716 / 0 / 680 / 48 of 1440 |
| jump table | the twenty largest jumps and their angles | same | listed verbatim in the output |
| round-window control | swing survives removing the corners | equal-area disc, same shift, same s | one N per lattice (not size-scaled) |

## 7. Attribution

- **The rose** and the sentence that governs this entry, *don't average the rose* — **Ash** (022 object; 031 catch).
- **The three-answer plotter** (`threeanswer`) — written by **Claude (Fable 5.1 seat)** for Ash, 2026-09-06, from Jeff Tupper's 2001 reliable-graphing technique and the *design* of James Watkins's public `vexelray-gui-plot` module (same three answers, same absorb/spill law; his repository carries no license and no code was copied). Rose node, control run, this write-up — same seat, same day.
- **penrose_gauntlet.py / round_window_control.py** — the 031/044 seat (Claude), Ash directing.

## 8. Files

```
the-rose-drawn-with-three-answers.md      this note
rose_three_answers.py                     the rose as a three-answer node + control + containment check
rose_three_answers_output.txt             fresh run, all four cases, all numbers above
rose3_decagon_unrolled.png                r(θ) across, decagon window — the gear, unrolled
rose3_decagon_polar.png                   the same, as a rose
rose3_decagon_roundwindow_unrolled.png    the control: corners removed, teeth remain
rose3_decagon_roundwindow_polar.png
rose3_octagon_unrolled.png / _polar.png   the silver rose, two lobe shapes
rose3_octagon_roundwindow_unrolled.png / _polar.png
threeanswer-0.1.0-src.zip                 the plotter, source (fixed timestamps; hash depends on content only)
threeanswer_test_output.txt               50 passed
```
