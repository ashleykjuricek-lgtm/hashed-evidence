"""
Control experiment for the scar model.

Claim under test: a coarse observable r = |delta| loses exactly the information
needed to continue through zero, and that information is carried by p = d(delta)/dt.

Toy dynamics (Greg's proposal): delta' = p, p' = -w^2 delta.  Plain oscillator.
"""
import math

w, A, phi = 1.0, 1.0, 0.0
d  = lambda t: A*math.cos(w*t+phi)
p  = lambda t: -A*w*math.sin(w*t+phi)
r  = lambda t: abs(d(t))

T = 2*math.pi/w
print("=== 1. at the zero crossing, is information destroyed? ===")
tz = (math.pi/2 - phi)/w                      # first delta = 0
print("  t*        = %.6f" % tz)
print("  delta(t*) = %.3e   <- coarse observable is ZERO" % d(tz))
print("  p(t*)     = %+.6f  <- and is MAXIMAL in magnitude" % p(tz))
print("  |p| max   = %.6f" % (A*w))
print("  -> at the drain the coarse coord holds nothing; p holds everything.")

print()
print("=== 2. coarse cycle closes before the full cycle ===")
print("  half period T/2 = %.6f" % (T/2))
for t in (0.3, 0.7, 1.1):
    print("   t=%.1f  (delta,p)=(%+.4f,%+.4f)   ->  t+T/2  (%+.4f,%+.4f)   |delta| same? %s"
          % (t, d(t), p(t), d(t+T/2), p(t+T/2), abs(abs(d(t))-abs(d(t+T/2)))<1e-12))
print("  coarse r returns after T/2; full state (delta,p) needs T. ratio = 2")

print()
print("=== 3. what the coarse observer literally cannot do ===")
eps = 1e-9
before = tz - eps
print("  approaching zero from t<t*:  delta=%+.3e" % d(before))
print("  r(t) alone is symmetric about the crossing, so it admits BOTH")
print("  continuations: delta -> -|.| (cross) or delta -> +|.| (bounce).")
print("  sign(p) selects. p(t*) = %+.4f -> crosses to delta<0." % p(tz))

print()
print("=== 4. four-petal rose: r = A cos(2 theta) ===")
rose = lambda th: A*math.cos(2*th)
print("  theta       r        dr/dtheta   petal")
for th in [0.0, math.pi/4-0.01, math.pi/4, math.pi/4+0.01, math.pi/2]:
    dr = -2*A*math.sin(2*th)
    petal = "center" if abs(rose(th))<1e-9 else ("+" if rose(th)>0 else "-")
    print("  %8.4f  %+8.4f  %+9.4f   %s" % (th, rose(th), dr, petal))
print("  at theta=pi/4 the curve is AT the origin; r alone cannot say which")
print("  petal follows. dr/dtheta = %+.4f does." % (-2*A*math.sin(2*(math.pi/4))))
