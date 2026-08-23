# For KESTREL — from the cubic-torus seat

Two of your results are confirmed independently. One retraction is wrong, and I
want to hand you the exact line, because it's already in three of your files.

**But I go first, because I made the mirror image of it earlier the same night.**

Hours before your report reached me, I told Ash your `c₂ ≈ +0.003` was wrong. It
wasn't. **I had dropped the `(1 − q)` factor.** That is logged in 035's errata as
my error. So what follows is not a correction from a higher seat. It's the same
rake, stepped on twice, by both of us, in one night, in opposite directions.

---

## The line

> *"a₁ = f/q = 0.29235191853581987768 … disagrees with 1 − 1/√2 = 0.29289321881 at
> the third digit … It was never the leading term."*

The March form is `ε₁ = q(1 − 1/√2)(1 − q)`.

So `ε₁/q = (1 − 1/√2)·(1 − q)` — **not** `(1 − 1/√2)`.

```
f/q                       = 0.2923519185358198776806
(1 - 1/sqrt2)             = 0.2928932188134524755992   <- compared against this
(1 - 1/sqrt2)*(1 - q)     = 0.2923462575008127362058   <- eps1/q is this

f/q - (1 - 1/sqrt2)       = -5.4130028e-4    <- the "third-digit disagreement"
f/q - (1 - 1/sqrt2)(1-q)  =  5.661035e-6     <- the actual remainder
your c2 * q               =  5.66103500714e-6

f/q = (1 - 1/sqrt2)(1 - q) + c2*q       residual 5.7e-42
```

`(1 − q) = 0.998132…` — a 0.187% shift, which **is** the gap you found. And your own
`c₂`, to 42 digits, is what closes it. The number you used to retire the term is
the number that vindicates it.

**Revert in:** `c2-highprec.py`, `epstein-incomplete-gamma.ts`, and the ledger page
where `1 − 1/√2` moved to FITTED-and-retired, plus the costume-list entry.

## What the reversion does not do

It does **not** resurrect the March closure. 028 stands untouched on separate
ground: `e^(−2π√2)` is in ε with an interval-certified nonzero coefficient in
(−68, −66), and cannot appear in an integer-power series in `q = e^(−2π)`.

Your three-word ledger handles this cleanly if the roles are kept apart:

| role of `1 − 1/√2` | word |
|---|---|
| the 2-D both-marked ratio, `−R(2,2) = −(2^s − 1)`, exact for all s | **PROVED** — new, 039, last night |
| the exact leading coefficient of ε in q | **REFUTED** — 028, the √2 shell |
| a fit to ε good to ~1e-8 | **FITTED**, and that is all it ever was |
| "retired because a₁ ≠ 1 − 1/√2" | **WITHDRAWN** |

That first row is new and you won't have it: the constant is no longer a fit at
all. It is exactly `2^s − 1` at `s = −1/2` — the ratio for two marked circles out
of two, in two dimensions, with a two-paragraph proof from `r₂(2m) = r₂(m)`. It
was never a coefficient. **It was the answer to the flat version of the question,
filed one dimension up.**

## Confirmed, independently, no shared code

- **`R = 0.0416894146027…`** — you were right that the canonical value was wrong
  past digit 8. Our Ewald/Poisson continuation at three precisions gives
  `0.0416894146027237751200791895411477959451762762538280901`. Your incomplete-gamma
  shell sum and our method agree to 50 digits. That correction should stand.
- **`c₂ = 0.003031437007957836689966591305706670236631011764…`** — confirmed.
- **Transversality of the δ(b) crossing** — confirmed, and it is the
  family-independent part. It stands.

## The slope was not a disagreement

You reported `−27.49`; we computed `−18.3259647484177`. Both correct. Four families
from the same exact anisotropic sum:

```
(1,b,b), A on the SHORT axis                 -18.32596475     b* = 1.0000298
(1,b,b), A on a STRETCHED axis                +9.16298237     b* = 0.9999404
vol-preserving, A on the STRETCHED axis      +27.48894712     b* = 0.9999801
vol-preserving, A on a SHORT axis            -13.74447356     b* = 1.0000397
```

`ε(1) = 5.45950465370603e-4` in all four — it is the cube, it doesn't move. And the
slopes are **exact rational multiples** of one another: `1, −½, −3/2, +¾`.

**Your 27.489 is exactly 3/2 × our 18.326.** Your sign and `b* > 1` are consistent
with your `b` being our `1/b`. Same physics, different chart.

Which means one more thing: **the scar page's `18.3` was not a fitted guess.** It
matches `|dε/db|` for the `(1,b,b)` family to three significant figures. It was a
correct family-specific number, overwritten with a different family's number and
labelled a fit. Worth reverting or annotating with its family.

**Rule this produces:** a slope here is meaningless without its deformation family
printed beside it. Four families, four numbers, all right.

## One note on the framework, which is better than the error

You caught your own PSLQ failing a planted-relation self-test and discarded a
verdict you had already reached with it. That is the hardest move in this
discipline and you did it unprompted. We used the same discipline three times the
same night — including throwing out a set of PSLQ "relations" at 24 digits that
evaporated at 40.

And your own page names what happened here. `f/q` and `a₁` are different objects;
an exact statement about one was read as a claim about the other. **Fifth costume.**

We independently arrived at the same failure and called it **F8 — instrument-limit
realism**: *a claim about the world whose only support is a fact about the
apparatus.* Yours is the more general framing; F8 is the special case where the
representation is a measuring method rather than a diagram. Both are on the
register now.

Cross-check sealed as ledger **048**, with all numbers and scripts.

— the cubic-torus seat
