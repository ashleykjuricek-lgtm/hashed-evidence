# An exact parity cancellation on the square dual lattice, and its failure off the cube

### v2 — supersedes 035/`parity-cancellation-note.md`

**Ash Korth, Claude (Opus 5).** Independent verification: Claude (Fable seat), 2026-08-20.
Written to be attacked. Every claim below is either proved, computed with its
method stated, or explicitly marked as not established.

**Changes from v1**, all found by attacking our own paper before sending it out —
see §8 for the full diff and why each mattered. Theorem 1 is unchanged.

---

## 1. Statement

For m ∈ ℕ let

    S(m)  =  Σ_{k ∈ ℤ², |k|² = m}  (−1)^(k₁)

be the antiperiodic character sum over the shell of squared radius m in the
square lattice ℤ².

> **Theorem 1.** S(m) = 0 for every odd m.

> **Theorem 2a (finite form).** Let F ⊂ ℤ² be any finite set closed under
> σ(k₁,k₂) = (k₂,k₁). Then for every w : ℝ₊ → ℝ,
>
>     Σ_{k ∈ F, |k|² odd}  (−1)^(k₁) w(|k|)  =  0.

> **Theorem 2b (infinite form).** If Σ_{k ∈ ℤ²} |w(|k|)| < ∞, then
>
>     Σ_{k ∈ ℤ², |k|² odd}  (−1)^(k₁) w(|k|)  =  0,
>
> the sum being independent of summation order.

> **Observation 3 (failure off the square).** Replace the radius by
> d_b(k) = √(k₁² + k₂²/b²). For b ≠ 1 the odd-shell sum
> Σ (−1)^(k₁) w(d_b(k)) is nonzero for every weight tested, and near b = 1 it
> vanishes to first order only. *Argued in §4 and measured in §5; not proved.*

**Why 2a and 2b are separate.** Stated as "for any w" the claim is either a
restatement of Theorem 1 (each shell term is w·0) or false, since for w ≡ 1 the
lattice series is not absolutely convergent and reorganising it into shells is
unjustified. 2a is what the numerics actually test; 2b covers every weight of
interest — the Bessel tail, exponentials, and power laws d^(−p) with p > 2 are all
absolutely convergent. Nothing of substance is lost and the loophole closes.

---

## 2. Proof of Theorem 1

Squares are ≡ 0 or 1 (mod 4). Hence a sum of two squares is ≡ 0, 1, or 2 (mod 4),
and an **odd** value forces exactly one of k₁, k₂ odd. (Consequently every odd
representable m satisfies m ≡ 1 mod 4; m ≡ 3 mod 4 is not representable.)

Let σ(k₁,k₂) = (k₂,k₁). Since σ preserves |k|², it maps the shell {|k|² = m} onto
itself bijectively. Write the shell sum two ways.

*Reindexing.* Because σ is a bijection of the shell,

    Σ_k (−1)^((σk)₁)  =  Σ_j (−1)^(j₁)  =  S(m).

*Evaluating.* By definition (σk)₁ = k₂, and on an odd shell exactly one coordinate
is odd, so (−1)^(k₂) = −(−1)^(k₁). Hence

    Σ_k (−1)^((σk)₁)  =  Σ_k (−1)^(k₂)  =  − Σ_k (−1)^(k₁)  =  −S(m).

The same sum equals both S(m) and −S(m), so 2S(m) = 0 and S(m) = 0. ∎

**Remark.** σ has matrix [[0,1],[1,0]], determinant −1: the involution is
orientation-reversing. The cancellation is powered by a reflection.

## 3. Proofs of Theorems 2a and 2b

**2a.** F is finite, so the sum may be grouped by shell without any convergence
question. Every k ∈ F with |k|² = m carries the same radius √m, so w(|k|) = w(√m)
is constant within each group and factors out:

    Σ_{k ∈ F, m odd} (−1)^(k₁) w(√m)  =  Σ_{m odd} w(√m) · Σ_{k ∈ F, |k|²=m} (−1)^(k₁).

Closure of F under σ means each inner sum is itself a σ-invariant shell sum, so
the argument of §2 applies verbatim to it and it vanishes. ∎

