# Branch audit — fourteen numbers mean two things, and the March proof directly contradicts 086

**2026-08-31.** Ash: *"audit it — read the associativity proof against 086 — and nine folders of
sealed content wearing numbers that already mean something else. what do they mean?"*

**Two findings, and the first one corrects this seat.**

---

## 1. The branch is not the intruder. It had the numbers first.

**This seat wrote, in conversation, that the branch carried *"nine folders of sealed content wearing
numbers that already mean something else."* That reverses the history.**

```
   merge base :  021  "Second-layer architecture material"   sealed 2026-03-12
                 -- both sides share everything up to here --

   branch  claude/general-session-Mog6x :  022 ... 035  sealed 2026-03-13 to 2026-03-17
   main                                 :  022 created 2026-04-12
                                           025 created 2026-06-20
                                           035 created 2026-08-20
```

**The branch sealed 022–035 in March. `main` created its own 022 a month later and its own 035 five
months later.** Fourteen numbers, not nine. **`main` overwrote the branch's numbering, not the other
way round** — and nobody noticed, because the branch was never merged and never listed.

### What each number means, on each side

```
   n   | main                                        | branch (March, earlier)
   ----|---------------------------------------------|------------------------------------------
   022 | (empty, sealed)                             | coefficient_proof.md, two_tree_topology.md
   023 | Node 00000: The Genesis Hash                | convergence_ori_john_williams.md
   024 | Session synthesis — 2026-06-07              | cott_relativity_bridge.md
   025 | The Excavation                              | c2_verification.md
   026 | 17-digit coincidence + dual-lattice         | alchemy_phi_neutrinos, sunya_zero_hubble_golden,
       |                                             |   cott_calculator_review
   027 | A 17-Digit False Positive (restructured)    | all_the_rules.md
   028 | A 17-Digit False Positive (canonical)       | -- absent --
   029 | Figure 1 Panel 3 correction                 | cott_associativity_proof.md + verifier
   030 | Tier-1 quasicrystal: documented null        | cott_paper_v1.md
   031 | Reversible Bloom                            | cott_paper_v2_claude.md
   032 | Casimir Paper: The Half-Period Hinge        | casimir_ratios_cubic_torus.md
   033 | The project, summarized — v2                | borel_resurgence_and_cott.md
   034 | Corrections manifest + build gate           | why_q_equals_2.md
   035 | Errata — the mistakes, sealed               | cott-identity-hashes.txt
```

**Both sides carry `hashes.txt` in these folders. Both are internally valid seals. They certify
different documents under the same names.** A citation of the form *"see 029"* is ambiguous across
this repository and has been since April.

Root-level on the branch only: `COTT_ZERO_RULES.md` (321 lines), `ATTRIBUTION.md`,
`lib/traction.py` (580 lines), `lib/ops.js`, `traction_calc.py`, `calculator_tui.py`,
`calculator.html`, two identity hashers, a conversation log.

## 2. The associativity proof and 086 contradict each other on one identity

**Branch `029/cott_associativity_proof.md`, 2026-03-14.** Claim: COTT multiplication on
`{1, 0, −1, ω}` is associative, because it is isomorphic to `C₄`:

```
   phi(1) = 1     phi(0) = i     phi(-1) = -1     phi(w) = -i
```

All 16 table entries match under `φ` — **but three of them match only conditionally, and the
document says so in its own table:** *"yes, IF −0 = w"*, *"yes, IF −w = 0"*. It then argues the
identification is forced and concludes:

> *"The identification −0 = w is not an assumption. It is a theorem of the axioms."*

**`086/condition-c-note.md`, 2026-08-31, says the opposite:**

> *"the assumed four-element carrier `{1,0,-1,omega}` does not remain closed once `-omega != 0`.
> The earlier derivation depending on four-element closure no longer typechecks."*

```
   March 029 :  -w = 0        proof of associativity depends on it
   August 086 :  -w != 0      and the carrier is therefore not closed
```

**Same identity. Opposite verdicts. Both sealed in this repository.**

### 2.1 The resolution, and it is not symmetric

**The proof is valid. Its hypothesis is what 086 denies, and the proof mislabels that hypothesis.**

