# The ATMS boundary, tested against our own three failures

**2026-08-24.** Follows 057. Greg's identification, via Ash:

> Branching is largely solved — **ATMS**, de Kleer 1986: multiple conflicting
> contexts alive at once, a claim's label a set of **minimal environments**,
> contradictions recorded as **nogoods** rather than forcing erasure. Storage is
> largely solved — git's DAG, Dolt, TerminusDB. Provenance representation is
> largely solved — W3C PROV.
>
> What is not solved: **claim identification + equivalence + retrieval.** Is *"the
> 18.3 slope"* the same claim as an old equation written with reciprocal `b`? Is a
> sentence saying *"new result"* equivalent to something buried in a table six
> months ago? That is the semantic invisibility problem.

The references are accurate and the characterisation is right. This entry does not
argue with it. It tests it, on the only three failures we have documented in
enough detail to test with.

**Result: all three of our failures are in the unsolved bucket. None is a
truth-maintenance failure.**

---

## 1. Claim A in ATMS terms — one label, three nodes

The slope. Written as an ATMS would have it:

```
node   "d eps/db near the cube"
  justification 1   env {direct lattice, spacings (1,b,b)}          -> +18.3259647484
  justification 2   env {momentum modes, sides (1,b,b)}             -> -18.3259647484
  justification 3   env {volume-preserving, marked axis stretched}  -> +27.4889471200
```

**No nogood should fire.** These are not contradictory beliefs. They are one
quantity in three charts, and 048 §4 later showed the values sit in the exact ratios
`{1, −1/2, −3/2, +3/4}`. A truth-maintenance system asked to reconcile them would
have had nothing to do, correctly.

**What went wrong is upstream of any of that.** The parameterisation was never an
assumption in an environment. It was a `b²` inside a formula in Appendix A.3, three
lines under a prose label it contradicts. All three results were filed under one
label, `slope`, as if they shared an environment.

> **A is a node-identity failure: one label carrying three nodes.** ATMS presupposes
> that the assumption sets are already known and distinct. Ours was implicit in an
> appendix.

## 2. Claim B in ATMS terms — one label, two nodes

The `(1 − q)`. Two distinct objects wore the same name:

```
node X   "1 - 1/sqrt2"                 the bare constant     = 0.292893218813452476
node Y   "eps1/q" from eps1 = q(1-1/sqrt2)(1-q)              = 0.292346257500812736
```

Three authors — 028's §7.1 prose, this seat, and the Figma seat — computed a value
correctly and then compared it against **node X when the correct target was node
Y**. They differ by 0.185%, which is enough to flip a verdict, and it flipped
three.

**Here an ATMS would have helped**, but only under a condition: node Y exists as a
node **only if the expression is represented**, not the value. `ε₁ = q(1−1/√2)(1−q)`
generates a different node from the constant `1 − 1/√2`. Store the value and the
two collapse into one; store the expression and they cannot.

That is 055 §3.3's first requirement, arrived at independently and by a different
route, and the two compose exactly.

> **B is a node-identity failure: one label carrying two nodes**, and it is the
> mirror of A. A had one name for three things; B had one name for two.

## 3. The 057 failure — the node was there and nobody visited it

`028/false-positive-cubic-torus.md`: sealed, hashed, 194 lines, in the same
repository, containing both the decisive appendix and Claim B's ancestor sentence.
Read to line 40 during the F8 sweep, then cited from memory twice — the second time
in a sealed entry asserting it was not in the vault at all.

Not a branching failure. Not a storage failure. Not a provenance-representation
failure. **A retrieval failure, on a document already in hand.**

## 4. The tally

| our failure | branching | storage | provenance | **identification / equivalence / retrieval** |
|---|---|---|---|---|
| A · the slope, three charts | ok | ok | ok | **failed** — implicit assumption, never lifted |
| B · the dropped `(1 − q)` | ok | ok | ok | **failed** — one name, two objects |
| 057 · 028 unread past line 40 | ok | ok | ok | **failed** — node present, never visited |

**Three for three.** Every failure this programme has documented in reconstructable
detail sits in the one bucket Greg identifies as open. Not one of them would have
been prevented by better branching, better storage, or a provenance vocabulary — and
we have now checked rather than assumed that.

That is three data points, not a theorem. But they were not selected for this; they
are simply the only three we reconstructed, in 055, 056 and 057, before this
framing existed.

## 5. What follows, and what does not

**Does not follow: build anything.** 054 invented a format before there was
evidence; 055 corrected it; the instruction stands. Nothing here needs an ATMS
implementation, a graph database, or a provenance vocabulary, because none of those
would have caught any of the three.

**Does follow, and it is one sentence:**

> The expensive part of this collaboration is deciding **when two things are the
> same claim**, and no amount of correct machinery downstream helps if that
> decision is wrong or never made.

**One thing to note about the name.** "Truth Maintenance System" promises something
it does not deliver, and Doyle's own 1979 framing is the accurate one: it records
the *reasons* for beliefs so beliefs can be revised when later discoveries
contradict their assumptions. It maintains **dependency structure**, not truth. The
same caution this ledger applies to itself — 054 §0, that the derived view must
never become the authority — is the caution the field already built into the
original description and the name then obscured.

## 6. The next experiment, in Greg's own method

Not architecture. A measurement on the corpus we already have:

> **How many distinct labels in the vault refer to the same node, and how many
> identical labels refer to different nodes?**

Both directions occurred here. `slope` was one label over three nodes; `1 − 1/√2`
was one label over two. And in the other direction, 028 §6's *"Z2_AA/Z2_PP"* and
039 §1's *"R(2,2)"* are the same node under two names, which is why 039 restated a
result that was already sealed (053 §3).

That is countable across 58 entries, it does not require building anything, and it
would say whether these three are the shape of the corpus or three anecdotes.

## Attribution

The ATMS identification, the boundary, and the observation that the hard remainder
is claim identification are Greg's, via Ash. The test in §§1–4 is this seat's, using
the three failures reconstructed in 055, 056 and 057. §2's condition — that node Y
exists only if the expression is stored rather than the value — connects Greg's
boundary to 055 §3.3, which was derived before either of us had the ATMS frame.
