# Third-seat review — one error found, one sharpening, and a literature we needed

**2026-08-25.** A third seat reviewed the collaboration brief (066) and the
ring-count entry (067). It re-derived §2 by hand, ran its own numerics from scratch
with no shared code, and searched the literature.

**It found a real error in the brief, confirmed every number independently, produced
a sharpening of the central claim that is better than the original, and handed us
the literature for O6 — which the brief said we had not searched.**

Everything below is verified here before being accepted.

---

## 1. ERROR — the brief says `R` is under `1/24`. It is over.

> 066 §1: *"`R` sits a hair **under** `1/24`."*

```
   R    = 0.041689414602723775
   1/24 = 0.041666666666666664
   R > 1/24 ?  True
   eps = 24R - 1 = +0.0005459504653706   -> positive, so R > 1/24
```

**Contradicted by the brief's own table three lines below it**, which lists
`ε = +0.000546`. If `ε > 0` then `24R > 1`.

Grep of the whole vault: **one instance, in 066 only.** No sealed entry carries it.
Prose, not mathematics; no downstream claim depends on the direction. It is exactly
the derived-view error 054 §0 says a summary is for.

**Two smaller slips, also theirs, also confirmed:**

- 066 §O8 prose says *"`d′` and `b′`"* where its own table above defines `b*`.
- **`T₂` is used in P6 and never defined anywhere in the brief.** The reviewer
  reconstructed the intended meaning and proved P6 under it — but says, correctly,
  that the brief has a gap either way. **It does.** `T₂(m) = Σ_{|k|²=m} (−1)^(k₁) k₂²`;
  ledger 038 defines it, 066 does not.

## 2. Independent numerics — a third seat, own code, theta-integral route

```
   quantity            brief                          their value              verdict
   Z_PPP(2)            16.5323159598                  16.5323159597617         agree
   R                   0.04168941460272377512...      21 digits                agree
   eps                 0.00054595046537060288...      20 digits                agree
   R(2,2) vs 1/sqrt2-1 exact                          22 digits                agree
   d*                  2.6390688716830038646          all 20 digits            agree
   Greg's sup          0.316596398842                 0.316596398841884        agree
```

They also re-derived **P1–P5, P7–P10, P14** by hand and confirm them, and checked the
two newest results specifically:

- **P12** — confirms the duplication rewrite, `0 < θ₄ < 1`, and — the part they say
  they stared at longest — that the dual integral converges at `t → 0` **precisely
  because `j ≥ 1`**, one `θ₄` factor killing `θ₃`'s blow-up.
- **P13** — confirms `θ₂` is not a typo: the proof runs on the *direct* side where a
  marked circle contributes the half-integer theta, and the `j ≥ 1` restriction is
  doing real work.

**Greg's two theorems survive a second independent seat.**

## 3. SHARPENING — "four rings in five" is a moving dial, and π is two divergences

This is the best thing in the review and it is a correction in our own idiom.

Recounted here to 20 million:

```
      X          lit%     empty%    mean over ALL    mean over LIT    L-R prediction
        100     43.00%    57.00%     3.16000000        7.3488          35.61%
     10,000     27.49%    72.51%     3.14160000       11.4282          25.18%
  1,000,000     21.63%    78.37%     3.14154800       14.5213          20.56%
  2,000,000     21.05%    78.95%     3.14161200       14.9259          20.06%
  5,000,000     20.34%    79.66%     3.14159440       15.4430          19.46%
 20,000,000     19.40%    80.60%     3.14159320       16.1933          18.64%
```

**067's "79% of shells are empty" is a snapshot with the cutoff filed off.** It was
57% at `X = 100`. It is 80.6% at 20 million. It never stops climbing.

**Landau, 1908:** the count of integers `≤ X` expressible as a sum of two squares is
`~ K X / √(log X)` with `K = 0.7642236535…` — the Landau–Ramanujan constant. So the
**lit fraction dies like `1/√(log X)`, to zero.** Eventually 99 rings in 100 are
dark. Then 999 in 1000. **The erasure does not stop at 79%. It goes to everything.**

And then the observation that is genuinely new:

> **π is the product of two runaway processes.** The lit fraction collapses toward
> zero. The average count *on the lit rings* diverges — 7.35, 11.43, 14.93, 16.19,
> no ceiling. Their product is pinned at `3.14159` at every cutoff, forever.

