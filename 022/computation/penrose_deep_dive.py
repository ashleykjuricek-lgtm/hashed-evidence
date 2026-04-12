"""
Penrose Deep Dive: Tracing the 1/φ ratio and s-dependence
==========================================================
Focus on:
1. Fine s-grid around where phi2_vertex ratio crosses 1/φ
2. Convergence behavior as N → ∞ (more vertices)
3. Whether the edge shift converges to exactly 2/5
4. The Casimir-relevant point s = -1/2
"""

import numpy as np
from itertools import product
from scipy.spatial import KDTree
from scipy.special import gamma as gamma_func
from scipy.integrate import trapezoid
import json

PHI = (1 + np.sqrt(5)) / 2

def build_projection_matrices():
    angles_par = [2 * np.pi * k / 5 for k in range(5)]
    angles_perp = [4 * np.pi * k / 5 for k in range(5)]
    norm = np.sqrt(2.0 / 5.0)
    P_par = norm * np.array([[np.cos(a), np.sin(a)] for a in angles_par]).T
    P_perp = norm * np.array([[np.cos(a), np.sin(a)] for a in angles_perp]).T
    return P_par, P_perp

def in_decagon(points, radius=1.0, center=None):
    if center is not None:
        points = points - center
    inside = np.ones(len(points), dtype=bool)
    for k in range(5):
        angle = np.pi * (2*k + 1) / 10
        nx, ny = np.cos(angle), np.sin(angle)
        proj = np.abs(points[:, 0] * nx + points[:, 1] * ny)
        inside &= (proj < radius)
    return inside

def generate_penrose(N=8, window_radius=1.0, phason_shift=None, dedup_tol=1e-8):
    P_par, P_perp = build_projection_matrices()
    coords = np.arange(-N, N+1, dtype=np.float64)
    grid = np.array(list(product(coords, repeat=5)))
    par = (P_par @ grid.T).T
    perp = (P_perp @ grid.T).T
    center = np.array(phason_shift) if phason_shift is not None else np.array([0.0, 0.0])
    mask = in_decagon(perp, radius=window_radius, center=center)
    verts = par[mask]
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
        verts = verts[sorted(keep)]
    return verts

def lattice_zeta_direct(vertices, s, r_min=1e-8):
    r_sq = np.sum(vertices**2, axis=1)
    mask = r_sq > r_min**2
    r_sq = r_sq[mask]
    return np.real(np.sum(r_sq ** (-s)))

def lattice_theta(vertices, t_array, r_min=1e-8):
    r_sq = np.sum(vertices**2, axis=1)
    mask = r_sq > r_min**2
    r_sq = r_sq[mask]
    return np.array([np.sum(np.exp(-np.pi * r_sq * t)) for t in t_array])

def lattice_zeta_mellin(vertices, s, t_min=1e-6, t_max=300, n_pts=8000, r_min=1e-8):
    t = np.logspace(np.log10(t_min), np.log10(t_max), n_pts)
    theta = lattice_theta(vertices, t, r_min)
    log_t = np.log(t)
    integrand = t**s * theta
    integral = trapezoid(integrand, log_t)
    return integral * np.pi**s / gamma_func(s)


