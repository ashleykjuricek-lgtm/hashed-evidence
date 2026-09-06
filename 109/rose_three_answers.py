"""
THE ROSE, DRAWN WITH THREE ANSWERS.

The Penrose rose (ledger 022, penrose_rose.py) is r(theta) = Z_shifted(theta) / Z_unshifted,
where Z is a zeta sum over the cut-and-project point set and the acceptance window in
perpendicular space is shifted by MAG*(cos theta, sin theta).  It is a STEP function of
theta: as the window slides, lattice points drop in and out one at a time.

penrose_rose.py drew it by point-sampling 721 angles and joining them.  A joined polyline
draws a confident diagonal through every step.  Here the rose is fed to the three-answer
plotter as its own expression node: for each ARC of angle, every lattice point is either

    definitely inside the shifted window for the whole arc,
    definitely outside for the whole arc, or
    undecided (its window boundary crosses somewhere inside the arc),

and so Z over the arc is enclosed by [sum of definite, sum of definite + sum of undecided].
That range is sound.  Where an arc contains a step, the range is fat, and the plotter draws a
bar from the lower level to the upper level -- "the jump is somewhere in here" -- instead of
a line pretending to know where.

Nothing is averaged.  The mean is not drawn.

Two windows are run for each lattice: the polygon of 022's recipe, and a ROUND window of the
same area (round_window_control.py's control).  If the round window flattened the rose, the
rose would be the aperture's corners.  It does not.

Soundness of this node, stated plainly: the lattice projection, the window normals and the
zeta weights are ordinary floats (as in penrose_gauntlet.py); each is padded outward by a
relative 1e-12 before use.  The cos/sin of the arc come from mpmath's interval type.  The
check at the bottom evaluates the original point-sampled rose at 1440 angles and confirms
every sample lies inside the enclosure of the arc that contains it.
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

from threeanswer import Bounded, Frame, raster_curve, raster_polar, save_png
from threeanswer.expr import Expr
from threeanswer.plot import columns
from penrose_gauntlet import PHI, decagon_proj, octagon_proj, grid, poly_window, dedup, zeta

OUTDIR = os.path.dirname(os.path.abspath(__file__))
MAG = 1 / PHI ** 2      # 022's shift magnitude
S = 2.0                 # zeta exponent: weight = (x^2 + y^2)^(-S)
PAD = 1e-12             # relative outward pad on every float the lattice hands us
TWO_PI = 2 * np.pi
N_ARCS = 1440           # quarter-degree arcs


def _pad(lo, hi):
    """Widen [lo, hi] outward by a relative PAD (and one ulp), elementwise."""
    lo = np.asarray(lo, float); hi = np.asarray(hi, float)
    lo2 = np.nextafter(lo - np.abs(lo) * PAD, -np.inf)
    hi2 = np.nextafter(hi + np.abs(hi) * PAD, np.inf)
    return lo2, hi2


def _mul(a, lo, hi):
    """scalar a times interval [lo, hi], sign-aware, padded."""
    p, q = a * lo, a * hi
    return _pad(np.minimum(p, q), np.maximum(p, q))


def _sq(lo, hi):
    """interval square, sign-aware: an interval containing zero squares to [0, max^2]."""
    a, b = lo * lo, hi * hi
    sq_lo = np.where((lo <= 0) & (hi >= 0), 0.0, np.minimum(a, b))
    sq_hi = np.maximum(a, b)
    return _pad(sq_lo, sq_hi)


def round_R2(half):
    """R^2 of the disc with the same area as the 2*half-gon of inradius 1."""
    return (2 * half * np.tan(np.pi / (2 * half))) / np.pi


class RoseZeta(Expr):
    """r(theta) = Z(window shifted by MAG*(cos theta, sin theta)) / Z(unshifted).

    window="poly"  : the 2*half-gon of inradius 1 (022's recipe)
    window="round" : a disc of the same area, no corners (the control)
    """

    def __init__(self, proj_fn, half, D, N, name="theta", window="poly"):
        self.name = name
        self.window = window
        self.half = half
        self.R2 = round_R2(half)
        Ppar, Pperp = proj_fn()
        g = grid(N, D)
        PAR = g @ Ppar.T
        PERP = g @ Pperp.T

        # dedup exactly as the original: unique PAR (1e-8 key).  Duplicates must share PERP,
        # otherwise "dedup after windowing" and "dedup before" could differ.  Check it.
        key = np.round(PAR / 1e-8).astype(np.int64)
        _, first, inverse = np.unique(key, axis=0, return_index=True, return_inverse=True)
        inverse = inverse.ravel()
        perp_spread = np.zeros(len(first))
        np.maximum.at(perp_spread, inverse, np.abs(PERP - PERP[first][inverse]).max(axis=1))
        assert perp_spread.max() < 1e-9, f"duplicate PAR points with different PERP: {perp_spread.max()}"
        PAR, PERP = PAR[first], PERP[first]

        # drop the origin (zeta does), and everything that can never enter the shifted window
        r2 = np.sum(PAR * PAR, axis=1)
        keep = r2 > 1e-12
        reach = max(1.0 / np.cos(np.pi / (2 * half)), np.sqrt(self.R2)) + MAG + 1e-9
        keep &= np.hypot(PERP[:, 0], PERP[:, 1]) < reach
        PAR, PERP, r2 = PAR[keep], PERP[keep], r2[keep]

        w = r2 ** (-S)
        self.w_lo, self.w_hi = _pad(w, w)
        self.n_points = len(w)
        self.qx_lo, self.qx_hi = _pad(PERP[:, 0], PERP[:, 0])
        self.qy_lo, self.qy_hi = _pad(PERP[:, 1], PERP[:, 1])

        # polygon half-space normals, as in poly_window
        self.normals = [(np.cos(np.pi * (2 * k + 1) / (2 * half)), np.sin(np.pi * (2 * k + 1) / (2 * half)))
                        for k in range(half)]
        self.d = []
        for nx, ny in self.normals:
            d = PERP[:, 0] * nx + PERP[:, 1] * ny
            self.d.append(_pad(d, d))

        # the unshifted base, using the plain float recipe (what the original divides by)
        if window == "round":
            base_mask = (PERP[:, 0] ** 2 + PERP[:, 1] ** 2) < self.R2
        else:
            base_mask = poly_window(PERP, half, 1.0, np.zeros(2))
        self.base_value = float(np.sum(w[base_mask]))
        blo, bhi = _pad(self.base_value, self.base_value)
        self.base = Bounded.of(float(blo), float(bhi))

    def variables(self):
        return {self.name}

    def enclose(self, cell):
        arc = cell[self.name]
        c, s = arc.cos(), arc.sin()
        clo, chi = _pad(float(c.lo), float(c.hi))
        slo, shi = _pad(float(s.lo), float(s.hi))

        if self.window == "round":
            # |q - MAG*(c, s)|^2 < R^2, as an interval over the arc
            mclo, mchi = _mul(MAG, clo, chi)
            mslo, mshi = _mul(MAG, slo, shi)
            uxlo, uxhi = _pad(self.qx_lo - mchi, self.qx_hi - mclo)
            uylo, uyhi = _pad(self.qy_lo - mshi, self.qy_hi - mslo)
            sxlo, sxhi = _sq(uxlo, uxhi)
            sylo, syhi = _sq(uylo, uyhi)
            r2lo, r2hi = _pad(sxlo + sylo, sxhi + syhi)
            inside = r2hi < self.R2
            outside = r2lo >= self.R2
        else:
            inside = np.ones(self.n_points, bool)      # definitely inside for every normal
            outside = np.zeros(self.n_points, bool)    # definitely outside for some normal
            for (nx, ny), (dlo, dhi) in zip(self.normals, self.d):
                tlo1, thi1 = _mul(nx, clo, chi)          # t = n . (cos, sin) over the arc
                tlo2, thi2 = _mul(ny, slo, shi)
                tlo, thi = _pad(tlo1 + tlo2, thi1 + thi2)
                mlo, mhi = _mul(MAG, tlo, thi)
                vlo, vhi = _pad(dlo - mhi, dhi - mlo)    # v = q.n - MAG * t
                inside &= (vhi < 1.0) & (vlo > -1.0)
                outside |= (vlo >= 1.0) | (vhi <= -1.0)
        undecided = ~inside & ~outside
        z_lo = float(np.sum(self.w_lo[inside]))
        z_hi = float(np.sum(self.w_hi[inside]) + np.sum(self.w_hi[undecided]))
        z_lo, z_hi = _pad(z_lo, z_hi)
        return Bounded.of(float(z_lo), float(z_hi)).div(self.base)

    def __str__(self):
        return f"rose(theta; {self.window} window)"


# --------------------------------------------------------------------------- #
# the original, point-sampled, for the containment check
# --------------------------------------------------------------------------- #

def sampled_rose(proj_fn, half, D, N, thetas, window="poly"):
    Ppar, Pperp = proj_fn()
    g = grid(N, D)
    PAR = g @ Ppar.T
    PERP = g @ Pperp.T
    R2 = round_R2(half)

    def win(shift):
        if window == "round":
            p = PERP - shift
            return (p[:, 0] ** 2 + p[:, 1] ** 2) < R2
        return poly_window(PERP, half, 1.0, shift)

    base = zeta(dedup(PAR[win(np.zeros(2))]), S)
    return np.array([zeta(dedup(PAR[win(MAG * np.array([np.cos(t), np.sin(t)]))]), S) / base for t in thetas])


def report(name, node, n_arcs=N_ARCS):
    """Enclose every arc once and say what the three answers were and where the steps are."""
    frame = Frame(0, TWO_PI, 0, 1)
    arcs = columns(frame, n_arcs)
    encs = [node.enclose({"theta": a}) for a in arcs]
    kinds = {}
    for e in encs:
        kinds[e.kind()] = kinds.get(e.kind(), 0) + 1
    widths = np.array([float(e.hi - e.lo) if e.kind() == "bounded" else np.nan for e in encs])
    los = np.array([float(e.lo) if e.kind() == "bounded" else np.nan for e in encs])
    his = np.array([float(e.hi) if e.kind() == "bounded" else np.nan for e in encs])
    thin = widths < 1e-9
    fat = ~thin
    mean_level = float(np.nanmean((los + his) / 2))
    print(f"\n{name}")
    print(f"  {node.n_points} lattice points can ever enter the window; unshifted Z = {node.base_value:.7f}")
    print(f"  three-answer tally over {n_arcs} arcs of {360/n_arcs:.3f} deg: {kinds}")
    print(f"  arcs where r is a single value (flat step): {thin.sum()}")
    print(f"  arcs that contain a jump (fat enclosure):    {fat.sum()}")
    print(f"  lowest level {np.nanmin(los):.6f}   highest level {np.nanmax(his):.6f}   "
          f"swing {np.nanmax(his)-np.nanmin(los):.6f}  = {100*(np.nanmax(his)-np.nanmin(los))/mean_level:.2f}% of the arc-mean {mean_level:.6f}")
    levels = np.unique(np.round(los[thin], 6))
    print(f"  distinct flat levels: {len(levels)}")
    jumps = widths[fat]
    if len(jumps):
        print(f"  jump sizes: smallest {jumps.min():.2e}   largest {jumps.max():.4f}   median {np.median(jumps):.2e}")
        edges = [1e-9, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]
        h, _ = np.histogram(jumps, bins=edges)
        print("  jump sizes by decade: " + "  ".join(f"[{lo:.0e},{hi:.0e}):{c}" for lo, hi, c in zip(edges, edges[1:], h)))
        big = np.sort(np.unique(np.round(jumps[jumps > 1e-3], 5)))[::-1]
        print(f"  distinct jump sizes above 1e-3: {big}")
    order = np.argsort(-np.nan_to_num(widths, nan=0))[:20]
    print("  the twenty largest jumps (deg, size): " + ", ".join(
        f"({np.degrees((float(arcs[i].lo)+float(arcs[i].hi))/2):.1f}, {widths[i]:.4f})" for i in sorted(order)))
    return arcs, encs


def containment_check(name, node, arcs, encs, proj_fn, half, D, N):
    thetas = np.linspace(0, TWO_PI, N_ARCS + 1)[:-1]
    print(f"  containment check: sampling the ORIGINAL float recipe at {len(thetas)} angles ...", end="", flush=True)
    r = sampled_rose(proj_fn, half, D, N, thetas, node.window)
    bad = 0
    idx = np.minimum((thetas / TWO_PI * len(arcs)).astype(int), len(arcs) - 1)
    for t, v, i in zip(thetas, r, idx):
        cands = [encs[i]] + ([encs[i - 1]] if i > 0 and abs(t - float(arcs[i].lo)) < 1e-12 else [])
        if not any(float(c.lo) <= v <= float(c.hi) for c in cands):
            bad += 1
    print(f" {len(thetas) - bad} inside, {bad} outside")
    return bad


def main():
    t0 = time.time()
    print(f"rose_three_answers.py  --  shift magnitude {MAG:.6f} (= 1/phi^2), exponent s = {S:g}, "
          f"{N_ARCS} arcs, pad {PAD:g}")
    jobs = [("DECAGON (Penrose P3, fivefold), N=8, decagon window (022's recipe)", decagon_proj, 5, 5, 8, "poly"),
            ("DECAGON (Penrose P3, fivefold), N=8, ROUND window of equal area (the control)", decagon_proj, 5, 5, 8, "round"),
            ("OCTAGON (silver, eightfold), N=10, octagon window", octagon_proj, 4, 4, 10, "poly"),
            ("OCTAGON (silver, eightfold), N=10, ROUND window of equal area (the control)", octagon_proj, 4, 4, 10, "round")]
    for name, proj, half, D, N, window in jobs:
        node = RoseZeta(proj, half, D, N, window=window)
        print(f"\n[{time.time()-t0:6.1f}s] built: {name}")
        arcs, encs = report(name, node)
        bad = containment_check(name, node, arcs, encs, proj, half, D, N)
        assert bad == 0, "the enclosure missed a sampled value -- the node is not sound"

        los = [float(e.lo) for e in encs]
        his = [float(e.hi) for e in encs]
        rlo, rhi = min(los), max(his)
        pad = 0.12 * (rhi - rlo)
        slug = ("decagon" if half == 5 else "octagon") + ("" if window == "poly" else "_roundwindow")
        wname = f"{2*half}-gon window" if window == "poly" else "round window, equal area"

        img = raster_curve(node, Frame(0, TWO_PI, rlo - pad, rhi + pad), 1440, 480, depth=0, name="theta")
        p1 = save_png(img, os.path.join(OUTDIR, f"rose3_{slug}_unrolled.png"),
                      f"{slug.split('_')[0]} rose, {wname}, unrolled: r over 0..360 deg  (r from {rlo:.4f} to {rhi:.4f})")
        R = rhi * 1.15
        img = raster_polar(node, Frame(-R, R, -R, R), 720, 720, 0, 2, n_arcs=N_ARCS, depth=0, name="theta")
        p2 = save_png(img, os.path.join(OUTDIR, f"rose3_{slug}_polar.png"),
                      f"{slug.split('_')[0]} rose, {wname}, polar: r = Z_shifted / Z_unshifted, shift {MAG:.4f}, s = {S:g}")
        print(f"  saved {os.path.basename(p1)}\n  saved {os.path.basename(p2)}   [{time.time()-t0:.1f}s]")
    print(f"\ndone in {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
