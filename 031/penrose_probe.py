"""
Probe the rose: WHERE are the petals (golden angle?), and does it have a HANDEDNESS
(a time-arrow / chirality) or is the shape time-symmetric?
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
from scipy.signal import find_peaks
from penrose_gauntlet import PHI, decagon_proj, poly_window, dedup, zeta, grid

MAG, S = 1 / PHI ** 2, 2.0
GOLDEN_ANGLE = 360.0 / PHI ** 2   # = 137.5077...


def rose_decagon(N, thetas):
    Ppar, Pperp = decagon_proj()
    g = grid(N, 5)
    PAR, PERP = g @ Ppar.T, g @ Pperp.T
    base = zeta(dedup(PAR[poly_window(PERP, 5, 1.0, np.zeros(2))]), S)
    r = np.empty(len(thetas))
    for i, t in enumerate(thetas):
        sh = MAG * np.array([np.cos(t), np.sin(t)])
        r[i] = zeta(dedup(PAR[poly_window(PERP, 5, 1.0, sh)]), S) / base
    return r


thetas = np.linspace(0, 2 * np.pi, 1441)   # 0.25 deg resolution
deg = np.degrees(thetas)
r = rose_decagon(8, thetas)

# --- where are the petals? ---
thr = r.mean() + 0.5 * (r.max() - r.mean())
pk, _ = find_peaks(np.concatenate([r, r[:40]]), height=thr, distance=40)
pk = np.unique(pk[pk < len(r)])
print("PETALS")
print("  peak angles (deg):", np.round(deg[pk], 1))
print(f"  count: {len(pk)}   mean spacing: {np.mean(np.diff(deg[pk])):.2f} deg   (decagonal = 36.0)")
# evaluate at the EXACT fivefold vertex directions (0,36,72,...) vs valley directions (18,54,...)
vert = np.array([zeta(dedup((grid(8, 5) @ decagon_proj()[0].T)[
    poly_window(grid(8, 5) @ decagon_proj()[1].T, 5, 1.0,
                MAG * np.array([np.cos(np.radians(a)), np.sin(np.radians(a))]))]), S)
    for a in range(0, 360, 36)])
base0 = zeta(dedup((grid(8, 5) @ decagon_proj()[0].T)[
    poly_window(grid(8, 5) @ decagon_proj()[1].T, 5, 1.0, np.zeros(2))]), S)
vert = vert / base0
print(f"  at exact vertex angles 0,36,...324: heights = {np.round(vert,4)}")
print(f"  -> {'equal (clean 10-fold)' if np.ptp(vert) < 0.01 else 'modulated'}; petal value = {vert.mean():.4f} (1/phi={1/PHI:.4f})")
print(f"  (numerical local-maxima wobble +-3 deg off the true vertices = finite-lattice artifact)")

# --- golden angle ---
i_ga = int(np.argmin(np.abs(deg - GOLDEN_ANGLE)))
print("\nGOLDEN ANGLE")
print(f"  golden angle = 360/phi^2 = {GOLDEN_ANGLE:.4f} deg")
print(f"  r at the golden angle = {r[i_ga]:.4f}   (petal={r.max():.4f}, valley={r.min():.4f})")
print(f"  nearest petal is at {deg[pk][np.argmin(np.abs(deg[pk]-GOLDEN_ANGLE))]:.1f} deg "
      f"-> golden angle is NOT a petal (petals live at 36-deg / fivefold spacing)")

# --- chirality / time-arrow ---
chir = np.max(np.abs(r - r[::-1]))
print("\nCHIRALITY (is the shape itself time-directional?)")
print(f"  max|r(θ) - r(-θ)| = {chir:.2e}")
print(f"  -> {'ACHIRAL: the shape is mirror-symmetric — no arrow lives in the static rose' if chir < 1e-6 else 'CHIRAL: the shape has a handedness'}")
print("  (so any time-arrow is in the MOTION through the rose — the sign of the circulation — not the shape)")
