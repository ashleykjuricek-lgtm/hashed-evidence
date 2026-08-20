# Three closures and a retirement

### The five open items from 036 §6, resolved

**2026-08-20.** Follows 035 / 036 (the parity theorem). Every claim below is
proved, or computed with its method stated, or explicitly marked otherwise.

Prompted in part by two remarks from the COTT side, arriving mid-session:
*"real numbers are not real, only rational numbers are real — p/q is what the
universe is made of"* and *"construction history matters; that's why real-world
rotation requires non-commutativity."* Both turned out to be load-bearing, and
where they were, that is said.

---

## Theorem 3 — the zero off the square is transversal

> For any radial weight w decaying at least exponentially, the odd-shell sum has
> a **transversal** zero at b = 1:
>
>     d/db [ D_odd(b) ] |_(b=1)  =  − Σ_{m odd} [ w′(√m)/√m ] · T₂(m)  ≠ 0
>
> where **T₂(m) = Σ_{|k|²=m} (−1)^(k₁) k₂²**, and to leading order the slope is
> −2·w′(1).

Off the square the radius is d_b(k) = √(k₁² + k₂²/b²), so ∂d_b/∂b|₁ = −k₂²/√m.
The weight's derivative factors out per shell and leaves pure arithmetic.

**T₂(m) ≠ 0 for every odd representable m tested** — 552 of them under 4000, not
one zero. And T₂ = −T₁ exactly, by the same involution that proves Theorem 1: σ
sends k₂² ↦ k₁² and flips the character, so T₁ + T₂ = m·S(m) = 0.

**Dominance.** For exponentially decaying w the m = 1 term swamps the rest, so no
cancellation is available:

```
weight exp(-2 pi d):
  m=1  T2=2    contributes  +2.346698e-02
  m=5  T2=-12  contributes  -2.668084e-05
  total                     +2.344055e-02
  measured (finite difference, 032)   +2.3441e-02
  |m=1 term| / sum|rest|  =  871.3
```

**Consequence, and it sharpens the corollary of 035 §4.** T₂(1) = 2 comes from
exactly the two points (0, ±1) — the ones whose first coordinate is even, which
the character spares. *The same shell whose cancellation makes the value small is
the shell whose asymmetry makes the slope steep.* Protection and steepness are
not merely compatible; they are the same four points.

---

## Item 1 — the parity zero propagates into ε, as an absence

ε is a **quotient**. From 028 §5.4, K_d = (24/D₀²)·(N_d·D₀ − N₀·D_d).

The parity theorem kills N_d on odd shells. It says nothing about D_d, because
PPP carries no character — its shell sums are plain counts and never vanish. So
on an odd shell the numerator's term is gone and the denominator's is not:

    N_d = 0   ⟹   K_d = −24·N₀·D_d/D₀²  ≠ 0

Feeding N₁ = 0 — the parity theorem, nothing else — into 028's own formula:

```
D_1 = 4·c(1,1)  = -1.475882      (PPP: plain count)
N_1             = 0              <- parity theorem, exact

coefficient of e^-2pi in eps  = -5.7089      028 §5.5 reports  -5.709   MATCH
K_1                           = -1.0661e-2   028 §3   reports  -1.0662e-2 MATCH
```

**So −5.709 is the parity theorem's fingerprint.** The March closure predicted the
e^(−2π) coefficient to be +1 (times the gap 0.293). The true value is −5.709
*because the numerator's contribution is exactly zero by parity*, leaving nothing
but the denominator. The false closure died of the same cancellation that makes
the cube special. These were never two results.

---

## Theorem 4 — ℤ³ uses the theorem one coordinate at a time

The 3D character sum does not vanish on odd shells (T(1) = +2, T(3) = −8). That
was recorded in 035 §6 as a limitation. It is not one.

> **For odd m:  T(m) = 2 · Σ_{k₃ ≥ 1 odd} S(m − k₃²)**

