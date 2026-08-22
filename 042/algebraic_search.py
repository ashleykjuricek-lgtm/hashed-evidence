"""An HONEST algebraic search, replacing the 24-digit version.

Rule used: a relation among n+1 terms with coefficients up to C is only meaningful
if you hold roughly (n+1)*log10(C) digits. Below that PSLQ fits noise and always
succeeds -- which is exactly how this programme once produced a beautiful closed
form for a 3.4% quadrature bug. Each test below states its digit requirement and
is run only when the requirement is met.
"""
from mpmath import mp, mpf, pslq, identify, nstr, pi, sqrt, log, e
mp.dps = 45
# 40 digits, agreeing across dps=40/55 independent runs
d1 = mpf('2.639068871683003864638172449745923136866')
DIGITS = 40
print(f"d* to {DIGITS} verified digits = {nstr(d1, DIGITS)}")
print()
print("algebraic degree tests (need (n+1)*log10(C) digits to be meaningful):")
for n, C in [(2, 10**12), (3, 10**8), (4, 10**6), (5, 10**5), (6, 10**4), (8, 10**3)]:
    need = (n+1)*len(str(C))
    ok = need <= DIGITS
    if not ok:
        print(f"   degree <= {n}, coeff <= {C:>12}:  SKIPPED (needs ~{need} digits, have {DIGITS})")
        continue
    r = pslq([d1**k for k in range(n+1)], maxcoeff=C, maxsteps=10**6)
    print(f"   degree <= {n}, coeff <= {C:>12}:  {r}   (needs ~{need} digits, have {DIGITS})")
print()
print("PSLQ against constants, coeff <= 10^5 (4 terms -> needs ~20 digits):")
for name, cs in {"pi":[pi], "sqrt2":[sqrt(2)], "log2":[log(2)], "e":[e],
                 "pi,sqrt2":[pi,sqrt(2)], "pi,log2":[pi,log(2)]}.items():
    r = pslq([d1, mpf(1)] + list(cs), maxcoeff=10**5, maxsteps=10**6)
    print(f"   {name:>10}: {r}")
print()
print("identify, large basis:", identify(d1, ['pi','sqrt(2)','sqrt(3)','sqrt(5)','log(2)','exp(1)']))
