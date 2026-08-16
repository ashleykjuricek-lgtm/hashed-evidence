"""
Anisotropic Epstein zeta on the 1 x b x b torus, continued to s = -1/2.

Independent implementation (Ewald / theta split + Poisson), NOT ported from
hashed-evidence A.3, so it is a real cross-check.

Q(x) = a1 x1^2 + a2 x2^2 + a3 x3^2,  a = (1, 1/b^2, 1/b^2)
Z(s; alpha) = sum'_{n in Z^3} Q(n+alpha)^{-s}

Gamma(s) Z(s) = int_lam^inf t^{s-1} [Theta(t) - delta] dt
                - delta * lam^s / s
                + C * lam^{s-3/2} / (s - 3/2)
                + C * sum_{k != 0} e^{2 pi i k.alpha} * (pi^2 R_k)^{-(3/2-s)}
                                   * Gamma(3/2-s, pi^2 R_k / lam)

Theta(t) = sum_n exp(-t Q(n+alpha)),  C = pi^{3/2}/sqrt(a1 a2 a3),
R_k = sum k_i^2 / a_i,  delta = 1 iff alpha in Z^3.
"""
from mpmath import mp, mpf, exp, sqrt, pi, gamma, gammainc, quad, findroot

mp.dps = 40

LAM = mpf(1)
NDIR = 14   # direct-sum half-width for Theta
NDUAL = 14  # dual-sum half-width


def zeta_aniso(b, alpha, s=mpf(-0.5), lam=LAM, ndir=NDIR, ndual=NDUAL):
    b = mpf(b)
    a = [mpf(1), 1 / b**2, 1 / b**2]
    a1, a2, a3 = a
    C = pi**mpf(1.5) / sqrt(a1 * a2 * a3)
    delta = 1 if all(x == 0 for x in alpha) else 0

    def Q(x):
        return a1 * x[0]**2 + a2 * x[1]**2 + a3 * x[2]**2

    def Theta(t):
        tot = mpf(0)
        for n1 in range(-ndir, ndir + 1):
            v1 = n1 + alpha[0]
            e1 = a1 * v1 * v1
            for n2 in range(-ndir, ndir + 1):
                v2 = n2 + alpha[1]
                e2 = e1 + a2 * v2 * v2
                for n3 in range(-ndir, ndir + 1):
                    v3 = n3 + alpha[2]
                    tot += exp(-t * (e2 + a3 * v3 * v3))
        return tot

    tail = quad(lambda t: t**(s - 1) * (Theta(t) - delta), [lam, mp.inf])

    c = mpf(1.5) - s
    dual = mpf(0)
    for k1 in range(-ndual, ndual + 1):
        for k2 in range(-ndual, ndual + 1):
            for k3 in range(-ndual, ndual + 1):
                if k1 == 0 and k2 == 0 and k3 == 0:
                    continue
                Rk = k1 * k1 / a1 + k2 * k2 / a2 + k3 * k3 / a3
                p = pi**2 * Rk
                phase = (-1)**k1 if alpha[0] == mpf(0.5) else 1
                dual += phase * p**(-c) * gammainc(c, p / lam)
    dual *= C

    total = tail + C * lam**(s - mpf(1.5)) / (s - mpf(1.5)) + dual
    if delta:
        total -= lam**s / s
    return total / gamma(s)


def eps(b):
    """eps(b) = 24 * Z_APP / Z_PPP - 1"""
    P = zeta_aniso(b, [mpf(0), mpf(0), mpf(0)])
    A = zeta_aniso(b, [mpf(0.5), mpf(0), mpf(0)])
    return 24 * A / P - 1, P, A


if __name__ == "__main__":
    print("=== VALIDATION AT THE CUBE (b=1) ===")
    e1, P, A = eps(1)
    print("Z_PPP(-1/2) =", mp.nstr(P, 25))
    print("  reference = -0.26659627871839347461049847...")
    print("Z_APP(-1/2) =", mp.nstr(A, 25))
    print("  reference = -0.011114242795034410520050...")
    print("ratio       =", mp.nstr(A / P, 25))
    print("  reference =  0.041689414602723775120079...")
    print("eps(1)      =", mp.nstr(e1, 20))
    print("  reference =  0.00054595046537060288190...")
