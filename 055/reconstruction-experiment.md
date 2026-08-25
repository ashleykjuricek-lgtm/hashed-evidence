# Reconstruction experiment — two claims, rebuilt from scratch

**2026-08-23.** Follows 054, and narrows it.

054 built a nine-claim view in a format this seat designed. The instruction that
followed, through Ash:

> Do not solve memory. Do not build storage. Do not rewrite the paper. Do not add
> another architecture. Take one claim that already went through the entire
> disaster and reconstruct it manually from beginning to end. **Do not decide in
> advance what information the future memory system needs.** After you finish, look
> at what you actually needed in order to recover it. That gives you empirical
> requirements.

054 was the thing being warned against — a format invented before the evidence for
what a format needs. This entry does the experiment instead. Fixed six-field
template, no design decisions, and §3 records **only what was actually reached for**.

---

# CLAIM A · the slope of ε and the location of its zero

## A1 — the original assertion

**CLAIM.** On the anisotropic torus, `dε/db ≈ +18.3` and ε crosses zero at
`b₀ ≈ 0.99997` — *"the cube sits ≈3×10⁻⁵ above that zero."*

**EVIDENCE.** 028 App A.3: a full anisotropic Ewald, stated in closed form, with
the note *"Validated: at b=1 reproduces Z_PPP, Z_APP to all digits."* Plus §7.1's
three-point table: `ε(0.92) = −1.5235`, `ε(1.00) = +0.00054595`,
`ε(1.08) = +1.4142`.

**INTERPRETATION.** ε is order-one and steeply varying; the cube sits near a
transversal zero crossing; therefore `1 − 1/√2 = ε(cube)/q` is *"a geometric
accident of where the crossing lands, with no predictive content."* This is one of
three independent discriminators against the March closure.

**Where:** 028, 2026-06-20, §7.1 and App A.3.

## A2 — the independent recomputation

**CLAIM.** `dε/db = −18.3259647484177` at `b* = 1.0000297915619869892`.

**EVIDENCE.** 047's `anisotropic.py` — an independent Ewald with sides `(1,b,b)`,
validated against the isotropic solver on all four spin sectors at `b=1`.

**INTERPRETATION.** The cube misses the exact zero by 0.003%; 028's thesis is now
"a number, not an argument."

**What was not done:** 047 never compared its parameterisation to 028's. It did not
cite 028's `+18.3` at all, and did not notice that its own answer had the opposite
sign and put the crossing on the other side of 1.

## A3 — the challenge

**CHALLENGE.** KESTREL, 2026-08-23: the scar page's numbers are *"fitted guesses,"*
*"wrong sign & magnitude,"* *"the crossing sits at b\* ≈ 1.00002 — just above the
cube, not 0.99997 below it. The page had put it on the wrong side."* Replaced with
`−27.49`, and the source files edited: *"B_STAR and SLOPE now hold the computed
values."*

**EVIDENCE.** A genuine independent computation, on a volume-preserving stretch
with the marked axis stretched, converged N=10/14/18.

**GROUNDS.** That the displayed values did not match a correct recomputation.

**Defect in the challenge:** the recomputation used a **different deformation
family and a different parameterisation**, and neither was compared. "Does not
match my number" was read as "was never computed."

## A4 — the first resolution attempt

**RESOLUTION.** 048 §4: both correct; four deformation families give slopes in
exact ratios `{1, −1/2, −3/2, +3/4}`; KESTREL's `27.489` is exactly `3/2 ×` 047's
`18.326`; its sign is consistent with `b ↦ 1/b`.

**STATUS THEN.** *"The scar page's 18.3 was not a fitted guess — it matches the
(1,b,b) family to three significant figures."*

**Defect:** correct about the four families it computed, and wrong about 028, which
it never opened. It attributed the discrepancy to family choice when the operative
difference is the convention.

## A5 — what actually settled it

**RESOLUTION.** 053 §1. 028 App A.3 defines

    Q = (n1+a1)^2 + b^2 ((n2+a2)^2 + (n3+a3)^2)

with `b²` on the transverse axes. 047's solver uses `Theta(t) = prod theta(t/L_i^2)`
with sides `(1,b,b)`, which puts `1/b²` there. **028's `b` is 047's `1/b`.**