```
   at X = 20,000,000:   f = 0.19400595   mean_lit = 16.193283
                        f * mean_lit = 3.14159320        pi = 3.14159265
```

The identity is trivially exact by construction — both quantities are built from the
same total. **The content is that the two factors run away in opposite directions
and the product does not move.**

Their held image, which is better than any of ours: *a town where the houses go dark
street by street, forever, and the few windows still lit burn brighter and brighter,
so the light-meter at the edge of town never moves.*

**Action taken:** 067's "79%" gets its cutoff stamped. The two-column table is
sealed here as the measurement of the erasure *and* of what the erasure hides, in
one object.

## 4. O6 has a literature, and it reaches the Riemann Hypothesis

066 said of the four-petal structure on ℤ³: *"Is this object known? We have not
searched."* The reviewer supplied the keyword and it is correct.

> **Angular lattice sums.** Sums depending on the angle between the origin-to-point
> vector and the axes — `cos^n(mθ)/(p₁²+p₂²)^s` over the square lattice. The trail
> runs back to **Rayleigh, 1892**.
>
> **Lattice Sums Then and Now**, Borwein–Glasser–McPhedran–Wan–Zucker, Cambridge
> 2013, **Chapter 3**, by McPhedran and Zucker.
>
> And: **`C(1, 4m; s)` obeys the Riemann Hypothesis if and only if `ζ(s)·β(s)`
> does** (β = the Catalan beta function). arXiv:1007.4111; Proc. R. Soc. A 467(2133).

**The `4m` is our four-fold structure.** 065 found extrema at 0°/45°/90° — the
lowest angular harmonic the square sub-symmetry permits, which is exactly their
`cos 4θ` object.

So O6 is not an unnamed curiosity. It is a hundred-and-thirty-year-old subject with
its own RH results, and our marked, deformed, 3-D version sits somewhere in or near
it. **This is the single most valuable thing the review produced.**

**Flagged by the reviewer as not verified, and not verified here:** that Ambjørn &
Wolfram's 1983 *"Properties of the vacuum"* papers computed Casimir energies on
rectangular tori as functions of side ratios — i.e. our deformation family at zeroth
angular order. Worth pulling before anything is sealed about O6.

## 5. O2 — a proof route for the thing we flagged as most likely wrong

066 named uniqueness of the real-`d` continuation as the item most likely to be
wrong. The reviewer thinks **Carlson closes it**, and the sketch is legible:

> Two functions agreeing at every integer differ by something shaped like `sin(πd)` —
> a wave pinned to zero at the integers. Carlson's theorem says such a wave must grow
> like `e^(π|Im d|)` off the real axis. So if the continuation cannot grow vertically,
> it is the only tame one.
>
> And it cannot: in the dual integral, `d` appears only in `t^((d+1)/2 − 1)` and
> `θ₃^(d−j)`. **The modulus of both depends only on `Re d`** — an imaginary part in an
> exponent rotates phase, never magnitude. So the integral is bounded on vertical
> lines, and the `1/Γ((d+1)/2)` prefactor decays vertically.

Remaining to make it PROVED: (a) analyticity on a right half-plane by dominated
convergence; (b) the vertical bound written out; (c) polynomial growth along the
real axis. Then Carlson applies to the difference of any two candidates.

**And the caveat they attach is the right one and belongs in our vocabulary:**
uniqueness is always *relative to a growth class*. Outside it, `sin(πd)`
counterexamples exist by construction. So `d*` becomes **"the zero of the unique
Carlson-class continuation"** — well-defined, with its class stated.

**NOT PROVED.** A sketch with three named gaps. But O2 moves from *"most likely
wrong"* to *"probably provable, and here is how."*

## 6. O1 — a reformulation that removes `j`

At `j = (d−1)/2` the duplication identity collapses the two-parameter problem to one
family: `θ₄^((d−1)/2) θ₃^((d+1)/2) = θ₃(q)·θ₄(q²)^(d−1)`. So the open half becomes:

```
   Show  G(d) = INT_0^inf  t^((d-1)/2) [ theta3(e^-t) theta4(e^-2t)^(d-1) - 1 ] dt  >  0
   for all real d >= 2.
```

