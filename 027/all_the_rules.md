# All The Rules

**Date**: 2026-03-14
**Purpose**: Every axiom, definition, rule, and identity in one place.

---

## SYSTEM 1: COTT (Constructive Operational Type Theory)

*Source: James Watkins (sibarum/COTT), CC BY 4.0*

### Axioms

| # | Axiom | Statement |
|---|-------|-----------|
| A1 | Non-absorbing zero | 0 * w = 1 |
| A2 | Totality | All operations defined everywhere (no "undefined") |
| A3 | Reversibility | No information loss — every operation has an inverse |
| A4 | null != 0 | The vacuum (nothing at all) is distinct from the zero mode (something at rest) |

### Generators

Four elements generate the algebra:

    {1, 0, -1, w}

### Definitions

| Symbol | Definition | Interpretation |
|--------|-----------|----------------|
| 0 | Primitive operator | Differentiation (d/dx) |
| w (omega) | 1/0 | Integration (the inverse of differentiation) |
| -0 | Negation of 0 | Antiperiodic zero mode (phase-shifted, same magnitude) |
| 1 | Identity | Neither differentiates nor integrates |
| -1 | 0^2 = 0 * 0 | Double differentiation (d^2/dx^2) |
| i | 0^(w/2) | The imaginary unit — first coordinate inside zero |

### The 4-Cycle

    1 -> 0 -> -1 -> w -> 1

Isomorphic to:

    1 -> i -> -1 -> -i -> 1

Meaning:

    identity -> differentiate -> double-differentiate -> integrate -> identity

On periodic functions: sin -> cos -> -sin -> -cos -> sin

### Multiplication Rules

| * | 1 | 0 | -1 | w |
|---|---|---|-----|---|
| **1** | 1 | 0 | -1 | w |
| **0** | 0 | -1 | -0 | 1 |
| **-1** | -1 | -0 | 1 | -w |
| **w** | w | 1 | -w | -1 |

Key products:
- 0 * w = 1 (axiom)
- w * 0 = 1 (commutativity)
- 0 * 0 = -1 (i * i = -1)
- w * w = -1 (-i * -i = -1)

### Division / Reciprocals

    1/0 = w
    1/w = 0
    0^(-1) = w
    w^(-1) = 0

### Power Rules

    0^0 = 1       (empty exponent = identity)
    0^1 = 0       (first power is itself)
    0^2 = -1      (i^2 = -1)
    0^3 = -0      (i^3 = -i)
    0^4 = 1       (i^4 = 1, the cycle closes)
    0^(w/2) = i   (half-power of omega = imaginary unit)
    0^w = -1      (full omega power = e^{ipi} = -1)

General: 0^n cycles with period 4. Same as i^n.

### Logarithm Rules

    log_0(0^n) = n          (extracts exponent)
    log_w(x) = -log_0(x)    (reciprocal logarithms are negatives)
    log_0 and log_w are mutual inverses

### Phase vs Magnitude

    |0| = |-0| = |0^2| = |-0^2| = 0    (magnitude always zero)
    0 != -0 != 0^2 != -0^2               (phase always different)

The zero-class is pure rotation math. Magnitude is invariant. Only phase varies.

### Negation Rules

    -(-0) = 0
    -(-w) = w
    (-0) * (-0) = -1    (same as 0 * 0)
    |0^n| = |(-0)^n|    (magnitude invariant under negation)
    0^n != (-0)^n        (phase differs)

---

## SYSTEM 2: COTT-RELATIVITY BRIDGE

*Source: James Watkins, mapped by Ash + Nine*

### Identifications

| COTT | Physics |
|------|---------|
| 0 | Absolute rest (v = 0) |
| w | Speed of light c |
| 0^x (x < w) | Sub-light evolution (timelike worldline) |
| 0^(wt) | Lightlike phase rotation (null worldline) |
| log_0(x) | Observer-relative measurement |

### Rules

