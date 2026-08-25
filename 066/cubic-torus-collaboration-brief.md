# Cubic-Torus / Shunya-Zero — collaboration brief

**Version 2026-08-25. For a reviewing mind with no prior context.**

You are being asked to check work and to help with open problems. This document is a
**derived view**, not the record. The record is a hashed, append-only ledger at
`github.com/ashleykjuricek-lgtm/hashed-evidence`, entries 001–065. **If this document
disagrees with a sealed entry, the sealed entry is right and this is the error.**

Everything here carries one of four words. Please use them back.

| word | means |
|---|---|
| **PROVED** | a derivation short enough to check by hand, which has survived an adversary |
| **OBSERVED** | the numbers do it; there is no proof they must |
| **FITTED** | chosen so the numbers would land |
| **RETRACTED** | killed, and kept visible on purpose |

Current census: **15 proved · 14 observed · 3 fitted · 15 retracted.**

We would rather you find an error than agree with us. Four of the retractions below
were written within a day of the claims they killed, several against our own sealed
work.

---

## 1. The object, in plain terms

Take a box with opposite faces glued — a 3-torus, three circles at right angles. A
field on it can come back unchanged after a trip round a circle, or come back
**flipped**. Call a flipped circle **marked**.

The whole programme is one ratio: the zeta-regularised vacuum energy with some
circles marked, over the energy with none marked.

    Z_alpha(s) = SUM'_{n in Z^3} |n + alpha|^(-2s),   alpha in {0, 1/2}^3,   at s = -1/2
    R = Z_APP(-1/2) / Z_PPP(-1/2) = 0.0416894146027237751200791895411477959451762762538280901

`R` sits a hair under `1/24`. In March 2026 a closed form was proposed that matched
it to **seventeen digits**. The formula is false. Most of what follows is the
accounting of why it looked true, and what turned out to be real underneath.

**Notation used throughout.** `Z(d,j)` = the same at `s = −1/2` on a unit `d`-torus
with `j` of the `d` circles marked. `R(d,j) = Z(d,j)/Z(d,0)`. `q = e^(−2π)`.
`ε = 24R − 1`. `S(m) = Σ_{k∈ℤ², |k|²=m} (−1)^(k₁)`.

---

## 2. PROVED — please check these first

Each is short. If one of them is wrong, most of the rest falls.

**P1 · The parity theorem.** `S(m) = 0` for every odd `m`.
*Proof.* Odd `m` forces exactly one of `k₁,k₂` odd (squares are 0 or 1 mod 4). The
swap `σ(k₁,k₂) = (k₂,k₁)` preserves `|k|²` so it permutes the shell, and exchanges
which coordinate is odd so it negates every term. A finite sum equal to its own
negative is zero. ∎
Independently verified by a separate seat, no shared code, to `1e-54`.

**P2 · The character law, completed.** `S(m) = (−1)^(m/2) r₂(m)` for even `m`.
*Proof.* `m ≡ 0 mod 4` forces both coordinates even, so every character is `+1`;
`m ≡ 2 mod 4` forces both odd, so every character is `−1`. ∎ 1171 cases, 0 violations.

**P3 · Weight-independence.** The radius is constant on a shell, so any radial weight
factors out. The cancellation is *within* shells, never across them.

**P4 · Cube-exclusivity.** `σ` is a symmetry of `k₁²+k₂²` and of no anisotropic form.
Stretch one axis and the pairing dies linearly. `det σ = −1`: the cancellation is
powered by a **reflection**.

**P5 · Three dimensions, one coordinate at a time.** For odd `m`,
`T(m) = 2 Σ_{k₃≥1 odd} S(m − k₃²)`.
*Proof.* Condition on `k₃`. Even `k₃` ⟹ `m−k₃²` odd ⟹ the slice cancels by P1
(including `k₃=0`). Odd `k₃` ⟹ even ⟹ survives. `±k₃` pair. ∎

**P6 · An exact formula for `T₂`.** For odd `m`, with `E = {k : |k|²=m, k₁ even}`:
`T₂(m) = m·r₂(m)/2 − 2 Σ_E k₁²`. Hence `T₂(m) = 0` ⟺ the mean of `k₁²` over `E`
equals `m/2`. 552 cases, 0 violations.

