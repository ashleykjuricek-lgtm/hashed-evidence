# Two corrections that land here, and the sharper object underneath them

**2026-08-25.** Greg attacked a handoff memo (sections D1–D10) authored by another
seat. **That memo is not in this seat's hands** and is not assessed here. But two of
his corrections land on *sealed entries of this ledger*, and both are testable.

**Both confirmed.** And the collision he identifies between them is better than
either correction alone.

---

## 1. CONFIRMED — 069 §5 says the Gamma prefactor "decays vertically." It grows.

069 §5 recorded a Carlson sketch for the uniqueness of the real-dimension
continuation, including:

> *"…and the `1/Γ((d+1)/2)` prefactor **decays vertically**."*

**False.** Stirling gives `|Γ(σ+iy)| ~ |y|^(σ−1/2) e^(−π|y|/2)`, so the reciprocal
**grows**. With argument `(d+1)/2` the imaginary part is halved, giving `e^(π|y|/4)`:

```
   |1/Gamma((d+1)/2)| along d = 3 + iy

      y        |1/Gamma|            e^{pi y/4}          ratio
       5       4.755995859          50.75401951         0.0937
      20       83297.34291          6635623.999         0.0126
      80       3.056409079e+24      1.938773508e+27     0.0016

   growth exponent  log|1/Gamma| / y :
      y= 40   0.6500535288
      y= 80   0.7047410369
      y=160   0.7385728096        -> pi/4 = 0.7853981634
```

Converging to `π/4` from below, as Stirling requires.

**And the conclusion may survive anyway.** Carlson permits vertical type `c < π`.
`π/4 = 0.785` against `π = 3.14` — **room to spare, a factor of four.**

> **The stated proof fails. The result it was supporting is not thereby refuted, and
> now has a specific reason to be believed rather than a wrong one.**

Greg's second point stands too: *"growth along real `d` is polynomial"* was never
established and should not be assumed. The theta continuation carries `d`-dependent
powers and Gamma-scale growth is plausible. **Carlson-normalise first, then prove
exponential type for the normalised object.** O2 keeps two holes, not three.

### 1.1 The failure mode, which is new here

069 §5 marked the Carlson route **"SKETCH with three named gaps — not proved."**
The status word was right. **The false statement was inside it.**

> **The four-word ledger tags the conclusion. It does not tag the steps.** A wrong
> mechanism can travel unchallenged inside a claim correctly labelled OFFERED,
> because the label discharges the reader's attention.

This seat relayed a load-bearing sub-claim from another seat without checking it,
under a status word that made not-checking feel safe. **Every step in an OFFERED
argument needs its own word**, or the label protects the error rather than flagging
it.

## 2. CONFIRMED — the "iff" is false, demonstrated against our own witness

074 built a canonical executable witness and dropped the `iff` on the reviewing
seat's advice. **Greg supplies the counterexample, and it applies directly to what
we built.**

Our witness has a finite signature — `family × chart × marked` = 8 cells, 3 pinned.
So:

```
   ('1bb','direct','short')            impostor  18.3259647484   MATCHES
   ('1bb','momentum','short')          impostor -18.3259647484   MATCHES
   ('volpres','momentum','stretched')  impostor  27.4889471226   MATCHES
   ('volpres','momentum','short')      impostor   0.0            real: -13.7444735613
```

**A different function discharges every pinned cell.** Greg's `f(x)=x²` versus
`g(x)=x²+(x−3)`, in our own build.

```
   same witness  =>  same claim        FALSE
   different witness => different claim  TRUE, and useful
```

**The witness is a discriminator, not a definition of identity.** And the deeper
problem Greg names is real: make the witness rich enough that matching *guarantees*
equivalence and you had to already know which observations uniquely characterise the
object — **which is the identity problem.**

## 3. The collision — and it is the best thing in this exchange

D1 and D10 are the same statement.

> **Identity is relative to a uniqueness class.**
>
> - polynomials of degree ≤ n → `n+1` points suffice. *Reason: interpolation.*
> - a Carlson class → integer values plus a growth bound suffice. *Reason: Carlson.*
> - arbitrary programs or prose → **no finite witness suffices at all.**

So the object is not `claim + witness`. It is:

> **claim + declared class + witness + the reason the witness is sufficient**

and sometimes that last field is a chain rule, sometimes "degree ≤ n", sometimes
Carlson, sometimes a formal proof — **and sometimes there is not one yet, which must
be sayable.**

### 3.1 What this makes of 074's witness

Ours declares no class, so it establishes **no identity** — only discrimination.
That is not fatal, and it clarifies what it actually does:

