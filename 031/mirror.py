"""
MIRROR-SYMMETRY TEST  (does O_δ respect the Galois mirror  √5 -> -√5 ?)
======================================================================

The deep fact Ash spotted: the hidden-shadow coordinate IS the Galois conjugate of
the physical coordinate. Physical space is built from φ = (1+√5)/2 (i.e. +√5); the
internal/window space is built from φ' = (1-√5)/2 (i.e. -√5). Swapping √5 -> -√5 is
an exact algebraic reflection that turns one into the other.

Because K's entries are polynomials in the coordinates:
    K_conj (circulation from the shadow coords) = the entry-by-entry Galois conjugate
    of K_phys (circulation from the physical coords).
S = -Laplacian has integer entries, so it is its OWN mirror (S* = S).
Therefore   O_conj(δ) = S + δ·K_conj   is the exact Galois mirror of   O_phys(δ).

Question: is the operator invariant (or cleanly related) under that mirror?

We measure two things, because there are two ways it can be asymmetric:
  RAW mirror        -- the honest Galois mirror. NOTE the shadow coords are smaller
                       (|φ'| = 1/φ² ≈ 0.38 of physical), so circulation is naturally
                       WEAKER on the mirror side. Any asymmetry here is partly this
                       intrinsic contraction -- which is itself real geometry.
  NORMALISED mirror -- rescale both K's to the same strength first, to isolate whether
                       the STRUCTURE (not just the scale) is asymmetric.

Pre-registered read:
  gap ≈ 0            -> the two sides match: O_δ has a genuine mirror symmetry.
  gap > 0, structured-> no exact symmetry, but the ASYMMETRY may be special to the
                       quasicrystal (whose number field actually contains √5; the
                       periodic/random controls don't, so the mirror is only truly
                       meaningful for the QC -- controls are rough baselines).
"""

import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")   # Windows console defaults to cp1252
except Exception:
    pass
import numpy as np
from numpy.linalg import norm, eig
from scipy.spatial import cKDTree
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tier1 import PHI, LATTICE_R, make_cut_and_project, make_random

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PHYS_RADIUS = 3.0
K_NEIGHBORS = 6


def graph_knn(x, k):
    n = len(x)
    kk = min(k, n - 1)
    tree = cKDTree(x)
    _, idx = tree.query(x, k=kk + 1)
    A = np.zeros((n, n))
    for i in range(n):
        for j in idx[i, 1:]:
            A[i, j] = 1.0
            A[j, i] = 1.0
    return A


def make_S(A):
    return -(np.diag(A.sum(1)) - A)          # -Laplacian; integer entries => self-conjugate


def make_K(coords, axis, A):
    n = len(coords)
    K = np.zeros((n, n))
    ii, jj = np.where(np.triu(A, 1) > 0)
    val = np.cross(coords[ii], coords[jj]) @ axis
    K[ii, jj] = val
    K[jj, ii] = -val
    return K


def eddy(S, K):
    C = S @ K - K @ S
    return np.linalg.eigvalsh((C + C.T) / 2.0)


def relgap(a, b):
    """relative L2 distance between two sorted real spectra"""
    a, b = np.sort(a), np.sort(b)
    return float(norm(a - b) / (0.5 * (norm(a) + norm(b)) + 1e-30))


def analyse(name, xpar, xperp, axis_par, axis_perp):
    A = graph_knn(xpar, K_NEIGHBORS)
    S = make_S(A)
    Kp = make_K(xpar, axis_par, A)      # physical circulation
    Kc = make_K(xperp, axis_perp, A)    # mirror (Galois-conjugate) circulation

    # raw Galois mirror
    ep_raw, ec_raw = eddy(S, Kp), eddy(S, Kc)
    gap_raw = relgap(np.abs(ep_raw), np.abs(ec_raw))
    spread_raw = (ec_raw.max() - ec_raw.min()) / (ep_raw.max() - ep_raw.min())

    # normalised mirror (equal circulation strength)
    sS = norm(S, 2)
    Kpn = Kp * (sS / (norm(Kp, 2) + 1e-30))
    Kcn = Kc * (sS / (norm(Kc, 2) + 1e-30))
    ep_n, ec_n = eddy(S, Kpn), eddy(S, Kcn)
    gap_n = relgap(np.abs(ep_n), np.abs(ec_n))
    spread_n = (ec_n.max() - ec_n.min()) / (ep_n.max() - ep_n.min())

    # full O_δ spectra at δ=1, normalised, for the picture
    spec_phys = eig(S + Kpn)[0]
    spec_conj = eig(S + Kcn)[0]

    return dict(name=name, n=len(xpar),
                gap_raw=gap_raw, spread_raw=spread_raw,
                gap_n=gap_n, spread_n=spread_n,
                ep_n=ep_n, ec_n=ec_n, spec_phys=spec_phys, spec_conj=spec_conj,
                contract=norm(xperp) / (norm(xpar) + 1e-30))


