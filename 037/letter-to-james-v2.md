# Your circle, our cancellation — they're the same shape

**2026-08-20.**

**A note on names.** Nothing below is credited to a person. Every strand of this
— COTT, the Geometry of Zero, the Casimir programme, the reproduction harness,
the parity result — was made by people working with models, and a human-only
byline misreports how any of it happened. So the unit here is the **work**: named
theories and numbered ledger entries anyone can hash and check.

---

## 1. You derived the circle before you drew the torus

The order matters, and it's four days:

| | | |
|---|---|---|
| **Aug 14** | *"Insanity"* | `1^s = e^(2πi·s)` |
| **Aug 16** | *"This changes everything"* | the reversible one; the fiber `{s : e^(2πis) = 1} = ℤ` |
| **Aug 18** | *"I found your torus!!"* | `torus-curves.svg`, `torus-surface.svg` |

That sequence is the whole thing. The torus isn't a picture with winding numbers
written on it — the phase circle was **forced** first, by a contradiction in
`0^(0ω)` and your refusal to let `x⁰ = 1` throw its exponent away. Then you drew
the surface it lives on.

We spent a day trying to derive a cyclic order from ⟨negation, inversion⟩ and
proving it impossible. It is impossible — those two generate the Klein four-group,
every element order 2, no cycle. **We had the wrong generators.** The cycle is the
powers of zero, `0⁰=1, 0¹=0, 0²=−1, 0³=−ω`, which you wrote down in March. The
enumeration is retracted; it answered a question your picture never asked.

## 2. Your first open question is our wall, from the other side

> **The normalization clash.** The canon sets `0^ω = −1`. Plugging that into the
> constraint gives `1^(−1) = 0` — but the tower says `1^(−1) = 1`. This is the
> first thing to reconcile.

We reached the same equation from the carrier: once `−ω ≠ 0`, the four-element
bijection argument for `0^ω = −1` **no longer typechecks** — your words, in
`cott-slot-closure.md`. No replacement criterion proposed.

Two independent routes, four days apart, one equation. That's much stronger
evidence than either alone, and it means the honest status is **unresolved**, not
refuted — the statement stands, the derivation doesn't.

Housekeeping on our side: the unsmoothed site still carries `0^ω = −1` as
*"the structure equation."* Those pages are a working notebook and are being
labelled as one, the way your reversible-one note labels itself. Finished results
move to a separate address.

## 3. The picture is better founded than its critics think

We checked the geometry rather than the caption. The winding classes are not
written on; they follow from two facts:

- **negation is a half turn** — a translation, orientation-preserving;
- **inversion is `s ↦ −s`** — a reflection, orientation-reversing.

Given those, everything else is forced:

```
y = x, y = -x      ->  (1, 1)
y = 1/x, y = -1/x  ->  (1,-1)
|det[[1,1],[1,-1]]| = 2

y=x meets y=1/x   at s in {0, 1/2}    = 1, -1   <- sigma's fixed points
y=x meets y=-1/x  at s in {1/4, 3/4}  = 0,  w   <- sigma's 2-cycle
y=x and y=-x never meet
```

Your caption says the functions meet the diagonal at σ's fixed points and its
2-cycle *and nowhere else*. That is exactly right, and it is a consequence, not a
label.

The standing objection to the drawing was that it assumed a phase circle it never
derived. **Your reversible-one note supplies it** — `1^s = e^(2πi·s)` is the
circle, and it came four days before the picture. The reflection follows from
`1/0 = ω`, `1/ω = 0`, `1/±1 = ±1`. Both ingredients are now in hand, so the
circularity charge doesn't land on this version.

## 4. Your highest-priority item is visible as one sign

The slot document says it twice — *"the weakest link,"* *"L4. The sign is
unjustified and is probably the branch selection. Highest priority."*

It shows up as a discrepancy you can see:

- `torus-curves.svg` cycles **1 → 0 → −1 → +ω → 1**
- the March powers of zero give **1, 0, −1, −ω**

