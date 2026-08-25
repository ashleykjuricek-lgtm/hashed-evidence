"""Can the programme's object live on a sphere?

The whole programme computes R = Z_marked / Z_unmarked at s = -1/2.
Marking = a flat Z2 bundle = a homomorphism pi_1 -> Z2. So the question is
really about pi_1 and about the heat-kernel expansion.

Test the nearest sphere-with-a-circle: S^1 x S^2."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
from mpmath import mp, mpf, exp, sqrt, pi, quad, inf, gamma, nstr
mp.dps = 25

def S2(t, L=400):
    """heat trace on the unit 2-sphere: sum (2l+1) exp(-t l(l+1))"""
    return sum((2*l+1)*exp(-t*l*(l+1)) for l in range(L))

print("=== 1. the S^2 heat trace and its small-t expansion ===")
print("   claim:  S2(t) ~ 1/t + 1/3 + t/15 + 4t^2/315 + ...")
for tv in ['0.2','0.1','0.05','0.02','0.01']:
    t = mpf(tv)
    approx = 1/t + mpf(1)/3 + t/15 + 4*t**2/315
    print(f"   t={tv:>6}  S2 = {nstr(S2(t),12):>16}   series = {nstr(approx,12):>16}"
          f"   diff = {nstr(S2(t)-approx,3)}")

print()
print("=== 2. where the pole is ===")
print("   Theta(t) = theta_alpha(t) * S2(t)  ~  sqrt(pi/t) * [1/t + 1/3 + t/15 + ...]")
print("            =  sqrt(pi) [ t^-3/2 + (1/3) t^-1/2 + (1/15) t^+1/2 + ... ]")
print()
print("   Mellin:  INT_0^lam t^(s-1) t^((k-3)/2) dt  has a pole at s = -(k-3)/2")
print("     k=0  ->  pole at s = +3/2")
print("     k=2  ->  pole at s = +1/2")
print("     k=4  ->  pole at s = -1/2      <-- EXACTLY where we work")
print()
print("   coefficient of t^+1/2 is sqrt(pi)/15 =", nstr(sqrt(pi)/15, 10), "!= 0")
print("   -> zeta(s) HAS A POLE at s = -1/2 on S^1 x S^2.")
print("   On a FLAT torus the expansion terminates at k=0 (no curvature terms),")
print("   so there is no pole and Z(-1/2) is finite and unambiguous.")

print()
print("=== 3. but the DIFFERENCE is always finite ===")
print("   theta_P(t) - theta_A(t) = sqrt(pi/t) * 4 * sum_{k>=1 odd} exp(-pi^2 k^2 / t)")
for tv in ['0.5','0.2','0.1','0.05']:
    t = mpf(tv)
    thP = sum(exp(-t*mpf(n)**2) for n in range(-60,61))
    thA = sum(exp(-t*(mpf(n)+mpf(1)/2)**2) for n in range(-60,61))
    pred = sqrt(pi/t)*4*sum(exp(-pi**2*k*k/t) for k in range(1,8,2))
    print(f"   t={tv:>6}  thP-thA = {nstr(thP-thA,10):>14}   predicted {nstr(pred,10):>14}")
print()
print("   exponentially small as t->0, for ANY manifold factor.")
print("   So Theta_P - Theta_A is exponentially small, the poles CANCEL,")
print("   and Z_A - Z_P is finite even when each term diverges.")

print()
print("=== 4. what survives: the DIFFERENCE, computed on S^1 x S^2 ===")
print("   (v1 of this section was WRONG: it truncated the theta sums at n=+/-40.")
print("    A truncated theta does NOT have the exponential-smallness property --")
print("    that is asymptotic to the FULL sum. The truncated difference read 2e-5")
print("    instead of exp(-pi^2/t), and t^-3/2 at t=1e-6 multiplied it by 1e9.")
print("    Verdict discarded, not patched. Redone with the exact dual form.)")
print()
s = mpf(-1)/2; lam = mpf(1)

def dth_diff(t):
    """theta_A(t) - theta_P(t), EXACT via Poisson:  -4 sqrt(pi/t) sum_{k odd} exp(-pi^2 k^2/t)"""
    return -4*sqrt(pi/t)*sum(exp(-pi**2*k*k/t) for k in range(1,12,2))

def thP(t, N=80): return sum(exp(-t*mpf(n)**2)            for n in range(-N,N+1))
def thA(t, N=80): return sum(exp(-t*(mpf(n)+mpf(1)/2)**2) for n in range(-N,N+1))
def S2n(t):
    L = max(60, int(8/sqrt(t))+10)
    return sum((2*l+1)*exp(-t*l*(l+1)) for l in range(L))

# below t=0.25 the difference is < 1e-17 even after the t^-5/2 prefactor: verified, then dropped
print("   size of the low-t integrand, to justify cutting it:")
for tv in ['0.30','0.25','0.20']:
    t = mpf(tv)
    val = abs(t**(s-1)*dth_diff(t)*S2n(t))
    print(f"      t={tv}   |t^(s-1) (thA-thP) S2| = {nstr(val,4)}")

lo = quad(lambda t: t**(s-1)*dth_diff(t)*S2n(t), [mpf('0.25'), lam])
hi = quad(lambda t: t**(s-1)*(thA(t)*S2n(t) - (thP(t)*S2n(t) - 1)), [lam, inf])
D  = (lo + lam**s/s + hi)/gamma(s)
print()
print("   low piece  =", nstr(lo, 10))
print("   lam^s / s  =", nstr(lam**s/s, 10))
print("   high piece =", nstr(hi, 10))
print("   Z_A - Z_P on S^1 x S^2 (unit radii) =", nstr(D, 10))
print()
print("   finite, as the argument requires -- while Z_A and Z_P each diverge.")
print("   flat comparison, T^3:  Z_APP - Z_PPP =",
      nstr(mpf('-0.0111142427950344') - mpf('-0.266596278718393'), 12))