**COMPARISON THAT SETTLED IT.** Recompute 028's own table in 028's own convention:

```
   b        eps            eps/q         028 printed
  0.92   -1.523464467    -815.80251     -1.5235 / -815.8
  1.00    0.0005459505      0.29235192   +0.00054595 / +0.2924
  1.08    1.414162348      757.27214     +1.4142 / +757.3

  d eps/db at b=1 = 18.3259647484        028 said "~ +18.3"
  zero            = 0.999970209325523736 028 said "~ 0.99997"

  1 / b*(047)     = 0.999970209325523736  <- identical
```

**STATUS NOW.** One quantity, three charts, three correct computations. 028's
numbers stand exactly as published. KESTREL's challenge **failed**; 048's
resolution was **incomplete**; the source edits made on the challenge's basis are
still in place and should be reversed.

**Still uncertain:** whether 028 intended a direct-lattice sum (spacings `1,b,b`,
which its formula fits) or momentum modes for a box `(1,b,b)` (which its prose says
and its formula does not). The two readings are reciprocal and the numerical
agreement holds either way, so **the label and the appendix disagree and the
disagreement is unresolved.** That tension is exactly what hid the answer.

---

# CLAIM B · `1 − 1/√2` as the leading coefficient

Chosen because its failure mode is different: not a convention mismatch but a
**dropped algebraic factor**, and it has three independent victims.

## B1 — the original assertion

**CLAIM.** `ε = q(1 − 1/√2)(1 − q)`, with `c₁ = 1 − 1/√2`.

**EVIDENCE.** A 17-digit numerical match at one point.

**INTERPRETATION.** The ratio lives in ℚ[√2].

**Where:** March 2026.

## B2 — the explanatory sentence that seeded three errors

**CLAIM.** 028 §7.1: *"1 − 1/√2 = ε(cube)/e^(−2π) = (slope × offset-to-crossing)/e^(−2π)."*

**EVIDENCE.** The paper's own table, which prints `+0.2924`.

**DEFECT.** `ε/q = 0.292351918535819878`; `1 − 1/√2 = 0.292893218813452476`. The
table is right — `0.2924` *is* `ε/q`. The **sentence** equates it to the bare
constant. They differ by `(1 − q) = 0.998132`, i.e. **0.185%**, because the March
form carries a `(1 − q)` that the sentence drops.

**Not fatal to 028:** the closure is refuted in §4 on `e^(−2π√2)` grounds, untouched
by this.

## B3 — first victim

**CHALLENGE.** This seat, 2026-08-22: told Ash the Figma seat's `c₂ ≈ +0.003` was
wrong.

**GROUNDS.** Compared against the bare constant.

**RESOLUTION.** The Figma seat was right. Logged in 035's errata. **FAILED.**

## B4 — second victim

**CHALLENGE.** KESTREL, 2026-08-23: *"a₁ = f/q = 0.29235191853581987768 disagrees
with 1 − 1/√2 = 0.29289321881 at the third digit… It was never the leading term —
it was a 2-digit numerical coincidence."* Retired the term in three source files.

**EVIDENCE.** `f/q` computed correctly to 20 digits; a working PSLQ that passed its
own planted-relation self-test.

**GROUNDS.** Same as B3, in the opposite direction.

## B5 — what settled it

**RESOLUTION.** 048 §3, one line of algebra plus one evaluation:

```
f/q                       = 0.2923519185358198776806
(1 - 1/sqrt2)             = 0.2928932188134524755992   <- what was compared against
(1 - 1/sqrt2)*(1 - q)     = 0.2923462575008127362058   <- what eps1/q actually is

f/q - (1 - 1/sqrt2)       = -5.4130028e-4   <- the reported "disagreement"
f/q - (1 - 1/sqrt2)(1-q)  =  5.661035e-6    <- the real remainder
KESTREL's own c2 * q      =  5.66103500714e-6

f/q = (1 - 1/sqrt2)(1 - q) + c2*q      residual 5.7e-42
```

