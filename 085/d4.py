import numpy as np, math
M = 20000; K = math.isqrt(M)

a1 = np.zeros(M+1, dtype=np.int64); b1 = np.zeros(M+1, dtype=np.int64)
e1 = np.zeros(M+1, dtype=np.int64); o1 = np.zeros(M+1, dtype=np.int64)
a1[0]=1; b1[0]=1; e1[0]=1
for n in range(1,K+1):
    a1[n*n]+=2; b1[n*n]+=2*(-1)**n
    (e1 if n%2==0 else o1)[n*n]+=2

def step(inp, seed):
    out = np.zeros(M+1, dtype=np.int64)
    for k in range(K+1):
        s = seed[k*k]
        if s: out[k*k:] += s*inp[:M+1-k*k]
    return out
def build(seeds):
    v = np.zeros(M+1, dtype=np.int64); v[0]=1
    for s in seeds: v = step(v, s)
    return v

X = {j: build([b1]*j + [a1]*(4-j)) for j in range(5)}
r4 = X[0]
r4half = {d: build([a1]*d) for d in (1,2,3,4)}

# N_k = number of solutions with exactly k ODD coordinates
N = {k: math.comb(4,k)*build([o1]*k + [e1]*(4-k)) for k in range(5)}

m = np.arange(M+1); sign = np.where(m%2==0,1,-1); allm = m>=1
def rep(name, bad, tot):
    print(f"   {name:<58s} {'HOLDS' if bad==0 else 'FAILS'}   exceptions {bad} / {tot}")
def chk(name, lhs, rhs, mask):
    rep(name, int(np.count_nonzero((lhs!=rhs)&mask)), int(mask.sum()))

print("d = 4.  m :   r_4    | X(4,1)  X(4,2)  X(4,3)  X(4,4) |  N0   N1   N2   N3   N4")
print("   " + "-"*84)
for mm in range(1,21):
    print(f"      {mm:3d} : {r4[mm]:6d}  |{X[1][mm]:7d} {X[2][mm]:7d} {X[3][mm]:7d} {X[4][mm]:7d} |"
          f"{N[0][mm]:5d}{N[1][mm]:5d}{N[2][mm]:5d}{N[3][mm]:5d}{N[4][mm]:5d}")

print()
print("A - the shell count itself, with NO constant of any kind (Jacobi):")
print("   " + "-"*84)
sig = np.zeros(M+1, dtype=np.int64)      # sum of divisors d of m with 4 not dividing d
for d in range(1, M+1):
    if d % 4: sig[d::d] += d
chk("r_4(m) = 8 * sum of divisors d of m with 4 not | d", r4, 8*sig, allm)
chk("r_4(m) = 8*sigma(m) for ODD m", r4, 8*sig, (m%2==1))

print()
print("B - THE MIRROR'S FIXED POINT, j = 2:")
print("   " + "-"*84)
chk("X(4,2)(m) = 0 on odd m", X[2], np.zeros(M+1,dtype=np.int64), (m%2==1))
half = np.zeros(M+1,dtype=np.int64); half[::2] = sign[:M//2+1]*r4[:M//2+1]
chk("X(4,2)(2k) = (-1)^k * r_4(k)   <- SELF-SIMILAR AT HALF SCALE", X[2], half, (m%2==0)&allm)

print()
print("C - the non-fixed markings:")
print("   " + "-"*84)
chk("X(4,4)(m) = (-1)^m r_4(m)        [LAW 1]", X[4], sign*r4, allm)
chk("X(4,3)(m) = (-1)^m X(4,1)(m)     [LAW 1]", X[3], sign*X[1], allm)
eps = np.where(m%4==1, 1, -1)
chk("X(4,1)(m) = eps * r_4(m)/2 on ODD m   eps=+1 if m=1 mod 4", 2*X[1], eps*r4, (m%2==1))
chk("X(4,1)(m) = 4*sigma(m)*eps on ODD m", X[1], eps*4*sig, (m%2==1))
chk("X(4,1)(m) = 0 for m = 2 mod 4         <- A SECOND VANISHING", X[1], np.zeros(M+1,dtype=np.int64), (m%4==2))
q = np.zeros(M+1,dtype=np.int64); q[::4] = r4[:M//4+1]
chk("X(4,1)(m) = r_4(m/4) for m = 0 mod 8", X[1], q, (m%8==0)&allm)
chk("X(4,1)(m) = r_4(m/4) - N4(m) for m = 4 mod 8", X[1], q-N[4], (m%8==4))
chk("X(4,1)(m) = N0 - N4 for ALL even m", X[1], N[0]-N[4], (m%2==0)&allm)

print()
print("D - which parity classes are EMPTY (this is what forces C):")
print("   " + "-"*84)
for k,cond,name in [(0,(m%4!=0),"N0 (all even) = 0 unless m = 0 mod 4"),
                    (4,(m%8!=4),"N4 (all odd)  = 0 unless m = 4 mod 8"),
                    (1,(m%4==3),"N1 = 0 when m = 3 mod 4"),
                    (3,(m%4==1),"N3 = 0 when m = 1 mod 4"),
                    (2,(m%4==0)&allm,"N2 = 0 when m = 0 mod 4")]:
    chk(name, N[k], np.zeros(M+1,dtype=np.int64), cond&allm)
chk("N0(m) = r_4(m/4)  for m = 0 mod 4", N[0], np.where(m%4==0, np.pad(r4[:M//4+1],(0,M-M//4))[ (m//4).clip(0,M) ], 0), (m%4==0)&allm)
