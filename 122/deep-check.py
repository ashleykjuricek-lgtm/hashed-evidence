# 122: deeper run, self-contained. At level 16 the 2-adic Euler factors reach 2^(-4s'),
# so honest coefficients for d=8 can exceed 1000. 130 digits, coeffs <= 1e7
# (a 13-term basis needs ~91 digits to fake a relation). Same widened basis for every d.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".pylib"))
from mpmath import mp, mpf, quad, pi, exp, gamma, inf, nstr, zeta, sqrt, pslq
mp.dps = 130
K, M = 22, 500
th  = lambda t: 1 + 2*sum(exp(-pi*k*k*t) for k in range(1, K))
thh = lambda t: 2*sum(exp(-pi*(k+mpf(1)/2)**2*t) for k in range(0, K))
thc = lambda t: 1 + 2*sum((-1)**k*exp(-pi*k*k*t) for k in range(1, K))
s = -mpf(1)/2; pre = pi**(-s)*gamma(s)
cuts = [1, 2, 4, 8, 16, inf]
PPP = lambda d: (quad(lambda t: (t**(s-1) + t**(mpf(d)/2-s-1))*(th(t)**d - 1), cuts) - 1/s + 1/(s-mpf(d)/2)) / pre
APP = lambda d: (quad(lambda t: t**(s-1)*thh(t)*th(t)**(d-1) + t**(mpf(d)/2-s-1)*(thc(t)*th(t)**(d-1) - 1), cuts) + 1/(s-mpf(d)/2)) / pre
beta = lambda x: (zeta(x, mpf(1)/4) - zeta(x, mpf(3)/4)) / 4**x
D = lambda Z, d: -2*pi*Z * pi**(mpf(d+1)/2) / gamma(mpf(d+1)/2)
def eta_q(num, den=()):
    c = [0]*M; c[0] = 1
    for step, pw in num:
        for _ in range(pw):
            for n in range(step, M, step):
                for j in range(M-1, n-1, -1): c[j] -= c[j-n]
    for step, pw in den:
        for _ in range(pw):
            for n in range(step, M, step):
                for j in range(n, M): c[j] += c[j-n]
    return [0] + c[:M-1]
def Lval(a, k, N, sp):
    f = lambda y: sum(a[n]*exp(-2*pi*n*y/sqrt(N)) for n in range(1, M))
    direct = sum(a[n]*mpf(n)**(-sp) for n in range(1, M))
    cands = [quad(lambda y: f(y)*(y**(sp-1) + e*y**(k-1-sp)), [1, 3, inf]) / (N**(sp/2)*(2*pi)**(-sp)*gamma(sp)) for e in (1, -1)]
    return min(cands, key=lambda L: abs(L - direct))
g6 = eta_q([(4, 6)]); g8 = eta_q([(2, 4), (4, 4)]); g16 = eta_q([(4, 16)], [(2, 4), (8, 4)])
for d in (3, 4, 6, 7, 8):
    sp, h = mpf(d+1)/2, mpf(3)/2
    base = [zeta(sp)*zeta(h), beta(sp)*beta(h), zeta(sp)*beta(h), beta(sp)*zeta(h)]
    if d == 6: base += [Lval(g6, 3, 16, sp)]
    if d == 8: base += [Lval(g8, 4, 8, sp), Lval(g16, 4, 16, sp)]
    for name, Z in (("plain  ", PPP(d)), ("twisted", APP(d))):
        basis = [D(Z, d)] + base + [sqrt(2)*b for b in base]
        rel = pslq(basis, maxcoeff=10**7, maxsteps=10**7)
        if rel is None or rel[0] == 0: print(f"d={d} {name}: no relation (coeffs <= 1e7, 130 digits)", flush=True)
        else: print(f"d={d} {name}: CLOSES {rel}  residual {nstr(abs(sum(c*b for c, b in zip(rel, basis))), 3)}", flush=True)