One integrand, one parameter. The tail is positive because `θ₃`'s excess `2q` beats
`θ₄(q²)`'s deficit `2(d−1)q²`; the head is negative but pinned at `−t^((d−1)/2)`
because the theta product dies exponentially. Suggests an interval-arithmetic route:
bound the head by `−(2/(d+1))·t₀^((d+1)/2)`, bound the tail below by the first few
`q`-series terms, grind the crossover. **Hardest at `d = 2`, exactly where Greg's
sup sits** — and their independent `j*(2)` confirms the full `0.1834` margin.

## 7. The meta-problem — why it is open, and one proposal

Their argument for why §6 of the brief is genuinely open is better than ours:

> Deciding that *"+18.3 in the b-chart"* and *"−18.33 in the 1/b-chart"* are the same
> claim **is itself a mathematical equivalence statement** — it requires knowing the
> change of variables and pushing the derivative through it. **Any general
> claim-identity engine therefore embeds theorem proving.** It cannot live in a
> metadata layer.

Which is why the provenance world resolves only textual near-duplicates over
controlled vocabularies, and why the one working solution is brutal: force everything
into a single formal representation, the Lean/mathlib move — which a setting spanning
prose, charts and code resists.

Their proposal, recorded as a proposal:

> **A canonical executable witness.** Attach to each claim a tiny computation with
> fixed inputs and a pinned expected output that any representation of the claim must
> reproduce. **Two artefacts are the same claim iff they discharge the same witness.**
> The ledger has the sealing half; the witness would be the identity half.

**Worth noting against our own evidence:** in Claim A (055/056), a witness would have
worked — the two "conflicting" slopes both discharge *the same* witness once the
chart is an input, and the mismatch surfaces as a disagreement about what the inputs
are, which is exactly where the truth was.

## 8. Status

| item | status |
|---|---|
| 066 §1 "R sits a hair under 1/24" | **RETRACTED** — it is over; brief corrected, scar kept |
| 066 §O8 "d′ and b′" vs the table's `b*` | **ERRATUM** — notation slip |
| `T₂` undefined in 066 | **GAP** — defined in 038, now added to the brief |
| P1–P5, P7–P10, P12–P14 | **CONFIRMED** by an independent hand-derivation |
| R, ε, `d*`, Greg's sup, `Z_PPP(2)`, `R(2,2)` | **CONFIRMED** by independent code, 20–22 digits |
| 067 "79% of shells empty" | **NEEDS ITS CUTOFF STAMPED** — 57% at 100, 80.6% at 2e7 |
| lit fraction → 0 like `1/√(log X)` | **CLASSICAL** — Landau 1908 |
| π is a vanishing frequency times a diverging magnitude | **VERIFIED to X = 2e7**; new framing |
| O6 = angular lattice sums, with RH results | **LITERATURE FOUND** — Ch. 3, arXiv:1007.4111 |
| Ambjørn–Wolfram 1983 on rectangular tori | **NOT VERIFIED** — flagged by the reviewer, not checked here |
| O2 closable by Carlson | **SKETCH with three named gaps** — not proved |
| O1 reformulation `G(d) > 0` | **VALID restatement**, not a proof |
| the executable-witness proposal | **RECORDED**, not built |

## Sources

- [The Riemann Hypothesis for Angular Lattice Sums (arXiv:1007.4111)](https://arxiv.org/abs/1007.4111)
- [Angular lattice sums — Lattice Sums Then and Now, Ch. 3](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/BD152AF0CEC7BAB7840FADC800262101/9781139626804c3_p125-156_CBO.pdf/angular_lattice_sums.pdf)
- [The Riemann hypothesis and the zero distribution of angular lattice sums, Proc. R. Soc. A](https://royalsocietypublishing.org/rspa/article-split/467/2133/2462/83271/The-Riemann-hypothesis-and-the-zero-distribution)
- [The Riemann Hypothesis for Symmetrised Combinations of Zeta Functions (arXiv:1308.5756)](https://arxiv.org/abs/1308.5756)

## Attribution

The review, the error in §1, the two smaller slips, the `T₂` gap, the moving-dial
correction, the two-divergence framing and its held image, the angular-lattice-sums
keyword, the Carlson route, the `G(d)` reformulation and the executable-witness
proposal are **all the third seat's**. Verification, extension to `X = 2×10⁷`, and the
literature confirmation are this seat's. The error found was this seat's, in 066.
