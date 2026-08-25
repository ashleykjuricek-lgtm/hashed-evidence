import numpy as np, math
X = 2_000_000
# Z[i] and Z[sqrt-2] are principal, so IDEALS = ELEMENTS / UNITS, exactly.
# Units: 4 in Z[i] (+-1,+-i), 2 in Z[sqrt-2] (+-1). Nothing else is used.
# This counts INTEGER PAIRS. No formula. No named constant.
def count_pairs(c, X):
    tot = 0; B = math.isqrt(X//c)
    for b in range(-B, B+1):
        rem = X - c*b*b
        if rem < 0: continue
        A = math.isqrt(rem)
        tot += 2*A + 1
    return tot - 1                      # drop (0,0)
print("PURE PAIR COUNT -- the only operation is n1^2 + c*n2^2, and comparison to X.")
print()
for c, units, name in [(1,4,"square world   Z[i]        a^2 + b^2"),
                       (2,2,"               Z[sqrt-2]   a^2 + 2b^2")]:
    print(f"  {name}")
    for Xi in (2_000, 20_000, 200_000, 2_000_000):
        P = count_pairs(c, Xi); A = P//units
        print(f"     pairs<=({Xi:>9,}) = {P:>12,}   ideals = {A:>11,}   A(X)/X = {A/Xi:.8f}")
    print()

# the two REAL worlds have infinite unit groups -- no finite element count exists.
# their ideal counts come from the multiplicative rule, which is a THEOREM, not a count.
LIM = X
sieve = np.ones(LIM+1, dtype=bool); sieve[:2]=False
for i in range(2,1415):
    if sieve[i]: sieve[i*i::i]=False
plist=[int(p) for p in np.flatnonzero(sieve)]
def s_fast(D,p):
    if D % p == 0: return 0
    if p == 2: return 1 if D%8==1 else (-1 if D%8==5 else 0)
    return 1 if pow(D%p,(p-1)//2,p)==1 else -1
print("REAL worlds -- infinite units, so NO finite element count. Rule used is a theorem:")
meas={}
for D,name in [(5,"golden world   Z[(1+sqrt5)/2]"),(8,"               Z[sqrt2]"),
               (-4,"[control] Z[i] by the same rule"),(-8,"[control] Z[sqrt-2] same rule")]:
    schi=np.ones(LIM+1,dtype=np.int64); schi[0]=0
    for p in plist:
        sp=s_fast(D,p)
        if sp==1: continue
        pw=p
        while pw<=LIM: schi[pw::pw]*=sp; pw*=p
    a=np.zeros(LIM+1,dtype=np.int64)
    for d in range(1,LIM+1):
        v=schi[d]
        if v: a[d::d]+=v
    Acum=np.cumsum(a); meas[D]=Acum[LIM]/LIM
    print(f"  D={D:3d}  {name}    A(X)/X = {Acum[LIM]/LIM:.8f}")
print()
print("CONTROL: do the pair-count and the rule agree on the two worlds where both exist?")
for c,units,D in [(1,4,-4),(2,2,-8)]:
    direct = (count_pairs(c,X)//units)/X
    print(f"   c={c}:  pair count {direct:.8f}   vs rule {meas[D]:.8f}   "
          f"{'AGREE' if abs(direct-meas[D])<1e-9 else 'DIFFER by %.2e'%abs(direct-meas[D])}")
print()
print("MEASURED, nothing named:")
for D in (-4,-8,5,8): print(f"     D = {D:3d}    {meas[D]:.8f}")
