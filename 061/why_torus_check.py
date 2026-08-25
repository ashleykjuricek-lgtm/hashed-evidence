"""Audit of the 'Why the Torus' page's three load-bearing claims."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, pi, gamma, exp, sqrt, nstr, mpc, e
mp.dps = 20

print('CLAIM 1: "Q(n) = n1^2/L1^2 + ... -- no transcendentals. No pi."')
print("   The SUMMAND is pi-free. True.")
print("   The SUM is not. The functional equation used in 050 test 5:")
print("      Z(d,j) = pi^(-1-d/2) * Gamma((d+1)/2)/Gamma(-1/2) * SUM' chi(m)|m|^-(d+1)")
for d in [2,3]:
    pref = pi**(-1-mpf(d)/2)*gamma((mpf(d)+1)/2)/gamma(mpf(-1)/2)
    print(f"      d={d}: prefactor = {nstr(pref,12)}   (pi^(-1-d/2) alone = {nstr(pi**(-1-mpf(d)/2),8)})")
print("   Gamma(-1/2) =", nstr(gamma(mpf(-1)/2),12), "= -2 sqrt(pi)")
print("   -> pi is in the VALUE of every Z this programme has ever computed.")
print("      It is also in the Ewald split (pi^(d/2), exp(-pi^2 k^2/t)) and in")
print("      the heat kernel (4 pi t)^(-d/2) on the FLAT torus.")
print()

print('CLAIM 2: "My eigenfunctions are e^(i n x / L) -- winding modes"')
L = mpf(3)
for n in [1,2,3]:
    f0 = exp(mpc(0,1)*n*0/L); fL = exp(mpc(0,1)*n*L/L)
    print(f"   n={n}: e^(i n 0/L) = {nstr(f0,6)}   e^(i n L/L) = {nstr(fL,6)}   equal? {abs(f0-fL) < mpf(10)**-15}")
print("   -> e^(i n x / L) is NOT periodic on a circle of circumference L.")
print("      The correct mode is e^(2 pi i n x / L). The 2 pi is in the exponent")
print("      on a torus exactly as on a sphere. It is not a patching tax.")
print()

print('CLAIM 3: "hbar -> h/L"')
print("   hbar : J s          (action)")
print("   h/L  : J s / m = kg m / s   (momentum)")
print("   -> different units. h/L is the momentum quantum p_n = n h / L on a")
print("      circle, which is correct and standard -- but it does not replace hbar.")
print()

print('CLAIM 4: "the sphere is the torus with the periodicity forgotten"')
print("   Gaussian curvature:  flat T^3 = 0 everywhere;  S^2 of radius a = 1/a^2 > 0.")
print("   Zooming in on a flat torus gives FLAT space, at every scale.")
print("   And from 061 above:  pi_1(T^3) = Z^3 vs pi_1(S^2) = 0;")
print("   heat coefficient a_4 = 0 (flat) vs sqrt(pi)/15 (S^1 x S^2).")
print("   -> neither is a limit of the other, in curvature OR in topology.")
