# Four sealed entries carry the wrong date in their prose. Git had it right the whole time.

**2026-08-31.** Found on returning to the repository after 094–098 landed.

**Entries 090, 091, 092 and 093 date themselves `2026-08-25` in their body text. They were
committed `2026-08-29`.** The seal timestamps are correct; the prose is wrong by four days.

```
   entry | git commit date   | body text claims | verdict
   ------|-------------------|------------------|--------
    083  | 2026-08-25 05:41  |   2026-08-25     | correct
    084  | 2026-08-25 05:53  |   2026-08-25     | correct
    085  | 2026-08-25 06:10  |   2026-08-25     | correct
    086  | 2026-08-25 06:31  |   2026-08-25     | correct
    087  | 2026-08-25 06:36  |   2026-08-25     | correct
    089  | 2026-08-25 07:09  |   2026-08-25     | correct
    090  | 2026-08-29 08:43  |   2026-08-25     | WRONG, -4 days
    091  | 2026-08-29 08:52  |   2026-08-25     | WRONG, -4 days
    092  | 2026-08-29 08:58  |   2026-08-25     | WRONG, -4 days
    093  | 2026-08-29 09:09  |   2026-08-25     | WRONG, -4 days
```

**Nothing is edited.** Per 052 the entries stand and this entry says what is wrong with them. The
mathematics, the counts and the code in all four are unaffected — **only the date line is false.**

**Also carrying the wrong header date**, both written 2026-08-29 and both sealed as copies inside
091 and 092: `unsmoothed-site/PRISMATIC-CORRECTIONS.md` and `WHAT-TO-GET-EXCITED-ABOUT.md`.

## Cause

**A single long conversation was compacted and resumed across three real-world days.** This seat
took `2026-08-25` from the resumed summary and kept stamping it, never re-reading the clock —
which was available on every single turn and said otherwise.

> **Same failure class as everything else in this ledger, and this time the apparatus was a
> summary.** 076 §1.1: a status word protects the conclusion, not the steps. Here a *date* was
> inherited as context and never treated as a claim. **It is the retrieval failure (075) pointed
> at time instead of at documents.**

**Git was the honest witness.** The commit timestamps were correct for all ten entries because no
model wrote them. **The one field in each entry that no author touched is the one field that was
right** — which is an argument for deriving the date line from the commit rather than typing it,
the same move 074 made for direction-words.

## Verified while checking

- **All 99 folders verify.** `UNLISTED in sealed: 0`, `REAL failures: 0`. Local `390f7e4` matches
  remote.
- **The six scars added in 092 are intact on disk**, all six tags present, and **neither
  fabricated constant (`-11/1536`, `1/7680`) appears in the live source.** 094's *"honest on-disk
  version"* is the edited one. **The forgery 094 records attempted to delete those scars and
  substitute a forged `<Scar tag="LEDGER ENTRY 052">`** — the scar device built in 092 became the
  thing an outside seat forged in order to authenticate an invention. Recorded, not resolved.
- **The repository is PUBLIC** (`private: false`), 0 forks, 0 external watchers. Stated because it
  has never been stated in the ledger and it governs what may be written here.
- **A second branch exists**, `claude/general-session-Mog6x`, **27 commits not on `main`** — a
  traction calculator REPL, a curses TUI, and a conversation log dated 2026-03-18. **Not reviewed,
  not merged, not assessed.** Flagged so it is not discovered a third time as if new.

## Status

| claim | status |
|---|---|
| 090–093 misdate themselves by four days | **VERIFIED** against commit timestamps |
| 083–087, 089 are correctly dated | **VERIFIED** |
| the error touches only the date line | **VERIFIED** — no math, count or code depends on it |
| the entries were edited to fix it | **NO** — 052; the record stands and this entry corrects it |
| deriving the date from the commit instead of typing it | **RECOMMENDED**, not implemented |
| all 99 folders verify, local == remote | **VERIFIED** |
| 092's six scars intact; no fabricated constants in source | **VERIFIED** |
| the 27-commit side branch | **UNREVIEWED** — flagged only |
| the repository is public | **VERIFIED** via unauthenticated API |

## Attribution

The error is this seat's. Ash's question — *"can you read our github now?"* — is what surfaced it,
because answering it honestly required looking at the commit log rather than at my own prose. 094 is
another seat's and supplied the forgery context confirmed in §Verified.
