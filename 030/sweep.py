"""
TIER-1 ROBUSTNESS + ALPHA SWEEP  (+ a pre-registered zeta-zero test)
====================================================================

Two real questions and one honesty check.

  Q1  Does the one survivor from Tier-1 hold up?  i.e. across many wirings (k),
      blends (alpha), random seeds, and patch sizes, does the QUASICRYSTAL keep
      the TIGHTEST [S,K] "eddy" spectrum -- tighter than the periodic crystal and
      the random baseline?  We measure a DIMENSIONLESS spread (divided by ||S||^2)
      so the comparison does not depend on how we happened to scale K.

  Q2  Does the geometry/shadow blend ALPHA actually matter?  We sweep alpha from
      0 (all icosahedral geometry) to 1 (all hidden shadow) and watch the eddy
      spread.  If the curve is flat, the blend is cosmetic; if it moves, it's real.

  PRE-REGISTERED ZETA TEST (Ash's 49.77 observation, stated BEFORE running):
      The raw QC eddy edge was 49.7 in one run and 19.7 in another.  49.77 is the
      10th nontrivial Riemann zero.  Claim to falsify:
          "the raw eddy edge clusters near 49.77 across configurations."
      YES  = raw edge stays within a few percent of 49.77 across the whole sweep.
      NO   = it wanders over a wide range (which would mean 49.77 was coincidence,
             as expected, because the raw edge carries arbitrary units).
      We just report the honest distribution and let it decide.

Everything reuses the exact Tier-1 builders, so no new physics sneaks in.
"""

import os
import numpy as np
from numpy.linalg import norm, eig
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from tier1 import (PHI, LATTICE_R, make_cut_and_project, make_random,
                   build_graph, build_operators)

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# imaginary parts of the first ten nontrivial Riemann zeros
RIEMANN = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
           37.586178, 40.918719, 43.327073, 48.005151, 49.773832]

# ----------------------------- sweep grid -----------------------------
KS     = [4, 6, 8, 10]              # neighbours per point (wiring)
ALPHAS = [0.0, 0.25, 0.5, 0.75, 1.0]  # geometry <-> shadow blend
RADII  = [2.6, 3.0, 3.4]           # patch size (changes point count)
SEEDS  = [1, 2, 3]                 # random-control realisations
# ----------------------------------------------------------------------


def eddy_stats(S, K):
    """[S,K] health + spread, raw and dimensionless (divided by ||S||^2)."""
    C = S @ K - K @ S
    asym = norm(C - C.T) / (norm(C) + 1e-30)
    ev = np.linalg.eigvalsh((C + C.T) / 2.0)   # symmetric -> real spectrum
    Snorm = norm(S, 2)
    scale = Snorm ** 2 + 1e-30
    return dict(
        asym=float(asym),
        emax_raw=float(np.max(np.abs(ev))),
        espread_raw=float(ev.max() - ev.min()),
        emax_norm=float(np.max(np.abs(ev)) / scale),
        espread_norm=float((ev.max() - ev.min()) / scale),
        Snorm=float(Snorm),
    )


