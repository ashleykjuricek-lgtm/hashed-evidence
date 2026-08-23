"""KESTREL: slope = -27.49, family = volume-preserving stretch, APP on the STRETCHED axis.
Us (047):   slope = -18.326, family = 1 x b x b, APP on the UNSTRETCHED axis.
And the scar page carried +18.3, which KESTREL called a fitted guess.

Compute both families exactly and see whether the numbers are two right answers
to two different questions."""
import anisotropic
from mpmath import mp, mpf, diff, nstr, sqrt
mp.dps = 25
A, P = mpf(1)/2, mpf(0)

def eps_of(Lfun, alpha):
    def f(b):
        L = Lfun(mpf(b))
        return 24*anisotropic.Z(L, alpha)/anisotropic.Z(L, [P,P,P]) - 1
    return f

fams = {
  "047:  L=(1,b,b), A on the SHORT (unstretched) axis":
      (lambda b: [1, b, b], [A, P, P]),
  "047b: L=(1,b,b), A on a STRETCHED axis":
      (lambda b: [1, b, b], [P, A, P]),
  "KESTREL: volume-preserving L=(b,1/sqrt(b),1/sqrt(b)), A on STRETCHED axis":
      (lambda b: [b, 1/sqrt(b), 1/sqrt(b)], [A, P, P]),
  "KESTREL': volume-preserving, A on a SHORT axis":
      (lambda b: [b, 1/sqrt(b), 1/sqrt(b)], [P, A, P]),
}
print("eps(1) is family-independent (it is the cube):")
for name, (Lf, al) in fams.items():
    f = eps_of(Lf, al)
    e1 = f(1); s = diff(f, mpf(1))
    print()
    print(f"  {name}")
    print(f"     eps(1)   = {nstr(e1, 15)}")
    print(f"     d eps/db = {nstr(s, 10)}")
    print(f"     b* ~ 1 + = {nstr(-e1/s, 8)}   ->  b* = {nstr(1-e1/s, 14)}")
