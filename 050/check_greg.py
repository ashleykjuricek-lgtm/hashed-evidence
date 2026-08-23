"""Verification of Greg's halving-law argument. Four independent tests."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, jtheta, sqrt, pi, nstr, linspace, exp
mp.dps = 30

print("="*72)
print("TEST 1 -- the duplication identity  theta3(q) theta4(q) = theta4(q^2)^2")
print("="*72)
bad = 0
for qv in ['0.01','0.1','0.3','0.5','0.7','0.9','0.97']:
    q = mpf(qv)
    lhs = jtheta(3,0,q)*jtheta(4,0,q)
    rhs = jtheta(4,0,q*q)**2
    d = abs(lhs-rhs); bad += (d > mpf(10)**-25)
    print(f"   q={qv:>6}   lhs={nstr(lhs,18):>22}   rhs={nstr(rhs,18):>22}   diff={nstr(d,3)}")
print(f"   -> identity holds: {bad==0}")

print()
print("="*72)
print("TEST 2 -- the MECHANISM.  Is  theta4^j theta3^(d-j) < 1  exactly when 2j >= d?")
print("   (if it were < 1 for some 2j < d too, the argument would prove")
print("    positivity where we measure negativity -- i.e. it would be broken)")
print("="*72)
qs = [mpf(x)/1000 for x in range(1, 1000, 3)]
print("   d  j   2j>=d   max over q of theta4^j*theta3^(d-j)      verdict")
fails = []
for d in range(1, 9):
    for j in range(0, d+1):
        vals = [jtheta(4,0,q)**j * jtheta(3,0,q)**(d-j) for q in qs]
        M = max(vals)
        pred = (2*j >= d)
        under1 = M < 1
        ok = (under1 == pred)
        if not ok: fails.append((d,j))
        print(f"   {d:2d} {j:2d}    {str(pred):>5}   max = {nstr(M,12):>16}   "
              f"{'<1' if under1 else '>1'}   {'OK' if ok else '*** MISMATCH ***'}")
    print()
print(f"   -> mechanism matches the sign law in every cell: {len(fails)==0}   {fails}")
