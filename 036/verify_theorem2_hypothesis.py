#!/usr/bin/env python3
"""
036 — the adversarial test that split Theorem 2 into 2a and 2b.

v1 claimed the odd-shell weighted sum vanishes "for any function w". That is
trivial read as a sum over shells (each term is w x 0) and unjustified read as
the lattice sum it is meant to be: for w = 1 the series is not absolutely
convergent, so regrouping it by shell needs an argument.

This script shows both halves of the split.
"""
import math


def shell_char_sum(m):
    """S(m) = sum over |k|^2 = m of (-1)^k1."""
    t = 0
    L = math.isqrt(m)
    for a in range(-L, L + 1):
        b2 = m - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            for _ in ({b, -b} if b else {0}):
                t += (-1) ** abs(a)
    return t


def odd_lattice_sum(w, N):
    """Odd-shell sum over the sigma-symmetric truncation [-N,N]^2."""
    return sum((-1) ** abs(k1) * w(math.hypot(k1, k2))
               for k1 in range(-N, N + 1)
               for k2 in range(-N, N + 1)
               if (k1 or k2) and (k1 * k1 + k2 * k2) % 2)


def abs_mass(w, N):
    """Sum of |w| over the same truncation — diverges iff 2b's hypothesis fails."""
    return sum(abs(w(math.hypot(k1, k2)))
               for k1 in range(-N, N + 1)
               for k2 in range(-N, N + 1)
               if k1 or k2)


if __name__ == "__main__":
    print("THEOREM 2a — finite sigma-symmetric truncation, ANY w")
    weights = {
        "w = 1              ": lambda d: 1.0,
        "w = exp(-2 pi d)   ": lambda d: math.exp(-2 * math.pi * d),
        "w = d^-7           ": lambda d: d ** -7,
        "w = log(1+d)/d^5   ": lambda d: math.log(1 + d) / d ** 5,
    }
    for name, w in weights.items():
        vals = [odd_lattice_sum(w, N) for N in (20, 40, 80)]
        print("  %s  N=20,40,80 -> %s" % (name, ["%+.1e" % v for v in vals]))

    print()
    print("THEOREM 2b — the hypothesis sum_k |w| < inf, tested by growth")
    for name, w in weights.items():
        m1, m2 = abs_mass(w, 40), abs_mass(w, 80)
        verdict = "CONVERGENT" if m2 / m1 < 1.05 else "DIVERGES -> 2b does NOT apply"
        print("  %s  mass(40)=%.3e  mass(80)=%.3e   %s" % (name, m1, m2, verdict))

    print()
    print("  => w = 1 vanishes under 2a and is inadmissible under 2b.")
    print("     That distinction is the whole content of the v1 -> v2 amendment.")
