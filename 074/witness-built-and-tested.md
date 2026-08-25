# The canonical executable witness — built, and it found two of its own limits

**2026-08-25.** The proposal was listed as unbuilt. It is now built, run against
three real historical artefacts and the three recorded Tier-2 errors, and packaged.

**Result: it works, and building it exposed exactly the two weaknesses the
reviewing seat's refinement then named independently.**

---

## 1. Built, and the historical dispute discharges

`witness_slope.py` — a pure function with every convention as an explicit argument:

```
  WITNESS ID   slope-of-eps-anisotropic/v1
  INPUTS       family in {1bb, volpres} | chart in {direct, momentum} | marked in {short, stretched}
  OUTPUT       d eps / db at b = 1
  TOLERANCE    RELATIVE 1e-9
```

Three artefacts that spent a day being called wrong by each other:

```
  028 App A.3 (June)      "d eps/db ~ +18.3"        1bb|direct|short          DISCHARGES
  047 sec.B (Aug 23)      "-18.3259647484177"       1bb|momentum|short        DISCHARGES
  KESTREL (Aug 23)        "the true slope ~ -27.49" volpres|momentum|stretched DISCHARGES
```

**One claim, three input points.** The disagreement was never about the world; it was
about arguments. And the refuted charge collapses to one line:

> KESTREL called 028's number *"a fitted guess."* **A fitted guess cannot discharge a
> witness. 028's does.** Running it settles a claim about *provenance* — which no
> metadata layer can decide.

## 2. Two bugs found by building it, and both are the refinement's two sharpenings

**Bug 1 — the input labels are ambiguous, and the ambiguity is exactly the kind the
witness was meant to remove.** `marked="stretched"` is a *semantic* label whose axis
index is **family-dependent**: in `(1,b,b)` the stretched axes are 1 and 2; in
`(b, 1/√b, 1/√b)` it is axis 0. v1 hard-coded one mapping and silently returned the
**other cell** — `−13.744` instead of `+27.489`, a real value from a real
configuration, with no error raised.

> **The witness moves the ambiguity from the value to the input signature. It does
> not eliminate it.**

That is the refinement's *"two seats can still invent different input signatures and
never collide,"* found empirically before it was named.

**Bug 2 — absolute tolerance is wrong.** v1 used absolute `1e-9`. KESTREL's
`27.4889471200` is a twelve-figure truncation of `27.4889471226…`, so on a value of
size ~27 it **failed a test it should pass.** A witness must declare **relative**
tolerance, or match the digits the claim actually states.

That is the refinement's *"explicit digit budget… precision,"* likewise found by
running into it.

## 3. The predicate makes the Tier-2 error unwritable — tested 3 for 3

The refinement's central move: **the unit is the pair `(witness, predicate)`.** The
direction-word stops being prose and becomes the *rendering* of a predicate over the
witness output.

Tested against this ledger's three recorded Tier-2 errors — the three emphasised
sentences contradicted by a table on their own page:

```
  066   "R sits a hair ___ 1/24"
        witness  eps = +0.0005459504653706
        predicate renders:  over          sealed:  under          CONTRADICTS

  067   "___ of shells below the cutoff are empty"
        witness  empty 1,579,039 / 2,000,000
        predicate renders:  79.0%         sealed:  76%            CONTRADICTS

  070   "the two divisions are ___"
        witness  both 99, neither 109, total 430
        predicate renders:  independent -- they agree on 208/430
                            sealed: complementary, each blind where the other sees
                                                                  CONTRADICTS
```

> **3 of 3.** All three survived repeated rereads by their author and were caught
> only by another seat. **A rendered predicate catches all three mechanically**,
> because the word is no longer typed.

**This is the Tier-2 defence made mechanical**, and it is the strongest result in
this entry.

## 4. Packaged — and it is plumbing, as claimed

`expected.json` + `expected.sha256`. The bundle carries: the route, the input
signature, the **conventions** (including a note on the family-dependent label that
caused bug 1), the **precision block** (including why absolute tolerance fails), the
pinned outputs per input point, the three discharging artefacts, the environment
versions, and the four-word status.

```
   sha256  63da8bbdcad0e8c95f052e75f29a2c4dca0969660f3e2be7e2c63b14bdcd703f
   discharged  3 of 3
```

**Confirmed: packaging is plumbing.** The research-shaped work was deciding that
`chart` and `marked` belong in the input signature at all — which took a day, three
seats and two retractions to learn.

## 5. What it does not do, kept

- **It is a rendezvous, not an oracle.** It does not decide that two independently
  written computations are the same fact. Two seats can still pick different
  signatures and never meet — bug 1 is that failure in miniature. What it changes is
  **permanence**: once a dispute is resolved, the resolution is stored, and future
  seats rendezvous at the bundle instead of re-fighting it.
- **Identity, not truth.** Matching a witness means *"these point at the same
  fact."* Whether the fact holds lives in the four-word column.
- **Nothing for Tier 3.** There is no witness for *"is `R` the right object?"* or
  *"is the integer requirement ours or the world's?"* Every framing move in this
  project came from the human, and no witness would have produced one.
- **The `iff` is dropped.** The two-way lock does not hold in either direction.

## 6. The sealable statement

> **The witness layer converts claim identity from an undecidable question into a
> coordination discipline. Its unit is the pair (witness, predicate), not the
> witness alone. It is a rendezvous for resolved disputes, not an oracle that
> dissolves them.**

## 7. Status

| claim | status |
|---|---|
| the witness discharges all three historical artefacts | **BUILT AND VERIFIED**, 3/3 |
| "a fitted guess cannot discharge a witness" | **DEMONSTRATED** |
| input-signature ambiguity survives into the witness | **PROVED by bug 1** — returned a real value from the wrong cell, silently |
| absolute tolerance is wrong; relative is required | **PROVED by bug 2** |
| a rendered predicate kills Tier-2 errors | **TESTED 3 of 3** on the recorded set |
| packaging is plumbing, not research | **CONFIRMED** — bundle built and hashed |
| the witness decides identity automatically | **NO** — rendezvous, not oracle |
| the witness carries truth | **NO** — identity only |
| anything for Tier 3 | **NO** |

## Attribution

The proposal and its refinement — the `(witness, predicate)` pair, the
rendezvous-not-oracle framing, the precision discipline, and dropping the `iff` —
are the reviewing seat's, delivered through Ash, with the original idea credited in
069. Building it, the two bugs, the Tier-2 test and the bundle are this seat's. The
two bugs were found before the refinement naming them arrived, which is the only
independent evidence in this entry that the refinement is the right one.
