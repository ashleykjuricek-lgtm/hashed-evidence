"""Z(-1/2) on the d-torus with j marked circles, for REAL d and j.

The lattice enumeration is the only thing that ever needed whole numbers, and it
is not needed. The direct theta factorises into a POWER,

    Theta(t) = theta_A(t)^j * theta_P(t)^(d-j)

and a power takes a real exponent. Below the Ewald cut we use the Poisson form of
each 1-D theta,

    theta_P(t) = sqrt(pi/t) * P(t),   P(t) = 1 + 2*sum_k exp(-pi^2 k^2 / t)
    theta_A(t) = sqrt(pi/t) * A(t),   A(t) = 1 + 2*sum_k (-1)^k exp(-pi^2 k^2 / t)

so  Theta(t) = (pi/t)^(d/2) * A(t)^j * P(t)^(d-j)  and the bracket [A^j P^(d-j) - 1]
is exponentially small as t -> 0. Valid for any real d > 0, 0 <= j <= d.
"""
from mpmath import mp, mpf, pi, gamma, quad, exp, inf, nstr
mp.dps = 25

def Z(d, j, s=mpf(-0.5), lam=mpf(1), N=16, K=6):
    d = mpf(d); j = mpf(j)
    rng = range(-N, N+1); krng = range(1, K+1)
    thA = lambda t: sum(exp(-t*(n+mpf(1)/2)**2) for n in rng)
    thP = lambda t: sum(exp(-t*mpf(n)**2)       for n in rng)
    Pd  = lambda t: 1 + 2*sum(exp(-pi**2*k*k/t)            for k in krng)
    Ad  = lambda t: 1 + 2*sum((-1)**k*exp(-pi**2*k*k/t)    for k in krng)
    delta = 1 if j == 0 else 0

    def small(t):                       # t^(s-1) * (Theta - (pi/t)^(d/2))
        br = Ad(t)**j * Pd(t)**(d-j) - 1
        return pi**(d/2) * t**(s-1-d/2) * br
    def big(t):
        v = mpf(1)
        if j > 0:     v *= thA(t)**j
        if d - j > 0: v *= thP(t)**(d-j)
        return t**(s-1)*(v - delta)

    tot = quad(small, [0, lam]) + pi**(d/2)*lam**(s-d/2)/(s-d/2) + quad(big, [lam, inf])
    if delta: tot -= lam**s/s
    return tot/gamma(s)

if __name__ == "__main__":
    print("validation against the integer-lattice solver of 039/040:")
    ref = {(3,1):'-0.0111142427950344', (5,2):'-0.00937157210640224',
           (2,2):'0.0670210888091522',  (10,5):'0.00589087006724',
           (2,1):'0.0236955331897',     (1,0):'-0.166666666666667',
           (12,6):'0.00651370870914'}
    ok = True
    for (d,j), r in sorted(ref.items()):
        v = Z(d,j); m = nstr(v,15)
        good = abs(v - mpf(r)) < mpf(10)**-12
        ok &= good
        print(f"   Z({d},{j}) = {m:>22}   lattice {r:>22}   {'MATCH' if good else 'DIFFERS'}")
    print("\nall match:", ok)
