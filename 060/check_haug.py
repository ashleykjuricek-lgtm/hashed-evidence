"""Audit of the Haug (2025) extremal-RN Carnot claim, as presented on the page."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, sqrt, pi, nstr
mp.dps = 25

hbar = mpf('1.054571817e-34')
c    = mpf('299792458')
kB   = mpf('1.380649e-23')
lp   = mpf('1.616255e-35')
mp_pl= mpf('2.176434e-8')
Mpc  = mpf('3.0856775814913673e22')

def R_H(H0_kms_Mpc):   # H0 in km/s/Mpc  ->  Hubble radius in m
    H0 = mpf(H0_kms_Mpc)*1000/Mpc
    return c/H0
def H0_from_RH(R):
    return (c/R)*Mpc/1000

T_max = hbar*c/(8*pi*lp*kB)                 # Hawking T of a Planck-mass BH (r_s = 2 l_p)
print("T_max = hbar c / (8 pi l_p k_B) =", nstr(T_max, 8), "K")
print("   page says '~10^32 K (Planck temperature scale)'")
T_planck = mp_pl*c**2/kB
print("   actual Planck temperature   =", nstr(T_planck, 8), "K")
print("   ratio T_planck / T_max      =", nstr(T_planck/T_max, 8), " = 8*pi =", nstr(8*pi,8))
print("   -> T_max is 10^30.75, NOT 10^32.  The page's exponent is off by 8*pi ~ 25.")
print()

for H0 in ['66.8712', '67.4', '73.0']:
    R = R_H(H0)
    T_min = hbar*c/(4*pi*R*kB)
    T_cmb = sqrt(T_max*T_min)
    print(f"H0 = {H0:>8} km/s/Mpc   R_H = {nstr(R,6)} m")
    print(f"     T_min = {nstr(T_min,6)} K      T_CMB = sqrt(T_max T_min) = {nstr(T_cmb,8)} K")
print()
print("measured T_CMB (Fixsen 2009) = 2.72548 +/- 0.00057 K")
print()

# invert: H0 from T_CMB
T_obs = mpf('2.72548'); T_err = mpf('0.00057')
H0_pred = (T_obs**2/T_max)*kB*4*pi/hbar*Mpc/1000
H0_err  = 2*(T_err/T_obs)*H0_pred
print("INVERSION  H0 = (T_CMB^2 / T_max) * k_B * 4 pi / hbar")
print("   H0 =", nstr(H0_pred, 10), "+/-", nstr(H0_err, 3), "km/s/Mpc")
print("   page claims 66.8712 +/- 0.0019")
print()
print("   NOTE: the error bar is PROPAGATED from T_CMB, not measured.")
print("         dH0/H0 = 2 dT/T =", nstr(200*T_err/T_obs, 4), "%")
print()
print("TENSION CHECK")
for name, val, err in [("Planck 2018", mpf('67.4'), mpf('0.5')),
                       ("SH0ES local", mpf('73.0'), mpf('1.0'))]:
    d = abs(H0_pred - val); s = d/sqrt(err**2 + H0_err**2)
    print(f"   vs {name:12} {nstr(val,4)} +/- {nstr(err,2)}:  diff {nstr(d,3)}  = {nstr(s,3)} sigma")
print()
print("REVERSE: what T_CMB does the relation require, given Planck's H0?")
T_req = sqrt(T_max*hbar*c/(4*pi*R_H('67.4')*kB))
print("   T_CMB required =", nstr(T_req, 8), "K   vs measured", nstr(T_obs,8))
print("   discrepancy    =", nstr(100*(T_req-T_obs)/T_obs, 4), "%  =",
      nstr((T_req-T_obs)/T_err, 4), "sigma of the T_CMB measurement")
print()
print("LISA geometric-mean prediction (the page's own addition, not Haug's):")
print("   sqrt(66.8712 * 73.0) =", nstr(sqrt(mpf('66.8712')*73), 6), "km/s/Mpc")
