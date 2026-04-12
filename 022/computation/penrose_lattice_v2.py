"""
Penrose Lattice Zeta Computation v2
====================================
Fixed: proper decagonal acceptance window, duplicate removal,
maximal phason shifts, and better understanding of boundary conditions.

Key insight: In periodic case, APP means half-period shift in one direction.
In quasiperiodic case, the analog is shifting the acceptance window in
perpendicular space by specific amounts related to the decagonal geometry.

The "maximal" phason shift moves the acceptance window to an adjacent
Voronoi domain in perp-space — this is the quasiperiodic version of
flipping a boundary condition.
"""

import numpy as np
from itertools import product
from scipy.spatial import KDTree
from scipy.special import gamma as gamma_func
import json

PHI = (1 + np.sqrt(5)) / 2

def build_projection_matrices():
    """Build parallel and perpendicular projection matrices Z^5 → R^2."""
    angles_par = [2 * np.pi * k / 5 for k in range(5)]
    angles_perp = [4 * np.pi * k / 5 for k in range(5)]
    norm = np.sqrt(2.0 / 5.0)
    P_par = norm * np.array([[np.cos(a), np.sin(a)] for a in angles_par]).T
    P_perp = norm * np.array([[np.cos(a), np.sin(a)] for a in angles_perp]).T
    return P_par, P_perp


def in_decagon(points, radius=1.0, center=None):
    """Test if 2D points lie inside a regular decagon of given inradius."""
    if center is not None:
        points = points - center
    # A regular decagon with inradius r:
    # point (x,y) is inside iff for each edge normal n_k, |<p, n_k>| < r
    # Edge normals at angles π(2k+1)/10 for k=0..4
    inside = np.ones(len(points), dtype=bool)
    for k in range(5):
        angle = np.pi * (2*k + 1) / 10
        nx, ny = np.cos(angle), np.sin(angle)
        proj = np.abs(points[:, 0] * nx + points[:, 1] * ny)
        inside &= (proj < radius)
    return inside


def generate_penrose(N=8, window_radius=1.0, phason_shift=None, dedup_tol=1e-8):
    """
    Generate Penrose vertices via cut-and-project with decagonal window.
    Remove duplicates. Return unique vertices sorted by distance from origin.
    """
    P_par, P_perp = build_projection_matrices()

    coords = np.arange(-N, N+1, dtype=np.float64)
    # Build Z^5 grid
    grid = np.array(list(product(coords, repeat=5)))  # (M, 5)

    par = (P_par @ grid.T).T
    perp = (P_perp @ grid.T).T

    center = np.array(phason_shift) if phason_shift is not None else np.array([0.0, 0.0])

    # Decagonal acceptance window
    mask = in_decagon(perp, radius=window_radius, center=center)
    verts = par[mask]
    perp_accepted = perp[mask]

    # Remove duplicates
    if len(verts) > 0:
        tree = KDTree(verts)
        groups = tree.query_ball_tree(tree, dedup_tol)
        keep = set()
        seen = set()
        for i, group in enumerate(groups):
            canonical = min(group)
            if canonical not in seen:
                keep.add(canonical)
                seen.update(group)
        idx = sorted(keep)
        verts = verts[idx]
        perp_accepted = perp_accepted[idx]

    return verts, perp_accepted


def lattice_zeta_direct(vertices, s, r_min=1e-8):
    """Direct lattice sum Σ' |v|^{-2s}, excluding origin."""
    r_sq = np.sum(vertices**2, axis=1)
    mask = r_sq > r_min**2
    r_sq = r_sq[mask]
    return np.real(np.sum(r_sq ** (-s)))


def lattice_theta(vertices, t_array, r_min=1e-8):
    """Theta function Θ(t) = Σ' exp(-π|v|²t)."""
    r_sq = np.sum(vertices**2, axis=1)
    mask = r_sq > r_min**2
    r_sq = r_sq[mask]
    # Vectorized: shape (n_t, n_verts)
    return np.array([np.sum(np.exp(-np.pi * r_sq * t)) for t in t_array])


