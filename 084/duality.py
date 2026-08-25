import numpy as np, math
M = 20000; K = math.isqrt(M)
a1 = np.zeros(M+1, dtype=np.int64); b1 = np.zeros(M+1, dtype=np.int64)
a1[0]=1; b1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; b1[n*n]+=2*(-1)**n
def step(inp, seed):
    out = np.zeros(M+1, dtype=np.int64)
    for k in range(K+1):
        s = seed[k*k]
        if s: out[k*k:] += s*inp[:M+1-k*k]
    return out
X = {}
for d in range(1,7):
    for j in range(d+1):
        v = np.zeros(M+1, dtype=np.int64); v[0]=1
        for i in range(d): v = step(v, b1 if i<j else a1)
        X[(d,j)] = v

m = np.arange(M+1); sign = np.where(m%2==0, 1, -1); allm = m>=1; odd = (m%2==1)
def rep(name, ok, tot):
    print(f"   {name:<56s} {'HOLDS' if ok==0 else 'FAILS'}   exceptions {ok} / {tot}")

print("LAW 1 — marking-complement duality:   X(d,j) = (-1)^m * X(d, d-j)")
print("   " + "-"*84)
tot = 0
for d in range(1,7):
    bad = sum(int(np.count_nonzero((X[(d,j)]!=sign*X[(d,d-j)]) & allm)) for j in range(d+1))
    rep(f"d = {d}   (all j from 0 to {d})", bad, (d+1)*M)

print()
print("LAW 2 — the SELF-DUAL marking (j = d/2) must vanish on odd m")
print("   " + "-"*84)
for d in range(1,7):
    if d % 2 == 0:
        j = d//2
        rep(f"d = {d}, j = {j}  SELF-DUAL  ->  X = 0 on odd m",
            int(np.count_nonzero((X[(d,j)]!=0) & odd)), M//2)
    else:
        anyzero = [j for j in range(d+1) if not np.count_nonzero(X[(d,j)][1::2])]
        print(f"   d = {d}   no j with j = d-j   ->  predict NO vanishing marking."
              f"   found: {anyzero if anyzero else 'none'}")

print()
print("LAW 3 — d=3, ONE circle marked:  3*X(3,1)(m) = eps(m mod 4) * r_3(m)")
print("        eps = +3, +1, -1, -3   for m = 0, 1, 2, 3 mod 4")
print("   " + "-"*84)
eps = np.array([3,1,-1,-3])[m % 4]
rep("3 * X(3,1)(m) == eps(m mod 4) * r_3(m)",
    int(np.count_nonzero((3*X[(3,1)] != eps*X[(3,0)]) & allm)), M)
rep("...and the same eps law for X(3,2), via LAW 1",
    int(np.count_nonzero((3*X[(3,2)] != sign*eps*X[(3,0)]) & allm)), M)
print()
print("   the four multipliers, checked directly (m, r_3, X(3,1), ratio):")
for mm in (4,8,12,1,5,9,2,6,10,3,11,19):
    r,x = int(X[(3,0)][mm]), int(X[(3,1)][mm])
    print(f"      m={mm:3d} (m mod 4 = {mm%4})   r_3 = {r:4d}   marked = {x:5d}   3*marked/r_3 = {3*x//r if r else 0:+d}")

print()
print("LAW 3's PROOF — it rests only on 'a square is 0 or 1 mod 4, and 0,1,4 mod 8'.")
print("   split every solution of Q(n)=m by the PARITIES of its three coordinates:")
print("   " + "-"*84)
sols = {}
LIM = 4000
Kk = math.isqrt(LIM)
cnt = {}
for x in range(-Kk,Kk+1):
    for y in range(-Kk,Kk+1):
        s2 = x*x+y*y
        if s2 > LIM: continue
        for z in range(-Kk,Kk+1):
            s = s2+z*z
            if s > LIM: continue
            par = (x%2)+(y%2)+(z%2)          # number of ODD coordinates
            cnt.setdefault(s, [0,0,0,0])[par] += 1
bad = {k:0 for k in ("m=0 mod 4 -> ONLY all-even solutions",
                     "m=2 mod 4 -> NO all-even solutions",
                     "m=1 mod 4 -> NO all-odd solutions",
                     "m=3 mod 4 -> NO two-even-one-odd solutions",
                     "m=1,2 mod 4 -> r_3(m) divisible by 3")}
tot = 0
for mm in range(1, LIM+1):
    c = cnt.get(mm, [0,0,0,0]); r = sum(c); tot += 1
    if mm%4==0 and (c[1] or c[2] or c[3]): bad["m=0 mod 4 -> ONLY all-even solutions"] += 1
    if mm%4==2 and c[0]:                   bad["m=2 mod 4 -> NO all-even solutions"] += 1
    if mm%4==1 and c[3]:                   bad["m=1 mod 4 -> NO all-odd solutions"] += 1
    if mm%4==3 and c[1]:                   bad["m=3 mod 4 -> NO two-even-one-odd solutions"] += 1
    if mm%4 in (1,2) and r%3:              bad["m=1,2 mod 4 -> r_3(m) divisible by 3"] += 1
for k,v in bad.items():
    print(f"   {k:<56s} {'HOLDS' if v==0 else 'FAILS'}   exceptions {v} / {tot}")
