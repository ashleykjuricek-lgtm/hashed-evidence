"""
Certified enclosures of zeta(-1/2) and beta(-1/2)  -- closes hashed-evidence 028 App. A.4's
one non-self-contained input ("for maximal rigor, a self-contained enclosure of zeta(-1/2),
beta(-1/2) ... which is routine").

Method (every step in mpmath INTERVAL arithmetic, mpmath.iv; no call to mpmath's own
zeta/beta, which are not interval-certified):
  1. Reflection to s = 3/2, where the series converge:
        zeta(-1/2) = -zeta(3/2) / (4 pi)                               [functional equation]
        beta(-1/2) = (2/pi)^{3/2} sin(3pi/4) Gamma(3/2) beta(3/2)
                   = (2/pi)^{3/2} (1/sqrt2) (sqrt(pi)/2) beta(3/2)
                   = beta(3/2) / pi                                     [simplified]
        and beta(3/2) = 4^{-3/2} [ zeta(3/2, 1/4) - zeta(3/2, 3/4) ].
  2. Each Hurwitz zeta(3/2, a) = sum_{n<N} (n+a)^{-3/2} + Euler-Maclaurin tail at x0 = N+a,
     with p Bernoulli terms and the RIGOROUS remainder bound
        |R_p| <= 2 zeta(2p) / (2 pi)^{2p} * |f^{(2p-1)}(x0)|,
     valid because f(x) = x^{-3/2} is completely monotone (f^{(2p)} has constant sign, so
     integral |f^{(2p)}| = |f^{(2p-1)}(x0)|), and |B_{2p}(x - floor x)| <= |B_{2p}|
     = 2 (2p)! zeta(2p) / (2pi)^{2p}. zeta(2p) <= 1 + 2^{1-2p}*... we bound zeta(2p) <= 2.
     The remainder interval [-bound, +bound] is ADDED to the result, so the output is an
     enclosure, not an estimate.
"""
import sys
sys.path.insert(0, "/tmp/pylib")
from mpmath import iv, mp, bernoulli, mpf

iv.dps = 80
mp.dps = 80
S = iv.mpf(3) / 2
N, P = 60, 30

def falling(k):            # f^{(k)}(x) = (-1)^k (s)(s+1)...(s+k-1) x^{-s-k}
    c = iv.mpf(1)
    for i in range(k):
        c *= (S + i)
    return c

def hurwitz_32(a):
    a = iv.mpf(a)
    tot = iv.mpf(0)
    for n in range(N):
        tot += (n + a) ** (-S)
    x0 = N + a
    tot += x0 ** (1 - S) / (S - 1)            # integral
    tot += x0 ** (-S) / 2                       # half endpoint
    for k in range(1, P + 1):                   # - sum B_2k/(2k)! f^{(2k-1)}(x0)
        B = iv.mpf(bernoulli(2 * k))
        fac = iv.mpf(mp.factorial(2 * k))
        deriv = -falling(2 * k - 1) * x0 ** (-S - (2 * k - 1))   # sign (-1)^{2k-1} = -1
        tot -= B / fac * deriv
    bound = 2 * iv.mpf(2) / (2 * iv.pi) ** (2 * P) * falling(2 * P - 1) * x0 ** (-S - (2 * P - 1))
    bmid = bound.b                                # upper end of the bound interval
    return tot + iv.mpf([-bmid, bmid])

zeta32 = hurwitz_32(1)
beta32 = (hurwitz_32(iv.mpf(1) / 4) - hurwitz_32(iv.mpf(3) / 4)) / iv.mpf(4) ** S
zeta_m12 = -zeta32 / (4 * iv.pi)
beta_m12 = beta32 / iv.pi

def report(name, x, ref):
    lo, hi = mpf(x.a.a), mpf(x.b.b)            # outer endpoints, as plain mpf
    w = hi - lo
    inside = lo <= ref <= hi
    print(f"{name}\n  enclosure  [{mp.nstr(lo, 62)},\n              {mp.nstr(hi, 62)}]")
    print(f"  width      {mp.nstr(w, 3)}      (028 used 1e-45-width intervals)")
    print(f"  mpmath 60-digit value inside enclosure: {inside}\n")
    return inside, w

mp.dps = 100
ok1, w1 = report("zeta(-1/2)", zeta_m12, mp.zeta(-0.5))
ok2, w2 = report("beta(-1/2)", beta_m12, (mp.zeta(-0.5, 0.25) - mp.zeta(-0.5, 0.75)) * mpf(4) ** 0.5)
print("CERTIFIED:", ok1 and ok2 and w1 < mpf(10) ** -45 and w2 < mpf(10) ** -45)
