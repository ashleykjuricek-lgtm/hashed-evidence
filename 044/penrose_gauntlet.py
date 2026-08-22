"""
PENROSE ROSE GAUNTLET
=====================
Ledger 022 claims: on a decagonal cut-and-project quasilattice, the zeta ratio
Z_shifted(s)/Z_unshifted(s) = 1/phi at s~2, when the acceptance window is shifted
by 1/phi^2 along a vertex direction. Sealed as FOUNDATIONAL, never deformed.

022's own recipe (faithfully reproduced, N=8 -> 0.6176133 = ledger JSON):
  - Z^5 -> R^2 (pentagon star), decagon window inradius 1, shift window in perp space.
  - Z(s) = sum' |x_phys|^(-2s), origin excluded.
  - shift = (1/phi^2)*(1,0);  ratio at s=2 ~ 1/phi.

The tell: shift = 1/phi^2 and output = 1/phi are ONE fact, because golden is the
unique number with 1/phi^2 = 1 - 1/phi. So if ratio ~ 1 - (shift magnitude), you get
1/phi FOR FREE from the shift choice, with nothing to do with fivefold-ness.

Three arms (027's law: derivation, deformation, generalization):
  A. DEFORMATION - sweep the shift magnitude d continuously. Is 1/phi a special
     feature of the curve, or just where a smooth ~ (1-d) curve happens to cross?
  B. GENERALIZATION - run the IDENTICAL recipe on the octagonal (sqrt2 / silver)
     quasicrystal and the 3D icosahedral one. If the sqrt2 octagon ALSO gives 1/phi
     at shift 1/phi^2, the Rose is shift-arithmetic, not geometry.
  C. SILVER FOIL - shift the octagon by the SILVER analog 1/silver^2. Does the
     output track the input (you get out what you put in)?
"""

import os
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import numpy as np
from scipy.spatial import cKDTree
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUTDIR = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
SILVER = 1 + 2 ** 0.5


# ---------- projections ----------
def decagon_proj():
    n = np.sqrt(2 / 5)
    Ppar = np.array([[n * np.cos(2 * np.pi * k / 5), n * np.sin(2 * np.pi * k / 5)] for k in range(5)]).T
    Pperp = np.array([[n * np.cos(4 * np.pi * k / 5), n * np.sin(4 * np.pi * k / 5)] for k in range(5)]).T
    return Ppar, Pperp


def octagon_proj():
    n = np.sqrt(2 / 4)
    Ppar = np.array([[n * np.cos(2 * np.pi * k / 8), n * np.sin(2 * np.pi * k / 8)] for k in range(4)]).T
    Pperp = np.array([[n * np.cos(2 * np.pi * 3 * k / 8), n * np.sin(2 * np.pi * 3 * k / 8)] for k in range(4)]).T
    return Ppar, Pperp


def icosa_proj():
    phi, pc = PHI, 1 - PHI
    nrm = np.sqrt(2 + phi)
    par = np.array([[0, 0, 1, 1, phi, -phi], [1, 1, phi, -phi, 0, 0], [phi, -phi, 0, 0, 1, 1]], float) / nrm
    perp = np.array([[0, 0, 1, 1, pc, -pc], [1, 1, pc, -pc, 0, 0], [pc, -pc, 0, 0, 1, 1]], float) / nrm
    return par, perp


# ---------- windows ----------
def poly_window(perp, half, W, shift):
    p = perp - shift
    inside = np.ones(len(p), bool)
    for k in range(half):
        a = np.pi * (2 * k + 1) / (2 * half)
        inside &= np.abs(p[:, 0] * np.cos(a) + p[:, 1] * np.sin(a)) < W
    return inside


def tria_window(perp, gens, W, shift):
    p = perp - shift
    G = gens.T
    inside = np.ones(len(p), bool)
    for i in range(6):
        for j in range(i + 1, 6):
            nn = np.cross(G[i], G[j]); ln = np.linalg.norm(nn)
            if ln < 1e-12:
                continue
            nn = nn / ln
            hw = 0.5 * np.sum(np.abs(G @ nn)) * W
            inside &= np.abs(p @ nn) <= hw
    return inside


# ---------- machinery ----------
def grid(N, D):
    c = np.arange(-N, N + 1, dtype=float)
    return np.array(np.meshgrid(*([c] * D), indexing="ij")).reshape(D, -1).T


def dedup(v):
    if len(v) == 0:
        return v
    key = np.round(v / 1e-8).astype(np.int64)
    _, idx = np.unique(key, axis=0, return_index=True)
    return v[idx]


def zeta(v, s):
    r2 = np.sum(v * v, axis=1)
    r2 = r2[r2 > 1e-12]
    return float(np.sum(r2 ** (-s)))


def points(kind, N, shift):
    if kind == "decagon":
        Ppar, Pperp = decagon_proj(); g = grid(N, 5)
        m = poly_window(g @ Pperp.T, 5, 1.0, shift)
        return dedup((g @ Ppar.T)[m])
    if kind == "octagon":
        Ppar, Pperp = octagon_proj(); g = grid(N, 4)
        m = poly_window(g @ Pperp.T, 4, 1.0, shift)
        return dedup((g @ Ppar.T)[m])
    if kind == "icosa":
        par, perp = icosa_proj(); g = grid(N, 6)
        m = tria_window(g @ perp.T, perp, 1.0, shift)
        return dedup((g @ par.T)[m])


NDEF = {"decagon": 6, "octagon": 8, "icosa": 4}
DIR = {"decagon": np.array([1.0, 0.0]), "octagon": np.array([1.0, 0.0])}


