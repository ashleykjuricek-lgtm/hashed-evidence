"""Where the sign change actually is, once whole numbers stop being a requirement."""
from mpmath import mp
mp.dps = 15
from fractional import Z
from mpmath import mpf, findroot, nstr

print("the crossing d* where Z(d, j) = 0, for j marked circles:")
print("    j            d*                    d* - 2j")
roots = {}
for j in range(1, 7):
    f = lambda d: Z(d, j, N=12, K=4)
    r = findroot(f, (mpf(2*j)+mpf('0.2'), mpf(2*j)+mpf('0.8')), solver='secant', tol=mpf(10)**-16)
    roots[j] = r
    print(f"   {j:2d}   {nstr(r,12):>18}   {nstr(r-2*j,12):>18}", flush=True)