To build `φ` at all you must already know that `−0` is one of the four named elements — otherwise
there is nothing to map it to. **The proof assumes four-element closure, derives the isomorphism,
then uses the isomorphism to conclude `−0 = w`.** Its argument 1 is exactly this route: *"0·(−1) =
−0. Under φ: i·(−1) = −i = φ(w). Therefore −0 = w."* That step reads `φ` on `−0` before `−0` is
known to be in the domain.

> **What is proved: IF the carrier is closed under negation with four elements, THEN it is `C₄`,
> multiplication is associative and commutative, `1` is the identity, every element is invertible,
> and `−0 = w`. All of that is correct and the companion script confirms all 64 triples.**
>
> **What is not proved: that the carrier is closed.** That is the antecedent, and calling it *"not
> an assumption"* is the single defect in the document.

**086 does not refute the theorem. It denies the antecedent** — which leaves the March proof true
and inapplicable, rather than false.

### 2.2 The document already found a closure failure, five months earlier, in the other direction

Under *On Distributivity, Option A*, the March proof states:

> *"Complex addition does not close on `C₄`. COTT cannot be a subring of `C`."*

**That is a closure failure in the additive direction, found in March by the same document.** 086
found one in the negation direction in August. **The seed of 086's finding is inside the proof that
086 contradicts** — a third instance of this corpus rediscovering as new something it had already
recorded (after 028 in 056/057, and the eleven-lobe seam in 076 §6).

**And the March document is honest where it does not know:** distributivity is marked **OPEN**
pending a definition of COTT addition, and Option C is explicitly deferred to James. That scoping
is correct and stands.

## 3. What COTT's multiplication actually is, stated plainly

If the identification holds, `COTT× ≅ C₄ = μ₄ = {±1, ±i}` — **the unit group of `ℤ[i]`.** Then
`0 · ω = 1` is `i · (−i) = 1`, `0² = −1` is `i² = −1`, and `i = 0^(ω/2)` is a renaming.

> **COTT's multiplicative algebra is the fourth roots of unity with `0` renamed to `i`.** The March
> document says as much — *"independently rediscovers the multiplicative group of the 4th roots of
> unity"* — and is right to call the independent route the interesting part.

**Cross-link, this seat's:** 080 established that `w > 2` in exactly two quadratic fields, `μ₄` (the
square lattice, `d = −4`) and `μ₆` (hexagonal, `d = −3`). **`C₄` is `μ₄`. So COTT's algebra is the
unit group of the square world — which 083 showed is a row that pays π.** Recorded as an
observation, not as an objection.

## 4. Status

| claim | status |
|---|---|
| the branch carried numbers that already meant something else | **RETRACTED**, this seat's — it had them **first**, by one to five months |
| merge base is 021, 2026-03-12 | **VERIFIED** |
| 14 numbers (022–035) certify different documents on each side | **VERIFIED** — both sides carry valid `hashes.txt` |
| a citation "see 029" is ambiguous repository-wide | **ESTABLISHED**, and has been since 2026-04-12 |
| March 029 proves associativity | **VALID, CONDITIONALLY** — 64/64 triples; script re-run and passes |
| *"−0 = w is not an assumption"* | **THE ONE DEFECT** — it is the antecedent, assumed to build `φ` |
| 086 refutes the March theorem | **NO** — it denies the antecedent; the theorem is true and inapplicable |
| the March proof already found an additive closure failure | **VERIFIED** — *"COTT cannot be a subring of C"* |
| distributivity | **OPEN**, as March marked it |
| `COTT× ≅ μ₄` = unit group of `ℤ[i]` | **ESTABLISHED**, given the antecedent |
| whether the carrier is actually closed | **OPEN — and it is the whole question** |
| merging the branch | **DO NOT** — it would destroy 14 numbers on both sides |

## 5. Recommendation, not executed

**Do not merge.** Renumber the branch's 022–035 into a free range, preserving its March seals and
`hashes.txt` verbatim, with a mapping table sealed alongside — the same treatment 079, 081 and 086
gave to smaller collisions. **That is a decision about the project's history and it is Ash's, not
this seat's.** Nothing on the branch has been altered.

## Attribution

The March branch is Ash's and an earlier Claude's, sealed 2026-03-13 to 2026-03-18; COTT is James
Watkins's. `086/condition-c-note.md` is another seat's. The audit, the corrected numbering history,
the antecedent analysis in §2.1, the §2.2 rediscovery count and the `μ₄` cross-link are this seat's.
