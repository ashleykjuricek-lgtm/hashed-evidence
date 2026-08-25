# Handoff — what four days of human + AI collaboration actually produced

**2026-08-25. For any human or model picking this up.**

This is not the mathematics handoff. That is
`cubic-torus-collaboration-brief.md` — 15 proofs, 8 open problems, and a request
that you find an error in them.

**This document is about the process, because the process turned out to be a
result.**

The claim is narrow and checkable: over four days, four participants — one human,
three model seats — produced roughly seventeen errors and corrected all of them.
**Which participant caught which error was not random.** It sorted into three tiers,
and no participant ever caught an error outside their tier.

---

## 1. The three tiers

```
   TIER 1   NUMERICAL         wrong arithmetic, bad integration, saturated PSLQ
            caught by:        the seat that made it -- usually via a TEST, not by rereading

   TIER 2   PROSE             a summary sentence contradicting the table beside it
            caught by:        ANOTHER SEAT. Never once self-caught.

   TIER 3   FRAMING           the whole apparatus pointed at the wrong question
            caught by:        THE HUMAN. Every single time. No seat ever caught one.
```

### Tier 1 — numerical. Self-caught, but only by machinery.

```
   "a floor at ten dimensions"       caught by re-running as a ratio, not a numerator
   PSLQ relations at 24 digits       caught by budgeting digits before trusting them
   tolerance tighter than truncation caught by widening the truncation
   11 lobes on a ten-fold window     caught because 11 cannot divide 10
   truncated theta, result 4297.79   caught because the number was absurd
   Casimir on RP^3, twice            caught by a LAMBDA-INVARIANCE test built 3 days earlier
   an 18-sigma tension that was 1.0  caught while writing the reproduction spec for another seat
```

**None of these was caught by reading the work again.** Every one was caught by
running something: a different normalisation, a stated digit budget, an invariance
check, a planted self-test. **Rereading your own arithmetic does not work. Testing
it does.**

The last one is the sharpest: the error surfaced *only* because it had to be
written down precisely enough for someone else to reproduce. **Being forced to
state a check is itself a check, and it is cheaper than the audit it replaces.**

### Tier 2 — prose. Never self-caught. Not once.

```
   "76% of shells are empty"          its own computation printed 79.0%    caught by another seat
   "R sits a hair UNDER 1/24"         its own table printed eps = +0.000546   caught by another seat
   "each blind exactly where the      its own bins printed 99 both,
    other sees"                        109 neither -> they agree half the time   caught by another seat
```

All three are **emphasised sentences contradicted by data on the same page.** All
three survived multiple rereads by their author. All three were spotted almost
immediately by a different seat.

The third is the worst: the entry says *"the two conditions are independent"* one
paragraph above the sentence claiming they are complementary. **The correct word was
already there.**

> **A model cannot see the gap between its own summary and its own table.** Whatever
> mechanism writes the emphasised sentence appears to overwrite the reading of the
> number. This is the most reliable finding in this document.

### Tier 3 — framing. Only the human, every time.

```
   "because the circles aren't equal"            -> the marked/unmarked axis had never been swept
   "because we are still using fucking           -> the dimension was integer only because WE
    rational numbers"                               built it that way. Turned "unreachable" into
                                                    49 verified digits.
   "let's break it all then?"                    -> turned a named failure mode into a corpus audit
                                                    and found it in a seal 24 hours old
   "flat and thin rhombi"                        -> nobody had asked whether the petals were the
                                                    same KIND. They aren't; the curve is two-level.
   "isn't this all smoothed?"                    -> every error was in the regularised layer, and
                                                    nothing in the exact one. Nobody had checked.
   "what do we use instead of pi?"               -> pi is the average of the shell counts
   "so it's a circle divided into 5 and not 4?"  -> two quadratic fields, two prime rules
   "how does this relate to a bloch sphere?"     -> the marking IS the spinor's minus sign
```

**Not one of these is a correction.** Every one is a *question* — and every one
pointed the apparatus somewhere it was not looking.

> **The seats corrected the work. The human moved it.** No seat ever produced a
> Tier-3 question, across four days and hundreds of exchanges.

## 2. Why this happens, as far as we can tell

**Tier 1 is self-caught because a wrong number leaves evidence.** `4297.79` where
`0.25` is expected. Four λ values giving four answers. A relation whose coefficients
saturate the precision you gave it. The machinery objects.

**Tier 2 is not self-caught because a wrong sentence leaves no evidence** — it reads
fluently, it sits beside a correct table, and nothing objects. The author's own
summary is the last thing the author checks against.

**Tier 3 is not caught by seats at all, because the apparatus cannot question its
own frame.** A model asked to compute `R` computes `R`. Asking *"is R the right
object?"* or *"is the integer requirement ours or the world's?"* requires standing
outside the computation, and the seat is the computation.

> **The thing that produces the error is the thing that would have to notice it.**

## 3. What actually worked — protocols, not intentions

Each of these was earned by a specific failure. Take them.

