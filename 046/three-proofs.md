# Three proofs — closing what was closable

**2026-08-22.** Follows 045. Ash: *"let's prove what we can."*

Three items that had been sitting as *verified but not proved* or as *pending*.
All three are now proved. Each proof is short, each is checked exhaustively rather
than sampled, and §4 says plainly what could **not** be proved and why.

Notation as in 035/036/038: for `k ∈ ℤ²`,

    S(m)  = sum over |k|^2 = m  of  (-1)^(k1)        with S(0) := 1
    T(m)  = the same over k in Z^3
    T2(m) = sum over |k|^2 = m  of  (-1)^(k1) * k2^2
    r2(m) = number of representations of m as a sum of two squares

---

## 1. The full character law — S(m) for **every** m

Theorem 1 (035/036) gave `S(m) = 0` for odd m and said nothing about even m. The
even case was listed as pending. It is three lines.

> **Theorem A.**  `S(m) = 0` for m odd, and `S(m) = (−1)^(m/2) · r₂(m)` for m even.

*Proof.* Squares are ≡ 0 or 1 (mod 4).

- **m odd.** Exactly one of `k₁², k₂²` is odd, so exactly one of `k₁, k₂` is odd.
  The swap `σ(k₁,k₂) = (k₂,k₁)` preserves `|k|²`, so it permutes the shell, and it
  exchanges which coordinate is odd, so it negates every term. A finite sum equal
  to its own negative is zero. *(This is Theorem 1, restated.)*
- **m ≡ 0 (mod 4).** Two residues from {0,1} summing to 0 mod 4 forces both to be
  0, so **both coordinates are even**, so `(−1)^(k₁) = +1` at every point and
  `S(m) = r₂(m)`. And `m/2` is even, so `(−1)^(m/2) = +1`. ✓
- **m ≡ 2 (mod 4).** Both residues must be 1, so **both coordinates are odd**, so
  `(−1)^(k₁) = −1` at every point and `S(m) = −r₂(m)`. And `m/2` is odd, so
  `(−1)^(m/2) = −1`. ✓  ∎

**Checked:** all 1171 representable `m ≤ 4000`. **0 violations.**

The character sum is now known in closed form on the whole of ℤ. Nothing about it
is open.

## 2. Theorem 4 proved in general

038 §"Theorem 4" recorded `T(m) = 2·Σ_{k₃ ≥ 1 odd} S(m − k₃²)` for odd m as
*"verified with no exceptions for all odd m < 300"* and noted the slice argument
was a proof sketch that **should be finished**. Finishing it:

> **Theorem B.**  For every odd m,  `T(m) = 2 · Σ_{k₃ ≥ 1, k₃ odd} S(m − k₃²)`.

*Proof.* Condition on the third coordinate:

    T(m) = sum over k3 in Z, k3^2 <= m  of  sum over k1^2+k2^2 = m-k3^2 of (-1)^(k1)
         = sum over k3  of  S(m - k3^2)

Let m be odd.

- `k₃` **even** ⟹ `m − k₃²` is odd ⟹ `S(m − k₃²) = 0` by Theorem A. This includes
  `k₃ = 0`, so the central slice contributes nothing.
- `k₃` **odd** ⟹ `m − k₃²` is even ⟹ the slice survives.

`k₃` and `−k₃` give identical terms, so the surviving slices pair off. ∎

**Checked:** all 500 odd `m < 1000`. **0 violations.** Status moves from
**VERIFIED (m < 300)** to **PROVED**.

The reading in 038 stands and is now on firm ground: `T(1) = 2` is `2·S(0)`, the
single surviving slice at `k₃ = ±1`; `T(3) = −8` is `2·S(2)`, the **√2 shell** —
the same survivor that forces `e^(−2π√2)` into ε and refutes the closed form.

## 3. An exact formula for T₂, and a sharp criterion replacing a brute search

