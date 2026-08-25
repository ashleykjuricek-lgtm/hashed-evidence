import math
print("Where does each measured constant COME FROM? Two different places.")
print()
print("REAL worlds -- an INTEGER SEARCH, then one logarithm.")
print("   search: smallest (a,b), b>0, with  a^2 - D*b^2 = +-4.   unit = (a + b*sqrt D)/2")
print("   " + "-"*74)
for D, meas in [(5, 0.43040600), (8, 0.62324200), (12, 0.76034450), (13, 0.66272700)]:
    found = None
    for b in range(1, 5000):
        for a in range(0, 5000):
            v = a*a - D*b*b
            if v*v == 16 and (a + b*math.isqrt(D*1))>0:
                if (a + b*math.sqrt(D))/2 > 1: found=(a,b); break
            if v < -16 and a > 4*b*math.isqrt(D)+8: break
        if found: break
    a,b = found
    eps = (a + b*math.sqrt(D))/2
    c = 2*math.log(eps)/math.sqrt(D)
    flag = "AGREE" if abs(c-meas) < 5e-5 else f"DIFFER {abs(c-meas):.2e}"
    print(f"   D={D:2d}: pair {str(found):8s} -> unit {eps:.10f} -> 2*log(u)/sqrt(D) = {c:.8f}"
          f"   measured {meas:.8f}  {flag}")
print()
print("IMAGINARY worlds -- NO integer search exists. The constant is an AREA.")
print("   " + "-"*74)
for D, meas, c, why in [(-4,0.78540300, math.pi/4, "disk a^2+b^2<=X, area pi*X, / 4 units"),
                        (-8,1.11070600, math.pi/(2*math.sqrt(2)), "ellipse a^2+2b^2<=X, area pi*X/sqrt2, / 2 units")]:
    print(f"   D={D}: {why}")
    print(f"          area/units = {c:.8f}   measured = {meas:.8f}   AGREE to {abs(c-meas):.1e}")
print()
print("ASYMMETRY: real worlds' constants are an integer pair wearing a logarithm.")
print("           square worlds' constants are not any integer object at all --")
print("           only the limit of a count divided by a scale.")
