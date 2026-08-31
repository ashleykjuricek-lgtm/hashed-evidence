"""Verify the exact shift<->character functional equation (097 section 2).

Route A (this file): evaluate the RHS of
    Gamma(s) Z_sh(s;b) = I_direct + b^2 pi^{2s-3/2} I_dual + b^2 pi^s/(s-3/2)
by direct theta sums and quadrature on [pi, inf).

Route B (independent): Z_sh(s;b) from the Ewald implementation ported from
sealed 032/epstein_aniso_check.py (different split, different code path).

Also: the master theta identity (097 section 1) checked pointwise.
"""
from __future__ import annotations

from mpmath import mp, mpf, exp, sqrt, pi, gamma, gammainc, quad

mp.dps = 30
N = 14  # 1D theta sum half-width (Gaussian decay: ample at t >= pi/2)


def _s0(x):
    """sum_n exp(-x n^2)  (1D, unshifted)."""
    return 1 + 2 * sum(exp(-x * n * n) for n in range(1, N + 1))


def _sh(x):
    """sum_n exp(-x (n+1/2)^2)  (1D, half-shifted)."""
    return 2 * sum(exp(-x * (n + mpf(1) / 2) ** 2) for n in range(0, N + 1))


def _sc(x):
    """sum_n (-1)^n exp(-x n^2)  (1D, character)."""
    return 1 + 2 * sum((-1) ** n * exp(-x * n * n) for n in range(1, N + 1))


def theta_sh(t, b):
    # diagonal form factorizes: (n1+1/2)^2 + (n2^2+n3^2)/b^2
    b = mpf(b)
    return _sh(t) * _s0(t / b ** 2) ** 2


def theta_ch(u, c):
    # character sum on the (1, c, c)-torus form: k1^2 + (k2^2+k3^2)/c^2
    c = mpf(c)
    return _sc(u) * _s0(u / c ** 2) ** 2


def rhs_gamma_Zsh(s, b):
    s, b = mpf(s), mpf(b)
    I_direct = quad(lambda t: t ** (s - 1) * theta_sh(t, b), [pi, 8, mp.inf])
    # section 2: integral of u^{1/2 - s} [Theta_ch - 1] du, exactly as stated
    I_dual = quad(lambda u: u ** (mpf(1) / 2 - s) * (theta_ch(u, 1 / b) - 1), [pi, 8, mp.inf])
    return I_direct + b ** 2 * pi ** (2 * s - mpf(3) / 2) * I_dual + b ** 2 * pi ** s / (s - mpf(3) / 2)


# ---- Route B: independent Ewald (ported from sealed 032) ----

def zeta_aniso(b, alpha, s=mpf(-0.5), lam=mpf(1), ndir=12, ndual=12):
    b = mpf(b)
    a1, a2, a3 = mpf(1), 1 / b ** 2, 1 / b ** 2
    C = pi ** mpf(1.5) / sqrt(a1 * a2 * a3)
    delta = 1 if all(x == 0 for x in alpha) else 0

    def Theta(t):
        # diagonal + our alpha patterns only: factorized 1D sums
        f1 = _sh(t * a1) if alpha[0] == mpf(0.5) else _s0(t * a1)
        return f1 * _s0(t * a2) * _s0(t * a3)

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


def main():
    print("=== master theta identity, pointwise (section 1) ===")
    for (t, b) in [(mpf("0.7"), mpf("1.3")), (mpf("1.9"), mpf("0.8")), (pi, mpf("1.1"))]:
        lhs = theta_sh(t, b)
        rhs = (pi / t) ** mpf(1.5) * b ** 2 * theta_ch(pi ** 2 / t, 1 / b)
        print(f"t={float(t):.4f} b={float(b):.2f}  |LHS-RHS| = {mp.nstr(abs(lhs - rhs), 5)}")

    print("\n=== completed equation at s=-1/2 vs independent Ewald (section 2) ===")
    s = mpf("-0.5")
    for b in [mpf(1), mpf("1.01"), mpf("0.97"), mpf("1.2")]:
        routeA = rhs_gamma_Zsh(s, b) / gamma(s)
        routeB = zeta_aniso(b, [mpf(0.5), mpf(0), mpf(0)], s=s)
        print(f"b={float(b):.2f}  routeA={mp.nstr(routeA, 18)}  "
              f"routeB={mp.nstr(routeB, 18)}  |diff|={mp.nstr(abs(routeA - routeB), 5)}")

    print("\n=== and at a second argument, s = 0.4 (the equation is all-s) ===")
    s = mpf("0.4")
    for b in [mpf("1.05")]:
        routeA = rhs_gamma_Zsh(s, b) / gamma(s)
        routeB = zeta_aniso(b, [mpf(0.5), mpf(0), mpf(0)], s=s)
        print(f"b={float(b):.2f}  routeA={mp.nstr(routeA, 18)}  "
              f"routeB={mp.nstr(routeB, 18)}  |diff|={mp.nstr(abs(routeA - routeB), 5)}")


if __name__ == "__main__":
    main()
