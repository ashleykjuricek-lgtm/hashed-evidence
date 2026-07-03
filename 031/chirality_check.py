"""
IS THE 1° REAL? — chirality check on the forward/backward swept-angle gap
========================================================================
watch_the_clock gave forward -534.8°, backward +535.6°  → gap = +0.8°.
Claim under test: this is an inherent chirality ("commutator leak / traction").

Mechanism check (analytic): under a mirror M through a plane containing the axis,
S->S and K->-K, so O_bwd = M O_fwd M^-1. Hence for a mirror-symmetric patch AND a
mirror-symmetric start, forward and backward are EXACT mirrors even though [S,K]!=0.
So a nonzero commutator does NOT force the gap. The gap should come from the start
bump being a single off-axis node (not mirror-symmetric) and/or finite-patch effects.

Test: run fwd+bwd from MANY starting nodes, at two patch sizes. Per node,
gap = swept_fwd + swept_bwd  (0 = perfect mirror).
  - scatters ~0 (both signs) & shrinks with size  -> artifact, no inherent chirality
  - systematically one sign & stable             -> real handedness, chase it
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
from numpy.linalg import norm
from scipy.linalg import expm
from tier1 import (PHI, LATTICE_R, K_NEIGHBORS, ALPHA,
                   make_cut_and_project, build_graph, build_operators)

TS = np.linspace(0, 2.5, 140)


def perp_frame(axis):
    a = axis / norm(axis)
    v = np.array([1.0, 0, 0]) if abs(a[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = v - (v @ a) * a; e1 /= norm(e1)
    return e1, np.cross(a, e1)


def swept(M, x0, q):
    x = x0.copy()
    ang = []
    rad = []
    for _ in range(len(TS)):
        w = x ** 2
        m = w.sum() + 1e-30
        cx = (w * q[:, 0]).sum() / m
        cy = (w * q[:, 1]).sum() / m
        ang.append(np.arctan2(cy, cx)); rad.append(np.hypot(cx, cy))
        x = M @ x
    ang = np.unwrap(ang); rad = np.array(rad)
    good = np.where(rad > 0.15 * rad[0])[0]
    k = good[-1] if len(good) else len(TS) - 1
    return np.degrees(ang[k] - ang[0])


def run(radius, n_nodes=30):
    xpar, xperp, ax, axp = make_cut_and_project(PHI, LATTICE_R, radius)
    A, _, _ = build_graph(xpar, K_NEIGHBORS)
    S, K = build_operators(xpar, xperp, A, ax, axp, ALPHA)
    e1, e2 = perp_frame(ax)
    q = np.column_stack([xpar @ e1, xpar @ e2])
    dt = TS[1] - TS[0]
    Mf = expm(dt * (S + K)); Mb = expm(dt * (S - K))

    rperp = norm(q, axis=1)
    order = np.argsort(-rperp)                    # off-axis nodes first
    nodes = order[:n_nodes]
    nn = 0.6 * np.median([norm(xpar[A[i] > 0] - xpar[i], axis=1).min() for i in nodes])

    gaps = []
    for i in nodes:
        x0 = np.exp(-np.sum((xpar - xpar[i]) ** 2, axis=1) / (2 * nn ** 2)); x0 /= norm(x0)
        gaps.append(swept(Mf, x0, q) + swept(Mb, x0, q))
    gaps = np.array(gaps)
    # the single farthest node = the one watch_the_clock used
    return dict(n=len(xpar), gaps=gaps, farthest=gaps[0])


print("=" * 64)
print("CHIRALITY CHECK — is the forward/backward 1° gap real?")
print("=" * 64)
for radius in [3.0, 3.4]:
    r = run(radius)
    g = r["gaps"]
    frac_pos = np.mean(g > 0)
    print(f"\npatch radius {radius}  ({r['n']} nodes),  {len(g)} starting bumps:")
    print(f"  farthest-node gap (the watch_the_clock case): {r['farthest']:+.2f}°")
    print(f"  mean gap    : {g.mean():+.3f}°   (0 = no preferred handedness)")
    print(f"  std of gap  : {g.std():.3f}°     (per-node scatter)")
    print(f"  range       : [{g.min():+.2f}, {g.max():+.2f}]°   fraction positive: {frac_pos:.2f}")
    verdict = ("systematic (mean >> scatter/sqrt(n)) → possible real chirality"
               if abs(g.mean()) > 3 * g.std() / np.sqrt(len(g)) else
               "consistent with ZERO mean → artifact of the asymmetric start bump")
    print(f"  -> {verdict}")