def shift_dir(kind):
    if kind == "icosa":
        _, perp = icosa_proj()
        d = perp[:, 0] / np.linalg.norm(perp[:, 0])
        return d
    return DIR[kind]


def ratio(kind, d, s, N=None):
    N = N or NDEF[kind]
    base = zeta(points(kind, N, np.zeros(shift_dir(kind).shape)), s)
    sh = zeta(points(kind, N, d * shift_dir(kind)), s)
    return sh / base


def main():
    print("=" * 68)
    print("PENROSE ROSE GAUNTLET")
    print("=" * 68)
    d0 = 1 / PHI ** 2
    print(f"golden shift 1/phi^2 = {d0:.6f}   target 1/phi = {1/PHI:.6f}   (1 - 1/phi^2 = {1-d0:.6f})")

    # faithfulness: reproduce 022 headline at N=8
    r8 = ratio("decagon", d0, 2.0, N=8)
    print(f"\n[faithful] decagon N=8, shift 1/phi^2, s=2:  ratio = {r8:.7f}  "
          f"(ledger 0.6176133, 1/phi 0.6180340)")

    # ---- ARM A: deformation, sweep shift magnitude ----
    ds = np.linspace(0.0, 1.0, 26)
    rdec = np.array([ratio("decagon", d, 2.0) for d in ds])
    dev = np.max(np.abs(rdec - (1 - ds)))
    print(f"\n[ARM A] decagon ratio(d) at s=2, N={NDEF['decagon']}:")
    print(f"        max |ratio(d) - (1 - d)| over the whole sweep = {dev:.4f}")
    print(f"        -> if ~0, the ratio is just 1 - shift, and 1/phi is where it crosses at d=1/phi^2")

    # ---- ARM B: generalization, same recipe, three quasicrystals, at the golden shift ----
    print(f"\n[ARM B] identical recipe (shift 1/phi^2, s=2) on three quasicrystals:")
    rat_golden = {}
    for kind in ["decagon", "octagon", "icosa"]:
        rr = ratio(kind, d0, 2.0)
        rat_golden[kind] = rr
        flag = "~ 1/phi !" if abs(rr - 1 / PHI) < 0.02 else ""
        print(f"        {kind:9s}: ratio = {rr:.5f}   {flag}")
    print("        -> if the sqrt2 OCTAGON also gives ~1/phi, the Rose is shift-arithmetic, not fivefold geometry")

    # ---- ARM C: silver foil ----
    dsil = 1 / SILVER ** 2
    r_sil = ratio("octagon", dsil, 2.0)
    print(f"\n[ARM C] silver foil: octagon shifted by 1/silver^2 = {dsil:.5f}")
    print(f"        ratio = {r_sil:.5f}   vs 1/silver = {1/SILVER:.5f}   vs (1 - 1/silver^2) = {1-dsil:.5f}")
    print("        -> tests whether output tracks (1 - shift) rather than the 'expected' 1/silver")

    # curves for all three (for the overlay plot)
    rall = {k: np.array([ratio(k, d, 2.0) for d in ds]) for k in ["decagon", "octagon", "icosa"]}

    # ---- verdict ----
    oct_close = abs(rat_golden["octagon"] - 1 / PHI) < 0.02
    print("\n" + "=" * 68)
    if dev < 0.03 and oct_close:
        print("VERDICT: DOCUMENTED NULL. ratio ~ (1 - shift); the sqrt2 octagon also yields")
        print("1/phi at a golden shift. The '1/phi Rose' is arithmetic of the chosen shift")
        print("(golden's 1/phi^2 = 1 - 1/phi), NOT a property of fivefold quasicrystals.")
    else:
        print("VERDICT: SURVIVES (so far). 1/phi is NOT simply 1 - shift and/or is specific")
        print("to the fivefold quasicrystals. Warrants the derivation arm.")
    print("=" * 68)

    # ---- plots ----
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.4))
    ax[0].plot(ds, rdec, "o-", color="#1f77b4", label="decagon ratio(d)")
    ax[0].plot(ds, 1 - ds, "--", color="gray", label="1 - d  (trivial geometry)")
    ax[0].axvline(d0, color="#d62728", lw=1, ls=":")
    ax[0].axhline(1 / PHI, color="#d62728", lw=1, ls=":")
    ax[0].plot([d0], [1 / PHI], "*", color="#d62728", ms=15, label="claimed (1/φ² → 1/φ)")
    ax[0].set_title("ARM A — is 1/φ special, or just where 1−d crosses?")
    ax[0].set_xlabel("shift magnitude d"); ax[0].set_ylabel("ratio at s=2"); ax[0].legend()

    cols = {"decagon": "#1f77b4", "octagon": "#ff7f0e", "icosa": "#2ca02c"}
    for k in ["decagon", "octagon", "icosa"]:
        ax[1].plot(ds, rall[k], "o-", ms=3, color=cols[k], label=k)
    ax[1].plot(ds, 1 - ds, "--", color="gray", label="1 - d")
    ax[1].axvline(d0, color="#d62728", lw=1, ls=":")
    ax[1].axhline(1 / PHI, color="#d62728", lw=1, ls=":", label="1/φ")
    ax[1].set_title("ARM B — same recipe, three quasicrystals (√5 decagon/icosa vs √2 octagon)")
    ax[1].set_xlabel("shift magnitude d"); ax[1].set_ylabel("ratio at s=2"); ax[1].legend()

    fig.suptitle("Penrose Rose gauntlet: is 1/φ geometry, or arithmetic of the shift?", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    out = os.path.join(OUTDIR, "penrose_gauntlet_summary.png")
    fig.savefig(out, dpi=110)
    print(f"\nSaved plot -> {out}")


if __name__ == "__main__":
    main()
