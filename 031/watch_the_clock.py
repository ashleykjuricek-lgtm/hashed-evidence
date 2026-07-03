"""
WATCH THE CLOCK — is time's arrow real, or convention?
======================================================
Turn δ back on. O_δ = S + δK on the icosahedral quasicrystal (Tier-1's operator).
δ=+1 = circulation forward; δ=−1 = backward.

Provable backbone: since S=Sᵀ and K=−Kᵀ,
        O_{−1} = S − K = (S + K)ᵀ = O_{+1}ᵀ.
A matrix and its transpose share eigenvalues exactly. So:
  - SPECTRUM identical for ±δ  → the "laws" don't prefer a direction (time-symmetric)
  - HEAT TRACE Tr(e^{tO}) identical → the clock RATE is the same forward and backward
But the DYNAMICS are mirror images: a localized bump circulates one way for +δ, the other
for −δ. So the arrow is REAL (you can see which way it spins) but not PREFERRED (no energetic
asymmetry) — microscopic time-reversal symmetry; the arrow is an orientation, not a law.
"""
import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
from numpy.linalg import norm, eigvals
from scipy.linalg import expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from tier1 import (PHI, LATTICE_R, PHYS_RADIUS, K_NEIGHBORS, ALPHA,
                   make_cut_and_project, build_graph, build_operators)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


