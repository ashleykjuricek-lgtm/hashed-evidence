# 122: the even-d twisted failures (d = 6, 8). Hypothesis: a cusp form enters.
# Add L(g, s') for the obvious level-16/8 cusp form and retry PSLQ (coeffs <= 1000).
#   d=6: g = eta(4z)^6         weight 3, level 16, character chi_-4 (CM by Q(i))
#   d=8: g = eta(2z)^4 eta(4z)^4  weight 4, level 8
# L(g,s) by the Mellin integral split at the Fricke-fixed point, sign fixed against a direct sum.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".pylib"))
from mpmath import mp, mpf, quad, pi, exp, gamma, inf, nstr, zeta, sqrt, pslq
exec(open(os.path.join(os.path.dirname(__file__), "closure-test.py")).read().split("print(\"d=3 check")[0])
M = 400
def qser(factors):  # factors: list of (step, power) for prod (1-q^(step n))^power, times q
    c = [0]*M; c[0] = 1
    for step, pw in factors:
        for _ in range(pw):
            for n in range(step, M, step):
                for j in range(M-1, n-1, -1): c[j] -= c[j-n]
    return [0] + c[:M-1]  # shift by q^1
def Lval(a, k, N, sp):
    f = lambda y: sum(a[n]*exp(-2*pi*n*y/sqrt(N)) for n in range(1, M))
    I = lambda e: quad(lambda y: f(y)*(y**(sp-1) + e*y**(k-1-sp)), [1, 3, inf])
    direct = sum(a[n]*mpf(n)**(-sp) for n in range(1, M))
    best = None
    for e in (1, -1):
        L = I(e) / (N**(sp/2)*(2*pi)**(-sp)*gamma(sp))
        if best is None or abs(L-direct) < abs(best-direct): best = L
    return best, direct
for d, fac, k, N in [(6, [(4, 6)], 3, 16), (8, [(2, 4), (4, 4)], 4, 8)]:
    sp = mpf(d+1)/2; h = mpf(3)/2
    a = qser(fac)
    L, direct = Lval(a, k, N, sp)
    print(f"d={d}  L(g,{sp}) = {nstr(L, 30)}   (direct sum, {M} terms: {nstr(direct, 12)})")
    Dt = D(APP(d), d)
    P = [zeta(sp)*zeta(h), beta(sp)*beta(h), zeta(sp)*beta(h), beta(sp)*zeta(h)]
    basis = [Dt] + P + [sqrt(2)*p for p in P] + [L, sqrt(2)*L]
    rel = pslq(basis, maxcoeff=1000, maxsteps=10**6)
    if rel is None or rel[0] == 0: print("   twisted D: still no relation"); continue
    print("   twisted D: CLOSES with cusp term:", rel, " residual", nstr(abs(sum(c*b for c, b in zip(rel, basis))), 3))
# d=8 retry: add the level-16 newform g16 = eta(4z)^16 / (eta(2z)^4 eta(8z)^4), weight 4.
def qser_q(num, den):  # eta-quotient, q^1 leading, num/den: list of (step, power)
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
d, sp, h = 8, mpf(9)/2, mpf(3)/2
L8, _ = Lval(qser([(2, 4), (4, 4)]), 4, 8, sp)
L16, dir16 = Lval(qser_q([(4, 16)], [(2, 4), (8, 4)]), 4, 16, sp)
print(f"d=8  L(g16,4.5) = {nstr(L16, 30)}   (direct: {nstr(dir16, 12)})")
Dt = D(APP(d), d)
P = [zeta(sp)*zeta(h), beta(sp)*beta(h), zeta(sp)*beta(h), beta(sp)*zeta(h)]
basis = [Dt] + P + [sqrt(2)*p for p in P] + [L8, sqrt(2)*L8, L16, sqrt(2)*L16]
rel = pslq(basis, maxcoeff=1000, maxsteps=10**6)
if rel is None or rel[0] == 0: print("   twisted D (with g8, g16): still no relation")
else: print("   twisted D: CLOSES with cusp terms:", rel, " residual", nstr(abs(sum(c*b for c, b in zip(rel, basis))), 3))