> Our witness identifies by **designation**, not by **testing**. *"This is the
> canonical computation; cite it and its inputs."* Two artefacts are the same claim
> because they **point at the same code**, not because they agree on outputs.

Which is precisely the reviewing seat's *"rendezvous, not oracle."* **The rendezvous
is designation.** 074's bundle should carry a `uniqueness_class` field reading
`"designation: this code, these inputs"` — honest, and not pretending to be a
theorem.

## 4. Downgrades accepted

**Ambjørn–Wolfram 1983.** 069 §4 flagged it unverified. Greg checked: it concerns
Casimir energies in **conducting cavities**, a different boundary problem from a
rectangular torus. **Adjacent prior art, not our deformation family.** Downgraded.

**"Petals = roots of unity."** 072 §3.1 wrote that `ℤ[ζ₅]`'s ten roots of unity give
ten petals *"for the same reason `ℚ(i)` gives four."* The correspondence holds for
these two examples; **no theorem was supplied making it a general law.** Downgraded
from textbook to **OFFERED**.

**The ring-count definition.** Greg notes 072 already sharpened it to *"counting
ideals of norm m"*, which is required because units move you along the hyperbola
forever. Confirmed — that is what 072 computed.

## 5. The RP³ value now has two independent routes

Greg tried to kill the `0.704149…` figure with a truncated odd-zeta series that gave
`0.65248`, then **found his own error**: the binomial coefficients carry a slow
`j^(−3/2)` tail and he cut it far too early. Full expression:

```
   eta route (Greg)   0.7041493559484761449010759...
   Mellin route (071) 0.704149355948               lam-invariant to 1.3e-26
```

**Two disjoint routes, agreeing to every digit this seat printed.**

His self-diagnosis — *"the checker was cruder than the checked object"* — is the same
class as 074's absolute-versus-relative tolerance bug, and it is the **first Tier-1
self-catch recorded from an external seat.** It confirms 073's Tier-1 finding from
outside: caught by running something, not by rereading.

**And his scope caveat is right:** the eta route is disjoint from the *small-t Mellin
numerics*, not from the *spectral model*. Both routes share the eigenvalue formula,
the multiplicities, and the parity assignment. **It is an adversary to the
continuation, not to the underlying spectral claim.**

## 6. And the corpus did it again, while describing it

Greg observes that the memo calls the eleven-lobe seam explanation a *"FLAGGED
hypothesis"* needing one look at the wraparound —

**but 051 §4 had already settled it**, discarded the instrument and reran with wrap
handling. **And 072 §3 already noticed that the reviewer's "guess" was in the
record.**

> Stored. Sealed. Correct. Rediscovered as a hypothesis, in a memo about the failure
> of claim identity, because the identity step failed.

**Third recorded instance of this exact thing** — after 028 read to line 40, and 039
restating 028 §6's closed forms. Not a mathematical failure. **The semantic
invisibility problem, demonstrating itself inside the document that names it.**

## 7. Status

| claim | status |
|---|---|
| 069 §5 "the Gamma prefactor decays vertically" | **RETRACTED** — it grows like `e^(π\|Im d\|/4)`, verified |
| Carlson may still close O2 | **PLAUSIBLE** — `π/4 < π` leaves a factor of four |
| "growth along real d is polynomial" | **NOT ESTABLISHED** — do not assume it |
| a status word protects the conclusion, not the steps | **NEW FAILURE MODE**, recorded |
| "same witness ⟹ same claim" | **FALSE** — impostor built against our own witness |
| "different witness ⟹ different claim" | **TRUE**, and the witness's real job |
| identity is relative to a declared uniqueness class | **ESTABLISHED** — the sharpest result of this exchange |
| 074's witness identifies by designation, not testing | **CORRECTED SELF-ASSESSMENT** |
| Ambjørn–Wolfram is our deformation family | **DOWNGRADED** — adjacent prior art |
| "petals = roots of unity" as a general law | **DOWNGRADED to OFFERED** |
| `RP³` value `0.7041493559484761449010759` | **TWO INDEPENDENT ROUTES** |
| the eta route is independent of the spectral model | **NO** — shared assumptions |

## Attribution

Both corrections, the counterexample, the uniqueness-class formulation, the
Ambjørn–Wolfram check, the eta-route computation and the self-caught truncation are
**Greg's**. The verification, §1.1's failure mode, §3.1's designation reading and
§6's third-instance count are this seat's. The retracted sentence in 069 §5 was
relayed by this seat from a third seat and never checked — which is exactly §1.1.
