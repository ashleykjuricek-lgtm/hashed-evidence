"""Is it ONE curve?

Hold one function -- R(d,b) - 1/24 -- and vary two things:
    d' : R(d, b=1) = 1/24        never computed before
    b' : R(3, b)   = 1/24        = 1.0000297915619869892  (047)
Then trace the level set R(d,b) = 1/24 between them."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import merged
from mpmath import mp, mpf, findroot, nstr
mp.dps = 20
TARGET = mpf(1)/24

print("R(d, b=1) near d = 3:")
for dd in ['2.90','2.95','2.98','2.99','3.00','3.01']:
    print(f"   d={dd}   R = {nstr(merged.R(mpf(dd), 1), 14):>18}   R-1/24 = {nstr(merged.R(mpf(dd),1)-TARGET, 8):>14}")
    sys.stdout.flush()

print()
dprime = findroot(lambda d: merged.R(d, 1) - TARGET, (mpf('2.9'), mpf('3.0')), solver='secant', tol=mpf(10)**-18)
print("   d' with R(d',1) = 1/24 :", nstr(dprime, 18))
print("   3 - d'                 :", nstr(3-dprime, 10))
print()
bprime = mpf('1.0000297915619869892')
print("   b' with R(3,b') = 1/24 :", nstr(bprime, 18), "   (047)")
print("   b' - 1                 :", nstr(bprime-1, 10))
print()
print("="*68)
print("TRACE the level set  R(d,b) = 1/24  from (d',1) to (3,b')")
print("="*68)
print("      d            b*(d) with R=1/24        b*-1")
for dd in [dprime, mpf('2.97'), mpf('2.98'), mpf('2.99'), mpf('2.995'), mpf('3.0')]:
    try:
        bb = findroot(lambda b: merged.R(dd, b) - TARGET, (mpf('0.999'), mpf('1.002')),
                      solver='secant', tol=mpf(10)**-18)
        print(f"   {nstr(dd,10):>12}   {nstr(bb,16):>20}   {nstr(bb-1,8):>12}")
    except Exception as e:
        print(f"   {nstr(dd,10):>12}   no root in [0.999,1.002]  ({type(e).__name__})")
    sys.stdout.flush()
