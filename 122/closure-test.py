# 122: does the twisted/plain ratio close up in d = 1..8?
# R_d = Z_APP(-1/2)/Z_PPP(-1/2) on Z^d (twist on one axis), Mellin split at t=1 (as 121).
# Mirror (120, any d): Z(-1/2) = -pi^(-s') Gamma(s') D(s') / (2 pi), s' = (d+1)/2,
# D = Dirichlet series of the lattice (plain: sum r_d(n) n^-s; twisted: signed (-1)^k1).
# Closure test: PSLQ D(s') against {1, sqrt2} x {zeta,beta}(s') x {zeta,beta}(3/2).
# (s' - d/2 + 1 = 3/2 for every d: the second Eisenstein argument.)
# A relation = "closed form in the Eisenstein shape". No relation = not in this shape.
# Basis order: [D, zz, bb, zb, bz, r2*zz, r2*bb, r2*zb, r2*bz]  (z=zeta, b=beta, first arg s', second 3/2)
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".pylib"))
from mpmath import mp, mpf, quad, pi, exp, gamma, inf, nstr, zeta, sqrt, pslq
mp.dps = 60
K = 14
th  = lambda t: 1 + 2*sum(exp(-pi*k*k*t) for k in range(1, K))
thh = lambda t: 2*sum(exp(-pi*(k+mpf(1)/2)**2*t) for k in range(0, K))
thc = lambda t: 1 + 2*sum((-1)**k*exp(-pi*k*k*t) for k in range(1, K))
s = -mpf(1)/2
pre = pi**(-s)*gamma(s)
def PPP(d):
    f = lambda t: (t**(s-1) + t**(mpf(d)/2-s-1))*(th(t)**d - 1)
    return (quad(f, [1, 2, 4, 8, inf]) - 1/s + 1/(s-mpf(d)/2)) / pre
def APP(d):
    f = lambda t: t**(s-1)*thh(t)*th(t)**(d-1) + t**(mpf(d)/2-s-1)*(thc(t)*th(t)**(d-1) - 1)
    return (quad(f, [1, 2, 4, 8, inf]) + 1/(s-mpf(d)/2)) / pre
beta = lambda x: (zeta(x, mpf(1)/4) - zeta(x, mpf(3)/4)) / 4**x
def D(Z, d):
    sp = mpf(d+1)/2
    return -2*pi*Z * pi**sp / gamma(sp)
def closes(val, d):
    sp = mpf(d+1)/2; h = mpf(3)/2
    P = [zeta(sp)*zeta(h), beta(sp)*beta(h), zeta(sp)*beta(h), beta(sp)*zeta(h)]
    if d == 2: P = P[:3]  # s' = 3/2 = h: the two mixed products coincide
    basis = [val] + P + [sqrt(2)*p for p in P]
    # small coefficients only: at 60 digits a 9-term basis with coeffs ~1e6 fits anything
    rel = pslq(basis, maxcoeff=1000, maxsteps=10**6)
    if rel is None or rel[0] == 0: return "no relation (coeff <= 1000)"
    resid = abs(sum(c*b for c, b in zip(rel, basis)))
    return f"CLOSES: {rel}  residual {nstr(resid, 3)}"
print("d=3 check: R should be 0.0416894146027237751...")
for d in range(2, 9):  # d=1 is 2*zeta(2s), trivially closed; Eisenstein shape starts at d=2
    a, p = APP(d), PPP(d)
    print(f"\nd={d}  R={nstr(a/p, 25)}")
    print("  plain   D:", closes(D(p, d), d))
    print("  twisted D:", closes(D(a, d), d))
