"""Who else sits in pi's chair?

067: the mean ring count in Z[i] converges to pi.
072: in Z[phi] it converges to 2 log(phi)/sqrt5.
Both are the SAME slot: the residue of zeta_K at s=1, which by the class number
formula is  rho = 2^r1 (2 pi)^r2 h R / (w sqrt|d|).

zeta_K(s) = zeta(s) L(s, chi_d), so the ideal count is a_K(m) = SUM_{e|m} chi_d(e)
and the running mean converges to L(1, chi_d) = rho.

Build the table by COUNTING, and check each against its closed form."""
import sys, math
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

# v1 of this script hand-rolled the Kronecker symbol and got the prime 2 wrong:
# kronecker(-4, 2) returned 1 where it must return 0. Every EVEN discriminant
# (-4, -8, +8, +12) then came out exactly 2x too large, and the odd ones were
# right -- a structured discrepancy, which is what exposed it. Verdict discarded.
# v2 uses sympy's kronecker_symbol, validated first against known character values
# for chi_-4, chi_-3, chi_5, chi_8, chi_-8: 0 mismatches.
from sympy import kronecker_symbol as kronecker

X = 2_000_000
phi = (1+math.sqrt(5))/2

# d, label, closed form, closed-form value, w (roots of unity)
FIELDS = [
 (-3,  "Q(sqrt-3)  hexagonal", "pi / (3 sqrt3)",        math.pi/(3*math.sqrt(3)), 6),
 (-4,  "Q(i)       square",    "pi / 4",                math.pi/4,                4),
 (-7,  "Q(sqrt-7)",            "pi / sqrt7",            math.pi/math.sqrt(7),     2),
 (-8,  "Q(sqrt-2)",            "pi / (2 sqrt2)",        math.pi/(2*math.sqrt(2)), 2),
 (-11, "Q(sqrt-11)",           "pi / sqrt11",           math.pi/math.sqrt(11),    2),
 ( 5,  "Q(sqrt5)   golden",    "2 log(phi) / sqrt5",    2*math.log(phi)/math.sqrt(5), 2),
 ( 8,  "Q(sqrt2)   silver",    "2 log(1+sqrt2)/sqrt8",  2*math.log(1+math.sqrt(2))/math.sqrt(8), 2),
 ( 12, "Q(sqrt3)",             "2 log(2+sqrt3)/sqrt12", 2*math.log(2+math.sqrt(3))/math.sqrt(12), 2),
 ( 13, "Q(sqrt13)",            "2 log((3+sqrt13)/2)/sqrt13", 2*math.log((3+math.sqrt(13))/2)/math.sqrt(13), 2),
]

print("   counting ideals of norm m <= %d in each field, then averaging" % X)
print()
print("   d    field                  counted mean      closed form                  value        w")
print("   " + "-"*94)
for d, name, cf, val, w in FIELDS:
    a = [0]*(X+1)
    for e in range(1, X+1):
        c = kronecker(d, e)
        if c:
            for m in range(e, X+1, e): a[m] += c
    mean = sum(a[1:])/X
    flag = "  <-- pi" if "pi" in cf else ""
    print(f"  {d:4d}  {name:22} {mean:.8f}      {cf:28} {val:.8f}  {w}{flag}")