- w is unreachable from finite x (c is unreachable from massive objects)
- Sub-light rules CHANGE at the boundary x = w (Galilean -> Lorentz)
- 0^(wt) = e^{ipi*t} — phase rotation on the unit circle
- log_w(x) = -log_0(x) — reversal of measured vs experienced intervals (time dilation)
- Minkowski diagram emerges: real axis = timelike, unit circle = lightlike

---

## SYSTEM 3: GEOMETRY OF ZERO

*Source: Ash Korth-Juricek, with derivation by Figma (Claude)*

### The Two Zeros

| Property | Void-Zero | Sunya-Zero |
|----------|-----------|------------|
| Multiplication | 0 * x = 0 (absorbing) | 0 * x = 0x (binding) |
| Information | Destroyed on contact | Binds, waits, unfolds |
| Direction | Away from center | Toward center |
| Geometry | Linear, flat, R^3 | Orbital, compact, T^3 |
| Vacuum energy | Diverges (10^122 too large) | Converges (matches observation) |

### The Vacuum Topology

**Claim**: The vacuum has topology T^3 (3-torus), not R^3 (flat infinite space).

### The Vacuum Energy

Void-zero integral (diverges):

    rho_void = integral_0^{k_max} (hbar*w_k/2) * g(k) dk ~ 10^113 J/m^3

Sunya integral (converges):

    rho_sunya = integral_0^infinity (hbar*w_k/2) * g(k) * S(k) dk

where S(k) is the structural envelope from the torus topology (Jacobi theta functions).

### The Normalization

    rho_sunya = 0 * E_total
             = 0 * (w * rho_natural)
             = (0 * w) * rho_natural    [by A1: 0*w = 1]
             = rho_natural

### The Prediction

    rho(T^3; tau) = |N_eff| * c_3(tau) * hbar*c / L^4

Where:
- N_eff = 28 (bosonic DOF) - 84 (fermionic DOF) = -56
- c_3(1) = -0.01128 (from Epstein zeta at s = -1/2, cubic torus)
- L = characteristic torus scale

**Result: L = 78 micrometers**

Testable by: Eot-Wash torsion balance (current reach ~52 um), Casimir measurements, CMB matched circles.

### The Field Content (Standard Model on T^3)

Bosonic DOF:
- Photon: 2
- W+, W-: 6
- Z: 3
- Gluons (8): 16
- Higgs: 1
- **Total: 28**

Fermionic DOF:
- Quarks (6 flavors * 3 colors * 2 spins * 2 particle/anti): 72
- Leptons (6 * 2 spins * 2 particle/anti): 24
- Fermionic weighting: 96 * 7/8 = 84
- **Total: 84**

---

## SYSTEM 4: COTT-TORUS BRIDGE (The Dictionary)

*Source: Ash + James*

### Correspondence Table

| COTT | Torus (T^3) | Physics |
|------|-------------|---------|
| null | Empty space, no excitations | Vacuum state |
| 0 | Zero mode (constant function on torus) | Ground state (NOT zero energy) |
| w | Fundamental cycle (full winding) | Integration operator, Poincare dual |
| 0 * w = 1 | Pairing zero-form with 3-form | Poincare duality |
| -0 | Antiperiodic zero mode | Antiperiodic boundary condition |
| 0^2 | Zero mode in 2D subspace | Bivector / 2-form (grade 2) |
| 0^3 | Zero mode in 3D (volume) | Trivector / volume form (grade 3) |
| 0^4 breaks | No 4-form on T^3 | Dimension of manifold = 3 |

### Exterior Algebra = COTT Powers

    0^0 = 1       scalar         (grade 0, 0-form)
    0^1 = 0       vector         (grade 1, 1-form)
    0^2           bivector       (grade 2, 2-form)
    0^3           trivector      (grade 3, 3-form / volume form)
    0^4           BREAKS         (no 4-form on a 3-manifold)

