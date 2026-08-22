"""Numerical check of three proofs. Every one is checked exhaustively, not sampled."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from collections import defaultdict

M = 4000
def shell(M):
    """all (k1,k2) with k1^2+k2^2 = m <= M, bucketed by m"""
    d = defaultdict(list)
    r = int(M**0.5) + 1
    for a in range(-r, r+1):
        for b in range(-r, r+1):
            m = a*a + b*b
            if 1 <= m <= M: d[m].append((a, b))
    return d
SH = shell(M)

def S(m):  return sum((-1)**a for a, b in SH.get(m, []))
def r2(m): return len(SH.get(m, []))
def T2(m): return sum((-1)**a * b*b for a, b in SH.get(m, []))

print("PROOF A -- full character law")
print("   S(m) = 0                 for m odd")
print("   S(m) = (-1)^(m/2)*r2(m)  for m even")
bad = [m for m in range(1, M+1) if m in SH and
       (S(m) != 0 if m % 2 else S(m) != (-1)**(m//2) * r2(m))]
print(f"   representable m tested: {len(SH)}     violations: {len(bad)}  {bad[:5]}")

print()
print("PROOF B -- 3D slicing, T(m) = 2*sum_{k3>=1 odd} S(m - k3^2), for m odd")
def T3(m):
    t = 0
    r = int(m**0.5) + 1
    for c in range(-r, r+1):
        rest = m - c*c
        if rest >= 0: t += S(rest) if rest > 0 else 1   # S(0)=1 (the origin, (-1)^0)
    return t
def T3_sliced(m):
    t = 0; c = 1
    while c*c <= m:
        rest = m - c*c
        t += (S(rest) if rest > 0 else 1)
        c += 2
    return 2*t
badB = [m for m in range(1, 1000, 2) if T3(m) != T3_sliced(m)]
print(f"   odd m tested: {len(range(1,1000,2))}     violations: {len(badB)}  {badB[:5]}")

print()
print("PROOF C -- exact formula  T2(m) = m*r2(m)/2 - 2*sum_{k1 even} k1^2   (m odd)")
def T2_formula(m):
    E = [(a, b) for a, b in SH.get(m, []) if a % 2 == 0]
    return m*r2(m)//2 - 2*sum(a*a for a, b in E)
odd = [m for m in range(1, M+1, 2) if m in SH]
badC = [m for m in odd if T2(m) != T2_formula(m)]
print(f"   odd representable m tested: {len(odd)}     violations: {len(badC)}  {badC[:5]}")

print()
print("   consequence: T2(m)=0  <=>  mean of k1^2 over the even-k1 half-shell = m/2")
zeros = [m for m in odd if T2(m) == 0]
print(f"   odd representable m <= {M} with T2(m) = 0:  {len(zeros)}   {zeros[:10]}")
print(f"   sample: T2(1)={T2(1)}  T2(5)={T2(5)}  T2(25)={T2(25)}  T2(325)={T2(325)}")
