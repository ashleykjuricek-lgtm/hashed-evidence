"""Is the 'floor at ten' real, or an artefact of quoting Z instead of the ratio R?
038's own rule: never quote a convention-dependent share. R = Z(d,j)/Z(d,0) is the
convention-free object. Recompute the balanced diagonal in R."""
from marked_circles import Z
from mpmath import mp, nstr
mp.dps = 20
print("  d    j     Z(d,d/2)          |Z(d,0)|         R = Z/Z0        trend(Z)  trend(R)")
pz = pr = None
for d in range(2, 25, 2):
    z0 = Z(d, 0); z = Z(d, d//2); R = z/z0
    tz = "" if pz is None else ("down" if z < pz else "UP  ")
    tr = "" if pr is None else ("down" if abs(R) < abs(pr) else "UP  ")
    print(f" {d:3d}  {d//2:3d}   {nstr(z,10):>14}  {nstr(abs(z0),10):>14}  {nstr(R,10):>14}    {tz:>5}    {tr:>5}")
    pz, pr = z, R
