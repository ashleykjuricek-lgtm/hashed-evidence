"""Two questions:
   (a) does j*/d approach 1/2, and how fast?
   (b) is d*(j=1) = 2.639068871683003864638172 any recognisable constant?"""
import fractional
from mpmath import mp, mpf, findroot, nstr, identify, sqrt, pi, log, e
mp.dps = 25

print("(a)  j*(d)/d  ->  1/2  from below?   deficit = 1/2 - j*/d")
prev = None
for d in range(6, 23):
    f = lambda j: fractional.Z(d, j, N=20, K=8)
    r = findroot(f, (mpf(d)/2-mpf('0.7'), mpf(d)/2+mpf('0.05')), solver='secant', tol=mpf(10)**-18)
    def_ = mpf(1)/2 - r/d
    ratio = "" if prev is None else nstr(def_/prev, 10)
    print(f"   d={d:3d}   j* = {nstr(r,14):>17}   j*/d = {nstr(r/d,12):>14}   deficit = {nstr(def_,8):>12}   ratio {ratio:>12}", flush=True)
    prev = def_
print("   for reference   1/sqrt2 =", nstr(1/sqrt(2), 10))

print()
print("(b) identify d* = 2.639068871683003864638172")
d1 = mpf('2.639068871683003864638172')
print("   plain            :", identify(d1))
print("   with pi,sqrt2    :", identify(d1, ['pi','sqrt(2)']))
print("   with log2,e      :", identify(d1, ['log(2)','exp(1)']))
print("   with sqrt5,golden:", identify(d1, ['sqrt(5)','(1+sqrt(5))/2']))
print("   d*-2             :", nstr(d1-2, 20), " ->", identify(d1-2))
