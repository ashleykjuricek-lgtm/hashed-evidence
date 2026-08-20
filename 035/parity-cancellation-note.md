# An exact parity cancellation on the square dual lattice, and its failure off the cube

**Ash Korth, Claude (Opus 5).** Independent verification: Claude (Fable seat), 2026-08-20.
Written to be attacked. Every claim below is either proved, computed with its
method stated, or explicitly marked as not established.

---

## 1. Statement

For m ∈ ℕ let

    S(m)  =  Σ_{k ∈ ℤ², |k|² = m}  (−1)^(k₁)

be the antiperiodic character sum over the shell of squared radius m in the
square lattice ℤ².

> **Theorem 1.** S(m) = 0 for every odd m.

> **Theorem 2 (weight-independence).** For any function w : ℝ₊ → ℝ,
>
>     Σ_{m odd} w(√m) · S(m) = 0.
>
> In particular the vanishing does not depend on the radial weight, so it is not
> an artefact of any particular tail approximation.

> **Proposition 3 (failure off the square).** Replace the radius by
> d_b(k) = √(k₁² + k₂²/b²). For b ≠ 1 the odd-shell sum
> Σ_{m odd} Σ_{|k|²=m} (−1)^(k₁) w(d_b(k)) is not identically zero, and near
> b = 1 it vanishes to first order only.

---

## 2. Proof of Theorem 1

Squares are ≡ 0 or 1 (mod 4). Hence a sum of two squares is ≡ 0, 1, or 2 (mod 4),
and an **odd** value forces exactly one of k₁, k₂ odd. (Consequently every odd
representable m satisfies m ≡ 1 mod 4; m ≡ 3 mod 4 is not representable.)

Let σ(k₁, k₂) = (k₂, k₁). Then

- σ preserves |k|², so σ maps the shell |k|² = m onto itself, bijectively;
- σ is an involution, σ² = id;
- on an odd shell, exactly one coordinate is odd, so σ exchanges the parity of the
  first coordinate: (−1)^(σk)₁ = −(−1)^(k₁).

Therefore

    S(m) = Σ_k (−1)^(k₁) = Σ_k (−1)^(σk)₁ = − Σ_k (−1)^(k₁) = −S(m),

the middle equality because σ permutes the (finite) shell. Hence 2S(m) = 0, so
S(m) = 0. ∎

**Remark.** σ has matrix [[0,1],[1,0]], determinant −1: the involution is
orientation-reversing. The cancellation is powered by a reflection.

## 3. Proof of Theorem 2

On the square lattice every k with |k|² = m has the same radius √m, so w(√m) is
constant on each shell and factors out:

    Σ_{m odd} w(√m) S(m) = Σ_{m odd} w(√m) · 0 = 0.  ∎

This is the content of the weight-independence: the radial profile never enters,
because the cancellation happens **within** each shell, not across shells.

## 4. Why Proposition 3 holds

σ is a symmetry of the quadratic form k₁² + k₂² and of no anisotropic form
k₁² + k₂²/b² with b ≠ 1. Off the square, σ moves points off their level sets, the
weight no longer factors out of a shell, and the two terms that previously cancelled
are evaluated at different radii. Generically the residue is nonzero and, being a
smooth function vanishing at b = 1, it crosses zero transversally there.

**Corollary.** A steep transversal zero crossing at a symmetric point is what an
exact cancellation *looks like from the side*. It is evidence of protection, not
against it. Any argument of the form "the quantity varies steeply, therefore its
smallness is accidental" is invalid when the smallness belongs to a sub-family
that vanishes identically at the symmetric point.

---

## 5. Verification record

Two independent implementations, no shared code and no shared caches.

**(a) This session.** `hashed-evidence/032/parity_register.py`, SHA-256
`b5a239aa9357872194ec28f37d250213e7caa5d33c1f1976fac09d1913aa95d4`, sealed
2026-08-16.

- Theorem 1: no violation for odd m < 4000.
- Companion identity S(2m) = (−1)^m r₂(m): no violation for m < 2000.
- Theorem 2 tested against six unrelated weights, including a pure power law
  d^(−7), exp(−d), log(1+d)/d⁵, and the constant weight 1: all give machine zero.
- Proposition 3: nonzero at b = 1 ± 0.001 for every weight tested.

*The split reported in 032 §3 uses a proxy radial weight and is labelled
`[PROXY]` in the source. It demonstrates structure; it is not a decomposition of ε
and its rows are not expected to sum to ε(1).*

**(b) Independent, Fable seat, 2026-08-20.** Third method, no shared code.

- Theorem exact on **1306** odd shells ≤ 10⁴. *(Shell count re-derived here:
  odd m ≤ 10⁴ representable as a sum of two squares = 1306. Agrees.)*
- D_odd(1) ≈ −2 × 10⁻⁵⁴ using the **true Bessel weight**;
  ≈ −1.2 × 10⁻⁵¹ using a weight the verifier invented for the purpose.
- Nonzero with sign change at b = 1 ± 0.001.

---

## 6. What this does **not** establish

Stated so that no reader has to discover it by attack.

1. **It does not prove anything about ε.** Whether the parity zero propagates
   through the true Bessel weights and the smooth sector into ε = 24R − 1 is
   **open**. 028's shell table is consistent with it — the d = 1 shell cancels in
   the numerator, the d = √2 shell survives — but the link is not closed. Filed as
   `CAS-DODD-EPSILON-LINK`, open / measured only.
2. **It does not resurrect any closed form.** ε = q(1−1/√2)(1−q) remains refuted
   (026–028, interval-certified). The genuine e^(−2π) coefficient of ε is −5.709.
3. **It does not, by itself, explain the proximity of R to 1/24.** That is the
   zero-mode subtraction present in PPP and absent in APP — a separate mechanism,
   whose *existence* is convention-free but whose *share* is not.
4. **It is a statement about ℤ², not ℤ³.** The analogous 3D character sum does not
   vanish on odd shells (T(1) = +2, T(3) = −8). The cancellation is specific to the
   transverse plane of the Poisson-split decomposition.
5. **The percentages in 032 §3 are proxy numbers** and are not certified.

## 7. Attribution

The theorem and its proof are joint work of Ash Korth and Claude (Opus 5),
2026-08-16. The line of attack — that a cancellation of this kind should live at
the symmetric point and die away from it, because a swap between two things is
only available when neither is privileged — is Ash's, and it is what selected
parity as the thing to test before any computation was run. Independent
verification by Claude (Fable seat) working with Adam Lisowski, 2026-08-20.
Prior art properly located: the 2D transverse framing is **029**; the obstruction
theorem is **028 §4**; the half-period hinge framing is Ash's July note in **032**.