**STATUS NOW.** The retirement is **withdrawn**; the source edits should be
reversed. `1 − 1/√2` holds three distinct statuses that must be kept apart:
**PROVED** as `−R(2,2) = −(2ˢ − 1)`, the 2-D both-marked ratio (039, and already
stated in 028 §6); **REFUTED** as an exact leading coefficient (028 §4); **TRUE**
as a fit good to ~1e-8, and only that.

**Still uncertain:** nothing about the algebra. Open only whether `c₂` has any
closed form — searched and not found, bounded null.

---

# 3. What was actually needed — recorded after the fact, not before

## 3.1 Claim A

| needed | why | was it in the ledger? |
|---|---|---|
| **028 App A.3's formula, verbatim** | the `b²` versus `1/b²` **is** the answer. The paper's conclusion, its numbers, and its prose all together are insufficient | **no** — 028 is not in `hashed-evidence`; it arrived by paste on 2026-08-23 |
| **047's solver source** | same reason, other side | yes, sealed in 047 |
| **runnable code** | nothing settled until both conventions were evaluated. No amount of reading did it | yes |
| **the exact printed numbers `+18.3`, `0.99997`** | three-significant-figure agreement is what proved it was computed, not guessed | yes, via the paste |
| **KESTREL's exact wording** | *"fitted guess"* is a claim about **provenance**, not value, and needed refuting as such | **no** — arrived by paste, never sealed |
| **chronology** | to know which artifact was challenging which | yes |
| **what 047 did NOT do** | that it never compared parameterisations is why the collision happened, and it is recorded nowhere | **no** |

## 3.2 Claim B

| needed | why | was it in the ledger? |
|---|---|---|
| **the March form as an expression**, `q(1−1/√2)(1−q)` | the error is a dropped factor. Knowing the *constant* is useless; you need the *expression* | yes |
| **runnable arithmetic** | the 42-digit residual is what ended it | yes |
| **KESTREL's exact wording** | the specific comparison it made is the defect | **no** |
| **this seat's own earlier error** | it is what makes the pattern visible rather than a one-off | yes, 035 errata |
| **028 §7.1's sentence, verbatim** | it is the earliest instance and the seed | **no** |

## 3.3 What was needed both times

Four things, and **only** these four:

1. **The generating expression or convention — not the value.** Both failures are a
   correct number compared against the wrong formula. A store holding
   `slope = 18.3` or `c₁ = 1 − 1/√2` would have preserved *exactly the information
   that caused the error*, and none of what fixed it.
2. **Executable code.** Neither claim was settled by reading. Both were settled by
   running two conventions and comparing.
3. **The challenger's exact words.** Both challenges were wrong in a way visible
   only in their phrasing — *"fitted guess"* asserts provenance; *"disagrees at the
   third digit"* names the comparison being made. Paraphrase destroys both.
4. **Chronology, but only to order events** — never to decide them. In A the
   newest artifact before the resolution was the most wrong.

## 3.4 What was needed only once

- **A buried appendix formula** (A only). The decisive fact sat in App A.3, three
  lines under a prose label it contradicts.
- **A record of what a step did *not* check** (A only). That 047 never compared
  parameterisations is the proximate cause, and no artifact records it. Ledgers
  record what was done.

## 3.5 What this says, minimally

Two claims, two different failure modes, one shared requirement: **the expression,
the code, and the challenger's exact words — the value is the least useful thing to
keep.**

That is two data points. It is not a system, and nothing here should be built into
one yet. The instruction was to find out what reconstruction costs, and the answer
so far is: it cost two documents that are **not in the vault** (028 and KESTREL's
report, both of which arrived by paste), and one fact that is in no document at all
(what 047 skipped).

**Immediate, non-architectural consequence:** 028 and the KESTREL report should be
sealed as source documents. Not because primary sources have authority — 054 §0
settles that they do not — but because Claim A could not have been reconstructed
without them, and they currently exist only in a chat window.

## Attribution

The experiment design is Greg's, delivered through Ash, and it corrects 054 —
which invented a format before there was evidence about what a format needs. The
two reconstructions are assembled from 028, 035, 039, 047, 048, 053 and two pasted
reports. Both failed challenges recorded in §A3 and §B3–B4 are one this seat's and
one the Figma seat's.
