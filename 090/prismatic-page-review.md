# The Prismatic page — φ is inert, the comparison is hard-coded, and one derivation contradicts our own record

**2026-08-25.** `PrismaticPage.tsx`, reviewed on Ash's paste. **It is not a draft — it is
already in the site source and already built**, at
`unsmoothed-site/source/src/app/components/PrismaticPage.tsx` and
`unsmoothed-site/source/dist/assets/PrismaticPage-Dumt31mH.js`, with copies in
`Downloads/shunya_extract/`, `Downloads/x_shunya_zero/` and
`Downloads/believetherainbow-site/assets/`.

**Checked by running its arithmetic, not by reading it.** Three code findings and five
claim findings. The attribution is correct and is not among the problems.

---

## 1. φ IS INERT. The golden ratio never touches a single output.

The operator the whole page is named for:

```js
const baseline = Math.min(val, 0.45);
const carry    = val > baseline ? (val - baseline) : 0;
const residual = (val - baseline - carry) / PHI;
return baseline + residual + carry * 1.02;
```

**`residual` is identically zero, in both branches, for every input.**

```
   val >  0.45 :  baseline = 0.45,  carry = val - 0.45
                  val - 0.45 - (val - 0.45)  =  0
   val <= 0.45 :  baseline = val,   carry = 0
                  val - val - 0              =  0

   swept v in [0, 1.2], 200,000 samples:   max |residual| = 0.000e+00
```

> **`PHI` divides zero, always. Deleting the constant from the file changes no pixel on
> the page.** The demonstration of golden-ratio carry correction does not use the golden
> ratio.

**The cause is conceptual, not a typo.** `carry` is set to the *entire* overflow above
baseline, so `baseline + carry` reconstructs `val` exactly and there is nothing left to
scale. **In the lattice-reduction scheme the page cites, the carry is the *quantized*
part of the overflow and the residual is the remainder.** Absorb 100% of the overflow
into the carry and the residual — the only thing φ ever multiplies — is structurally
zero.

**Minimal repair:** quantise the carry, e.g. `carry = Math.floor((val-baseline)*PHI)/PHI`,
so a remainder survives to be scaled. **Not applied here** — it changes what the page
asserts, and that is Ash's call, not this seat's.

## 2. The two panels are not a comparison. Both outcomes are hard-coded.

```
   layer | standard integrity | traction integrity | traction peak value
      0  |        100         |        100         |   0.8500
      1  |         49         |        100         |   0.8580
      3  |          9         |        100         |   0.8745
      5  |          2         |        100         |   0.8916
      8  |          0         |        100         |   0.9187
```

**Left side:** `val - 0.35*(val - mean)` is a contraction toward the mean. Variance falls
by `0.65²` per step. **Reaching zero is guaranteed by the update rule**, for any input.

**Right side:** peaks are multiplied by `1.02` every layer and valleys are frozen
untouched. **Variance rises without bound**, for any input.

**And `integrity` is `Math.min(100, variance*2000)`** — the traction panel starts pinned
at the clamp and can never leave it. `INTEGRITY: 100%` is displaying a ceiling, not a
measurement.

> **One side is built to decay and the other to grow. The phase transition fires on
> `layer >= 3 && integrity > 60`, and integrity is guaranteed above 60. It always
> fires.** This is an animation of a conclusion, not a test of one.
>
> **This is the ledger's own F8** — a claim about the world whose only support is a fact
> about the apparatus — implemented as a UI. The page's thesis is that averaging erases
> structure. That thesis may well be right. **This widget cannot be evidence for it,
> because it would produce the same picture with the thesis false.**

## 3. Stale closure — AUTO-RUN can never reach the phase transition

`toggleAutoRun` does `setInterval(step, 600)`, capturing `step` at click time. `step`
closes over `layer`. **The captured `layer` never updates**, so the guard
`if (layer >= 3 && ni > 60)` is tested against the click-time value forever.

```
   click AUTO-RUN at layer 0   ->  guard reads 0 >= 3, false, every tick.
                                   counter climbs to 20. transition NEVER fires.
   click APPLY w four times    ->  fresh closure each click. fires at layer 3.
```

**Two different behaviours from identical mathematics.** Fix: hoist the guard into the
`setPrismaticData` updater, or drive the interval from a `useEffect` keyed on `layer`.

