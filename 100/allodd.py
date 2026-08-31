import numpy as np, math
M=20000; K=math.isqrt(M)
a1=np.zeros(M+1,dtype=np.int64); e1=np.zeros(M+1,dtype=np.int64); o1=np.zeros(M+1,dtype=np.int64)
a1[0]=1; e1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; (e1 if n%2==0 else o1)[n*n]+=2
def step(i,s):
    o=np.zeros(M+1,dtype=np.int64)
    for k in range(K+1):
        v=s[k*k]
        if v: o[k*k:]+=v*i[:M+1-k*k]
    return o
def build(ss):
    v=np.zeros(M+1,dtype=np.int64); v[0]=1
    for s in ss: v=step(v,s)
    return v
m=np.arange(M+1); allm=m>=1
print("UNIFIED ALL-ODD IDENTITY")
print("  On the class mod 8 where all-odd solutions exist and one companion class shares it:")
print("     ORDERED all-odd count  =  2 x ORDERED companion count")
print("  (ordered = before the C(d,k) placement factor)")
print("   " + "-"*70)
for D,res,kc in [(5,5,1),(6,6,2),(7,7,3),(4,4,0)]:
    Aord=build([o1]*kc+[e1]*(D-kc))     # ordered, companion class
    Bord=build([o1]*D)                   # ordered, all odd
    sel=(m%8==res)&allm
    bad=int(np.count_nonzero(Bord[sel]!=2*Aord[sel]))
    print(f"   d={D}, m={res} mod 8, companion k={kc}:  B == 2A   "
          f"{'HOLDS' if bad==0 else 'FAILS'}   exc {bad}/{int(sel.sum())}")
print()
print("  which reproduces every observed ratio, via N_k = C(d,k)*ordered:")
for D,res,kc in [(5,5,1),(6,6,2),(7,7,3)]:
    c1,c2=math.comb(D,kc),1
    print(f"   d={D}: N_{kc}/N_{D} = C({D},{kc})*A / B = {c1}A/2A = {c1/2}")
print()
print("DIVISIBILITY forced by X being an integer:")
for D,res in [(5,5),(7,7),(7,3)]:
    r=build([a1]*D); sel=(m%8==res)&allm&(r!=0)
    for p in (5,7,37):
        bad=int(np.count_nonzero(r[sel]%p))
        if bad==0: print(f"   d={D}, m={res} mod 8:  {p} divides r_{D}(m)   HOLDS  0/{int(sel.sum())}")
