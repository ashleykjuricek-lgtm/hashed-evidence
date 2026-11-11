# 120 check battery: each claim checked by a route independent of the one that produced it.
import sys; sys.path.insert(0, "/workspaces/default/.pylib")
from mpmath import mp, mpf, gammainc, pi, cos, gamma, zeta, exp, log, diff
mp.dps = 25
N = 6
def G(s, x): return gammainc(s, x) * x**(-s)
def Lam(s, L, a):
    """pi^-s Gamma(s) Z(s), Z = sum' |((n_i+a_i)/L_i)|^-2s, box sides L, twist a."""
    V = L[0]*L[1]*L[2]; t = mpf(0); r = range(-N, N+1)
    for i in r:
        for j in r:
            for k in r:
                q = ((i+a[0])/L[0])**2 + ((j+a[1])/L[1])**2 + ((k+a[2])/L[2])**2
                if q: t += G(s, pi*q)
                p = (i*L[0])**2 + (j*L[1])**2 + (k*L[2])**2
                if p: t += V*cos(2*pi*(i*a[0]+j*a[1]+k*a[2])) * G(mpf(3)/2-s, pi*p)
    t += V/(s-mpf(3)/2)
    if a == (0,0,0): t -= 1/s
    return t
def Z(s, L, a): return Lam(s, L, a) / (pi**(-s)*gamma(s))
h = mpf(1)/2
A0, AP = (h,0,0), (0,0,0)
cube = (1,1,1)
out = []
def say(*x): print(*x); sys.stdout.flush()

say("== C1  R at the cube, Ewald (this code) vs c2-highprec.py")
R = Z(-h,cube,A0)/Z(-h,cube,AP); say("  R =", R, " sealed 0.04168941460272377512")

say("== C2  mirror identity Lam_shift(s) = Lam_char(3/2-s) at several s (char = phase on dual)")
def Lam_char(s):
    # character sum: sum' (-1)^k1 |k|^-2s, as Lam with a=0 on direct side but phase (-1)^n1 there
    t = mpf(0); r = range(-N, N+1)
    for i in r:
        for j in r:
            for k in r:
                q = i*i+j*j+k*k
                if q: t += (-1)**i * G(s, pi*q)
                p = (i+h)**2 + j*j + k*k
                t += G(mpf(3)/2-s, pi*p)
    return t - 1/s
for s in [mpf(-3)/2, -h, mpf(1)/4, mpf(2)/3]:
    say(f"  s={float(s):+.3f}  shift={Lam(s,cube,A0)}  char(3/2-s)={Lam_char(mpf(3)/2-s)}")
say("  PPP self-mirror at s=-1/2:", Lam(-h,cube,AP), Lam(mpf(2),cube,AP))

say("== C3  slope sign & size: finite differences of Ewald R on two families")
def eps(x, twist_on_short):
    b = exp(x)
    L = (1, b, b) if twist_on_short else (b, b, 1)   # twist always on axis 1
    return 24*Z(-h,L,A0)/Z(-h,L,AP) - 1
for fam, lab in [(True, "(1,b,b), twist on the '1' axis"), (False, "(b,b,1), twist on a 'b' axis")]:
    d = mpf("1e-4")
    e0, ep, em = eps(0,fam), eps(d,fam), eps(-d,fam)
    s1 = (ep-em)/(2*d); s2 = (ep-2*e0+em)/d**2
    say(f"  {lab}: eps0={e0}  slope={s1}  half 2nd deriv(x)={s2/2}")
say("  sealed: slope -18.3259647, A 0.58260865319")
say("  (my mirror-sum formula gave +18.3260; 'twist on short side' family should match whichever sign)")

say("== C4  zeta(-1/2), beta(-1/2): mpmath built-ins vs 119 enclosure")
say("  zeta(-1/2) =", zeta(-h), "  119: -0.20788622497735456601730672539")
beta = lambda s: 4**(-s)*(zeta(s,mpf(1)/4)-zeta(s,mpf(3)/4))
say("  beta(-1/2) =", beta(-h), "  119:  0.27517974122882025011666516766")
say("  reflection beta(-1/2)=beta(3/2)/pi:", beta(mpf(3)/2)/pi)

say("== C5  1-D pair: Hurwitz zeta(-1,1/2) and zeta(-1)")
say("  ", zeta(-1, h) - 0, "(Hurwitz at a=1/2; antiperiodic sum = zeta(-1,1/2)·2^? check sign)", zeta(-1))
