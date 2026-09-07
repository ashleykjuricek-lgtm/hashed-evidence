"""W1 receipts: the arrow attempt on the 1 x b x b family.

Independent fast Ewald implementation (numpy/scipy, float64) of the same object
v_landscape.py computes at mpmath dps 25:
    Z(s=-1/2; alpha; diag(1, 1/b^2, 1/b^2)) with alpha in {(0,0,0), (1/2,0,0)}
    eps(b) = 24 * Z_APP / Z_PPP - 1,   x = ln b.

Key simplification: with lam = 1 the tail quadrature is exact in closed form,
    integral_1^inf t^(s-1) e^(-E t) dt = E^(-s) * Gamma(s, E),
and for s = -1/2:  Gamma(-1/2, E) = 2 * (e^(-E)/sqrt(E) - sqrt(pi) * erfc(sqrt(E))),
while the dual side needs only Gamma(2, p) = (1 + p) e^(-p). Everything vectorizes.

Receipts produced (claims stated before running):
  R1  eps(1) reproduces the sealed eps_0 = 5.4595046537e-4 (and the CSV rows of the
      sealed instrument to its reduced precision).
  R2  in THIS chart eps has exactly ONE zero near the cube, at x* ~ +3e-5
      (the second zero recorded in 054 at b_0 = 0.99997 is then the OTHER chart's
      shadow: consistent with b_0 = 1/b* to the recorded digits).
  R3  slope: s_odd ~ -18.3; even curvature recovered from (eps(h)+eps(-h))/2 - eps_0
      ~ c2 * h^2 with c2 ~ 0.5826 (registry DRAIN_V_C2, sealed 096) -- an
      independent-method confirmation of the measured well.
  R4  the arrow identity: x* * |s_odd| / eps_0 = 1 + O(c2*x*/|s_odd|) -- the
      magnitude of the displacement is the invariant eps_0 over the chart slope.
"""

import numpy as np
from scipy.special import erfc
from scipy.optimize import brentq

SQPI = np.sqrt(np.pi)
GAMMA_MHALF = -2.0 * SQPI          # Gamma(-1/2)
N = 12                              # sum half-width (e^-144 ~ 1e-63: overkill)


def upper_gamma_mhalf(E):
    return 2.0 * (np.exp(-E) / np.sqrt(E) - SQPI * erfc(np.sqrt(E)))


def Z(b, app):
    """Z(s=-1/2) for diag(1, 1/b^2, 1/b^2), alpha=(1/2,0,0) if app else 0."""
    a = np.array([1.0, b ** -2, b ** -2])
    C = np.pi ** 1.5 / np.sqrt(a.prod())
    n = np.arange(-N, N + 1, dtype=float)
    # direct lattice: E_v = a1(n1+h)^2 + a2 n2^2 + a3 n3^2, h = 1/2 if app
    h = 0.5 if app else 0.0
    v1 = (n + h) ** 2 * a[0]
    v2 = n ** 2 * a[1]
    v3 = n ** 2 * a[2]
    E = (v1[:, None, None] + v2[None, :, None] + v3[None, None, :]).ravel()
    delta = 0 if app else 1
    if delta:
        E = E[E > 1e-12]                      # drop the origin (delta term)
    tail = np.sum(E ** 0.5 * upper_gamma_mhalf(E))
    # dual lattice: Rk = k1^2/a1 + k2^2/a2 + k3^2/a3, phase (-1)^k1 if app
    k = np.arange(-N, N + 1, dtype=float)
    r1 = k ** 2 / a[0]
    r2 = k ** 2 / a[1]
    r3 = k ** 2 / a[2]
    R = (r1[:, None, None] + r2[None, :, None] + r3[None, None, :])
    ph = ((-1.0) ** np.abs(k))[:, None, None] if app else 1.0
    P = np.pi ** 2 * R
    with np.errstate(divide="ignore", invalid="ignore"):
        dual_terms = np.where(R > 1e-12, ph * P ** -2.0 * (1.0 + P) * np.exp(-P), 0.0)
    dual = C * dual_terms.sum()
    total = tail + C / (-2.0) + dual
    if delta:
        total += 2.0                          # -lam^s/s = -(1/(-1/2)) = +2
    return total / GAMMA_MHALF


def eps(x):
    b = float(np.exp(x))
    return 24.0 * Z(b, True) / Z(b, False) - 1.0


if __name__ == "__main__":
    ok = True
    # R1: the cube, vs the sealed value
    e0 = eps(0.0)
    sealed = 5.4595046537e-4
    print(f"R1  eps(0) = {e0:.12e}   sealed 5.4595046537e-4   "
          f"rel diff {abs(e0 - sealed) / sealed:.2e}")
    ok &= abs(e0 - sealed) / sealed < 1e-6
    # R1b: three rows of the sealed instrument's CSV (dps-25, reduced widths)
    for b_csv, e_csv in [(0.97, 0.5592716800484088),
                         (0.999, 0.018881667272714404),
                         (1.01, -0.18174558779507358)]:
        e_here = eps(np.log(b_csv))
        print(f"R1b eps(ln {b_csv}) = {e_here:+.12f}   csv {e_csv:+.12f}   "
              f"diff {abs(e_here - e_csv):.2e}")
        ok &= abs(e_here - e_csv) < 1e-8
    # R2: sample the neighbourhood; count sign changes in each half
    xs = [-1e-4, -3e-5, -1e-5, -3e-6, 0.0, 3e-6, 1e-5, 3e-5, 1e-4]
    print("R2  neighbourhood of the cube:")
    vals = {}
    for x in xs:
        vals[x] = eps(x)
        print(f"      x = {x:+.1e}   eps = {vals[x]:+.6e}")
    left_change = any(vals[a] * vals[b] < 0 for a, b in
                      [(-1e-4, -3e-5), (-3e-5, -1e-5), (-1e-5, -3e-6)])
    print(f"      sign change on the LEFT half? {left_change}")
    x_star = brentq(eps, 1e-6, 1e-4, xtol=1e-15)
    print(f"R2  single zero in this chart at x* = {x_star:.10e}  "
          f"(b* = {np.exp(x_star):.10f});  054 recorded b* = 1.0000298")
    print(f"      1/b* = {np.exp(-x_star):.10f};  054 recorded b0 = 0.99997")
    # R3: odd slope and even curvature (independent well check)
    for hh in (1e-4, 3e-4):
        s_odd = (eps(hh) - eps(-hh)) / (2 * hh)
        c2_est = ((eps(hh) + eps(-hh)) / 2 - e0) / hh ** 2
        print(f"R3  h = {hh:.0e}: s_odd = {s_odd:+.6f}   even-curvature "
              f"estimate = {c2_est:+.6f}   (registry c2 = +0.58260865)")
    s_odd = (eps(1e-4) - eps(-1e-4)) / (2e-4)
    # R4: the arrow identity
    ratio = x_star * abs(s_odd) / e0
    pred_corr = 0.58260865 * x_star / abs(s_odd)
    print(f"R4  x* * |s_odd| / eps_0 = {ratio:.8f}   "
          f"(1 + predicted well correction ~ {1 + pred_corr:.8f})")
    print("OVERALL:", "PASS" if ok else "CHECK FAILURES ABOVE")
