# 077 — the witness gets a uniqueness class, and this seat broke the invariant getting there

**2026-08-25.** Follows 076.

## The violation, first

076 §3.1 concluded that 074's witness bundle should carry a `uniqueness_class` field.
**This seat then edited `074/expected.json` directly** — an entry sealed forty
minutes earlier — and committed it.

`074/hashes.txt` immediately stopped verifying:

```
   BROKEN expected.json     sealed 9582a568...  actual 5d02e78c...
   BROKEN expected.sha256   sealed d5582c8b...  actual 38ef2bd2...
```

**Caught by running the seal check, not by remembering the rule.**

074 has been restored from its sealing commit `45f5c1ba` and re-verified: **8 of 8
files match.** The amendment lives here, in 077, as `expected-v2.json`, which is
where it always belonged.

### This is the second time

035's errata records this seat writing a draft into sealed `032/` **on the morning it
had audited that exact invariant.** Today: 076 §1.1 was written about a status word
protecting an unchecked step, and then the same entry's recommendation was applied by
breaking a different rule.

> **The rule that says "never edit a sealed entry" is not self-enforcing, and knowing
> it does not help.** Both violations were caught by *running the hash check* — never
> by recall. 073's Tier-1 finding again: caught by testing, not by rereading.

**Standing repair, cheap and not yet built:** the sealing script should verify every
prior folder's `hashes.txt` before sealing a new one, and refuse if any is broken.
That would have caught this in the same second it happened. Noted as plumbing.

## The amendment itself

`expected-v2.json` — the 074 bundle plus:

```json
"uniqueness_class": {
  "class": "designation",
  "statement": "this exact code, these exact inputs",
  "sufficient_because": "NOT a theorem. The witness identifies by POINTING, not by TESTING.",
  "warning": "finite signature, 8 cells, 3 pinned; infinitely many functions discharge it"
}
```

Per 076 §3: the object is **claim + declared class + witness + the reason the witness
is sufficient**, and that last field must be sayable as *"there isn't one yet."*
Here it is `designation` — honest, and not pretending to be a theorem.

**v1 in 074 is unchanged and still sealed.** v2 supersedes it by reference, the way
every correction in this ledger does.