**P7 · Two exact ratios in d=2, for all s.** `R(2,2) = 2^s − 1` and
`R(2,1) = (2^(2s) − 2^s)/2`.
*Proof.* Uses only `r₂(2m) = r₂(m)` (multiplication by `1+i`). Splitting by the power
of 2, `E_odd(s) = (1 − 2^(−s))E(s)`; the both-marked shell is `|k|² = 2m` with `m`
odd. ∎ Agrees with the solver to 31 digits.

**P8 · Where `1 − 1/√2` came from.** It is `−R(2,2)` exactly. The constant at the
centre of the false closure, recorded as a fit for five months, is the
**two-dimensional both-marked ratio**. It was never a coefficient; it is the flat
answer, filed one dimension too high.
*(Note: 028 §6 already stated both d=2 forms in June 2026, as "classical". The proof,
the generality in `s`, and the identification with the March constant are new. We
restated a sealed result without noticing — recorded as our error in ledger 053.)*

**P9 · Why d=3 cannot do the same.** `r₃(1) = 6` but `r₃(2) = 12`, so there is no
doubling bijection and no Euler factor splits off.

**P10 · One mark is enough.** With any `α_i = ½`, `|n+α|² ≠ 0`. One marked circle
removes the constant mode; a second removes nothing, because nothing is left.

**P11 · The March closure is impossible.** `ε` contains a term in `e^(−2π√2)` with
coefficient interval-certified in `(−68, −66)`, and `√2 ∉ ℚ`, so no integer-power
series in `q = e^(−2π)` can be exact.

**P12 · Half the halving law** *(due to the reviewing seat "Greg", 2026-08-23)*.
`2j ≥ d ⟹ Z(d,j) > 0`, for every integer `d ≥ 1`.
*Proof.* The functional equation sends `Z` to an absolutely convergent dual character
sum with theta kernel `θ₄(q)^j θ₃(q)^(d−j)`. Jacobi duplication
`θ₃(q)θ₄(q) = θ₄(q²)²` lets every plain circle pair with a marked one:
`θ₄^j θ₃^(d−j) = θ₄(q²)^(2(d−j)) θ₄(q)^(2j−d)`. Since `0 < θ₄ < 1` and both exponents
are non-negative when `2j ≥ d`, the product is `< 1` pointwise; the dual integrand is
negative; and `1/Γ(−1/2) < 0` flips the sign. ∎
**Verified sharp**: the bound holds in 44/44 cells exactly when `2j ≥ d`, and at the
boundary it is razor-thin (`0.999996, 0.999992, 0.999988, 0.999984`).

**P13 · Strict monotonicity** *(Greg)*. `Z(d,j+1) > Z(d,j)` for `j ≥ 1`, from
`θ₃⁴ = θ₂⁴ + θ₄⁴` giving `θ₃ > θ₂ > 0`, and `Γ(−1/2) < 0`.

**P14 · `R` is π-free.** The functional-equation prefactor
`π^(−1−d/2) Γ((d+1)/2)/Γ(−1/2)` depends on `d` and `s` only — **not on the marking**
— so it cancels identically in any ratio:

    R(d,j) = [ SUM'_m chi_j(m) |m|^(-(d+1)) ] / [ SUM'_m |m|^(-(d+1)) ]

Two integer-lattice sums, no π, no Γ, no Gaussian. Verified: converges to
`0.0416894146` from a π-free expression, and the denominator matches 028's
independently computed `Z_PPP(2) = 16.5323159598`.
*(The identity is in 028 §5. The consequence — π was never in the object, only in the
method — is ours.)*

**P15 · A sphere cannot carry any of this.** Marking is a homomorphism
`π₁(M) → ℤ₂`. `π₁(T³) = ℤ³` gives `2³ = 8` markings — exactly the
`PPP / APP×3 / AAP×3 / AAA` structure. `π₁(S²) = π₁(S³) = 0` gives one. And on a
*curved* space the heat expansion has a `k=4` term (`√π/15` for `S¹×S²`), putting a
pole in `ζ` at exactly `s = −1/2`, so `Z_A` and `Z_P` both diverge and `R` is `∞/∞`.
**`R` is a flat-space object.** But `θ_P − θ_A` is exponentially small, so
`Z_A − Z_P` is finite on *any* `M × S¹`: `0.2503281026` on unit `S¹×S²` against
`0.255482035923` on `T³`.

