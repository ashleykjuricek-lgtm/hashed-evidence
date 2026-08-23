"""What sets the lobe width?  (v2 -- seam-corrected)

v1 reported 11 lobes on a 10-fold window, which is impossible: the run detector
split a lobe across the 0/360 seam. Fixed here (wrap handled, 0.25 deg resolution,
as in 045). v1's verdict is discarded, not patched.

Test: MAG is a free parameter of the recipe (022 chose 1/phi^2). If lobe width
tracks MAG, the 8 deg of 045 is a geometric overlap effect, not a property of the
tiling."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
from penrose_gauntlet import PHI, decagon_proj, octagon_proj, poly_window, dedup, zeta, grid

S = 2.0
TH = np.linspace(0, 2*np.pi, 1441)[:-1]      # drop duplicate endpoint
DEG = np.degrees(TH)
STEP = 360.0/len(TH)

def rose_at(proj_fn, half, D, N, mag):
    Ppar, Pperp = proj_fn()
    g = grid(N, D); PAR = g @ Ppar.T; PERP = g @ Pperp.T
    base = zeta(dedup(PAR[poly_window(PERP, half, 1.0, np.zeros(2))]), S)
    return np.array([zeta(dedup(PAR[poly_window(PERP, half, 1.0,
                     mag*np.array([np.cos(t), np.sin(t)]))]), S)/base for t in TH])

def lobes(r):
    """count contiguous high runs on a CIRCLE (wrap-aware)"""
    hi = r > 0.5*(r.min()+r.max())
    n = len(hi)
    if hi.all() or not hi.any(): return 0, 0.0
    start = next(i for i in range(n) if hi[i] and not hi[i-1])   # i-1 wraps
    runs, i, cnt = [], 0, 0
    while i < n:
        k = (start+i) % n
        if hi[k]: cnt += 1
        else:
            if cnt: runs.append(cnt*STEP)
            cnt = 0
        i += 1
    if cnt: runs.append(cnt*STEP)
    return len(runs), float(np.mean(runs))

for name, proj, half, D, N, fold in [("DECAGON (10-fold window)", decagon_proj, 5, 5, 8, 10),
                                     ("OCTAGON  (8-fold window)", octagon_proj, 4, 4, 10, 8)]:
    print(name, "   022 used mag = 1/phi^2 = %.5f" % (1/PHI**2))
    print("    mag      lobes   width(deg)    duty      swing      count ok")
    for mag in [0.05, 0.1, 0.2, 1/PHI**2, 0.5, 0.7, 0.9]:
        r = rose_at(proj, half, D, N, mag)
        n, w = lobes(r)
        duty = w/(360.0/n) if n else 0.0
        star = "  <- 022" if abs(mag-1/PHI**2) < 1e-9 else ""
        print(f"   {mag:6.4f}   {n:4d}    {w:8.3f}    {duty:6.4f}   {r.max()-r.min():8.5f}"
              f"    {'yes' if n==fold else 'NO ('+str(fold)+' expected)'}{star}")
        sys.stdout.flush()
    print()