def main():
    print("=" * 72)
    print("MIRROR-SYMMETRY TEST  (Galois  √5 -> -√5)")
    print("=" * 72)

    qx, qxp, qax, qaxp = make_cut_and_project(PHI, LATTICE_R, PHYS_RADIUS)
    px, pxp, pax, paxp = make_cut_and_project(13.0 / 8.0, LATTICE_R, PHYS_RADIUS)
    perp_scale = float(np.max(norm(qxp, axis=1)))
    rx, rxp, rax, raxp = make_random(len(qx), PHYS_RADIUS, perp_scale, 1)

    sets = [analyse("quasicrystal", qx, qxp, qax, qaxp),
            analyse("periodic",     px, pxp, pax, paxp),
            analyse("random",       rx, rxp, rax, raxp)]

    print(f"\n{'set':<14}{'N':>6}{'gap RAW':>10}{'spread RAW':>12}"
          f"{'gap NORM':>10}{'spread NORM':>13}{'shadow/phys':>13}")
    for s in sets:
        print(f"{s['name']:<14}{s['n']:>6}{s['gap_raw']:>10.3f}{s['spread_raw']:>12.3f}"
              f"{s['gap_n']:>10.3f}{s['spread_n']:>13.3f}{s['contract']:>13.3f}")

    print("\nReading it:")
    print("  gap    = how different the eddy spectrum is on the two mirror sides (0 = symmetric)")
    print("  spread = mirror-side eddy spread / physical-side  (<1 = mirror side is quieter/tighter)")
    print("  shadow/phys = intrinsic contraction of the shadow space (golden: ~1/φ² ≈ 0.38)")
    qc = sets[0]
    print(f"\n  quasicrystal: RAW mirror gap {qc['gap_raw']:.2f}, NORM mirror gap {qc['gap_n']:.2f}")
    if qc["gap_n"] < 0.05:
        print("  -> NORMALISED gap ~0: the STRUCTURE is mirror-symmetric; raw asymmetry is just contraction.")
    else:
        print("  -> NORMALISED gap stays > 0: the asymmetry is structural, not only scale.")
    print(f"  Is the QC more mirror-symmetric than controls? "
          f"QC gap_n={qc['gap_n']:.2f} vs periodic={sets[1]['gap_n']:.2f}, random={sets[2]['gap_n']:.2f}")

    # ------------------------------- plots -------------------------------
    fig, ax = plt.subplots(1, 3, figsize=(17, 5.2))

    # (0) eddy spectra, physical vs mirror, quasicrystal (normalised)
    ax[0].plot(np.sort(qc["ep_n"]), label="physical (+√5)", color="#1f77b4")
    ax[0].plot(np.sort(qc["ec_n"]), label="mirror / shadow (−√5)", color="#d62728")
    ax[0].set_title("QC: [S,K] eddy spectrum, physical vs mirror")
    ax[0].set_xlabel("index (sorted)"); ax[0].set_ylabel("eigenvalue"); ax[0].legend()

    # (1) O_δ=1 spectra in complex plane, physical vs mirror, quasicrystal
    ax[1].scatter(qc["spec_phys"].real, qc["spec_phys"].imag, s=10, alpha=0.6,
                  color="#1f77b4", label="physical (+√5)")
    ax[1].scatter(qc["spec_conj"].real, qc["spec_conj"].imag, s=10, alpha=0.6,
                  color="#d62728", label="mirror (−√5)")
    ax[1].axhline(0, lw=0.5, color="gray")
    ax[1].set_title("QC: spectrum of O_{δ=1}, physical vs mirror")
    ax[1].set_xlabel("Re(λ)"); ax[1].set_ylabel("Im(λ)"); ax[1].legend()

    # (2) normalised mirror gap, all three sets
    names = [s["name"] for s in sets]
    gaps = [s["gap_n"] for s in sets]
    ax[2].bar(names, gaps, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
    ax[2].set_title("normalised mirror gap (0 = perfectly mirror-symmetric)")
    ax[2].set_ylabel("gap")

    fig.suptitle("Mirror test: does O_δ respect √5 → −√5 ?", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(OUTDIR, "mirror_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
