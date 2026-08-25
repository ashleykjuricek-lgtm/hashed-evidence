import numpy as np, math
M = 20000; K = math.isqrt(M)
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
m=np.arange(M+1); allm=m>=1
def chk(name,lhs,rhs,mask):
    bad=int(np.count_nonzero((lhs!=rhs)&mask))
    print(f"   {name:<62s} {'HOLDS' if bad==0 else 'FAILS'}  exc {bad}/{int(mask.sum())}")

r  = {d: build([a1]*d) for d in (1,2,3,4,5,6)}
X41= build([b1]+[a1]*3)
N  = {k: math.comb(4,k)*build([o1]*k+[e1]*(4-k)) for k in range(5)}

print("E - the mirror's fixed point is a HALF-SCALE COPY, in every even dimension:")
print("   " + "-"*84)
for d in (2,4,6):
    Xf = build([b1]*(d//2)+[a1]*(d//2))
    h  = np.zeros(M+1,dtype=np.int64)
    kk = np.arange(M//2+1); h[::2] = np.where(kk%2==0,1,-1)*r[d][:M//2+1]
    chk(f"d={d}, j={d//2}:  X(2k) = (-1)^k * r_{d}(k)", Xf, h, (m%2==0)&allm)
    # and the proof route: X(d,d/2) = X(2,1) convolved with itself d/2 times
    X21 = build([b1,a1]); v = np.zeros(M+1,dtype=np.int64); v[0]=1
    for _ in range(d//2): v = np.convolve(v, X21)[:M+1]
    chk(f"   ...because X({d},{d//2}) = X(2,1) convolved {d//2} times", Xf, v, allm)

print()
print("F - the m = 4 mod 8 shells, where TWO parity classes are occupied:")
print("   " + "-"*84)
chk("N4(m) = 2 * N0(m)  for m = 4 mod 8", N[4], 2*N[0], (m%8==4))
q=np.zeros(M+1,dtype=np.int64); kk=np.arange(M//4+1)
q[::4]=np.where(kk%2==0,1,-1)*r[4][:M//4+1]
chk("X(4,1)(m) = (-1)^(m/4) * r_4(m/4)  for m = 0 mod 4", X41, q, (m%4==0)&allm)

print()
print("G - how hard is each dimension, in pure divisor language:")
print("   " + "-"*84)
d13=np.zeros(M+1,dtype=np.int64)
for dd in range(1,M+1,2): d13[dd::dd] += 1 if dd%4==1 else -1
sig=np.zeros(M+1,dtype=np.int64)
for dd in range(1,M+1):
    if dd%4: sig[dd::dd]+=dd
chk("d=1:  r_1(m) = 2 if m is a square, else 0", r[1], np.where(np.isin(m,np.arange(K+1)**2)&(m>0),2,0), allm)
chk("d=2:  r_2(m) = 4 * (#divisors 1 mod 4 - #divisors 3 mod 4)", r[2], 4*d13, allm)
chk("d=4:  r_4(m) = 8 * sum of divisors not divisible by 4", r[4], 8*sig, allm)
print("   d=3:  NO such formula exists -- r_3 needs class numbers (083, Gauss)")
