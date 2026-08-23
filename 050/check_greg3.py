"""TEST 5 -- the sign chain itself.

Greg's chain is  Z > 0  <=  dual character sum < 0  <=  theta bound.
The middle step is the functional equation, and its PREFACTOR carries the sign:

  Z(d,j) = pi^(-1-d/2) * Gamma((d+1)/2)/Gamma(-1/2) * SUM'_m (-1)^(m1+..+mj) |m|^(-(d+1))

Gamma(-1/2) = -2*sqrt(pi) < 0, so the prefactor is NEGATIVE. That is the entire
sign flip Greg relies on. Verify the formula reproduces Z, sign included.

The dual sum converges like 1/N (terms r^-(d+1), shell count r^(d-1)), so this is
a sign-and-magnitude check, not a precision check. That is what is at stake."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, itertools, math

def dual_sum(d, j, N):
    ax = np.arange(-N, N+1, dtype=np.int64)
    grids = np.meshgrid(*([ax]*d), indexing='ij')
    n2 = sum(g.astype(np.float64)**2 for g in grids)
    sgn = np.ones_like(n2)
    if j: sgn = (-1.0)**sum(g for g in grids[:j])
    n2[n2 == 0] = np.inf                      # drop the origin
    return float(np.sum(sgn * n2**(-(d+1)/2.0)))

REF = {(1,1):0.0833333333333333, (2,1):0.0236955331897287, (2,2):0.0670210888091522,
       (3,0):-0.266596278718393, (3,1):-0.0111142427950344, (3,2):0.0347814624899515,
       (3,3):0.0622964802744454, (4,2):0.0113490825476328, (5,3):0.0244859192310022}
NS = {1:200000, 2:900, 3:90, 4:32, 5:17}

print("Gamma(-1/2) = %.10f   (negative -- this is the sign flip)" % math.gamma(-0.5))
print()
print("  d  j     prefactor x dual sum        independent Z        ratio    sign ok")
allok = True
for (d, j), ref in REF.items():
    N = NS[d]
    pref = math.pi**(-1-d/2.0)*math.gamma((d+1)/2.0)/math.gamma(-0.5)
    approx = pref*dual_sum(d, j, N)
    ratio = approx/ref
    signok = (approx > 0) == (ref > 0)
    allok &= signok
    print(f"  {d:2d} {j:2d}   {approx:>22.10f}   {ref:>18.10f}   {ratio:>7.4f}   "
          f"{'OK' if signok else '*** WRONG SIGN ***'}")
print()
print("  -> sign of the functional-equation form matches Z in every case:", allok)
print("  (ratios near 1 confirm magnitude too; residual gap is the 1/N tail)")
