"""The Bloch sphere and the marked circle.

  Bloch sphere = CP^1 = S^2, pure states of one qubit.   pi_1 = 0  -> NO marking.
  Total space  = S^3 (unit vectors in C^2), Hopf S^3 -> S^2, fibre S^1.  pi_1 = 0.
  SU(2) -> SO(3) is a DOUBLE COVER, and SO(3) = RP^3 = S^3 / Z_2.
  pi_1(SO(3)) = Z_2  ->  EXACTLY TWO markings.

That Z_2 is the spinor sign: rotate a spin-1/2 by 2 pi and it comes back as -1.
It is the same Z_2 as our marked circle. So compute the two spin structures on RP^3.

Laplacian on S^3 (unit radius): eigenvalue n(n+2), degeneracy (n+1)^2.
The antipodal map acts on degree-n harmonics by (-1)^n, so on RP^3:
   untwisted (periodic)      n EVEN
   twisted   (antiperiodic)  n ODD
"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, exp, quad, inf, gamma, nstr, sqrt, pi
mp.dps = 25

NMAX = 400
def ThP(t): return sum((n+1)**2*exp(-t*mpf(n)*(n+2)) for n in range(0, NMAX, 2))
def ThA(t): return sum((n+1)**2*exp(-t*mpf(n)*(n+2)) for n in range(1, NMAX, 2))

print("small-t behaviour: does the DIFFERENCE stay tame while each blows up?")
print("      t        Theta_P        Theta_A       Theta_P - Theta_A")
for tv in ['0.5','0.2','0.1','0.05','0.02','0.01']:
    t = mpf(tv)
    a, b = ThP(t), ThA(t)
    print(f"   {tv:>6}   {nstr(a,10):>14} {nstr(b,10):>14}   {nstr(a-b,10):>14}")
print()
print("   each grows like t^(-3/2); the difference stays O(1).")
print("   -> the poles cancel, exactly as 061 proved for any M x S^1 --")
print("      and here for a quotient rather than a product.")
print()

s = mpf(-1)/2

# Two earlier versions of this section were wrong, both discarded not patched:
#   v1 cut the small-t piece at t=1e-4 and integrated t^(-3/2)*1 numerically
#      instead of continuing it analytically. That contributed ~186 and gave -55.73.
#   v2 continued it correctly but integrated the DIFFERENCE down to t=0, where
#      ThA and ThP are each ~t^(-3/2), truncated at NMAX, and their difference is
#      cancellation garbage. Gave ~1e19 and was lam-DEPENDENT, which is the tell.
# v3: measure the integrand before cutting, as 061 section 3 does.

def dif(t): return t**(s-1)*(ThA(t) - ThP(t))
print("size of the low-t integrand, to justify where it is cut:")
for tv in ['0.20','0.10','0.07','0.05']:
    print(f"      t={tv}   |t^(s-1)(ThA-ThP)| = {nstr(abs(dif(mpf(tv))),4)}")
CUT = mpf('0.05')
print(f"   -> cut at t={CUT}; everything below is under the numerical floor.")
print()

def Zdiff(lam):
    lo = quad(dif, [CUT, lam])
    hi = quad(lambda t: t**(s-1)*(ThA(t) - ThP(t) + 1), [lam, inf])
    return (lo + lam**s/s + hi)/gamma(s)

print("lam-independence -- the acceptance test:")
vals = []
for lv in ['0.7','1.0','1.6','2.5']:
    v = Zdiff(mpf(lv)); vals.append(v)
    print(f"      lam={lv:>4}   {nstr(v, 14)}")
spread = max(vals)-min(vals)
print(f"   spread = {nstr(spread,4)}   {'INVARIANT' if abs(spread) < mpf(10)**-12 else 'STILL WRONG'}")
print()
print("Casimir energy DIFFERENCE between the two spin structures on RP^3 = SO(3):")
print("   Z_twisted - Z_untwisted =", nstr(vals[1], 12))
print()
print("   for comparison:")
print("      T^3  (flat)      Z_APP - Z_PPP = 0.255482035923")
print("      S^1 x S^2        Z_A   - Z_P   = 0.2503281026     (061)")
print()
print("   NOTE: Casimir energy on RP^3 is a standard example in QFT on curved")
print("   space. This number is very probably in the literature. Not searched.")