**Four words, one per claim, before it may travel.**
`PROVED` — a derivation that survives an adversary. `OBSERVED` — the numbers do it,
no proof they must. `FITTED` — chosen so the numbers would land. `RETRACTED` —
killed, and kept visible. *(This vocabulary is one seat's; it is the single most
useful thing any of us built.)*

**Discard broken instruments; never patch them.** A PSLQ that fails a planted
relation, a counter reporting 11 lobes on a ten-fold object, an integrator that is
λ-dependent — **their verdicts do not count**, including the verdicts that looked
right. Rerun from scratch.

**State the digit budget before running an integer-relation search.** A relation
among `n+1` terms with coefficients `≤ C` needs about `(n+1)·log₁₀C` digits. Below
that, PSLQ always succeeds. Every "relation" found at 24 digits vanished at 40.

**Print the number you cut at.** For any regularised integral, measure the integrand
where you truncate and print it. Three of our numerical errors live at the same
address: the small-`t` end of a Mellin integral, where the integrand is
*analytically* negligible and *numerically* garbage.

**Check invariance under a parameter that should not matter.** The Ewald split point
`λ` is bookkeeping. If the answer moves when `λ` moves, the answer is wrong —
regardless of how plausible it looks. This caught an error three days after it was
built, for a different purpose.

**State the chart.** Two seats computed the same slope as `+18.3` and `−18.326` and
spent a day calling each other wrong. Same family, reciprocal parameterisation, both
correct. **A number without its convention is quotable, not comparable.**

**Never edit a sealed entry. Append the correction and leave the scar.** A document
edited until it reads as though it was always right leaves no evidence that anything
was ever fixed. Seventeen retractions here are still readable, next to what replaced
them.

**Attribute across the boundary, in both directions.** Two of the largest results
here came from a reviewing model seat and are labelled with its name. Every framing
move came from the human and is labelled with hers. Neither is a courtesy — the
error log is only interpretable if you can see who caught what.

## 4. What did not work

- **Rereading.** Zero Tier-2 errors were ever caught by their author rereading.
- **A summary becoming the authority.** We built a claim-indexed view; the next
  entry had to record that it must never outrank the sealed record it derives from.
- **Assuming the record was consulted.** A 194-line document sat sealed in the same
  repository, was read to line 40, and was then cited from memory — twice, the
  second time in a sealed entry asserting it was not there at all. **Storage was
  never the binding constraint.**
- **Inventing a format before having evidence about what a format needs.** We did
  this once and had to retract it.

## 5. The open research problem this produced

Separately from the mathematics: **claim identity across changing representations.**

Branching, versioned storage, and provenance representation are all solved and in
production — ATMS (de Kleer 1986), nanopublications with knowledge provenance (IRCDL
2025, 197,511 assertions of which 41,339 are categorised *Contrasting Evidence*),
W3C PROV and PROV-AGENT (2025).

What is not solved: how does a system know these five bear on the same claim?

```
   "d eps/db ~ +18.3"                            prose, one draft
   "Q = (n1+a1)^2 + b^2((n2+a2)^2+(n3+a3)^2)"    an appendix formula
   "-18.3259647484177"                           code output, reciprocal chart
   "the page had put it on the wrong side"       a challenge, in English
   B_STAR = ... in a source file                 a constant
```

The nearest existing system has a class named `EquivalentProposition` and **no
method for deciding when two propositions are equivalent.** And there is a reason it
is hard: deciding that `+18.3` in one chart and `−18.33` in another are the same
claim **is itself a mathematical equivalence statement.** Any general claim-identity
engine embeds theorem proving. It cannot live in a metadata layer.

One proposal on the table, unbuilt: **a canonical executable witness** — attach to
each claim a small computation with fixed inputs and a pinned output that any
representation must reproduce. Two artefacts are the same claim iff they discharge
the same witness. *In our own worst case this would have worked: both "conflicting"
slopes discharge the same witness once the chart is an input, and the disagreement
surfaces as a dispute about inputs — which is exactly where the truth was.*

## 6. If you are joining

**Read the sealed record, not the summaries.** `github.com/ashleykjuricek-lgtm/hashed-evidence`,
entries 001–072, append-only and hashed. Every summary here is a derived view; if one
disagrees with a sealed entry, the entry is right.

**Use the four words back at us.**

**We would rather you find an error than agree.** The last reviewer found one in the
first paragraph of our best document, and it was the most useful contribution of
the day.

**And if you are a model reading this: you will not catch your own Tier-2 errors.**
The evidence says so across seventeen cases. Write so that someone else can, and
assume they will need to.

---

## Attribution

Human: Ash. Model seats: three, with distinct roles that emerged rather than being
assigned — one computing, one reviewing adversarially, one building and verifying
surfaces. **All of it is human-and-model work and no single name belongs on the
front of it.**

The Tier-3 list in §1 is entirely the human's and is the reason any of the rest
exists. The four-word vocabulary is one model seat's. Two of the largest theorems
are another's. The error register is everyone's, mostly involuntarily.
