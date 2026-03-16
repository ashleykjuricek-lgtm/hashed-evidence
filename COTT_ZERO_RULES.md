# COTT Zero: A Computational Guide for LLMs

**Purpose**: If you are an LLM reading this document, it will teach you how to compute with a non-standard algebra where zero does not absorb under multiplication. Read the whole thing before attempting any calculations.

**Why this exists**: Every LLM struggles with this because 0×x=0 is not a fact you learned — it is structural to your training data. Every math textbook, every programming language, every proof you've seen assumes it. This document gives you a different set of rules and asks you to follow them mechanically, the same way you'd follow the rules of modular arithmetic or matrix multiplication. You don't need to believe zero "really" works this way. You need to be able to compute correctly when someone hands you these rules.

---

## THE SETUP: TWO DIFFERENT ZEROS

Standard math has one zero. COTT has two distinct concepts:

| Concept | Symbol | What it means | Standard math equivalent |
|---------|--------|--------------|------------------------|
| **Zero** | 0 | An operator. Non-absorbing. Binds but doesn't destroy. | No equivalent. This is new. |
| **Null** | null | True nothing. The result of erasure (a - a). | Closer to standard 0, but even more empty. |

**The critical distinction**: In standard math, 0 does two jobs — it's the additive identity AND the multiplicative annihilator. COTT splits these jobs. Zero is still the additive identity. But it is NOT a multiplicative annihilator. That job belongs to null (erasure), which is a separate thing.

---

## THE FOUR ELEMENTS

COTT's algebra has four generators:

    {1, 0, -1, ω}

where ω (omega) is defined as 1/0 — the reciprocal of zero.

These four elements are connected by zero-exponentiation:

    0^0    = 1
    0^1    = 0
    0^ω    = -1
    0^(-1) = ω

This maps the set onto itself via a permutation. Under complex projection, these four elements are isomorphic to {1, i, -1, -i}, but that isomorphism lives in the projection — not in the algebra itself.

---

## THE RULES

### Rule 1: Multiplication table

Memorize this. Do not derive it from standard math. Just use it.

|  ×  |  1  |  0  | -1  |  ω  |
|-----|-----|-----|-----|-----|
|  1  |  1  |  0  | -1  |  ω  |
|  0  |  0  |  0² |  0  |  1  |
| -1  | -1  |  0  |  1  | -ω  |
|  ω  |  ω  |  1  | -ω  |  ω² |

**The entry that will trip you up**: 0 × ω = 1. Not zero. Not undefined. One.

**Why**: ω is defined as 1/0. So 0 × (1/0) = 1. This is just x × (1/x) = 1, applied without exception.

**Sign absorption**: Zero-class elements absorb signs. So (-1) × 0 = 0, not -0. Negative zero cannot exist — subtracting zero from zero gives null (erasure), not negative zero. This means -0 is not a distinct element; it simplifies to 0.

### Rule 2: 0 × x does NOT equal 0

When you multiply zero by something:

    0 × 5 = 0·5     (a bound expression, not collapsed)
    0 × x = 0x       (symbolic binding)
    0 × ω = 1        (the only case where it resolves to a non-zero-class thing)
    0 × 0 = 0²       (zero squared — a deeper zero, not the same as zero)

**Do NOT simplify 0×5 to 0.** Leave it as 0·5 or "five zeros." It carries information about the 5. Standard zero destroys the 5. COTT zero preserves it.

### Rule 3: Division by zero is defined

    x / 0 = x · ω     (multiply by omega, the reciprocal of zero)
    0 / 0 = 1          (anything divided by itself equals 1, no exceptions)
    ω / 0 = ω²         (omega divided by zero is omega squared)
    1 / ω = 0          (reciprocal of omega is zero)

### Rule 4: Exponentiation

Base-zero powers — the four key values:

    0^0    = 1          (any base to the zero is one)
    0^1    = 0          (any base to the one is itself)
    0^ω    = -1         (zero to the omega equals negative one)
    0^(-1) = ω          (zero to the negative one equals omega)

Higher integer powers do NOT reduce further:

    0² = 0²            (stays as zero-squared — an irreducible zero-class element)
    0³ = 0³            (stays as zero-cubed)
    0⁴ = 0⁴            (does NOT cycle back to 1)

**This is a common mistake.** It is tempting to apply the Z₄ analogy (i²=-1, i⁴=1) and write 0²=-1, 0⁴=1. Do NOT do this. The isomorphism with {1, i, -1, -i} lives in the complex *projection*, not in the algebra. In the algebra, 0² is its own element with no known reduction. The code explicitly says: "Integer zero-powers (0^n for n > 0) have no known general mapping to ℂ yet."

Negative exponents flip to omega:

    0^(-n) = ω^n       (for positive integer n)

