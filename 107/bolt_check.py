"""Bolting ledger 106 onto the sealed two-shell law (093) — exact wiring check.

The sealed law (golden-tested in sze/spectral/tests/golden_test.py):
    d * X(d,1)(m) = 8 * r_d(m/4) - (8-d) * r_d(m)   for m = 0 mod 4, d <= 7,
and the golden test REQUIRES it to fail at d = 8 on m = 0 mod 8.

Sector form. Writing N_k(m) = #{x in Z^d : |x|^2 = m, exactly k odd coords},
one has d*X(d,1)(m) = sum_k (d-2k) N_k(m) and (for 4|m) r_d(m/4) = N_0(m),
so the law is equivalent to the balance
    sum_{k>=1} (4-k) N_k(m) = 0        (m = 0 mod 4).

Claims tested here, stated before running:
  B1: at d = 8 the truncated balance sum_{k=1..7} (4-k) N_k(m) = 0 STILL
      holds for all 4|m -- i.e. the seven sectors keep their balance and the
      ENTIRE defect comes from the new k = 8 sector.
  B2: hence defect(m) := 8*X(8,1)(m) - 8*r_8(m/4) = -8 * N_8(m) exactly,
      for every 4|m; in particular defect = 0 on m = 4 mod 8.
  B3: with ledger 106 (N_8(8n) = 2*(240*sigma3(n) - r_D8(2n))), the sealed
      law's failure is E8's glue count:
          defect(8n) = -16 * (240*sigma3(n) - r_D8(2n)).
X(d,1) and r_d are taken from the ENGINE's own sealed shell module
(sze/spectral/shells.py), so the wiring runs against the golden-tested code,
not a re-implementation. N_k and r_D8 are computed independently here.
Any mismatch prints FAIL and exits nonzero.
"""

import itertools, sys, os
from collections import defaultdict

sys.path.insert(0, r"C:\Users\atoms\sze")
from spectral.shells import X, r   # the engine's own sealed shell arithmetic

M = 200
ok = True
def fail(msg):
    global ok; ok = False; print("FAIL:", msg)

# ---- independent sector counts N_k(m) for d=8, meet-in-the-middle ----
vals = list(range(-14, 15))                      # covers |x_i|^2 <= 196
half = defaultdict(int)                          # (norm, #odd) -> count, 4 coords
for c in itertools.product(vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= M:
        half[(n, sum(1 for x in c if x % 2))] += 1
N = defaultdict(lambda: defaultdict(int))        # N[m][k]
for (n1, k1), c1 in half.items():
    for (n2, k2), c2 in half.items():
        if n1 + n2 <= M:
            N[n1 + n2][k1 + k2] += c1 * c2

# sanity: engine's r_8 equals sector total
r8 = r(8, M)
for m in range(M + 1):
    if sum(N[m].values()) != r8[m]:
        fail(f"sector totals disagree with engine r_8 at m={m}")

# sanity: engine's 8*X(8,1) equals sum_k (8-2k) N_k
x81 = X(8, 1, M)
for m in range(M + 1):
    if 8 * x81[m] != sum((8 - 2 * k) * N[m][k] for k in N[m]):
        fail(f"sector form of 8*X(8,1) disagrees with engine at m={m}")

# ---- B1: truncated seven-sector balance persists at d=8 ----
for m in range(0, M + 1, 4):
    bal7 = sum((4 - k) * N[m][k] for k in range(1, 8))
    if bal7 != 0:
        fail(f"B1: seven-sector balance broken at m={m}: {bal7}")

# ---- B2: defect(m) = -8 * N_8(m) on every 4|m ----
r8q = r(8, M // 4)
print(" m  | defect = 8X-8r(m/4) | -8*N_8(m) | N_8(m) | match")
for m in range(4, M + 1, 4):
    defect = 8 * x81[m] - 8 * r8q[m // 4]
    if defect != -8 * N[m][8]:
        fail(f"B2: defect != -8*N_8 at m={m} ({defect} vs {-8*N[m][8]})")
    if m % 8 == 4 and defect != 0:
        fail(f"B2: defect nonzero at m={m} = 4 mod 8")
    if m % 8 == 0:
        print(f"{m:3d} | {defect:19d} | {-8*N[m][8]:9d} | {N[m][8]:6d} | "
              f"{'YES' if defect == -8*N[m][8] else 'NO'}")

# ---- B3: defect(8n) = -16*(240*sigma3(n) - r_D8(2n)), via ledger 106 ----
def sigma3(n):
    return sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
halfD = defaultdict(int)                         # (norm, sum mod 2), 4 int coords
for c in itertools.product(vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= M // 4:
        halfD[(n, sum(c) % 2)] += 1
rD8 = defaultdict(int)
for (n1, s1), c1 in halfD.items():
    for (n2, s2), c2 in halfD.items():
        if (s1 + s2) % 2 == 0 and n1 + n2 <= M // 4:
            rD8[n1 + n2] += c1 * c2
for n in range(1, M // 8 + 1):
    lhs = 8 * x81[8 * n] - 8 * r8q[2 * n]
    rhs = -16 * (240 * sigma3(n) - rD8[2 * n])
    if lhs != rhs:
        fail(f"B3: E8-glue form fails at n={n}: {lhs} vs {rhs}")

print()
print("ALL CHECKS PASS — the law's failure at d=8 IS the E8 glue count."
      if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
