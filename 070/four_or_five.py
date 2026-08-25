"""Is the circle divided into 4 or into 5?

Both. They are two different quadratic fields, and each has its own
lattice, its own prime rule, and its own allowed symmetry.

  Z[i]   Gaussian integers    norm x^2 + y^2       primes split on p mod 4
  Z[phi] golden integers      norm x^2 + xy - y^2  primes split on p mod 5
"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

M = 3000
def primes(n):
    s = np.ones(n+1, bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]
P = primes(M)

# ---- Z[i] : x^2 + y^2 ----
N = int(math.isqrt(M))+1
rep4 = set()
for x in range(0, N+1):
    for y in range(0, N+1):
        v = x*x + y*y
        if 0 < v <= M: rep4.add(v)

# ---- Z[phi] : x^2 + xy - y^2   (discriminant 5)  -- represent |N| ----
B = 200
rep5 = set()
for x in range(-B, B+1):
    for y in range(-B, B+1):
        v = abs(x*x + x*y - y*y)
        if 0 < v <= M: rep5.add(v)

print("=== the two prime rules ===")
print()
print("  Z[i]  -- a prime is represented by x^2 + y^2  iff  p = 2 or p = 1 mod 4")
bad4 = [int(p) for p in P if (int(p) in rep4) != (p == 2 or p % 4 == 1)]
print(f"     primes tested to {M}: {len(P)}    mismatches: {len(bad4)}  {bad4[:5]}")
print("     represented:", [int(p) for p in P[:14] if int(p) in rep4])
print("     not:        ", [int(p) for p in P[:14] if int(p) not in rep4])
print()
print("  Z[phi] -- a prime is represented by x^2 + xy - y^2  iff  p = 5 or p = +-1 mod 5")
bad5 = [int(p) for p in P if (int(p) in rep5) != (p == 5 or p % 5 in (1,4))]
print(f"     primes tested to {M}: {len(P)}    mismatches: {len(bad5)}  {bad5[:5]}")
print("     represented:", [int(p) for p in P[:14] if int(p) in rep5])
print("     not:        ", [int(p) for p in P[:14] if int(p) not in rep5])
print()
print("=== the two worlds ===")
print()
print("            field        norm form        prime rule    lattice        symmetry")
print("   ------------------------------------------------------------------------------")
print("   FOUR     Q(i)         x^2 + y^2        p mod 4       Z^2, Z^3       2,3,4,6-fold")
print("            disc -4                                     PERIODIC       10-fold FORBIDDEN")
print()
print("   FIVE     Q(sqrt5)     x^2 + xy - y^2   p mod 5       Penrose        10-fold")
print("            disc +5                                     QUASIPERIODIC  from Z^5 -> R^2")
print()
print("   the cubic torus lives in the first. the rose lives in the second.")
print("   065 separated them by the crystallographic restriction.")
print("   this is the same wall seen from the number-theory side.")

print()
print("=== and they are NOT the same division ===")
four = [int(p) for p in P if p == 2 or p % 4 == 1]
five = [int(p) for p in P if p == 5 or p % 5 in (1,4)]
S4, S5 = set(four), set(five)
both = sorted(S4 & S5); only4 = sorted(S4 - S5); only5 = sorted(S5 - S4)
neither = sorted(set(int(p) for p in P) - S4 - S5)
print(f"   lit in BOTH worlds   : {len(both):3d}   {both[:10]}")
print(f"   lit only in FOUR     : {len(only4):3d}   {only4[:10]}")
print(f"   lit only in FIVE     : {len(only5):3d}   {only5[:10]}")
print(f"   dark in BOTH         : {len(neither):3d}   {neither[:10]}")
print()
print("   11, 19, 31 are 3 mod 4 -- they EMPTY a square ring.")
print("   11, 19, 31 are +-1 mod 5 -- they FILL a golden one.")
print()
print("   13, 17, 37 are 1 mod 4 -- they fill a square ring.")
print("   13, 17, 37 are 2 or 3 mod 5 -- they empty a golden one.")
print()
print("   So a shell that is DARK in one world can be LIT in the other.")
print("   There is not one circle divided one way. There are two divisions,")
print("   and each is blind exactly where the other sees.")