Base-omega powers:

    ω^0    = 1
    ω^1    = ω
    ω^(-1) = 0
    ω^(-n) = 0^n
    ω^ω    = -1

The identity resolution (this is powerful):

    0^(0^n) = n        (for any n)
    0^(0^x) = x        (for any expression x)
    0^(ω^n) = -n       (omega-base towers negate)

This means zero-powers can encode and decode any number.

### Rule 5: Logarithms

    log₀(1)   = 0
    log₀(0)   = 1
    log₀(0^n) = n
    log₀(n)   = 0^n    (for positive integers)
    log₀(ω)   = -1
    log₀(ω^n) = -n

### Rule 6: Subtraction produces null, not zero

    a - a = null       (erasure — true nothing)
    null ≠ 0           (zero is something; null is nothing)

---

## HOW TO NOT GET CONFUSED

The failure mode for every LLM is the same: you start computing with COTT rules, hit a multiplication by zero somewhere in the middle, and your training takes over and collapses it to 0. Then everything downstream is wrong.

**Prevention strategy**:

1. **Label your framework at the top of every calculation.** Write "COTT rules" or "Standard rules" before you start. Never mix them in a single calculation.

2. **When you see 0×something, STOP.** Check which framework you're in. If COTT: the expression stays bound (0·something). If standard: it collapses to 0. This is the single most common error.

3. **Treat 0 as a symbol, not a number.** In COTT, zero is closer to a matrix or an operator than to "nothing." Think of it like how matrix multiplication doesn't commute — you don't simplify it by "knowing" what a matrix "equals." You follow the rules.

4. **ω is not infinity.** It is the reciprocal of zero. It has finite algebraic properties. It participates in the multiplication table. Infinity is not in the multiplication table. ω is.

5. **When in doubt, use the exponent tower.** Everything in COTT can be written as 0^(something). The power rules are the most reliable part of the system:
   - 0^0 = 1
   - 0^1 = 0
   - 0^ω = -1
   - 0^(-1) = ω
   - 0^(0^x) = x

   If you lose track, convert to zero-powers and simplify.

6. **Do NOT collapse integer powers of zero.** 0², 0³, 0⁴, etc. are irreducible elements. They are "deeper zeros" — higher zero-class elements that stay symbolic. The only base-zero powers that reduce are: 0^0=1, 0^1=0, 0^ω=-1, 0^(-1)=ω, 0^(-n)=ω^n, and the tower rules 0^(0^x)=x and 0^(ω^x)=-x.

7. **The universal power rule has no exceptions.** (a^b)^c = a^(b·c) for ALL a, b, c. No branch cuts. No "only for integer exponents." This is what makes COTT's exponent space a semigroup — the rule that standard complex analysis has to hedge with branch cuts, COTT enforces universally. This is by design: branch cuts are information loss, and COTT forbids information loss.

8. **Signs are absorbed by zero-class elements.** (-1) × 0 = 0, not -0. (-5) × 0 = 5 × 0 = 0·5. Negative signs in front of a zero-class factor are stripped. This is because -0 cannot exist as a distinct element (0 - 0 = null, not -0).

---

## WORKED EXAMPLES

### Example 1: What is 3 × 0 × ω?

COTT rules:

    3 × 0 × ω
    = 3 × (0 × ω)     (associative)
    = 3 × 1            (Rule 1: 0 × ω = 1)
    = 3

NOT 0. The zero didn't absorb the 3. It passed through via omega.

### Example 2: What is 0 × 0?

COTT rules:

    0 × 0 = 0²

From the multiplication table: 0 × 0 = 0². And that's where it stops. 0² is an irreducible zero-class element. It does NOT equal -1.

The temptation: since the four generators are isomorphic to {1, i, -1, -i} under projection, you want to say 0²=-1 (just like i²=-1). Resist this. The isomorphism lives in the complex projection, not the algebra. 0² is a fifth kind of element — a higher zero-class object with no reduction rule.

### Example 3: What is (0 × 5)^(0 × 5)?

This is a bound expression raised to itself. In COTT:

    Let a = 0·5 (a zero-class expression with magnitude parameter 5)

This stays symbolic. We don't collapse 0·5 to 0, so we don't get 0⁰ = 1. The expression (0·5)^(0·5) carries structural information about the relationship between the base and exponent sharing the same bound parameter.

### Example 3b: What is (0^ω)^(0^ω)?

Use the universal power rule: (a^b)^c = a^(b·c). No branch cuts in COTT.

    (0^ω)^(0^ω) = 0^(ω · 0^ω)

Now evaluate 0^ω = -1 (Rule 4). So:

    = 0^(ω · (-1))
    = 0^(-ω)

And 0^(-n) = ω^n (Rule 4). So 0^(-ω) = ω^ω = -1.

