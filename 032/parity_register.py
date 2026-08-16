#!/usr/bin/env python3
"""
032 — The parity law and the register.

Two claims, both about the 2D transverse dual shell of entry 029 / paper 028 §3,
where the antiperiodic character (-1)^k1 acts on the dual lattice of the plane
(antiperiodic axis, one periodic axis).

CLAIM A (exact, proved).  The character annihilates EVERY odd shell, not just m=1:

        S(m) = sum_{k1^2+k2^2=m} (-1)^k1 = 0   for all odd m.

    Proof. If m is odd then exactly one of k1,k2 is odd. The involution
    (k1,k2) -> (k2,k1) maps the shell to itself and flips the parity of k1,
    hence negates every term while permuting the same finite set. A set equal
    to its own negative sums to zero. QED

    Companion (verified here, not proved): S(2m) = (-1)^m * r2(m).

CLAIM B (measured).  The involution of Claim A is a coordinate swap, so it
    exists only when the two transverse sides are equal, i.e. only on the cube.
    Split the tail into shells that cancel at the cube (odd m) and shells that
    survive (even m), as a function of the anisotropy b on the 1 x b x b torus.
    The odd part is exactly zero at b=1 and linear around it; its derivative
    supplies essentially the whole slope of the tail.

    Consequence: paper 028 Prop. 3 argues that a steep transversal zero crossing
    implies accidental smallness, and that only a flat minimum would indicate
    protection. That dichotomy does not hold. A sub-family cancelling exactly at
    a symmetric point is zero there and generically linear away from it, which
    forces a steep transversal crossing. The steepness is the signature of the
    cancellation, not evidence against it.

The radial weight below is a PROXY, exp(-2 pi d), not the true Bessel tail.
Claim A and the vanishing of the odd part at b=1 are weight-independent (the
shell sum is zero, so any radial weight gives zero). The numerical slope shares
are proxy-dependent in magnitude, not in sign or dominance.

Authors: Ash Korth + Claude (Opus 5).  2026-08-14.
"""

import math

# ---------------------------------------------------------------- Claim A


def shell(m):
    """All (k1,k2) in Z^2 with k1^2 + k2^2 == m."""
    out = []
    L = math.isqrt(m)
    for a in range(-L, L + 1):
        b2 = m - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            for bb in ({b, -b} if b else {0}):
                out.append((a, bb))
    return out


def S(m):
    """Antiperiodic character sum over the shell |k|^2 = m."""
    return sum((-1) ** abs(a) for a, _ in shell(m))


def r2(m):
    return len(shell(m))


def claim_a(odd_limit=4000, even_limit=2000):
    bad_odd = [m for m in range(1, odd_limit, 2) if r2(m) and S(m) != 0]
    bad_even = [(m, S(2 * m), (-1) ** m * r2(m))
                for m in range(1, even_limit)
                if r2(m) and S(2 * m) != (-1) ** m * r2(m)]
    print("CLAIM A — the parity law")
    print("  S(m) = 0 for all odd m,  m = 1..%d" % (odd_limit - 1))
    print("    violations: %s" % ("NONE" if not bad_odd else bad_odd[:8]))
    print("  S(2m) = (-1)^m r2(m),   m = 1..%d" % (even_limit - 1))
    print("    violations: %s" % ("NONE" if not bad_even else bad_even[:8]))
    print()
    print("  first shells (m, r2(m), S(m)):")
    for m in range(1, 21):
        if r2(m):
            print("    %3d %5d %6d%s" % (m, r2(m), S(m),
                                         "   <- cancels" if S(m) == 0 else ""))
    print()


# ---------------------------------------------------------------- Claim B

def tail_split(b, N=40):
    """
    Transverse dual sum with the antiperiodic character on a 1 x b rectangle,
    partitioned by the shell index m = k1^2 + k2^2 that the vector HAS AT THE
    CUBE.  'odd' = the shells that cancel exactly at b=1.
    Radial weight exp(-2 pi d), d = sqrt(k1^2 + k2^2/b^2).   [PROXY]
    """
    odd = even = 0.0
    for k1 in range(-N, N + 1):
        for k2 in range(-N, N + 1):
            if k1 == 0 and k2 == 0:
                continue
            m = k1 * k1 + k2 * k2
            d = math.sqrt(k1 * k1 + k2 * k2 / (b * b))
            t = ((-1) ** abs(k1)) * math.exp(-2 * math.pi * d)
            if m % 2:
                odd += t
            else:
                even += t
    return odd, even


def uncharged(b, N=40):
    return sum(math.exp(-2 * math.pi * math.sqrt(k1 * k1 + k2 * k2 / (b * b)))
               for k1 in range(-N, N + 1) for k2 in range(-N, N + 1)
               if (k1, k2) != (0, 0))


def claim_b():
    print("CLAIM B — the register (cancellation exists only on the cube)")
    print("    b        odd part          even part         odd/even")
    for b in [0.98, 0.99, 0.999, 1.0, 1.001, 1.01, 1.02]:
        o, e = tail_split(b)
        print("  %6.4f  %+.8e   %+.8e   %+8.3f" % (b, o, e, o / e))
    print()

    o1, e1 = tail_split(1.0)
    print("  at the cube:")
    print("    odd shells  = %+.4e   (parity law says exactly 0)" % o1)
    print("    even shells = %+.4e   (the surviving sqrt2 tower)" % e1)
    print()

    print("  suppression bought by the character, at the cube:")
    print("    without character = %+.6e" % uncharged(1.0))
    print("    with character    = %+.6e" % (o1 + e1))
    print("    measured factor   = %.2fx" % abs(uncharged(1.0) / (o1 + e1)))
    print("    predicted factor  = %.2fx   = exp(2 pi (sqrt2 - 1))"
          % math.exp(2 * math.pi * (math.sqrt(2) - 1)))
    print("      (leading survivor moves from radius 1 to radius sqrt2)")
    print()

    h = 1e-4
    op, ep = tail_split(1 + h)
    om, em = tail_split(1 - h)
    do, de = (op - om) / (2 * h), (ep - em) / (2 * h)
    print("  slopes at b = 1:")
    print("    d(odd)/db  = %+.4e   <- the cancellation breaking" % do)
    print("    d(even)/db = %+.4e" % de)
    print("    odd share of total slope = %.1f%%" % (100 * abs(do / (do + de))))
    print()
    print("  => the entire steepness of the tail at the cube is generated by")
    print("     the breaking of an exact cancellation. Cf. 028 Prop. 3.")
    print()


if __name__ == "__main__":
    print("=" * 68)
    print("032 — parity law and register.  Ash Korth + Claude (Opus 5).")
    print("=" * 68)
    print()
    claim_a()
    claim_b()
