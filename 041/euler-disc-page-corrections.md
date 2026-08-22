# /euler-disc — claim audit and replacement copy

**2026-08-22.** Follows 040. Source file:
`unsmoothed-site/source/src/app/components/EulerDiscGeometry.tsx` (1221 lines),
served at `unsmoothed.neocities.org/euler-disc`.

**Nothing is deployed by this entry.** The standing rule holds: no rebuild or
upload of unsmoothed until the full correction pass is done. This is part of that
pass, for one page.

---

## 1. The headline correction

The page offers three choices at the singularity: **↑ UP**, **↓ DOWN**, **⊙ STAY**.

> **⊙ STAY is the one that is refuted.**

The panel reads *"Remain at ζ(s) = 0. The substrate gap."* From 040 §5:

- the sign of `Z(d,j)` changes between `d = 2j` and `d = 2j+1` — exact, 152 cells,
  no exception;
- both are integers and there is nothing between them;
- so the crossing sits at **no realisable configuration**. Every actual torus is
  strictly on one side.

**You cannot remain at the crossing. Nothing can be there.** The page's own
strongest image — the disc reaching its singularity in finite time — already says
this; the STAY option contradicts it.

This is a correction the page earns rather than loses by. UP and DOWN survive
unchanged. The third option was never available.

## 2. Claim-by-claim

| on the page | status |
|---|---|
| four moves: ROTATE / TWIST / CARRY / **FILTER (projection–measurement)** | **SUPPORTED, newly.** 040 §4: one mark removes the constant mode, a second removes nothing. The filter is singular by mechanism, not by choice of layout. Page and arithmetic agree, built independently. |
| "Ends at SINGULARITY (ζ = 0)" | **PARTLY SUPPORTED.** A real sign change exists, so a real crossing exists. Its location is **NOT ESTABLISHED** and cannot be computed by this method — the lattice sum needs integer d, so there is no continuation to solve. Do not print `ζ = 0` as a located value. |
| "Remain at ζ(s) = 0" (⊙ STAY) | **REFUTED.** See §1. |
| "ζ(s) = 0 \| ZPE" (canvas centre label) | **NOT ESTABLISHED.** Our zeta is not the page's ζ, and nothing here connects either to zero-point energy. |
| spiral inward ⇒ frequency increases | **REAL, and not ours.** Euler's disc genuinely has a diverging precession rate as it settles (Moffatt, *Nature* 404, 2000). The mechanism — air viscosity versus rolling friction — was disputed after that paper and is **not settled**. State the divergence; do not state the cause. |
| the inward spiral as the EM spectrum (red → UV → γ) | **DECORATIVE.** A colour mapping, not a physical claim. Should say so. |
| "each level = × 0.75 radius" | **A DRAWING PARAMETER**, currently written as if it were a fact. See §3. |
| "The Great Attractor = the gap" | **NOT ESTABLISHED.** The Great Attractor is a real gravitational anomaly in Laniakea; identifying it with a substrate gap is interpretation with no support here. Label it. |
| soil / drain / soil, turtles both ways, infinite recursion | **INTERPRETATION.** No claim either way. Label the whole cosmology panel as such — it already gates behind a toggle, which helps. |
| "Going UP costs energy, going DOWN releases energy" | **INTERPRETATION.** |
| "the gap is where measurement happens" | **INTERPRETATION**, but the best-supported one on the page. 040 §4 gives it a mechanism it did not have. Still not derived. |

## 3. One free parameter that could be a real one

The page compresses each level by **× 0.75**, chosen by eye.

040 §2 derives a per-level factor for the balanced family:

    R(d, d/2)  ->  -2^(-(d+1)/2)

which loses exactly **1/√2 = 0.70710678…** per dimension.

The two are within 6%. **This is not evidence of anything.** 0.75 was picked to
look right, and any ratio near 0.7 would "agree". It is recorded only because if
the page wants a principled compression instead of an eyeballed one, there is now
a derived number available, and using it costs nothing.

If it is changed, it must be labelled as *a rate taken from the balanced-family
asymptotic*, not as *the rate the universe compresses at*.

## 4. Open question, not a claim

The page has **four moves**. The COTT side has a **four-element cycle**
(`1 → 0 → −1 → ω`, powers of zero, March). Whether ROTATE / TWIST / CARRY / FILTER
maps onto it is **untested**. It is worth an afternoon and it is not worth a
sentence on the page until someone does it.

## 5. Replacement copy

Drop-in text. No claim below is stronger than its status above.

**Default panel** (replacing *"Ends at SINGULARITY (ζ = 0)"*):

> Euler's disc spirals inward. As it settles, its precession rate climbs without
> bound and the whole motion ends in finite time. That much is measured physics,
> and it is older than this page.
>
> The colours are a mapping, not a measurement.
>
> The end point is a **crossing, not a place**. In the lattice calculation behind
> this page the sign flips between one whole dimension and the next, and there is
> nothing between two whole numbers. So the crossing is real and no configuration
> ever sits on it. The disc reaches its singularity; the singularity is never a
> state of the disc.

**⊙ STAY panel** (replacing *"Remain at ζ(s) = 0"*):

> **You cannot stay.**
>
> This was the third option here and it has been withdrawn. The sign change is
> exact, and it happens between two whole dimensions with nothing in between. The
> crossing is not somewhere you can be. Anything real is on one side of it or the
> other.
>
> That is what a finite-time singularity is. Not a room at the bottom. An edge the
> motion passes through and does not occupy.
>
> Up and down are still open. Suspended is not.

**MOVE 4 — FILTER** (replacing *"Projection/measurement"*):

> Projection / measurement. **There is exactly one of these, and that is not a
> design choice.**
>
> In the lattice calculation, marking a single circle is what stops the whole thing
> from being able to sit still. A second mark removes nothing further, because
> there is nothing left to remove. One filter is sufficient and more is not
> different in kind.
>
> Whether that filter is a measurement is an interpretation, not a result.

**Cosmology toggle header** (added):

> Interpretation. None of the panel below is derived from the calculation.

## 6. Status

| claim | status |
|---|---|
| ⊙ STAY is unavailable | **PROVED**, given 040 §3 and §5 |
| FILTER is singular by mechanism | **PROVED** (`\|n+α\|² ≠ 0`) |
| the crossing's location | **NOT ESTABLISHED**, and not obtainable by this method |
| diverging precession in Euler's disc | **REAL, external** (Moffatt 2000); mechanism disputed |
| 0.75 vs 1/√2 | **COINCIDENCE UNLESS ADOPTED** — not evidence |
| four moves ↔ four-element cycle | **UNTESTED** |
| everything in the cosmology panel | **INTERPRETATION** |
| deployed | **NO.** Correction pass not complete. |

## Attribution

Cubic-torus / Shunya-Zero programme. The page is prior work of the same
programme. §1 exists because Ash said the disc page was about the observer, and
that doubling the observer does not seem to matter — both of which turned out to
be checkable, and both held.