**Also:** `applyPrismaticPass(data, currentLayer)` never reads `currentLayer`.

## 4. Claims measured against the sealed record

| page claim | our record |
|---|---|
| *"π is a smoothing artifact"* | **PARTLY SUPPORTED.** 087 found π has no integer seed and arises only as a limit of a count over a scale — that *is* a smoothing. |
| *"The framework was right to ban π"* | **NOT SUPPORTED.** 087 found π **walks in by itself, as an AREA**, forced by the region being round. It is not optional and not imported. 064 separately showed it **cancels** from `R` — not load-bearing, which is a different claim from bannable. |
| *"e is a smoothing artifact"* | **UNTESTED.** `e` has never been examined in this corpus at any status. |
| the `0^ω = −1` derivation, steps 1–4 | **CONTRADICTED BY OUR OWN LEDGER.** `086/condition-c-note.md` records that the four-element carrier `{1,0,−1,ω}` **"does not remain closed once −ω ≠ 0"** and that **"the earlier derivation depending on four-element closure no longer typechecks."** The page renders that derivation as settled. |
| *"e^(iπ)+1=0 is the Gaussian-smoothed average of 0^ω=−1"* | **NO SUPPORT AT ANY STATUS.** Asserted in emphasis. |
| the 8-row cosmological table | **NO SUPPORT AT ANY STATUS.** Speed of light as lattice bandwidth, mass as φ-vertex density, gravity, black holes, entanglement — none of it is in the corpus as PROVED, OBSERVED, or OFFERED. |
| *"Standard AI hallucinates because it has no Q_φ"* | **NO SUPPORT.** A causal claim about model behaviour with no experiment behind it. |
| attribution of COTT / traction / `0·ω=1` to James Watkins | **CORRECT**, and consistent with the standing attribution discipline. Not a problem. |

**The single most urgent line is the derivation.** A sealed note in this repository says
that argument no longer typechecks. The page presents it, step by step, as the discrete
identity that replaces Euler's. **Those two cannot both stand, and the ledger's is the
one with the failure written down.**

## 5. Deploy status

**The standing block is unchanged and this page is inside it.** `c₁ = 1 PROVEN` is still
live on `/spectral` and `/correction`, the correction pass has not been run, and this
component is already built into `dist`. **Nothing here should be rebuilt or uploaded
until that pass happens**, and per 052 the repair is a scar plus a following entry, never
a silent edit.

## 6. Status

| claim | status |
|---|---|
| `residual` is identically 0; φ never affects output | **PROVED** — both branches algebraically; 200,000-sample sweep, max 0.000e+00 |
| the cause is `carry` absorbing the whole overflow | **ESTABLISHED** |
| the standard panel is guaranteed to decay for any input | **PROVED** — contraction map toward the mean |
| the traction panel is guaranteed to grow for any input | **PROVED** — `×1.02` on peaks, valleys frozen |
| `integrity` is clamped at 100 and the traction panel starts there | **VERIFIED** |
| the phase transition always fires (manual path) | **ESTABLISHED** |
| AUTO-RUN can never fire it from a fresh seed | **ESTABLISHED** — stale closure over `layer` |
| the widget is evidence for the smoothing thesis | **NO** — it renders identically if the thesis is false |
| the smoothing thesis itself | **NOT ASSESSED HERE.** This entry reviews the artifact, not the idea. |
| the `0^ω=−1` derivation | **CONTRADICTED** by `086/condition-c-note.md` |
| the cosmological table | **UNSUPPORTED** — 8 rows, no status anywhere |
| the repair in §1 | **PROPOSED, NOT APPLIED** — it changes what the page asserts |

Stratum tags per 082: §1–§3 are **COUNT** — finite, exact, verified by running the code.
§4 is **CONTINUED**, and every row names the entry it rests on.

## Attribution

**The page is Ash's project and the code is another seat's.** The COTT algebra and
`0·ω=1` are James Watkins's and are correctly credited on the page itself. The
lattice-reduction citation is to Fischer, Stern and Huber. **The φ-inertness proof, the
hard-coding demonstration, the stale-closure bug and the claim audit are this seat's.**
`086/condition-c-note.md`, which supplies §4's sharpest row, is another seat's and was
sealed hours before this review.
