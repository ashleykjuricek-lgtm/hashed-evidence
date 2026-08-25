import numpy as np, math, cmath

N = 2_000_000
w = cmath.exp(2j*math.pi/3)

def chi_array(mod, table):
    idx = np.arange(N+1) % mod
    out = np.zeros(N+1, dtype=complex)
    for r,v in table.items():
        out[idx==r] = v
    out[0] = 0
    return out

def ideal_counts(chi):
    """a_K = 1 * chi * chibar  for a CYCLIC CUBIC field."""
    cb = np.conj(chi)
    g = np.zeros(N+1, dtype=complex)      # g = 1 * chi
    for d in range(1, N+1):
        K = N//d
        g[d::d] += chi[1:K+1]
    a = np.zeros(N+1, dtype=complex)      # a = g * chibar
    for d in range(1, N+1):
        if g[d] != 0:
            K = N//d
            a[d::d] += g[d]*cb[1:K+1]
    return a.real

def regulator(roots, unit_polys):
    """rows = embeddings 0,1 ; cols = the two units, each a poly in alpha"""
    M = [[math.log(abs(f(roots[i]))) for f in unit_polys] for i in (0,1)]
    return abs(M[0][0]*M[1][1] - M[0][1]*M[1][0])

FIELDS = [
  dict(name="Q(zeta_7)+  cyclic cubic, conductor 7",
       mod=7, tab={1:1,6:1,3:w,4:w,2:w**2,5:w**2},
       disc=49, h=1, w_roots=2,
       roots=[2*math.cos(2*math.pi*k/7) for k in (1,2,3)]),
  dict(name="Q(zeta_9)+  cyclic cubic, conductor 9",
       mod=9, tab={1:1,8:1,2:w,7:w,4:w**2,5:w**2},
       disc=81, h=1, w_roots=2,
       roots=[2*math.cos(2*math.pi*k/9) for k in (1,2,4)]),
]

print(f"counting ideals of norm m <= {N:,} in cyclic CUBIC fields")
print("r1 = 3, r2 = 0  (totally real)  ->  class number formula gives")
print("    residue = 2^r1 (2pi)^r2 h R / (w sqrt|d|) = 8 h R / (2 sqrt d) = 4 h R / sqrt d")
print()

for F in FIELDS:
    chi = chi_array(F["mod"], F["tab"])
    a = ideal_counts(chi)

    # ---- validate against the splitting rule, independently ----
    bad = []
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,71,113,127,197,211,223]:
        if p > N: continue
        c = chi[p]
        want = 3 if abs(c-1) < 1e-9 else (0 if abs(c) > 1e-9 else 1)   # split / inert / ramified
        if abs(a[p]-want) > 1e-6: bad.append((p, a[p], want))
    # ideals of norm p^2 for a split p must be 6 = C(4,2)
    for p in [13,29,41,43,71]:
        if p*p <= N and abs(chi[p]-1) < 1e-9 and abs(a[p*p]-6) > 1e-6:
            bad.append((p*p, a[p*p], 6))

    mean = a[1:N+1].mean()
    R = regulator(F["roots"], [lambda x: x, lambda x: x*x - 2])
    closed = 4*F["h"]*R/math.sqrt(F["disc"])

    print(F["name"])
    print(f"   splitting-rule check      {'PASS  0 mismatches' if not bad else 'FAIL '+str(bad)}")
    print(f"   counted mean              {mean:.8f}")
    print(f"   4 h R / sqrt(d)           {closed:.8f}     R = {R:.10f}  (a 2x2 DETERMINANT of logs)")
    print(f"   ratio counted/closed      {mean/closed:.6f}")
    print(f"   would-be value WITH pi    {closed*2*math.pi:.8f}   <- ratio to counted {mean/(closed*2*math.pi):.4f}")
    print()

print("for contrast, the price in each shape, from Dirichlet's formula:")
print("   2^r1 (2pi)^r2 h R / (w sqrt|d|)      r2 = number of COMPLEX embedding pairs")
print("                                        R  = det of an (r1+r2-1) x (r1+r2-1) log matrix")
print()
print("   shape                 r1 r2  unit rank  pi?   what R is")
print("   imaginary quadratic    0  1      0      YES   empty determinant = 1")
print("   real quadratic         2  0      1      no    ONE logarithm")
print("   totally real cubic     3  0      2      no    a 2x2 DETERMINANT  <- counted above")
print("   complex cubic          1  1      1      YES   one logarithm, times 2pi")
