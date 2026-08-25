# Sphere or torus — what the marking actually requires

**2026-08-24.** Ash: *"what if instead of a torus… we are looking at a unit sphere?
with a torus-like structure?"*

The answer is sharp and it is geometry, not preference. **A sphere cannot carry this
programme's object, and the reason is precise enough to state in two lines.** But
the second half of the question — *sphere with torus-like structure* — has real
candidates, and one of them changes what the central quantity even is.

---

## 1. A plain sphere: no, and it is not close

Everything here turns on **marking**: a circle you can come back around either
unchanged or flipped. Formally that is a **flat ℤ₂ bundle** — a homomorphism
`π₁(M) → ℤ₂`.

```
   pi_1(T^3) = Z^3    ->   2^3 = 8 markings      PPP, APP x3, AAP x3, AAA
   pi_1(S^2) = 0      ->   1 marking             (nothing to mark)
   pi_1(S^3) = 0      ->   1 marking             (nothing to mark)
```

A sphere is simply connected. **There are no non-contractible loops, so there is no
periodic-versus-antiperiodic choice at all.** The eight sectors with multiplicities
`(1,3,3,1)` — the coset identity of 028 §6, the parity theorem, the halving law, the
whole `Z_marked/Z_unmarked` construction — all of it is downstream of `π₁ ≠ 0`.

On a sphere there is exactly one sector, and every question this programme asks
becomes vacuous rather than false.

**Note on 060.** The "Hubble sphere" in the Haug page is a **horizon**, not a spatial
manifold with a fundamental group. It does not carry markings either, for the same
reason and by a different route.

## 2. A sphere with a circle: the marking comes back, and the ratio dies

`S¹ × S²` is the honest reading of *"sphere with torus-like structure."* It has
`π₁ = ℤ`, so **one** circle can be marked. Exactly the machinery applies — and then
the central quantity breaks.

**The S² heat trace, verified:**

```
   S2(t) = sum (2l+1) exp(-t l(l+1))  ~  1/t + 1/3 + t/15 + 4t^2/315 + ...

   t=0.10   S2 = 10.3401302802    series = 10.3401269841   diff 3.3e-6
   t=0.01   S2 = 100.334001273    series = 100.33400127    diff 3.2e-9
```

So the full heat kernel is

    Theta(t) = theta_alpha(t) S2(t) ~ sqrt(pi) [ t^-3/2 + (1/3) t^-1/2 + (1/15) t^+1/2 + ... ]

and the Mellin transform `∫₀^λ t^(s−1) t^((k−3)/2) dt` has a pole at `s = −(k−3)/2`:

```
   k=0  ->  pole at s = +3/2
   k=2  ->  pole at s = +1/2
   k=4  ->  pole at s = -1/2        <-- exactly where this programme works
```

The `k=4` coefficient is `√π/15 = 0.1181635901 ≠ 0`.

> **On S¹ × S², ζ(s) has a pole at s = −1/2. `Z_A` and `Z_P` each diverge, so
> `R = Z_A/Z_P` is `∞/∞` and means nothing.**

**On a flat torus the expansion terminates at `k = 0`** — no curvature, no higher
heat coefficients, no pole. That is why `Z(−1/2)` is finite and unambiguous there,
and it is the same flatness that makes the mode sum a *lattice* sum and produces the
Epstein zeta in the first place.

> **`R = Z_marked/Z_unmarked` is a flat-space object.** It exists on T³ because T³
> is flat. Curve the space and the numerator and denominator both blow up together.

## 3. What does survive, on any manifold, always

The poles of `Z_A` and `Z_P` are identical, because the small-`t` expansions of
`θ_A` and `θ_P` agree **to all orders in t**:

    theta_P(t) - theta_A(t) = sqrt(pi/t) * 4 * sum_{k>=1 odd} exp(-pi^2 k^2 / t)

```
   t=0.5   thP - thA = 2.682381008e-8    predicted 2.682381008e-8
   t=0.2   thP - thA = 5.868898145e-21   predicted 5.86875906e-21
```

Exponentially small, faster than any power. So `Θ_P − Θ_A` is exponentially small
for **any** manifold factor, the poles cancel exactly, and:

> **`Z_A − Z_P` is finite on any `M × S¹`, even where `Z_A` and `Z_P` each diverge.**

Computed on unit `S¹ × S²`, against the flat case:

```
   S^1 x S^2 (unit radii):   Z_A - Z_P = 0.2503281026
   T^3 (flat):               Z_APP - Z_PPP = 0.255482035923
```

