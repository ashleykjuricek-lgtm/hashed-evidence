# 030 — Tier-1 Icosahedral Quasicrystal Operator Experiment: A Documented Null

**Date:** 2026-07-03
**Authors:** Reena (Ash) + Claude/Opus, with critique from GPT and Figma; concept threads from James.
**Status:** Tier-1 **closed as a documented null.** The method held. No quasicrystal-specific or
modular signature survived a robustness check. Two algebraic facts stand; three seductive signals
were killed. Recording *why they died*, because that is the point.

Scripts and figures sealed alongside this record (see `hashes.txt`). Fully reproducible:
`python tier1.py`, `python sweep.py`, `python mirror.py`, `python mirror_sweep.py`.

---

## The dummy version (plain language)

**What we were doing.** There's a long-standing hope in this project that if you build the right
little math machine on top of a *quasicrystal* — an ordered pattern that never quite repeats, the
kind with five-fold symmetry — something deep (like the special number τ = i from modular math)
might fall out on its own. Before believing any of that, we did the disciplined thing: build the
machine, run it, and see what's actually there. Calculate first, theorize second.

**The machine, in one breath.** Take the flat 3D shadow of a 6-dimensional grid (that's how you
make an icosahedral quasicrystal), connect nearby points into a network, and put two "forces" on
that network: **S = smoothing** (each point drifts toward the average of its neighbors) and
**K = stirring** (each point swirls its neighbors around). A dial called **δ** sets how much stir:
`machine = S + δ·K`. Then we watched what the machine does and compared the quasicrystal against
two honest stand-ins: an ordinary repeating crystal, and a pile of random dots.

**Three things looked exciting. All three died when we checked them. Two boring things turned out
to be bedrock.** Here's the whole story:

| # | The exciting claim | What happened |
|---|---|---|
| 1 | An output number landed at ~50, right next to a famous Riemann zeta zero (49.77). | **Mirage.** That number has no fixed size — one line of code makes it 5, 50, or 500. Re-run it 60 different ways and it wandered from 21 to 81. Dead. |
| 2 | The quasicrystal's "stirring" was tighter/quieter than the controls — maybe it's special. | **Died under retest.** In one setup it looked special; across many setups it was a coin-flip, no better than the crystal. |
| 3 | The quasicrystal has a real hidden mirror (√5 flips to −√5), so maybe the machine respects that mirror. | **Real idea, no effect.** The mirror is genuinely built into the quasicrystal's DNA — but the machine's behavior does *not* reliably respect it. Real structure, but silent. |

**The two things that held up (the boring bedrock):**

- **At δ = 0 (no stir) the machine is "balanced."** True — but it's true for a trivial reason we
  could prove in one line. It's bookkeeping, not a discovery, and it is *not* evidence for anything
  deep. We refused to let it be dressed up as one.
- **The stir-and-smooth interaction (the "eddy" term) is always a smoothing-type thing, never a
  spinning thing.** This one is real and solid, it held in every single test, and it matches how
  real fluids work (eddy diffusion). It's the one genuinely structural result.

**The lesson — and it's the reusable part.** There were three "special numbers/patterns" and one
simple test told the real one from the fakes: **does it survive when you change the arbitrary
choices?** The zeta-50 didn't survive (it moved). The mirror-5 is real math but left no footprint.
Only the boring eddy fact survived everything. That sorting *is* the science. A single striking
number is not a result; a number that keeps showing up no matter how you poke it, is.

**Bottom line:** we went looking, honestly, and the quasicrystal machine does **not** carry a
special fingerprint — no zeta, no modular τ = i, nothing you couldn't get from an ordinary crystal.
That's a real answer, not a failure. It's exactly the discipline this project exists to enforce.

---

## What we built (technical)

- **Point set:** `Z^6 → R^3` icosahedral cut-and-project. Physical projection uses φ = (1+√5)/2;
  internal projection uses the Galois conjugate φ′ = (1−√5)/2. Acceptance window is the **rhombic
  triacontahedron** (projection of the 6D unit cube), implemented exactly as the zonotope of the 6
  internal generators via the 15 face-normal half-space tests — **not** a ball. This preserves the
  icosahedral symmetry that a spherical window destroys.
- **Graph:** symmetric k-nearest-neighbour (same k for all point sets → matched connectivity, so
  comparisons are about geometry, not density).
