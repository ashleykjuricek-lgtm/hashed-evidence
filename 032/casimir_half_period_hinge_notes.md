# Casimir Paper Update: The Half-Period Hinge

Prepared for Ash Korth / Claude Code handoff.

## Purpose

This note is meant to update the newer audited Casimir paper, not revive the older “Near-Rational Casimir Ratios” draft as the final skeleton.

The older draft already contains the important seed:

- PPP uses `alpha = (0,0,0)`.
- APP uses `alpha = (1/2,0,0)`.
- In theta language, the comparison is localized to replacing one `theta_3` factor with `theta_2`.

The update should foreground that half-period shift as the structural hinge of the calculation while preserving the later, safer audit framing:

> The near-`1/24` value is a structured cancellation residue of the half-shifted spectral lattice, not a proven closed-form `q`-series identity.

Do not let the paper drift back into “we derived the full correction” language unless the proof is actually included.

---

## Recommended Placement

Add a new subsection immediately after the paper defines the periodic and antiperiodic sectors.

Suggested title:

## 2.1 The Half-Period Hinge

---

## Insertable Draft Section

### 2.1 The Half-Period Hinge

Periodic and antiperiodic boundary conditions differ by a half-period shift in one lattice direction. In the Epstein-zeta representation, the periodic sector is indexed by

```math
\alpha_{PPP}=(0,0,0),
```

while the singly antiperiodic sector is indexed by

```math
\alpha_{APP}=\left(\frac12,0,0\right).
```

Thus APP is not merely PPP with one mode removed or one sign changed. It is a different spectral lattice: one coordinate has been shifted by half a period before the regularized sum is formed.

Equivalently, in the theta representation on the cubic torus, the boundary-condition change appears as a single theta-factor replacement:

```math
\Theta_{PPP}(t)=\theta_3(it)^3,
```

```math
\Theta_{APP}(t)=\theta_2(it)\theta_3(it)^2.
```

The entire APP/PPP comparison is therefore localized to the replacement

```math
\theta_3 \longrightarrow \theta_2
```

in one direction. This replacement is the structural hinge of the calculation.

Geometrically, periodicity says that after one circuit of the torus, the field returns to itself:

```math
\phi(x+L)=\phi(x).
```

Antiperiodicity says that after one circuit, the field returns with opposite sign:

```math
\phi(x+L)=-\phi(x).
```

The half-shift is the spectral expression of this sign reversal. It changes the allowed modes, removes the ordinary zero-mode channel, and alters the cancellation pattern shell by shell.

For this reason, the near-`1/24` behavior should not be treated as a primary numerological target. The more precise statement is that the observed ratio is downstream of a half-period spectral obstruction. The APP lattice differs from PPP by a phase inversion in one direction, and the resulting quotient records the residual effect of that obstruction after analytic continuation.

In the audited formulation, the near-rational value is therefore interpreted not as evidence for a simple closed-form identity, but as a structured residue of the half-shifted lattice comparison.

---

## Abstract Revision

Use this if the current abstract still overclaims the first-order modular correction.

```text
We compute the ratio R = Z_APP(-1/2)/Z_PPP(-1/2) of analytically continued Epstein-zeta values on the cubic three-torus, comparing periodic boundary conditions with a singly antiperiodic half-period shift alpha = (1/2,0,0). Numerically, R is close to 1/24 but not equal to it. We show that the APP/PPP comparison is controlled by a single spectral replacement, theta_3 -> theta_2, corresponding to the half-shifted lattice direction. Later shell-level analysis indicates that the near-rational value is best understood as a structured cancellation residue rather than as a proven analytic q-series identity. We provide reproducible numerical evaluations, an Ewald/Poisson decomposition, and a shell audit isolating the terms responsible for the deviation. The origin of the dimension-specific closeness to 1/24 remains open.
```

---

## Short Intro Patch

Use this in the introduction if it currently says the paper is “explaining why the value is near `1/24`” too strongly.