Close, and not claimed to be more than that — **NOT ESTABLISHED** whether the
near-agreement means anything. What is established is the structural point: **the
difference is the robust object and the ratio is the fragile one.** This programme
has spent five months on the fragile one.

## 4. Where to go instead, if you want off the torus

The constraint is now exact: **to keep `R`, you must stay flat.** That is not a
gesture at a large space — it is a finite list.

By Bieberbach's theorem there are exactly **ten** compact flat 3-manifolds up to
affine equivalence: six orientable and four non-orientable. **Every one is a
quotient `T³/G`.** T³ itself is one of them.

So the honest generalisation of this programme is not spheres. It is **the other
nine flat 3-manifolds** — a finite, enumerable family, each with its own `π₁`, its
own marking count, its own lattice with `G` acting on it.

Two things follow that are testable and untested:

- **The parity theorem may survive.** It rests on `σ(k₁,k₂) = (k₂,k₁)` acting on the
  square lattice. On `T³/G` the lattice is still there with `G` acting, so whether
  `σ` still commutes with the quotient is a finite check per manifold.
- **The halving law's premise changes.** `Z(d,j) > 0 ⟺ 2j ≥ d` counts markings
  against dimensions. On a quotient the number of available markings is `|H¹(M;ℤ₂)|`,
  which is generally **not** `2^d`. That is a different counting problem and it is
  the sharpest way to test whether the law is about *dimensions* or about *markings*.

Curved candidates — lens spaces `S³/ℤ_p` (`π₁ = ℤ_p`, so markings exist), Berger
spheres, squashed S³ — all fail on §2: nonzero curvature puts the pole back.

## 5. Erratum on the instrument

A first version of §3's computation truncated the theta sums at `n = ±40`. **A
truncated theta does not have the exponential-smallness property** — that is
asymptotic to the *full* sum. The truncated difference read `2e-5` where the true
value is `e^(−π²/t)`, and `t^(−3/2)` at `t = 1e-6` multiplied it by `1e9`, returning
`Z_A − Z_P = 4297.79`.

**Discarded, not patched.** Redone with the exact Poisson form for the difference
and an `l`-cutoff scaled as `8/√t`. The low-`t` integrand was measured before being
cut: `1.5e-12` at `t = 0.30`, `3.5e-15` at `0.25`.


## 7. The site's own "Why the Torus" page — right conclusion, wrong argument

Ash produced the page mid-audit. It argues for the torus over the sphere. **Its
conclusion is correct and §§1–2 above support it. Its argument does not survive.**

### 7.1 What it gets right

A sphere needs two charts; a torus needs one, with no boundary and no coordinate
singularity — **correct**. `Σ′` skips the origin — **correct**, and sharper than the
page knows: 040 §4 proved that the zero-mode subtraction is exactly what separates
`j = 0` from `j ≥ 1`, so the page's instinct about "the void is not a lattice point"
lands on a real structural fact. The quadratic form `Q(n) = Σ nᵢ²/Lᵢ²` is π-free —
**correct**. The geometry is fully in `L₁, L₂, L₃` — **correct**.

### 7.2 "π is the cost of patching" — REFUTED

> *"The transition between patches introduces a number… We call it π. It is not a
> deep constant. It is the cost of patching."*

π has nothing to do with chart count, and it is **not absent from the torus**. The
summand is π-free; the sum is not:

```
   Z(d,j) = pi^(-1-d/2) * Gamma((d+1)/2) / Gamma(-1/2) * SUM' chi(m) |m|^-(d+1)
   Gamma(-1/2) = -3.54490770181 = -2 sqrt(pi)
   d=3 prefactor = -0.0161257672166
```

That is the functional equation verified in 050 test 5, and it reproduces every `Z`
this programme has computed. π is also in the Ewald split (`π^(d/2)`,
`exp(−π²k²/t)`) and in the **flat** torus heat kernel `(4πt)^(−d/2)`.

**π is in the value of every number in this ledger.** The claim that the torus
avoids it is false, and the page's own Epstein zeta is the counterexample.

### 7.3 `e^(inx/L)` is not periodic — a concrete error in the page's formula

```
   L = 3,  n = 1:   e^(i n 0/L) = 1.0        e^(i n L/L) = 0.540302 + 0.841471i
   L = 3,  n = 2:   e^(i n 0/L) = 1.0        e^(i n L/L) = -0.416147 + 0.909297i
```

