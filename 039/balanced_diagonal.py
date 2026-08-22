from marked_circles import Z
from mpmath import mp, mpf
mp.dps = 25
print("exactly half marked  (j = d/2):")
prev=None
for d in range(2, 25, 2):
    v = Z(d, d//2)
    arrow = "" if prev is None else ("  down" if v < prev else "  UP")
    print(f"  d={d:3d}  j={d//2:2d}   Z = {mp.nstr(v,12):>16}{arrow}")
    prev = v
print()
print("sign-flip law:  is Z(2j, j) > 0 > Z(2j+1, j) for every j?")
for j in range(1, 9):
    a, b = Z(2*j, j), Z(2*j+1, j)
    print(f"  j={j}:  Z({2*j},{j})={mp.nstr(a,8):>12}   Z({2*j+1},{j})={mp.nstr(b,8):>12}   law holds: {a>0>b}")
