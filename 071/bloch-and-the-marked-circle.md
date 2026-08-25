# The Bloch sphere and the marked circle — and three errors in one computation

**2026-08-25.** Ash: *"how does this relate to a bloch sphere?"*

**The connection is exact, not analogical: our marked circle and the spinor's minus
sign are the same ℤ₂.** But the Bloch sphere itself carries no marking, and the
place that does is a curved quotient where 061's theorem still holds. Computed.

**This entry also contains three failed versions of one computation**, all this
seat's, in the same failure family. §4.

---

## 1. The structural answer

```
   Bloch sphere = CP^1 = S^2      pure states of one qubit      pi_1 = 0   NO marking
   total space  = S^3            unit vectors in C^2            pi_1 = 0   NO marking
   Hopf fibration  S^3 -> S^2, fibre S^1
   SU(2) -> SO(3)  is a DOUBLE COVER,  SO(3) = RP^3 = S^3 / Z_2
                                                      pi_1(SO(3)) = Z_2   TWO markings
```

**That ℤ₂ is the spinor sign.** Rotate a spin-½ by 2π and the state comes back as
`−|ψ⟩`; only 4π returns it. The loop in `SO(3)` is not contractible, and it lifts in
`SU(2)` to a path from `I` to `−I`.

**Our marked circle is a homomorphism `π₁(M) → ℤ₂`. The spinor sign is the
non-trivial element of `π₁(SO(3)) = ℤ₂`. Same group, same role.**

And the physics link is standard, not ours: **fermions are antiperiodic around the
Euclidean time circle.** The marking *is* the fermionic boundary condition, and
fermions are exactly the objects carrying that minus sign.

**So the Bloch sphere is not the object — its double cover is.** `S²` and `S³` are
simply connected and admit nothing to mark, exactly as 061 §1 found. `ℝP³ = SO(3)`
admits exactly two markings, and they are *periodic* and *spinor*.

This also answers 061's other half concretely: **the Hopf fibration `S³ → S²` with
`S¹` fibres is literally "a sphere with a torus-like structure."** It still has no
marking. The marking appears only after the ℤ₂ quotient.

## 2. Computed — the two spin structures on SO(3)

On `S³` (unit radius) the Laplacian has eigenvalue `n(n+2)` with degeneracy
`(n+1)²`. The antipodal map acts on degree-`n` harmonics by `(−1)^n`, so on `ℝP³`:

```
   untwisted (periodic)      n EVEN
   twisted   (antiperiodic)  n ODD
```

**061 proved `Z_A − Z_P` is finite on any `M × S¹` because `θ_P − θ_A` is
exponentially small. `ℝP³` is a quotient, not a product — and the difference is
still tame:**

```
      t        Theta_P        Theta_A       Theta_P - Theta_A
     0.5      1.164994357   0.9013708945     0.2636234627
     0.2      3.026140166     3.02488345     0.001256716382
     0.1      7.743091625    7.743091596     2.881152692e-8
    0.05      20.83265717    20.83265717     3.01375522e-18
```

Each grows like `t^(−3/2)`; the difference is O(1) and then vanishes. **The poles
cancel in a quotient as well as in a product — a genuine extension of 061's scope.**

```
   Z_twisted - Z_untwisted  on RP^3 = SO(3)  =  0.704149355948

   lam-independence:  lam = 0.7, 1.0, 1.6, 2.5  ->  all 0.70414935594848
                      spread 1.292e-26   INVARIANT
```

For comparison:

```
   T^3 (flat)   Z_APP - Z_PPP = 0.255482035923
   S^1 x S^2    Z_A   - Z_P   = 0.2503281026      (061)
   RP^3         Z_tw  - Z_un  = 0.704149355948    (this entry)
```

The first two are close; `ℝP³` is roughly 2.8× larger. **NOT ESTABLISHED** that any
of that means anything.

**Very probably known.** Casimir energy on `ℝP³` is a standard example in QFT on
curved space. **Not searched.** Anyone citing this number should look first.

## 3. What is NOT claimed

- **Nothing here says `R` computes anything about qubits.** `R` does not exist on
  `ℝP³` at all — the space is curved, so by 061 §2 there is a pole at `s = −1/2` and
  `Z_A`, `Z_P` each diverge. **Only the difference exists.**
