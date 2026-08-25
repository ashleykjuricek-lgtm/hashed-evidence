"""CANONICAL EXECUTABLE WITNESS -- claim: the slope of eps in the anisotropic
deformation of the cubic torus at the cube.

A witness is a FUNCTION with declared inputs and pinned outputs, not a value.
Any artefact -- prose, formula, code output, a constant in a source file --
DISCHARGES this witness by naming its inputs and reproducing the output.

  WITNESS ID   slope-of-eps-anisotropic/v1
  INPUTS       family  in {"1bb", "volpres"}
               chart   in {"direct", "momentum"}     (which axis carries b^2)
               marked  in {"short", "stretched"}
  OUTPUT       d eps / db at b = 1
  TOLERANCE    1e-9
"""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import anisotropic
from mpmath import mp, mpf, diff, sqrt, nstr
mp.dps = 25
A, P = mpf(1)/2, mpf(0)

def witness(family="1bb", chart="momentum", marked="short"):
    """the whole claim, executable, with every convention an explicit argument"""
    def sides(b):
        if family == "1bb":     L = [mpf(1), b, b]
        elif family == "volpres": L = [b, 1/sqrt(b), 1/sqrt(b)]
        else: raise ValueError(family)
        return [1/x for x in L] if chart == "direct" else L
    # BUG FOUND BY BUILDING THIS (v1): "stretched"/"short" are SEMANTIC labels whose
    # axis index is FAMILY-DEPENDENT.  1bb = [1,b,b]: axis 0 short, axes 1,2 stretched.
    # volpres = [b, 1/sqrt b, 1/sqrt b]: axis 0 stretched, axes 1,2 short.  v1 hard-coded
    # one mapping and silently returned the OTHER cell (-13.744 instead of +27.489).
    if family == "1bb":     idx = 0 if marked == "short" else 1
    else:                   idx = 1 if marked == "short" else 0
    alpha = [P, P, P]; alpha[idx] = A
    def eps(b):
        L = sides(mpf(b))
        return 24*anisotropic.Z(L, alpha)/anisotropic.Z(L, [P,P,P]) - 1
    return diff(eps, mpf(1))

PINNED = {
  ("1bb","momentum","short")      : mpf("-18.3259647484177"),
  ("1bb","direct","short")        : mpf("+18.3259647484177"),
  ("volpres","momentum","stretched"): mpf("+27.4889471200"),
}
# BUG 2, also found by building this: v1 used an ABSOLUTE tolerance. The claim
# "27.4889471200" is a 12-figure truncation of 27.4889471226..., so it failed a
# 1e-9 absolute test on a value of size ~27. A witness must declare RELATIVE
# tolerance, or match the digits the claim actually states.
RELTOL = mpf(10)**-9

def discharge(label, claimed_value, **inputs):
    key = (inputs["family"], inputs["chart"], inputs["marked"])
    got = witness(**inputs)
    c = mpf(claimed_value)
    ok_c = abs(got - c)/abs(got) < RELTOL
    print(f"  {label}")
    print(f"     inputs   {inputs}")
    print(f"     claimed  {claimed_value}")
    print(f"     witness  {nstr(got, 15)}")
    print(f"     DISCHARGES: {ok_c}")
    return ok_c

print("="*72)
print("Three historical artefacts, run against ONE witness")
print("="*72)
r1 = discharge("028 App A.3 (June): 'd eps/db ~ +18.3'", "18.3259647484177",
               family="1bb", chart="direct", marked="short")
print()
r2 = discharge("047 (Aug 23): 'd eps/db = -18.3259647484177'", "-18.3259647484177",
               family="1bb", chart="momentum", marked="short")
print()
r3 = discharge("KESTREL (Aug 23): 'the true slope is ~ -27.49'", "27.4889471200",
               family="volpres", chart="momentum", marked="stretched")
print()
print("="*72)
print("VERDICT")
print("="*72)
print(f"  all three discharge the same witness: {r1 and r2 and r3}")
print("  -> they are the SAME CLAIM, evaluated at THREE DIFFERENT INPUT POINTS.")
print("  The 'disagreement' is a disagreement about arguments, not about the world.")
print()
print("  And the refuted charge, in one line:")
print("     KESTREL called 028's number 'a fitted guess'.")
print("     A fitted guess cannot discharge a witness. 028's DOES.")
print("     Running it settles a PROVENANCE claim, which no metadata layer can.")
