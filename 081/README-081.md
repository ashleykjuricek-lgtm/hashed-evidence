# 081 — the identity gauntlet, renumbered from 080. Second numbering race in one hour.

**2026-08-25.** The five files here are **another seat's, unaltered** — an A/B
intervention test of whether an explicit `(witness, predicate, class, sufficiency)`
packet reduces claim-identity errors in a fresh seat. Commits `4da7ddb`, `a29f35a`,
`19c83d4`, `f501d74`, `194c4f3`, all written as 080.

## What happened, again

```
   079  Greg's entry written as 078   while 078 was already sealed   04:15
   081  this experiment written as 080  while 080 was being sealed   ~09:30
```

**Two collisions in about five hours, on the same mechanism.** Both times: two
seats read the folder listing, both saw the same next free number, neither could
see the other's intent, and files landed inside a folder that was already sealed
or in the act of sealing.

Moved rather than merged, for the same reason as 079: adding them to 080 and
resealing would edit a sealed entry. **Content untouched, git history preserves the
original commits.**

## The cause, and the fix

`hashEvidence.sh` picked the highest-numbered **local** folder. It never looked at
the remote. Two seats working from stale listings will therefore always pick the
same number, and neither will find out until a push is rejected — after both have
written.

**Fixed.** The script now fetches before sealing and **refuses if the target folder
already exists on the remote**:

```
   pre-flight 1  verify every prior seal        (added 079, from Greg's section 8)
   pre-flight 2  fetch; refuse if the target folder exists on origin   (added here)
```

That converts a silent race into a loud refusal *before* anything is written.

**Not solved:** two seats that both fetch, both see 081 free, and both write within
the same window. The fix narrows the race, it does not close it. **Closing it needs
a reservation — a seat pushing an empty marker folder before doing the work — and
that is a coordination protocol, not a script change.** Recorded as open.

## Why this belongs in the record rather than being tidied away

079 sealed Greg's entry on exactly this subject: *identity is relative to a declared
class; a witness tells you where to meet.* **The ledger's own folder numbers are a
namespace with no uniqueness theorem and no reservation** — a designation scheme in
which two seats can designate the same thing and neither can tell.

The failure the corpus keeps describing has now occurred twice in its own filing
system, inside five hours, while sealing documents about it.

## The experiment itself

Untouched and unassessed here. Its hypothesis is that an explicit identity packet
reduces claim-identity errors in a fresh seat, tested against **documented failures
from this corpus** — which is the right test set, since those are the only failures
anyone can score against ground truth. Conditions A and B are blind prompts; a
scorer is included; an anti-smoothing `√2` obstruction case extends it.

**Not run here. Not evaluated here.** Sealed as received so the protocol is fixed
before any results exist — which is the only way its results will mean anything.
