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
for D in (5,6):
    r=build([a1]*D); X1=build([b1]+[a1]*(D-1))
    N={k: math.comb(D,k)*build([o1]*k+[e1]*(D-k)) for k in range(D+1)}
    q=np.zeros(M+1,dtype=np.int64); q[::4]=r[:M//4+1]
    print(f"=== d = {D} : is every residue class mod 8 CLOSED? ===")
    closed=0
    for res in range(8):
        sel=(m%8==res)&allm&(r!=0)
        if not sel.any(): print(f"   m={res} mod 8 : no shells"); continue
        occ=[k for k in range(D+1) if N[k][sel].any()]
        vals=np.unique((D*X1[sel])/r[sel])
        if len(vals)==1:
            print(f"   m={res} mod 8 : k={occ}  ONE MULTIPLIER {vals[0]:+.6g}"); closed+=1
        elif res%4==0:
            bad=int(np.count_nonzero(D*X1[sel]!=8*q[sel]-(8-D)*r[sel]))
            print(f"   m={res} mod 8 : k={occ}  TWO-SHELL LAW {'HOLDS' if bad==0 else 'FAILS'} ({bad} exc)")
            closed+= (bad==0)
        else:
            # is the ratio between the two occupied classes fixed?
            k1,k2=occ[0],occ[-1]
            with np.errstate(divide='ignore',invalid='ignore'):
                rr=np.unique(N[k1][sel]/np.where(N[k2][sel]==0,np.nan,N[k2][sel]))
            rr=rr[~np.isnan(rr)]
            print(f"   m={res} mod 8 : k={occ}  {len(vals)} multipliers; "
                  f"N_{k1}/N_{k2} takes {len(rr)} value(s)"
                  f"{' = %.4f'%rr[0] if len(rr)==1 else ''}")
    print(f"   -> {closed}/8 classes closed\n")
