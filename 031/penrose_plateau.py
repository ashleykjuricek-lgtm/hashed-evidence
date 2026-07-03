"""
PENROSE PLATEAU — is the decagon phason-plateau value ACTUALLY 1/phi?
====================================================================
Arm A showed the decagon zeta-ratio is a shift-robust PLATEAU (not a tuned point),
and Arm B showed it is decagon-specific (octagon/icosa don't reproduce it). Now the
two questions that decide whether it's real:

  1. PRECISION + CONVERGENCE: what is the plateau value exactly, averaged over the
     flat region, and does it converge to 1/phi as the lattice N grows?
  2. s-SPECIFICITY: the plateau value depends on s. Is it 1/phi only at s=2 (a second
     tuned knob), or over a range?

Compares the plateau mean to 1/phi and to nearby simple constants, so we don't fool
ourselves that "~0.6" is "golden."
"""
import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from penrose_gauntlet import PHI, points, zeta, shift_dir

OUTDIR = os.path.dirname(os.path.abspath(__file__))
INV_PHI = 1 / PHI
PLATEAU_DS = np.linspace(0.12, 0.55, 10)   # inside the flat region seen in Arm A


def plateau(kind, N, s=2.0):
    d = shift_dir(kind)
    base = zeta(points(kind, N, np.zeros_like(d)), s)
    vals = np.array([zeta(points(kind, N, x * d), s) / base for x in PLATEAU_DS])
    return vals


def main():
    print("=" * 66)
    print("PENROSE PLATEAU PRECISION")
    print("=" * 66)
    print(f"1/phi = {INV_PHI:.6f}   nearby simple constants: 3/5=0.6, 5/8=0.625, phi-1={PHI-1:.6f}")

    # 1. convergence of the decagon plateau value with N
    print("\n[1] decagon plateau (mean over d in [0.12,0.55]) vs lattice size N, s=2:")
    print(f"    {'N':>3}{'plateau mean':>14}{'std':>10}{'min':>9}{'max':>9}{'Δ from 1/phi':>14}")
    Ns, means = [], []
    for N in [4, 5, 6, 7, 8]:
        v = plateau("decagon", N)
        Ns.append(N); means.append(v.mean())
        print(f"    {N:>3}{v.mean():>14.6f}{v.std():>10.4f}{v.min():>9.4f}{v.max():>9.4f}{v.mean()-INV_PHI:>+14.6f}")
    trend = "UP toward 1/phi" if means[-1] > means[0] and means[-1] < INV_PHI else \
            ("through/past 1/phi" if means[-1] >= INV_PHI else "not converging to 1/phi")
    print(f"    trend: {trend}")

    # 2. controls at their own plateau (same d range)
    print("\n[2] control plateau means (same d range, s=2) — should NOT be ~1/phi:")
    for kind, N in [("octagon", 8), ("icosa", 4)]:
        v = plateau(kind, N)
        print(f"    {kind:9s} N={N}: mean {v.mean():.4f}  (std {v.std():.4f})   "
              f"{'~1/phi?!' if abs(v.mean()-INV_PHI)<0.03 else 'not golden'}")

    # 3. s-specificity: is the plateau value 1/phi only at s=2?
    print("\n[3] decagon plateau mean vs exponent s (N=7):")
    ss = np.linspace(1.4, 3.0, 17)
    d = shift_dir("decagon")
    base_pts = points("decagon", 7, np.zeros_like(d))
    # use several plateau shifts, average the ratio at each s
    shift_sets = [points("decagon", 7, x * d) for x in PLATEAU_DS]
    plat_vs_s = []
    for s in ss:
        b = zeta(base_pts, s)
        plat_vs_s.append(np.mean([zeta(ps, s) / b for ps in shift_sets]))
    plat_vs_s = np.array(plat_vs_s)
    # where does it cross 1/phi?
    cross = None
    for i in range(len(ss) - 1):
        if (plat_vs_s[i] - INV_PHI) * (plat_vs_s[i + 1] - INV_PHI) <= 0:
            f = (INV_PHI - plat_vs_s[i]) / (plat_vs_s[i + 1] - plat_vs_s[i])
            cross = ss[i] + f * (ss[i + 1] - ss[i])
            break
    print(f"    plateau = 1/phi at s = {cross:.4f}" if cross else "    never crosses 1/phi in [1.4,3]")
    print(f"    plateau value AT s=2 exactly: {plat_vs_s[np.argmin(np.abs(ss-2))]:.5f}")
    print("    -> if the crossing s is right at 2.00, s=2 is special; if it's just near 2, s is another knob")

    # ---- plots ----
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    ax[0].plot(Ns, means, "o-", color="#1f77b4", label="decagon plateau mean")
    ax[0].axhline(INV_PHI, color="#d62728", ls="--", label="1/φ = 0.6180")
    ax[0].axhline(0.6, color="gray", ls=":", label="3/5 = 0.6")
    ax[0].set_title("[1] plateau value vs lattice size N")
    ax[0].set_xlabel("N"); ax[0].set_ylabel("plateau mean ratio (s=2)"); ax[0].legend()

    ax[1].plot(ss, plat_vs_s, "o-", color="#1f77b4", label="decagon plateau(s)")
    ax[1].axhline(INV_PHI, color="#d62728", ls="--", label="1/φ")
    ax[1].axvline(2.0, color="gray", ls=":", label="s = 2")
    if cross:
        ax[1].plot([cross], [INV_PHI], "*", color="#d62728", ms=14)
    ax[1].set_title("[3] plateau value vs exponent s")
    ax[1].set_xlabel("s"); ax[1].set_ylabel("plateau mean ratio"); ax[1].legend()

    fig.suptitle("Is the decagon plateau actually 1/φ — precisely, and only at s=2?", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    out = os.path.join(OUTDIR, "penrose_plateau_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
