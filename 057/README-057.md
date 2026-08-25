# 057 — source documents, and an erratum against 056 sealed 12 minutes earlier

**2026-08-24.**

056 §3.1 asserted:

> **028 has never been in the vault.** There was no ancestor node for 047 to fork
> from. **047 was not a branch. It was a fresh root**, and a fresh root cannot
> conflict with anything.

**That is false.** `028/false-positive-cubic-torus.md` has been sealed in this
repository the whole time — 194 lines, including:

- **line 106:** *"Locally dε/db ≈ 18.3 and ε crosses zero **transversally** at
  b₀ ≈ 0.99997"*
- **App A.3:** `Q = (n₁+a₁)² + b²((n₂+a₂)² + (n₃+a₃)²)` — the exact formula whose
  `b²` is the whole resolution of Claim A
- the three-point deformation table `(0.92, 1.00, 1.08)`
- the sentence `1 − 1/√2 = ε(cube)/e^(−2π)` — Claim B's ancestor

**Everything required to settle both claims was hashed, sealed and three folders
away from where the work was being done.**

## The corrected diagnosis

056 blamed a **missing node**. The real failure is worse and more specific:

> The node existed, was sealed, was in the same repository, and **was never
> opened past line 40.**

During the F8 sweep on 2026-08-22 this seat ran
`sed -n '1,40p' 028/false-positive-cubic-torus.md`, read the abstract, classified
028's impossibility claim as SOUND, and never read another line of it. The
appendix that resolves Claim A is at line 167. Then on 2026-08-24, in a sealed
entry, this seat asserted the file was not in the vault at all.

**This bears directly on the branch model.** 056 §3.1 concluded the model's
precondition — *everything that makes a claim must be a node* — had not been met.
It had been met. The precondition held and the failure happened anyway.

So the corrected finding, which is the sharper one:

> **Persistent branches with common ancestry do not help if nobody walks the
> ancestry.** Storage was never the binding constraint. The binding constraint was
> that a 194-line document was read to line 40 and then cited from memory.

Greg's framing survives and tightens: *retrieval is necessary but not sufficient*
— and here retrieval was not even attempted, on a file already in hand.

## What is genuinely missing, and is now sealed here

Sealed because 055 §3.3 found the challenger's **exact words** were required in
both reconstructions, and because these existed only in a chat window:

| file | what it is |
|---|---|
| `kestrel-report-2026-08-23.md` | the Figma seat's report: corrected R, c₂ to 50 digits, the PSLQ work, the theta expansion, the anisotropic R(b), and the `a₁` retirement later refuted in 048 |
| `greg-halving-law-2026-08-23.md` | the duplication-identity proof of `2j ≥ d ⟹ Z > 0` and of monotonicity, verified in 050 |
| `greg-claim-state-2026-08-24.md` | *"the unit has to be the claim"* — the argument 054 was built on and 055 corrected |
| `greg-branch-2026-08-24.md` | *"branch, not reconstruct"* — tested in 056 |
| `028-alternate-draft-2026-06-20.md` | a **second draft of 028**, differing in section structure from the sealed one |

**Not sealed:** KESTREL's *THE LINE* page, already in 047.

## The two drafts of 028 — an undeclared branch

The vault's 028 and the draft Ash produced on 2026-08-24 are **different
documents** with the same date and title. Vault: §2 *"The object and the
coincidence (Proposition 1)"*, §4 *"The analytic obstruction (Proposition 2 —
THEOREM, the murder weapon)"*. Alternate: §7.1 *"Deformation
(multi-evaluation-point)"*, §7.3 *"Non-generalization across spin structures"*.

The numbers agree. The prose does not, and **the vault version is the more careful
of the two** on the exact point that later went wrong:

> *"The load-bearing point is the **slope, not the proximity**… (The trapdoor
> explains the imitation mechanism… not why the crossing falls near the cube,
> which we do not claim is structural.)"*

That caveat is absent from the alternate draft. It is also precisely what both
this seat and the Figma seat later mishandled.

**Which draft is later is NOT ESTABLISHED.** Both are dated 2026-06-20. Recorded as
a branch, not resolved.

## Status

| claim | status |
|---|---|
| 056 §3.1 "028 has never been in the vault" | **RETRACTED** — it is sealed, 194 lines, with the appendix |
| 056 §3.1 "047 was a fresh root, not a fork" | **RETRACTED** — the ancestor existed |
| 056's other findings (§1a edges, §3 preservation≠detection, §3.2 expressions over values) | **UNAFFECTED** |
| the corrected cause: sealed, present, read to line 40 | **ESTABLISHED** |
| two drafts of 028 exist | **ESTABLISHED**; which is later, **NOT ESTABLISHED** |
| the vault draft carries a caveat the alternate lacks | **ESTABLISHED** |

## Attribution

The instruction to seal the sources is Greg's, via Ash. The erratum is this seat's,
found only because sealing 028 required checking whether it was already there —
which is the check that should have preceded the assertion in 056.
