"""
THE ROSE AT LARGER N.  Does 109's picture hold as the lattice grows?

109 (N=8 decagon, N=10 octagon) found: a gear of identical tabs, a hierarchy of small jumps,
and -- the control -- the teeth survive a round window of equal area.  All at one lattice size.
Here the same node is run at growing N, both windows, and four things are tracked:

    swing        (highest - lowest) as a % of the arc-mean
    teeth        how many big tabs, their centres, their width in degrees
    big jump     the size of the largest single step (one heavy point)
    levels       how many distinct flat levels at quarter-degree resolution

plus a containment check at every N (the original float recipe, restricted to the points that
can ever enter the window -- which is the whole recipe, since the others contribute nothing).

Nothing is averaged over theta.  The "arc-mean" is reported only to normalize the swing.
"""

import os
import sys
import time

sys.path.insert(0, r"C:\Users\atoms\three-answer-plot")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from threeanswer import Frame, raster_curve, save_png
from threeanswer.plot import columns
from penrose_gauntlet import decagon_proj, octagon_proj, poly_window, dedup, zeta
from rose_three_answers import RoseZeta, MAG, S, TWO_PI, round_R2

OUTDIR = os.path.dirname(os.path.abspath(__file__))
N_ARCS = 1440
CHECK_ANGLES = 360


def enclose_all(node):
    arcs = columns(Frame(0, TWO_PI, 0, 1), N_ARCS)
    encs = [node.enclose({"theta": a}) for a in arcs]
    lo = np.array([float(e.lo) for e in encs]); hi = np.array([float(e.hi) for e in encs])
    return arcs, encs, lo, hi


def teeth(arcs, widths, big_threshold):
    """Group the big jumps into rising/falling edge pairs and report tab centres and widths."""
    deg = np.array([np.degrees((float(a.lo) + float(a.hi)) / 2) for a in arcs])
    big = np.where(widths >= big_threshold)[0]
    edges = deg[big]
    # consecutive big edges alternate up/down; pair them
    if len(edges) < 2:
        return 0, [], []
    # a tab is the short gap between two consecutive edges (the wide gap is the valley)
    gaps = np.diff(np.concatenate([edges, [edges[0] + 360]]))
    short = gaps < np.median(gaps)
    centres = [(edges[i] + gaps[i] / 2) % 360 for i in range(len(edges)) if short[i]]
    widths_deg = [gaps[i] for i in range(len(edges)) if short[i]]
    return len(centres), sorted(centres), widths_deg


def sampled_check(node, encs, arcs):
    """Original float recipe on the node's own point set (all points that can ever enter)."""
    thetas = np.linspace(0, TWO_PI, CHECK_ANGLES + 1)[:-1]
    PAR, PERP = node.PAR, node.PERP
    R2 = round_R2(node.half)

    def win(shift):
        if node.window == "round":
            p = PERP - shift
            return (p[:, 0] ** 2 + p[:, 1] ** 2) < R2
        return poly_window(PERP, node.half, 1.0, shift)

    base = zeta(dedup(PAR[win(np.zeros(2))]), S)
    bad = 0
    for t in thetas:
        v = zeta(dedup(PAR[win(MAG * np.array([np.cos(t), np.sin(t)]))]), S) / base
        i = min(int(t / TWO_PI * len(arcs)), len(arcs) - 1)
        if not (float(encs[i].lo) <= v <= float(encs[i].hi)):
            bad += 1
    return bad


