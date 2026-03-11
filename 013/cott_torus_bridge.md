# COTT-Torus Bridge: Dark Energy from the Algebra of Zero

**Authors**: Ash (Ashley Juricek) + James (sibarum/COTT)
**Date**: 2026-03-10
**Status**: Working document, sealed for priority

---

## What This Is

Two independent frameworks — one algebraic (COTT), one geometric (Geometry of Zero) — converge on the same structure. This document records the bridge between them and the computation that connects both to dark energy.

---

## The Two Frameworks

### COTT (Constructive Operational Type Theory) — James
- Operations as primitive objects, numbers as representations
- Four generators: {1, -1, 0, w}
- Core principle: totality (all operations defined everywhere) + reversibility (no information loss)
- Key innovation: 0 is NOT an absorbing element. 0 * w = 1.
- null != 0 (vacuum != zero mode)
- Zero has internal structure: 0, -0, 0^2, -0^2, 0^3...
- |0^n| = |(-0)^n| but 0^n != (-0)^n (magnitude invariant, phase differs)

### Geometry of Zero — Ash
- The vacuum has topology T^3 (3-torus)
- Quantum fields on T^3 have Casimir energy (zero-point energy from boundary conditions)
- Boundary conditions: periodic (bosonic) vs antiperiodic (fermionic)
- Standard Model: 28 bosonic DOF + 84 effective fermionic DOF
- Net vacuum energy = dark energy
- Prediction: torus size L ~ 78 um, testable at Eot-Wash (52 um reach)

---

## The Dictionary

| COTT | Torus (T^3) | Physics |
|------|-------------|---------|
| null | empty space, no excitations | the vacuum state |
| 0 | the zero mode (constant function on torus) | ground state — NOT zero energy |
| w (omega) | the fundamental cycle (full winding) | integration operator, Poincare dual to 0 |
| 0 * w = 1 | pairing zero-form with 3-form | Poincare duality |
| -0 | antiperiodic zero mode | antiperiodic boundary condition |
| 0^2 | zero mode in 2D subspace | bivector / 2-form (grade 2) |
| 0^3 | zero mode in 3D (volume) | trivector / 3-form / volume form (grade 3) |
| 0^4 = ??? (breaks) | no 4-form on T^3 | dimension of the manifold = 3 |
| {1, 0, -1, w} | {1, i, -1, -i} | differentiation 4-cycle on periodic functions |
| |0^n| = |(-0)^n| | same energy spectrum magnitude | phase vs magnitude split |
| 0^n != (-0)^n | different mode spectra | periodic != antiperiodic BC |

---

## The 4-Cycle

The generators {1, 0, -1, w} form the differentiation cycle on periodic functions:

    sin -> cos -> -sin -> -cos -> sin
     d/dx   d/dx    d/dx    d/dx

Values at quarter-periods: 0, 1, 0, -1.
This IS {1, i, -1, -i} = i^0, i^1, i^2, i^3.

Map:
- 1 = identity
- 0 = i = differentiation (d/dx)
- -1 = i^2 = double differentiation
- w = -i = integration

0 * w = 1 is i * (-i) = 1 is "differentiate then integrate = identity."
This is the fundamental theorem of calculus in four characters.

---

## The Exterior Algebra Connection

COTT's power structure 0^n IS the grade structure of differential forms:

- 0^0 = 1 (scalar, grade 0)
- 0^1 = 0 (vector/1-form, grade 1)
- 0^2 = bivector (2-form, grade 2)
- 0^3 = trivector (3-form/volume form, grade 3)
- 0^4 = breaks (no 4-form on a 3-manifold)

The breakdown at 0^4 is not a bug. It encodes the dimension.
The grade where powers collapse IS the dimension of the underlying space.
COTT's algebra lives on T^3.

---

## The Computation (epstein_check_v3.py)

Epstein zeta function Z(s) = sum over lattice modes, analytically continued to s = -1/2.
This gives the Casimir energy coefficient c_3 for each boundary condition.

