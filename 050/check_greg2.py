"""Tests 3 and 4 of Greg's argument."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import fractional
from mpmath import mp, mpf, nstr, quad, exp, inf, gamma, pi
mp.dps = 20

print("="*72)
print("TEST 3 -- strict monotonicity in j:  Z(d,j+1) > Z(d,j)")
print("   Greg proves it for j >= 1 via  theta3 > theta2 > 0.  Check integer")
print("   cells AND fractional j (which only the real-j continuation can see).")
print("="*72)
bad = []
for d in range(1, 11):
    vals = [fractional.Z(d, j, N=16, K=6) for j in range(0, d+1)]
    inc = all(vals[i+1] > vals[i] for i in range(len(vals)-1))
    inc1 = all(vals[i+1] > vals[i] for i in range(1, len(vals)-1))   # j>=1 only
    if not inc: bad.append(d)
    print(f"   d={d:2d}  strictly increasing over all j: {str(inc):>5}   (over j>=1: {inc1})")
print(f"   -> monotone in every row: {len(bad)==0}   {bad}")

print()
print("   fractional j, d = 7:")
prev = None
for jj in ['0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']:
    v = fractional.Z(7, mpf(jj), N=16, K=6)
    flag = "" if prev is None else ("UP" if v > prev else "*** DOWN ***")
    print(f"      j={jj:>4}   Z = {nstr(v,14):>18}   {flag}")
    prev = v

print()
print("="*72)
print("TEST 4 -- the remaining lemma:  Z(d, (d-1)/2) < 0 ?")
print("   If true, monotonicity closes the whole law.")
print("="*72)
allneg = True
for d in range(2, 15):
    j = (mpf(d)-1)/2
    v = fractional.Z(d, j, N=16, K=6)
    neg = v < 0
    allneg &= neg
    print(f"   d={d:2d}   j=(d-1)/2={nstr(j,6):>6}   Z = {nstr(v,12):>16}   {'NEGATIVE ok' if neg else '*** POSITIVE -- LEMMA FALSE ***'}")
print(f"   -> lemma holds on every d tested: {allneg}")
