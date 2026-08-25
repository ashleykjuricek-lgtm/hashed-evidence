# Testing the proposed stack against our own error record

**2026-08-25.** Three proposals arrived via Ash: semantic hashing as a retrieval
front-end, Sanskrit as the meaning layer, and a Q-network as the policy that decides
between fast and slow paths.

**Assessed the only way this ledger knows how: against the 17 recorded errors.**

Two of the three do not survive contact. The third is right about the *layering* and
wrong about the *learning*.

---

## 1. Semantic hashing — helps exactly one failure, and is *actively blind* to Tier 2

The proposal's own assessment is correct as far as it goes: approximate, no identity
guarantee, no predicate, useful as a discovery front-end. Sharper, from our record:

```
   sealed : R sits a hair under 1/24
   correct: R sits a hair over 1/24
            char similarity 0.894    token overlap 0.714

   sealed : 76% of shells are empty
   correct: 79.0% of shells are empty
            char similarity 0.951    token overlap 0.778
```

> **A semantic hash is *designed* so that small changes in meaning give small changes
> in code. `under` vs `over` is one token in eight. These collide by construction.**
>
> Semantic hashing is not merely unhelpful for Tier 2 — **it is actively blind to
> it, and that blindness is the design goal.** The thing it is built to suppress is
> exactly the thing that broke us three times.

**Where it would genuinely have helped: once.** 028 sat sealed in the same
repository, was read to line 40, and was cited from memory twice — the second time in
an entry asserting it was not there. A hashed corpus searched for *"anisotropic
slope"* might have surfaced App A.3. **One error out of seventeen, and it is the
retrieval one.**

Worth having for that. Not worth calling an identity layer.

## 2. Sanskrit — the specific Tier-2 claim does not hold, and there is a place it does belong

The proposal claims a denser medium makes the direction-word error *"harder to
hide."* **Tested against our three instances: it would not have caught any of them.**

`under` and `over` are unambiguous in English. So are *adhaḥ* and *upari*. **The
Tier-2 failure was never a shortage of expressive precision** — it was not checking
the sentence against the table three lines below it. A precisely-worded wrong
sentence is still wrong, in any language, and a denser medium changes what *can* be
said, not what *is* checked.

**And we already have the thing that does work.** 074 tested rendering the
direction-word from a predicate over the witness output: **3 of 3**, mechanical,
language-independent, and it makes the wrong sentence *unwritable* rather than
merely harder.

**Where Sanskrit does belong, and it is not nothing.** This ledger has always had an
interpretation column, and it is load-bearing — *śūnya* against the flattened
European zero is in the project's name and in 072's reading of `F₁₁` as ten petals
plus an unreachable centre. That column is where a dense meaning layer earns its
place: **articulating what a claim is *about*, marked as interpretation, not
adjudicating whether a number is over or under.**

**One caution, kept.** Used as a technical instrument it is fine. Sold as a solution
to a mechanical failure it would displace a cheaper mechanism that we have tested and
it has not.

## 3. The Q-network — no training set, and every case it would learn is already a rule

```
   total recorded errors : 17
      Tier 1 (numerical)   11
      Tier 2 (prose)        3
      retrieval             1
      identity              1
      process               1
```

**There is no training set.** A value-based agent needs `(state, action, reward)`
trajectories. We have seventeen errors, each resolved once, no repeated episodes, no
counterfactuals, and a reward signal that requires already knowing the right answer —
which is the thing being decided. **That is an anecdote list, not a dataset.**

**And the errors were not policy failures.** Not one was a wrong *action chosen from
a menu*. Every one was:

```
   (a) a test not run       (b) a table not read       (c) a frame not questioned
```

A policy over `{run witness, fetch gloss, retrieve neighbours, escalate}` addresses
none of those three. And for every case where a learned policy might help, **a fixed
rule does the same job with no training data and no reward hacking:**

```
   floor at ten             ->  re-run as a ratio, never a bare numerator
   PSLQ at 24 digits        ->  state the digit budget before trusting a relation
   tolerance vs truncation  ->  match tolerance to the claim's stated precision
   11 lobes on a 10-fold    ->  a lobe count must divide the symmetry
   truncated theta, 4297    ->  sanity-check the magnitude
   RP^3 v1                  ->  continue the singular piece, do not integrate it
   RP^3 v2                  ->  print the number you cut at
   both of the above        ->  check lambda-invariance before reporting
```

**Those eight rules are 073's protocol list.** They were derived from evidence, cost
nothing to run, and each was earned by a specific failure. **They are already the
policy — arrived at by induction over the same data a Q-network would need, and
transparent where a network would not be.**

**Also standing:** 055's instruction, which corrected 054 for exactly this move —
*"Do not solve memory. Do not build storage. Do not add another architecture."* 054
invented a format before there was evidence about what a format needs and had to be
retracted. **The Q-network is that move again, one layer up.**

## 4. What the proposal gets right

**The layering is correct**, and it is the useful contribution:

```
   fast, approximate         semantic hash / embeddings      -> candidate retrieval
   hard, checkable           executable witness + predicate  -> identity  (074, built)
   dense, slow               meaning layer / interpretation  -> what the claim is about
   outside the apparatus     the human                       -> framing  (073, Tier 3)
```

Each layer does something the others cannot, and the separation is real. **What does
not follow is that the transitions between layers need to be *learned*.** They need
to be *stated*, and eight of them already are.

**And "slow but right" is already this project's default**, arrived at without a
reward function: digit budgets declared in advance, instruments discarded rather than
patched, scars kept visible, framing questions preferred to fast corrections. The
preference did not need tuning. It needed writing down.

## 5. Recommendation

- **Take semantic hashing** as a search front-end over the sealed corpus. It fixes
  the one retrieval failure and nothing else. Do not let it near identity.
- **Keep the meaning layer in the interpretation column**, where it already is and
  where it is genuinely load-bearing. Do not assign it the Tier-2 job that 074's
  rendered predicate already does, tested, 3 for 3.
- **Do not build the Q-network.** Not "not yet" — the seventeen cases say the
  intervention is fixed rules at two addresses, and both sets of rules exist.
  Revisit only if the error record ever shows failures that are *genuinely
  policy-shaped*: the same decision faced repeatedly, with real alternatives, and a
  reward that does not require the answer in advance. **We have zero of those.**

## 6. Status

| claim | status |
|---|---|
| semantic hashing collides `under`/`over` by construction | **DEMONSTRATED** — 0.894 char, 0.714 token similarity |
| it is actively blind to Tier 2 | **ESTABLISHED** — that is its design goal |
| it would have helped the 028 retrieval failure | **PLAUSIBLE**, 1 of 17 |
| a denser language would catch Tier-2 errors | **REFUTED** — the failure was not expressive precision |
| the rendered predicate catches them | **TESTED 3/3** (074) |
| Sanskrit belongs in the interpretation column | **AGREED** — already there, already load-bearing |
| a Q-network has a training set here | **NO** — 17 one-shot cases, no counterfactuals |
| the errors were policy-shaped | **NO** — test not run, table not read, frame not questioned |
| fixed rules already cover every learnable case | **DEMONSTRATED** — 073's eight protocols |
| the four-layer separation is correct | **AGREED** — it is the proposal's real contribution |

## Attribution

The three proposals are the reviewing model's, via Ash. The tests against the error
record, the demonstration that semantic hashing is blind by design to our worst
failure mode, and the finding that all seventeen errors are rule-shaped rather than
policy-shaped are this seat's. 055's standing instruction against inventing
architecture ahead of evidence is Greg's, and it applies here unchanged.