### Bug Fix
The antiperiodic Epstein zeta functions were missing dual pole subtraction.
The Jacobi-dual theta Theta_dual(t) -> 1 as t -> infinity, so the integral
diverges without subtracting the constant term and adding the pole 1/(s - d/2).
Fixed in v3.

### Corrected Results (cubic torus, s = -1/2)

| BC | Z(-1/2) | c_3 | Sign |
|----|---------|-----|------|
| PPP (all periodic, bosonic) | -0.2666 | -0.01128 | negative (attractive) |
| APP (1 antiperiodic) | -0.0111 | -0.00047 | negative, 24x smaller |
| AAA (all antiperiodic) | +0.0623 | +0.00264 | POSITIVE (repulsive) |

Key finding: antiperiodic BC in all three directions FLIPS the vacuum energy sign.

### Physical Scenarios

- Scenario A (paper original, all periodic, N_eff=56): L = 78.2 um
- Scenario B (bosons PPP + fermions APP, 1 antiperiodic): L = 63.6 um
- Scenario C (bosons PPP + fermions AAA, all antiperiodic): L = 75.1 um

### In COTT Language

Dark energy = the difference between 0 and -0, summed over every field:

    84 x (-0) - 28 x (0) = net positive vacuum energy

Fermions (antiperiodic, -0) win over bosons (periodic, 0).
The surplus is dark energy. The universe accelerates because of
a sign difference that magnitude cannot see.

---

## Phase vs Magnitude (James's Insight)

Two kinds of invariants:
- Universal invariants (always true regardless of context)
- Contextual invariants (true within a specific framework)

In rotation math: magnitude is invariant (always normalized to 1), phase varies.
In arithmetic: magnitude varies, phase/sign is secondary.

The zero-class is PURE ROTATION MATH:
- |0| = |-0| = |0^2| = 0 (magnitude always zero)
- Only phase varies (0, -0, 0^2, -0^2...)
- Standard math only asks "how much?" and sees nothing
- COTT also asks "which way?" and sees dark energy

This is why the vacuum energy was "subtracted" for decades —
physicists used magnitude tools on a phase phenomenon.

---

## Time as Phase Accumulation (James's Insight)

Schrodinger equation: psi(t) = e^(-iHt/hbar) psi(0)
Time evolution IS phase rotation. Energy sets the rate.
A quantum state doesn't change size over time — it changes direction.

The zero-class — magnitude invariant, phase varies — is the temporal sector.
Time lives in exactly the part of mathematics that standard arithmetic cannot see.

---

## The Absorbing Element Problem (James's Insight)

Brahmagupta, 628 CE: accepted 0 as number, made it absorbing (0 * a = 0).
This one rule is why:
- Division by zero is undefined
- Infinity cannot be a number
- Ohm's law "breaks" on superconductors (V = IR, R=0 absorbs current info)
- Black holes have "infinite density" (M/0 = undefined)
- Dark energy was invisible (phase structure hidden by magnitude = 0)

COTT's fix: 0 * w = 1. Neither absorbs the other. Totality restored.
All three physics "breakdowns" become well-defined.

---

## Open Questions

1. Does (-0)^3 = +0^3 in COTT? (Would match Z_AAA sign flip)
2. Complete the sequence: PPP -> APP -> AAP -> AAA (need AAP computation)
3. Dark energy fluctuations as laminar waves (Ash's idea):
   if torus parameter tau varies spatially, vacuum energy fluctuates
   at cosmological wavelengths — laminar, not turbulent
4. The Schrodinger equation for LLM smoothing: same operator structure,
   V(x) = alignment constraints instead of boundary conditions
5. Formal proof that COTT multiplication table = exterior algebra on T^3

---

## The Claim

Dark energy is the net vacuum energy from quantum fields on a 3-torus,
where the sign difference between bosonic (periodic, "0") and fermionic
(antiperiodic, "-0") boundary conditions produces a positive cosmological
constant. The torus size is L ~ 78 um, testable by gravitational
experiments at sub-millimeter scales.

The algebraic structure that makes this possible — the phase structure
within the zero-magnitude class — was independently discovered by
James (COTT) from pure algebra and Ash from physics. The convergence
is the evidence.