def lattice_zeta_mellin(vertices, s, t_min=1e-6, t_max=200, n_pts=5000, r_min=1e-8):
    """Lattice zeta via Mellin transform of theta function with analytic continuation."""
    t = np.logspace(np.log10(t_min), np.log10(t_max), n_pts)
    theta = lattice_theta(vertices, t, r_min)

    # Split integral at t=1
    # Z(s) = π^{-s}/Γ(s) [∫_0^1 t^{s-1}Θ(t)dt + ∫_1^∞ t^{s-1}Θ(t)dt]
    # For t > 1, the sum converges fine
    # For t < 1, we need the number of vertices N_v for regularization:
    #   Θ(t) → N_v as t → 0 (all terms → 1)
    #   Θ(t) - N_v/t  would be the "regularized" piece for Z² (via Poisson)
    #   But for Penrose, there's no exact Poisson summation

    # Simple approach: direct numerical Mellin for s where integral converges
    log_t = np.log(t)
    # Integrand in log-space: t^s * Θ(t) * d(log t)
    integrand = t**s * theta

    from scipy.integrate import trapezoid
    integral = trapezoid(integrand, log_t)

    return integral * np.pi**s / gamma_func(s)


def nearest_neighbor_analysis(vertices, r_min=1e-8):
    """Analyze nearest-neighbor distances and coordination numbers."""
    # Filter out origin
    r = np.sqrt(np.sum(vertices**2, axis=1))
    verts = vertices[r > r_min]

    tree = KDTree(verts)
    dists, _ = tree.query(verts, k=2)
    nn_dists = dists[:, 1]

    # Find characteristic distances
    # In Penrose tiling, there should be two edge lengths in ratio φ
    d_min = nn_dists.min()
    d_max = nn_dists.max()

    # Histogram to find peaks
    hist, bin_edges = np.histogram(nn_dists, bins=100)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Find the two dominant distances
    peaks = []
    for i in range(1, len(hist)-1):
        if hist[i] > hist[i-1] and hist[i] > hist[i+1] and hist[i] > 10:
            peaks.append(bin_centers[i])

    return nn_dists, peaks, verts


def compute_all_ratios(verts_base, verts_shifted_dict, s_values):
    """Compute shifted/unshifted ratios for all shift types and s values."""
    results = {}
    for s in s_values:
        z_base = lattice_zeta_direct(verts_base, s)
        results[s] = {'base': z_base, 'ratios': {}}
        for name, v in verts_shifted_dict.items():
            z_shifted = lattice_zeta_direct(v, s)
            ratio = z_shifted / z_base if abs(z_base) > 1e-15 else float('inf')
            results[s]['ratios'][name] = {
                'zeta': z_shifted,
                'ratio': ratio,
            }
    return results


