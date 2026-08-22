"""The honest replacement for 039 section 3: R(d, d/2) is monotone, and it decays
by a factor 2^s = 1/sqrt2 per dimension."""
from marked_circles import Z
from mpmath import mp, nstr, sqrt, power, mpf
mp.dps = 20
s = mpf(-1)/2
print("  d      R(d,d/2)            R(d)/R(d-2)      R * 2^(d/2)")
prev = None
for d in range(2, 41, 2):
    R = Z(d, d//2)/Z(d, 0)
    r = "" if prev is None else nstr(R/prev, 12)
    print(f" {d:3d}   {nstr(R,12):>16}   {r:>16}   {nstr(R*power(2, mpf(d)/2), 12):>16}")
    prev = R
print()
print("predicted limit of the step ratio:  2^s = 1/sqrt2 =", nstr(power(2,s), 12))
