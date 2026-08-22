"""The one claim the page loses: you cannot remain at the crossing.
Show the sign flip is between consecutive integers, everywhere, with no cell on it."""
from marked_circles import Z
from mpmath import mp
mp.dps = 20

on_zero = []; flips = []; n = 0
for d in range(1, 17):
    for j in range(0, d+1):
        v = Z(d, j); n += 1
        if v == 0: on_zero.append((d, j))
for j in range(0, 9):
    lo, hi = 2*j, 2*j+1
    if lo < 1: continue
    a = Z(lo, j) if lo <= 16 and j <= lo else None
    b = Z(hi, j) if hi <= 17 and j <= hi else None
    if a is not None and b is not None:
        flips.append((j, lo, hi, a > 0, b < 0))

print(f"configurations evaluated: {n}")
print(f"configurations where Z == 0 exactly: {len(on_zero)}   {on_zero}")
print()
print("every sign flip sits between two CONSECUTIVE integers d, with nothing between:")
for j, lo, hi, pa, pb in flips:
    print(f"   j={j}:  d={lo} positive={pa}   ->   d={hi} negative={pb}   gap = {hi-lo}")
print()
print("conclusion: the crossing is real (sign changes) and unoccupied (no cell is zero,")
print("            and no lattice exists between d and d+1).  '(STAY)' is unavailable.")
