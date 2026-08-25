import math
from collections import defaultdict

# h(d) for d<0 : count reduced forms (a,b,c), b^2-4ac=d, |b|<=a<=c,
#                b>=0 whenever |b|==a or a==c
def h(d):
    assert d < 0 and d % 4 in (0,1)
    n = 0
    B = int(math.isqrt(-d//3)) + 1
    for b in range(-B, B+1):
        t = b*b - d
        if t % 4: continue
        ac = t//4
        if ac == 0: continue
        for a in range(max(1,abs(b)), int(math.isqrt(ac))+1):
            if ac % a: continue
            c = ac//a
            if not (abs(b) <= a <= c): continue
            if (abs(b)==a or a==c) and b < 0: continue
            n += 1
    return n

# r3(m) = number of (x,y,z) in Z^3 with x^2+y^2+z^2 = m   -- the SHELL COUNTS of our lattice
LIM = 3000
r3 = defaultdict(int)
K = int(math.isqrt(LIM))
for x in range(-K,K+1):
    for y in range(-K,K+1):
        s2 = x*x+y*y
        if s2 > LIM: continue
        for z in range(-K,K+1):
            s = s2+z*z
            if s <= LIM: r3[s] += 1

def squarefree(m):
    for p in range(2, int(math.isqrt(m))+1):
        if m % (p*p) == 0: return False
    return True

print("GAUSS: the shell counts of the flat 3-torus lattice Z^3,")
print("       against class numbers of IMAGINARY QUADRATIC fields (the pi rows).")
print()
print("     m   m mod 8      r3(m)   Gauss prediction        h        law")
print("   " + "-"*72)
ok = bad = 0
shown = 0
for m in range(1, LIM+1):
    if not squarefree(m): continue
    r = r3[m]
    if m % 8 == 7:
        pred, hv, law = 0, None, "= 0            (Legendre)"
    elif m % 8 == 3:
        d=-m;  hv=h(d); wd = 6 if d==-3 else 2
        pred = 24*hv*2//wd; law = f"24 h(-m) * 2/w   [w={wd}]"
    elif m % 4 in (1,2):
        d=-4*m; hv=h(d); wd = 4 if d==-4 else 2
        pred = 12*hv*2//wd; law = f"12 h(-4m) * 2/w  [w={wd}]"
    else:
        continue
    if r == pred: ok += 1
    else:
        bad += 1
        if bad <= 5: print(f"   MISMATCH m={m} r3={r} pred={pred}")
    if shown < 10 and m > 1:
        print(f"   {m:5d}    {m%8}      {r:6d}   {pred:6d}              {hv if hv is not None else '-':>4}   {law}")
        shown += 1

print("   " + "-"*72)
print(f"   squarefree m <= {LIM}:   {ok} agreements, {bad} mismatches")
print()
print("Every shell count of Z^3 is a class number of an IMAGINARY quadratic field")
print("times 24/w.  Imaginary quadratic = r2 = 1 = the rows that pay pi.")