`T₂(m) ≠ 0` was **verified to 4000, not proved** (038). It is still not proved.
But the search can be replaced by an identity.

> **Theorem C.**  For odd m, with `E = { k : |k|² = m, k₁ even }`,
>
>     T2(m) = m * r2(m)/2  -  2 * sum over E of k1^2
>
> and therefore  **T₂(m) = 0  ⟺  the mean of `k₁²` over E equals `m/2`.**

*Proof.* For odd m exactly one coordinate is odd, so the shell splits into
`E` (k₁ even, k₂ odd) and `O` (k₁ odd, k₂ even), and `σ(k₁,k₂) = (k₂,k₁)` is a
bijection `E → O`; hence `|E| = |O| = r₂(m)/2`.

    T2(m) = sum_E k2^2  -  sum_O k2^2

For `(a,b) ∈ E`, `σ(a,b) = (b,a) ∈ O` has second coordinate `a`, so
`Σ_O k₂² = Σ_{(a,b)∈E} a²`. Therefore

    T2(m) = sum_E (b^2 - a^2)

and on the shell `a² + b² = m`, so `b² − a² = m − 2a²`, giving

    T2(m) = m*|E| - 2*sum_E a^2 = m*r2(m)/2 - 2*sum_E a^2.   ∎

**Checked:** all 552 odd representable `m ≤ 4000`. **0 violations.**
`T₂(1) = 2`, `T₂(5) = −12`, `T₂(25) = 22`, `T₂(325) = 220` — matching 038's values.

**Corollary (the arithmetic form).** For odd m, `r₂(m) = 4(d₁(m) − d₃(m))`, so

    T2(m)/2 = m*(d1(m) - d3(m))  -  sum over E of k1^2

**What this changes.** "T₂ never vanishes" was a claim resting on 552 checks. It is
now the claim that **the even coordinate's mean square never equals exactly half
the radius²** on an odd shell — a statement about second moments of
representations, which is the kind of thing that can be attacked. It is still open.
No zero was found below 4000.

## 4. What could NOT be proved, and why

Stated plainly rather than left to look like an oversight.

- **The sign law `Z(d,j) > 0 ⟺ 2j ≥ d`** (040 §3, 152 cells, no exception).
  **Not proved, and not seriously attempted tonight.** The three theorems above are
  finite combinatorial statements about lattice shells; the sign law is an analytic
  statement about the ratio `θ_A(t)/θ_P(t)` raised to a real power and integrated
  against `t^(s−1)`. It needs a different toolkit — a monotonicity or convexity
  argument in that ratio — and guessing at one at this hour would produce something
  that looks like a proof and isn't. **Open, and the most valuable thing on the
  list.**
- **Uniqueness of the real-dimension continuation** (042 §2). Untouched. Would need
  a Carlson-type growth argument.
- **`R(d,d/2) → −2^(−(d+1)/2)`** (040 §2). Numerically compelling to d = 40; no
  proof attempted.
- **`T₂(m) ≠ 0`.** Reduced, not closed. See §3.
- **The lobe width** (045): 8° of 36° for the decagon, 28° of 45° for the octagon.
  No account of either.

## 5. Status changes

| item | was | now |
|---|---|---|
| `S(m)` for even m | **PENDING** since 035 | **PROVED** — Theorem A |
| Theorem 4 (3D slicing) | **VERIFIED m < 300** | **PROVED** — Theorem B |
| `T₂(m)` closed form | did not exist | **PROVED** — Theorem C |
| `T₂(m) ≠ 0` | verified to 4000 | **REDUCED** to a second-moment criterion; still open |
| sign law `2j ≥ d` | verified, 152 cells | **still open**, and named as the priority |

## Attribution

Cubic-torus / Shunya-Zero programme. Theorem A completes a result whose odd half
was proved in 035/036 from a reading that was Ash's. Theorem B finishes a sketch
038 flagged as unfinished. Theorem C is new. All of it is human-and-model work and
no single name belongs on the front of it.
