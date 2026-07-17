# Second glance at the 1/24: is leech.md's "APP/PPP = zeta(2s) universally"
# the SAME object as the T^3 boundary-condition ratio Z_APP/Z_PPP ~ 1/24 ?
#
# Test at s where lattice sums converge absolutely (s=2 and s=3, i.e. |n|^-4, |n|^-6 on Z^3).
#
# Objects:
#   Z_full(s)  = sum over nonzero n in Z^3 of |n|^(-2s)                  ["PPP" in both readings]
#   Z_prim(s)  = same, restricted to primitive vectors (gcd = 1)
#   Z_APP(s)   = sum of (-1)^(n1) |n|^(-2s)      [T^3 antiperiodic BC in one direction]
#   Z_AAA(s)   = sum of (-1)^(n1+n2+n3) |n|^(-2s) [antiperiodic in all three]
#
# leech.md's identity:   Z_full = Z_prim * zeta(2s)   =>  Z_full/Z_prim = zeta(2s).  (classical)
# The question: does Z_APP/Z_full equal zeta(2s) too? If not, the site's current
# canonical 1/24 account renamed a different ratio "APP/PPP".

import numpy as np
from mpmath import mp, zeta, pi

mp.dps = 20

def lattice_sums(N, s):
    r = np.arange(-N, N + 1)
    X, Y, Z = np.meshgrid(r, r, r, indexing="ij")
    n2 = (X * X + Y * Y + Z * Z).astype(np.float64)
    mask = n2 > 0
    w = np.zeros_like(n2)
    w[mask] = n2[mask] ** (-s)          # |n|^(-2s) with n2 = |n|^2
    full = w.sum()
    app = (np.where((X % 2 == 0), 1.0, -1.0) * w).sum()
    aaa = (np.where(((X + Y + Z) % 2 == 0), 1.0, -1.0) * w).sum()
    g = np.gcd(np.gcd(np.abs(X), np.abs(Y)), np.abs(Z))
    prim = w[(g == 1)].sum()
    return full, prim, app, aaa

for s, N in [(2, 120), (3, 60)]:
    full, prim, app, aaa = lattice_sums(N, s)
    z2s = float(zeta(2 * s))
    print(f"--- s = {s}  (cutoff N = {N}) ---")
    print(f"Z_full/Z_prim = {full/prim:.9f}   vs zeta({2*s}) = {z2s:.9f}   "
          f"[match: {abs(full/prim - z2s) < 5e-3}]")
    print(f"Z_APP /Z_full = {app/full:+.9f}   (T^3 one-direction antiperiodic ratio)")
    print(f"Z_AAA /Z_full = {aaa/full:+.9f}   (all-antiperiodic ratio)")
    print(f"  -> Z_APP/Z_full == zeta({2*s})?  {abs(app/full - z2s) < 1e-2}")
    print()

print("Known continued values at s = -1/2 (from the project's own 50-digit numerics):")
print("  Z_APP(-1/2)/Z_PPP(-1/2) = 0.041689414602...  (~ 1/24 * 1.00055)")
print("  zeta(-1)                = ", float(zeta(-1)), "  ( -1/12 )")
print("  -zeta(-1)/2             = ", float(-zeta(-1) / 2), "  ( = 1/24 exactly )")
print()
print("If APP/PPP were the zeta(2s) identity, the BC ratio would be EXACTLY -1/12")
print("(or exactly 1/24 after the -1/2 normalization) with NO epsilon. It is not.")
