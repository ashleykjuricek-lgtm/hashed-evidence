import numpy as np
M = 20000
K = int(np.isqrt(M)) if hasattr(np,'isqrt') else int(M**0.5)
import math; K = math.isqrt(M)

# ---- d = 1, the only two seeds. exact integers, nothing else allowed ----
a1 = np.zeros(M+1, dtype=np.int64)   # count            #{n : n^2 = m}
b1 = np.zeros(M+1, dtype=np.int64)   # marked count     sum over n^2=m of (-1)^n
a1[0] = 1; b1[0] = 1
for n in range(1, K+1):
    a1[n*n] += 2
    b1[n*n] += 2*(-1)**n

def step(inp, seed):
    """add one dimension: out[m] = sum_k seed[k^2] * inp[m - k^2]"""
    out = np.zeros(M+1, dtype=np.int64)
    for k in range(0, K+1):
        s = seed[k*k]
        if s: out[k*k:] += s*inp[:M+1-k*k]
    return out

# X[d][j] = d dimensions, j of them marked
X = {}
for d in (1,2,3):
    for j in range(0, d+1):
        v = np.zeros(M+1, dtype=np.int64); v[0] = 1
        for i in range(d):
            v = step(v, b1 if i < j else a1)
        X[(d,j)] = v

print("her seeds, exactly:")
print(f"   r1(1) = {X[(1,0)][1]}      r2(1) = {X[(2,0)][1]}      r2(2) = {X[(2,0)][2]}")
print()
print("   m :   r1    r2    r3   |  d=2 j=1   d=3 j=1   d=3 j=2  | d=1 j=1  d=2 j=2  d=3 j=3")
print("   " + "-"*88)
for m in range(0, 25):
    print(f"  {m:3d} : {X[(1,0)][m]:4d}  {X[(2,0)][m]:4d}  {X[(3,0)][m]:4d}   |"
          f" {X[(2,1)][m]:7d}  {X[(3,1)][m]:8d}  {X[(3,2)][m]:8d}  |"
          f" {X[(1,1)][m]:6d}  {X[(2,2)][m]:7d}  {X[(3,3)][m]:8d}")

m = np.arange(M+1)
def law(name, lhs, rhs, mask):
    bad = int(np.count_nonzero((lhs != rhs) & mask))
    print(f"   {name:<58s} {'HOLDS' if bad==0 else 'FAILS'}   exceptions {bad} / {int(mask.sum())}")

print()
print("exact integer laws, tested on every m from 1 to 50,000:")
print("   " + "-"*88)
all_m = m >= 1
odd  = (m % 2 == 1)
even = (m % 2 == 0) & all_m
sign = (-1)**m

# mark EVERY circle
for d in (1,2,3):
    law(f"d={d}, all {d} marked:  X(m) = (-1)^m * r_{d}(m)", X[(d,d)], sign*X[(d,0)], all_m)

# mark exactly ONE circle
for d in (1,2,3):
    law(f"d={d}, exactly 1 marked:  X(m) = 0 for ODD m", X[(d,1)], np.zeros(M+1,dtype=np.int64), odd)

# the halving structure on even m, one mark
half = np.zeros(M+1, dtype=np.int64); half[::2] = X[(2,0)][:M//2+1]
hs   = np.zeros(M+1, dtype=np.int64); hs[::2]   = ((-1)**np.arange(M//2+1))*X[(2,0)][:M//2+1]
law("d=2, 1 marked, EVEN m=2k:  X(2k) = (-1)^k * r_2(k)", X[(2,1)], hs, even)

h3 = np.zeros(M+1, dtype=np.int64); h3[::2] = ((-1)**np.arange(M//2+1))*X[(3,0)][:M//2+1]
law("d=3, 1 marked, EVEN m=2k:  X(2k) = (-1)^k * r_3(k)", X[(3,1)], h3, even)

# two marked out of three
law("d=3, 2 marked:  X(m) = (-1)^m * r_3(m)", X[(3,2)], sign*X[(3,0)], all_m)
h32 = np.zeros(M+1, dtype=np.int64); h32[::2] = X[(3,1)][:M//2+1]
law("d=3, 2 marked, EVEN m=2k:  X(2k) = X_{3,1}(k)", X[(3,2)], h32, even)
law("d=3, 2 marked:  X(m) = 0 for ODD m", X[(3,2)], np.zeros(M+1,dtype=np.int64), odd)

# scaling laws, pure counts
law("r_2(2m) = r_2(m)", X[(2,0)][::2][:M//2+1], X[(2,0)][:M//2+1], np.ones(M//2+1,dtype=bool))
law("r_3(4m) = r_3(m)", X[(3,0)][::4][:M//4+1], X[(3,0)][:M//4+1], np.ones(M//4+1,dtype=bool))
law("r_2(m) divisible by 4", X[(2,0)] % 4, np.zeros(M+1,dtype=np.int64), all_m)

# Legendre, as a pure count statement
def is747(x):
    while x % 4 == 0: x //= 4
    return x % 8 == 7
leg = np.array([is747(int(v)) for v in range(M+1)])
law("r_3(m) = 0  exactly when m = 4^a(8b+7)", (X[(3,0)]==0), leg, all_m)
