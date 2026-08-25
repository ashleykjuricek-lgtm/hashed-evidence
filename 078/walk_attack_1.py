"""WALK, attack surface 1: is {sign, interval, digits-to-precision} sufficient for
every claim in the ledger's four columns?

The closed language is over a WITNESS'S OUTPUT FIELDS -- a finite tuple of numbers
produced by one run. Classify all 15 PROVED claims by whether any such predicate
can express them."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

# (id, statement, logical form, expressible in {sign, interval, digits}?)
P = [
 ("P1","S(m) = 0 for EVERY odd m",
      "universal over infinitely many m", False,
      "a witness computes S(m) for ONE m. 'for every odd m' is not a property of one output tuple."),
 ("P2","S(m) = (-1)^(m/2) r2(m) for EVERY even m",
      "universal", False, "same"),
 ("P3","weight-independence: holds for ANY radial weight",
      "universal over a FUNCTION SPACE", False,
      "quantifies over weights, not over numbers. No finite output tuple ranges over it."),
 ("P4","sigma is a symmetry of k1^2+k2^2 and of NO anisotropic form",
      "universal + NEGATIVE existential", False,
      "a non-existence claim over a family. No output value witnesses an absence."),
 ("P5","T(m) = 2 SUM S(m - k3^2) for EVERY odd m",
      "universal", False, "same as P1"),
 ("P6","T2(m) = m r2(m)/2 - 2 SUM_E k1^2 for EVERY odd m",
      "universal (an identity)", False,
      "an identity is a universal. Checking it at m=5 is not asserting it."),
 ("P7","R(2,2) = 2^s - 1 for ALL s",
      "universal over a continuum", False,
      "expressible only at a POINT. 'for all s' is not."),
 ("P8","1 - 1/sqrt2 = -R(2,2) at s = -1/2",
      "two numbers, one point", True,
      "digits-to-precision. THE CLOSED LANGUAGE HANDLES THIS."),
 ("P9","r3(1) = 6 and r3(2) = 12",
      "two integers", True,
      "digits-to-precision. HANDLED."),
 ("P10","|n+alpha|^2 != 0 whenever any alpha = 1/2",
      "universal over the lattice", False,
      "universal, though trivially provable. Still not an output property."),
 ("P11","NO integer-power series in q can be exact",
      "NEGATIVE existential over a function class", False,
      "the strongest failure. Nothing a witness outputs can witness 'no such series exists'."),
 ("P12","2j >= d  =>  Z(d,j) > 0, for EVERY integer d >= 1",
      "universal over d, j", False,
      "sign IS expressible per cell. The quantifier is not."),
 ("P13","Z(d,j+1) > Z(d,j) for j >= 1",
      "universal", False, "same"),
 ("P14","the prefactor cancels in ANY ratio, every d and s",
      "universal over d and s", False, "same"),
 ("P15","pi_1(S^2) = 0, so a sphere admits no marking",
      "NON-NUMERICAL: a topological fact", False,
      "not a number at all. No witness output has a homotopy group as a field."),
]

print("="*78)
print("ATTACK 1 -- the closed predicate language against the PROVED column")
print("="*78)
print()
ok = [p for p in P if p[3]]
no = [p for p in P if not p[3]]
for pid, st, form, exp, why in P:
    tag = "EXPRESSIBLE" if exp else "NOT EXPRESSIBLE"
    print(f"  {pid:4} {tag:16} {form}")
print()
print(f"  expressible     : {len(ok):2d} of {len(P)}   ({', '.join(p[0] for p in ok)})")
print(f"  NOT expressible : {len(no):2d} of {len(P)}")
print()
print("  by reason:")
from collections import Counter
c = Counter(p[2] for p in no)
for k,v in c.most_common(): print(f"     {v:2d}  {k}")
print()
print("="*78)
print("THE ANSWER THEY ASKED FOR")
print("="*78)
print()
print("  P11 is the cleanest kill:")
print("     'NO integer-power series in q = e^(-2pi) can be exact.'")
print("     A negative existential over a function class. There is no output field")
print("     whose sign, interval, or digits witnesses the NON-EXISTENCE of a series.")
print("     P11 is 028's murder weapon -- the result the whole programme turns on.")
print()
print("  P3 is the second:")
print("     'holds for ANY radial weight' quantifies over a FUNCTION SPACE.")
print("     It is the property that makes the parity theorem survive every smoothing")
print("     (062), i.e. the reason it is the one result never walked back.")
print()
print("  P15 is the third, and different in kind:")
print("     pi_1(S^2) = 0 is not a number. No witness tuple has a homotopy group in it.")
print()
print("  SCOPE RESULT:")
print("     the (witness, predicate) machinery covers the OBSERVED column almost")
print("     entirely -- R, eps, c2, d*, b*, the slopes, the bins, all are pinned")
print("     numbers with signs and digits -- and covers 2 of 15 PROVED claims.")
print()
print("     It is a discipline for MEASUREMENTS, not for THEOREMS.")
