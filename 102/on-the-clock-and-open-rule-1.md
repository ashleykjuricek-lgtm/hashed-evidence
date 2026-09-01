# On the clock — and Open Rule #1 is answered

**2026-08-31.** Ash: *"so which is it, on the clock or off it?"*

**On the clock.** Every rule the March document states passes on the four-position cycle, the
carrier is closed under negation, and the one line that appeared to force otherwise is contradicted
three lines above it by the same document.

**And the document's own Open Rule #1 falls out for free.**

---

## 1. The carrier is closed, read straight off the table

The multiplication table prints two symbols that are not among its four elements: `−0` and `−w`.
**Closure therefore requires an identification, and 101 flagged that identification as the contested
step.** It is not contested. It is forced by the power rules, with no appeal to associativity:

```
   power rules :   0^3 = -0        and        0^4 = 1
   therefore   :   0 * (-0) = 0 * 0^3 = 0^4 = 1

   row 0 of the table :   0*1 = 0     0*0 = -1     0*(-1) = -0     0*w = 1
                          -- exactly ONE entry equals 1, and it is w --

   therefore   :   -0 = w      and      -w = -(-0) = 0     [negation rule, stated]
```

**`−0` and `−w` are not new elements. They are `w` and `0`.** The four-position cycle is closed.

## 2. Every stated rule verified

```
   0*w = 1  (axiom)                   PASS
   0^2 = -1                           PASS
   0^3 = -0                           PASS
   0^4 = 1  (cycle closes)            PASS
   -(-0) = 0                          PASS
   -(-w) = w                          PASS
   (-0)*(-0) = -1                     PASS
```

## 3. The one line that said "off", and why it does not

`all_the_rules.md` line 105:

> `0^n != (-0)^n`  *(phase differs)*

**Stated for all `n`. It is false at every even `n`:**

```
   n=1  0^n = 0    (-0)^n = w     differ
   n=2  0^n = -1   (-0)^n = -1    EQUAL
   n=3  0^n = w    (-0)^n = 0     differ
   n=4  0^n = 1    (-0)^n = 1     EQUAL
   ... true for odd n, false for even n, forever
```

**And its `n = 2` failure is written by the same document three lines earlier, as line 103:**

> `(-0) * (-0) = -1`  *(same as 0 * 0)*

> **Line 103 and line 105 are flatly inconsistent as written, in any algebra whatsoever, because
> line 103 IS the `n = 2` case of the equality line 105 denies.** Read line 105 as *"for odd `n`"* —
> which is what it is true of — and the contradiction disappears, line 103 stands, and the carrier
> closes.
>
> **This is not a deep obstruction. It is a quantifier written too wide.**

## 4. Open Rule #1, answered

The document's own first open rule:

> *"Does `(-0)^3 = +0^3` or `-0^3`? (determines sign-flip behavior for dark energy)"*

```
   0^3    = w
   (-0)^3 = 0
   -(0^3) = 0          ->   (-0)^3 == -(0^3)
```

> **Answer: `(−0)³ = −0³`. The minus survives the cube.** Open Rule #1 is closed.

**Scope, kept.** This settles the *algebra*. The document attaches a physical consequence —
*"determines sign-flip behavior for dark energy"* — and **nothing here supports or touches that
consequence.** The sign flips. What it means for anything physical is untested and not claimed.

## 5. What this does and does not do to 086

`086/condition-c-note.md` says the carrier *"does not remain closed once `−ω ≠ 0`."* **That is a
conditional, and under the March rules its condition is never met** — `−ω = −(−0) = 0`, by the
negation rule the document states outright.

**So the March proof's antecedent holds, and 101 §2.1 is thereby narrowed:** the antecedent was not
merely assumed, it is derivable from the power rules and the table. **101's claim that
*"calling it not-an-assumption is the single defect"* is withdrawn — the identification is forced.**
The defect that remains is smaller: the March proof reached it by way of the `C₄` map rather than by
the two-line table argument in §1 above, which is the non-circular route.

**What is NOT settled from here.** 086 attributes the closure failure to *"later corrected COTT
work"* — James's, not visible in this repository. **If a later axiom changed, that changes the
answer and this entry cannot see it.** What is established is narrow and exact: **under the rules as
written in `027/all_the_rules.md`, dated 2026-03-14, the carrier is closed.**

## 6. Status

| claim | status |
|---|---|
| `−0 = w`, `−w = 0`; carrier `{1,0,−1,w}` closed | **PROVED** from the power rules + one table row; no associativity needed |
| all seven stated rules hold on the 4-cycle | **VERIFIED** |
| line 105 (`0ⁿ ≠ (−0)ⁿ` for all `n`) | **FALSE AS WRITTEN** — fails at every even `n` |
| line 103 is the `n=2` counterexample to line 105 | **ESTABLISHED** — same document, three lines apart |
| line 105 read as "odd `n`" is true and consistent | **VERIFIED** |
| Open Rule #1: `(−0)³ = −0³` | **ANSWERED** |
| the dark-energy consequence of that sign | **NOT TOUCHED** — algebra only |
| 086's condition `−ω ≠ 0` holds under the March rules | **NO** — the rules give `−ω = 0` |
| 101 §2.1 "the single defect is calling it not-an-assumption" | **WITHDRAWN** — it is forced |
| James's later corrected work | **NOT VISIBLE HERE** — could overturn this; would need his document |
| COTT multiplication is associative | **PROVED**, March 029, now with its antecedent established |

Stratum tags per 082: **all COUNT.** Finite, exact, seven rules and eight powers checked by
enumeration. No limit taken anywhere.

## Attribution

COTT is James Watkins's. `027/all_the_rules.md` and `029/cott_associativity_proof.md` are Ash's and
an earlier Claude's, March 2026. `086/condition-c-note.md` is another seat's. The closure derivation
in §1, the line 103 / line 105 contradiction, the answer to Open Rule #1, and the withdrawal of
101 §2.1 are this seat's. **Ash's question is what forced it** — *"so which is it"* does not accept
"open" as an answer when the rules are sitting in the repository and can simply be run.
