# Check of the 120 derivation: Z(-1/2) = -Ztilde(2)/(2 pi^3) in both sectors.
# Z at s=-1/2 by Ewald / incomplete gamma (the only finite route). Ztilde(2) by direct sum
# (absolutely convergent) with an integral tail estimate - independent of the Ewald code.
import sys; sys.path.insert(0, "/tmp/pylib")
from mpmath import mp, mpf, gammainc, pi, exp, cos
mp.dps = 30
N = 6
def ewald(s, a):
    # pi^-s Gamma(s) Z_a(s), Z_a = sum |n+a|^-2s (n=0 dropped if a=0); dual phase e^{2 pi i k.a}
    tot = mpf(0)
    rng = range(-N, N+1)
    for i in rng:
        for j in rng:
            for k in rng:
                x = (i+a[0])**2 + (j+a[1])**2 + (k+a[2])**2
                if x: tot += gammainc(s, pi*x) * (pi*x)**(-s)
                y = i*i + j*j + k*k
                if y:
                    ph = cos(2*pi*(i*a[0]+j*a[1]+k*a[2]))
                    tot += ph * gammainc(mpf(3)/2 - s, pi*y) * (pi*y)**(s - mpf(3)/2)
    tot += 1/(s - mpf(3)/2)
    if a == (0,0,0): tot -= 1/s
    return tot / (pi**(-s) * mp.gamma(s))
def direct(sign, M=60):
    t = mpf(0)
    for i in range(-M, M+1):
        for j in range(-M, M+1):
            for k in range(-M, M+1):
                r = i*i+j*j+k*k
                if r and r <= M*M:
                    t += ((-1)**i if sign else 1) / mpf(r)**2
    return t + (0 if sign else 4*pi/M)   # unsigned tail ~ 4 pi / M; signed tail cancels
s = mpf(-1)/2
for name, a, sign in [("PPP", (0,0,0), False), ("APP", (mpf(1)/2,0,0), True)]:
    zm = ewald(s, a); z2e = ewald(mpf(2), (0,0,0)) if not sign else None
    z2 = direct(sign)
    print(name, "Z(-1/2) Ewald        =", zm)
    print(name, "-Ztilde(2)/(2pi^3)   =", -z2/(2*pi**3), " (direct sum, ~4 digits)")
    print(name, "ratio                =", zm / (-z2/(2*pi**3)))
zA = ewald(s,(mpf(1)/2,0,0)); zP = ewald(s,(0,0,0))
print("R (Ewald, s=-1/2) =", zA/zP)
