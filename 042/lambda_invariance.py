"""Correctness test for the real-dimension continuation.

The Ewald cut lam is a free parameter of the SPLIT, not of the object. If the
continuation is right, Z must not depend on it -- at fractional d as well as
integer d. If it were botched, lam-dependence is where that shows.
"""
import fractional
from mpmath import mp, mpf, nstr
mp.dps = 25

cases = [(mpf('2.639068871683003864638172'), 1), (mpf('3.5'), mpf('1.25')),
         (mpf('11'), mpf('5.4218057568927310605')), (mpf('7.77'), mpf('3.03'))]
for d, j in cases:
    print(f"d = {nstr(d,12)}, j = {nstr(j,12)}")
    vals = []
    for lam in ['0.4', '0.7', '1', '1.6', '2.5']:
        v = fractional.Z(d, j, lam=mpf(lam), N=26, K=10)
        vals.append(v)
        print(f"    lam = {lam:>4}   Z = {nstr(v, 20)}")
    spread = max(vals) - min(vals)
    print(f"    spread across lam: {nstr(spread,4)}   {'INVARIANT' if abs(spread) < mpf(10)**-18 else 'DEPENDS ON LAM -- BUG'}")
    print()
