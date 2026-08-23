"""R(b) from the REAL anisotropic Epstein sum -- KESTREL's ask #1.

Torus with side lengths L = (L1,...,Ld). Modes are (n_i + alpha_i)/L_i, so

    Theta(t) = prod_i  theta_{alpha_i}( t / L_i^2 )

which factorises exactly as in 042 -- only the argument is rescaled. Small-t:
theta(t/L^2) ~ L*sqrt(pi/t), so Theta(t) ~ V * (pi/t)^(d/2) with V = prod L_i.

No fitted slope anywhere. Exact Ewald, arbitrary real b.
"""
from mpmath import mp, mpf, pi, gamma, quad, exp, inf, nstr, sqrt
mp.dps = 30

def Z(L, alpha, s=mpf(-0.5), lam=mpf(1), N=20, K=8):
    """L = list of side lengths, alpha = list of 0 or 1/2 per axis."""
    L = [mpf(x) for x in L]; d = len(L)
    V = mpf(1)
    for x in L: V *= x
    rng = range(-N, N+1); krng = range(1, K+1)
    half = mpf(1)/2
    delta = 1 if all(a == 0 for a in alpha) else 0

    def th_direct(u, a):                      # sum_n exp(-u (n+a)^2)
        return sum(exp(-u*(n+a)**2) for n in rng)
    def th_dualfac(u, a):                     # theta(u) = sqrt(pi/u) * F(u)
        if a == 0: return 1 + 2*sum(exp(-pi**2*k*k/u) for k in krng)
        return      1 + 2*sum((-1)**k*exp(-pi**2*k*k/u) for k in krng)

    def small(t):
        br = mpf(1)
        for Li, a in zip(L, alpha): br *= th_dualfac(t/Li**2, mpf(a))
        return V*pi**(d/2)*t**(s-1-mpf(d)/2)*(br - 1)
    def big(t):
        v = mpf(1)
        for Li, a in zip(L, alpha): v *= th_direct(t/Li**2, mpf(a))
        return t**(s-1)*(v - delta)

    tot = quad(small, [0, lam]) + V*pi**(mpf(d)/2)*lam**(s-mpf(d)/2)/(s-mpf(d)/2) + quad(big, [lam, inf])
    if delta: tot -= lam**s/s
    return tot/gamma(s)

if __name__ == "__main__":
    import sys
    A, P = mpf(1)/2, mpf(0)
    print("validation at b = 1 against the isotropic solver (039/042):")
    for name, al, ref in [("PPP", [P,P,P], "-0.266596278718393"),
                          ("APP", [A,P,P], "-0.0111142427950344"),
                          ("AAP", [A,A,P], "0.0347814624899515"),
                          ("AAA", [A,A,A], "0.0622964802744454")]:
        v = Z([1,1,1], al)
        print(f"   {name}  {nstr(v,15):>22}   ref {ref:>22}")
    print()
    print("R(b) = Z_APP / Z_PPP  on the 1 x b x b torus, from the exact sum:")
    print("      b            R(b)                    eps(b) = 24R - 1")
    for b in ['0.90','0.95','0.98','0.99','1.00','1.01','1.02','1.05','1.10']:
        bb = mpf(b)
        num = Z([1,bb,bb], [A,P,P]); den = Z([1,bb,bb], [P,P,P])
        R = num/den
        print(f"   {b:>6}   {nstr(R,18):>22}   {nstr(24*R-1,14):>18}")
        sys.stdout.flush()
