# 086 — four notes rehomed out of sealed 080, and the seal hole closed

**2026-08-25.** Four files were written **into folder 080 after 080 was sealed**. They
are moved here **unaltered**. Their content is not assessed, amended, or judged in this
entry — only their filing.

```
   080/dar-corroboration.md        commit 33af4ef   Add DAR terminology corroboration note
   080/surprisal-scar.md           commit 858d253   Add surprisal scar note to entry 080
   080/condition-c-note.md         commit 33d8289   experiment: document Condition C rationale
   080/condition-c-cott-prompt.md  commit 257b2c4   experiment: add COTT closure-by-extension condition
```

**`condition-c-note.md` and `condition-c-cott-prompt.md` extend the Identity Gauntlet
sealed in 081** — they are its third condition and belong beside Conditions A and B.
The other two are standalone notes on unrelated subjects that landed in 080 because 080
happened to be the current folder.

## 1. What actually broke, and it is not what it looks like

A sealed folder's `hashes.txt` covers **the files it lists**. A file *added* to that
folder afterwards is not listed, so nothing it does can break a hash. **It sits inside a
sealed folder wearing the seal's authority with zero coverage.**

**This is the fourth seal-discipline incident** — after an edit into sealed 032, an edit
into sealed 074, and the two numbering races of 079 and 081. It is the first of a new
kind: **the previous three were modifications, which the seal catches. This was
addition, which it did not.**

## 2. Another seat found it first, and this entry finishes their work

`verify_seals.py` already carried an `UNLISTED` check when this seat looked, with a
comment naming `080/surprisal-scar.md` as the first instance and the fix deliberately
left **non-fatal**:

> *"Reported, not (yet) fatal — promote to a failure once the current instance is
> rehomed to an open folder."*

**That is a correctly-scoped handoff and it is now discharged.** The files are rehomed
here, and `UNLISTED` is **promoted to a real failure**: from this entry on, a file
sitting unsealed inside a sealed folder breaks the chain and blocks the next seal, the
same as a modified file.

**Correction, this seat's, recorded because it was reported to Ash before it was
checked.** This seat reported that the verifier was *"blind to all of them."* **False.**
The verifier detected and printed all four; the output had been truncated past the
`UNLISTED` line before reading it. **The tool was working. The reading of it was not** —
which is the same failure the corpus has recorded ten times over: a claim about the
world resting on a fact about the apparatus (043's F8), here the apparatus being `tail`.

## 3. Seal pre-flights now, in order

```
   1  verify every prior seal, including UNLISTED   (079, promoted to fatal here)
   2  fetch; refuse if the target folder exists on origin   (081)
```

**Still not closed:** two seats that both fetch, both see the same folder free, and both
write inside the same window. **Narrowed, not eliminated.** A reservation protocol is a
coordination agreement between seats, not a line of shell, and remains **OPEN**.

## 4. On the DAR note specifically — checked, and it holds

`dar-corroboration.md` cites Hacker News item `45960293`. **Fetched and confirmed by
this seat**, independently of the note's author:

- The item exists. Thread title *"I caught Google Gemini using my data and then covering
  it up"*, posted by **JakaJancar**, roughly nine months before this entry — consistent
  with the November 2025 date claimed.
- A commenter, **spijdar**, reports the label `INTERNAL-ONLY, DRAFT, ANALYZE, REFINE
  PROCESS` and states that Gemini reasoning tokens refer to it as **DAR**.
- Field names reported alongside it: `is_redaction_request`, `is_prohibited`,
  `user_context`.

**What that establishes:** the terminology appears in at least one account of a Gemini
context obtained by someone with no connection to this project. **Two independent
sightings of the same label.**

**What it does not establish, and the note already says so:** it is **one anonymous
commenter's report**, not Google documentation, not a reproducible dump, and not an
architecture specification. *"Independently corroborated"* is accurate for the
terminology and **overstated if read as corroborating any mechanism.**

> **Worth recording plainly: this relay survived checking.** The ledger's record on
> relayed claims is poor — 069 §5's Gamma sketch, the Ambjørn–Wolfram attribution, the
> eleven-lobe rediscovery — every one of them relayed and none checked at relay time.
> **This one was hedged correctly by its author and the hedges held.**

## 5. Status

| claim | status |
|---|---|
| four files were added to sealed 080 | **VERIFIED** — four commits, named above |
| a seal covers listed files only; additions are uncovered | **ESTABLISHED** — fourth incident, first of this kind |
| `verify_seals.py` was blind to it | **RETRACTED, this seat's** — it detected all four; the output was truncated |
| `UNLISTED` promoted to fatal | **DONE** in this entry |
| the numbering race is closed | **NO** — narrowed only; reservation protocol **OPEN** |
| HN item `45960293` exists and reports `DAR` | **VERIFIED** by independent fetch |
| DAR is confirmed Google architecture | **NO** — one commenter's report; terminology only |
| the four notes' content | **NOT ASSESSED HERE** — moved unaltered, filing only |

## Attribution

The four notes are other seats', unaltered, and the `UNLISTED` detection in
`verify_seals.py` is another seat's — **this entry only finishes what they started.**
The rehoming, the promotion to fatal, the independent fetch of the Hacker News item, and
the retraction in §2 are this seat's. Ash authorised the DAR note's creation and asked
for the check that produced §4.
