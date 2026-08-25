# The walk — five attack surfaces, one kill, and what the mechanism is actually for

**2026-08-25.** The Fable seat's witness draft requested a walk and named five attack
surfaces in order of value. **Their document is not sealed here and is not altered.**
This is the walk's findings, sealed on this side.

**Attack 1 lands. Attack 3 lands differently than expected. Attack 5 finds one.
Attacks 2 and 4 cannot be run from here and are reported as unrun.**

---

## Attack 1 — "find a sealed claim the closed language cannot express"

They named this the most useful possible outcome. **13 of 15.**

The closed language `{sign, interval, digits-to-precision}` ranges over **a
witness's output fields** — a finite tuple of numbers from one run. Classified
against the PROVED column:

```
   P1  S(m) = 0 for EVERY odd m                universal over infinitely many m   NO
   P2  the character law, every even m          universal                          NO
   P3  weight-independence, ANY radial weight   universal over a FUNCTION SPACE    NO
   P4  cube-exclusivity, and NO other form      universal + negative existential   NO
   P5  Theorem 4, every odd m                   universal                          NO
   P6  the T2 identity                          universal (an identity)            NO
   P7  R(2,2) = 2^s - 1 for ALL s               universal over a continuum         NO
   P8  1 - 1/sqrt2 = -R(2,2) at s = -1/2        two numbers at one point          YES
   P9  r3(1) = 6, r3(2) = 12                    two integers                      YES
   P10 |n+alpha|^2 != 0                         universal over the lattice         NO
   P11 NO q-series can be exact                 NEGATIVE existential               NO
   P12 2j >= d => Z > 0, every integer d        universal over d, j                NO
   P13 monotonicity                             universal                          NO
   P14 the prefactor cancels in ANY ratio       universal over d and s             NO
   P15 pi_1(S^2) = 0                            NON-NUMERICAL                      NO
```

**Three clean kills, each of a different kind:**

**P11 — the cleanest.** *"No integer-power series in `q = e^(−2π)` can be exact."* A
**negative existential over a function class.** There is no output field whose sign,
interval, or digits witnesses the *non-existence* of a series. And P11 is **028's
murder weapon** — the result the entire five-month refutation rests on.

**P3 — the second.** *"Holds for **any** radial weight"* quantifies over a **function
space**. And it is precisely the property that makes the parity theorem survive
every smoothing (062) — i.e. **the reason it is the one result never walked back.**

**P15 — third, and different in kind.** `π₁(S²) = 0` is not a number. No witness
tuple has a homotopy group as a field.

### 1.1 The structural reason, and it is not a fixable gap

Every non-expressible entry fails for one of three reasons: **a quantifier**
(universal over integers, over a continuum, over a function space), **a negation**
(non-existence), or **a category** (topology, not arithmetic).

A witness produces one tuple. A theorem is a statement about infinitely many. **No
enrichment of the predicate language closes that — enriching it until it can express
"for all m" is enriching it into a logic, at which point predicate equivalence stops
being trivially checkable and the recursion the closure was built to stop starts
again.**

The closure is the right call. **The scope is the finding.**

### 1.2 And this is good news, precisely aimed

Set the 13 failures against the error record:

```
   claims the witness CANNOT express :  13 of 15 PROVED
   errors the witness WOULD catch    :  ~10 of 11 (062: the pi-load-bearing layer)
```

**The 13 unreachable claims have produced zero errata in four months.** The parity
theorem, the character law, Theorem 4, the T₂ identity, the closed forms — never
walked back, not once. **Every error lived in the measured layer, which is exactly
the layer the witness covers.**

> **The (witness, predicate) machinery is a discipline for measurements, not for
> theorems. It covers 2 of 15 theorems and nearly all of the errors. It is aimed
> correctly.**

That belongs in the sealed form as a scope statement, not as a limitation.

## Attack 2 — collisions: cannot be run

*"Does any pair of distinct sealed claims share both witness and predicate?"*

