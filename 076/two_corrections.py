"""Two of Greg's corrections land on sealed entries here. Test both."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, mpc, gamma, pi, exp, log, nstr, sqrt
mp.dps = 30

print("="*74)
print("CORRECTION 1 -- 069 sec.5 says 1/Gamma((d+1)/2) 'decays vertically'.")
print("Greg: it GROWS like e^{pi|Im d|/4}. Stirling.")
print("="*74)
print()
print("   |1/Gamma((d+1)/2)| along d = 3 + iy :")
print("      y        |1/Gamma((d+1)/2)|      e^{pi y/4}         ratio")
for yv in [0, 5, 10, 20, 40, 80]:
    y = mpf(yv)
    d = mpc(3, y)
    val = abs(1/gamma((d+1)/2))
    pred = exp(pi*y/4)
    print(f"   {yv:>5}   {nstr(val,10):>20}   {nstr(pred,10):>14}   {nstr(val/pred,8):>12}")
print()
print("   -> |1/Gamma| GROWS. 069's 'decays vertically' is WRONG. Greg is right.")
print()
print("   the growth EXPONENT, extracted:")
for yv in [40, 80, 160]:
    y = mpf(yv)
    r = log(abs(1/gamma((mpc(3,y)+1)/2)))/y
    print(f"      y={yv:>4}   log|1/Gamma| / y = {nstr(r,10)}     pi/4 = {nstr(pi/4,10)}")
print()
print("   Carlson permits type c < pi on vertical lines.  pi/4 = 0.785 < pi = 3.14.")
print("   -> the STATED proof fails; the CONCLUSION may survive with room to spare.")

print()
print("="*74)
print("CORRECTION 2 -- 074's witness: does discharging it pin the claim?")
print("Greg's counterexample, applied to OUR OWN build.")
print("="*74)
print()
print("   074's witness has a finite input signature:")
print("      family in {1bb, volpres} x chart in {direct, momentum} x marked in {short, stretched}")
print("      = 8 cells, of which 3 are pinned.")
print()
print("   Construct a DIFFERENT function agreeing on all 3 pinned cells:")

PINNED = {("1bb","direct","short"):      mpf("18.3259647484177"),
          ("1bb","momentum","short"):    mpf("-18.3259647484177"),
          ("volpres","momentum","stretched"): mpf("27.4889471226266")}

def impostor(family, chart, marked):
    """agrees with the real witness on every pinned cell, differs elsewhere"""
    k = (family, chart, marked)
    if k in PINNED: return PINNED[k]
    return mpf(0)          # the real witness gives -13.744... at volpres|momentum|short

print()
for k, v in PINNED.items():
    print(f"      {str(k):42} impostor {nstr(impostor(*k),12):>18}  MATCHES")
k = ("volpres","momentum","short")
print(f"      {str(k):42} impostor {nstr(impostor(*k),12):>18}  real: -13.7444735613")
print()
print("   The impostor DISCHARGES the witness on every pinned cell and is a")
print("   different function. Greg's f(x)=x^2 vs g(x)=x^2+(x-3), in our own build.")
print()
print("   -> 'same witness => same claim' is FALSE.")
print("      'different witness => different claim' remains TRUE and useful.")
print()
print("   The witness is a DISCRIMINATOR, not a definition of identity.")
