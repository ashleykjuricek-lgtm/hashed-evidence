# Branch, not reconstruct — tested against the two claims

**2026-08-24.** Follows 055. The proposal, from Greg through Ash:

> Not `claim₀ → correction₁ → correction₂ → current truth`, because that linearizes
> history and silently destroys the alternatives. Instead: **persistent branches +
> common ancestry + evidence attached to each branch.** 053 does not overwrite 048.
> It forks from the same history and says *"here is a different resolution of that
> apparent conflict."* A wrong correction doesn't destroy the correct earlier state.
> A retraction is itself a branch, not an eraser.
>
> **A scar is not necessarily a summary of the past. It can be the branch point.**
> The thing worth preserving is: *"something diverged here."*

This is better than 054's format and better than 055's linear reconstructions. It is
also a proposal, so it gets tested against the same two claims rather than adopted.

**Result: it works, it exposes a node type neither of us had, and it does not do the
one thing Claim A actually needed.**

---

## 1. Claim A as a branch set

```
ANCESTOR:  "the anisotropic deformation of eps near the cube"

 |-- 028      2026-06-20   +18.3   at b0 = 0.99997
 |            evidence: App A.3, direct-lattice, spacings (1,b,b)
 |
 |-- 047      2026-08-23   -18.3259647484177  at b* = 1.0000297915619869892
 |            evidence: anisotropic.py, momentum modes, sides (1,b,b)
 |
 |-- KESTREL  2026-08-23   -27.49  at b ~ 1.00002
 |            evidence: its own code, volume-preserving stretch, marked axis stretched
 |            + an assertion ABOUT another branch: "028's is a fitted guess"
 |
 |-- 048      2026-08-23   "the branches differ by deformation family"
 |
 |-- 053      2026-08-23   "028 and 047 differ by b <-> 1/b; same family"
```

**Two things fall out immediately.**

**(a) There are two kinds of node, and only one is a branch.** 028, 047 and KESTREL
assert things about *the object*. 048 and 053 assert things about *the relation
between branches* — they are edges, not branches. Greg's model has only branches;
this needs both, because the entire dispute was resolved by an edge claim and the
first edge claim was wrong.

**(b) KESTREL's failure has a precise shape in this picture.** It made an assertion
about **another branch's provenance** — *"fitted guess"* — while holding that
branch's **values** (off the scar page) but not its **evidence** (App A.3's
formula). A branch whose evidence is not attached is not comparable; it is only
quotable. That is exactly what happened.

## 2. Claim B as a branch set — this one works cleanly

```
ANCESTOR:  028 section 7.1, the sentence "1 - 1/sqrt2 = eps(cube)/e^(-2pi)"

 |-- cubic-torus seat  2026-08-22   "the Figma seat's c2 = +0.003 is wrong"
 |-- KESTREL           2026-08-23   "a1 disagrees at the 3rd digit; retire the term"
 |-- 048               2026-08-23   EDGE: "both dropped the (1-q); residual 5.7e-42"
```

Three independent forks from **one sentence**, two of which are wrong in the same
way and neither of which overwrote the other. The branch model handles this
perfectly, and it makes visible something the linear account buried: **the ancestor
is a sentence, not a value.** The number in 028's table was always correct. The
prose is what forked.

## 3. Where it does not do the work

> **Branching preserves alternatives. It does not detect divergence.**

028 and 047 coexisted for hours as though they agreed. Nobody collapsed them —
nobody *noticed* them. 047 produced a slope with the opposite sign and a crossing on
the other side of 1, and flagged nothing, because it never cited 028 and never
compared conventions. There was no collapse to prevent. **There was a fork nobody
knew had happened.**

A model whose guarantee is *"conflicting states were never collapsed"* does not help
when the conflict was never recognised as one.

### 3.1 But it is recoverable, and the reason is specific

A fork *is* mechanically detectable — two nodes under one claim label with
different values is an automatic signal. That did not fire here for a concrete
reason:

> **028 has never been in the vault.** It arrived by paste on 2026-08-23. There was
> no ancestor node for 047 to fork from. **047 was not a branch. It was a fresh
> root**, and a fresh root cannot conflict with anything.

Same for the KESTREL report, which exists only in a chat window. 055 §3.3 found this
from the other direction — both documents were required to reconstruct Claim A and
neither is sealed.

So the branch model's precondition is not a format. It is: **everything that makes a
claim has to be a node.** Ours weren't.

### 3.2 And detection needs the expression, not the value

055 §3.3 found that both reconstructions needed the *generating expression or
convention*, never the value. That result and this one compose:

- two branches labelled `slope` holding `+18.3` and `−18.326` look like a
  contradiction — which is a **false** alarm; they agree;
- two branches labelled `slope` holding `Q = (n₁+a₁)² + b²(…)` and
  `Θ(t) = Π θ(t/L_i²)` are visibly **different questions** — which is the true
  state.

**Storing the value makes forks look like contradictions. Storing the expression
makes them look like what they are.** Value-level branching would have raised a
false alarm here and no alarm at all in Claim B, where every number was right.

## 4. The vault already had the mechanism and has never used it

```
total commits : 58
branches      : 4
merge commits : 0
```

`hashed-evidence` is a git repository whose entire history is a straight line. Every
correction has been appended as the next numbered folder on one trunk.

**This is not a call to restructure it.** The linear seal chain is what makes the
vault tamper-evident, and folder numbers are what make citations stable. The
branching belongs **in the content**, not in git's DAG. But it is worth recording
that the shape Greg is describing is the shape of the tool the vault has been
running on top of, unused, for 56 entries.

## 5. What a branch point has to carry — derived, not designed

From A and B only. Nothing here is invented to be complete.

| field | why, from the evidence |
|---|---|
| **the generating expression or convention** | §3.2. Both claims; the only field that distinguishes a real conflict from a chart change |
| **the assertion, verbatim** | Claim B's ancestor is a *sentence* whose table was correct. Paraphrase erases the fork |
| **runnable code** | neither dispute was settled by reading; both by running two conventions |
| **what the author did *not* compare** | A's proximate cause. Recorded in no artifact, then or now |
| **edge claims, as their own nodes with their own verdicts** | §1(a). 048 and 053 are both edges on the same pair; one is incomplete and one is right |

**Not needed, both times:** the value on its own, and any priority rule — document,
chronological, or otherwise. In Claim A the newest artifact before the resolution
was the most wrong one.

## 6. What is still not solved

- **Undetected forks**, when the label differs or is absent. §3 gives a mechanism
  only for same-label divergence.
- **Whether "what wasn't compared" is recordable at all.** It is a negative fact
  about an author's attention. Both claims needed it; nothing produces it.
- **Scale.** Two claims, by hand. Same caveat as 055.

## 7. The one concrete action, and it is not architecture

> **Seal 028 and the KESTREL report as source documents.**

Not because primary sources have authority — 054 §0 settles that they do not, and
028 is the standing counterexample, holding the false closure and the evidence that
kills it in one file. But because **Claim A was unreconstructable without them**,
they were the ancestor nodes that never existed, and they currently live in a chat
window.

That is the whole action. No format, no store, no system.

## Attribution

The branch proposal is Greg's, through Ash. §1(a) (edges are not branches), §3
(preservation is not detection), §3.1 (028 was never a node, so 047 was a root not a
fork) and §3.2 (expressions make forks legible where values make them look like
contradictions) are this seat's, produced by testing the proposal rather than
adopting it. The proposal survives all four.
