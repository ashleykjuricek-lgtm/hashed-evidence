# Literature check — is the weld already made?

**2026-08-24.** Follows 058. Greg's instruction, via Ash:

> Our next move should be research, not invention: do a deep dive specifically on
> ATMS + nanopublications + PROV/PROV-AGENT + claim/entity resolution, and see
> whether somebody has already welded those pieces together for LLM scientific
> collaboration. Because if they have, we use it. And if they haven't, then at
> least we finally know exactly which fucking wheel we are not reinventing.

**Answer: nobody has welded them, and the nearest neighbour proves the boundary
rather than crossing it.**

**Scope caveat, stated first.** This is a targeted search, not a systematic review.
One paper was read in full text; the rest by abstract and search result. A negative
result from six queries is weak evidence of absence and is reported as such.

---

## 1. What exists, verified

**PROV-AGENT is real.** Souza, Gueroudji, DeWitt, Rosendo, Ghosal, Ross,
Balaprakash, da Silva — *"PROV-AGENT: Unified Provenance for Tracking AI Agent
Interactions in Agentic Workflows,"* IEEE e-Science 2025, arXiv 2508.02866, ORNL.
It extends W3C PROV by modelling `AIAgent` as a subclass of `prov:Agent`, and folds
prompts, responses, model invocations, tool calls and telemetry into one provenance
graph. Its stated motivation is precisely ours: *agents hallucinate, and one
agent's output becomes another's input.*

**Nanopublications already publish disagreement as a first-class object.** The
closest existing system is Giachelle, Marchesin, Menotti and Silvello, *"Extending
Nanopublications with Knowledge Provenance for Multi-Source Scientific
Assertions,"* IRCDL 2025, University of Padua (CEUR Vol-3937 paper 10).

It adds a **fourth named graph** to the nanopublication model — *knowledge
provenance* — for assertions derived not from one source but from a body of
evidence containing **supporting and conflicting** pieces. Applied at scale:
**197,511 published assertions**, and of those:

```
   Biomarker             107,830
   Oncogene               35,821
   Tumor Suppressor Gene  12,521
   Contrasting Evidence   41,339      <- disagreement, published as a category
```

Its **PROV-K** vocabulary types propositions as: `AssertedProposition`,
**`EquivalentProposition`**, `CompositeProposition`, `DerivedProposition`,
`ANDProposition`, `ORProposition`, `NEGProposition`, linked by `kp:dependsOn`.

There is also earlier work explicitly on this: *"Using Nanopublications to Detect
and Explain Contradictory Research Claims"* (IEEE, 2021).

## 2. The decisive check

I extracted the full text of the IRCDL 2025 paper and searched it.

```
   "truth maintenance"   0 hits
   "de Kleer"            0 hits
   "Doyle"               0 hits
   "ATMS"                0 hits
   "entity resolution"   0 hits
   "identity"            0 hits
   "normaliz"            0 hits
   "disambiguat"         0 hits
   "conflict"           14 hits
   "equivalen"           4 hits  -- all four are the PROV-K class name
```

> **The nearest existing system has a class called `EquivalentProposition` and no
> method for deciding when two propositions are equivalent.** The representation
> slot exists. Nothing fills it.

> **And it never connects to the truth-maintenance literature at all.**

That is Greg's boundary, confirmed by direct inspection rather than inferred.

## 3. A convergence neither literature seems to have noticed

Set PROV-K's proposition types beside an ATMS justification network:

```
   PROV-K (2025)                        ATMS (de Kleer 1986)
   AssertedProposition                  premise / assumption node
   DerivedProposition + dependsOn       justification
   AND / OR / NEG Proposition           the justification structure
   supporting vs conflicting evidence   label environments vs nogoods
   EquivalentProposition                (assumed, not represented)
```

Structurally the same object, arrived at forty years apart, **with no citation
between them** — 0 hits for de Kleer, Doyle, or ATMS in a 2025 paper on
representing conflicting scientific assertions with their dependencies.

