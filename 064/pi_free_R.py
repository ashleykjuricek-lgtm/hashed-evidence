"""Is R pi-free?

Z(d,j) at s=-1/2  =  PREFACTOR(d) * SUM'_m chi_j(m) |m|^-(d+1)
with PREFACTOR(d) = pi^(-1-d/2) Gamma((d+1)/2)/Gamma(-1/2)  -- depends on d ONLY.

The marking j does not appear in it. So in R = Z(d,j)/Z(d,0) it CANCELS:

    R(d,j) = [ SUM'_m chi_j(m) |m|^-(d+1) ] / [ SUM'_m |m|^-(d+1) ]

For d=3 that is a ratio of two integer-lattice sums at exponent 4. No pi anywhere.
Test it against the 50-digit value."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

REF = 0.0416894146027237751200791895411477959451762762538280901

for N in [120, 200, 300]:
    M = N*N
    ax = np.arange(-N, N+1, dtype=np.int64)
    X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
    n2 = (X*X + Y*Y + Z*Z).ravel()
    sgn = ((-1.0)**X).ravel()
    keep = (n2 > 0) & (n2 <= M)
    n2 = n2[keep]; sgn = sgn[keep]
    # bin
    den_bins = np.bincount(n2, minlength=M+1).astype(np.float64)          # r3(m)
    num_bins = np.bincount(n2, weights=sgn, minlength=M+1)                # c(m)
    m = np.arange(1, M+1, dtype=np.float64)
    den = float(np.sum(den_bins[1:M+1]/m**2))
    num = float(np.sum(num_bins[1:M+1]/m**2))
    tail = 4*math.pi/math.sqrt(M)          # sum_{m>M} r3(m)/m^2 ~ 4 pi / sqrt(M)
    print(f"N={N:4d}  |m|^2 <= {M}")
    print(f"    numerator  SUM' (-1)^m1 |m|^-4 = {num:.12f}    (alternating: converges fast)")
    print(f"    denominator SUM'      |m|^-4   = {den:.9f}  + tail {tail:.6f} = {den+tail:.9f}")
    print(f"    R = {num/(den+tail):.10f}      reference {REF:.10f}")
    print()
print("known value of the denominator, from 028 section 5:  Z_PPP(2) = 16.5323159598")
print("   -> R would be", f"{0.0}")
