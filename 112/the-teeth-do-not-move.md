# 112 — The teeth do not move: the rose at larger N (closes 109 §5)

**2026-09-06 (run), sealed 2026-09-07 UTC.** Ash: *"run it at larger N."*

**Status:** COMPUTED and CHECKED. 22 cases, containment 360/360 in every one. Closes the size-scaling caveat left open in **109 §5**. No new theorem.

**Depends on:** 109 (the three-answer rose node), and `penrose_gauntlet.py` (031/044, `92e9a622…`). `rose_three_answers.py` sealed here is a **modified** copy of 109's: the grid-and-project step is replaced by `lattice_points()`, which builds the grid one slab at a time and keeps only points whose perpendicular image can ever enter the window. Equivalent by construction (dedup first, then filter; duplicates share PERP, asserted) and confirmed by reproducing 109's N=8 numbers exactly (8820 points, base Z 521.387831, r in [0.521239, 0.617632]).

---

## 1. What was run

Both windows (022's polygon; the equal-area disc of 109 §3) at growing lattice size: **decagon N = 6, 8, 10, 12, 14, 16** (at N=16 the grid is 33⁵ ≈ 39 M points, of which 34,270 can ever enter the window); **octagon N = 8, 10, 14, 20, 28** (57⁴ ≈ 10.6 M; 36,224 reachable). Quarter-degree arcs; the original float recipe checked against every bracket at 360 angles per case. 92 seconds total.

## 2. What is frozen (COUNT; to four digits across every N)

| | decagon, 10-gon | decagon, round | octagon, 8-gon | octagon, round |
|---|---|---|---|---|
| swing, % of arc-mean | 17.70 | 15.38 | 22.79 | 27.11 |
| teeth | 10 × 8.25° | 10 × 12.75° | 8 × 16.75° | 8 × 16.25° |
| first tooth centre | 0.0° | 0.0° | 22.5° | 22.5° |
| largest single jump | 0.0830 | 0.4605 | 0.2541 | 0.2487 |

Tooth width spread across the teeth: 0.00° in every case. The teeth are set by the handful of heavy points nearest the origin in physical space, all present by N=6; growing the lattice adds nothing to them.

## 3. What changes with N — only the tails (COUNT)

| N (decagon) | 6 | 8 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|
| flat quarter-degree arcs, polygon | 852 | 716 | 648 | 540 | 496 | 444 |
| distinct flat levels, polygon | 15 | 14 | 14 | 14 | 13 | 12 |
| base Z (unshifted) | 521.298 | 521.388 | 521.430 | 521.453 | 521.467 | 521.476 |

Round window: **0 flat arcs at every N** for the decagon; octagon round falls 104 → 48 → 0 → 0 → 0. Far points keep arriving, each a step too small to see; the flat stretches fill in with them. Base Z converges as a sum of inverse fourth powers should (SUM in the limit).

## 4. Verdict

**The round-window survival holds at every size.** The rose is the point set, not the window's corners, and that no longer rests on one N. 109's sentence loses its caveat.

**Not closed here:** shift magnitude and exponent were not varied (tooth width is known from the July lobe-width test to track the shift). This run answers the size question and only that.

## 5. Witness units

| witness | predicate | declared class | sufficiency |
|---|---|---|---|
| containment | every sampled value inside its arc's bracket | float recipe, pad 10⁻¹², quarter-degree arcs | 22 cases × 360 angles, 0 misses |
| N=8 reproduction | chunked builder equals 109's direct build | same | points, base Z, r-range identical to 109 |
| frozen table | swing %, tooth count/width/centre, big jump constant in N | four significant digits | 6 sizes (decagon), 5 (octagon), both windows |

## 6. Files

```
the-teeth-do-not-move.md                      this note
rose_scaling.py                               the sweep
rose_scaling_output.txt                       fresh run, every case, every number above
rose_scaling_table.txt                        the same as a table
rose_scaling_summary.png                      swing / tooth width / levels vs N
rose_three_answers.py                         109's node with the chunked point builder (see header)
rose3_decagon_N16_poly_unrolled.png           the gear at N=16
rose3_decagon_N16_roundwindow_unrolled.png    the control at N=16
rose3_octagon_N28_poly_unrolled.png
rose3_octagon_N28_roundwindow_unrolled.png
```

**Attribution:** object and instruction — Ash; sweep, node change, write-up — Claude (Fable 5.1 seat), 2026-09-06/07.
