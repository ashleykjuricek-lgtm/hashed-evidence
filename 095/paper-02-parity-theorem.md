# The parity theorem, whole

**Drafted 2026-08-30, Ash + Claude (Fable seat), from sealed entries 035, 036,
046, 084, 085.** This is the paper's centerpiece result written out in full:
the statement, the proof, the generalisation, the scope, the prediction record,
and — because this is the one result in the programme that has never once been
walked back — the reason why.

---

## 1. The picture first

Take the grid of whole-number points in the plane. Draw rings around the
origin: each ring collects every grid point at one exact squared distance `m`.
Now count the points on a ring with signs — each point counts +1 if its first
coordinate is even, −1 if odd.

**On every odd ring, the signed count is exactly zero.**

The reason is one move. On an odd ring, every point has exactly one odd
coordinate — because squares leave remainder 0 or 1 when divided by 4, and an
odd total forces exactly one of the two. Swap a point's coordinates and you
land on another point of the *same* ring — but the odd coordinate has changed
seats, so the sign flips. Every +1 point has a −1 twin, its mirror across the
diagonal. The ring pairs off completely, one for one, and a sum equal to its
own negative can only be zero.

The whole theorem comes down to a fact a child can check: a whole number and
its square are always both even or both odd.

## 2. The theorem, formally (sealed 036)

For `m ∈ ℕ` let `S(m) = Σ_{k ∈ ℤ², |k|² = m} (−1)^(k₁)` — the signed count on
the shell of squared radius `m`.

> **Theorem 1.** `S(m) = 0` for every odd `m`.

*Proof.* Squares are ≡ 0 or 1 (mod 4), so an odd `m` forces exactly one of
`k₁, k₂` odd. Let `σ(k₁,k₂) = (k₂,k₁)`. Since `σ` preserves `|k|²` it maps the
shell onto itself bijectively. Write the sum `Σ_k (−1)^((σk)₁)` two ways:

- *Reindexing:* `σ` is a bijection of the shell, so the sum equals `S(m)`.
- *Evaluating:* `(σk)₁ = k₂`, and on an odd shell exactly one coordinate is
  odd, so `(−1)^(k₂) = −(−1)^(k₁)` at every point; the sum equals `−S(m)`.

The same sum equals both `S(m)` and `−S(m)`, so `2S(m) = 0`. ∎

*Remark.* `σ` has determinant −1: it is orientation-reversing. **The
cancellation is powered by a reflection.**

## 3. Weight independence — why the smoothing can never touch it

Nearly every other number in this programme is built by summing infinitely many
ring contributions against a fading weight and taking a limit. That
limit-taking is the smoothing, and its conventions — which weight, which order,
which continuation — are where every one of the corpus's eleven errors-in-one-
night lived (052 §3). This theorem never enters that layer:

> **Theorem 2a (finite form).** For any finite set `F ⊂ ℤ²` closed under the
> swap `σ`, and *any* weight `w` whatsoever:
> `Σ_{k ∈ F, |k|² odd} (−1)^(k₁) w(|k|) = 0`.

> **Theorem 2b (infinite form).** If `Σ_{k ∈ ℤ²} |w(|k|)| < ∞`, then the full
> odd-shell weighted sum is zero, independent of summation order.

*Proof of 2a.* `F` is finite, so grouping by shell needs no convergence
argument; within a shell `w` is constant and factors out, leaving `w(√m) ·
(shell sum)`, and each shell sum vanishes by the argument of §2. ∎
*Proof of 2b.* Absolute convergence permits regrouping by shell; each grouped
term is `w(√m) · S(m) = 0`. ∎

**This is the content of weight-independence: the radial profile never enters,
because the cancellation happens *within* each shell, not across shells.** Each
ring hands you a zero — a finite count of whole numbers, closed before any
weight touches it — and zero times any weight is zero. Run it through any
smoothing, any convention, any limit: you are summing zeros.

*A scar, kept visible:* v1 (sealed 035) stated Theorem 2 as "for any function
`w`" in the infinite case — which is trivial under one reading and **false**
under the other, since for `w ≡ 1` the lattice series does not converge
absolutely and regrouping by shell is unjustified. The split into 2a/2b (v2,
sealed 036) was found by attacking our own paper before circulation. v1 stays
sealed, uncorrected in place.

## 4. The failure off the square — the theorem's edge, honestly

Deform the distance: `d_b(k) = √(k₁² + k₂²/b²)`. For `b ≠ 1` the swap `σ` is no
longer a symmetry of the form, points move off their level sets, the weight no
longer factors out, and the two terms that cancelled are evaluated at different
radii. The odd-shell sum is then **nonzero for every weight tested**, crossing
zero transversally at `b = 1`. *(Observation, sealed 036 §4–5 — measured, not
proved; genericity is not claimed.)*

The corollary is a lesson about instruments: **a steep transversal zero
crossing at a symmetric point is what an exact cancellation looks like from the
side.** It is evidence of protection, not against it. The line of attack that
selected parity as the thing to test before any computation ran is Ash's: *a
swap between two things is only available when neither is privileged.*