The grade where powers break IS the dimension of the underlying space.

### Boundary Conditions = Signs of Zero

| Type | COTT | Shift Vector | Z(-1/2) | c_3 | Energy |
|------|------|--------------|---------|-----|--------|
| PPP (all periodic) | 0 (bosonic) | (0,0,0) | -0.2666 | -0.01128 | Attractive |
| APP (1 antiperiodic) | mixed | (0.5,0,0) | -0.0111 | -0.00047 | Attractive, 24x smaller |
| AAP (2 antiperiodic) | mixed | (0.5,0.5,0) | +0.034 | +0.00144 | REPULSIVE |
| AAA (all antiperiodic) | -0 (fermionic) | (0.5,0.5,0.5) | +0.0623 | +0.00264 | REPULSIVE |

**Dark energy in four symbols:**

    84 * (-0) - 28 * (0) = net positive vacuum energy

Fermions (-0, antiperiodic) beat bosons (0, periodic). The surplus is dark energy.

---

## SYSTEM 5: THE CORRECTION FORMULA

*Source: Ash, Nine, Jeff Korth (pi as "the door")*

### The Ratio

    R = Z_APP(-1/2) / Z_PPP(-1/2) = (1/24) * [1 + epsilon]

### The Correction

    epsilon = c_1 * q * beta * (1 - q)

where:

    q     = e^{-2*pi}         = 1.8674 * 10^{-3}    (nome at self-dual point tau = i)
    beta  = 1 - 1/sqrt(2)     = 0.2929               (BC gap at self-dual point)
    (1-q) = 0.9981             (first eta factor)
    c_1   = 1.0000193...       (forced by isometry)

### The Four Ingredients of 1/24

