"""Z on the d-torus with sides (1, b, b, ..., b), one marked axis (the length-1 one).
Real d, real b. Merges the 042 real-dimension continuation with the 047 anisotropic
sum -- they were the same factorised theta with a different argument all along.

  Theta_A(t) = theta_A(t) * theta_P(t/b^2)^(d-1)      one marked axis
  Theta_P(t) = theta_P(t) * theta_P(t/b^2)^(d-1)      none marked
  V = b^(d-1)
"""
from mpmath import mp, mpf, pi, gamma, quad, exp, inf, nstr
mp.dps = 25

def Z(d, b, marked, s=mpf(-0.5), lam=mpf(1), N=18, K=8):
    d = mpf(d); b = mpf(b); V = b**(d-1)
    rng = range(-N, N+1); krng = range(1, K+1)
    h = mpf(1)/2
    thA = lambda u: sum(exp(-u*(n+h)**2) for n in rng)
    thP = lambda u: sum(exp(-u*mpf(n)**2) for n in rng)
    fA  = lambda u: 1 + 2*sum((-1)**k*exp(-pi**2*k*k/u) for k in krng)
    fP  = lambda u: 1 + 2*sum(exp(-pi**2*k*k/u)         for k in krng)
    delta = 0 if marked else 1
    def small(t):
        br = (fA(t) if marked else fP(t)) * fP(t/b**2)**(d-1)
        return V*pi**(d/2)*t**(s-1-d/2)*(br - 1)
    def big(t):
        v = (thA(t) if marked else thP(t)) * thP(t/b**2)**(d-1)
        return t**(s-1)*(v - delta)
    tot = quad(small,[0,lam]) + V*pi**(d/2)*lam**(s-d/2)/(s-d/2) + quad(big,[lam,inf])
    if delta: tot -= lam**s/s
    return tot/gamma(s)

def R(d, b, **kw): return Z(d, b, True, **kw)/Z(d, b, False, **kw)

if __name__ == "__main__":
    print("validation:")
    for (d,b,ref) in [(3,1,'0.0416894146027238'), (2,1,'-0.103553390593274'),
                      (5,1,'0.191188548061399'), (1,1,'-0.5')]:
        print(f"   R({d},b={b}) = {nstr(R(d,mpf(b)),15):>20}   ref {ref}")
    print()
    print("   eps(3,b) = 24R-1 at b=1:", nstr(24*R(3,1)-1, 15), " (ref 0.000545950465371)")
    print("   eps(3,b) = 24R-1 at b=1.00003:", nstr(24*R(3,mpf('1.0000297915619869892'))-1, 6))
