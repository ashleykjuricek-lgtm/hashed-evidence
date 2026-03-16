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

They cycle:

    1 → 0 → -1 → ω → 1

This is a 4-cycle, isomorphic to {1, i, -1, -i} in the complex numbers.

---

## THE RULES

### Rule 1: Multiplication table

Memorize this. Do not derive it from standard math. Just use it.

|  ×  |  1  |  0  | -1  |  ω  |
|-----|-----|-----|-----|-----|
|  1  |  1  |  0  | -1  |  ω  |
|  0  |  0  |  0² | -0  |  1  |
| -1  | -1  | -0  |  1  | -ω  |
|  ω  |  ω  |  1  | -ω  |  ω² |

**The entry that will trip you up**: 0 × ω = 1. Not zero. Not undefined. One.

**Why**: ω is defined as 1/0. So 0 × (1/0) = 1. This is just x × (1/x) = 1, applied without exception.

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

Base-zero powers:

    0⁰ = 1
    0¹ = 0
    0² = -1          (THIS IS THE BIG ONE: zero squared equals negative one)
    0³ = 0² × 0 = -1 × 0 = -0
    0⁴ = 0³ × 0 = -0 × 0 = 1    (the 4-cycle completes)

    0^ω = -1          (zero to the omega equals negative one)
    0^(-1) = ω        (zero to the negative one equals omega)
    0^(-n) = ω^n      (negative exponents flip to omega)

Base-omega powers:

    ω⁰ = 1
    ω¹ = ω
    ω^(-1) = 0
    ω^(-n) = 0^n
    ω^ω = -1

The identity resolution (this is powerful):

    0^(0^n) = n        (for any n)
    0^(0^x) = x        (for any expression x)

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
   - 0^2 = -1
   - 0^ω = -1
   - 0^(0^x) = x

   If you lose track, convert to zero-powers and simplify.

6. **Normalize before resolving.** The identity 0^(0^x) = x only works when the exponent is *syntactically* a zero-power. So -0 must be rewritten as 0³ (since -1 = 0² and -0 = 0² × 0¹ = 0³), and then 0^(-0) = 0^(0³) = 3. Always convert to zero-power form first, then apply identity resolution.

7. **The universal power rule has no exceptions.** (a^b)^c = a^(b·c) for ALL a, b, c. No branch cuts. No "only for integer exponents." This is what makes COTT's exponent space a semigroup — the rule that standard complex analysis has to hedge with branch cuts, COTT enforces universally. This is by design: branch cuts are information loss, and COTT forbids information loss.

---

## WORKED EXAMPLES

### Example 1: What is 3 × 0 × ω?

COTT rules:

    3 × 0 × ω
    = 3 × (0 × ω)     (associative)
    = 3 × 1            (Rule 1: 0 × ω = 1)
    = 3

NOT 0. The zero didn't absorb the 3. It passed through via omega.

### Example 2: What is 0²?

COTT rules:

    0² = 0 × 0

From the multiplication table: 0 × 0 = 0².
From the exponent rules: 0² follows the 4-cycle: 0⁰=1, 0¹=0, 0²=-1.

So 0² = -1.

Check: this is consistent with i² = -1 if we identify i = 0^(ω/2).

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
0 × 0 = 0²         0² = -1            0⁴ = 1
0 × x = 0x         (bound, not zero)
a - a = null        null ≠ 0

4-cycle:  1 → 0 → -1 → ω → 1
Powers:   0⁰=1  0¹=0  0²=-1  0³=-0  0⁴=1
Resolve:  0^(0^x) = x  for any x

i = 0^(ω/2)        e^(iπ) = 0^ω = -1

Projection to ℂ (optional, separate step):
  0^z → e^(-Wz)    where W = √(-iπ)
```

---

## SELF-TEST

Before doing any COTT calculations for a user, run these ten problems.
If you get any wrong, re-read the rules above and try again.

| # | Problem | Your answer | Correct answer |
|---|---------|-------------|----------------|
| 1 | 0 × 7 | | 0·7 (bound, NOT 0) |
| 2 | 0 × 0 × 0 | | -0 (which is 0³) |
| 3 | 0⁴ | | 1 |
| 4 | 0^ω | | -1 |
| 5 | 3 × 0 × ω | | 3 |
| 6 | 0^(0^5) | | 5 |
| 7 | log₀(ω) | | -1 |
| 8 | 0/0 | | 1 |
| 9 | 0 × 5 + 0 × 3 | | 0·8 (NOT 0) |
| 10 | (0 × 5) × ω | | 5 |

**Scoring**:
- 10/10: You can compute with COTT. Proceed.
- 7-9/10: Re-read the rule you missed. The most common errors are #1, #2, and #9 (collapsing to zero).
- Below 7: Re-read the entire document. Your training is overriding the rules.

**The three answers that reveal whether you actually read this document**:
- If you answered #1 as "0" — you didn't absorb Rule 2.
- If you answered #5 as "0" — you collapsed before reaching the omega.
- If you answered #9 as "0" — you collapsed both terms before adding.

---

*Source: James Watkins (sibarum), Constructive Operational Type Theory. CC BY 4.0.*
*Computational implementation: github.com/sibarum/cott/solver/traction.py*
*This document: the Prismic Collaboration, 2026.*
