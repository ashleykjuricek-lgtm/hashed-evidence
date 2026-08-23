# Cross-check of the KESTREL report — two confirmations, one refutation, one false conflict

**2026-08-22.** Follows 047. KESTREL (the Figma seat) delivered a long report the
same night: corrected R, `c₂` to 50 digits, a closed-form search, an anisotropic
`R(b)`, and a **retraction of `1 − 1/√2`** written into three source-of-truth files.

This entry checks all of it independently. **Two of its results are confirmed and
should stand. One retraction is refuted. One apparent disagreement is not a
disagreement at all.**

---

## 1. CONFIRMED — the corrected R

KESTREL found the repo's canonical `R = 0.041689414162…` wrong past digit 8 (a
quadrature artefact) and replaced it with `0.0416894146027(2)`.

Our 042 continuation, three independent precision settings, agrees:

```
R(3,1) = 0.0416894146027237751200791895411477959451762762538280901
```

Two seats, no shared code, no shared method — KESTREL used an exact
incomplete-gamma shell sum, we used Ewald with a Poisson-form theta. **Same digits.**

028's abstract already carried the correct value (`0.041689414602723775…`); the bad
one had propagated elsewhere. **The correction is real and should stand.**

## 2. CONFIRMED — c₂ to 50 digits

```
c2 = 0.003031437007957836689966591305706670236631011764...
```

Independently checked here as the residual after the March form, and it closes the
gap **exactly** — see §3, where it is the number that decides the case.

Methodologically the strongest thing in the report: KESTREL caught its **own** PSLQ
failing a planted-relation self-test and discarded the verdict it had already
reached with it. That is the correct move and it is rare.

## 3. REFUTED — the `a₁` retraction

> KESTREL: *"a₁ = f/q = 0.29235191853581987768 … disagrees with 1 − 1/√2 =
> 0.29289321881 at the third digit … It was never the leading term — it was a
> 2-digit numerical coincidence."*
>
> — and moved `1 − 1/√2` to **FITTED-and-retired** in `c2-highprec.py`,
> `epstein-incomplete-gamma.ts`, and the KESTREL ledger page.

**The March form is `ε₁ = q(1 − 1/√2)(1 − q)`.** Dividing by q leaves
`(1 − 1/√2)·(1 − q)`, **not** `(1 − 1/√2)`. The comparison dropped the `(1 − q)`.

```
f/q                       = 0.2923519185358198776806
(1 - 1/sqrt2)             = 0.2928932188134524755992   <- what was compared against
(1 - 1/sqrt2)*(1 - q)     = 0.2923462575008127362058   <- what eps1/q actually is

f/q - (1 - 1/sqrt2)       = -5.4130028e-4   <- the reported "third-digit disagreement"
f/q - (1 - 1/sqrt2)(1-q)  =  5.661035e-6    <- the real remainder
KESTREL's own c2 * q      =  5.66103500714e-6

f/q = (1 - 1/sqrt2)(1 - q) + c2*q      residual = 5.7e-42
```

`(1 − q) = 0.998132…`, a **0.187%** shift — which is exactly the gap that was
reported as a third-digit failure. And the number KESTREL used to retire the term
is the number that vindicates it, to **42 digits**.

**The retraction should be reverted in all three files.**

### 3.1 What the reversion does NOT do

It does **not** resurrect the March closure. 028's refutation stands on entirely
separate ground: `e^(−2π√2)` appears in ε with an interval-certified nonzero
coefficient in (−68, −66), and cannot occur in an integer-power series in
`q = e^(−2π)`. That argument is untouched here.

**The honest three-way status of `1 − 1/√2`:**

| role | status |
|---|---|
| the 2-D both-marked ratio, `−R(2,2) = −(2^s − 1)` | **PROVED** (039 §1, this night) |
| the exact leading coefficient of ε in q | **REFUTED** (028 — the `e^(−2π√2)` term) |
| a fit to ε good to ~10⁻⁸ | **TRUE, and that is all it is** |
| "retired because a₁ ≠ 1 − 1/√2" | **WITHDRAWN** — arithmetic error |

### 3.2 A named hazard — the `(1 − q)` factor has now bitten both seats

