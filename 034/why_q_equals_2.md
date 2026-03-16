# Why q = 2: The Fixed Point Where Arithmetic Is Self-Consistent

**Date**: 2026-03-16
**Authors**: The Prismic Collaboration (see [ATTRIBUTION.md](../ATTRIBUTION.md))
**Primary contributors this file**: Ash (Ashley Juricek), Nine (Claude Code, Opus 4.6)
**Builds on**: Folders 032 (Casimir ratios), 022 (coefficient proof), 008 (Geometry of Zero), 033 (Borel resurgence)

---

## 1. THE OBSERVATION

Every calculation in this repository — every theta function, every lattice sum, every Casimir ratio, every plot — uses the Euclidean norm. The L^2 norm. The sum-of-squares-then-square-root.

    |n|_2 = (n_1^2 + n_2^2 + n_3^2)^{1/2}

We chose this without thinking. Physics chose it without thinking. It's "the" norm. But the general L^q norm is:

    |n|_q = (|n_1|^q + |n_2|^q + |n_3|^q)^{1/q}

Why q = 2? Why not q = 3, or q = 1, or q = 1.7?

The standard answer: "Euclidean geometry." "Pythagorean theorem." "It's the one that works."

The deeper answer: **2 is the unique number where addition, multiplication, and exponentiation agree.**

---

## 2. THE 2-FIXED-POINT

Consider three operations applied to a number a with itself:

    Addition:        a + a = 2a
    Multiplication:  a × a = a^2
    Exponentiation:  a^a

For these three to give the same result:

    2a = a^2 = a^a

From 2a = a^2:  a^2 - 2a = 0,  so a(a-2) = 0.  Therefore a = 2 (excluding 0).

Check: 2 + 2 = 4.  2 × 2 = 4.  2^2 = 4.

**2 is the unique positive number where a + a = a × a = a^a.**

This is not numerology. This is a fixed point of the map between arithmetic operations. At a = 2, the three fundamental binary operations collapse into one. You can add, multiply, or exponentiate — you get the same answer.

---

## 3. WHY THIS MATTERS FOR THE CASIMIR CALCULATION

The Epstein zeta function on T^3 is:

    Z(s; alpha) = sum'_{n in Z^3} |n + alpha|^{-2s}

where |n + alpha| is the Euclidean norm. The calculation requires three things to interoperate:

### 3.1 Addition (summing modes)

The sum over n in Z^3 is additive. Each lattice point contributes independently. The total is a sum.

### 3.2 Multiplication (the Mellin transform)

The Mellin integral representation:

    Z(s) = pi^s / Gamma(s) * integral_0^infty t^{s-1} Theta(t) dt

This is a multiplicative transform — the kernel t^{s-1} scales multiplicatively. The theta function Theta(t) = sum exp(-pi t |n|^2) factorizes as a product over dimensions precisely because the norm is quadratic:

    exp(-pi t |n|_2^2) = exp(-pi t n_1^2) * exp(-pi t n_2^2) * exp(-pi t n_3^2)

This factorization — addition in the exponent becoming multiplication of exponentials — is what makes the theta function a product of one-dimensional theta functions. **This only works for q = 2.** For q != 2:

    exp(-pi t |n|_q^q) != product of 1D factors

The entire Jacobi inversion machinery (Section 2 of folder 032) depends on this factorization.

### 3.3 Exponentiation (the nome and modular structure)

The nome q = e^{-2*pi} appears as the fundamental small parameter. The correction formula:

    R = (1/24) * [1 + q(1 - 1/sqrt(2))(1 - q) + O(q^2)]

is an expansion in powers of q. The modular transformation tau -> -1/tau, which forces c_1 = 1 (folder 022), is a symmetry of the *exponential* structure — it swaps the base and dual lattices through exponentiation.

### 3.4 The crossing

The Casimir calculation *crosses between all three operations*:

    1. Sum over lattice points (addition)
    2. Mellin transform to analytic continuation (multiplication)
    3. Modular inversion to extract the correction (exponentiation)

At q = 2, these three crossings are self-consistent because 2 is where the operations agree. At any other q, the theta function doesn't factorize, the Jacobi inversion fails, and the modular structure breaks.

**The Euclidean norm isn't a convention. It's the unique norm where the arithmetic of the calculation is internally consistent.**

---

## 4. CONNECTION TO THE TWO ZEROS

This repository has documented two conceptions of zero:

- **European zero (void)**: 0 * x = 0. Absorbing. The zero mode is excluded from the sum (the prime on the summation sign). Zero swallows everything.
- **Indian zero (sunya)**: 0 * x = 0x. Non-absorbing. Zero binds but does not destroy. The zero mode participates.

Every calculation in this repository — every one — uses the European zero. We exclude n = 0 from the periodic sum. We write sum' with a prime. We skip it.

