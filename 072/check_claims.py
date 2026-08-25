"""Verify the reviewing seat's three claims."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math

def sieve(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]

print("="*70)
print("CLAIM 1 -- 070's sentence 'each blind exactly where the other sees'")
print("="*70)
P = sieve(3000)
f4 = lambda p: p==2 or p%4==1
f5 = lambda p: p==5 or p%5 in (1,4)
b = sum(1 for p in P if f4(p) and f5(p));  o4 = sum(1 for p in P if f4(p) and not f5(p))
o5 = sum(1 for p in P if f5(p) and not f4(p)); nn = sum(1 for p in P if not f4(p) and not f5(p))
T = len(P)
print(f"   both {b}   four-only {o4}   five-only {o5}   neither {nn}   total {T}")
print(f"   the lenses AGREE (both lit or both dark) on {b+nn}/{T} = {100*(b+nn)/T:.1f}%")
print(f"   they DISAGREE on {o4+o5}/{T} = {100*(o4+o5)/T:.1f}%")
print()
print("   'blind exactly where the other sees' predicts both=0 and neither=0.")
print(f"   observed both={b}, neither={nn}.  -> the sentence is REFUTED by its own bins.")
print()
print("   independence test: if independent, each bin ~ 1/4 of total")
for nm,v in [("both",b),("four-only",o4),("five-only",o5),("neither",nn)]:
    print(f"      {nm:10} {100*v/T:5.1f}%   (independent prediction 25.0%)")
print("   mod 4 and mod 5 are coprime -> CRT: the classes mod 20 equidistribute.")
print("   Each lens reads the other as a FAIR COIN. INDEPENDENT, not complementary.")

print()
print("="*70)
print("CLAIM 2 -- the ten-cycle mod 11, and 11 minimal")
print("="*70)
c=[1]; x=1
for _ in range(10):
    x = (x*2) % 11; c.append(x)
print("   powers of 2 mod 11:", " -> ".join(map(str,c)))
print(f"   distinct nonzero residues visited: {len(set(c[:-1]))} of 10   closes: {c[-1]==1}")
print()
print("   smallest prime p with 10 | p-1  (i.e. p = 1 mod 10):")
print("     ", [int(p) for p in sieve(200) if p % 10 == 1][:6], "-> 11 is first")
print("   (2,3,5,7 all fail: p-1 = 1,2,4,6, none divisible by 10)")

print()
print("="*70)
print("CLAIM 3 -- the golden-world average is 2 log(phi)/sqrt5, no pi")
print("="*70)
X = 1_000_000
# ideals of norm m in Z[phi]: multiplicative; p splits iff p = +-1 mod 5, ramified at 5, else inert
a = np.zeros(X+1, dtype=np.int64); a[1] = 1
for p in sieve(X):
    p = int(p)
    if p == 5:      loc = lambda k: 1
    elif p % 5 in (1,4): loc = lambda k: k+1
    else:           loc = lambda k: 1 if k % 2 == 0 else 0
    pk, k = p, 1
    while pk <= X:
        # multiply in the local factor
        idx = np.arange(pk, X+1, pk)
        pk *= p; k += 1
    # simpler: build multiplicatively below
# rebuild by direct multiplicative sieve
a = np.zeros(X+1, dtype=np.int64); a[1] = 1
for p in sieve(X):
    p = int(p)
    if p == 5: locs = [1]*(int(math.log(X,p))+2)
    elif p % 5 in (1,4): locs = [k+1 for k in range(int(math.log(X,p))+2)]
    else: locs = [1 if k%2==0 else 0 for k in range(int(math.log(X,p))+2)]
    new = a.copy()
    pk = p; k = 1
    while pk <= X:
        idx = np.arange(pk, X+1, pk)
        base = idx // pk
        ok = (base % p != 0)
        new[idx[ok]] = a[base[ok]] * locs[k]
        pk *= p; k += 1
    a = new
phi = (1+math.sqrt(5))/2
for Xc in [10_000, 100_000, 1_000_000]:
    m = a[1:Xc+1].sum()/Xc
    print(f"   mean ideal count, m <= {Xc:>9} : {m:.8f}")
print(f"   exact limit 2 log(phi)/sqrt5           : {2*math.log(phi)/math.sqrt(5):.8f}")
print()
print(f"   for contrast, square world limit pi/4  : {math.pi/4:.8f}")
print("   Dirichlet class number formula, one slot, two occupants:")
print("      imaginary disc (-4):  2 pi h / (w sqrt|d|) = 2 pi / (4 * 2) = pi/4")
print("      real disc     (+5):  4 h R / (w sqrt d)   = 4 log(phi) / (2 sqrt5) = 2 log(phi)/sqrt5")