1. **24** = modular anomaly of Dedekind eta: eta(tau) = q^{1/24} * prod(1 - q^n)
2. **0** = void-zero pole exclusion (the Sigma' convention excluding n = 0)
3. **pi** = transcendental door: q = e^{-2*pi*tau}, connects discrete to continuous
4. **sqrt(2)** = self-dual signature: [theta_2(i) / theta_3(i)]^2 = 1/sqrt(2)

### Three Vanishing Conditions (forcing the form)

    epsilon -> 0  as  q -> 0          (lattice degenerates)
    epsilon -> 0  as  BC_APP -> BC_PPP (boundary conditions match)
    epsilon -> 0  as  (1-q) -> 0       (eta product collapses)

These three conditions uniquely force: epsilon = q * (1 - 1/sqrt(2)) * (1 - q)

### Why c_1 = 1 (The Isometry Argument)

The Mellin integral splits at t = 1:

    integral_0^inf = integral_0^1 (top tree, UV) + integral_1^inf (bottom tree, IR)

Jacobi's imaginary transformation:

    theta_3(i/t) = t^{1/2} * theta_3(it)
    theta_2(i/t) = t^{1/2} * theta_4(it)

At t = 1: theta_2(i) = theta_4(i). The two halves are identical at the junction.

The map t -> 1/t is an isometry of the Poincare half-plane. It reflects without distortion.
Therefore the O(q) correction from both halves must be equal. No rescaling at the junction.

**c_1 = 1 because a mirror reflecting a mirror does not distort.**

### Why c_2 != Clean

At O(q^2), theta_2 and theta_4 diverge (half-integer shifts vs alternating signs).
Self-similarity breaks at second order. The mirror has its first flaw.

### Dimension Uniqueness

    d = 1:  ratio = -1/2   (exact, trivial)
    d = 2:  ratio = 0.145  (14.7% from any simple fraction)
    d = 3:  ratio = 0.0417 (0.055% from 1/24)  <-- UNIQUELY CLOSE
    d = 4:  ratio = 0.0165 (3.2% from 1/60)
    d = 5:  ratio = 0.007  (no nearby fraction)

d = 3 is the unique dimension where the ratio nearly hits a simple fraction.

---

## SYSTEM 6: THE GOLDEN RATIO IDENTITIES

### Definitions

    phi = (1 + sqrt(5)) / 2 = 1.618...
    psi = (1 - sqrt(5)) / 2 = -0.618...

Both satisfy: x^2 - x - 1 = 0

### Vieta's Formulas (connecting to COTT)

    phi + psi = 1 = 0 * w        <- the COTT axiom
    phi * psi = -1 = 0^w = e^{ipi}  <- the lightlike operator

### Self-reciprocal Property

    1/phi = phi - 1 = psi + 1 = 0.618...
    phi^2 = phi + 1
    phi^n = phi^{n-1} + phi^{n-2}    (Fibonacci recurrence in phi)

### Fibonacci Connection

    F(n) = (phi^n - psi^n) / sqrt(5)     (Binet's formula)
    F(n)/F(n-1) -> phi   as n -> infinity

---

## SYSTEM 7: KOIDE FORMULA

*Source: Yoshio Koide (1981), connected to torus by Ash*

### The Formula

    Q = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2

### The Numbers

    m_e   = 0.5110 MeV     sqrt(m_e)   = 0.7148
    m_mu  = 105.7 MeV      sqrt(m_mu)  = 10.2790
    m_tau = 1776.9 MeV      sqrt(m_tau) = 42.1528

    Q = 1883.0294 / 2824.5701 = 0.6666605...
    2/3 = 0.6666667...

    Match: 0.000004% (four parts per million)

### Geometric Interpretation

    Q = 1/(3*cos^2(theta))

    Q = 2/3  <=>  theta = pi/4 (exactly 45 degrees)

The vector (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)) makes angle pi/4 with (1,1,1).

- theta = 0: all masses equal (no information, gimbal lock)
- theta = pi/4: maximum information density (nature's choice)
- theta = pi/2: one mass dominates (gimbal lock, collapse)

### Torus Connection

Three generations = three cycles of T^3.
Masses = eigenvalues of the torus Laplacian.
Mass ratios determine torus shape:

    L_1/L_2 = m_mu/m_e = 206.77
    L_1/L_3 = m_tau/m_e = 3477.2
    m_geo = (m_e * m_mu * m_tau)^{1/3} = 45.78 MeV

---

## SYSTEM 8: THE S-TRANSFORMATION

### Modular Group Generator

    tau -> -1/tau

Swaps the two cycles of the torus. Exchanges hole with body.

### Theta Function Transformation

    theta_3(-1/tau) = sqrt(-i*tau) * theta_3(tau)

### The Identification

    0 * w = 1  IS  the S-transformation of the vacuum

Zero and omega are the two faces of the same torus, related by the fundamental symmetry of the structure.

### Self-Dual Point

    tau = i (equivalently tau = 1 for shape)

At the self-dual point:
- theta_2(i) = theta_4(i)
- [theta_2(i) / theta_3(i)]^2 = 1/sqrt(2)
- The torus equals its own dual
- The S-transformation is its own inverse

---

## SYSTEM 9: EULER'S IDENTITY (REINTERPRETED)

    e^{i*pi} + 1 = 0

In COTT:

    0^w + 1 = 0

Meaning: the lightlike limit plus the identity equals the zero mode.
Or: differentiation at full power plus identity equals ground state.

The five constants (e, i, pi, 1, 0) converge at the meeting point of dual perspectives — not absorption, but rotation.

---

## THE OPEN RULES (Not Yet Proven)

1. Does (-0)^3 = +0^3 or -0^3? (determines sign-flip behavior for dark energy)
2. Full associativity proof for COTT multiplication
3. Full distributivity proof for COTT over addition
4. Closed-form expression for c_2 at O(q^2)
5. Formal derivation of Koide's Q = 2/3 from torus eigenvalues
6. Proof that 0^4 breaks specifically because d = 3
7. The critical exponent gamma = 6.7 from theta function structure