def run(kind, proj, half, D, Ns):
    rows = []
    for N in Ns:
        for window in ("poly", "round"):
            t0 = time.time()
            node = RoseZeta(proj, half, D, N, window=window)
            arcs, encs, lo, hi = enclose_all(node)
            widths = hi - lo
            flat = widths < 1e-9
            mean = float(np.mean((lo + hi) / 2))
            swing = float(hi.max() - lo.min())
            bigjump = float(widths.max())
            n_teeth, centres, wdeg = teeth(arcs, widths, 0.5 * bigjump)
            levels = len(np.unique(np.round(lo[flat], 6)))
            bad = sampled_check(node, encs, arcs)
            rows.append(dict(kind=kind, N=N, window=window, points=node.n_points, base=node.base_value,
                             lo=float(lo.min()), hi=float(hi.max()), mean=mean, swing=swing,
                             swing_pct=100 * swing / mean, bigjump=bigjump, teeth=n_teeth,
                             tooth_width=float(np.mean(wdeg)) if wdeg else float("nan"),
                             tooth_width_spread=float(np.ptp(wdeg)) if wdeg else float("nan"),
                             first_centre=centres[0] if centres else float("nan"),
                             levels=levels, flat_arcs=int(flat.sum()), bad=bad, secs=time.time() - t0))
            r = rows[-1]
            print(f"  {kind:8s} N={N:2d} {window:5s} pts={r['points']:6d} baseZ={r['base']:12.6f} "
                  f"r in [{r['lo']:.6f}, {r['hi']:.6f}] swing={r['swing_pct']:6.2f}%  bigjump={r['bigjump']:.5f}  "
                  f"teeth={r['teeth']:2d} width={r['tooth_width']:5.2f}deg (spread {r['tooth_width_spread']:.2f}) "
                  f"first@{r['first_centre']:.1f}  levels={r['levels']:3d} flat={r['flat_arcs']:4d}  "
                  f"check {CHECK_ANGLES - bad}/{CHECK_ANGLES}  [{r['secs']:.0f}s]", flush=True)
            assert bad == 0
            if N == Ns[-1]:
                pad = 0.12 * swing
                img = raster_curve(node, Frame(0, TWO_PI, lo.min() - pad, hi.max() + pad), 1440, 420, depth=0, name="theta")
                wn = "poly" if window == "poly" else "roundwindow"
                save_png(img, os.path.join(OUTDIR, f"rose3_{kind}_N{N}_{wn}_unrolled.png"),
                         f"{kind} rose, N={N}, {'polygon' if window == 'poly' else 'round'} window, unrolled  (r from {lo.min():.4f} to {hi.max():.4f})")
    return rows


def main():
    t0 = time.time()
    print(f"rose_scaling.py -- shift {MAG:.6f}, s={S:g}, {N_ARCS} arcs, containment at {CHECK_ANGLES} angles")
    rows = []
    rows += run("decagon", decagon_proj, 5, 5, [6, 8, 10, 12, 14, 16])
    rows += run("octagon", octagon_proj, 4, 4, [8, 10, 14, 20, 28])
    print(f"\nall containment checks passed; {time.time()-t0:.0f}s total")

    # summary figure: swing % vs N, both windows, both lattices; tooth width vs N
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))
    for kind, col in [("decagon", "#1f77b4"), ("octagon", "#ff7f0e")]:
        for window, ls, mk in [("poly", "-", "o"), ("round", "--", "s")]:
            rr = [r for r in rows if r["kind"] == kind and r["window"] == window]
            Ns = [r["N"] for r in rr]
            ax[0].plot(Ns, [r["swing_pct"] for r in rr], ls, marker=mk, color=col, label=f"{kind}, {window} window")
            ax[1].plot(Ns, [r["tooth_width"] for r in rr], ls, marker=mk, color=col, label=f"{kind}, {window}")
            ax[2].plot(Ns, [r["levels"] for r in rr], ls, marker=mk, color=col, label=f"{kind}, {window}")
    ax[0].set_title("swing, % of arc-mean"); ax[0].set_xlabel("N (grid half-width)"); ax[0].legend(fontsize=8)
    ax[1].set_title("tooth width, degrees"); ax[1].set_xlabel("N")
    ax[2].set_title("distinct flat levels (quarter-degree arcs)"); ax[2].set_xlabel("N"); ax[2].set_yscale("log")
    fig.suptitle("The rose as the lattice grows: the teeth do not move, the tails fill in", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    out = os.path.join(OUTDIR, "rose_scaling_summary.png")
    fig.savefig(out, dpi=110)
    print("saved", out)

    with open(os.path.join(OUTDIR, "rose_scaling_table.txt"), "w", encoding="utf-8") as f:
        f.write("kind      N window  points     baseZ          lo         hi        swing%  bigjump  teeth width(deg) spread  first@  levels  flat  check\n")
        for r in rows:
            f.write(f"{r['kind']:8s} {r['N']:2d} {r['window']:5s} {r['points']:7d} {r['base']:12.6f} {r['lo']:.6f} {r['hi']:.6f} "
                    f"{r['swing_pct']:6.2f} {r['bigjump']:.5f} {r['teeth']:2d} {r['tooth_width']:6.2f} {r['tooth_width_spread']:5.2f} "
                    f"{r['first_centre']:6.1f} {r['levels']:5d} {r['flat_arcs']:5d}  {CHECK_ANGLES-r['bad']}/{CHECK_ANGLES}\n")
    print("saved rose_scaling_table.txt")


if __name__ == "__main__":
    main()