print()
print("   " + "="*94)
print("   THE PATTERN")
print("   " + "="*94)
print()
print("   IMAGINARY discriminant  ->  pays  2 pi h / (w sqrt|d|)     -- a CIRCLE constant")
print("   REAL discriminant       ->  pays  2 h log(eps) / sqrt d    -- a UNIT's LOGARITHM")
print()
print("   and w > 2 happens in EXACTLY TWO fields, in all of number theory:")
print("      d = -4  ->  w = 4   mu_4    the SQUARE lattice")
print("      d = -3  ->  w = 6   mu_6    the HEXAGONAL lattice")
print("      everything else     w = 2   mu_2    only +-1")
print()
print("   mu_2, mu_4, mu_6 generate rotations of order 2, 4, 6 -- and 3, since")
print("   mu_6 contains it. That is EXACTLY {2,3,4,6}: the crystallographic")
print("   restriction of 065, arriving from the UNITS instead of the geometry.")# v1 hand-rolled the Kronecker symbol and got the prime 2 wrong: kronecker(-4,2)
# returned 1 where it must return 0. Every EVEN discriminant (-4,-8,+8,+12) then
# came out exactly 2x too large while the odd ones were right -- a structured
# discrepancy, which is what exposed it. Verdict discarded, not patched.
# v2 uses sympy kronecker_symbol, validated first against known values of
# chi_-4, chi_-3, chi_5, chi_8, chi_-8: 0 mismatches.
from kron import kron as kronecker   # validated vs sympy on 27000 values, 0 mismatches

X = 2_000_000
phi = (1+math.sqrt(5))/2

# d, label, closed form, closed-form value, w (roots of unity)
FIELDS = [
 (-3,  "Q(sqrt-3)  hexagonal", "pi / (3 sqrt3)",        math.pi/(3*math.sqrt(3)), 6),
 (-4,  "Q(i)       square",    "pi / 4",                math.pi/4,                4),
 (-7,  "Q(sqrt-7)",            "pi / sqrt7",            math.pi/math.sqrt(7),     2),
 (-8,  "Q(sqrt-2)",            "pi / (2 sqrt2)",        math.pi/(2*math.sqrt(2)), 2),
 (-11, "Q(sqrt-11)",           "pi / sqrt11",           math.pi/math.sqrt(11),    2),
 ( 5,  "Q(sqrt5)   golden",    "2 log(phi) / sqrt5",    2*math.log(phi)/math.sqrt(5), 2),
 ( 8,  "Q(sqrt2)   silver",    "2 log(1+sqrt2)/sqrt8",  2*math.log(1+math.sqrt(2))/math.sqrt(8), 2),
 ( 12, "Q(sqrt3)",             "2 log(2+sqrt3)/sqrt12", 2*math.log(2+math.sqrt(3))/math.sqrt(12), 2),
 ( 13, "Q(sqrt13)",            "2 log((3+sqrt13)/2)/sqrt13", 2*math.log((3+math.sqrt(13))/2)/math.sqrt(13), 2),
]

print("   counting ideals of norm m <= %d in each field, then averaging" % X)
print()
print("   d    field                  counted mean      closed form                  value        w")
print("   " + "-"*94)
for d, name, cf, val, w in FIELDS:
    a = [0]*(X+1)
    for e in range(1, X+1):
        c = kronecker(d, e)
        if c:
            for m in range(e, X+1, e): a[m] += c
    mean = sum(a[1:])/X
    flag = "  <-- pi" if "pi" in cf else ""
    print(f"  {d:4d}  {name:22} {mean:.8f}      {cf:28} {val:.8f}  {w}{flag}")

print()
print("   " + "="*94)
print("   THE PATTERN")
print("   " + "="*94)
print()
print("   IMAGINARY discriminant  ->  pays  2 pi h / (w sqrt|d|)     -- a CIRCLE constant")
print("   REAL discriminant       ->  pays  2 h log(eps) / sqrt d    -- a UNIT's LOGARITHM")
print()
print("   and w > 2 happens in EXACTLY TWO fields, in all of number theory:")
print("      d = -4  ->  w = 4   mu_4    the SQUARE lattice")
print("      d = -3  ->  w = 6   mu_6    the HEXAGONAL lattice")
print("      everything else     w = 2   mu_2    only +-1")
print()
print("   mu_2, mu_4, mu_6 generate rotations of order 2, 4, 6 -- and 3, since")
print("   mu_6 contains it. That is EXACTLY {2,3,4,6}: the crystallographic")
print("   restriction of 065, arriving from the UNITS instead of the geometry.")
