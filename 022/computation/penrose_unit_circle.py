"""
Plot the direction-dependent Penrose ratio on the unit circle.
Overlay W, ω, and the COTT structure constants.
"""

import numpy as np
from itertools import product
from scipy.spatial import KDTree
import json

PHI = (1 + np.sqrt(5)) / 2

def build_proj():
    norm = np.sqrt(2/5)
    P_par = np.array([[norm*np.cos(2*np.pi*k/5), norm*np.sin(2*np.pi*k/5)] for k in range(5)]).T
    P_perp = np.array([[norm*np.cos(4*np.pi*k/5), norm*np.sin(4*np.pi*k/5)] for k in range(5)]).T
    return P_par, P_perp

P_par, P_perp = build_proj()

def in_decagon(pts, r=1.0, cx=0, cy=0):
    pts = pts.copy()
    pts[:, 0] -= cx; pts[:, 1] -= cy
    inside = np.ones(len(pts), dtype=bool)
    for k in range(5):
        a = np.pi*(2*k+1)/10
        inside &= np.abs(pts[:,0]*np.cos(a) + pts[:,1]*np.sin(a)) < r
    return inside

def gen(N, W=1.0, sx=0, sy=0):
    coords = np.arange(-N, N+1, dtype=np.float64)
    grid = np.array(list(product(coords, repeat=5)))
    par = (P_par @ grid.T).T
    perp = (P_perp @ grid.T).T
    mask = in_decagon(perp, W, sx, sy)
    v = par[mask]
    if len(v) > 0:
        tree = KDTree(v)
        groups = tree.query_ball_tree(tree, 1e-8)
        keep = set(); seen = set()
        for i, g in enumerate(groups):
            c = min(g)
            if c not in seen:
                keep.add(c); seen.update(g)
        v = v[sorted(keep)]
    return v

def zeta(v, s):
    r2 = np.sum(v**2, axis=1)
    r2 = r2[r2 > 1e-12]
    return np.sum(r2**(-s))

# Generate base
N = 8
vb = gen(N)
print(f"Base: {len(vb)} vertices")

# Scan all directions at 1° resolution
shift_mag = 1.0 / PHI**2  # phi^2 scaled shift
angles = np.arange(0, 360, 1)
ratios = []

for deg in angles:
    rad = deg * np.pi / 180
    sx = shift_mag * np.cos(rad)
    sy = shift_mag * np.sin(rad)
    vs = gen(N, sx=sx, sy=sy)
    r = zeta(vs, 2.0) / zeta(vb, 2.0)
    ratios.append(r)
    if deg % 36 == 0:
        print(f"  {deg:3d}°: ratio = {r:.8f}")

ratios = np.array(ratios)

# Key statistics
print(f"\nRatio statistics:")
print(f"  Max: {ratios.max():.8f} at {angles[np.argmax(ratios)]}°")
print(f"  Min: {ratios.min():.8f} at {angles[np.argmin(ratios)]}°")
print(f"  Mean: {ratios.mean():.8f}")
print(f"  Std: {ratios.std():.8f}")
print(f"  1/φ = {1/PHI:.8f}")
print(f"  Mean/1/φ = {ratios.mean()/(1/PHI):.8f}")

# Gaussian-smoothed version (what you'd get if you averaged)
from scipy.ndimage import gaussian_filter1d
smoothed = gaussian_filter1d(ratios, sigma=30, mode='wrap')

print(f"\n  Smoothed mean: {smoothed.mean():.8f}")
print(f"  Smoothed std: {smoothed.std():.8f}")

# The smoothed version approaches a circle (constant)
print(f"  Smoothed max-min: {smoothed.max() - smoothed.min():.8f}")

# COTT angles
W_angle = -45  # W = √π · e^{-iπ/4}
omega_angle = 45  # ω = conjugate

print(f"\n  Ratio at W angle (-45°/315°): {ratios[315]:.8f}")
print(f"  Ratio at ω angle (45°): {ratios[45]:.8f}")
print(f"  Ratio at 0° (vertex): {ratios[0]:.8f}")
print(f"  Ratio at 36° (vertex): {ratios[36]:.8f}")

# Where exactly are the peaks?
peak_angles = []
for i in range(len(ratios)):
    prev = ratios[(i-1) % 360]
    next = ratios[(i+1) % 360]
    if ratios[i] > prev and ratios[i] > next and ratios[i] > 0.6:
        peak_angles.append((angles[i], ratios[i]))

print(f"\nPeak directions:")
for deg, r in peak_angles:
    print(f"  {deg}°: {r:.8f}")

# Valley analysis
valley_angles = []
for i in range(len(ratios)):
    prev = ratios[(i-1) % 360]
    next_r = ratios[(i+1) % 360]
    if ratios[i] < prev and ratios[i] < next_r and ratios[i] < 0.55:
        valley_angles.append((angles[i], ratios[i]))

print(f"\nValley directions:")
for deg, r in valley_angles[:10]:
    print(f"  {deg}°: {r:.8f}")

# What IS the valley value?
valley_vals = [r for _, r in valley_angles]
if valley_vals:
    mean_valley = np.mean(valley_vals)
    print(f"\nMean valley value: {mean_valley:.8f}")
    # Check against known constants
    checks = {
        '1/2': 0.5,
        'cos(π/5)·1/φ': np.cos(np.pi/5)/PHI,
        'cos(2π/5)+1/2': np.cos(2*np.pi/5) + 0.5,
        '(1+1/φ)/2 - 1/φ': (1+1/PHI)/2 - 1/PHI,
        'e^{-W_RE}/φ': np.exp(-np.sqrt(np.pi/2)) * PHI,
        '1/φ - 1/(φ·5)': 1/PHI - 1/(PHI*5),
    }
    for name, val in sorted(checks.items(), key=lambda kv: abs(mean_valley - kv[1])):
        print(f"  {name:30s} = {val:.8f} (Δ = {mean_valley - val:+.8f})")

# Save for visualization
output = {
    'angles_deg': angles.tolist(),
    'ratios': ratios.tolist(),
    'smoothed': smoothed.tolist(),
    'phi': PHI,
    'one_over_phi': 1/PHI,
    'peak_angles': [p[0] for p in peak_angles],
    'valley_mean': float(np.mean(valley_vals)) if valley_vals else 0,
    'W_angle': -45,
    'omega_angle': 45,
    'mean_ratio': float(ratios.mean()),
}

with open('/sessions/pensive-magical-bardeen/unit_circle_data.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\nSaved to unit_circle_data.json")
