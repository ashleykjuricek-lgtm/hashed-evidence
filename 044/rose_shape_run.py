"""
LOOK AT THE SHAPE — the actual Penrose rose (the thing I wrongly averaged).

Same recipe as ledger 022, but instead of collapsing to a scalar we sweep the shift
DIRECTION and keep the whole angular curve r(theta) = Z_shifted(theta)/Z_unshifted.
That curve IS the rose. The 'null' I reported (the mean, 0.592) is drawn as the flat
grey circle so you can see exactly what averaging erased.

Also does the octagon (sqrt2 pole) so both of James's poles show their own shape.
Projects the lattice ONCE, then only re-windows per angle (fast).
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
from penrose_gauntlet import PHI, decagon_proj, octagon_proj, poly_window, dedup, zeta, grid

OUTDIR = os.path.dirname(os.path.abspath(__file__))
MAG = 1 / PHI ** 2   # same shift magnitude as 022
S = 2.0


def rose(proj_fn, half, D, N, thetas):
    Ppar, Pperp = proj_fn()
    g = grid(N, D)
    PAR = g @ Ppar.T
    PERP = g @ Pperp.T
    base = zeta(dedup(PAR[poly_window(PERP, half, 1.0, np.zeros(2))]), S)
    r = np.empty(len(thetas))
    for i, t in enumerate(thetas):
        sh = MAG * np.array([np.cos(t), np.sin(t)])
        r[i] = zeta(dedup(PAR[poly_window(PERP, half, 1.0, sh)]), S) / base
    return r


def main():
    thetas = np.linspace(0, 2 * np.pi, 721)
    print("computing decagon rose (N=8)...")
    r_dec = rose(decagon_proj, 5, 5, 8, thetas)
    print("computing octagon rose (N=10)...")
    r_oct = rose(octagon_proj, 4, 4, 10, thetas)

    for name, r in [("decagon (√5)", r_dec), ("octagon (√2)", r_oct)]:
        print(f"\n{name}:  petal(max)={r.max():.4f}  valley(min)={r.min():.4f}  "
              f"MEAN={r.mean():.4f}   (1/phi={1/PHI:.4f})")

    fig, axes = plt.subplots(1, 2, figsize=(13, 6.5), subplot_kw={"projection": "polar"})
    for ax, (name, r, col) in zip(
        axes, [("decagon  (√5 pole) — 10 petals", r_dec, "#1f77b4"),
               ("octagon  (√2 pole) — 8 petals", r_oct, "#ff7f0e")]):
        ax.plot(thetas, r, color=col, lw=2, label="the rose  r(θ)")
        ax.plot(thetas, np.full_like(thetas, r.mean()), "--", color="gray", lw=1.3,
                label=f"the mean, {r.mean():.3f}  (the erasure)")
        ax.set_title(name, va="bottom", fontsize=11)
        ax.set_rlabel_position(90)
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.18), fontsize=8, ncol=2)
    fig.suptitle("Look at the shape: the diameter breathes with the angle → a rose, not a circle",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    out = os.path.join(OUTDIR, "penrose_rose_shape.png")
    fig.savefig(out, dpi=120)
    print(f"\nSaved -> {out}")


if __name__ == "__main__":
    main()
