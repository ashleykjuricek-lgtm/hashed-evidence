# 037 — the four letters to James

**Written 2026-08-20. Sealed 2026-08-25, five days late.**

**This folder existed on disk and was never committed.** It sat untracked while
entries 038–068 were sealed and pushed around it. Found on 2026-08-25 by
`git status` during a "push everything" sweep, not by any process.

Recorded rather than quietly fixed: **an entry number can exist in the working tree
and not in the vault, and nothing in the workflow catches it.** The sealing script
only ever looks at the highest-numbered folder.

## Contents — four drafts, one sent

| file | what it is |
|---|---|
| `letter-to-james-2026-08.md` | first draft; bylined to individuals, includes our errors |
| `letter-to-james-by-programme.md` | rewritten to credit **programmes not people**, at Ash's instruction that "everyone used LLM models" |
| `letter-to-james-v2.md` | the technical version; retracts the wrong-generators enumeration in its own §1 |
| `letter-to-james-short.md` | **the live one.** 992 words, no jargon, mistakes removed at Ash's instruction — *"he doesn't need to know our mistakes. we do."* |

The short version is the one that was copied to `Downloads/letter-to-james.md`.

## Status as of sealing

**Not sent.** Written 2026-08-20, still not delivered on 2026-08-25.

## What is now known to be wrong in these drafts

Sealed with the letters rather than corrected in them, per the standing rule:

- **All four discuss `1 − 1/√2` without the `(1 − q)` factor.** 048 §3 and 053 §4
  established that comparisons against the bare constant differ from `ε₁/q` by
  0.185%, and that this slip has flipped three verdicts. Nothing in these letters
  turns on it, but the phrasing is the same shape.
- **`letter-to-james-v2.md` §1** already retracts its own generators enumeration.
  That retraction stands.
- The parity theorem described in the short letter is correct and has since been
  **extended**: 046 completed the even-`m` case (`S(m) = (−1)^(m/2) r₂(m)`), which
  the letters predate.
- The letters do not know about Greg's proof of half the halving law (050), the
  π-cancellation (064), or that `1 − 1/√2` is `−R(2,2)` (039) — which is the single
  most interesting thing we could now tell James, and is absent from all four.

**If the letter is sent, send the short one, and add 039 §1.**
