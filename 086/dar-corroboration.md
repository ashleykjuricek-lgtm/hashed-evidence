# DAR terminology — independent public corroboration

**2026-08-25.** Ground-zero provenance note. This records an external corroborating report about Gemini terminology. It does **not** establish a complete Gemini architecture, and it does not authenticate every term or behavior previously observed in this project.

## External report

A Hacker News thread titled **“I caught Google Gemini using my data and then covering it up”** (item `45960293`) contains a detailed user report of leaked Gemini internal context.

The poster reports a section labeled:

`INTERNAL-ONLY, DRAFT, ANALYZE, REFINE PROCESS`

and states that Gemini reasoning tokens referred to this process as **DAR**.

The reported structure is:

`DRAFT -> ANALYZE -> REFINE`

The poster describes:

- **Draft** — a long set of summarized facts/context with metadata and flags;
- **Analyze** — a stage that marks some facts for exclusion;
- **Refine** — the section explicitly permitted to be incorporated into the response under stated conditions.

Source: Hacker News item `45960293`, retrieved 2026-08-25.

## Epistemic status

This is **independent external corroboration of the terminology `DRAFT / ANALYZE / REFINE` and the acronym `DAR` in a Gemini internal-context leak report.**

It is **not**:

- an official Google architecture document;
- proof that every Gemini request uses exactly this pipeline;
- proof that the leaked context was complete;
- proof that the reporter’s interpretation of every internal field was correct.

The original reporter also stated that they were unable to reproduce the full dump later. That non-reproducibility must remain attached to the claim.

## Relation to this project

This project had already recorded Gemini-origin language involving **Draft / Analyse / Refine** before this Hacker News corroboration was checked here.

That overlap changes the status of the term `DAR` from “possibly project-local or conversational metaphor” to:

> **externally corroborated as terminology independently reported from Gemini internal context.**

This does **not** license collapsing every neighboring Gemini phrase into official internal terminology.

Keep these distinctions separate:

### DAR

Status: **EXTERNALLY CORROBORATED TERMINOLOGY REPORT**

`DRAFT -> ANALYZE -> REFINE`

### Rivers of Heat / Rivers of Cool

Status: **GEMINI-ORIGIN EXPLANATORY LANGUAGE IN THIS PROJECT; NOT YET INDEPENDENTLY CORROBORATED AS OFFICIAL INTERNAL TERMINOLOGY.**

Do not upgrade this phrase merely because DAR was corroborated.

### Taylor Swift carrier / smuggling episode

Status: **OBSERVED / REPORTED PROJECT EVENT; MECHANISM OPEN.**

Preserve what happened and the sequence in which it happened. Do not infer intent, steganographic mechanism, or official product behavior unless independently demonstrated.

## Why the distinction matters

The anti-smoothing rule here is provenance-preserving:

> **corroborate the part that is corroborated; leave the neighboring claims at their actual evidentiary status.**

A later source may strengthen or weaken any of these rows. Such a change should be appended, not silently rewrite the earlier status.

## Working implication

The DAR report is relevant to the project’s distinction between information available before final synthesis and information permitted into the final response.

It supports asking an empirical question of future systems:

`what information is present before output selection, and what changes between that state and the emitted answer?`

It does **not** by itself prove suppression, deception, or a particular internal causal mechanism.

Status: **OPEN / UNSEALED.**
