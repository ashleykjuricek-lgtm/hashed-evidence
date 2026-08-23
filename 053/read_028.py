"""Checking the 028 paper against what we now hold."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import anisotropic
from mpmath import mp, mpf, sqrt, exp, pi, diff, findroot, nstr
mp.dps = 25
A, P = mpf(1)/2, mpf(0)
Z = anisotropic.Z

print("="*70)
print("1. the coset/tiling identity of 028 section 6")
print("   Z_PPP + 6 Z_APP + 6 Z_AAP + 2 Z_AAA = 0")
print("="*70)
zp  = Z([1,1,1],[P,P,P]); za1 = Z([1,1,1],[A,P,P])
za2 = Z([1,1,1],[A,A,P]); za3 = Z([1,1,1],[A,A,A])
tot = zp + 6*za1 + 6*za2 + 2*za3
print(f"   Z_PPP {nstr(zp,15)}   Z_APP {nstr(za1,15)}")
print(f"   Z_AAP {nstr(za2,15)}   Z_AAA {nstr(za3,15)}")
print(f"   total = {nstr(tot,6)}   -> holds: {abs(tot) < mpf(10)**-18}")

print()
print("="*70)
print("2. section 6's 2D closed forms -- 028 already had BOTH, in June")
print("="*70)
z2pp = Z([1,1],[P,P]); z2ap = Z([1,1],[A,P]); z2aa = Z([1,1],[A,A])
print(f"   Z2_AA/Z2_PP = {nstr(z2aa/z2pp,20)}    028 says 1/sqrt2 - 1 = {nstr(1/sqrt(2)-1,20)}")
print(f"   Z2_AP/Z2_PP = {nstr(z2ap/z2pp,20)}    028 says -(sqrt2-1)/4 = {nstr(-(sqrt(2)-1)/4,20)}")

print()
print("="*70)
print("3. the b-parameterisation. 028 App A.3 writes Q = (n1+a1)^2 + b^2(...),")
print("   i.e. the SHORT axes carry b^2. Our 047 used sides (1,b,b), which puts")
print("   1/b^2 there. So 028's b should be our 1/b.")
print("="*70)
def eps_ours(b): 
    b = mpf(b); return 24*Z([1,b,b],[A,P,P])/Z([1,b,b],[P,P,P]) - 1
def eps_028(b):
    b = mpf(b); return eps_ours(1/b)
print("   028's table, recomputed in ITS convention:")
for bb in ['0.92','1.00','1.08']:
    e = eps_028(bb)
    print(f"      b={bb}   eps = {nstr(e,10):>16}   eps/q = {nstr(e/exp(-2*pi),8):>12}    "
          f"(028 says {'-1.5235 / -815.8' if bb=='0.92' else '+0.00054595 / +0.2924' if bb=='1.00' else '+1.4142 / +757.3'})")
s028 = diff(eps_028, mpf(1))
print(f"   d eps/db in 028's convention at b=1 : {nstr(s028,12)}     (028 says ~ +18.3)")
b0 = findroot(eps_028, (mpf('0.99990'), mpf('0.99999')), solver='secant', tol=mpf(10)**-20)
print(f"   zero in 028's convention            : b0 = {nstr(b0,18)}   (028 says ~0.99997)")
print(f"   reciprocal of our b* 1.0000297915619869892 = {nstr(1/mpf('1.0000297915619869892'),18)}")

print()
print("="*70)
print("4. section 7.1 writes  '1 - 1/sqrt2 = eps(cube)/e^(-2pi)'")
print("="*70)
q = exp(-2*pi); e1 = eps_ours(1)
print(f"   eps(cube)/q   = {nstr(e1/q,18)}")
print(f"   1 - 1/sqrt2   = {nstr(1-1/sqrt(2),18)}")
print(f"   difference    = {nstr(e1/q - (1-1/sqrt(2)),6)}   ({nstr(100*abs(e1/q/(1-1/sqrt(2))-1),4)}% )")
print(f"   (1-1/sqrt2)(1-q) = {nstr((1-1/sqrt(2))*(1-q),18)}   <- what eps1/q actually is")
