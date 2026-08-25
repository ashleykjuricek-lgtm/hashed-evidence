import numpy as np, math
M = 8000; K = math.isqrt(M)
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
m=np.arange(M+1); sign=np.where(m%2==0,1,-1); allm=m>=1

print("A - PARITY PURITY: how many of the (d+1) parity classes are occupied on a shell?")
print("    (a shell is 'pure' when every point on it has the same number of odd coords)")
print("   " + "-"*80)
for d in range(1,7):
    N = np.stack([math.comb(d,k)*build([o1]*k+[e1]*(d-k)) for k in range(d+1)])
    occ = (N[:,1:]>0).sum(axis=0)
    hist = np.bincount(occ, minlength=d+2)
    pure = int(hist[1]); tot = int((occ>0).sum())
    print(f"   d={d}:  max classes on any shell = {occ.max()};  "
          f"pure shells {pure}/{tot} = {100*pure/tot:5.1f}%   distribution {list(hist[1:])}")

print()
print("B - the mirror, and its fixed point, at d=5 and d=6")
print("   " + "-"*80)
for d in (5,6):
    Xs = {j: build([b1]*j+[a1]*(d-j)) for j in range(d+1)}
    bad = sum(int(np.count_nonzero((Xs[j]!=sign*Xs[d-j])&allm)) for j in range(d+1))
    print(f"   d={d}  X(d,j) = (-1)^m X(d,d-j), all j      {'HOLDS' if bad==0 else 'FAILS'}  exc {bad}")
    if d%2==0:
        j=d//2
        z = int(np.count_nonzero(Xs[j][1::2]))
        print(f"   d={d}  self-dual j={j} vanishes on odd m   {'HOLDS' if z==0 else 'FAILS'}  exc {z}")
    else:
        anyz=[j for j in range(d+1) if not np.count_nonzero(Xs[j][1::2])]
        print(f"   d={d}  ODD -> no self-dual slot; vanishing markings found: {anyz if anyz else 'NONE'}")
    globals()[f"X{d}"]=Xs

print()
print("C - does the d=3 'fixed multiplier' law survive?   d*X(d,1)(m) / r_d(m)")
print("   " + "-"*80)
for d in (3,4,5,6):
    Xs = globals().get(f"X{d}") or {j: build([b1]*j+[a1]*(d-j)) for j in (0,1)}
    r = Xs[0] if 0 in Xs else build([a1]*d)
    x1 = Xs[1]
    ok = True; rows=[]
    for res in range(8):
        sel = (m%8==res)&allm&(r!=0)
        if not sel.any(): rows.append("-"); continue
        vals = np.unique((d*x1[sel]*1.0)/r[sel])
        rows.append(f"{vals[0]:+.3g}" if len(vals)==1 else f"{len(vals)} values")
        if len(vals)!=1: ok=False
    print(f"   d={d}  by m mod 8: [{'  '.join(rows)}]   -> {'ONE MULTIPLIER PER CLASS' if ok else 'NO fixed multiplier'}")
