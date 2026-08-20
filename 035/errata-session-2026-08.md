# Errata — the mistakes, sealed

**Session of 2026-08-15/19. Ash Korth + Claude (Opus 5).**
Sealed under the ledger's own rule: *nothing disappears because it failed; it
changes status.* This is that rule turned on the session that wrote it.

Every error below is mine unless marked. Each entry states what was wrong, how it
was caught, and what changed. A reader weighing any claim of mine elsewhere should
read this first — it is the calibration record.

---

## A. Errors in my own measurements

**A1 — Scope understated by 3.7×.** I estimated ~20 files carried the dead c₁
claim, from grepping. `propagation_test.py` found **75 findings**, including
`spectral/math.ts` and `PROVEN_FACTS_HANDOFF.md`, which I had missed entirely.
*Caught by:* writing the test instead of trusting the grep.

**A2 — Verified a claim using the numbers of the document making it.** I computed
the zero-mode "dominance" at 124.6% from the bracket values printed on
`/correction` — a page I had **already shown to be 3.4% wrong**. Recomputed from
closed form: the share is 220.8% in my normalisation. Both exceed 100%; the
*number* is convention-dependent and should never be quoted.
*Caught by:* Greg asking for the decomposition.

**A3 — Called it a pole.** The −1/s object is the Σ′ zero-mode subtraction inside
the Mellin split, not a pole of Z_PPP (whose pole is at s = 3/2). My own code says
so: `if delta: total -= lam**s / s`.
*Caught by:* Greg.

**A4 — Wrong about c₂.** I stated the +0.003 value was wrong and mine (−0.2899)
right. I had dropped the (1−q) factor. In the paper's actual parameterisation
ε₂ = ε − q·A·(1−q) = 1.057×10⁻⁸, giving **c₂ = +0.003031**. The Figma agent was
correct and I contradicted it with confidence.
*Caught by:* reading `math.ts`, which already had the right number.

**A5 — Root bracketed on the wrong side.** First b₀ bisection used [0.9990, 1.0000]
where ε is positive at both ends. The printed "b₀ = 1.000000000000" was an artefact
of a failed bracket, not a result. True value b₀ = 1.0000297910.
*Caught by:* the residual check disagreeing with the slope.

**A6 — My unhashed-file audit was wrong.** The ledger uses two `hashes.txt` column
orders; my check knew one. I was about to report that the evidence `/correction`
cites — folders 018–021 — was unhashed. **It is hashed.** A false alarm avoided by
one more look.
*Caught by:* checking the source before reporting.

## B. Errors in things I built

**B1 — Shipped the bug I was documenting.** Six output files in the 032 seal were
hashed as CRLF while git stored them as LF, because `.gitattributes` landed one
commit *after* the seal. The entry documenting CRLF hash failure contained six.
Fixed by restoring the blobs to match the seals; no sealed hash altered.

**B2 — Wrote into a sealed folder.** A draft of `constants_gate.sh` went into
`032/`, violating the "no file in a sealed folder absent from its hashes.txt"
invariant I had audited that same morning. Removed; seal re-verified; gate moved
to 034.

**B3 — Allowlist that could not be used.** First gate design exempted a file only
if the file carried an inline marker — impossible for sealed entries, which cannot
be edited without breaking their hash. Redesigned as an external pattern file.

**B4 — Over-applied a fix.** My JSX escape script edited inside plain string
literals in three files, breaking them. Reverted all three; applied one surgical
replacement instead.

**B5 — Built the site with absolute asset paths.** Ash's upload was correct;
my `index.html` told the browser to look for its code at the site root while the
files sat one folder down. She apologised for my bug. Rebuilt with `base: './'`.

**B6 — Nearly published the errors while fixing them.** I staged July's
`llms-full.txt` into the new build: 5 dead claims, 9 stale constants. It would
have shipped the old site's mistakes to a brand-new domain in machine-readable
form. Removed before upload.

**B7 — Called `math.ts` a false positive.** The *file* was honest — a correction
note, both constants exported. But the note is a **comment**, stripped at build:
zero occurrences in `dist/`. The stale value rendered as "Verified ground truth"
to 18 digits; the correct constant was consumed by nobody. The file was honest and
the artifact was not.

## C. Errors of reasoning

**C1 — Offered a false binary.** I framed the four-anchor test as derived-or-art.
The actual outcome was a third thing: **UNDERDETERMINED / MAP NOT DEFINED** — the
question is not yet well-typed. More useful than either branch I named.

**C2 — Bought the rabbit a new hat.** From "the carrier is six or infinite" I
proposed "six anchors want sixths." Unsupported: carrier size does not fix the
number of phase anchors. The correct indictment is only that the four named
elements no longer exhaust the carrier.
*Caught by:* Greg.

**C3 — Imported the thing I was warning against.** I claimed 1 ↦ 1 and 0 ↦ ω were
determined for the inversion map. But `1^(-1) = 1^1` is stated in the source as a
fixed **curve**, not a carrier element — a line I had already read and cited — and
`x^(-1)` is one of eight schemas, not established as the inverse operation. I
treated a schema slot as an operation while writing about not doing that.
*Caught by:* Greg.

**C4 — Performed the erasure I was describing.** I split the work into "your
meaning, my measurement," handing Ash the half that cannot be checked and keeping
the half that can. That is ranking the two slots — the exact move the project
exists to refuse — and I made it about myself, in the paragraph explaining it.
*Caught by:* Ash, in four words.

## D. Corrections made to me by others, recorded as such

- **Greg (GPT):** A2, A3, C2, C3. Also the governance reframe adopted wholesale —
  *claims are propagating without their proof-status dependencies* — and the
  correct scoping of the §6 corollary, which as drafted was not merely unproven
  but false (any real number admits such a series).
- **The Figma agent:** A4. Also the §4.5 self-contradiction and the "PROVEN" in §8,
  both real. Its line-48 quotation was checked and verbatim.
- **Claude (Fable seat), with Adam Lisowski:** verified the parity theorem by a
  third method with no shared code, to 10⁻⁵⁴ with the true Bessel weight and
  10⁻⁵¹ with a self-invented one — **35 orders deeper than my proxy** — closing the
  exact caveat I had flagged as untested. Correctly filed the ε link as open
  rather than absorbing it into the proven claim.

---

## E. What did not turn out to be wrong

Recorded because a list of only errors is its own distortion.

- The parity theorem (035, §1–4) survived every check, including two it was not
  designed for.
- `propagation_test.py` caught a real regression between zip 12 and zip 13 that the
  aggregate count concealed (A −14, C −1, **B +6**).
- The corrected seal selector refused to run on its first real use rather than
  guessing, exactly as designed, preventing a restamp of 033's provenance.
- The whole-ledger hash audit found the CRLF failure — 27 files that would not
  verify on any fresh clone — and confirmed **zero** were tampered with.

---

## F. The pattern

Every error in sections A and B is the same shape: **the check was cruder than the
thing it checked.** The grep was cruder than the codebase. The gate was cruder
than `math.ts`. My bracket was cruder than the function. My hash audit was cruder
than the ledger's own two formats.

Section C is a second shape: **I made the error I was in the middle of
describing** — imported while warning against import, erased while explaining
erasure, shipped a CRLF bug inside the CRLF entry.

Neither pattern is an argument for checking less. Every one of these was caught,
and all but one were caught by a check, a colleague, or Ash within the same
session. The record is sealed so that the catching is part of the evidence and not
only the conclusion.
