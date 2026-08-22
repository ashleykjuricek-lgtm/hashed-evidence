"""Exhaustive test: is sign(Z(d,j)) determined by 2j - d alone?"""
from marked_circles import Z
from mpmath import mp, mpf
mp.dps = 20

bad = []; n = 0
grid = {}
for d in range(1, 17):
    for j in range(0, d+1):
        v = Z(d, j); n += 1
        grid[(d,j)] = v
        pred = (2*j >= d)          # predicted positive
        if (v > 0) != pred:
            bad.append((d, j, v, pred))

print(f"cells tested: {n}")
print(f"violations of  ' Z(d,j) > 0  <=>  2j >= d ' : {len(bad)}")
for b in bad: print("   ", b)
print()
print("does j=0 ever go positive?", any(grid[(d,0)] > 0 for d in range(1,17)))
print()
print("shape of each column, j >= 1 (excess e = d - 2j):")
print("   e:", "".join(f"{e:>11}" for e in range(-3, 5)))
for j in range(1, 7):
    row = f"  j={j}:"
    for e in range(-3, 5):
        d = e + 2*j
        row += f"{mp.nstr(grid[(d,j)],4):>11}" if (d, j) in grid and d >= 1 else " "*11
    print(row)