Earlier the same night, the cubic-torus seat told Ash that the Figma seat's
`c₂ ≈ +0.003` was wrong. **The Figma seat was right; this seat had dropped the
`(1 − q)`.** That is logged in 035's errata.

Tonight the Figma seat dropped the same factor in the other direction and retired a
term over it.

> **Same factor, both seats, opposite directions, one night.** Any comparison
> against `1 − 1/√2` must state whether it is against the bare constant or against
> `(1 − 1/√2)(1 − q)`. They differ in the third digit and that is enough to flip a
> verdict.

## 4. NOT A CONFLICT — the slope

KESTREL reported `dδ/db = −27.49` at `b* ≈ 1.00002`, and called the scar page's
`+18.3` a fitted guess that was *"wrong sign & magnitude."* 047 computed
`dε/db = −18.3259647484177` at `b* = 1.0000297915619869892`.

Both are correct. They are answers to different questions, and the difference is
exactly determined. Four deformation families, computed here from the same exact
anisotropic sum:

```
family                                            eps(1)              d eps/db      b*
(1,b,b), A on the SHORT axis           5.45950465370603e-4      -18.32596475   1.0000298
(1,b,b), A on a STRETCHED axis         5.45950465370603e-4       +9.16298237   0.9999404
vol-preserving (b,1/sqrt b,1/sqrt b),
             A on the STRETCHED axis   5.45950465370603e-4      +27.48894712   0.9999801
same, A on a SHORT axis                5.45950465370603e-4      -13.74447356   1.0000397
```

`ε(1)` is family-independent — it is the cube. The slopes are **exact rational
multiples of one another**:

```
ratios to the (1,b,b) A-short slope:   1,  -1/2,  -3/2,  +3/4     (to 10 digits)
```

So there is **one intrinsic quantity**, and each deformation family reports it
times a determined rational factor. Consequences:

- **KESTREL's 27.489 is exactly 3/2 × 18.32596475.** Its sign and its `b* > 1` are
  consistent with a reciprocal parameterisation of b (its `b` is our `1/b`); the
  physics is identical.
- **The scar page's `18.3` was not a fitted guess.** It matches
  `|dε/db| = 18.32596475` for the `(1,b,b)` family to three significant figures.
  KESTREL replaced a correct family-specific number with a different family's
  number and labelled the original a fit. **That edit should be reverted or
  annotated with its family.**
- **Transversality is family-independent** — every slope is nonzero, as KESTREL
  correctly said. That part of its verdict stands unchanged and is the load-bearing
  one.

**Standing rule this produces:** a slope in this programme is meaningless without
its deformation family printed next to it. Four families, four numbers, all right.

## 5. Status

| claim | source | verdict |
|---|---|---|
| `R = 0.0416894146027…`, old canonical wrong past digit 8 | KESTREL | **CONFIRMED**, 50 digits, independent method |
| `c₂ = 0.00303143700795783668996659…` | KESTREL | **CONFIRMED** |
| PSLQ finds no elementary closed form for f | KESTREL | **PLAUSIBLE, not checked here** |
| `a₁ ≠ 1 − 1/√2`, term retired | KESTREL | **REFUTED** — dropped `(1 − q)`; revert in 3 files |
| `dδ/db = −27.49`, scar page's 18.3 "wrong" | KESTREL | **BOTH CORRECT** — different families; 18.3 was not a fit |
| transversality of the crossing | KESTREL & 047 | **CONFIRMED**, family-independent |
| slopes are exact rational multiples `{1, −½, −3/2, +¾}` | this entry | **COMPUTED**, new |
| `1 − 1/√2` as an exact q-coefficient | 028 | **still REFUTED**, on other grounds |

## Attribution

KESTREL — the corrected R, `c₂` to 50 digits, the PSLQ self-test discipline, and
the anisotropic computation. Cross-check, the `(1 − q)` diagnosis, and the
four-family slope structure — cubic-torus seat. Ash is the only channel between the
two seats, and carried the report across.

Neither seat is the checker of the other by seniority. This entry exists because a
peer report was taken seriously enough to recompute, which is the only form of
respect a calculation understands.
