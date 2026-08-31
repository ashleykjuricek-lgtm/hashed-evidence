# 097 — The shift↔character functional equation, exactly — and it does NOT prove what 096 offered

**2026-08-31.** Follows 096, and sharpens its §3 (the OFFERED chart-invariance
argument) — downward. Writing the equation exactly is what 096 said would
promote the argument from OFFERED to proved. It does the opposite: it shows
the argument, as stated, does not go through, and it replaces the hand-wave
with the true exact statement. That is a better outcome than a confirmation,
and it is recorded as one.

---

## 1. The master theta identity (proved, one Poisson computation)

For a diagonal form Q_A(x) = Σᵢ aᵢxᵢ², shift vector α, character vector β,
define

    Θ[α; β](t; A)  =  Σ_{n∈ℤᵈ}  e^{2πi n·β}  e^{−t·Q_A(n+α)}

Poisson summation applied to g(x) = e^{2πi x·β} e^{−t Q_A(x)}
(Gaussian Fourier transform, computed coordinate-wise) gives, exactly:

    Θ[α; β](t; A)  =  e^{−2πi α·β} · (π/t)^{d/2} (det A)^{−1/2} · Θ[−β; α](π²/t; A⁻¹)

**Shift and character trade places** (α moves from shift slot to character
slot; β moves from character slot to shift slot, negated), **the lattice
dualizes** (A → A⁻¹), and **the heat parameter inverts** (t → π²/t, fixed
point t = π). This is sealed 032's sentence — "shift ↔ character, the two
sides of Poisson summation" — as a formula.

*Proof.* Σₙ g(n+α) = Σₖ e^{2πi k·α} ĝ(k) with
ĝ(k) = Πᵢ (π/(t aᵢ))^{1/2} e^{−π²(kᵢ−βᵢ)²/(t aᵢ)}; pull out
e^{−2πi α·β} to convert the left side to Θ[α;β]; recognize the right side
as Θ[−β;α] at π²/t on A⁻¹. Each step is a convergent-Gaussian identity. ∎

## 2. The completed zeta equation (our case: d = 3, APP on the 1×b×b torus)

Take A_b = diag(1, 1/b², 1/b²)  (side lengths (1, b, b)), so
det A_b = b⁻⁴, A_b⁻¹ = diag(1, b², b²) — **the dual lattice of the b-torus
is the (1, 1/b, 1/b)-torus.** Take α = (½,0,0), β = 0 (the APP shift; note
e^{2πi k·α} = (−1)^{k₁}).

Define the shift (APP) and character sums:

    Z_sh(s; b)  =  Σ_{n∈ℤ³} [ (n₁+½)² + (n₂²+n₃²)/b² ]^{−s}
    Z_ch(w; c)  =  Σ'_{k∈ℤ³} (−1)^{k₁} [ k₁² + (k₂²+k₃²)/c² ]^{−w}

Splitting the Mellin integral at the fixed point t = π and transforming the
lower half with §1 yields the **exact, all-s identity** (each integral
entire in s; this IS the analytic continuation):

    Γ(s) Z_sh(s; b)  =  ∫_π^∞ t^{s−1} Θ_sh(t; b) dt
                      + b² π^{2s−3/2} ∫_π^∞ u^{1/2−s} [ Θ_ch(u; 1/b) − 1 ] du
                      + b² π^{s} / (s − 3/2)

with Θ_sh(t;b) = Σₙ e^{−t[(n₁+½)² + (n₂²+n₃²)/b²]} and
Θ_ch(u;1/b) = Σₖ (−1)^{k₁} e^{−u[k₁² + b²(k₂²+k₃²)]}.

Equivalently, in completed form: **Λ_sh(s; b) = b² · Λ_ch(3/2 − s; 1/b)**
up to the stated pole term — the involution acts on the *triple*
(representation, argument, modulus):

    ( shift,  s,  b )   ⟷   ( character,  3/2 − s,  1/b )

Numerical verification: `verify_functional_equation.py` in this folder
evaluates the right-hand side directly (theta sums + quadrature) and
compares against the independent Ewald implementation of sealed
032/epstein_aniso_check.py — two routes, no shared code path — at
s = −1/2 for several b. Agreement to the working precision is printed in
`verify_output.txt`.

## 3. What this does to 096's OFFERED argument — the honest part

096 offered: *"a physical potential cannot depend on chart choice; the odd
part of ε flips under chart swap; therefore V = even part."* Written
exactly, the equation shows:

1. **The b ↔ 1/b involution is real but it never acts at fixed
   (representation, s).** It maps the shift sum at (s, b) to the character
   sum at (3/2−s, 1/b). At our fixed physical point — shift representation,
   s = −1/2 — there is **no exact symmetry** relating ε(b) to ε(1/b).
   The equation connects ε(b) at s = −1/2 to a *different* object
   (character-weighted, s = 2, modulus 1/b).
2. **053's chart identification is a relabeling statement** — the two
   teams' parameters name the same family — and a relabeling cannot force
   a function on the family to be even about a point. The 096 argument
   conflated relabeling invariance (tautological) with involution
   invariance (false at fixed s).
3. Therefore: **the measured near-oddness of ε about the cube (odd slope
   −18.3259645 dominating a 5.5×10⁻⁴ even part) is an APPROXIMATE
   phenomenon, currently unexplained** — genuinely interesting, possibly a
   shadow of the exact doubled-space involution, but not a consequence of
   any identity written down so far.
4. The measured well V(x) = ε₀ + 0.58260865 x² − 3.184 x⁴ **stands as a
   measurement** (096's computed rows are untouched). What died is its
   *derivation story*: "V = even part" is now a **definition awaiting a
   physical selection principle**, not a forced consequence. 096's OFFERED
   row is superseded by this entry: status **OPEN, sharpened** — the exact
   equation is now in hand, and the open question is precise: *is there a
   physical involution on the shape family at fixed s = −1/2, or does the
   drain coordinate live on the doubled space where the true involution
   acts?*

## 4. Status

| claim | status |
|---|---|
| master theta identity (§1), general (α, β, A) | **PROVED** — one Poisson computation, classical |
| completed equation (§2) for APP on 1×b×b, all s | **PROVED** given §1 (contour/split standard); **VERIFIED** numerically, two independent routes |
| the involution acts only on (rep, s, modulus) triples | **PROVED** — read off §2 |
| 096's chart-invariance argument forces V = even part | **DEAD** — §3; conflated relabeling with involution |
| the near-oddness of ε about the cube | **MEASURED (096), UNEXPLAINED** — open |
| V as measured in 096 | **STANDS** — measurement unaffected; its derivation is open |
| a physical selection principle for V | **OPEN** — the sharpened question, stated in §3.4 |

Stratum: §1–2 are exact identities (COUNT-adjacent: no regularization
choices; the continuation is the identity). §3 is the corrected framing.

## Attribution

The demand to "write the shift↔character functional equation exactly" is
Ash's, and it is what killed the hand-wave — the pattern of 089 again: the
author of the argument (this seat, in 096) could not see its flaw until
forced to formalize; formalization is a non-author. The Poisson mechanism
is classical (Epstein 1903; Terras); 032 named it for this project. The
derivation, the verification script, and the retraction of 096 §3's
argument (this seat's own, one entry old) are this seat's.
