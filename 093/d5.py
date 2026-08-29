import numpy as np, math
M = 40000; K = math.isqrt(M)
a1=np.zeros(M+1,dtype=np.int64); b1=np.zeros(M+1,dtype=np.int64)
e1=np.zeros(M+1,dtype=np.int64); o1=np.zeros(M+1,dtype=np.int64)
a1[0]=1; b1[0]=1; e1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; b1[n*n]+=2*(-1)**n; (e1 if n%2==0 else o1)[n*n]+=2
def step(inp,seed):
    out=np.zeros(M+1,dtype=np.int64)
    for k in range(K+1):
        s=seed[k*k]
        if s: out[k*k:]+=s*inp[:M+1-k*k]
    return out
def build(seeds):
    v=np.zeros(M+1,dtype=np.int64); v[0]=1
    for s in seeds: v=step(v,s)
    return v
D=5
r5  = build([a1]*D)
X51 = build([b1]+[a1]*(D-1))
N   = {k: math.comb(D,k)*build([o1]*k+[e1]*(D-k)) for k in range(D+1)}
m=np.arange(M+1); allm=m>=1
def rep(n,bad,tot): print(f"   {n:<56s} {'HOLDS' if bad==0 else 'FAILS'}  exc {bad}/{tot}")

print("A - which parity classes are OCCUPIED, by m mod 8   (d=5, k = # odd coords)")
print("   " + "-"*78)
for res in range(8):
    sel=(m%8==res)&allm
    occ=[k for k in range(6) if N[k][sel].any()]
    print(f"   m = {res} mod 8 :  k in {occ}"
          f"{'   <- TWO classes' if len(occ)>1 else ''}")

print()
print("B - the fixed multiplier, class by class:  5*X(5,1)(m) / r_5(m)")
print("   " + "-"*78)
for res in range(8):
    sel=(m%8==res)&allm&(r5!=0)
    if not sel.any(): print(f"   m = {res} mod 8 :  (no shells)"); continue
    vals=np.unique((5*X51[sel])/r5[sel])
    print(f"   m = {res} mod 8 :  {('%+.6g'%vals[0]) if len(vals)==1 else str(len(vals))+' distinct values'}")

print()
print("C - the two shells:  is X(5,1)(m) fixed by r_5(m) AND r_5(m/4) together?")
print("   " + "-"*78)
q=np.zeros(M+1,dtype=np.int64); q[::4]=r5[:M//4+1]        # r_5(m/4), zero unless 4|m
sel=(m%4==0)&allm
rep("m = 0 mod 4 :  5*X(5,1)(m) = 8*r_5(m/4) - 3*r_5(m)",
    int(np.count_nonzero(5*X51[sel] != 8*q[sel]-3*r5[sel])), int(sel.sum()))
rep("m = 0 mod 4 :  N_0(m) = r_5(m/4)   (all-even solutions)",
    int(np.count_nonzero(N[0][sel]!=q[sel])), int(sel.sum()))

print()
print("D - m = 5 mod 8 has TWO classes yet ONE multiplier. Why?")
print("   " + "-"*78)
sel=(m%8==5)&allm
rep("m = 5 mod 8 :  2*N_1(m) = 5*N_5(m)",
    int(np.count_nonzero(2*N[1][sel]!=5*N[5][sel])), int(sel.sum()))
print("      sample (m, N_1, N_5, ratio N_1/N_5):")
got=0
for mm in range(5,M+1,8):
    if N[5][mm] and got<6:
        print(f"        m={mm:5d}   N_1={N[1][mm]:6d}   N_5={N[5][mm]:5d}   ratio {N[1][mm]/N[5][mm]:.4f}")
        got+=1