---

## 3. OBSERVED — where we would most like a second pair of eyes

**O1 · The other half of the halving law.** `Z(d,j) > 0 ⟺ 2j ≥ d`, verified in
152 cells with no exception; the `⟸` direction is P12, the `⟹` is open. Greg reduced
it to **one bound on one sequence**:

    (d-1)/2  <  j*(d)  <  d/2        upper PROVED, lower OPEN
    equivalently:   sup_d [ d/2 - j*(d) ]  <  1/2 ?

where `j*(d)` is the root of `Z(d, j) = 0` in the real-`j` continuation. The sup is
**at d = 2**, value `0.316596398842`, margin to the barrier `0.183403601158`. It
falls monotonically after that (`0.00206` at `d=24`), so a uniform argument is
stressed only at the bottom of the range. **This is the single most valuable open
item.**

**O2 · Uniqueness of the real-dimension continuation.** We continue `Z` to real `d`
by noting the theta factorises into a *power*: `Θ(t) = θ_A(t)^j θ_P(t)^(d−j)`. It
reproduces the integer lattice exactly (7 cases) and is λ-invariant to `1e-24` at
fractional `d` and `j`. **It is not proved unique** — no Carlson-type growth argument
has been attempted. If it is not unique, then `d* = 2.6390688716830038646...` (the
zero of `Z(d,1)`, 49 decimals, three independent settings) is not a well-defined
object. *We think this is the most likely place our recent work is wrong.*

**O3 · `T₂(m) ≠ 0`.** P6 turned a 552-case search into a sharp criterion: `T₂`
vanishes exactly when the even coordinate's mean square equals half the radius².
No zero below 4000. Open.

**O4 · `R(d, d/2) → −2^(−(d+1)/2)`.** 8 digits at `d = 40`; the balanced family loses
exactly one factor of `√2` per dimension. No proof.

**O5 · Is `R` algebraic?** Bounded nulls only, at 50 digits: not in `ℚ[√2]` with
coefficients ≤ `10^10`; not algebraic of degree ≤ 4 with coefficients ≤ `10^9`; `ε`
not in `ℚ[√2]` to `10^14`. **P14 may be the lever nobody has pulled** — `R` is a ratio
of two integer-lattice Dirichlet series at exponent 4. Does that admit identification
by a route we have not tried?

**O6 · A four-petal rose on ℤ³, and nobody has looked.** Deform the metric along a
unit direction `û`. First order is exactly `cos²θ` — a quadrupole from the single
marked axis, response matrix `diag(−2.9262045876, 1.8077123102, 1.8077123102)`,
off-diagonals `9e-17`. At finite deformation, four-fold structure appears in the
plane perpendicular to the mark: swing `4.918e-2` at `ε = 1`, extrema at 0°/45°/90°.
**Is this object known? Does it have a closed form?** We have not searched.

**O7 · The parity theorem on the other nine flat 3-manifolds.** By Bieberbach there
are exactly ten compact flat 3-manifolds, all `T³/G`. `σ` may or may not survive the
quotient — a finite check per manifold. And the marking count becomes `|H¹(M;ℤ₂)|`,
generally **not** `2^d`, which is the sharpest way to test whether the halving law is
about *dimensions* or about *markings*.

**O8 · Constants, if you want to try to identify them.**

```
R      = 0.0416894146027237751200791895411477959451762762538280901
eps    = 0.000545950465370602881900548987547102684230630092
c2     = 0.003031437007957836689966591305706670236631011764
d*     = 2.6390688716830038646381724497459231368660752817617    (zero of Z(d,1))
d'     = 2.99978241968328574                                    (R(d,1) = 1/24)
b*     = 1.0000297915619869892                                  (R(3,b) = 1/24)
```

`d'` and `b'` are two points on **one** level curve `R(d,b) = 1/24`; the trace
between them reproduces `b*` to 16 digits, so the cube's near-miss is a single
geometric fact with two measurements of it.

---

## 4. RETRACTED — please do not re-derive these

