import numpy as np, math
M = 20000; K = math.isqrt(M)
a1=np.zeros(M+1,dtype=np.int64); b1=np.zeros(M+1,dtype=np.int64)
a1[0]=1; b1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; b1[n*n]+=2*(-1)**n
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
m=np.arange(M+1); allm=m>=1
print("THE TWO-SHELL LAW, m = 0 mod 4:")
print("     d * X(d,1)(m)  =  8 * r_d(m/4)  -  (8-d) * r_d(m)")
print()
print("   d  | exceptions / shells | verdict")
print("   " + "-"*58)
for d in range(1,10):
    r  = build([a1]*d)
    X1 = build([b1]+[a1]*(d-1))
    q  = np.zeros(M+1,dtype=np.int64); q[::4] = r[:M//4+1]
    sel=(m%4==0)&allm
    bad=int(np.count_nonzero(d*X1[sel] != 8*q[sel]-(8-d)*r[sel]))
    tag = "HOLDS" if bad==0 else f"FAILS ({bad} exc)"
    note = ""
    if d>=8: note = "   <- k=8 (eight odd coords) becomes possible here"
    print(f"   {d}  |     {bad:5d} / {int(sel.sum()):5d}      | {tag}{note}")
print()
print("consistency with what is already sealed:")
print("   d=3  law gives 3X = 8r(m/4) - 5r(m);  084 sealed 3X = +3r(m)")
print("        the two agree iff r_3(4m) = r_3(m)   -- which 085 verified separately")
print("   d=4  law gives 4X = 8r(m/4) - 4r(m);  085 sealed X = (-1)^(m/4) r_4(m/4)")
print("        agree iff r_4(m)=r_4(m/4) on m=0 mod 8 and r_4(m)=3r_4(m/4) on m=4 mod 8")
r3=build([a1]*3); r4=build([a1]*4)
q3=np.zeros(M+1,dtype=np.int64); q3[::4]=r3[:M//4+1]
q4=np.zeros(M+1,dtype=np.int64); q4[::4]=r4[:M//4+1]
s3=(m%4==0)&allm; s8=(m%8==0)&allm; s4=(m%8==4)&allm
print(f"        r_3(m) == r_3(m/4)          exc {int(np.count_nonzero(r3[s3]!=q3[s3]))}/{int(s3.sum())}")
print(f"        r_4(m) == r_4(m/4)  m=0(8)  exc {int(np.count_nonzero(r4[s8]!=q4[s8]))}/{int(s8.sum())}")
print(f"        r_4(m) == 3r_4(m/4) m=4(8)  exc {int(np.count_nonzero(r4[s4]!=3*q4[s4]))}/{int(s4.sum())}")