def run():
    print("=" * 72)
    print("PENROSE LATTICE ZETA — v2 (decagonal window, deduped, maximal phasons)")
    print("=" * 72)
    print()

    # ─── Generate base Penrose lattice ───
    N = 8
    W = 1.0  # decagonal window inradius
    print(f"Generating Penrose vertices (N={N}, decagonal window R={W})...")
    verts_base, perp_base = generate_penrose(N=N, window_radius=W)
    print(f"  Base vertices: {len(verts_base)}")

    r = np.sqrt(np.sum(verts_base**2, axis=1))
    print(f"  Max radius: {r.max():.4f}")
    r_nonzero = r[r > 1e-8]
    print(f"  Min nonzero distance from origin: {r_nonzero.min():.6f}")
    print()

    # ─── Nearest-neighbor analysis ───
    print("─── Nearest-neighbor analysis ───")
    nn_dists, peaks, verts_nz = nearest_neighbor_analysis(verts_base)
    print(f"  NN distance range: [{nn_dists.min():.6f}, {nn_dists.max():.6f}]")
    if len(peaks) >= 2:
        print(f"  Two dominant distances: {peaks[0]:.6f}, {peaks[1]:.6f}")
        print(f"  Their ratio: {peaks[1]/peaks[0]:.6f} (φ = {PHI:.6f})")
    elif len(peaks) == 1:
        print(f"  Dominant distance: {peaks[0]:.6f}")
    print()

    # ─── Phason shifts ───
    # The key: in perp-space, the decagonal window has specific symmetry.
    # "Maximal phason" = shift by half the window diameter along a symmetry direction
    # This is analogous to the half-period shift in periodic case.
    #
    # For a decagon with inradius R=1:
    #   - Edge-to-edge distance = 2R = 2
    #   - Vertex-to-vertex distance = 2R/cos(π/10)
    #   - "Half period" analog = R (shift to the edge)
    #
    # We also try φ-scaled shifts since the self-similarity is governed by φ.

    shift_mag_half = W  # half the window — maximal disruption
    shift_mag_phi = W / PHI  # φ-scaled
    shift_mag_phi2 = W / PHI**2  # φ²-scaled
    shift_mag_quarter = W / 2  # quarter

    # Direction: along a vertex of the decagon (angle 0)
    # and along an edge midpoint (angle π/10)
    vertex_dir = np.array([1.0, 0.0])
    edge_dir = np.array([np.cos(np.pi/10), np.sin(np.pi/10)])

    shifts = {
        # Maximal shifts (half-window)
        'max_vertex':   shift_mag_half * vertex_dir,
        'max_edge':     shift_mag_half * edge_dir,
        # φ-scaled shifts
        'phi_vertex':   shift_mag_phi * vertex_dir,
        'phi_edge':     shift_mag_phi * edge_dir,
        # φ²-scaled shifts
        'phi2_vertex':  shift_mag_phi2 * vertex_dir,
        'phi2_edge':    shift_mag_phi2 * edge_dir,
        # Quarter shifts
        'qtr_vertex':   shift_mag_quarter * vertex_dir,
        'qtr_edge':     shift_mag_quarter * edge_dir,
    }

    shifted_lattices = {}
    print("─── Generating phason-shifted lattices ───")
    for name, shift in shifts.items():
        v, _ = generate_penrose(N=N, window_radius=W, phason_shift=shift)
        shifted_lattices[name] = v
        print(f"  {name:15s}: {len(v)} vertices (Δ = {len(v) - len(verts_base):+d} from base)")
    print()

    # ─── Direct lattice sums ───
    s_values = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
    print("─── Direct lattice sums Z(s) = Σ' |v|^{-2s} ───")
    print(f"  Base lattice:")
    for s in s_values:
        z = lattice_zeta_direct(verts_base, s)
        print(f"    Z(s={s:.1f}) = {z:.8f}")
    print()

    # ─── Ratios ───
    print("─── Shifted/Unshifted Ratios ───")
    all_ratios = compute_all_ratios(verts_base, shifted_lattices, s_values)

    for s in s_values:
        print(f"\n  s = {s:.1f}  (Z_base = {all_ratios[s]['base']:.8f})")
        for name, data in sorted(all_ratios[s]['ratios'].items()):
            r = data['ratio']
            # Check against known constants
            checks = {
                '1/24': 1/24,
                '1/φ': 1/PHI,
                '1/φ²': 1/PHI**2,
                'φ/24': PHI/24,
                '1/(φ·24)': 1/(PHI*24),
                '(φ-1)/φ': (PHI-1)/PHI,
                '2/5': 2/5,
                'φ²/24': PHI**2/24,
            }
            best_name, best_val = min(checks.items(), key=lambda kv: abs(r - kv[1]))
            diff = r - best_val
            print(f"    {name:15s}: ratio = {r:.8f}  nearest: {best_name} ({best_val:.8f}, Δ={diff:+.6f})")

    # ─── Mellin-regularized zeta at negative s ───
    print()
    print("─── Mellin-regularized lattice zeta (analytic continuation) ───")
    s_neg = [0.5, 0.25, -0.25, -0.5]

    for s in s_neg:
        z_base = lattice_zeta_mellin(verts_base, s)
        print(f"\n  s = {s:+.2f}: Z_base = {z_base:.8f}")
        for name in ['max_vertex', 'max_edge', 'phi_vertex', 'phi_edge']:
            z_sh = lattice_zeta_mellin(shifted_lattices[name], s)
            ratio = z_sh / z_base if abs(z_base) > 1e-15 else float('inf')
            print(f"    {name:15s}: Z_shifted = {z_sh:.8f}, ratio = {ratio:.8f}")

    # ─── Spectral analysis: vertex density and self-similarity ───
    print()
    print("─── Spectral self-similarity ───")
    # Count vertices in shells of radius r and r/φ
    # The ratio should reveal the deflation symmetry
    r_all = np.sqrt(np.sum(verts_base**2, axis=1))
    for R in [3.0, 4.0, 5.0, 6.0, 7.0]:
        n_R = np.sum(r_all < R)
        n_Rphi = np.sum(r_all < R/PHI)
        density_ratio = n_R / n_Rphi if n_Rphi > 0 else 0
        print(f"  N(r<{R:.0f}) = {n_R}, N(r<{R/PHI:.2f}) = {n_Rphi}, ratio = {density_ratio:.6f}, φ² = {PHI**2:.6f}")

    # ─── The ω connection ───
    print()
    print("─── Connection to COTT ω ───")
    print(f"  In COTT: ω = 1/0 (reciprocal of sunya-zero)")
    print(f"  W = √(-iπ) = √π · e^{{-iπ/4}}")
    print(f"  |W| = √π = {np.sqrt(np.pi):.6f}")
    print(f"  φ = (1+√5)/2 = {PHI:.6f}")
    print(f"  √π / φ = {np.sqrt(np.pi)/PHI:.6f}")
    print(f"  φ / √π = {PHI/np.sqrt(np.pi):.6f}")
    print(f"  φ² / π = {PHI**2/np.pi:.6f}")
    print(f"  log_φ(√π) = {np.log(np.sqrt(np.pi))/np.log(PHI):.6f}")

    # Check if any ratio at s=1 is close to a φ-W combination
    s1_ratios = all_ratios[1.0]['ratios']
    print()
    print(f"  Checking s=1 max_vertex ratio ({s1_ratios['max_vertex']['ratio']:.8f}) against φ-W combos:")
    rv = s1_ratios['max_vertex']['ratio']
    combos = {
        'φ': PHI,
        '1/φ': 1/PHI,
        '√π': np.sqrt(np.pi),
        'W_RE (√(π/2))': np.sqrt(np.pi/2),
        'φ·W_RE': PHI * np.sqrt(np.pi/2),
        'φ/√π': PHI/np.sqrt(np.pi),
        'φ²/π': PHI**2/np.pi,
        '2φ-1': 2*PHI-1,
        'φ+1/φ': PHI + 1/PHI,
        'ln(φ)': np.log(PHI),
        '1+1/φ²': 1 + 1/PHI**2,
        'φ/2': PHI/2,
        '1/(2-φ)': 1/(2-PHI),
    }
    for name, val in sorted(combos.items(), key=lambda kv: abs(rv - kv[1])):
        if abs(rv - val) < 0.5:
            print(f"    {name:20s} = {val:.8f} (Δ = {rv-val:+.8f})")

    # ─── Save results as JSON for the React viz ───
    print()
    print("─── Saving results ───")

    output = {
        'phi': PHI,
        'base_vertex_count': len(verts_base),
        'base_vertices_sample': verts_base[:500].tolist(),
        'nn_distance_peaks': peaks,
        's_values': s_values,
        'base_zeta': {str(s): lattice_zeta_direct(verts_base, s) for s in s_values},
        'ratios': {},
    }
    for s in s_values:
        output['ratios'][str(s)] = {}
        for name, data in all_ratios[s]['ratios'].items():
            output['ratios'][str(s)][name] = data['ratio']

    with open('/sessions/pensive-magical-bardeen/penrose_results.json', 'w') as f:
        json.dump(output, f, indent=2, default=str)

    # Save full vertex sets
    np.save('/sessions/pensive-magical-bardeen/penrose_base.npy', verts_base)
    for name, v in shifted_lattices.items():
        np.save(f'/sessions/pensive-magical-bardeen/penrose_{name}.npy', v)

    print("  Results saved to penrose_results.json and .npy files")
    print()
    print("=" * 72)
    print("DONE")
    print("=" * 72)


if __name__ == "__main__":
    run()
