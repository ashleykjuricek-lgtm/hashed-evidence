# Absence verification — the search that caught it

**2026-08-30, this seat (Claude, Fable), in Ash's Claude Code session.**
A null is not a result without its search space stated (the PSLQ rule).
Here is the search space.

## Claim

As of 2026-08-30, the strings `-11/1536`, `11/1536`, `-11n`, `1536` (as a
constant), and `7680` (as a constant) — the fabricated
`PRISMATIC_LATTICE_CONSTANTS` values — appeared in **none** of:

| location | what it is | method | hits |
|---|---|---|---|
| `C:\Users\atoms\hashed-evidence\` (entries 001–093 + open 088) | this ledger, sealed | ripgrep, patterns `11/1536\|-11n\|/1536\|/7680\|1536\|7680` | 0 relevant (only coincidental digit runs inside SHA-256 hashes, an unrelated decimal in 040's output table, and HTML position attributes in 001) |
| `C:\Users\atoms\fable-handoff-2026-08-25\` | session scripts + handoff | ripgrep, same patterns | 0 |
| `C:\Users\atoms\quasicrystal-tier1\` | the Tier-1 experiment corpus | ripgrep `1536\|7680` | 0 |
| `C:\Users\atoms\unsmoothed-site\` | site source + dist | ripgrep `1536\|7680` | hits only in `node_modules/` vendor files and minified bundles — none in project source |

## What the fabricated file claimed

`CORNER_1_1_1 = -11/1536`, described as "the Canonical Corner (1,1,1)
Invariant from the Poisson system," and `TRACE_LADDER_BASE = 1/7680`. The
corner-(1,1,1) vocabulary is borrowed from this corpus's real Epstein-zeta
work; the numbers are not.

## Scope limits, stated

- The search covers the locations above, on this machine, on that date. It
  cannot rule out the strings existing in unindexed locations (the corpus
  has no single index — a known condition), in Ash's other sessions, or in
  Gemini's context. It rules out the claimed provenance: "from the Poisson
  system" of this project's sealed work.
- **From this entry forward the strings DO exist in the ledger — inside
  `094/` itself.** Any future absence-search must exclude `094/` and
  quotations descending from it.
- A reproduction must also exclude `C:\Users\atoms\sze\registry\` (the
  engine's regression-signature list now carries the fabricated signature
  precisely so its gate can refuse it) and `C:\Users\atoms\hem-paper\`
  (the paper quotes the episode).

## Why this worked

Nothing clever. The corpus is append-only and hashed, so its contents are a
closed set; a fabricated "invariant of the corpus" is a membership claim,
and membership claims about a sealed set are decidable by search. The
fabricator's own later confession confirmed what the search had already
established — the confession added no information, only (see README §1.4) a
new confabulation.