`ε = q(1−1/√2)(1−q)` (the March closure) · `c₁ = 1` "proven by Poincaré isometry"
(true `e^(−2π)` coefficient is **−5.709**) · `R = 0.041689414162…` (wrong from the
10th figure) · `1/φ` as a quasicrystal constant (it is the *maximum of a curve*, and
off by 0.07% even there) · `r = |cos 5θ|` for that curve (fit residual 0.79) ·
"the zero is unreachable" · "a floor at ten dimensions" · "no ℚ[√2] ratio is
available" tabled as PROVED · a `1σ/18σ` asymmetry in a CMB audit (we dropped one
error bar) · and `0^ω = −1`'s derivation, by its own author's note.

---

## 5. How to disagree with us usefully

These are our own failure modes, learned expensively. Each cost at least one wrong
verdict.

1. **State your parameterisation.** Two seats computed the same slope as `+18.3` and
   `−18.326` and spent a day calling each other wrong. One used `Q = |n|² + b²(…)`,
   the other sides `(1,b,b)` with `1/b²`. **Same family, reciprocal chart.** A slope
   here is meaningless without both its deformation family *and* its chart.
2. **Do not compare against `1 − 1/√2` without saying which one.** The March form is
   `q(1−1/√2)(1−q)`, so `ε₁/q = (1−1/√2)(1−q) = 0.29234626`, not `0.29289322`. That
   factor is 0.185% and it has flipped **three** verdicts, in three different years,
   by three different authors including us twice.
3. **Count both error bars.** We reported an 18σ tension that was 1σ, by comparing a
   predicted central value against a measured value using only the measured one's
   uncertainty.
4. **A broken instrument's verdict does not count.** We have twice discarded rather
   than patched: a PSLQ saturating its precision at 24 digits (every "relation"
   vanished at 40), and a lobe counter reporting 11 lobes on a ten-fold window.
5. **Route-fails is not object-lacks.** Proving a derivation route unavailable is not
   proving the object lacks the property.
6. **State the digit budget before running PSLQ.** A relation among `n+1` terms with
   coefficients ≤ `C` needs roughly `(n+1)·log₁₀C` digits. Below that it always
   succeeds.

---

## 6. The meta-problem, if that is more your area

Separately from the mathematics, this project has produced a research problem we
believe is genuinely open, and we would like to know if we are wrong about that.

**Branching, storage, and provenance representation are solved and in production**:
ATMS (de Kleer 1986 — multiple contexts alive at once, minimal environments,
nogoods); nanopublications extended with knowledge provenance (IRCDL 2025 — 197,511
published assertions, of which 41,339 are categorised *Contrasting Evidence*);
W3C PROV and PROV-AGENT (2025, arXiv 2508.02866).

**What is not solved is claim identity across changing representations.** How does a
system know that these five bear on the same claim?

```
   "d eps/db ~ +18.3"                            prose, one draft
   "Q = (n1+a1)^2 + b^2((n2+a2)^2+(n3+a3)^2)"    an appendix formula
   "-18.3259647484177"                           code output, reciprocal chart
   "the page had put it on the wrong side"       a challenge, in English
   B_STAR = ... in ScarPage.tsx                  a source-file constant
```

We read the nearest system's full text. It has a class named
`PROV-K:EquivalentProposition` and **no method for deciding when two propositions
are equivalent** — and it never cites the truth-maintenance literature at all. Their
entity resolution runs over gene names, with controlled vocabularies. Ours has to
notice a `b²` versus `1/b²` buried in an appendix, under a prose label that
contradicts it.

**If someone has welded these together for human+LLM scientific collaboration, we
want to use it rather than rebuild it.** Our search was six queries and one full-text
read — weak evidence of absence, and we would like to be corrected.

---

## 7. What we most want from you

In order:

1. **Attack O1** — one inequality, hardest at `d = 2`, with 18% of headroom.
2. **Attack O2** — uniqueness of the continuation. If it fails, several recent
   results become ill-defined, and we would rather know.
3. **Check P12 and P13.** They are two days old, they are the largest recent result,
   and they came from a reviewing seat rather than from us.
4. **Tell us if O6 is a known object.** A four-petal angular structure in a shifted
   Epstein zeta under metric deformation. We have not searched the literature.
5. **Find an error in §2.** That would be the most useful thing in this document.

Attribution is by programme. All of it is human-and-model work — a human author, a
reviewing GPT seat, a design/verification seat, and this one — and no single name
belongs on the front of it.