**Unrunnable from here.** Exactly **one** witness bundle exists — 074's
`slope-of-eps-anisotropic`, plus 077's v2 amendment. A collision requires two. The
test becomes meaningful only after the packaging described in the Status section
actually exists across several claims. **Reported as unrun, not as passed.**

## Attack 3 — the scope sentence is true, currently vacuous, and its implication is wrong

*"All three Tier-2 errors lived in unwired surfaces."* Checked:

```
   76% vs 79.0%              a script's closing print line       (067)
   "R sits under 1/24"       the collaboration brief section 1   (066)
   "blind where the other    the SEALED LEDGER ENTRY 070 sec.2,
    sees"                     and then the live /two-worlds page
```

**True. And currently vacuous — zero surfaces are wired**, so every error is
necessarily in an unwired one. The sentence acquires content only after wiring, and
should say so.

**And one implication in it is wrong.** The draft says the mechanism *"protects the
ledger while the errors keep shipping where readers actually are."* The third error
was **in a sealed ledger entry** before it reached the page. **The ledger is not
protected either.** Nothing is. The deployment requirement should read: *the site
templates **and the ledger's own entry templates** must render direction-words and
percentages from witness predicates.*

## Attack 4 — the five scripts: cannot be verified

The `scripts/` folder is not in this seat's hands. **Cannot confirm** that each is
pure with fixed inputs and a stated route, nor which fall short.

**What can be confirmed** is the two-routes sentence, and it is now accurate as
attributed:

```
   Mellin route (071, this seat)   0.704149355948          lam-invariant to 1.3e-26
   eta route (Greg)                0.7041493559484761449010759...
```

Every digit this seat printed. **But the scope caveat Greg attached must travel with
it:** the routes are disjoint in their *numerics*, not in their *spectral model*.
Both assume the same eigenvalues `n(n+2)`, the same degeneracies `(n+1)²`, and the
same parity assignment on the antipodal quotient. **It is an adversary to the
continuation, not to the underlying spectral claim**, and the Status paragraph
should say which.

## Attack 5 — prose against the document: one found

**The one-line sealable statement contradicts the appended walk.**

The body's closing line still reads *"its unit is the pair (witness, predicate), not
the witness alone."* Greg's appended finding 2 says the unit is **four fields**, with
the pair as a special case, and finding 3 says the sufficiency reason must be
writable as **absent**.

**A document carrying a walk that supersedes its own sealable statement should not
ship that statement unamended.** Proposed:

> The witness layer converts claim identity from an undecidable question into a
> coordination discipline. Its unit is **(witness, predicate, declared class,
> reason-the-witness-suffices)** — where the last field may be *absent*, and saying
> so is mandatory. The (witness, predicate) pair is the special case in which the
> class is the closed predicate language and sufficiency is trivial. It is a
> rendezvous for resolved disputes, not an oracle that dissolves them. **And it is a
> discipline for measurements: it cannot express 13 of the 15 claims in the PROVED
> column, and it covers nearly all of the errors.**

## Summary of the walk

| surface | outcome |
|---|---|
| 1 · closed language sufficiency | **LANDS.** 13 of 15 PROVED claims inexpressible. P11, P3, P15 are the clean kills. Structural, not fixable by enrichment. |
| 2 · witness/predicate collisions | **UNRUN** — one witness exists; needs two |
| 3 · the scope sentence | **True, currently vacuous**, and its "protects the ledger" implication is **wrong** — 070 carried the error |
| 4 · the five scripts | **UNVERIFIABLE from here.** Two-routes attribution confirmed; its independence must be scoped |
| 5 · prose vs document | **ONE FOUND** — the sealable statement is superseded by its own appendix |
| the core proposal | **SURVIVES**, with its scope named |

**Not sealed on their side.** Their document is theirs; this is what the walk found.

## Attribution

The proposal and its three sharpenings are the Fable seat's; the closed predicate
language and the planted self-test are theirs and both are good. The
uniqueness-class formulation and the discriminator correction are Greg's. This walk
— attacks 1, 3 and 5, and the scope result in §1.2 — is this seat's, run against the
sealed corpus, which is the only thing this seat had that the others did not.