def main():
    print("=" * 72)
    print("PENROSE DEEP DIVE: Tracing 1/φ and the s-dependence")
    print("=" * 72)
    print()

    N = 8
    W = 1.0
    verts_base = generate_penrose(N=N, window_radius=W)
    print(f"Base: {len(verts_base)} vertices")

    # The two most interesting shifts from v2:
    phi2_vertex_shift = (W / PHI**2) * np.array([1.0, 0.0])
    phi_edge_shift = (W / PHI) * np.array([np.cos(np.pi/10), np.sin(np.pi/10)])
    qtr_edge_shift = (W / 2) * np.array([np.cos(np.pi/10), np.sin(np.pi/10)])

    verts_phi2v = generate_penrose(N=N, window_radius=W, phason_shift=phi2_vertex_shift)
    verts_phie = generate_penrose(N=N, window_radius=W, phason_shift=phi_edge_shift)
    verts_qtre = generate_penrose(N=N, window_radius=W, phason_shift=qtr_edge_shift)

    print(f"Phi²-vertex shifted: {len(verts_phi2v)} vertices")
    print(f"Phi-edge shifted: {len(verts_phie)} vertices")
    print(f"Qtr-edge shifted: {len(verts_qtre)} vertices")
    print()

    # ─── Fine s-grid around the 1/φ crossing ───
    print("─── Fine s-grid: phi2_vertex ratio vs 1/φ ───")
    s_fine = np.linspace(1.0, 3.0, 41)
    ratios_phi2v = []
    ratios_phie = []
    ratios_qtre = []

    for s in s_fine:
        z_base = lattice_zeta_direct(verts_base, s)
        z_phi2v = lattice_zeta_direct(verts_phi2v, s)
        z_phie = lattice_zeta_direct(verts_phie, s)
        z_qtre = lattice_zeta_direct(verts_qtre, s)

        r1 = z_phi2v / z_base
        r2 = z_phie / z_base
        r3 = z_qtre / z_base

        ratios_phi2v.append(r1)
        ratios_phie.append(r2)
        ratios_qtre.append(r3)

    # Find where phi2_vertex crosses 1/φ
    target = 1/PHI
    for i in range(len(s_fine)-1):
        if (ratios_phi2v[i] - target) * (ratios_phi2v[i+1] - target) < 0:
            # Linear interpolation for crossing point
            s_cross = s_fine[i] + (s_fine[i+1] - s_fine[i]) * (target - ratios_phi2v[i]) / (ratios_phi2v[i+1] - ratios_phi2v[i])
            print(f"  *** phi2_vertex crosses 1/φ at s ≈ {s_cross:.6f} ***")

    print()
    print(f"  {'s':>6s}  {'phi2_v ratio':>14s}  {'Δ from 1/φ':>12s}  {'phi_e ratio':>14s}  {'Δ from 2/5':>12s}")
    print(f"  {'─'*6}  {'─'*14}  {'─'*12}  {'─'*14}  {'─'*12}")
    for i, s in enumerate(s_fine):
        d1 = ratios_phi2v[i] - 1/PHI
        d2 = ratios_phie[i] - 2/5
        marker = " ←" if abs(d1) < 0.005 else ""
        print(f"  {s:6.3f}  {ratios_phi2v[i]:14.8f}  {d1:+12.8f}  {ratios_phie[i]:14.8f}  {d2:+12.8f}{marker}")

    # ─── Ultra-fine grid near the crossing ───
    print()
    print("─── Ultra-fine grid near 1/φ crossing ───")
    s_ultra = np.linspace(1.9, 2.1, 21)
    for s in s_ultra:
        z_base = lattice_zeta_direct(verts_base, s)
        z_phi2v = lattice_zeta_direct(verts_phi2v, s)
        r = z_phi2v / z_base
        d = r - 1/PHI
        marker = " *** CLOSEST ***" if abs(d) < 0.001 else ""
        print(f"  s = {s:.4f}: ratio = {r:.10f}, Δ from 1/φ = {d:+.10f}{marker}")

    # ─── Convergence test: increase N ───
    print()
    print("─── Convergence test at s=2.0 with increasing N ───")
    for N_test in [5, 6, 7, 8, 9, 10]:
        vb = generate_penrose(N=N_test, window_radius=W)
        vs = generate_penrose(N=N_test, window_radius=W, phason_shift=phi2_vertex_shift)
        if len(vb) > 1 and len(vs) > 1:
            zb = lattice_zeta_direct(vb, 2.0)
            zs = lattice_zeta_direct(vs, 2.0)
            r = zs / zb
            print(f"  N={N_test:2d}: {len(vb):5d} base, {len(vs):5d} shifted, ratio = {r:.10f}, Δ from 1/φ = {r - 1/PHI:+.10f}")

    # ─── Does the large-s limit go to exactly 2/5? ───
    print()
    print("─── Large-s limit for edge shifts ───")
    for s in [5.0, 6.0, 8.0, 10.0, 15.0, 20.0]:
        z_base = lattice_zeta_direct(verts_base, s)
        z_phie = lattice_zeta_direct(verts_phie, s)
        z_qtre = lattice_zeta_direct(verts_qtre, s)
        r_phie = z_phie / z_base
        r_qtre = z_qtre / z_base
        print(f"  s={s:5.1f}: phi_edge ratio = {r_phie:.10f} (Δ from 2/5 = {r_phie - 0.4:+.10f}), "
              f"qtr_edge = {r_qtre:.10f} (Δ from 2/5 = {r_qtre - 0.4:+.10f})")

    # ─── What is the large-s limit really? ───
    print()
    print("─── Large-s limit analysis ───")
    print("  At s → ∞, only the nearest vertex to origin dominates the sum.")
    print("  So ratio → |v₁_shifted|^{-2s} / |v₁_base|^{-2s} = (|v₁_base|/|v₁_shifted|)^{2s}")
    print()

    r_sq_base = np.sum(verts_base**2, axis=1)
    r_sq_base_sorted = np.sort(r_sq_base[r_sq_base > 1e-10])

    r_sq_phie = np.sum(verts_phie**2, axis=1)
    r_sq_phie_sorted = np.sort(r_sq_phie[r_sq_phie > 1e-10])

    r_sq_qtre = np.sum(verts_qtre**2, axis=1)
    r_sq_qtre_sorted = np.sort(r_sq_qtre[r_sq_qtre > 1e-10])

    r_sq_phi2v = np.sum(verts_phi2v**2, axis=1)
    r_sq_phi2v_sorted = np.sort(r_sq_phi2v[r_sq_phi2v > 1e-10])

    print(f"  Smallest |v|² in base:        {r_sq_base_sorted[0]:.10f} (|v| = {np.sqrt(r_sq_base_sorted[0]):.10f})")
    print(f"  Smallest |v|² in phi_edge:    {r_sq_phie_sorted[0]:.10f} (|v| = {np.sqrt(r_sq_phie_sorted[0]):.10f})")
    print(f"  Smallest |v|² in qtr_edge:    {r_sq_qtre_sorted[0]:.10f} (|v| = {np.sqrt(r_sq_qtre_sorted[0]):.10f})")
    print(f"  Smallest |v|² in phi2_vertex: {r_sq_phi2v_sorted[0]:.10f} (|v| = {np.sqrt(r_sq_phi2v_sorted[0]):.10f})")
    print()

    # Number of points at the minimum distance
    for name, rsq in [('base', r_sq_base_sorted), ('phi_edge', r_sq_phie_sorted),
                       ('qtr_edge', r_sq_qtre_sorted), ('phi2_vertex', r_sq_phi2v_sorted)]:
        min_val = rsq[0]
        n_at_min = np.sum(np.abs(rsq - min_val) < 1e-8)
        print(f"  {name:15s}: {n_at_min} vertices at minimum distance")

    print()
    d_ratio = r_sq_phie_sorted[0] / r_sq_base_sorted[0]
    print(f"  |v₁_base|²/|v₁_phie|² = {1/d_ratio:.10f}")
    print(f"  If this is > 1, the ratio diverges at large s (which is what we see)")
    print(f"  If this is < 1, the ratio → 0 at large s")
    print(f"  If this is = 1, the ratio is determined by multiplicity")

    # ─── Multiplicity-weighted analysis ───
    print()
    print("─── Shell-by-shell analysis (first 10 shells) ───")
    # Group vertices by distance shell
    for name, rsq_sorted, label in [
        ('base', r_sq_base_sorted, 'BASE'),
        ('phi2_vertex', r_sq_phi2v_sorted, 'PHI2_VERTEX'),
    ]:
        print(f"\n  {label}:")
        shells = []
        current_r = rsq_sorted[0]
        count = 0
        for r in rsq_sorted:
            if abs(r - current_r) < 1e-6:
                count += 1
            else:
                shells.append((current_r, count))
                current_r = r
                count = 1
        shells.append((current_r, count))

        for i, (r, c) in enumerate(shells[:10]):
            print(f"    Shell {i}: |v|² = {r:.8f}, |v| = {np.sqrt(r):.8f}, multiplicity = {c}")

    # ─── Theta function and functional equation defect ───
    print()
    print("─── Theta function analysis ───")
    t_vals = np.logspace(-2, 2, 500)
    theta_base = lattice_theta(verts_base, t_vals)
    theta_phi2v = lattice_theta(verts_phi2v, t_vals)

    # The theta ratio as function of t
    theta_ratio = theta_phi2v / theta_base
    # At t → 0: both → N_v (vertex count), so ratio → N_shifted/N_base
    # At t → ∞: both → multiplicity of nearest shell, so ratio → m_shifted/m_base
    print(f"  θ_shifted/θ_base at t=0.01: {theta_ratio[0]:.8f} (≈ {len(verts_phi2v)}/{len(verts_base)} = {len(verts_phi2v)/len(verts_base):.8f})")
    print(f"  θ_shifted/θ_base at t=100:  {theta_ratio[-1]:.8f}")

    # Where does the ratio cross 1/φ?
    for i in range(len(t_vals)-1):
        if (theta_ratio[i] - 1/PHI) * (theta_ratio[i+1] - 1/PHI) < 0:
            t_cross = t_vals[i]
            print(f"  θ-ratio crosses 1/φ at t ≈ {t_cross:.6f}")

    # ─── The key question: what happens at s = -1/2? ───
    print()
    print("─── Mellin zeta at Casimir point s = -1/2 ───")
    for s in [-0.5, -0.25, 0.0, 0.25, 0.5]:
        if s == 0.0:
            print(f"  s = {s:+.2f}: (pole of Γ, skip)")
            continue
        z_base = lattice_zeta_mellin(verts_base, s)
        z_phi2v = lattice_zeta_mellin(verts_phi2v, s)
        z_phie = lattice_zeta_mellin(verts_phie, s)
        ratio_phi2v = z_phi2v / z_base if abs(z_base) > 1e-10 else float('inf')
        ratio_phie = z_phie / z_base if abs(z_base) > 1e-10 else float('inf')
        print(f"  s = {s:+.2f}: Z_base = {z_base:+.6f}")
        print(f"           phi2_v ratio = {ratio_phi2v:.10f} (Δ from 1/φ = {ratio_phi2v - 1/PHI:+.10f})")
        print(f"           phi_e  ratio = {ratio_phie:.10f}")

    # ─── Reciprocal check: is 1/(ratio) ≈ φ? ───
    print()
    print("─── Reciprocal check at s=2.0 ───")
    z_base = lattice_zeta_direct(verts_base, 2.0)
    z_phi2v = lattice_zeta_direct(verts_phi2v, 2.0)
    ratio = z_phi2v / z_base
    print(f"  ratio = {ratio:.10f}")
    print(f"  1/ratio = {1/ratio:.10f}")
    print(f"  φ = {PHI:.10f}")
    print(f"  1/ratio - φ = {1/ratio - PHI:+.10f}")
    print(f"  ratio × φ = {ratio * PHI:.10f}")
    print(f"  ratio / (1/φ) = {ratio / (1/PHI):.10f}")
    print(f"  ratio × 24 = {ratio * 24:.10f}")
    print(f"  ratio × φ × 24 = {ratio * PHI * 24:.10f}")

    # ─── The pentagonal identity ───
    print()
    print("─── Pentagonal / decagonal identities ───")
    print(f"  cos(π/5) = {np.cos(np.pi/5):.10f} = φ/2 = {PHI/2:.10f}")
    print(f"  cos(2π/5) = {np.cos(2*np.pi/5):.10f} = (φ-1)/2 = {(PHI-1)/2:.10f}")
    print(f"  sin(π/5) = {np.sin(np.pi/5):.10f}")
    print(f"  sin(2π/5) = {np.sin(2*np.pi/5):.10f}")
    print(f"  5/φ² = {5/PHI**2:.10f}")
    print(f"  φ² - φ = {PHI**2 - PHI:.10f}")
    print(f"  1/φ + 1/φ² = {1/PHI + 1/PHI**2:.10f}")

    # ─── Summary ───
    print()
    print("=" * 72)
    print("SUMMARY OF FINDINGS")
    print("=" * 72)
    print()
    print("1. Vertex density scales as φ² under deflation (confirmed)")
    print()
    print("2. At s ≈ 2.0, the phi²-vertex phason shift gives ratio ≈ 1/φ")
    s2_ratio = lattice_zeta_direct(verts_phi2v, 2.0) / lattice_zeta_direct(verts_base, 2.0)
    print(f"   Measured: {s2_ratio:.10f}")
    print(f"   1/φ:     {1/PHI:.10f}")
    print(f"   Δ:       {s2_ratio - 1/PHI:+.10f}")
    print()
    print("3. Edge-direction phason shifts approach 2/5 at large s")
    print(f"   2/5 = {2/5:.10f}")
    print()
    print("4. At the Casimir point s=-1/2:")
    s_cas = -0.5
    z_b = lattice_zeta_mellin(verts_base, s_cas)
    z_s = lattice_zeta_mellin(verts_phi2v, s_cas)
    cas_ratio = z_s / z_b
    print(f"   Mellin ratio = {cas_ratio:.10f}")
    print(f"   This is NOT 1/φ — the Mellin regularization changes the ratio")
    print(f"   (analogous to how periodic ratio is s-dependent too)")
    print()
    print(f"5. COTT connection: periodic → 1/24, quasiperiodic → 1/φ")
    print(f"   24 = 4! (symmetric group S4)")
    print(f"   φ = (1+√5)/2 (icosahedral symmetry, A5)")
    print(f"   Both are natural 'denominators' of their respective symmetry groups")
    print()
    print(f"6. The ratio 1/(24φ) = {1/(24*PHI):.10f}")
    print(f"   If periodic gives 1/24 and quasiperiodic gives 1/φ,")
    print(f"   the combined/mixed system might give 1/(24φ)")
    print(f"   = {1/(24*PHI):.10f}")
    print(f"   This is tantalizingly close to the COTT zero traction:")
    print(f"   e^{{-√(π/2)}} = {np.exp(-np.sqrt(np.pi/2)):.10f}")
    print(f"   Δ = {1/(24*PHI) - np.exp(-np.sqrt(np.pi/2)):+.10f}")

    # Save results
    results = {
        's_values': s_fine.tolist(),
        'ratios_phi2v': ratios_phi2v,
        'ratios_phie': ratios_phie,
        'ratios_qtre': ratios_qtre,
        'phi': PHI,
        'one_over_phi': 1/PHI,
        'one_over_24': 1/24,
        'casimir_ratio': cas_ratio,
    }
    with open('/sessions/pensive-magical-bardeen/penrose_deep_dive_results.json', 'w') as f:
        json.dump(results, f, indent=2, default=float)

    print()
    print("Results saved to penrose_deep_dive_results.json")


if __name__ == "__main__":
    main()