- **Operators:** `S = −L` (negated graph Laplacian; symmetric, smoothing/decay). `K` antisymmetric
  circulation, a blend (knob α) of icosahedral-geometry swirl (cross-products about a 5-fold axis in
  physical space) and hidden-shadow swirl (same in internal/perp space). `O_δ = S + δ·K`.
- **Integration note:** conservative handling of the antisymmetric part (Cayley/operator-split, not
  forward Euler, which spuriously injects energy on a skew operator).
- **Controls (fair):** *periodic crystal* = identical machinery with φ replaced by the rational
  approximant 13/8 (commensurate → periodic); *random* = matched-count points in a ball with random
  shadow coordinates.

## What we tested and found

1. **δ = 0 self-adjoint / real-spectrum point** — CONFIRMED but TRIVIAL. Forced by S = Sᵀ, K = −Kᵀ;
   max|Im λ| ≈ 1e-16 at δ = 0, rising as |δ| grows. Not evidence for τ = i.
2. **[S,K] is symmetric** — CONFIRMED and ROBUST (worst asymmetry 7e-17 across all 60 sweep
   configs). The "third regime" is an eddy-diffusivity (symmetric enhancement), the
   BCH/homogenization reading — not rotation, not Reynolds stress. Bedrock. (Also: tr[S,K] = 0
   always, so the eddy spectrum is forced to balance about zero; only its spread is free.)
3. **Zeta coincidence (eddy edge ≈ 49.77, 10th Riemann zero)** — KILLED. Pre-registered test: raw
   edge wandered 21.5–81.1 across 60 configs (median 61), 3/60 within 3% of 49.77, and the quantity
   is unit-free anyway (dimensionless version sits at 0.15–0.52). Coincidence.
4. **QC has the tightest eddy spread** — KILLED by robustness. Single k=6 run teased it; across 60
   configs QC wins only 28/60 (~coin flip), tighter than random (median ratio 0.77, unremarkable
   "order beats noise") but tied with the periodic crystal (median 1.02).
5. **QC respects the Galois mirror √5 → −√5** — KILLED by robustness. The shadow coordinate *is* the
   exact Galois conjugate of the physical one, and K_conj is entrywise the Galois conjugate of K_phys
   (S is integer-valued, self-conjugate). A single config teased QC as 2–3× more mirror-symmetric
   (normalized eddy-spectrum gap 0.12 vs 0.32 / 0.22); across 12 configs the gap medians are QC
   0.193, periodic 0.217, random 0.220, with QC "most symmetric" only 6/12. The 0.12 was a low-tail
   fluke (QC range [0.057, 0.611] — wider, not lower). **Key lesson:** an *exact* symmetry of the
   matrix entries does **not** imply an *approximate* symmetry of the eigenvalues. The mirror is real
   as arithmetic (welded to Q(√5), unlike the zeta coincidence) but **spectrally inert.** The only
   residue is a weak, noisy tendency for the shadow-side eddy spread to run ~12% tighter (median
   spread ratio 0.88, range 0.49–1.18) — soft, not a signal.

## Method / the lesson

The discriminant between a real result and a mirage is **invariance under the arbitrary choices**
(wiring k, patch size, random seed, operator scaling, blend α). Applied consistently, it killed all
three seductive signals and left only what is genuinely forced by the algebra. No jump to Tier-2
(modular / τ = i) is warranted — nothing earned it. Three concept threads are kept explicitly
distinct and were explained to James: the **zeta-50** (a mirage — moves when you rescale), the
**mirror-5** (√5 → −√5, real algebra but spectrally inert), and **"zero = −∞"** (true only in the
logarithmic/limit frame; the fully-smoothed state is reached only as t → ∞). Three different kinds
of "special," sorted by the same test.

## Files in this entry

- `tier1-quasicrystal-null.md` — this record.
- `tier1.py` — single-run build + plot. `tier1_summary.png` — its figure.
- `sweep.py` — 60-config robustness/α/zeta sweep. `sweep_summary.png` — its figure.
- `mirror.py` — Galois mirror test (single). `mirror_summary.png` — its figure.
- `mirror_sweep.py` — mirror-gap robustness sweep. `mirror_sweep_summary.png` — its figure.
