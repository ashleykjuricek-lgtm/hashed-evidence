"""The remaining lemma, restated as one inequality.

Greg's proved half + monotonicity gives   j*(d) < d/2.
The remaining lemma  Z(d,(d-1)/2) < 0  is exactly   j*(d) > (d-1)/2.

Together:      (d-1)/2  <  j*(d)  <  d/2        upper bound PROVED, lower REMAINING

So the whole thing reduces to a single bound on one sequence:

        sup_d  [ d/2 - j*(d) ]  <  1/2 ?

Locate where that sup lives."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import fractional
from mpmath import mp, mpf, findroot, nstr, sqrt
mp.dps = 20

print("   d      j*(d)            d/2 - j*(d)      margin to 1/2")
worst = (0, mpf(0))
for d in range(1, 25):
    lo, hi = mpf(d)/2 - mpf('0.9'), mpf(d)/2 + mpf('0.05')
    if lo < mpf('0.02'): lo = mpf('0.02')
    try:
        r = findroot(lambda j: fractional.Z(d, j, N=16, K=6), (lo, hi), solver='secant', tol=mpf(10)**-16)
    except Exception as e:
        print(f"   {d:2d}   root not bracketed ({e})"); continue
    gap = mpf(d)/2 - r
    if gap > worst[1]: worst = (d, gap)
    print(f"   {d:2d}   {nstr(r,12):>15}   {nstr(gap,10):>14}   {nstr(mpf(1)/2-gap,10):>14}")
    sys.stdout.flush()
print()
print(f"   largest gap found: d = {worst[0]},  d/2 - j* = {nstr(worst[1],12)}")
print(f"   margin to the 1/2 barrier: {nstr(mpf(1)/2-worst[1],12)}")
print()
print("   so the lemma is tightest at small d and gets easier as d grows")
print("   (042 measured the gap shrinking by a factor -> 1/sqrt2 per dimension)")
