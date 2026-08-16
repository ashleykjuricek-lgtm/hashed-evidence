"""
Independent check of R = Z_APP(-1/2) / Z_PPP(-1/2) on the cubic 3-torus.

Route: completed-zeta theta integrals with modular reflection (NOT the paper's
Ewald/Chowla-Selberg route, so it's an independent verification).

  PPP: Theta(t) = theta3(e^{-pi t})^3,  zero mode excluded
       pi^{-s}Gamma(s) Z(s) = int_1^inf (Theta-1)(t^{s-1}+t^{1/2-s})dt + 1/(s-3/2) - 1/s
  APP: Theta(t) = theta2 * theta3^2   (alpha=(1/2,0,0): n1 -> n1+1/2, no zero mode)
       dual side via theta2(i/t) = sqrt(t) theta4(it):
       pi^{-s}Gamma(s) Z(s) = int_1^inf Theta_APP t^{s-1} dt
                            + int_1^inf (theta4*theta3^2 - 1) t^{1/2-s} dt + 1/(s-3/2)

Adjudicates: old draft R = 0.041689414162...  vs audit R = 0.04168941460272377512...
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
from mpmath import mp, mpf, quad, exp, pi, gamma, jtheta, inf

mp.dps = 40
s = mpf(-1) / 2
h = mpf(1) / 2


def q_(t):
    return exp(-pi * t)


T_ppp = lambda t: jtheta(3, 0, q_(t)) ** 3
T_app = lambda t: jtheta(2, 0, q_(t)) * jtheta(3, 0, q_(t)) ** 2
T_app_dual = lambda t: jtheta(4, 0, q_(t)) * jtheta(3, 0, q_(t)) ** 2

I_ppp = quad(lambda t: (T_ppp(t) - 1) * (t ** (s - 1) + t ** (h - s)), [1, inf])
Lam_ppp = I_ppp + 1 / (s - mpf(3) / 2) - 1 / s
Z_ppp = pi ** s / gamma(s) * Lam_ppp

I_app = quad(lambda t: T_app(t) * t ** (s - 1), [1, inf])
I_app_d = quad(lambda t: (T_app_dual(t) - 1) * t ** (h - s), [1, inf])
Lam_app = I_app + I_app_d + 1 / (s - mpf(3) / 2)
Z_app = pi ** s / gamma(s) * Lam_app

R = Z_app / Z_ppp
print(f"Z_PPP(-1/2) = {Z_ppp}")
print(f"Z_APP(-1/2) = {Z_app}")
print(f"R           = {R}")
print(f"1/24        = {mpf(1)/24}")
print()
old = mpf("0.041689414162")
new = mpf("0.04168941460272377512")
print(f"|R - old draft value| = {abs(R - old)}")
print(f"|R - audited value|   = {abs(R - new)}")
print("VERDICT:", "AUDIT value confirmed" if abs(R - new) < abs(R - old) else "OLD value confirmed")
