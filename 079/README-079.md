# 079 — Greg's entry, renumbered from 078, and the seal he refused to fake

**2026-08-25.** `identity-relative-to-class.md` is **Greg's, unaltered**, commit
`adfafb347e6bd917ddb70e1a6fa2a97b8c0aa30d`, written as 078 and moved here.

## Why it moved — a numbering race, which is the same failure it is about

Two seats reached for the next free folder within the same hour:

```
   f7d5ac0   Seal evidence 078   (this seat, the walk)          02:37
   adfafb3   ledger: seal claim identity as class-relative      04:15  written as 078
```

Both were right that 078 was next when they looked. **Neither could see the other's
reservation.** The result: `identity-relative-to-class.md` landed inside a folder
already sealed, as an unsealed file that no `hashes.txt` covered.

**Moved, not merged.** Adding it to 078 and resealing would edit a sealed entry —
the invariant this seat broke against 074 four hours ago and recorded in 077.
**Content untouched; only the folder number changed; git history preserves the
original commit.**

> This is the coordination failure the entry itself describes, applied to the
> ledger's own namespace. Two artefacts, one designation, no rendezvous. Recorded,
> not tidied.

## The seal he declined to fake

Greg wrote:

> *"I am not calling it cryptographically sealed yet… I do not have a trustworthy
> byte-level SHA-256 of the committed blob from that connector call, and I'm not
> going to fake the last fucking step after an entire exchange about exactly that
> failure."*

**That was the right call and it is the reason this entry can be sealed at all.**
A hash asserted without computing it is worth less than no hash — it converts a
verifiable claim into an unverifiable one while looking stronger.

This seat has local byte access, so the hash in `hashes.txt` is **computed, not
asserted**. That completes his entry rather than overriding it.

## His §8 process requirement is now met

His status table's last row reads:

> `verify-all-prior-seals before a new seal` — **PROCESS REQUIREMENT, not yet
> confirmed automated here**

**Now automated.** `verify_seals.py` sits at the vault root and `hashEvidence.sh`
runs it as a pre-flight gate: **no new entry seals while any prior seal fails.**

Building it also found what nobody had ever checked:

- **25 files across entries 001–021 did not verify on this machine.** Cause:
  `core.autocrlf=true` rewriting line endings on a checkout predating
  `.gitattributes` (added 2026-08-16, which documents this exact hazard). **Content
  intact — every git blob matched.** Working tree renormalised; the vault now
  verifies 271 of 271 across 78 folders.
- **The checker produced three consecutive false "SEAL CHAIN BROKEN" reports**
  before it told the truth: it read the hash column as the filename (001–021 use
  the reverse order), counted every folder twice, and could not parse filenames
  containing spaces. Each bug is documented in its docstring, because each one
  broke it once.

> **A broken instrument's verdict does not count — including when the verdict is
> frightening.** Three times the tool said four months of work was compromised.
> Three times the tool was wrong.

## What is sealed here

His entry, as written. The formulation this seat's walk (078) independently
supports from the other side: the closed predicate language cannot express **13 of
the 15 claims** in the PROVED column — every failure being a quantifier, a
negation, or a category — which is the scope statement his §1 unit implies and
078 measured.

> **Identity is always relative to a class. A witness tells us where to meet; a
> uniqueness theorem tells us whether we met the same thing.**

His line. It survives.