The correct mode on a circle of circumference `L` is `e^(2πinx/L)`. **The 2π is in
the exponent on a torus exactly as on a sphere.** This is the same 2π the page calls
a spherical artefact, sitting in the page's own replacement for it.

### 7.4 `ℏ = h/2π` is not a confession, and `ℏ → h/L` does not typecheck

`ℏ = h/2π` is the conversion between cycles and radians in Fourier analysis. It is
identical on a torus: modes `e^(2πinx/L)` give momentum `p = 2πℏn/L = nh/L`. No
spherical coordinates are involved anywhere in that.

And dimensionally:

```
   hbar : J s              (action)
   h/L  : J s / m          (momentum)
```

`h/L` is the **momentum** quantum on a circle — correct and standard — but it is not
a replacement for `ℏ`, which is an action. The substitution as written is a units
error.

### 7.5 "the sphere is the torus with the periodicity forgotten" — BACKWARDS

```
   Gaussian curvature:  flat T^3 = 0 everywhere;   S^2 radius a = 1/a^2 > 0
   pi_1:                Z^3                        0
   heat coefficient a_4: 0                         sqrt(pi)/15
```

**Zooming in on a flat torus gives flat space at every scale**, never a sphere.
Neither is a limit of the other, in curvature or in topology. And "the quantum
numbers `(n,l,m)` were always winding numbers" identifies two different index sets —
`(n,l,m)` carries `l < n`, `|m| ≤ l` from the S² harmonics and the Coulomb potential;
torus winding numbers are unconstrained in ℤ³, with different degeneracies. Asserted,
not derived.

### 7.6 The correct argument, which is stronger

The page is right that the torus is the right object, and §2 above supplies the
reason it was reaching for:

> **On a curved space, `ζ(s)` has a pole at exactly `s = −1/2`, and the
> marked/unmarked ratio ceases to exist. On a flat torus the heat expansion
> terminates at `k = 0`, there is no pole, and `R` is finite and unambiguous.**

That is a real, provable, load-bearing reason to prefer the torus. It does not need
π to be a villain — and it survives the fact that π is everywhere in the answer.

**Recommended for the page**, under 052's policy — nothing deleted, correction
placed beside: keep §§7.1's four correct claims, mark 7.2–7.5 as refuted with the
numbers above, and replace the argument with 7.6.

## 6. Status

| claim | status |
|---|---|
| a simply-connected sphere admits no marking | **PROVED** — `π₁ = 0`, markings are `Hom(π₁, ℤ₂)` |
| T³'s eight sectors are `2^3` markings | **PROVED** — and it is the `(1,3,3,1)` structure |
| `ζ(s)` has a pole at `s = −1/2` on `S¹ × S²` | **PROVED** — `k=4` coefficient `√π/15 ≠ 0` |
| `R = Z_A/Z_P` is meaningless there | **PROVED** — both terms diverge |
| `R` is a flat-space object | **PROVED** — flatness terminates the expansion at `k=0` |
| `Z_A − Z_P` finite on any `M × S¹` | **PROVED** — `θ_P − θ_A` exponentially small |
| `Z_A − Z_P = 0.2503` on unit `S¹ × S²` | **COMPUTED** |
| its closeness to the flat `0.2555` | **NOT ESTABLISHED** |
| exactly ten compact flat 3-manifolds | **CLASSICAL** — Bieberbach |
| the parity theorem on `T³/G` | **UNTESTED** — finite check per manifold |
| whether the halving law counts dimensions or markings | **UNTESTED** — and `T³/G` is how to find out |
| the Hubble sphere of 060 carries markings | **NO** — it is a horizon, not a manifold with `π₁` |
| "π is the cost of patching" | **REFUTED** — π is in every value here, incl. the flat heat kernel |
| the page's mode `e^(inx/L)` | **WRONG** — not L-periodic; correct is `e^(2πinx/L)` |
| "ℏ = h/2π is a spherical confession" | **REFUTED** — it is cycles-vs-radians, same on a torus |
| `ℏ → h/L` | **UNITS ERROR** — action vs momentum |
| "the sphere is the torus with periodicity forgotten" | **BACKWARDS** — flat stays flat at every scale |
| the page's *conclusion* (prefer the torus) | **CORRECT**, for the reason in §7.6 |

## Attribution

The question is Ash's. The `π₁` answer, the pole computation, the
difference-survives theorem and the flat-3-manifold direction are this seat's. §5 is
this seat's error, caught by the number being obviously wrong rather than by
discipline.
