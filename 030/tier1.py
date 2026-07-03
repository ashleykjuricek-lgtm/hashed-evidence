"""
TIER-1 QUASICRYSTAL OPERATOR EXPERIMENT
=======================================

Plain-language map of what this does:

  1. Build a small chunk of the 3D icosahedral quasicrystal the *right* way:
     project the 6D integer lattice (Z^6) down to 3D, keeping a point only if its
     "hidden shadow" (internal coordinate) lands inside the rhombic triacontahedron
     window -- NOT a ball. The triacontahedron is the shadow of the 6D unit cube,
     and it is what carries the icosahedral symmetry.

  2. Turn that point cloud into a graph (connect near neighbours).

  3. On the graph build two operators:
        S  = "smoothing"   -> each point relaxes toward its neighbours (symmetric)
        K  = "circulation" -> each point STIRS its neighbours (antisymmetric)
     K is a 50/50 blend (ALPHA) of:
        - icosahedral-geometry swirl: cross-products of the 3D positions, about an
          icosahedral 5-fold axis
        - hidden-shadow swirl: the same, but using the internal/perp coordinate
     The dial is   O_delta = S + delta * K   with delta in {-1, 0, +1} (and a sweep).

  4. Measure three things and ASK three crisp questions:
        (a) Spectrum of O_delta as delta sweeps. Claim under test: delta=0 is the
            ONLY place the eigenvalues are purely real (self-adjoint point). We expect
            this to be TRUE but TRIVIAL -- it falls straight out of S=S^T, K=-K^T.
            The plot of max|Im(lambda)| vs delta should sit at ~0 at delta=0.
        (b) The commutator [S,K] = S@K - K@S. Claim: it is SYMMETRIC (so it behaves
            like an effective "eddy diffusivity", not like rotation). We check the
            residual ||C - C^T|| and look at its (real) spectrum.
        (c) Heat trace H(t) = Re Tr(exp(t*O_delta)). Sanity: stays bounded/decaying
            for all delta, because the antisymmetric K cannot push Re(lambda) above 0.

  5. CONTROLS (fair ones):
        - quasicrystal : real golden ratio (irrational slope) -> genuine quasicrystal
        - periodic     : golden ratio swapped for a rational (13/8) -> a periodic
                         crystal built by the SAME machinery (textbook control)
        - random       : random points in a ball, with random shadow coords
     If the quasicrystal does something the controls don't, that's signal.
     If they all look alike, the effect is generic -- also worth knowing.

This is Tier-1 only: clean, falsifiable linear-algebra facts. It deliberately does
NOT go looking for "modular-looking" structure -- that is Tier-2 and needs sharp,
pre-registered yes/no thresholds before any code runs.
"""

import os
import numpy as np
from numpy.linalg import norm, eig
from scipy.spatial import cKDTree
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2

# ----------------------------- knobs you can turn -----------------------------
LATTICE_R   = 3        # how far out in 6D we scan (each coordinate in -R..R)
PHYS_RADIUS = 3.0      # keep quasicrystal points within this distance of the origin
K_NEIGHBORS = 6        # each point wires to its k nearest neighbours (same k for all 3 -> fair comparison)
ALPHA       = 0.5      # K blend: 0 = all icosahedral geometry, 1 = all hidden shadow
DELTA_SWEEP = np.linspace(-1, 1, 41)
DELTAS_KEY  = [-1.0, 0.0, 1.0]
HEAT_TS     = np.linspace(0.0, 3.0, 60)
RNG_SEED    = 12345
# -----------------------------------------------------------------------------