```text
The central structural feature of the APP/PPP comparison is the half-period shift in one lattice direction. Passing from PPP to APP replaces alpha = (0,0,0) with alpha = (1/2,0,0), or equivalently replaces one theta_3 factor by theta_2 in the theta representation. This half-shift changes the spectral lattice before analytic continuation is performed. The near-1/24 ratio is therefore treated here as a downstream residue of the half-shifted lattice comparison, not as a primary closed-form target.
```

---

## Notes for Claude Code

```text
TASK: Update the Casimir paper to foreground the half-period hinge while preserving the later audited framing.

1. Add a new subsection after Setup titled:
   “The Half-Period Hinge”

2. Insert the supplied subsection text. Keep the tone formal. Do not add metaphors.

3. Make sure the paper defines:
   PPP: alpha = (0,0,0), zero mode excluded
   APP: alpha = (1/2,0,0)

4. Preserve the theta-factor statement:
   Theta_PPP(t) = theta_3(it)^3
   Theta_APP(t) = theta_2(it) theta_3(it)^2

5. Add one explicit sentence:
   “The APP/PPP comparison is localized to the replacement of one theta_3 factor by theta_2.”

6. Do NOT claim that the near-1/24 value has a proven closed form.

7. Downgrade any language like:
   “we derive the first-order correction”
   “the correction is forced”
   “the coefficient is proven”
   “both derived”
   “full closed form”
   unless the later audit already proves it.

8. Replace with safer language:
   “observed”
   “captured numerically”
   “consistent with”
   “suggestive of”
   “not established as an analytic identity”
   “single-point cancellation residue”
   “half-shifted spectral obstruction”

9. Audit the sentence:
   “Casimir energies on T^d are encoded by Epstein zeta functions analytically continued to s = -d/2.”
   For the ratio used in this paper, the relevant evaluation is s = -1/2. Do not leave a contradictory s = -d/2 statement unless separately justified by a clearly defined normalization.

10. Check all numerical values against the later audited values.
    The old draft used R = 0.041689414162...
    Later audit may use R = 0.04168941460272377512...
    Do not mix old and new values.

11. If the first-order q correction remains in the paper, mark it as an empirical/modular ansatz or first-order approximation, not as a theorem, unless the proof is included.

12. Keep physical speculation, dark-energy scale, Koide geometry, and cosmological-constant language out of the main theorem unless placed in a clearly labeled speculative/model-dependent section.

13. Add a short interpretive note after the shell audit:
    “The shell audit supports the interpretation that the near-rational behavior is a residue of the half-shifted APP lattice, not an analytic q-series identity.”
```

---

## Optional Commit Message

```text
docs(casimir): foreground APP half-period hinge and downgrade q-series claims

- add half-period hinge subsection after setup
- clarify APP as alpha=(1/2,0,0), not PPP with a removed term
- connect theta_3 -> theta_2 replacement to spectral phase inversion
- preserve audited framing: near-1/24 as cancellation residue, not closed form
- add guardrails against overclaiming first-order modular correction
- flag s=-1/2 and numerical value audit points
```

---

## Claims to Keep

These are safe and useful.

```text
APP differs from PPP by a half-period shift in one lattice direction.

The theta representation localizes the APP/PPP difference to one theta-factor replacement.

The half-shift changes the allowed spectral modes before analytic continuation.

The near-1/24 value is numerically stable and structurally meaningful.

The later shell audit supports a cancellation-residue interpretation.

The deeper reason for the dimension-specific closeness remains open.
```

---

## Claims to Avoid

These are too strong unless independently proved in the later paper.

```text
We derive the exact correction.

The coefficient is proven by modular symmetry.

The q-series is analytic.

The 1/24 ratio is explained completely.

The result proves a cosmological-constant model.

The dark-energy scale follows necessarily.

The dimension-three phenomenon is analytically solved.
```

---

## Tiny Human Note

The old draft found the door.

The newer audited paper should name the hinge.

The hinge is the half-period shift:

```math
n \mapsto n+\frac12
```

or, in boundary-condition language:

```math
\phi(x+L)=-\phi(x).
```

Everything else should be treated as downstream until proved otherwise.
