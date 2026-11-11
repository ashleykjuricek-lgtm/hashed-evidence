# 121: plain (PPP) and twisted (APP) Casimir-type energies Z(-1/2) with dimension d as a
# continuous dial. Defined by Theta(t) = theta(t)^d (1-D theta functions, real power),
# Mellin split at t=1; agrees with the lattice sums at integer d (checked below).
import sys; sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__file__), ".pylib"))
from mpmath import mp, mpf, quad, pi, exp, gamma, findroot, inf, nstr
mp.dps = 20
K = 12
th   = lambda t: 1 + 2*sum(exp(-pi*k*k*t) for k in range(1, K))
thh  = lambda t: 2*sum(exp(-pi*(k+mpf(1)/2)**2*t) for k in range(0, K))
thc  = lambda t: 1 + 2*sum((-1)**k*exp(-pi*k*k*t) for k in range(1, K))
s = -mpf(1)/2
def pre(): return pi**(-s)*gamma(s)
def PPP(d):
    f = lambda t: (t**(s-1) + t**(d/2-s-1))*(th(t)**d - 1)
    return (quad(f, [1, 4, inf]) - 1/s + 1/(s-d/2)) / pre()
def APP(d):
    f = lambda t: t**(s-1)*thh(t)*th(t)**(d-1) + t**(d/2-s-1)*(thc(t)*th(t)**(d-1) - 1)
    return (quad(f, [1, 4, inf]) + 1/(s-d/2)) / pre()
print("integer check (lattice values: d=3 APP -0.0111142428, PPP -0.2665962787)")
for d in (1, 2, 3, 4):
    a, p = APP(mpf(d)), PPP(mpf(d))
    print(f"  d={d}  APP={nstr(a,10)}  PPP={nstr(p,10)}  R={nstr(a/p,10)}")
print("scan")
for d in [x/mpf(4) for x in range(2, 25)]:
    a, p = APP(d), PPP(d)
    print(f"  d={nstr(d,4):>5}  APP={nstr(a,8):>12}  R={nstr(a/p,8)}")
dstar = findroot(APP, mpf("2.9"))
print("crossover d* (twisted energy = 0):", nstr(dstar, 15))
print("3 - d* =", nstr(3 - dstar, 10))
# where does R = 1/24 exactly?
d24 = findroot(lambda d: 24*APP(d) - PPP(d), mpf(3))
print("d where R = 1/24 exactly:", nstr(d24, 15), "  3 - d =", nstr(3-d24, 8))