def main():
    print("=" * 74)
    print("TIER-1 ROBUSTNESS + ALPHA SWEEP")
    print("=" * 74)

    records = []
    max_asym = 0.0

    for radius in RADII:
        qx, qxp, qax, qaxp = make_cut_and_project(PHI, LATTICE_R, radius)
        px, pxp, pax, paxp = make_cut_and_project(13.0 / 8.0, LATTICE_R, radius)
        perp_scale = float(np.max(norm(qxp, axis=1))) if len(qxp) else 1.0

        for k in KS:
            Aq, _, _ = build_graph(qx, k)
            Ap, _, _ = build_graph(px, k)
            rsets = []
            for seed in SEEDS:
                rx, rxp, rax, raxp = make_random(len(qx), radius, perp_scale, seed)
                Ar, _, _ = build_graph(rx, k)
                rsets.append((rx, rxp, rax, raxp, Ar))

            for alpha in ALPHAS:
                Sq, Kq = build_operators(qx, qxp, Aq, qax, qaxp, alpha)
                Sp, Kp = build_operators(px, pxp, Ap, pax, paxp, alpha)
                q = eddy_stats(Sq, Kq)
                p = eddy_stats(Sp, Kp)

                rs = []
                for (rx, rxp, rax, raxp, Ar) in rsets:
                    Sr, Kr = build_operators(rx, rxp, Ar, rax, raxp, alpha)
                    rs.append(eddy_stats(Sr, Kr))
                r = {key: float(np.mean([d[key] for d in rs])) for key in rs[0]}

                max_asym = max(max_asym, q["asym"], p["asym"], r["asym"])
                records.append(dict(radius=radius, k=k, alpha=alpha,
                                    Nq=len(qx), Np=len(px), q=q, p=p, r=r))

    n = len(records)
    print(f"\nconfigurations run: {n}   (k×alpha×radius = {len(KS)}×{len(ALPHAS)}×{len(RADII)})")
    print(f"point counts: quasicrystal {records[0]['Nq']}..{records[-1]['Nq']}, "
          f"periodic {records[0]['Np']}..{records[-1]['Np']}")

    # ---- sanity: does the [S,K]-is-symmetric fact survive everywhere? ----
    print(f"\n[SANITY] worst [S,K] asymmetry across ALL {n} configs: {max_asym:.2e}  "
          f"(should be ~1e-15 -> commutator stays symmetric everywhere)")

    # ---- Q1: is the quasicrystal reliably the tightest? ----
    q_tightest = sum(1 for rec in records
                     if rec["q"]["espread_norm"] < rec["p"]["espread_norm"]
                     and rec["q"]["espread_norm"] < rec["r"]["espread_norm"])
    ratio_qr = np.array([rec["q"]["espread_norm"] / rec["r"]["espread_norm"] for rec in records])
    ratio_qp = np.array([rec["q"]["espread_norm"] / rec["p"]["espread_norm"] for rec in records])
    print(f"\n[Q1] quasicrystal has the tightest eddy spread in "
          f"{q_tightest}/{n} configs ({100*q_tightest/n:.0f}%)")
    print(f"     QC/random  spread ratio: median {np.median(ratio_qr):.2f}  "
          f"(range {ratio_qr.min():.2f}..{ratio_qr.max():.2f})   [<1 means QC tighter]")
    print(f"     QC/periodic spread ratio: median {np.median(ratio_qp):.2f}  "
          f"(range {ratio_qp.min():.2f}..{ratio_qp.max():.2f})")

    # ---- Q2: does alpha matter? ----
    print("\n[Q2] eddy spread (dimensionless) vs blend alpha, averaged over k/radius/seed:")
    print(f"     {'alpha':>6}{'quasicrystal':>14}{'periodic':>12}{'random':>12}")
    for a in ALPHAS:
        sub = [rec for rec in records if rec["alpha"] == a]
        mq = np.mean([rec["q"]["espread_norm"] for rec in sub])
        mp = np.mean([rec["p"]["espread_norm"] for rec in sub])
        mr = np.mean([rec["r"]["espread_norm"] for rec in sub])
        print(f"     {a:>6.2f}{mq:>14.3f}{mp:>12.3f}{mr:>12.3f}")

    # ---- pre-registered zeta test ----
    emax_raw = np.array([rec["q"]["emax_raw"] for rec in records])
    near = np.sum(np.abs(emax_raw - 49.773832) / 49.773832 < 0.03)
    print("\n[ZETA TEST] raw QC eddy edge across configs:")
    print(f"     range {emax_raw.min():.2f} .. {emax_raw.max():.2f}   "
          f"(median {np.median(emax_raw):.2f})")
    print(f"     configs landing within 3% of the 10th zero (49.77): {near}/{n}")
    verdict = ("YES -- clusters at 49.77" if near > 0.5 * n
               else "NO -- it wanders; 49.77 was coincidence (as expected: arbitrary units)")
    print(f"     VERDICT: {verdict}")

    # ------------------------------- plots -------------------------------
    fig, ax = plt.subplots(2, 2, figsize=(14, 10))
    C = {"q": "#1f77b4", "p": "#ff7f0e", "r": "#2ca02c"}

    # (0,0) alpha dependence
    for key, lab in [("q", "quasicrystal"), ("p", "periodic"), ("r", "random")]:
        ys = [np.mean([rec[key]["espread_norm"] for rec in records if rec["alpha"] == a]) for a in ALPHAS]
        ax[0, 0].plot(ALPHAS, ys, "o-", color=C[key], label=lab)
    ax[0, 0].set_title("Q2: eddy spread vs blend α  (0=geometry, 1=shadow)")
    ax[0, 0].set_xlabel("α"); ax[0, 0].set_ylabel("dimensionless eddy spread"); ax[0, 0].legend()

    # (0,1) QC/random ratio across all configs
    ax[0, 1].hist(ratio_qr, bins=20, color=C["q"], alpha=0.7, label="QC / random")
    ax[0, 1].hist(ratio_qp, bins=20, color=C["p"], alpha=0.5, label="QC / periodic")
    ax[0, 1].axvline(1.0, color="k", lw=1.2, ls="--", label="equal (=1)")
    ax[0, 1].set_title(f"Q1: is QC tighter?  ({q_tightest}/{n} configs yes)")
    ax[0, 1].set_xlabel("eddy-spread ratio  (<1 → QC tighter)"); ax[0, 1].set_ylabel("count"); ax[0, 1].legend()

    # (1,0) zeta test: raw edge distribution vs Riemann zeros
    ax[1, 0].hist(emax_raw, bins=25, color="#7f7f7f", alpha=0.8)
    for z in RIEMANN:
        ax[1, 0].axvline(z, color="#d62728", lw=0.7, alpha=0.5)
    ax[1, 0].axvline(49.773832, color="#d62728", lw=2.0, label="10th zero = 49.77")
    ax[1, 0].set_title("ZETA TEST: raw QC eddy edge vs Riemann zeros")
    ax[1, 0].set_xlabel("raw eddy edge (arbitrary units)"); ax[1, 0].set_ylabel("count"); ax[1, 0].legend()

    # (1,1) dimensionless edge distribution (the honest, unit-free version)
    emax_norm = np.array([rec["q"]["emax_norm"] for rec in records])
    ax[1, 1].hist(emax_norm, bins=25, color=C["q"], alpha=0.8)
    ax[1, 1].set_title("same edge, made dimensionless (÷||S||²) — no fixed units to match")
    ax[1, 1].set_xlabel("dimensionless eddy edge"); ax[1, 1].set_ylabel("count")

    fig.suptitle("Tier-1 sweep: robustness, α-dependence, and the zeta-zero check", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out = os.path.join(OUTDIR, "sweep_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