def star_vectors(phi):
    """The 6 physical + 6 internal 'star' vectors (as columns), parameterised by phi.

    phi = golden ratio          -> icosahedral quasicrystal
    phi = rational (e.g. 13/8)  -> periodic crystal (same construction, commensurate)
    """
    pc = 1.0 - phi  # conjugate slope (Galois conjugate of the true golden ratio)
    par = np.array([
        [0.0, 0.0, 1.0,  1.0,  phi, -phi],
        [1.0, 1.0, phi, -phi,  0.0,  0.0],
        [phi, -phi, 0.0, 0.0,  1.0,  1.0],
    ])
    perp = np.array([
        [0.0, 0.0, 1.0,  1.0,  pc, -pc],
        [1.0, 1.0, pc, -pc,  0.0,  0.0],
        [pc, -pc, 0.0, 0.0,  1.0,  1.0],
    ])
    nrm = np.sqrt(2.0 + abs(phi))
    return par / nrm, perp / nrm


def in_triacontahedron(xperp, perp_gens, tol=1e-9):
    """Is each internal-space point inside the rhombic triacontahedron window?

    The window is the zonotope of the 6 internal generators over [-1/2, 1/2].
    A 3D zonotope with 6 generators has 30 faces in 15 parallel pairs; each pair's
    normal is the cross product of two generators, and the half-width in that
    direction is 1/2 * sum_k |g_k . n|. A point is inside iff it passes all 15 tests.
    """
    G = perp_gens.T  # (6,3): rows are the generators
    inside = np.ones(len(xperp), dtype=bool)
    for i in range(6):
        for j in range(i + 1, 6):
            n = np.cross(G[i], G[j])
            ln = norm(n)
            if ln < 1e-12:
                continue
            n = n / ln
            halfwidth = 0.5 * np.sum(np.abs(G @ n))
            inside &= (np.abs(xperp @ n) <= halfwidth + tol)
    return inside


def make_cut_and_project(phi, lattice_r, phys_radius):
    """Build a patch via the cut-and-project method. Returns (xpar, xperp, axes)."""
    coords = np.arange(-lattice_r, lattice_r + 1)
    grid = np.array(np.meshgrid(*([coords] * 6), indexing="ij")).reshape(6, -1).T
    par, perp = star_vectors(phi)
    xpar = grid @ par.T
    xperp = grid @ perp.T
    keep = in_triacontahedron(xperp, perp) & (norm(xpar, axis=1) <= phys_radius)
    axis_par = par[:, 0] / norm(par[:, 0])      # an icosahedral 5-fold axis (physical)
    axis_perp = perp[:, 0] / norm(perp[:, 0])   # its conjugate (internal)
    return xpar[keep], xperp[keep], axis_par, axis_perp


def make_random(n_points, phys_radius, perp_scale, seed):
    """Random points in a ball, with random shadow coordinates. The 'any graph' baseline."""
    rng = np.random.default_rng(seed)

    def ball(n, r):
        v = rng.normal(size=(n, 3))
        v /= norm(v, axis=1, keepdims=True)
        return v * (r * rng.random(n)[:, None] ** (1.0 / 3.0))

    xpar = ball(n_points, phys_radius)
    xperp = ball(n_points, perp_scale)
    axis = np.array([0.0, 0.0, 1.0])
    return xpar, xperp, axis, axis


def build_graph(xpar, k):
    """Symmetric k-nearest-neighbour graph: connect i-j if either is in the other's
    k nearest. Same k for every point set, so connectivity is matched and any
    remaining difference is about geometry, not density."""
    n = len(xpar)
    kk = min(k, n - 1)
    tree = cKDTree(xpar)
    d, idx = tree.query(xpar, k=kk + 1)        # +1 because the first hit is the point itself
    A = np.zeros((n, n))
    for i in range(n):
        for j in idx[i, 1:]:
            A[i, j] = 1.0
            A[j, i] = 1.0
    dmin = float(np.median(d[:, 1]))
    return A, dmin, kk


