"""
Same continuation as fastb0.py but with the direct-lattice energies bucketed by
multiplicity, which collapses the inner loop from ~15625 terms to a few hundred.
"""
import math
from collections import Counter

PI = math.pi
LAM = 1.0
NDIR = 12
NDUAL = 12
NQ = 60000


def _buckets(b, alpha, ndir=NDIR):
    """Distinct (n1+a1)^2 and ((n2+a2)^2+(n3+a3)^2) combos with multiplicity."""
    c1 = Counter()
    for n1 in range(-ndir, ndir + 1):
        v = n1 + alpha[0]
        c1[v * v] += 1
    c23 = Counter()
    for n2 in range(-ndir, ndir + 1):
        v2 = (n2 + alpha[1]) ** 2
        for n3 in range(-ndir, ndir + 1):
            c23[v2 + (n3 + alpha[2]) ** 2] += 1
    inv = 1.0 / (b * b)
    out = Counter()
    for e1, m1 in c1.items():
        for e23, m23 in c23.items():
            out[e1 + inv * e23] += m1 * m23
    return sorted(out.items())


def zeta(b, alpha, lam=LAM, ndual=NDUAL, nq=NQ):
    a1, a2 = 1.0, 1.0 / (b * b)
    C = PI ** 1.5 / math.sqrt(a1 * a2 * a2)
    delta = 1.0 if all(x == 0 for x in alpha) else 0.0
    buck = _buckets(b, alpha)

    tot = 0.0
    for i in range(nq):
        u = (i + 0.5) / nq
        t = lam / u
        s = 0.0
        for q, m in buck:
            x = t * q
            if x < 700.0:
                s += m * math.exp(-x)
            elif q > 0:
                break
        tot += t ** (-1.5) * (s - delta) * lam / (u * u)
    tail = tot / nq

    dual = 0.0
    for k1 in range(-ndual, ndual + 1):
        ph = -1.0 if (alpha[0] == 0.5 and k1 % 2) else 1.0
        for k2 in range(-ndual, ndual + 1):
            for k3 in range(-ndual, ndual + 1):
                if k1 == 0 and k2 == 0 and k3 == 0:
                    continue
                Rk = k1 * k1 + (k2 * k2 + k3 * k3) / a2
                p = PI * PI * Rk
                if p / lam < 700.0:
                    dual += ph * (1.0 + p / lam) * math.exp(-p / lam) / (p * p)
    dual *= C

    total = tail - C * 0.5 / lam ** 2 + dual
    if delta:
        total += 2.0 * lam ** -0.5
    return total / (-2.0 * math.sqrt(PI))


def eps(b):
    return 24.0 * zeta(b, (0.5, 0.0, 0.0)) / zeta(b, (0.0, 0.0, 0.0)) - 1.0


if __name__ == "__main__":
    REF = 5.459504653706e-04
    e1 = eps(1.0)
    print("eps(1) = %.12e   ref %.12e   rel.err %.2e" % (e1, REF, abs(e1 - REF) / REF))

    h = 1e-5
    slope = (eps(1 + h) - eps(1 - h)) / (2 * h)
    print("slope at b=1 = %.5f   (028 magnitude 18.3)" % slope)

    b0 = 1.0 - e1 / slope
    print()
    print("b0 (linear)  = %.10f" % b0)
    print("|b0 - 1|     = %.4e   (028: ~3e-5)" % abs(b0 - 1.0))
    print("eps(b0)      = %+.4e   (residual check)" % eps(b0))

    print()
    print("=== DUALITY  eps(b) + eps(1/b) ===")
    for b in [0.96, 0.98, 0.99, 1.01, 1.04]:
        x, y = eps(b), eps(1.0 / b)
        print("  b=%-6.3f  eps(b)=%+.9e  eps(1/b)=%+.9e  sum=%+.4e  sum/|eps|=%+.5f"
              % (b, x, y, x + y, (x + y) / abs(x)))
