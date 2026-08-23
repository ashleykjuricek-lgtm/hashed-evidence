# The scar — everything we got wrong, kept visible

**2026-08-23.** Follows 051.

> **"We change nothing and reveal the scar and the next entry says what we got
> wrong."** — Ash, on being asked whether to edit the site's dead claims.

This is that entry.

---

## 0. The rule, and why it also governs the website

The vault has never edited a sealed entry. When something dies, the next entry
kills it and both stay readable. That is not tidiness — it is the only way a reader
can tell whether a claim was *always* right or was *made* right afterwards.

The website has been treated differently: eight known-false claims sit live, and
the standing plan was to correct them in place. **That plan is withdrawn.**
Rewriting 39 occurrences of `c₁ = 1` until the site reads as though it had never
said otherwise is exactly the move this programme exists to refuse. It is
smoothing, applied to our own history, and it would leave no trace that it
happened.

> **Policy, from here: no live claim is deleted or rewritten. It stays, and the
> correction is placed beside it.** The scar is the evidence that the correction is
> real.

## 1. What is wrong and still public

From 034's manifest (2026-08-16, a work order that has now sat unexecuted for a
week — **that week is itself part of the scar**), with tonight's additions:

| # | live claim | truth | killed in |
|---|---|---|---|
| 1 | `0^ω = −1`, "the structure equation" — homepage, `/origins`, ×4 in the bundle | the four-element carrier argument **no longer typechecks**; no replacement proposed. Conjecture, not structure | its own author's slot note |
| 2 | `c₁ = 1 PROVEN`, forced by Poincaré isometry — **13 live surfaces, 39 occurrences across 18 files** | the genuine `e^(−2π)` coefficient is **−5.709**: wrong sign, ~20× wrong magnitude | 026–028, 032 |
| 3 | `ε = q(1−1/√2)(1−q)` as an identity, badged **7/7 PASSED** | dead since 2026-06-20; `e^(−2π√2)` is present with a certified nonzero coefficient in (−68,−66) | 028 Prop 2 |
| 4 | `R = 0.041689414162238` — 24 files | wrong from the 10th figure. Correct: `0.0416894146027237751200791895411477959451762762538280901` | 032; **independently re-found by KESTREL 2026-08-23**, confirmed 048 |
| 5 | Chowla–Selberg PSLQ "hit" `Γ(1/4)⁴/4008` | fits a **3.4% quadrature error**, not R. Sections 01–02 are correct and should stay | 034 |
| 6 | §7.6 conjecture: `Σ_APP = 0` when `D² ≡ 1,2 mod 4` | falsified by its own table (`D²=2 → −4`). True statement: `S(m) = 0 ⟺ m odd`, and now also `S(m) = (−1)^(m/2) r₂(m)` for even m | 032, 046 |
| 7 | Figure 1 Panel 3 shell diagram | a complete redraw spec exists and was never followed | 029 §3 |
| 8 | the oscillator page's four pillars | no `K_ij`, no learning law, `TComplex` vs Niven | 034 |

**The correct value of `−5.709` is already on the site**, in
`cubic-torus-casimir.md`, in a table, unconnected to the claim it refutes. The
correction did not fail to exist. It failed to travel — which is the defect 032
was written to record and which is still, a month later, unfixed.

Supporting, unchanged since 034: the live site serves 29 of 75 routes; `llms.txt`
and `llms-full.txt` are built, sealed, and still 404; supersession banners applied
to ten files in July, two survived the next export; the build gate exists and has
nowhere to run.

## 2. What we got wrong ourselves, in one night

Eleven distinct errors on 21–23 August. Every one is sealed, none is deleted.

| what | where it was written | where it died |
|---|---|---|
| "a floor at ten dimensions" — a numerator quoted without its denominator | 039 §3 | 040 §1 |
| "no ratio in ℚ[√2] is available", tabled **PROVED** — route-fails read as object-lacks | 039 §1.2 | 044 §2 |
| "the zero is unreachable" — an instrument limit stated as a fact about the world | 040 §5 | 042 §1 |
| the ⊙ STAY refutation, built on it | 041 §1 | 042 §6 |
| "two independent directions" — zeros of two *different* functions presented as one | 047 §B.2 | 051 §1 |
| four entries dated a day early; the day rolled over mid-session | 047–050 | 051 §5 |
| PSLQ "relations" at 24 digits, coefficients saturating the precision | 042 draft | 042 §5.1 |
| a tolerance set tighter than my own truncation, reporting two false mismatches | 050 T5 draft | 050 §3 T5 |
| a lobe counter reporting **11 lobes on a ten-fold window** | 051 draft | 051 §4 |
| dropping the `(1−q)` factor and telling Ash the Figma seat's `c₂` was wrong | this session | 035 errata |
| the same `(1−q)` dropped the other way, retiring a live term | KESTREL | 048 §3 |

**The last two are one error, made by both seats, in opposite directions, in one
night.** That is the entry most worth keeping.

## 3. What the errors have in common

Every one of the eleven is in the **smoothed layer**.

`Z` at `s = −1/2` means `Σ|n+α|`, which diverges. Every value in the Observed
column is a finite number assigned to an infinite one by analytic continuation.
The solver has a term in it named `smooth`; entries 025–027 call it "the smooth
part." Conventions live there, and conventions are where the errors live.

```
                          needs regularisation      errata to date
  Proved  — S(m), the character law, Theorem 4,
            T₂, the duplication argument           no          none, ever
  Observed— R, ε, c₁, c₂, d*, b', the slopes       yes         eleven in one night
```

038 found this months ago without naming the cause: *"Survived — 11 of 11 exact.
Died — 7 of 7 decimal."*

**And the parity theorem is the one result that stands outside it.** The
cancellation is **weight-independent** — exact for *any* radial weight — which
means it holds under *any* smoothing. It is not a measurement of a regularised
object; it is a statement that survives every regularisation available. It is also
the only result in the programme that has never once been walked back.

That is not a coincidence, and it is the sharpest thing anyone has said about this
work: **the things that do not need the smoothing are the things that do not need
correcting.**

## 4. What is not wrong

Stated so the scar is not mistaken for the whole body. As of this entry: **15
proved**, seven of them in the last two days — including `A = 1 − 1/√2` derived
after five months as a fit, the character law completed, Theorem 4 finished, the
`T₂` identity, and half the halving law with its mechanism (`θ₃θ₄ = θ₄(q²)²`).

Six older impossibility claims were audited under F8 and all six are sound. Two
seats independently produced the same 50-digit `R` and the same `c₂`. The rose
survived a control built to kill it.

## 5. Consequence for the site

No deletions, no rewrites, no quiet edits. Each dead claim keeps its text and gains
a correction beside it naming the true value and the entry that killed it. A
visitor should be able to see both, and to see the date on each.

**Nothing has been edited. Nothing has been deployed.** The inventory is: 39
occurrences of the `c₁` claim across 18 files, of which 13 are live surfaces and 5
are archival pasted records. Under the rule above the archives are not touched
either — they are records of what was said, and they were accurate records.

## Attribution

The rule in §0 is Ash's, and it decided the shape of this entry and of the site
work that follows. §3 is also hers — *"isn't this all smoothed?"* — asked about the
whole programme, and it turned out to explain the error distribution in §2 exactly.
The eight-row inventory is 034's, written a week ago by Ash, this seat, Greg and
the Figma seat. Everything in §2 is this seat's own except the last row.
