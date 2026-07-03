"""
MIRROR-GAP ROBUSTNESS SWEEP
===========================
Does the quasicrystal's near-mirror-symmetry (Galois √5 -> -√5) hold up across
many wirings (k), patch sizes (radius), and random seeds? And does the normalised
mirror-side spread ratio settle down (single mirror.py run gave ~1.05; the earlier
α-sweep implied ~0.80 -- reconcile).

Reports, for each of quasicrystal / periodic / random:
  - distribution of the normalised mirror gap (0 = perfectly mirror-symmetric)
  - how often the quasicrystal is the MOST mirror-symmetric of the three
"""

import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
from numpy.linalg import norm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tier1 import PHI, LATTICE_R, make_cut_and_project, make_random
from mirror import graph_knn, make_S, make_K, eddy, relgap

OUTDIR = os.path.dirname(os.path.abspath(__file__))
KS    = [4, 6, 8, 10]
RADII = [2.6, 3.0, 3.4]
SEEDS = [1, 2, 3]


def gap_spread(xpar, xperp, axp, axpp, k):
    A = graph_knn(xpar, k)
    S = make_S(A)
    Kp = make_K(xpar, axp, A)
    Kc = make_K(xperp, axpp, A)
    sS = norm(S, 2)
    Kpn = Kp * (sS / (norm(Kp, 2) + 1e-30))
    Kcn = Kc * (sS / (norm(Kc, 2) + 1e-30))
    ep, ec = eddy(S, Kpn), eddy(S, Kcn)
    gap = relgap(np.abs(ep), np.abs(ec))
    spread = (ec.max() - ec.min()) / (ep.max() - ep.min())
    return gap, spread


def main():
    print("=" * 66)
    print("MIRROR-GAP ROBUSTNESS SWEEP")
    print("=" * 66)

    gq, gp, gr, spread_q = [], [], [], []
    qc_lowest = 0
    n_cfg = 0

    for radius in RADII:
        qx, qxp, qax, qaxp = make_cut_and_project(PHI, LATTICE_R, radius)
        px, pxp, pax, paxp = make_cut_and_project(13.0 / 8.0, LATTICE_R, radius)
        perp_scale = float(np.max(norm(qxp, axis=1)))
        for k in KS:
            g_q, s_q = gap_spread(qx, qxp, qax, qaxp, k)
            g_p, _ = gap_spread(px, pxp, pax, paxp, k)
            r_vals = []
            for seed in SEEDS:
                rx, rxp, rax, raxp = make_random(len(qx), radius, perp_scale, seed)
                r_vals.append(gap_spread(rx, rxp, rax, raxp, k)[0])
            g_r = float(np.mean(r_vals))

            gq.append(g_q); gp.append(g_p); gr.append(g_r); spread_q.append(s_q)
            if g_q < g_p and g_q < g_r:
                qc_lowest += 1
            n_cfg += 1

    gq, gp, gr, spread_q = map(np.array, (gq, gp, gr, spread_q))
    print(f"\nconfigs: {n_cfg}  (k×radius = {len(KS)}×{len(RADII)}; random averaged over {len(SEEDS)} seeds)")
    print(f"\n{'set':<14}{'median gap':>12}{'range':>22}")
    for name, arr in [("quasicrystal", gq), ("periodic", gp), ("random", gr)]:
        print(f"{name:<14}{np.median(arr):>12.3f}{f'[{arr.min():.3f}, {arr.max():.3f}]':>22}")

    print(f"\nquasicrystal is the MOST mirror-symmetric in {qc_lowest}/{n_cfg} configs "
          f"({100*qc_lowest/n_cfg:.0f}%)")
    print(f"QC gap below periodic in {int(np.sum(gq < gp))}/{n_cfg}, "
          f"below random in {int(np.sum(gq < gr))}/{n_cfg}")
    print(f"\nQC mirror-side spread ratio: median {np.median(spread_q):.3f}  "
          f"(range [{spread_q.min():.3f}, {spread_q.max():.3f}])")
    print("  (single mirror.py run said ~1.05; α-sweep implied ~0.80 — this reconciles it)")

    # ------------------------------- plots -------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    ax[0].boxplot([gq, gp, gr], labels=["quasicrystal", "periodic", "random"])
    ax[0].set_title(f"mirror gap across {n_cfg} configs (lower = more symmetric)")
    ax[0].set_ylabel("normalised mirror gap")

    ax[1].hist(spread_q, bins=12, color="#1f77b4", alpha=0.8)
    ax[1].axvline(1.0, color="gray", ls="--", lw=1, label="equal (=1)")
    ax[1].axvline(np.median(spread_q), color="#d62728", lw=2,
                  label=f"median {np.median(spread_q):.2f}")
    ax[1].set_title("QC mirror-side eddy spread ratio (conj / phys)")
    ax[1].set_xlabel("spread ratio"); ax[1].set_ylabel("count"); ax[1].legend()

    fig.suptitle("Mirror-gap robustness: is the quasicrystal reliably the most √5-symmetric?", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(OUTDIR, "mirror_sweep_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
