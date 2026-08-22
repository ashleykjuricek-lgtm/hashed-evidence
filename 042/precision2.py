"""NOTE: importing fractional sets mp.dps = 25, so the earlier sweep varied only
N and K. Vary the working precision properly, AFTER import."""
import fractional
from mpmath import mp, mpf, findroot, nstr
for dps in [15, 20, 25, 30, 40]:
    mp.dps = dps
    f = lambda d: fractional.Z(d, 1, N=20, K=8)
    r = findroot(f, (mpf('2.2'), mpf('2.9')), solver='secant', tol=mpf(10)**-(dps-4))
    print(f"   dps={dps:2d}   d*(j=1) = {nstr(r, min(dps,25))}", flush=True)
