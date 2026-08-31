import numpy as np, math
M=20000; K=math.isqrt(M)
a1=np.zeros(M+1,dtype=np.int64); b1=np.zeros(M+1,dtype=np.int64)
e1=np.zeros(M+1,dtype=np.int64); o1=np.zeros(M+1,dtype=np.int64)
a1[0]=1;b1[0]=1;e1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; b1[n*n]+=2*(-1)**n; (e1 if n%2==0 else o1)[n*n]+=2
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
D=7
r=build([a1]*D); X1=build([b1]+[a1]*(D-1))
N={k: math.comb(D,k)*build([o1]*k+[e1]*(D-k)) for k in range(D+1)}
q=np.zeros(M+1,dtype=np.int64); q[::4]=r[:M//4+1]

print("d = 7  —  does it close the way d=5 did?")
print("   m mod 8 | occupied k | multiplier 7*X(7,1)/r_7 | ratio of the two classes")
print("   " + "-"*76)
closed=0
for res in range(8):
    sel=(m%8==res)&allm&(r!=0)
    if not sel.any(): continue
    occ=[k for k in range(D+1) if N[k][sel].any()]
    vals=np.unique((D*X1[sel])/r[sel])
    if len(vals)==1:
        mult=f"{vals[0]:+.6g}"; ratio=""
        closed+=1
    else:
        mult=f"{len(vals)} values"
        k1,k2=occ[0],occ[-1]
        den=np.where(N[k2][sel]==0,np.nan,N[k2][sel])
        rr=np.unique(N[k1][sel]/den); rr=rr[~np.isnan(rr)]
        ratio=f"N_{k1}/N_{k2}: {len(rr)} value(s)"+(f" = {rr[0]:.5f}" if len(rr)==1 else "")
        if res%4==0:
            bad=int(np.count_nonzero(D*X1[sel]!=8*q[sel]-(8-D)*r[sel]))
            ratio="TWO-SHELL LAW "+("HOLDS" if bad==0 else f"FAILS({bad})")
            closed+= (bad==0)
    print(f"      {res}     |  {str(occ):9s} | {mult:>22s}  | {ratio}")
print(f"   -> {closed}/8 classes closed")
print()
print("cross-checks:")
bad=sum(int(np.count_nonzero((build([b1]*j+[a1]*(D-j))!=np.where(m%2==0,1,-1)*build([b1]*(D-j)+[a1]*j))&allm)) for j in range(D+1))
print(f"   mirror  X(7,j) = (-1)^m X(7,7-j), all j      {'HOLDS' if bad==0 else 'FAILS'}  exc {bad}")
anyz=[j for j in range(D+1) if not np.count_nonzero(build([b1]*j+[a1]*(D-j))[1::2])]
print(f"   d=7 is ODD -> predict NO vanishing marking.  found: {anyz if anyz else 'NONE'}")