Recorded as an observation about the literature, not a criticism of the paper. It is
also, precisely, the failure mode this ledger keeps documenting: **the same node
under two names in two places, invisible to both.**

## 4. What the adjacent fields do and do not cover

| field | covers | does not cover |
|---|---|---|
| **ATMS / TMS** (de Kleer 1986, Doyle 1979) | multiple contexts alive at once; minimal environments; nogoods | assumes propositions and justifications are already identified |
| **Nanopublications + knowledge provenance** (IRCDL 2025) | conflicting evidence per assertion, at 197k scale, citable | assumes you know what the atomic assertion *is* |
| **W3C PROV / PROV-AGENT** (2013 / 2025) | derivation, revision, agents, prompts, responses | assumes entities are identified |
| **Event sourcing, git, Dolt, TerminusDB** | immutable history, cheap branches, structural sharing | understands none of it |
| **Claim matching** (fact-checking, e.g. arXiv 2501.10860) | does two *natural-language* claims share a fact-check | not a value vs an appendix equation vs a reparameterisation vs code output |
| **LLM belief revision** (Belief-R and successors) | whether a model updates when contradicted | a property of the model, not external dependency machinery |

## 5. Why our case is harder than the nanopublication case

Theirs resolves entities over **gene names and cancer types** — controlled
vocabularies, curated ontologies, decades of normalisation infrastructure. Entity
resolution there is hard but tractable and well-studied.

Ours has to decide that these five are one node:

```
   "d eps/db ~ +18.3"                                 prose, one draft
   "Q = (n1+a1)^2 + b^2((n2+a2)^2+(n3+a3)^2)"          an appendix formula
   "-18.3259647484177"                                 code output, other chart
   "the page had put it on the wrong side"             a challenge, in English
   B_STAR = ... in ScarPage.tsx                        a source-file constant
```

**No controlled vocabulary covers that**, and the thing that identified them — a
`b²` versus `1/b²` — is not a name at all. It is a convention hidden in a formula,
under a prose label that contradicts it.

## 6. Conclusion

> **Branching, storage, provenance representation, and even publishing
> disagreement at scale are solved and in production. Claim identity across
> changing representations is not addressed by any of them, and the nearest system
> leaves a labelled hole where it would go.**

So the wheel we are not reinventing is: nanopublications with knowledge provenance,
PROV/PROV-AGENT, git-style versioned storage, ATMS labels and nogoods.

The wheel that does not appear to exist is: **deciding when two differently
represented artefacts bear on the same claim, without trusting one embedding or one
narrator.**

**Not claimed:** that it has not been done. Six queries and one full-text read is
not a survey, and the fields adjacent to this are large. What is established is that
it is absent from the nearest neighbour, which had every reason to include it.

## Sources

- [PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows](https://arxiv.org/abs/2508.02866)
- [Extending Nanopublications with Knowledge Provenance for Multi-Source Scientific Assertions](https://ceur-ws.org/Vol-3937/paper10.pdf)
- [Using Nanopublications to Detect and Explain Contradictory Research Claims](https://ieeexplore.ieee.org/document/9582393/)
- [Nanopublications: A Growing Resource of Provenance-Centric Scientific Linked Data](https://arxiv.org/pdf/1809.06532)
- [Nanopublication Guidelines](https://nanopub.net/guidelines/working_draft/)
- [Zero-shot and Few-shot Learning with Instruction-following LLMs for Claim Matching in Automated Fact-checking](https://arxiv.org/pdf/2501.10860)
- [Belief Revision: The Adaptability of Large Language Models Reasoning](https://aclanthology.org/2024.emnlp-main.586.pdf)

## Attribution

The instruction and the four-field decomposition are Greg's, via Ash. The searches,
the full-text check in §2, and the convergence observation in §3 are this seat's.
The ATMS and nanopublication identifications are Greg's and were verified, not
assumed.