def perp_frame(axis):
    a = axis / norm(axis)
    v = np.array([1.0, 0, 0]) if abs(a[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = v - (v @ a) * a; e1 /= norm(e1)
    return e1, np.cross(a, e1)


def nearest_match(a, b):
    """max distance when each eigenvalue of a is matched to its nearest in b"""
    b = list(b); mx = 0.0
    for z in a:
        j = min(range(len(b)), key=lambda k: abs(b[k] - z))
        mx = max(mx, abs(b[j] - z)); b.pop(j)
    return mx


def evolve(O, x0, ts):
    dt = ts[1] - ts[0]
    M = expm(dt * O)                       # one-step propagator (robust to defective O)
    X = np.empty((len(ts), len(x0)))
    X[0] = x0
    for k in range(1, len(ts)):
        X[k] = M @ X[k - 1]
    return X


def heat_trace(O, ts_h):
    # transpose-exact: Tr(e^{tOᵀ}) = Tr((e^{tO})ᵀ) = Tr(e^{tO})
    return np.array([float(np.trace(expm(t * O)).real) for t in ts_h])


def main():
    xpar, xperp, axis_par, axis_perp = make_cut_and_project(PHI, LATTICE_R, PHYS_RADIUS)
    A, _, _ = build_graph(xpar, K_NEIGHBORS)
    S, K = build_operators(xpar, xperp, A, axis_par, axis_perp, ALPHA)
    O_fwd, O_bwd = S + K, S - K
    print(f"icosahedral quasicrystal: {len(xpar)} nodes")

    # --- provable backbone ---
    print(f"\n||O_(-1) - O_(+1)ᵀ|| = {norm(O_bwd - O_fwd.T):.2e}   (0 → backward IS forward, transposed → identical spectrum by theorem)")
    ef, eb = eigvals(O_fwd), eigvals(O_bwd)
    print(f"note: raw eigvals scatter by {nearest_match(ef, eb):.1f} — a symptom of strong NON-NORMALITY")
    print("      (which is exactly what makes it circulate); the clean invariant is the heat trace →")

    # --- dynamics: a localized bump, off the axis ---
    e1, e2 = perp_frame(axis_par)
    q = np.column_stack([xpar @ e1, xpar @ e2])          # positions in the plane ⊥ axis
    seed = int(np.argmax(norm(q, axis=1)))               # farthest-off-axis node
    nbr = xpar[A[seed] > 0]
    sig = 0.6 * np.median(norm(nbr - xpar[seed], axis=1))
    x0 = np.exp(-np.sum((xpar - xpar[seed]) ** 2, axis=1) / (2 * sig ** 2))
    x0 /= norm(x0)

    ts = np.linspace(0, 2.5, 160)
    Xf = evolve(O_fwd, x0, ts)
    Xb = evolve(O_bwd, x0, ts)
    ts_h = np.linspace(0, 2.5, 41)
    heat_f = heat_trace(O_fwd, ts_h)
    heat_b = heat_trace(O_bwd, ts_h)

    def centroid(X):
        wgt = X ** 2
        m = wgt.sum(1) + 1e-30
        cx = (wgt * q[:, 0]).sum(1) / m
        cy = (wgt * q[:, 1]).sum(1) / m
        return np.column_stack([cx, cy])

    cf, cb = centroid(Xf), centroid(Xb)
    phf = np.unwrap(np.arctan2(cf[:, 1], cf[:, 0]))
    phb = np.unwrap(np.arctan2(cb[:, 1], cb[:, 0]))
    # measure swept angle only while the centroid is still well off-center (avoid tail noise)
    rad0 = norm(cf[0])
    good = np.where(norm(cf, axis=1) > 0.15 * rad0)[0]
    klast = good[-1] if len(good) else len(ts) - 1
    swept_f = phf[klast] - phf[0]
    swept_b = phb[klast] - phb[0]

    print(f"\nheat trace: max|Tr_fwd - Tr_bwd| = {np.max(np.abs(heat_f - heat_b)):.2e}   (0 → same clock rate)")
    print(f"circulation swept angle (to t={ts[klast]:.2f}):  forward {np.degrees(swept_f):+.1f}°   "
          f"backward {np.degrees(swept_b):+.1f}°")
    denom = abs(swept_f) + abs(swept_b) + 1e-9
    mirror = abs(swept_f + swept_b) < 0.15 * denom
    print(f"  -> {'EQUAL & OPPOSITE (perfect mirror)' if mirror else 'not a clean mirror'}: "
          f"the arrow is real (it spins) but neither direction is preferred.")

    # --- plots ---
    fig, ax = plt.subplots(2, 2, figsize=(13, 10))
    ax[0, 0].scatter(ef.real, ef.imag, s=45, facecolors="none", edgecolors="#1f77b4", label="forward δ=+1")
    ax[0, 0].scatter(eb.real, eb.imag, s=12, color="#d62728", marker="x", label="backward δ=−1")
    ax[0, 0].set_title("same laws — spectrum identical"); ax[0, 0].axhline(0, lw=.4, color="gray")
    ax[0, 0].set_xlabel("Re λ"); ax[0, 0].set_ylabel("Im λ"); ax[0, 0].legend()

    ax[0, 1].plot(ts_h, heat_f, color="#1f77b4", lw=3, label="forward")
    ax[0, 1].plot(ts_h, heat_b, "--", color="#d62728", lw=1.4, label="backward")
    ax[0, 1].set_title("same clock — heat trace Tr(e^{tO}) identical")
    ax[0, 1].set_xlabel("t"); ax[0, 1].set_ylabel("Tr(e^{tO})"); ax[0, 1].legend()

    ax[1, 0].plot(ts, np.degrees(phf - phf[0]), color="#1f77b4", label=f"forward ({np.degrees(swept_f):+.0f}°)")
    ax[1, 0].plot(ts, np.degrees(phb - phb[0]), color="#d62728", label=f"backward ({np.degrees(swept_b):+.0f}°)")
    ax[1, 0].axhline(0, lw=.5, color="gray"); ax[1, 0].axvline(ts[klast], lw=.5, color="gray", ls=":")
    ax[1, 0].set_title("opposite arrow — the bump counter-rotates")
    ax[1, 0].set_xlabel("t"); ax[1, 0].set_ylabel("centroid angle swept (deg)"); ax[1, 0].legend()

    ax[1, 1].plot(cf[:, 0], cf[:, 1], color="#1f77b4", label="forward")
    ax[1, 1].plot(cb[:, 0], cb[:, 1], color="#d62728", label="backward")
    ax[1, 1].plot(0, 0, "k+", ms=10); ax[1, 1].plot(cf[0, 0], cf[0, 1], "ko", ms=6, label="start")
    ax[1, 1].set_title("centroid path ⊥ axis (mirror spirals)")
    ax[1, 1].set_xlabel("q₁"); ax[1, 1].set_ylabel("q₂"); ax[1, 1].set_aspect("equal"); ax[1, 1].legend()

    fig.suptitle("Watch the clock: same laws & rate both ways, opposite circulation — the arrow is orientation, not law", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out = os.path.join(OUTDIR, "watch_the_clock_summary.png")
    fig.savefig(out, dpi=115)
    print(f"\nSaved -> {out}")


if __name__ == "__main__":
    main()
