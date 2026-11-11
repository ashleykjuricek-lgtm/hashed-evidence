"""
Reproduce the well curvature A from its definition (float, stdlib only).

  Family: torus with side lengths (1, b, b); the antiperiodic direction is the length-1 side.
  eps(b) = 24 R(b) - 1,   R(b) = zeta_APP(-1/2) / zeta_PPP(-1/2)
  x = ln b,   A = coefficient of x^2 in eps = (1/2) d^2 eps / dx^2 at x = 0
            = (1/2)(eps'(1) + eps''(1))

Method: exact Ewald / incomplete-gamma split at s = -1/2 (same as c2-highprec.py,
generalised to a diagonal form). Gamma(-1/2, x) and Gamma(2, x) are closed-form, so
no quadrature. The curvature comes from a Richardson-extrapolated central difference.
"""
import math

S = -0.5
def g_high(x):   # x^{1/2} Gamma(-1/2, x)
    return math.sqrt(x) * 2.0 * (math.exp(-x) / math.sqrt(x) - math.sqrt(math.pi) * math.erfc(math.sqrt(x)))
def g_low(x):    # x^{-2} Gamma(2, x)
    return (1.0 + x) * math.exp(-x) / x**2

def zeta(b, anti, N=7):
    a = (1.0, 1.0 / b**2, 1.0 / b**2)            # Q(n) = sum a_i n_i^2
    rdet = 1.0 / math.sqrt(a[0] * a[1] * a[2])
    sh = 0.5 if anti else 0.0
    hi = lo = 0.0
    r = range(-N, N + 1)
    for i in r:
        for j in r:
            for k in r:
                Q = a[0] * (i + sh)**2 + a[1] * j * j + a[2] * k * k
                if Q > 0: hi += g_high(math.pi * Q)
                if i or j or k:
                    Qd = i * i / a[0] + j * j / a[1] + k * k / a[2]
                    lo += (-1 if (anti and i % 2) else 1) * g_low(math.pi * Qd)
    poles = (0.0 if anti else -1.0 / S) + rdet / (S - 1.5)
    return -(hi + rdet * lo + poles) / (2 * math.pi)

def eps(x):
    b = math.exp(x)
    return 24 * zeta(b, True) / zeta(b, False) - 1

def d2(h):
    return (eps(h) - 2 * eps(0.0) + eps(-h)) / (h * h)

if __name__ == "__main__":
    e0 = eps(0.0)
    h = 0.004
    A = 0.5 * (4 * d2(h / 2) - d2(h)) / 3       # Richardson
    print("eps(0) = 24R-1  =", e0, "   sealed 5.4595046537e-4")
    print("A               =", A, "   sealed 0.58260865319173")
