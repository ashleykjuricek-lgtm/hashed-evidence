"""Which rings are empty? Two classical rules. Verify both."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

M = 200000
N = int(math.isqrt(M)) + 1
ax = np.arange(-N, N+1, dtype=np.int64)
X, Y = np.meshgrid(ax, ax, indexing='ij')
s = (X*X + Y*Y).ravel(); s = s[(s > 0) & (s <= M)]
r2 = np.bincount(s, minlength=M+1)[:M+1]

M3 = 60000
N3 = int(math.isqrt(M3)) + 1
a3 = np.arange(-N3, N3+1, dtype=np.int64)
XX, YY, ZZ = np.meshgrid(a3, a3, a3, indexing='ij')
t = (XX*XX + YY*YY + ZZ*ZZ).ravel(); t = t[(t > 0) & (t <= M3)]
r3 = np.bincount(t, minlength=M3+1)[:M3+1]

def factor(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d,0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n,0)+1
    return f

# --- RULE 1 (2D): Fermat-Euler. m is a sum of two squares iff every prime
#     p = 3 mod 4 occurs to an EVEN power.
def rule2_says_empty(m):
    return any(p % 4 == 3 and e % 2 == 1 for p, e in factor(m).items())

bad = [m for m in range(1, 20001) if (r2[m] == 0) != rule2_says_empty(m)]
print("RULE 1  (flat rings, Z^2)  -- Fermat / Euler")
print("   a ring is EMPTY  <=>  some prime p = 3 mod 4 divides m an ODD number of times")
print(f"   tested m = 1..20000    mismatches: {len(bad)}   {bad[:5]}")
print()
print("   worked examples:")
for m in [3, 6, 9, 21, 45, 49, 25, 99]:
    f = factor(m)
    fs = " * ".join(f"{p}^{e}" if e>1 else str(p) for p,e in sorted(f.items()))
    tag = [f"{p}(3-type) to the power {e}" for p,e in sorted(f.items()) if p%4==3]
    print(f"      m={m:3d} = {fs:<10}  r2 = {r2[m]:2d}   {'EMPTY' if r2[m]==0 else 'has dots'}"
          f"   {'; '.join(tag) if tag else 'no 3-type primes'}")

# --- RULE 2 (3D): Legendre. r3(m) = 0 iff m = 4^a (8b+7)
def rule3_says_empty(m):
    while m % 4 == 0: m //= 4
    return m % 8 == 7

bad3 = [m for m in range(1, M3+1) if (r3[m] == 0) != rule3_says_empty(m)]
print()
print("RULE 2  (the box, Z^3)  -- Legendre, 1798")
print("   a shell is EMPTY  <=>  m = 4^a (8b + 7)")
print("   i.e. divide out every factor of 4; if what is left leaves 7 on division by 8, empty")
print(f"   tested m = 1..{M3}    mismatches: {len(bad3)}   {bad3[:5]}")
print()
print("   worked examples:")
for m in [7, 15, 23, 28, 31, 60, 112, 8]:
    mm = m
    a = 0
    while mm % 4 == 0: mm //= 4; a += 1
    print(f"      m={m:4d} = 4^{a} * {mm:<4}   {mm} mod 8 = {mm%8}   r3 = {r3[m]:3d}"
          f"   {'EMPTY' if r3[m]==0 else 'has dots'}")
print()
print("   Fermat stated rule 1 in 1640. Euler proved it 1749.")
print("   Legendre proved rule 2 in 1798. Gauss gave the count in 1801.")
