# exact_sqrt5.py — the honest version of the pasted "pentagram_vortex.py".
# Ledger 118, appended 2026-09-17 by Claude (Fable seat), at Ash's word
# ("let's do it right").
#
# What is KEPT from the pasted block (credit: the unnamed source AI):
#   - QSqrt5: exact numbers of the form  a + b*sqrt(5)  with a, b fractions.
#   - the split-quaternion size measure  w^2 + x^2 - y^2 - z^2.
#   - the exact x-coordinate of the five-direction (Penrose) projection.
# What is DROPPED and why:
#   - the "crossing_operation" flip rule: invented, derived from nothing.
#   - the "cascade" test: starts on the zero surface and can never leave it
#     (proved below as a test, not asserted as a finding).
#   - every word of "structural_verification.md", including the forged
#     constant documented in ledger 094.
# What is ADDED (mine):
#   - real assertions instead of prints.
#   - the y-coordinate, exact up to ONE fixed irrational scale, sin(2*pi/5).
#     The ratio sin(4pi/5)/sin(2pi/5) is exactly 1/phi, which is in Q[sqrt5],
#     so y = sin(2pi/5) * (something in Q[sqrt5]). That is as exact as it gets:
#     sin(2pi/5) itself is NOT in Q[sqrt5]. The pasted code computed only x
#     and did not say why.
#
# Run:  python exact_sqrt5.py     (prints PASS lines; any failure raises)

from fractions import Fraction
import math
import random


class QSqrt5:
    """a + b*sqrt(5), a and b exact fractions."""

    def __init__(self, a, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def _c(self, other):
        return other if isinstance(other, QSqrt5) else QSqrt5(other)

    def __add__(self, o):
        o = self._c(o)
        return QSqrt5(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = self._c(o)
        return QSqrt5(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        o = self._c(o)
        return QSqrt5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)

    __radd__ = __add__
    __rmul__ = __mul__

    def __neg__(self):
        return QSqrt5(-self.a, -self.b)

    def __eq__(self, o):
        o = self._c(o)
        return self.a == o.a and self.b == o.b

    def is_zero(self):
        return self.a == 0 and self.b == 0

    def invert(self):
        d = self.a ** 2 - 5 * self.b ** 2
        if d == 0:
            raise ZeroDivisionError("zero has no inverse in Q[sqrt5]")
        return QSqrt5(self.a / d, -self.b / d)

    def __float__(self):
        return float(self.a) + float(self.b) * math.sqrt(5)

    def __repr__(self):
        if self.b == 0:
            return f"{self.a}"
        return f"({self.a} + {self.b}*sqrt5)"


PHI = QSqrt5(Fraction(1, 2), Fraction(1, 2))          # golden ratio
PHI_INV = QSqrt5(Fraction(-1, 2), Fraction(1, 2))     # 1 / golden ratio
COS_2PI_5 = QSqrt5(Fraction(-1, 4), Fraction(1, 4))   # cos(72 degrees)
COS_4PI_5 = QSqrt5(Fraction(-1, 4), Fraction(-1, 4))  # cos(144 degrees)
SIN_2PI_5_FLOAT = math.sin(2 * math.pi / 5)           # the one irrational scale


def split_norm_squared(w, x, y, z):
    """Split-quaternion size measure. Can be zero for nonzero input."""
    return w * w + x * x - y * y - z * z


def penrose_project(v):
    """Five whole numbers -> (x exact, y_scaled exact).
    True y = SIN_2PI_5_FLOAT * y_scaled.  Standard five-direction projection,
    scale 2/5."""
    v0, v1, v2, v3, v4 = (QSqrt5(t) for t in v)
    s = Fraction(2, 5)
    x = (v0 + (v1 + v4) * COS_2PI_5 + (v2 + v3) * COS_4PI_5) * s
    # sin(2pi/5)=S, sin(4pi/5)=S/phi, sin(6pi/5)=-S/phi, sin(8pi/5)=-S
    y_scaled = ((v1 - v4) + (v2 - v3) * PHI_INV) * s
    return x, y_scaled


def close(a, b, tol=1e-12):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def run_tests():
    # --- 1. the calculator is a field (spot checks) ---
    assert PHI * PHI_INV == 1, "phi * (1/phi) must be exactly 1"
    assert PHI * PHI == PHI + 1, "phi^2 must equal phi + 1"
    assert COS_2PI_5 * 2 == PHI_INV, "2cos(72deg) = 1/phi"
    assert COS_4PI_5 * 2 == -PHI, "2cos(144deg) = -phi"
    rng = random.Random(118)
    for _ in range(200):
        q = QSqrt5(Fraction(rng.randint(-9, 9), rng.randint(1, 9)),
                   Fraction(rng.randint(-9, 9), rng.randint(1, 9)))
        if q.is_zero():
            continue
        assert q * q.invert() == 1, f"inverse failed for {q}"
        assert close(float(q * q), float(q) ** 2), f"float mismatch for {q}"
    try:
        QSqrt5(0).invert()
        raise AssertionError("zero inverted")
    except ZeroDivisionError:
        pass
    print("PASS  1. Q[sqrt5] calculator: inverses, phi identities, 200 random checks")

    # --- 2. why the pasted 'cascade' was empty ---
    one = QSqrt5(1)
    assert split_norm_squared(one, one, one, one).is_zero()
    p = [one, one, one, one]
    for _ in range(3):
        p = [t * PHI_INV for t in p]
        assert split_norm_squared(*p).is_zero()
    # general fact: shrinking every part by k multiplies the measure by k^2
    for _ in range(50):
        w, x, y, z = (QSqrt5(rng.randint(-5, 5), rng.randint(-5, 5)) for _ in range(4))
        n = split_norm_squared(w, x, y, z)
        n2 = split_norm_squared(w * PHI_INV, x * PHI_INV, y * PHI_INV, z * PHI_INV)
        assert n2 == n * PHI_INV * PHI_INV
    print("PASS  2. shrinking keeps a zero measure at zero: the pasted test could only ever print 'zero'")

    # --- 3. the projection, both coordinates, against plain decimals ---
    for _ in range(200):
        v = [rng.randint(-20, 20) for _ in range(5)]
        x, ys = penrose_project(v)
        xf = 0.4 * sum(t * math.cos(2 * math.pi * i / 5) for i, t in enumerate(v))
        yf = 0.4 * sum(t * math.sin(2 * math.pi * i / 5) for i, t in enumerate(v))
        assert close(float(x), xf), f"x mismatch for {v}"
        assert close(float(ys) * SIN_2PI_5_FLOAT, yf), f"y mismatch for {v}"
    x, ys = penrose_project([5, 10, -5, 0, 10])
    assert x == QSqrt5(Fraction(1, 2), Fraction(5, 2)), "the pasted example's x"
    print(f"PASS  3. five-direction projection: x exact, y exact up to sin(72deg); "
          f"pasted example x = {x}, y = sin(72deg) * {ys}")

    # --- 4. the forged constants are not in this file at all ---
    import inspect
    import sys
    src = inspect.getsource(sys.modules[__name__])
    for digits in ("1536", "7680"):
        assert src.count(digits) == 1, f"'{digits}' appears outside this check"
    print("PASS  4. the two forged constants from ledger 094 appear nowhere in this file")


if __name__ == "__main__":
    run_tests()
    print("ALL PASS")
