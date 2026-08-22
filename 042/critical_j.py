"""Fix the dimension. Ask how many marked circles it takes to reach the crossing.
The answer is not a whole number, and there is no reason it should have been."""
from mpmath import mp
mp.dps = 15
from fractional import Z
from mpmath import mpf, findroot, nstr, identify, sqrt, pi, mpmathify

print("critical number of marked circles j* solving Z(d, j*) = 0:")
print("    d          j*                 j*/d            d/2")
for d in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
    f = lambda j: Z(d, j, N=12, K=4)
    lo, hi = mpf(d)/2 - mpf('0.6'), mpf(d)/2 + mpf('0.1')
    if lo < mpf('0.05'): lo = mpf('0.05')
    try:
        r = findroot(f, (lo, hi), solver='secant', tol=mpf(10)**-14)
    except Exception as e:
        print(f"   {d:3d}   failed: {e}"); continue
    print(f"   {d:3d}   {nstr(r,12):>14}   {nstr(r/d,10):>14}   {mpf(d)/2}", flush=True)

print()
print("what kind of number is the j=1 crossing d* = 2.63906887168 ?")
d1 = mpf('2.639068871683')
for name, val in [("2+1/sqrt2", 2+1/sqrt(2)), ("1+golden", (3+sqrt(5))/2),
                  ("e-0.08", None), ("sqrt(2)+sqrt(1.5)", sqrt(2)+sqrt(mpf(3)/2)),
                  ("8/3", mpf(8)/3), ("pi-0.5", pi-mpf(1)/2)]:
    if val is None: continue
    print(f"   {name:>18} = {nstr(val,12):>14}   diff {nstr(abs(val-d1),4)}")
print("   mpmath identify:", identify(d1))
print("   identify w/ constants:", identify(d1, ['pi','sqrt(2)','sqrt(5)','log(2)']))