## 5. The fixed point — what the theorem actually is (sealed 084)

Generalise: `d` circles, `j` of them marked; `X(d,j)(m)` the signed count with
`j` of `d` coordinates marked; the operation is `Q(n) = n₁² + ⋯ + n_d²` and
nothing else — Ash's rule: *no π, no √2, no φ, no logarithms, no named
constants at all.*

> **Law 1 (marking-complement duality).** `X(d,j)(m) = (−1)^m · X(d,d−j)(m)`.

*Proof, one line.* For any integer `n`, `n ≡ n²` (mod 2), so on any solution
`(−1)^(n₁+⋯+n_d) = (−1)^m`; split the exponent between the marked set and its
complement. ∎ *(Verified `d ≤ 6`, `m ≤ 20,000`, 0 exceptions.)*

> **Law 2 (the parity theorem as fixed point).** If `j = d − j`, Law 1 reads
> `X = (−1)^m X`, so on odd `m`: `X(d, d/2)(m) = 0`.

**When a marking is its own complement, it must equal minus itself, so it
vanishes.** Theorem 1 is exactly the case `d = 2, j = 1`.

And this yields the theorem's exact scope, which the programme did not have
before 084:

- Self-dual markings exist **only when `d` is even** — only there can a marking
  be half of the whole.
- **Predicted before checking:** `d = 4` and `d = 6` have the vanishing. Both
  confirmed, 0 exceptions / 10,000 each.
- **Predicted absent:** `d = 1, 3, 5` admit no self-dual marking. None found.
- **The 3-torus — this programme's home object — has no parity theorem.** Not
  because it fails there: because the self-dual slot does not exist. Three is
  the awkward dimension, and every direction examined has said so independently
  (083, 084, 085 §3).

A theorem plus a successful prediction is the best thing in the corpus (092).

## 6. What the fixed point does on the shells it does not kill (sealed 085)

On even shells the self-dual marking does not vanish — it **reproduces the
entire lattice at half the shell number, sign alternating**:

> `X(d, d/2)(2k) = (−1)^k · r_d(k)`, for every even `d`.

*Proof by convolution:* marking is per-coordinate, so `X(d, d/2)` is the
two-dimensional marked object convolved `d/2` times with itself; apply the
`d = 2` case (§2 plus the character law, 046) and collect signs. No theta
function, no continuation. This is the Jacobi duplication identity that 039 and
046 reached through `θ₃θ₄ = θ₄(q²)²`, stated in integers for all even
dimensions at once. **Marking half the circles is not a new object. It is the
same object, seen at half scale.** The odd shells vanish because a half-scale
copy has nothing to stand on there.

## 7. Why this is the one result never walked back

The ledger's errors stratify perfectly (052 §3): every retraction-class error
in the corpus sits in the smoothed layer, where finite values are assigned to
divergent objects by regularisation and convention. The exact count-stratum
results have needed no errata — ever. This theorem is the extreme point of that
stratification: it is *provably* indifferent to the smoothed layer (§3), so
there is no convention through which an error could enter it. It is not a
measurement of a regularised object; it is a statement that survives every
regularisation available.

**The things that do not need the smoothing are the things that do not need
correcting** — and this theorem is that sentence's proof by example. Stratum
tag, per 082: everything in §§2, 5, 6 is COUNT — finite, exact, no limit taken
anywhere.

## 8. What this theorem does not establish

Stated so no reader has to discover it by attack (from 036 §6, updated):

1. It proves nothing about ε, the physical quantity — whether the parity zero
   propagates through the true weights into ε is **open**
   (`CAS-DODD-EPSILON-LINK`).
2. It resurrects no closed form; the March closure remains refuted (026–028).
3. It does not by itself explain the proximity of R to 1/24.
4. The three-dimensional analogue does **not** vanish (`T(1) = +2, T(3) = −8`);
   3D odd shells reduce to 2D by slicing (046 Thm B) but carry no cancellation
   of their own.
5. Whether the sign law's boundary `2j = d` and the self-dual condition are one
   fact seen twice is observed and **open** (084).
6. Laws 1–2 are elementary and near-certainly classical in substance; what is
   claimed as this programme's own is the framing, the scope result, and the
   prediction record (084's own status table).

## Attribution

The theorem and its proof are joint work of **Ash Korth and Claude (Opus 5)**,
sealed 2026-08-16, hardened to v2 by adversarial self-review 2026-08-20 (036).
The line of attack that selected parity before any computation ran — *a swap is
only available when neither of two things is privileged* — is Ash's.
Independent verification: Claude (Fable seat) working with Adam Lisowski,
2026-08-20, third method, no shared code. The fixed-point framing and the scope
result are 084's seat, working under Ash's integers-only rule, which is the
whole method of that entry; the half-scale identity is 085's, produced by Ash's
instruction *"do d=4 and see what the mirror does there."* The character law
completing the even shells is 046's. Jacobi's duplication identity is the
literature's.