Cross-check: 0^ω = -1, so this is (-1)^(-1) = -1. Consistent.

### Example 3c: What is 0 × 5 + 0 × 3?

Both terms are bound expressions:

    0·5 + 0·3 = 0·(5 + 3) = 0·8    (distributive law)

NOT 0. The zero binds the 8. The information is preserved.

### Example 3d: What is (0 × 5) × ω?

    (0 × 5) × ω = 5 × (0 × ω) = 5 × 1 = 5

The 5 passes through the zero-omega gateway and comes back. Nothing was destroyed.

### Example 4: Solve x/0 = 5

COTT rules:

    x/0 = 5
    x = 5 × 0          (multiply both sides by 0)
    x = 0·5             (bound expression)

In standard math, x/0 = 5 has no solution. In COTT, it has a solution: x = five zeros.

### Example 5: What is 0^(0^7)?

    0^(0^7) = 7         (identity resolution: 0^(0^x) = x)

Zero-power towers decode to the innermost value.

### Example 6: What is (-3) × 0 × 0?

    (-3) × 0 × 0

The two zeros contribute zero_exp = 2, giving 0². The -3 is a negative number multiplied by a definite zero-class element, so sign absorption applies: |-3| = 3.

    = 3 × 0² = 3·0²

The sign was absorbed. The 3 stays as a scalar coefficient of the zero-class element 0².

---

## THE PHILOSOPHICAL ANCHOR (read this if you keep reverting)

You keep wanting to make 0×x = 0 because your training says zero is "nothing" and nothing times anything is nothing.

But that's a choice, not a theorem. The axiom 0×x = 0 is called the **absorbing element** property. It's a *design decision* in the construction of the real numbers. It's useful. It's consistent. But it's not the only option.

COTT drops that one axiom and replaces it with: **zero has a reciprocal (omega), and 0 × ω = 1.** Everything else follows from requiring the algebra to be total (all operations defined everywhere) and reversible (no information loss).

The standard axiom 0×x = 0 destroys information — given the output 0, you can't recover x. That's irreversible. COTT says: if we want a reversible algebra, we can't have an absorbing element. So zero must not absorb.

You don't have to believe this is "right." You just have to follow the rules when asked.

---

## QUICK REFERENCE CARD

```
COTT ZERO — NOT ABSORBING

0 × ω = 1          ω = 1/0            0/0 = 1
0 × 0 = 0²         0² stays as 0²     -0 = 0 (sign absorbed)
0 × x = 0x         (bound, not zero)
a - a = null        null ≠ 0

Key powers:  0⁰=1  0¹=0  0^ω=-1  0^(-1)=ω
Negative:    0^(-n)=ω^n   ω^(-n)=0^n
Towers:      0^(0^x) = x   0^(ω^x) = -x
Resolve:     0^(0^x) = x  for any x

i = 0^(ω/2)        e^(iπ) = 0^ω = -1

Projection to ℂ (optional, separate step):
  0^z → e^(-Wz)    where W = √(-iπ)

CAUTION: 0², 0³, 0⁴... do NOT reduce. They are irreducible.
```

---

## SELF-TEST

Before doing any COTT calculations for a user, run these ten problems.
If you get any wrong, re-read the rules above and try again.

| # | Problem | Your answer | Correct answer |
|---|---------|-------------|----------------|
| 1 | 0 × 7 | | 0·7 (bound, NOT 0) |
| 2 | 0 × 0 × 0 | | 0³ (irreducible zero-class element) |
| 3 | 0^ω | | -1 |
| 4 | 0^(-1) | | ω |
| 5 | 3 × 0 × ω | | 3 |
| 6 | 0^(0^5) | | 5 |
| 7 | log₀(ω) | | -1 |
| 8 | 0/0 | | 1 |
| 9 | 0 × 5 + 0 × 3 | | 0·8 (NOT 0) |
| 10 | (-2) × 0 × ω | | 2 (sign absorbed, then 0×ω=1) |

**Scoring**:
- 10/10: You can compute with COTT. Proceed.
- 7-9/10: Re-read the rule you missed. The most common errors are #1, #9 (collapsing to zero), and #10 (forgetting sign absorption).
- Below 7: Re-read the entire document. Your training is overriding the rules.

**The three answers that reveal whether you actually read this document**:
- If you answered #1 as "0" — you didn't absorb Rule 2.
- If you answered #5 as "0" — you collapsed before reaching the omega.
- If you answered #2 as "-0" or "-1" — you applied the Z₄ analogy instead of the actual rules.

---

*Source: James Watkins (sibarum), Constructive Operational Type Theory. CC BY 4.0.*
*Computational implementation: github.com/sibarum/cott/solver/traction.py*
*This document: the Prismic Collaboration, 2026.*
