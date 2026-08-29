# PrismaticPage — corrections

**2026-08-25.** Full review sealed as `hashed-evidence/090`. This is the actionable version.

**Three code defects found by running the component's arithmetic, not by reading it. All three fixed.
Four prose claims contradict or outrun the sealed record. None of those are changed — they alter what
the site asserts, and per entry 052 the repair is a visible scar, never a silent edit.**

The file existed in **five** places, all byte-identical:

```
   unsmoothed-site/source/src/app/components/PrismaticPage.tsx    <- canonical, EDITED
   Downloads/shunya_extract/src/app/components/PrismaticPage.tsx  <- mirrored
   Downloads/x_shunya_zero/src/app/components/PrismaticPage.tsx   <- mirrored
   unsmoothed-site/source/dist/assets/PrismaticPage-Dumt31mH.js   <- STALE, still the old build
   Downloads/believetherainbow-site/assets/PrismaticPage-*.js     <- STALE, still the old build
```

---

## FIXED 1 — φ was inert. It never touched a single output.

```js
const baseline = Math.min(val, 0.45);
const carry    = val > baseline ? (val - baseline) : 0;
const residual = (val - baseline - carry) / PHI;      // <- always 0/PHI
return baseline + residual + carry * 1.02;
```

`carry` was set to the **entire** overflow above baseline, so `baseline + carry` reconstructed `val`
exactly and `residual` was identically zero in both branches. Swept 200,000 values across `[0, 1.2]`:
**max |residual| = 0.000e+00.**

> **The golden ratio divided zero, every time. Deleting `PHI` from the file would have changed no pixel.**

**Fix — the carry is the *quantised* part of the overflow; the leftover is what φ damps:**

```js
const baseline = Math.min(v, 0.45);
const overflow = v - baseline;
const carry    = Math.floor(overflow / step) * step;   // exact multiple of the lattice step
const residual = overflow - carry;                     // now genuinely nonzero
return baseline + carry + residual / PHI;
```

Verified after the change: **max |residual| = 0.382**, i.e. φ is active.

## FIXED 2 — the comparison was hard-coded. Neither panel could have done anything else.

| layer | standard | traction | traction peak |
|---|---|---|---|
| 0 | 100 | 100 | 0.8500 |
| 1 | 49 | 100 | 0.8580 |
| 3 | 9 | 100 | 0.8745 |
| 8 | 0 | 100 | 0.9187 |

- **Left** was `val − 0.35·(val − mean)`, a contraction toward the mean. It reaches zero for **any** input.
- **Right** multiplied peaks by `1.02` every layer and froze the valleys. It grows **without bound** for any input.
- `integrity` was `min(100, variance × 2000)`, so the traction panel began above the clamp and could never
  leave it. **It was displaying a ceiling as a measurement.**
- The phase transition fired on `layer ≥ 3 && integrity > 60`, and integrity was guaranteed above 60.
  **It always fired.**

> This is the ledger's own **F8** — a claim about the world whose only support is a fact about the
> apparatus — shipped as a UI. The widget would have drawn the identical picture if the thesis were false.

**Fix:** removed the `1.02` amplification; metric changed to **retention** (variance relative to the seed,
so both panels genuinely start at 100%); added a **lattice-step control** so the operator can be driven
into failure. Measured behaviour now:

```
   structure ABOVE the lattice step   std 100->0%     traction 100->65%, plateaus     operator holds
   structure BELOW the lattice step   std 100->0%     traction 100->0%                operator LOSES
   coarse lattice (1/phi), same seed  std 100->0%     traction 100->2%                operator LOSES
```

**Two of three regimes are failures. That is what makes it an instrument.**

## FIXED 3 — AUTO-RUN could never reach the phase transition

`setInterval(step, 600)` captured `step` once; the `layer` inside that closure never advanced, so
`layer >= 3` stayed false forever. Clicking **APPLY ω** four times fired it; **AUTO-RUN** never did.
Same mathematics, two behaviours.

**Fix:** metrics now derive from the data via `useEffect`, and the run loop is a `setTimeout` keyed on
`layer`, so there is no stale closure. Also removed the unused `currentLayer` parameter, and relabelled
`PHASE TRANSITION ACHIEVED` → `STRUCTURE HELD > 60% PAST LAYER 3`, which is what the code actually tests.

**Build check:** `vite build` to a scratch directory — **compiles clean, 20.46s.** `dist/` deliberately untouched.

---

## NOT CHANGED — needs your call

### A. The `0^ω = −1` derivation contradicts our own sealed note. Most urgent.

The page renders steps 1–4 as the settled discrete identity replacing Euler's. But
`hashed-evidence/086/condition-c-note.md`, sealed hours earlier, records:

> *"the assumed four-element carrier `{1,0,-1,omega}` does not remain closed once `-omega != 0`. The
> earlier derivation depending on four-element closure no longer typechecks."*

**Both cannot stand. The ledger's is the one with the failure written down.**

**Proposed scar** (add below the derivation, delete nothing):

> **Carrier-closure scar, 2026-08-25.** This derivation assumes a four-element carrier
> `{1, 0, −1, ω}`. That carrier is not closed once `−ω ≠ 0`, so the four-cycle step does not currently
> typecheck. The surviving principle is **closure by extension** — when an exact operation leaves the
> assumed carrier, enlarge the carrier rather than coerce the output into an existing slot. Sealed as
> `hashed-evidence/086`.

### B. Header — "π is a smoothing artifact. *e* is a smoothing artifact."

**π: partly supported.** 087 found π has no integer seed and arises only as a limit of a count over a
scale. **`e`: never examined in the corpus at any status.**

**Proposed:** *"π has no integer seed — it exists only as a limit of a count over a scale. Whether `e` is
the same has not been tested here."*

### C. Closing — "The framework was right to ban π. It just didn't know why yet."

087 was run at your instruction with π excluded from the setup, and **π walked in by itself, as an area**,
forced by the region being round. It is not imported and cannot be refused.

**Proposed:** *"π cannot be banned — count inside a round region and it appears, forced by the shape of
the question. What it cannot do is seed anything. No integer search produces it. The golden world's
constant is a pair of integers you can find by looking, wearing a logarithm."*

### D. Two unsupported assertions

- *"e^(iπ)+1=0 is the Gaussian-smoothed average of 0^ω=−1"* — **no support at any status.** Mark as
  conjecture or cut.
- *"Standard AI hallucinates because it has no Q_φ"* — **a causal claim with no experiment.** Soften to
  a hypothesis.
- The **8-row cosmological table** (light speed, mass, gravity, black holes, entanglement) is not in the
  corpus at any status. Suggest a header: **INTERPRETIVE — none of these rows is derived.**

**The attribution is correct and is not a problem.** COTT, traction and `0·ω = 1` are credited to James
Watkins on the page, consistent with the standing attribution discipline.

---

## Deploy

**The block still stands and this page is inside it.** `c₁ = 1 PROVEN` remains live on `/spectral` and
`/correction`; the correction pass has not run; building the current tree would take the dead claim from
2 live pages to ~20. **Nothing here should be rebuilt or uploaded until that pass happens.**

The `dist/` bundles still contain the **old, broken** PrismaticPage. That is deliberate — `dist` was not
regenerated. When the correction pass does run, it must cover **both** defects, not just this one.