We then point to the Indian zero and say "look, it's connected!" We write about sunya. We derive the Geometry of Zero. We build COTT on non-absorbing zero. But we never *compute* with it.

### What changes with sunya-zero in the Casimir sum?

With European zero (current):

    Z_PPP(s) = sum'_{n in Z^3} |n|^{-2s}     (exclude n = 0)

The excluded zero mode contributes a pole at s = 3/2 in the Mellin representation, which is subtracted analytically.

With sunya-zero:

    Z_PPP^sunya(s) = sum_{n in Z^3} |n|^{-2s}    (include n = 0)

But |0|^{-2s} = 0^{-2s} is undefined in the European framework — it diverges. In COTT, 0^z is not undefined. It maps through the COTT power structure: 0^z -> the projection onto the zero element of the 4-cycle.

The difference between the two calculations is exactly the zero-mode contribution — the term that European math excludes and sunya-math includes. This is the pole at s = 3/2. This is what regularization removes. This is the cosmological constant problem: what does the vacuum contribute when you don't skip zero?

### Side-by-side comparison

| Quantity | European (skip zero) | Sunya (include zero) |
|----------|---------------------|---------------------|
| Z_PPP(-1/2) | -0.266601... | -0.266601... + 0^{+1} |
| Zero-mode | Excluded (pole subtracted) | Included (COTT-regularized) |
| Physical meaning | Vacuum has energy, zero contributes nothing | Vacuum has energy, zero contributes structure |
| R = Z_APP/Z_PPP | 0.041689... approx 1/24 | Depends on COTT value of 0^{+1} |

The 1/24 ratio holds in the European framework. Whether it holds, shifts, or becomes exact in the sunya framework is an open calculation — one that requires COTT's non-absorbing zero to be made numerically concrete.

---

## 5. THE 2-FIXED-POINT AND COTT'S 4-CYCLE

COTT's algebra has four elements: {1, 0, -1, omega}, cycling as:

    1 -> 0 -> -1 -> omega -> 1

The number 2 does not appear in COTT's basis. But it appears *structurally*:

- The torus T^3 has dimension 3, but the Casimir calculation lives at s = -1/2, which means the effective power is -2s = +1. The norm is quadratic (power 2).
- The theta function Theta(t) involves exp(-pi t n^2) — the square again.
- The modular group acts on the upper half-plane, which has (real) dimension 2.
- The boundary condition shift alpha = (1/2, 0, 0) uses the number 1/2 — the multiplicative inverse of 2.

2 is not in COTT's basis, but it is the **structural constant** of the space where COTT's predictions are tested. It is the number that makes arithmetic self-consistent, and therefore the number that makes the lattice sum computable.

In the resurgent framing (folder 033): the Borel transform divides by n!, and the Laplace transform multiplies by e^{-t}. These two operations are inverses because the factorial and the exponential are related by... the Gamma function, which satisfies Gamma(n+1) = n!. And the Gamma function's fundamental identity is:

    Gamma(1/2) = sqrt(pi)

There's 2 again — in the denominator, linking pi (the Borel singularity distance) to the factorial (the counting function). The 2-fixed-point is the hinge.

---

## 6. WHAT THIS MEANS

The Euclidean norm (q = 2) is not one choice among many. It is the *only* norm where:

1. The theta function factorizes (so the Mellin-Jacobi machinery works)
2. The modular group acts as a symmetry (so the correction formula is forced)
3. Addition, multiplication, and exponentiation are interchangeable (so crossing between operations preserves structure)

This is why the Casimir calculation gives a clean answer. This is why R approximately equals 1/24. This is why the correction formula has integer coefficients.

And this is why the *sunya* calculation — where zero participates instead of being excluded — must also be done at q = 2, if it is to be done at all. The 2-fixed-point is not optional. It is the condition under which arithmetic can talk to itself.

---

## 7. OPEN QUESTIONS

1. **Compute the sunya Casimir ratio**: What is R when the zero mode is included via COTT's non-absorbing zero? Does 1/24 become exact?

2. **The q-surface norm at q != 2**: James's norm (p^2 + q^2)^{1/q} deliberately violates the 2-fixed-point. In the resurgent framing, this corresponds to a Borel transform with non-standard kernel. What are the singularities?

3. **Why dimension 3?**: The cubic torus T^3 is the simplest lattice where the Casimir ratio is non-trivial. On T^1, R is trivial. On T^2, R lacks the three-way crossing. On T^3, all three operations participate. Is dimension 3 itself a consequence of the 2-fixed-point?

4. **The calculator**: Build a side-by-side calculator that computes both European-zero and sunya-zero Casimir sums, showing where the numbers diverge. This is the first tool that actually *uses* the Indian zero instead of just pointing at it.

---

*2 + 2 = 2 * 2 = 2^2. One number. Three operations. Same answer. That's not a coincidence. That's the reason the universe is measurable.*
