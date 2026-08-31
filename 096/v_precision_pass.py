"""Precision pass on the drain potential: V(x) = even part of eps about the cube.

Family: 1 x b x b torus, alpha_APP = (1/2,0,0); x = ln b. Machinery ported
from sealed 032/epstein_aniso_check.py (independent Ewald implementation,
validated at the cube). Settings raised from the landscape probe
(dps 25 / widths 10) to dps 35 / widths 12; agreement between the two
settings is the numerical-stability check.

Measured objects, symmetric pairs x = +-h:
    even(h) = [eps(e^h) + eps(e^-h)] / 2      -> V
    odd(h)  = [eps(e^h) - eps(e^-h)] / (2h)   -> chart-dependent slope
    c2(h)   = (even(h) - eps0) / h^2          -> stiffness estimate
Richardson: with even = eps0 + c2 h^2 + c4 h^4, pairs of h give c2, c4.

NOTE (kept from the working session): even(h) -> eps0 as h -> 0 is
CONTINUITY, not a finding. The findings are the dominance of the odd part,
the stability of c2 across two decades, and the smallness of c4 h^2 within
the fitted window.
"""
from __future__ import annotations

from mpmath import mp, mpf, exp, sqrt, pi, gamma, gammainc, quad

mp.dps = 35
LAM = mpf(1)
NDIR = 12
NDUAL = 12


def zeta_aniso(b, alpha, s=mpf(-0.5), lam=LAM, ndir=NDIR, ndual=NDUAL):
    b = mpf(b)
    a1, a2, a3 = mpf(1), 1 / b ** 2, 1 / b ** 2
    C = pi ** mpf(1.5) / sqrt(a1 * a2 * a3)
    delta = 1 if all(x == 0 for x in alpha) else 0

    def Theta(t):
        tot = mpf(0)
        for n1 in range(-ndir, ndir + 1):
            v1 = n1 + alpha[0]
            e1 = a1 * v1 * v1
            for n2 in range(-ndir, ndir + 1):
                v2 = n2 + alpha[1]
                e2 = e1 + a2 * v2 * v2
                for n3 in range(-ndir, ndir + 1):
                    v3 = n3 + alpha[2]
                    tot += exp(-t * (e2 + a3 * v3 * v3))
        return tot

    tail = quad(lambda t: t ** (s - 1) * (Theta(t) - delta), [lam, mp.inf])
    c = mpf(1.5) - s
    dual = mpf(0)
    for k1 in range(-ndual, ndual + 1):
        for k2 in range(-ndual, ndual + 1):
            for k3 in range(-ndual, ndual + 1):
                if k1 == 0 and k2 == 0 and k3 == 0:
                    continue
                Rk = k1 * k1 / a1 + k2 * k2 / a2 + k3 * k3 / a3
                p = pi ** 2 * Rk
                phase = (-1) ** k1 if alpha[0] == mpf(0.5) else 1
                dual += phase * p ** (-c) * gammainc(c, p / lam)
    dual *= C
    total = tail + C * lam ** (s - mpf(1.5)) / (s - mpf(1.5)) + dual
    if delta:
        total -= lam ** s / s
    return total / gamma(s)


def eps(b):
    P = zeta_aniso(b, [mpf(0), mpf(0), mpf(0)])
    A = zeta_aniso(b, [mpf(0.5), mpf(0), mpf(0)])
    return 24 * A / P - 1


def main():
    e0 = eps(1)
    print(f"eps0 = eps(1) = {mp.nstr(e0, 15)}")
    print(f"  sealed ref  = 0.00054595046537060288190...")

    hs = [mpf("0.001"), mpf("0.003"), mpf("0.01")]
    evens, odds = {}, {}
    for h in hs:
        bp, bm = exp(h), exp(-h)
        ep_, em_ = eps(bp), eps(bm)
        ev = (ep_ + em_) / 2
        od = (ep_ - em_) / (2 * h)
        evens[h], odds[h] = ev, od
        c2 = (ev - e0) / h ** 2
        print(f"h={float(h):7.4f}  even={mp.nstr(ev, 12)}  odd-slope={mp.nstr(od, 10)}  "
              f"c2(h)={mp.nstr(c2, 10)}", flush=True)

    # Richardson from (h1, h2): even = e0 + c2 h^2 + c4 h^4
    for (h1, h2) in [(hs[0], hs[1]), (hs[1], hs[2]), (hs[0], hs[2])]:
        y1, y2 = evens[h1] - e0, evens[h2] - e0
        c4 = (y2 / h2 ** 2 - y1 / h1 ** 2) / (h2 ** 2 - h1 ** 2)
        c2 = y1 / h1 ** 2 - c4 * h1 ** 2
        print(f"pair h=({float(h1)},{float(h2)}):  c2 = {mp.nstr(c2, 10)}   "
              f"c4 = {mp.nstr(c4, 8)}")

    print("\nodd-slope at h->0 vs sealed C1 slope magnitude 18.3:")
    for h in hs:
        print(f"  h={float(h):7.4f}: {mp.nstr(odds[h], 10)}")


if __name__ == "__main__":
    main()
