"""Re-examine 060 section 4. Did the 18 sigma drop an error bar?"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, sqrt, nstr
mp.dps = 20

# the relation is  T^2 = k H0  for a fixed k. Work entirely in ratios.
T_m, T_e   = mpf('2.72548'), mpf('0.00057')      # Fixsen 2009
H_P, H_Pe  = mpf('67.4'),    mpf('0.5')          # Planck 2018
H_S, H_Se  = mpf('73.0'),    mpf('1.0')          # SH0ES
H_pred     = mpf('66.894')                       # from 060, T -> H0
H_prede    = 2*(T_e/T_m)*H_pred                  # dH/H = 2 dT/T

print("TEST EXPRESSED IN H0 UNITS  (what 060 called 'forward')")
print(f"   from T_CMB:  H0 = {nstr(H_pred,8)} +/- {nstr(H_prede,3)}")
for nm, v, e in [("Planck", H_P, H_Pe), ("SH0ES", H_S, H_Se)]:
    d = abs(H_pred-v); s = d/sqrt(e**2 + H_prede**2)
    print(f"   vs {nm:7} {nstr(v,4)} +/- {nstr(e,2)}:  diff {nstr(d,3):>7}  comb.err {nstr(sqrt(e**2+H_prede**2),3):>7}  {nstr(s,3)} sigma")

print()
print("TEST EXPRESSED IN T UNITS  (what 060 called 'reverse')")
T_req  = T_m*sqrt(H_P/H_pred)                    # T implied by Planck's H0
T_reqe = (mpf(1)/2)*(H_Pe/H_P)*T_req             # dT/T = (1/2) dH/H   <-- 060 OMITTED THIS
print(f"   from Planck H0:  T_CMB = {nstr(T_req,8)} +/- {nstr(T_reqe,3)}")
print(f"   measured         T_CMB = {nstr(T_m,8)} +/- {nstr(T_e,3)}")
d = abs(T_req-T_m)
print()
print("   060 computed:  diff / (measured error only)")
print(f"      {nstr(d,6)} / {nstr(T_e,3)} = {nstr(d/T_e,4)} sigma      <-- the '18 sigma'")
print()
print("   correct:       diff / sqrt(both errors)")
comb = sqrt(T_reqe**2 + T_e**2)
print(f"      {nstr(d,6)} / {nstr(comb,3)} = {nstr(d/comb,4)} sigma")
print()
print("VERDICT")
print(f"   H0-units test: {nstr(abs(H_pred-H_P)/sqrt(H_Pe**2+H_prede**2),4)} sigma")
print(f"   T-units test : {nstr(d/comb,4)} sigma")
print("   -> the SAME test. One constraint between two measured quantities.")
print("      Expressing it in different units cannot change its significance.")
print("      060's 'asymmetry' came from dropping the PREDICTED value's error bar")
print("      in one direction and keeping it in the other.")
