# 121 test of story (b): R on the (1,b,b) box, twist on the length-1 axis, at extreme b.
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".pylib"))
from mpmath import mp, mpf, gammainc, pi, cos, gamma, nstr
mp.dps = 15; N = 10
G = lambda s, x: gammainc(s, x)*x**(-s)
def Z(s, L, a):
    V = L[0]*L[1]*L[2]; t = mpf(0); r = range(-N, N+1)
    for i in r:
        for j in r:
            for k in r:
                q = ((i+a)/L[0])**2 + (j/L[1])**2 + (k/L[2])**2
                if q: t += G(s, pi*q)
                p = (i*L[0])**2 + (j*L[1])**2 + (k*L[2])**2
                if p: t += V*cos(2*pi*i*a)*G(mpf(3)/2-s, pi*p)
    t += V/(s-mpf(3)/2)
    if a == 0: t -= 1/s
    return t/(pi**(-s)*gamma(s))
s = -mpf(1)/2
for b in ["0.25", "0.5", "1", "2", "3"]:
    b = mpf(b); L = (1, b, b)
    print(f"b={nstr(b,3):>5}  R={nstr(Z(s,L,mpf(1)/2)/Z(s,L,0),10)}")
