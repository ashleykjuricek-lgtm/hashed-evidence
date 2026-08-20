#!/usr/bin/env python3
"""038 — the three closures, reproducible.

Theorem 3  transversality off the square, via T2(m)
Item 1     the parity zero reproduces 028's -5.709 through the quotient
Theorem 4  T(m) = 2 * sum_{k3 odd} S(m - k3^2)   for odd m
"""
import math


def shell2(m):
    if m == 0:
        return [(0, 0)]
    out, L = [], math.isqrt(m)
    for a in range(-L, L + 1):
        b2 = m - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            for bb in ({b, -b} if b else {0}):
                out.append((a, bb))
    return out


S  = lambda m: sum((-1) ** abs(a) for a, b in shell2(m))
T2 = lambda m: sum((-1) ** abs(a) * b * b for a, b in shell2(m))
T1 = lambda m: sum((-1) ** abs(a) * a * a for a, b in shell2(m))
r2 = lambda m: 0 if m == 0 else len(shell2(m))


def T3(m):
    t, L = 0, math.isqrt(m)
    for a in range(-L, L + 1):
        for b in range(-L, L + 1):
            c2 = m - a * a - b * b
            if c2 < 0:
                continue
            c = math.isqrt(c2)
            if c * c == c2:
                for _ in ({c, -c} if c else {0}):
                    t += (-1) ** abs(a)
    return t


print("THEOREM 3 — transversality")
z = [m for m in range(1, 4000, 2) if r2(m) and T2(m) == 0]
print("  odd m<4000 with T2(m)=0 :", z if z else "NONE")
bad = [m for m in range(1, 2000, 2) if r2(m) and T1(m) + T2(m) != m * S(m)]
print("  T1+T2 = m*S(m) violations:", bad if bad else "NONE")
wp = lambda d: -2 * math.pi * math.exp(-2 * math.pi * d)
terms = [(-wp(math.sqrt(m)) / math.sqrt(m) * T2(m)) for m in range(1, 2000, 2) if r2(m)]
print("  slope (closed form)      : %+.6e" % sum(terms))
print("  slope (032, finite diff) : +2.3441e-02")
print("  |m=1| / sum|rest|        : %.1f" % (abs(terms[0]) / sum(abs(t) for t in terms[1:])))

print()
print("ITEM 1 — the parity zero, through the quotient")
q = math.exp(-2 * math.pi)
D0, N0 = -0.26373, -0.01121
D1 = 4 * (-(1 / math.pi) * (1 + 1 / (2 * math.pi)))
coeff = 24 / D0 ** 2 * (0.0 * D0 - N0 * D1)
print("  N_1 = 0 (parity) -> coefficient of e^-2pi = %+.4f   [028: -5.709]" % coeff)
print("                      K_1                   = %+.5e  [028: -1.0662e-02]" % (coeff * q))

print()
print("THEOREM 4 — one coordinate at a time")
bad = [m for m in range(1, 300, 2)
       if T3(m) != 2 * sum(S(m - k * k) for k in range(1, math.isqrt(m) + 1, 2))]
print("  odd m<300, T(m) = 2*sum_{k3 odd} S(m-k3^2) violations:", bad if bad else "NONE")
print("  T(1) = %d = 2*S(0) = %d      T(3) = %d = 2*S(2) = %d  <- the sqrt2 shell"
      % (T3(1), 2 * S(0), T3(3), 2 * S(2)))
