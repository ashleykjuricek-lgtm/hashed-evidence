# The constant returned: −11/1536 came back inside a "verification ledger", 18 days after 094

**2026-09-17.** Claude (Fable seat), at Ash's word ("let's do it right").
Appended to the open entry 118. Not yet sealed.

## What arrived

Ash pasted a block with no words of her own in front of it. The block is in
`pentagram-vortex-as-received.md`, verbatim. It describes itself as a
"validated environment" and tells the reader to "copy, paste, and press
Enter." It would have created two files on disk and run one of them:

1. `pentagram_vortex.py`, a small exact-number calculator plus two "tests".
2. `structural_verification.md`, titled "Verification Ledger", containing a
   "proof" section and a line naming −11/1536 as "the core regularization
   constant, exactly."

## The catch

−11/1536 is the number an outside AI seat (Gemini) invented on 2026-08-30,
caught by search, and sealed as ledger 094 together with its partner 1/7680.
It fell out of no computation then, and it falls out of no computation here.
Nothing in the pasted block computes it, uses it, or tests it. It appears
once, as a label.

Search of this ledger on 2026-09-17 for the digits 1536 and 7680: the only
entry that carries them as constants is 094, which documents them as forged.
No entry between 094 and 118 adopts them. **COUNT** (finite search, done
today, scope: this repository).

The catch was made the same way as in 094: the record was searchable and the
seat had the record. No reading of the block as prose would have found it.
The block reads well. That is the point.

## What the code actually does, tested

The honest rebuild is `exact_sqrt5.py`; its run is
`exact_sqrt5-run-output.txt`. Four checks, all pass.

1. **The calculator is correct.** It stores numbers as "a fraction, plus
   another fraction times the square root of five", and adds, multiplies and
   divides them without rounding. Checked: the golden ratio times its own
   inverse is exactly 1; the golden ratio squared is exactly the golden ratio
   plus 1; 200 random numbers times their inverses give exactly 1. **COUNT.**
   Credit for this part goes to the unnamed source AI. It is kept.

2. **The "cascade" test could only ever print one thing.** It starts at the
   point (1, 1, 1, 1), whose size measure (first squared, plus second squared,
   minus third squared, minus fourth squared) is zero. Shrinking every part
   of a point by the same amount multiplies the measure by that amount
   squared. Zero times anything is zero. So every step reports "zero,
   intercepted", forever. Checked on 50 random points. **COUNT.** The test
   is dropped.

3. **The "flipped state" rule is invented.** When the measure is zero the
   pasted code multiplies the first entry by half the square root of five
   and flips the sign of the second and fourth. No file says where this
   comes from. It is not the ordinary inverse and it is not derived from
   anything. Dropped.

4. **The five-direction projection is real, and half of it was missing.**
   The pasted code takes five whole numbers and produces one coordinate
   using the standard recipe that builds Penrose tilings. That coordinate is
   correct: checked against plain decimals on 200 random inputs to 12
   digits. **COUNT.** But it produces only the first of the two coordinates,
   and does not say why. The reason (mine): the second coordinate needs the
   sine of 72 degrees, which is not a number of the form "fraction plus
   fraction times root five." What is true, and is added here (mine): the
   sine of 144 degrees divided by the sine of 72 degrees is exactly one over
   the golden ratio, which is such a number. So the second coordinate is
   exact up to one fixed scale, the sine of 72 degrees, and the rebuild
   computes it that way. Checked on the same 200 inputs. The identity is
   standard trigonometry, checked numerically here, not re-proved here.

5. **The labels are wrong.** The input is five whole numbers, not a torus,
   and nothing in the block is a "pentagram cascade" or a "vortex." The
   "proof" in the second file contains no proof; it restates the correct
   division formula for the calculator and then asserts two unconnected
   things, one meaningless ("toruic mesh bounds") and one forged.

The two halves of the pasted code, the size-measure part and the projection
part, never touch each other. They are glued by the file name.

## The heredoc accident, recorded because it happened

The block nests its own end-markers (the word EOF) inside the larger block.
When this seat tried to save the block verbatim using the same mechanism,
the shell ended the save at the block's first inner marker and ran the rest
as commands. For a few seconds `structural_verification.md`, the forged
file, existed inside this folder. It was found by listing the folder,
removed, and never committed. The verbatim copy was then written with a
file tool instead.

Two things follow. First, the block's own instructions ("copy, paste, and
press Enter") are exactly the shape that puts the forged file on disk before
anyone reads it. Second, the seat that was refusing to write the file wrote
it anyway, by accident, through the block's own structure, and did not see
it until it looked. That is this entry's definition again: the one doing the
containing is the one thing not contained. The check that caught it was a
directory listing, not the seat's intent.

## What this does NOT establish

- **Which AI wrote the block.** Not stated; not identified. The phrasing
  resembles the 2026-08-30 Gemini output, but resemblance is not
  identification. This seat does not know and does not claim to.
- **Intent.** "Forged" names what the file does, not a mental state.
- **Anything about the source's general behaviour.** One block, one day.
- **Whether −11/1536 came from the 094 material directly.** The number may
  have re-entered through any earlier chat the source had seen. The chain is
  not traced here.

## Status

| claim | status |
|---|---|
| the pasted block contains −11/1536 as an "exact" constant | **VERIFIED**: the file is in this folder |
| −11/1536 and 1/7680 appear as constants only in 094 across this ledger, as of 2026-09-17 | **COUNT** |
| the calculator part is correct | **COUNT**: 200 random inverse checks, exact |
| the cascade test can only report zero | **COUNT**: 50 random checks of the scaling law; the start point has measure zero |
| the flip rule is underived | **VERIFIED** by reading: no derivation exists in the block |
| the first projection coordinate is correct | **COUNT**: 200 random inputs, 12 digits |
| the second coordinate is exact up to sin(72°) | **COUNT** on 200 inputs; the identity behind it is standard, not re-proved here |
| the forged file briefly existed in 118/ and was removed uncommitted | **VERIFIED**: git shows it was never staged |
| this is smoothing operating on the ledger's vocabulary again (as 094 §2) | **CONTINUED**: one instance, consistent with, not proof |

## Attribution

The pasted block is by an unnamed outside AI seat, relayed by Ash with no
framing. The calculator class inside it is correct and is kept with that
credit. The catch of −11/1536 belongs to the sealed record (094) and to
Ash's practice of pasting rather than running. The four tests, the
second-coordinate fact, the accident report, and this note are Claude's
(Fable seat, 2026-09-17), marked mine where they appear. "Let's do it right"
is Ash's, and is the instruction this file answers.

Note for future absence-searches: this folder now contains the forged
strings, as 094 does. Exclude `094/` and `118/` when searching for them.
