"""d* to high precision, so PSLQ has something honest to work with."""
import fractional
from mpmath import mp, mpf, findroot, nstr
import sys
for dps, N, K in [(40, 34, 14), (55, 46, 20), (70, 58, 26)]:
    mp.dps = dps
    f = lambda d: fractional.Z(d, 1, N=N, K=K)
    r = findroot(f, (mpf('2.6390688'), mpf('2.6390689')), solver='secant', tol=mpf(10)**-(dps-6))
    print(f"dps={dps} N={N} K={K}")
    print("   d* =", nstr(r, dps-4))
    sys.stdout.flush()
