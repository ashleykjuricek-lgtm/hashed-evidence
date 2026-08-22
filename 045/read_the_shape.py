"""Read the structure properly: the curve is piecewise-flat, so bin by LEVEL and
find plateau centres and widths, instead of hunting local maxima in noise."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
from penrose_gauntlet import PHI, decagon_proj, octagon_proj
from penrose_rose import rose

TH = np.linspace(0, 2*np.pi, 1441)
DEG = np.degrees(TH)

for name, proj, half, D, N, fold in [("decagon (Penrose P3, 5-fold)", decagon_proj, 5, 5, 8, 5),
                                     ("octagon (silver, 8-fold)",     octagon_proj, 4, 4, 10, 8)]:
    r = rose(proj, half, D, N, TH)
    lo, hi = r.min(), r.max()
    mid = 0.5*(lo+hi)
    high = r > mid
    # contiguous runs of 'high'
    runs, i = [], 0
    while i < len(high):
        if high[i]:
            j = i
            while j+1 < len(high) and high[j+1]: j += 1
            runs.append((DEG[i], DEG[j])); i = j+1
        else: i += 1
    if runs and runs[0][0] == 0.0 and runs[-1][1] >= 359.0:      # wrap
        runs = [(runs[-1][0]-360.0, runs[0][1])] + runs[1:-1]
    print("="*64); print(name); print("="*64)
    print(f"  min={lo:.6f}  max={hi:.6f}  swing={hi-lo:.6f}  ({100*(hi-lo)/r.mean():.1f}% of mean)")
    print(f"  HIGH lobes: {len(runs)}")
    cen = [(a+b)/2 for a, b in runs]; wid = [b-a for a, b in runs]
    for (a,b),c,w in zip(runs, cen, wid):
        print(f"      {a:8.2f} .. {b:7.2f}   centre {c:7.2f}   width {w:5.2f}")
    if len(cen) > 1:
        d = np.diff(cen)
        print(f"  lobe spacing: mean {d.mean():.3f} deg   (360/{len(runs)} = {360/len(runs):.3f})")
        print(f"  lobe width  : mean {np.mean(wid):.3f} deg   duty cycle {np.mean(wid)/(360/len(runs)):.4f}")
    # how many distinct levels?
    q = np.round(r, 4)
    vals, cnt = np.unique(q, return_counts=True)
    top = sorted(zip(cnt, vals), reverse=True)[:6]
    print("  most-occupied levels (value: %% of sweep):")
    for c, v in top: print(f"      {v:.4f}  :  {100*c/len(r):5.1f}%")
    print()
