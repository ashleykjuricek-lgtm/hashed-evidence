"""Ash: "flat and thin rhombi."

Penrose P3 has exactly two prototiles -- the FAT rhomb (72/108 deg) and the THIN
rhomb (36/144 deg), occurring in ratio phi:1. If the rose is built from the tiling
rather than from the window's roundness, its petals should NOT all be the same:
there should be five of one and five of the other, alternating.

022 asserted "10 petals" and "r = |cos(5 theta)|". Neither was ever counted.
Count them.
"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
from penrose_gauntlet import PHI, decagon_proj, octagon_proj
from penrose_rose import rose

TH = np.linspace(0, 2*np.pi, 1441, endpoint=True)   # 0.25 deg resolution

def peaks(r, th):
    idx = [i for i in range(1, len(r)-1) if r[i] > r[i-1] and r[i] >= r[i+1]]
    return [(np.degrees(th[i]), r[i]) for i in idx]

def troughs(r, th):
    idx = [i for i in range(1, len(r)-1) if r[i] < r[i-1] and r[i] <= r[i+1]]
    return [(np.degrees(th[i]), r[i]) for i in idx]

for name, proj, half, D, N in [("decagon (5-fold, Penrose P3)", decagon_proj, 5, 5, 8),
                               ("octagon (8-fold, silver)",     octagon_proj, 4, 4, 10)]:
    print("="*66); print(name); print("="*66)
    r = rose(proj, half, D, N, TH)
    P, T = peaks(r, TH), troughs(r, TH)
    print(f"  peaks found: {len(P)}    troughs found: {len(T)}")
    print("  peak angle (deg) / height:")
    for a, v in P: print(f"      {a:7.2f}   {v:.6f}")
    hs = np.array([v for _, v in P])
    if len(hs) > 1:
        hi, lo = hs[hs > hs.mean()], hs[hs <= hs.mean()]
        print(f"  distinct peak heights?  above-mean n={len(hi)} mean={hi.mean():.6f}")
        print(f"                          below-mean n={len(lo)} mean={lo.mean() if len(lo) else float('nan'):.6f}")
        if len(hi) and len(lo):
            print(f"  ratio big/small = {hi.mean()/lo.mean():.6f}    phi = {PHI:.6f}   1/phi = {1/PHI:.6f}")
        print(f"  spread within the tall peaks : {hs.max()-hs.min():.2e}")
    # is it |cos(5 theta)| ?  fit amplitude+offset to |cos(5t)| and to cos(10t)
    for k, f in [(5, np.abs(np.cos(5*TH))), (10, np.cos(10*TH)), (20, np.cos(20*TH))]:
        A = np.vstack([f, np.ones_like(f)]).T
        c, res, *_ = np.linalg.lstsq(A, r, rcond=None)
        pred = A @ c
        rel = np.sqrt(np.mean((r-pred)**2))/np.std(r)
        print(f"  fit to k={k:2d} basis: residual/std = {rel:.4f}   {'GOOD' if rel < 0.15 else ''}")
    print()
