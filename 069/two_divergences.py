"""Third seat's claim: pi is the PRODUCT of two runaway processes.
   fraction of rings that are lit  -> 0     (Landau 1908)
   average count on the lit rings  -> inf
   their product                   =  pi    forever
Verify, and check Landau-Ramanujan tracking."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

M = 20_000_000
N = int(math.isqrt(M)) + 1
print(f"counting lattice points to |n|^2 <= {M} ...")
ax = np.arange(0, N+1, dtype=np.int64)
r2 = np.zeros(M+1, dtype=np.int64)
for x in range(0, N+1):
    x2 = x*x
    if x2 > M: break
    ymax = int(math.isqrt(M - x2))
    y = np.arange(0, ymax+1, dtype=np.int64)
    s = x2 + y*y
    # multiplicity from sign choices
    mult = np.where((x>0)&(y>0), 4, np.where((x>0)|(y>0), 2, 0))
    np.add.at(r2, s, mult)
r2[0] = 0

K = 0.7642236535892206   # Landau-Ramanujan constant
print()
print("      X        lit%     empty%    mean over ALL   mean over LIT    L-R pred lit%")
print("  " + "-"*76)
for X in [100, 10_000, 1_000_000, 2_000_000, 5_000_000, 20_000_000]:
    seg = r2[1:X+1]
    lit = int(np.count_nonzero(seg)); tot = float(np.sum(seg))
    f = lit/X
    mean_all = tot/X
    mean_lit = tot/lit
    lr = K/math.sqrt(math.log(X))
    print(f"  {X:>10}   {100*f:6.2f}%  {100*(1-f):6.2f}%   {mean_all:12.8f}   {mean_lit:11.4f}     {100*lr:6.2f}%")

print()
print("  pi = 3.14159265")
print()
print("=== the identity ===")
X = M
seg = r2[1:X+1]; lit = int(np.count_nonzero(seg)); tot = float(np.sum(seg))
f = lit/X; mean_lit = tot/lit
print(f"  at X = {X}:   f = {f:.8f}   mean_lit = {mean_lit:.6f}")
print(f"  f * mean_lit = {f*mean_lit:.8f}        pi = {math.pi:.8f}")
print()
print("  trivially exact by construction (both are total/X and total/lit),")
print("  but the CONTENT is that f -> 0 and mean_lit -> infinity separately,")
print("  while their product is pinned to pi at every cutoff.")
print()
print("=== Landau 1908 / Landau-Ramanujan ===")
print("  #{m <= X : m is a sum of two squares} ~ K X / sqrt(log X),  K = 0.76422365...")
print("  so the LIT fraction dies like 1 / sqrt(log X)  -- to ZERO, always.")
print("  Empty fraction -> 100%. 'Four in five' is a snapshot, not a fact.")