def build_operators(xpar, xperp, A, axis_par, axis_perp, alpha):
    """S = smoothing (symmetric), K = circulation (antisymmetric, geometry+shadow blend)."""
    n = len(xpar)
    deg = A.sum(axis=1)
    L = np.diag(deg) - A           # graph Laplacian (positive semidefinite)
    S = -L                         # smoothing generator: negative semidefinite -> decay

    K = np.zeros((n, n))
    ii, jj = np.where(np.triu(A, 1) > 0)
    kg = np.cross(xpar[ii], xpar[jj]) @ axis_par      # icosahedral-geometry swirl
    kp = np.cross(xperp[ii], xperp[jj]) @ axis_perp   # hidden-shadow swirl
    kval = (1.0 - alpha) * kg + alpha * kp
    K[ii, jj] = kval
    K[jj, ii] = -kval

    sS, sK = norm(S, 2), norm(K, 2)                   # match operator norms so delta is a fair dial
    if sK > 0:
        K = K * (sS / sK)
    return S, K


def analyse(name, xpar, xperp, axis_par, axis_perp):
    A, dmin, _k = build_graph(xpar, K_NEIGHBORS)
    S, K = build_operators(xpar, xperp, A, axis_par, axis_perp, ALPHA)
    n = len(xpar)
    deg = A.sum(axis=1)

    # (a) spectrum vs delta
    max_im = []
    for d in DELTA_SWEEP:
        ev = eig(S + d * K)[0]
        max_im.append(float(np.max(np.abs(ev.imag))))
    key_spec = {d: eig(S + d * K)[0] for d in DELTAS_KEY}

    # (b) commutator
    C = S @ K - K @ S
    asym = norm(C - C.T) / (norm(C) + 1e-30)
    ceig = np.linalg.eigvalsh((C + C.T) / 2.0)

    # (c) heat trace
    heat = {}
    for d in DELTAS_KEY:
        ev = key_spec[d]
        heat[d] = np.array([float(np.real(np.sum(np.exp(t * ev)))) for t in HEAT_TS])

    return dict(name=name, n=n, edges=int(A.sum() // 2), mean_deg=float(deg.mean()),
                dmin=dmin, xpar=xpar, max_im=np.array(max_im), key_spec=key_spec,
                C_asym=asym, ceig=ceig, heat=heat, Snorm=norm(S, 2))


def main():
    print("=" * 70)
    print("TIER-1 QUASICRYSTAL OPERATOR EXPERIMENT")
    print("=" * 70)

    # quasicrystal (real golden ratio)
    qx, qxp, ax_p, ax_pp = make_cut_and_project(PHI, LATTICE_R, PHYS_RADIUS)
    perp_scale = float(np.max(norm(qxp, axis=1))) if len(qxp) else 1.0

    # periodic crystal: same machinery, rational slope
    px, pxp, pax_p, pax_pp = make_cut_and_project(13.0 / 8.0, LATTICE_R, PHYS_RADIUS)

    # random baseline, matched count
    rx, rxp, rax_p, rax_pp = make_random(max(len(qx), 10), PHYS_RADIUS, perp_scale, RNG_SEED)

    sets = [
        analyse("quasicrystal", qx, qxp, ax_p, ax_pp),
        analyse("periodic",     px, pxp, pax_p, pax_pp),
        analyse("random",       rx, rxp, rax_p, rax_pp),
    ]

    print(f"\n{'set':<14}{'points':>8}{'edges':>8}{'mean.deg':>10}"
          f"{'maxImag(d=0)':>14}{'maxImag(d=1)':>14}{'[S,K] asym':>12}{'eddy range':>22}")
    for s in sets:
        i0 = int(np.argmin(np.abs(DELTA_SWEEP - 0.0)))
        i1 = int(np.argmin(np.abs(DELTA_SWEEP - 1.0)))
        eddy = f"[{s['ceig'].min():.3g}, {s['ceig'].max():.3g}]"
        print(f"{s['name']:<14}{s['n']:>8}{s['edges']:>8}{s['mean_deg']:>10.2f}"
              f"{s['max_im'][i0]:>14.2e}{s['max_im'][i1]:>14.3f}{s['C_asym']:>12.2e}{eddy:>22}")

    print("\nReading the table:")
    print("  - maxImag(d=0) ~ 0  -> delta=0 is the real-spectrum / self-adjoint point (expected, trivial)")
    print("  - maxImag(d=1) > 0  -> circulation opens up complex eigenvalues (rotation)")
    print("  - [S,K] asym  ~ 0   -> the commutator IS symmetric (eddy-diffusivity-like, not rotation-like)")
    print("  - eddy range        -> spectrum of [S,K]; compare quasicrystal vs controls")

    # ------------------------------- plots -------------------------------
    fig, ax = plt.subplots(2, 3, figsize=(16, 9))
    colors = {"quasicrystal": "#1f77b4", "periodic": "#ff7f0e", "random": "#2ca02c"}

    # (0,0) the quasicrystal patch, physical space (x-y)
    qc = sets[0]
    ax[0, 0].scatter(qc["xpar"][:, 0], qc["xpar"][:, 1], s=8, c=colors["quasicrystal"])
    ax[0, 0].set_title(f"quasicrystal patch (x-y), N={qc['n']}")
    ax[0, 0].set_aspect("equal"); ax[0, 0].set_xlabel("x"); ax[0, 0].set_ylabel("y")

    # (0,1) complex spectrum of QC at delta = -1, 0, +1
    for d, col in zip(DELTAS_KEY, ["#d62728", "#000000", "#1f77b4"]):
        ev = qc["key_spec"][d]
        ax[0, 1].scatter(ev.real, ev.imag, s=10, alpha=0.6, color=col, label=f"δ={d:+.0f}")
    ax[0, 1].set_title("quasicrystal: spectrum of O_δ")
    ax[0, 1].set_xlabel("Re(λ)"); ax[0, 1].set_ylabel("Im(λ)"); ax[0, 1].legend()
    ax[0, 1].axhline(0, lw=0.5, color="gray")

    # (0,2) max|Im(lambda)| vs delta, all sets  -- the "is delta=0 special" plot
    for s in sets:
        ax[0, 2].plot(DELTA_SWEEP, s["max_im"], color=colors[s["name"]], label=s["name"])
    ax[0, 2].axvline(0, lw=0.5, color="gray")
    ax[0, 2].set_title("max|Im(λ)| vs δ  (dip at δ=0 = self-adjoint point)")
    ax[0, 2].set_xlabel("δ"); ax[0, 2].set_ylabel("max|Im(λ)|"); ax[0, 2].legend()

    # (1,0) [S,K] eddy spectrum, all sets
    for s in sets:
        ax[1, 0].hist(s["ceig"], bins=30, alpha=0.5, color=colors[s["name"]],
                      label=f"{s['name']} (asym={s['C_asym']:.1e})")
    ax[1, 0].set_title("[S,K] spectrum  (symmetric → 'eddy diffusivity')")
    ax[1, 0].set_xlabel("eigenvalue of [S,K]"); ax[1, 0].set_ylabel("count"); ax[1, 0].legend()

    # (1,1) heat trace of QC at delta = -1, 0, +1
    for d, col in zip(DELTAS_KEY, ["#d62728", "#000000", "#1f77b4"]):
        ax[1, 1].plot(HEAT_TS, qc["heat"][d], color=col, label=f"δ={d:+.0f}")
    ax[1, 1].set_title("quasicrystal: heat trace Re Tr(e^{tO_δ})")
    ax[1, 1].set_xlabel("t"); ax[1, 1].set_ylabel("H(t)"); ax[1, 1].legend()

    # (1,2) heat trace at delta=1 across sets
    for s in sets:
        ax[1, 2].plot(HEAT_TS, s["heat"][1.0], color=colors[s["name"]], label=s["name"])
    ax[1, 2].set_title("heat trace at δ=+1, all sets")
    ax[1, 2].set_xlabel("t"); ax[1, 2].set_ylabel("H(t)"); ax[1, 2].legend()

    fig.suptitle("Tier-1: icosahedral quasicrystal vs periodic vs random — S + δK", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    out = os.path.join(OUTDIR, "tier1_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