- The Bloch sphere is not the torus and is not a limit of it.
- That the marking and the spinor sign are the same ℤ₂ is a statement about
  `Hom(π₁, ℤ₂)`. It does **not** make the cubic-torus programme a statement about
  spin systems.

## 4. Three failures in one computation, all this seat's

`Z_twisted − Z_untwisted` was computed three times before it was right.

| version | what it did | result | how it was caught |
|---|---|---|---|
| **v1** | cut the small-`t` piece at `t = 1e-4` and integrated `t^(−3/2)·1` **numerically** instead of continuing it analytically | `−55.7288` | the cut contributed ≈ 186 — the "answer" was the cutoff |
| **v2** | continued that piece correctly, but integrated the **difference** down to `t = 0`, where `ThA` and `ThP` are each `~t^(−3/2)`, truncated at `NMAX`, and their difference is cancellation garbage | `−1.61e19` | **λ-dependent** — 0.7/1.0/1.6/2.5 gave four different answers |
| **v3** | measured the integrand before cutting (`9.5e-11` at `t=0.07`, `2.7e-16` at `t=0.05`), cut at 0.05 | `0.704149355948` | λ-invariant to `1.3e-26` |

**All three discarded rather than patched.**

### 4.1 The λ-invariance test earned its keep

`λ` is a parameter of the *split*, not of the object. 047 §2.1 built that check to
validate the real-dimension continuation. **Today it caught v2 in one line** — four
split points, four different answers, so the computation is wrong regardless of
which one looks plausible.

**A test built three days ago caught an error today.** That is the only thing in
this entry worth generalising.

### 4.2 A named hazard — the small-`t` end of a Mellin integral

Three failures in this ledger now share one address:

```
   061 section 5    truncated theta does not have exponential smallness  ->  4297.79
   071 v1           cut instead of continued                            ->  -55.73
   071 v2           cancellation of two large truncated sums            ->  -1.6e19
```

> **The small-`t` end of a Mellin integral is where this programme's numerical
> errors live.** Three ingredients recur: an integrand that is *analytically*
> exponentially small but *numerically* garbage; a `t^(s−1)` prefactor that is huge
> there; and a piece that must be **continued**, not integrated.
>
> **Rule: measure the integrand before cutting, print the number you cut at, and
> check λ-invariance before reporting anything.**

## 5. 070 confirmed by a second seat

The Figma seat independently re-derived 070 — brute-force representation by both
forms against the congruences: **0/0 mismatches on 430 primes, bins 99/113/109/109,
and the crossover primes (11, 19, 31 dark-in-square/lit-in-golden; 13, 17, 37 the
reverse) all confirmed. CONFIRMED.**

Two seats, own code. 070 stands.

## 6. Status

| claim | status |
|---|---|
| `π₁(S²) = π₁(S³) = 0`, so the Bloch sphere admits no marking | **CLASSICAL** |
| `π₁(SO(3)) = ℤ₂`, and that ℤ₂ is the spinor sign | **CLASSICAL** |
| our marking and the spinor sign are the same ℤ₂ | **ESTABLISHED** — both are `Hom(π₁, ℤ₂)` |
| fermions are antiperiodic round the thermal circle | **STANDARD PHYSICS**, not ours |
| the difference stays finite on a **quotient**, not just a product | **COMPUTED** — extends 061 §3 |
| `Z_tw − Z_un` on `ℝP³` `= 0.704149355948` | **COMPUTED**, λ-invariant to `1.3e-26` |
| that number is new | **NO / UNKNOWN** — `ℝP³` Casimir is standard; not searched |
| its ratio to the `T³` and `S¹×S²` values means something | **NOT ESTABLISHED** |
| `R` exists on `ℝP³` | **NO** — curved, pole at `s = −1/2` (061 §2) |
| this makes the programme about qubits | **NO** |
| 070's two-field split | **CONFIRMED by a second seat**, 0/0 on 430 primes |

## Attribution

The question is Ash's. The `π₁` chain and the `ℝP³` computation are this seat's; so
are all three failures in §4. The λ-invariance test that caught v2 is from 047. The
independent confirmation of 070 is the Figma seat's.