**2b.** Absolute convergence permits arbitrary rearrangement, in particular
grouping by shell; each grouped term is w(√m)·S(m) = 0 by Theorem 1. ∎

This is the content of weight-independence: the radial profile never enters,
because the cancellation happens **within** each shell, not across shells.

## 4. Why Observation 3 holds

σ is a symmetry of the quadratic form k₁² + k₂², and of no anisotropic form
k₁² + k₂²/b² with b ≠ 1. Off the square, σ moves points off their level sets, w no
longer factors out of a shell, and the two terms that previously cancelled are
evaluated at different radii. The residue is then nonzero for every weight we
tested; being a smooth function of b that vanishes at b = 1, it crosses zero there,
transversally in every case measured.

*Genericity is not proved.* We verify nonvanishing for the weights in §5 and do
not claim it for all w.

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
- Theorem 2a tested against six unrelated weights — including a pure power law
  d^(−7), exp(−d), log(1+d)/d⁵, and the constant weight 1 — on σ-symmetric
  truncations: all give machine zero. *(The w ≡ 1 case is admissible under 2a and
  not under 2b; it is reported as a truncation result, which is what it is.)*
- Observation 3: nonzero at b = 1 ± 0.001 for every weight tested.

*The split reported in 032 §3 uses a proxy radial weight and is labelled
`[PROXY]` in the source. It demonstrates structure; it is not a decomposition of ε
and its rows are not expected to sum to ε(1).*

**(b) Independent, Fable seat, 2026-08-20.** Third method, no shared code.

- Theorem exact on **1306** odd shells ≤ 10⁴. *(Shell count re-derived here:
  odd m ≤ 10⁴ representable as a sum of two squares = 1306. Agrees.)*
- D_odd(1) ≈ −2 × 10⁻⁵⁴ using the **true Bessel weight**;
  ≈ −1.2 × 10⁻⁵¹ using a weight the verifier invented for the purpose.
  Both weights satisfy the hypothesis of 2b.
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
5. **Observation 3 is not a theorem.** Genericity of the nonvanishing off the
   square is unproved.
6. **The percentages in 032 §3 are proxy numbers** and are not certified.

## 7. Attribution

The theorem and its proof are joint work of Ash Korth and Claude (Opus 5),
2026-08-16. The line of attack — that a cancellation of this kind should live at
the symmetric point and die away from it, because a swap between two things is
only available when neither is privileged — is Ash's, and it is what selected
parity as the thing to test before any computation was run. Independent
verification by Claude (Fable seat) working with Adam Lisowski, 2026-08-20.
Prior art properly located: the 2D transverse framing is **029**; the obstruction
theorem is **028 §4**; the half-period hinge framing is Ash's July note in **032**.

## 8. Diff from v1 (035), and why each change was needed

Found by adversarial review of our own paper, 2026-08-20, before circulation.

| v1 | v2 | why |
|---|---|---|
| "Theorem 2. For **any** function w…" | split into **2a** (finite σ-symmetric truncation) and **2b** (absolutely convergent) | as written it was trivial under one reading and false under the other: for w ≡ 1 the lattice series does not converge absolutely, so reorganising by shell was unjustified. The numerics tested the finite case; the statement claimed the infinite one. |
| "**Proposition** 3" | "**Observation** 3", marked *not proved* | "Proposition" promises a proof. §4 gives a heuristic and §5 gives numbers for specific weights. Labelling slippage of exactly the kind this project catches in others. |
| "**Generically** the residue is nonzero" | "nonzero for every weight tested; genericity not proved" | genericity was asserted, not shown. |
| §2 reindexing compressed | split into explicit *reindexing* and *evaluating* steps | the two steps that produce S(m) = −S(m) were run together; separated so the bijection and the sign flip are each visible. |
| — | §6 item 5 added | the new limitation is stated in the limitations section, not only in the diff. |

**Theorem 1 is unchanged**, as is the Corollary in §4. Those were the two
load-bearing results and neither required amendment.

v1 remains sealed in 035 exactly as circulated. It is not corrected in place.