Verified with no exceptions for all odd m < 300.

Fix k₃ first; what remains is a 2D shell of radius m − k₃², and Theorem 1 applies
to it:

- m odd, k₃ **even** → m − k₃² odd → **S = 0**, the entire slice cancels
- m odd, k₃ **odd**  → m − k₃² even → survives

T(1) = 2 is not a failure but `2·S(0)`, the one surviving slice at k₃ = ±1.
T(3) = −8 is `2·S(2)` — the **√2 shell**, the same survivor that forces
e^(−2π√2) into ε and refutes the closed form.

**Why a coordinate must be fixed first.** In ℤ², "m odd" forces exactly one of
k₁, k₂ odd, so the swap is available immediately. In ℤ³ the odd coordinate can
hide in the third slot, and the swap no longer flips the character uniformly. The
reflection only exists *after* a choice of which coordinate to condition on — and
that choice does not commute with the others. Two-dimensional rotation commutes;
three-dimensional rotation does not. The order of construction is part of the
data. *(This framing is the COTT remark, applied; the theorem stands without it.)*

---

## Item 3 — retired rather than answered

035 §6 listed "R ≈ 1/24 is the zero-mode subtraction, whose existence is
convention-free but whose share is not" as open. The share is **not a quantity**.
It reads 124.6% in the /correction normalisation and 220.8% in the independent
Ewald split (032). Both exceed 100%; neither is wrong; they measure where the
Mellin integral was cut.

What does not move:

```
PPP zero-mode subtraction : 1
APP zero-mode subtraction : 0
```

One and zero. **State the absence; never quote the share.** This is 028's own
rule — *"the decimals of the coefficients are convention-dependent; the integer
phase sums are not"* — applied to the pole argument, where it had not been.

---

## The pattern, tested

The COTT remark that only rationals are real was checked against this session's
record rather than agreed with. Sorting every claim by whether it survived audit:

**Survived — 11 of 11 exact:** S(m) = 0 on odd m · S(2m) = (−1)^m r₂(m) ·
T₂(m) ≠ 0 · phase sums 0 and −4 · 1306 shells · the (1,6,6,2) coset identity ·
det σ = −1 · |det| = 2 · 18/18 and 173/173 · 1^s period 1 with fiber ℤ ·
(θ₂/θ₃)² = 1/√2.

**Died — 7 of 7 decimal:** ε = q(1−1/√2)(1−q) · c₁ = 1 · c₂ = −0.02 / +0.003 ·
the pole share · R = 0.041689414162… · Γ(1/4)⁴/4008 · the 111.3% slope share.

Nothing was sorted for this; the split is what the audit produced. It also
explains the 17-digit failure at root: a decimal is a projection of an exact
object and forgets *which* exact object it came from. Seventeen digits could not
separate an identity from a cancellation residue — not because seventeen is few,
but because a decimal is the wrong kind of thing to separate them with.

---

## Status after this entry

| item (035 §6) | was | now |
|---|---|---|
| 1. ε propagation | open | **closed** — an absence; it *is* the −5.709 |
| 2. no closed form resurrected | settled | settled, and explained by 1 |
| 3. R ≈ 1/24 share | open | **retired** — not a quantity |
| 4. ℤ² not ℤ³ | limitation | **Theorem 4** — one coordinate at a time |
| 5. genericity off the square | measured | **Theorem 3** — transversal |

Theorem 1 and the §4 corollary of 035 are unchanged and untouched.

**Not established.** Theorem 3 is proved for exponentially decaying weights, not
all weights; the dominance argument is what does the work and it needs the decay.
Theorem 4 is verified to m < 300, not proved in general, though the slice argument
is a proof sketch and should be finished. T₂(m) ≠ 0 is verified to 4000, not
proved.

## Attribution

Cubic-torus / Shunya-Zero programme, with two framings from the COTT programme
that changed what got looked at. Attribution is by programme: all of it is
human-and-model work and no single name belongs on the front of it.