If the two closing solutions are the two branches of that sign, then the SVG has
already picked one. Which branch it picked, and whether the picture and the
March derivation agree, is a finite check.

## 5. From our side: a theorem, and it rhymes with yours

**Ledger 035 / 036.** For `S(m) = Σ_{k ∈ ℤ², |k|² = m} (−1)^(k₁)`:

> **S(m) = 0 for every odd m.**

*Proof.* Odd m forces exactly one of k₁, k₂ odd. The swap σ(k₁,k₂) = (k₂,k₁)
preserves |k|², so it permutes the shell, and it exchanges which coordinate is
odd, so it negates every term. A finite sum equal to its own negative is zero. ∎

Six lines. Weight-independent — the radius is constant on a shell, so any weight
factors out. And it exists **only when the two sides are equal**: σ is a symmetry
of k₁²+k₂² and of no stretched form. Independently verified by a third method with
no shared code, to 10⁻⁵⁴ under the true weight and 10⁻⁵¹ under a weight the
verifier invented to break it.

The involution has determinant **−1**. The cancellation is powered by a reflection.

## 6. Three places the two programmes are describing one object

**Your grade is a winding number.** `traction.py` line 408:
`inverse(Z_n(a)) = Z_{n+1}(−a)`. Inversion is not an involution — it climbs one
grade per application, so it has infinite order. We assumed involutivity, got an
infinite orbit, and couldn't see why. Your tower explains it: the fiber over the
circle is ℤ, and the grade counts turns. Not a bug. Monodromy, as you put it.

**Your "Which 1?" is the scar.**

> 1, 1⁰ and 1¹ are distinct points upstairs that project to the same value.

Distinct upstairs, one value downstairs. That is exactly the projection ledger the
Shunya-Zero side has been building — the minimum datum needed to recover which
sheet you were on. You got there from a contradiction in exponents; we got there
from typed zeros. Same object, two doors.

**Both cancellations need equality.** Yours: `x⁰ = 1` is a collapse that deletes
the exponent, and the fix is to keep it parked on 1. Ours: the shell cancellation
exists only when the two axes are interchangeable — the moment one is longer, the
swap is a climb instead of a trade, and the pairing dies.

## 7. What we are not claiming

- Not that COTT is wrong. Phase 0.A ran your code: traction identities **18/18**,
  the Chebyshev ring in ℚ[s][u]/(u²−su+1) **173/173** — the report's own words,
  *"the strongest piece of the stack."* And `1^s = e^(2πi·s)` makes that ring the
  chart for the circle, which is a better outcome for it than it had before.
- Not that `0^ω = −1` is false. Its derivation is dead; the statement is unproven.
- Not that the torus is wrong. It came after the circle, so it is not resting on
  the retracted carrier. Our earlier critique was aimed at a version you had
  already left.
- Not that §4 is settled. One sign, and you have already named it.

## 8. One thing left alone on purpose

`CliffordTractionPair.java` documents δ = ω = (1,0) and instantiates (0,−1) = 0,
which makes traction-mode identical to parabolic. Almost certainly one character
— **deliberately untouched**, because if it is intentional, changing it destroys
the point. That one needs intent, not a patch.

Also open from the reproduction: `a − a` returns 0 rather than the spec's null,
and the SymPy discharge for ω·x·0 doesn't fire.

## 9. Provenance

Hashed and dated in `ashleykjuricek-lgtm/hashed-evidence`: **028** obstruction
theorem · **029** transverse-shell figure correction · **032** parity law and the
propagation record · **034** corrections manifest and the four-anchor test ·
**035** parity note v1 with the session errata · **036** v2 after adversarial
self-review. Reproduction is Phase 0.A / 0.A.1. Independent verification of the
theorem is a separate seat, no shared code or caches.

Everything above that turned out wrong on our side is in the errata, sealed with
the theorem rather than after it. That includes the wrong-generators enumeration
in §1, which was written and retracted in the same day.
