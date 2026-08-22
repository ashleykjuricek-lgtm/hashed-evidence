"""THE CONTROL.

The rose could be the TILING (real geometry) or the WINDOW'S CORNERS (an artefact
of the aperture we chose). Decagon window -> 10 lobes. Octagon window -> 8 lobes.
That pattern is exactly what corners would do.

So remove the corners. Same Z^5 -> R^2 projection, same shift magnitude, same
zeta, but a ROUND acceptance window. A circle has no preferred direction.

  If r(theta) goes FLAT   -> the rose is the aperture. It is a picture of the
                             observer, not of the tiling.
  If r(theta) KEEPS lobes -> the rose is in the point set. The tiling is doing it.

Matched by area so the two windows admit comparable numbers of points.
"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np
from penrose_gauntlet import PHI, decagon_proj, octagon_proj, poly_window, dedup, zeta, grid

MAG, S = 1/PHI**2, 2.0
TH = np.linspace(0, 2*np.pi, 721)

def round_window(perp, R, shift):
    p = perp - shift
    return (p[:, 0]**2 + p[:, 1]**2) < R*R

def sweep(proj_fn, N, D, winfn):
    Ppar, Pperp = proj_fn()
    g = grid(N, D); PAR = g @ Ppar.T; PERP = g @ Pperp.T
    base = zeta(dedup(PAR[winfn(PERP, np.zeros(2))]), S)
    return np.array([zeta(dedup(PAR[winfn(PERP, MAG*np.array([np.cos(t), np.sin(t)]))]), S)/base
                     for t in TH]), base

def report(tag, r):
    sw = r.max()-r.min()
    print(f"  {tag:34s} min={r.min():.6f} max={r.max():.6f} swing={sw:.6f}  ({100*sw/r.mean():5.2f}% of mean)")
    return sw

print("DECAGON PROJECTION (Penrose P3), N=8")
# decagon window, inradius 1  -> area = 10 * tan(pi/10) * 1^2
A = 10*np.tan(np.pi/10)
Rmatch = np.sqrt(A/np.pi)
r_poly, _ = sweep(decagon_proj, 8, 5, lambda P, s: poly_window(P, 5, 1.0, s))
sp = report("decagon window (10 corners)", r_poly)
r_rnd, _  = sweep(decagon_proj, 8, 5, lambda P, s: round_window(P, Rmatch, s))
sr = report(f"ROUND window (R={Rmatch:.5f}, area-matched)", r_rnd)
print(f"  -> round/polygon swing ratio = {sr/sp:.5f}")
print()
print("OCTAGON PROJECTION (silver), N=10")
A8 = 8*np.tan(np.pi/8); R8 = np.sqrt(A8/np.pi)
r8p, _ = sweep(octagon_proj, 10, 4, lambda P, s: poly_window(P, 4, 1.0, s))
s8p = report("octagon window (8 corners)", r8p)
r8r, _ = sweep(octagon_proj, 10, 4, lambda P, s: round_window(P, R8, s))
s8r = report(f"ROUND window (R={R8:.5f}, area-matched)", r8r)
print(f"  -> round/polygon swing ratio = {s8r/s8p:.5f}")
print()
print("VERDICT: a round-window swing near zero means the rose is the APERTURE.")
print("         a round-window swing comparable to the polygon's means it is the TILING.")
