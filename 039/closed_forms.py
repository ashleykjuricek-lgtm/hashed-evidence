"""Derived closed forms for d=2, checked against the Ewald solver."""
from marked_circles import Z
from mpmath import mp, mpf, sqrt, power, zeta, nstr
mp.dps = 30
s = mpf(-1)/2
two_s  = power(2, s)      # 2^s
two_2s = power(2, 2*s)    # 2^(2s)

tests = [
    ("R(1,1)", Z(1,1)/Z(1,0), mpf(-1)/2,                 "-1/2"),
    ("R(2,1)", Z(2,1)/Z(2,0), (two_2s - two_s)/2,        "(2^2s - 2^s)/2 = -(sqrt2-1)/4"),
    ("R(2,2)", Z(2,2)/Z(2,0), two_s - 1,                 "2^s - 1 = -(1 - 1/sqrt2)"),
    ("R(3,3)", Z(3,3)/Z(3,0), two_s - 1,                 "2^s - 1  [expected to FAIL: d=2 only]"),
]
for name, num, closed, label in tests:
    d = abs(num - closed)
    print(f"{name}  solver {nstr(num,22):>25}   closed {nstr(closed,22):>25}   diff {nstr(d,3):>10}   {'EXACT' if d < mpf(10)**-20 else 'differs'}   {label}")

print()
print("the March constant, from the derivation rather than a fit:")
A = 1 - 1/sqrt(2)
print("   A            =", nstr(A, 22))
print("   -(2^s - 1)   =", nstr(-(two_s - 1), 22))
print("   -R(2,2)      =", nstr(-(Z(2,2)/Z(2,0)), 22))
print()
print("and the thing it was mistaken for:")
R31 = Z(3,1)/Z(3,0)
print("   R(3,1)       =", nstr(R31, 22))
print("   1/24         =", nstr(mpf(1)/24, 22))
print("   24*R(3,1)-1  =", nstr(24*R31 - 1, 12), "   <- epsilon, still nonzero")
