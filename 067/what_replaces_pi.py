"""If pi cancels out of R (064), what is left doing the work?
The shell counts r_d(m). And pi turns out to be exactly their average."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

M = 2_000_000
print("=== r2(m): the number of (x,y) in Z^2 with x^2 + y^2 = m ===")
N = int(math.isqrt(M)) + 1
ax = np.arange(-N, N+1, dtype=np.int64)
X, Y = np.meshgrid(ax, ax, indexing='ij')
s = (X*X + Y*Y).ravel()
s = s[(s > 0) & (s <= M)]
r2 = np.bincount(s, minlength=M+1)[:M+1]

print("   the actual counts, m = 1..24:")
print("   ", " ".join(f"{m}:{r2[m]}" for m in range(1, 25)))
print()
zeros = [m for m in range(1, 100) if r2[m] == 0]
print(f"   r2(m) = 0 for m = {zeros[:14]} ...")
print(f"   {sum(1 for m in range(1,M+1) if r2[m]==0)*100.0/M:.1f}% of all shells below {M} are EMPTY.")
print()
print("   running mean of r2 -- this is what pi IS:")
c = np.cumsum(r2[1:].astype(np.float64))
for X0 in [100, 10_000, 500_000, M]:
    print(f"      mean over m <= {X0:>9} : {c[X0-1]/X0:.8f}     pi = {math.pi:.8f}")
print()

print("=== r3(m): the same in Z^3 ===")
M3 = 200_000
N3 = int(math.isqrt(M3)) + 1
a3 = np.arange(-N3, N3+1, dtype=np.int64)
XX, YY, ZZ = np.meshgrid(a3, a3, a3, indexing='ij')
t = (XX*XX + YY*YY + ZZ*ZZ).ravel()
t = t[(t > 0) & (t <= M3)]
r3 = np.bincount(t, minlength=M3+1)[:M3+1]
print("   the actual counts, m = 1..20:")
print("   ", " ".join(f"{m}:{r3[m]}" for m in range(1, 21)))
print()
z3 = [m for m in range(1, 200) if r3[m] == 0]
print(f"   r3(m) = 0 for m = {z3[:12]} ...")
print("   Legendre: r3(m) = 0 exactly when m = 4^a (8b + 7).  7, 15, 23, 28, 31, ...")
print()
print("   r3(m) averages 2 pi sqrt(m):")
c3 = np.cumsum(r3[1:].astype(np.float64))
for X0 in [1000, 50_000, M3]:
    pred = (4.0/3.0)*math.pi*X0**1.5
    print(f"      sum r3(m), m <= {X0:>7} : {c3[X0-1]:.1f}   vs (4/3) pi X^(3/2) = {pred:.1f}"
          f"   ratio {c3[X0-1]/pred:.6f}")
print()
print("=== the point ===")
print("   r2, r3 : integers. Wildly irregular. Often ZERO. No pi.")
print("   pi     : their average.  Nothing else.")
print()
print("   pi never vanishes. r2 vanishes on the majority of shells (computed above); r3 on the 4^a(8b+7).")
print("   Every shell the smoothing cannot see is a shell where the count is 0")
print("   and the average says 3.14159...")
