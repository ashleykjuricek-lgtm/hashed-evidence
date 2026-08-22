"""F8 turned on 039 itself.

039 §1.2 proved: the doubling identity r2(2m)=r2(m) has no analogue in d=3, so the
Euler-factor ROUTE to a Q[sqrt2] ratio is unavailable. It then wrote 'no ratio in
Q[sqrt2] is available' and tabled it as PROVED. Those are different claims. The
first is about a method. The second is about the object. Test the second.
"""
import fractional
from mpmath import mp, mpf, pslq, nstr, sqrt, identify

def R(d, j, dps, N, K):
    mp.dps = dps
    return fractional.Z(d, j, N=N, K=K)/fractional.Z(d, 0, N=N, K=K)

print("convergence of R(3,3) and R(3,1):")
vals = {}
for dps, N, K in [(30, 26, 12), (45, 40, 18), (60, 52, 24)]:
    r33, r31 = R(3,3,dps,N,K), R(3,1,dps,N,K)
    vals[dps] = (r33, r31)
    print(f"  dps={dps:3d}  R(3,3) = {nstr(r33, dps-6)}")
    print(f"            R(3,1) = {nstr(r31, dps-6)}")

print()
print("="*70)
print("IS R(3,3) OR R(3,1) IN Q[sqrt2]?  (the claim 039 tabled as PROVED)")
print("A 3-term relation with coefficients <= C needs ~3*log10(C) digits.")
print("We hold 50 verified digits, so C <= 1e16 is honest.")
print()
mp.dps = 60
R33 = mpf('-0.233673480267327105342114867705294349266650924956100769')
R31 = mpf('0.0416894146027237751200791895411477959451762762538280901')
s2  = sqrt(2)
for name, x in [("R(3,3)", R33), ("R(3,1)", R31)]:
    print(f"  {name} = {nstr(x, 50)}")
    for C in [10**6, 10**10, 10**16]:
        need = 3*len(str(C))
        r = pslq([x, mpf(1), s2], maxcoeff=C, maxsteps=10**6)
        print(f"      a*x + b + c*sqrt2 = 0,  coeff <= {C:>18}: {r}   (needs ~{need} digits, have 50)")
    for n, C in [(2, 10**16), (3, 10**12), (4, 10**9), (6, 10**7)]:
        need = (n+1)*len(str(C))
        if need > 50:
            print(f"      algebraic degree <= {n}, coeff <= {C}: SKIPPED (needs ~{need})"); continue
        r = pslq([x**k for k in range(n+1)], maxcoeff=C, maxsteps=10**6)
        print(f"      algebraic degree <= {n}, coeff <= {C:>14}: {r}   (needs ~{need} digits)")
    print()
print("also: is 24*R(3,1) - 1  (= epsilon) anything?")
eps = 24*R31 - 1
print("   eps =", nstr(eps, 45))
for C in [10**8, 10**14]:
    print(f"   in Q[sqrt2], coeff <= {C:>16}:", pslq([eps, mpf(1), s2], maxcoeff=C, maxsteps=10**6))
