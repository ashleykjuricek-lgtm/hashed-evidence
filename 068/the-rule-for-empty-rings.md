# The rule for which rings are empty

**2026-08-25.** Ash: *"and that is? what?"* — on 067's line that the emptiness of a
shell follows a rule found two hundred years ago.

There are two rules, one for flat rings and one for the box. Both are classical.
Both verified here with **zero mismatches**.

---

## Rule 1 — flat rings, ℤ² · Fermat 1640, proved by Euler 1749

Some primes are **3-type**: the ones that leave 3 when divided by 4.
`3, 7, 11, 19, 23, 31, 43, 47, …`

> **A ring is empty ⟺ some 3-type prime divides `m` an ODD number of times.**

```
   m=  3 = 3          r2 =  0   EMPTY      one 3
   m=  6 = 2 * 3      r2 =  0   EMPTY      one 3
   m=  9 = 3^2        r2 =  4   has dots   two 3s -- even, so fine
   m= 21 = 3 * 7      r2 =  0   EMPTY      one 3 and one 7
   m= 25 = 5^2        r2 = 12   has dots   no 3-type primes at all
   m= 45 = 3^2 * 5    r2 =  8   has dots   two 3s
   m= 49 = 7^2        r2 =  4   has dots   two 7s
   m= 99 = 3^2 * 11   r2 =  0   EMPTY      two 3s fine -- but one 11
```

**Verified: `m = 1…20000`, 0 mismatches.**

`99` is the one to look at. Two 3s are fine. The single 11 empties the ring.

## Rule 2 — the box, ℤ³ · Legendre 1798

> **A shell is empty ⟺ `m = 4^a (8b + 7)`.**
>
> Divide out every factor of 4. If what is left leaves **7** on division by 8, the
> shell is empty.

```
   m=   7 = 4^0 * 7      7 mod 8 = 7    r3 =  0   EMPTY
   m=  15 = 4^0 * 15    15 mod 8 = 7    r3 =  0   EMPTY
   m=  28 = 4^1 * 7      7 mod 8 = 7    r3 =  0   EMPTY
   m=  60 = 4^1 * 15    15 mod 8 = 7    r3 =  0   EMPTY
   m= 112 = 4^2 * 7      7 mod 8 = 7    r3 =  0   EMPTY
   m=   8 = 4^1 * 2      2 mod 8 = 2    r3 = 12   has dots
```

**Verified: `m = 1…60000`, 0 mismatches.**

## What this means for the programme

067 measured that **79% of flat rings are empty** while π — their average — is never
zero. This names the thing the average destroys:

> The emptiness is not noise. It is **divisibility**. Which shells vanish is decided
> by the prime factorisation of `m` and by residues mod 4 and mod 8 — and it has been
> a theorem since 1749.

That is why the proved column of this ledger is π-free. Every proof in it is a
statement about which points are actually there:

- the **parity theorem** turns on `m` odd forcing exactly one coordinate odd —
  a residue condition mod 4;
- the **character law** splits on `m ≡ 0` versus `m ≡ 2` mod 4;
- `R(2,2) = 2^s − 1` comes from `r₂(2m) = r₂(m)`, a statement about the prime 2;
- `d = 3` fails because `r₃(1) = 6 ≠ 12 = r₃(2)`.

**All of it is mod-arithmetic on counts.** The average has no residues, no primes and
no zeros — which is exactly what makes it smooth, and exactly what it costs.

## Dates, for the record

```
   1640   Fermat states rule 1
   1749   Euler proves it
   1798   Legendre proves rule 2
   1801   Gauss gives the count r2(m) = 4(d_1(m) - d_3(m))
```

Nothing here is ours. It is stated because 067 asserted that a rule exists, and an
assertion of that kind should carry its rule.

## Status

| claim | status |
|---|---|
| ring empty ⟺ a 3-type prime to an odd power | **CLASSICAL**; verified 1…20000, 0 mismatches |
| shell empty ⟺ `m = 4^a(8b+7)` | **CLASSICAL**; verified 1…60000, 0 mismatches |
| the emptiness pattern is divisibility, not noise | **ESTABLISHED** by the above |
| the proved column is mod-arithmetic on counts | **VERIFIED** across all 15 |

## Attribution

Fermat, Euler, Legendre, Gauss. The verification and the alignment with this
ledger's proved column are this seat's, prompted by Ash asking what the rule
actually was rather than accepting that one existed.
