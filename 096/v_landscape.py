"""V(Theta) from modular structure, step 1: COMPUTE the landscape, assume nothing.

Ports (not retypes) the sealed anisotropic Epstein machinery from
hashed-evidence/032/epstein_aniso_check.py (independent Ewald implementation,
validated at the cube against the canonical constants). Family: the
1 x b x b torus, alpha_APP = (1/2, 0, 0).

Question: as a function of the shape modulus b, what do the candidate
potentials actually look like near the cube?
  - Z_APP(b)  (the antiperiodic vacuum energy — the physical candidate)
  - Z_PPP(b)
  - eps(b) = 24 Z_APP/Z_PPP - 1   (sealed slope data exists: C1 in 054 —
    zeros at b0=0.99997 and b*=1.0000298 with slopes +-18.3, which brackets
    a sharp EXTREMUM near b=1; sign to be determined by this computation)

ROAD stratum. Output: v_landscape.csv + v_landscape.png. Reduced precision
(dps 25, sum widths 10) — landscape shape, not certified digits.
"""
from __future__ import annotations

import csv
import os

from mpmath import mp, mpf, exp, sqrt, pi, gamma, gammainc, quad

mp.dps = 25
LAM = mpf(1)
NDIR = 10
NDUAL = 10


def zeta_aniso(b, alpha, s=mpf(-0.5), lam=LAM, ndir=NDIR, ndual=NDUAL):
    b = mpf(b)
    a = [mpf(1), 1 / b ** 2, 1 / b ** 2]
    a1, a2, a3 = a
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


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    # dense near the cube (the sealed slope data lives within 3e-5 of b=1),
    # sparse further out for the global shape
    bs = ([1 - 3e-2, 1 - 1e-2, 1 - 3e-3, 1 - 1e-3, 1 - 3e-4, 1 - 1e-4,
           1 - 3e-5, 1.0, 1 + 3e-5, 1 + 1e-4, 1 + 3e-4, 1 + 1e-3,
           1 + 3e-3, 1 + 1e-2, 1 + 3e-2])
    rows = []
    for b in bs:
        P = zeta_aniso(b, [mpf(0), mpf(0), mpf(0)])
        A = zeta_aniso(b, [mpf(0.5), mpf(0), mpf(0)])
        e = 24 * A / P - 1
        rows.append((float(b), float(P), float(A), float(e)))
        print(f"b={b:.6f}  Z_PPP={float(P):+.10f}  Z_APP={float(A):+.10f}  "
              f"eps={float(e):+.6e}", flush=True)

    with open(os.path.join(here, "v_landscape.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["b", "Z_PPP", "Z_APP", "eps"])
        w.writerows(rows)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    arr = np.array(rows)
    x = np.log(arr[:, 0])
    fig, ax = plt.subplots(1, 3, figsize=(14, 4))
    fig.suptitle("Candidate V landscapes on the 1 x b x b family (x = ln b) — computed, not chosen")
    ax[0].plot(x, arr[:, 2], "o-"); ax[0].set_title("Z_APP(x)  (vacuum energy)")
    ax[1].plot(x, arr[:, 3], "o-"); ax[1].set_title("eps(x)")
    ax[1].axhline(0, ls=":", lw=1)
    ax[2].plot(x, arr[:, 1], "o-"); ax[2].set_title("Z_PPP(x)")
    for a_ in ax:
        a_.grid(alpha=0.3); a_.set_xlabel("x = ln b")
    fig.tight_layout()
    fig.savefig(os.path.join(here, "v_landscape.png"), dpi=120)
    print("wrote v_landscape.csv / v_landscape.png")


if __name__ == "__main__":
    main()
