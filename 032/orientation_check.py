#!/usr/bin/env python3
"""032 section 6.2 — orientation-blindness of the scalar Epstein sum.

Theorem: for any character chi_a(n) = exp(2 pi i a n1),  Z_a(s) = Z_{-a}(s),
and Z_a(s) is real, because the sum pairs n with -n at equal |n|.
"""
import math, cmath

def Zchar(alpha, s=2.0, N=14):
    tot = 0j
    for n1 in range(-N, N + 1):
        for n2 in range(-N, N + 1):
            for n3 in range(-N, N + 1):
                m = n1 * n1 + n2 * n2 + n3 * n3
                if m:
                    tot += cmath.exp(2j * math.pi * alpha * n1) / m ** s
    return tot

print("alpha      Z(+a)             |Z(-a)-Z(+a)|   |Im Z|")
for a in (0.5, 0.25, 1 / 3, 0.1234):
    p, q = Zchar(a), Zchar(-a)
    print("%-9.4f  %+.10f    %.2e       %.2e" % (a, p.real, abs(q - p), abs(p.imag)))

print()
print("swap matrix [[0,1],[1,0]] determinant =", 0 * 0 - 1 * 1,
      "-> orientation-REVERSING (the involution proving the parity law)")
