"""Where does eps(b) actually vanish, and how steep is it there?
Both from the exact anisotropic Epstein sum. No fit anywhere."""
import anisotropic
from mpmath import mp, mpf, findroot, diff, nstr
mp.dps = 25
A, P = mpf(1)/2, mpf(0)

def eps(b):
    b = mpf(b)
    return 24*anisotropic.Z([1,b,b], [A,P,P])/anisotropic.Z([1,b,b], [P,P,P]) - 1

print("eps(1) =", nstr(eps(1), 18), "   <- the cube is NOT on the zero")
print()
bstar = findroot(eps, (mpf('1.00001'), mpf('1.0001')), solver='secant', tol=mpf(10)**-20)
print("the zero of eps:")
print("   b* =", nstr(bstar, 20))
print("   b* - 1 =", nstr(bstar-1, 12))
print("   eps(b*) =", nstr(eps(bstar), 6))
print()
d = diff(eps, mpf(1))
print("slope at the cube, d eps / db |_(b=1) =", nstr(d, 15))
print("   linear estimate of the root: 1 +", nstr(-eps(1)/d, 12), "=", nstr(1 - eps(1)/d, 18))
print()
print("so the cube misses the exact zero by a relative", nstr(100*(bstar-1), 6), "percent")
