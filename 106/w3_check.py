"""W3 check: the all-odd sector of Z^8 vs the E8 glue coset.

Claim under test (pre-stated in round-4 memo, item W3):
  The all-eight-coordinates-odd sector of Z^8 -- the sector the sealed
  two-shell counting law watches open at dimension 8, on rings divisible
  by 8 -- is, at half scale, exactly the disjoint union of the two glue
  cosets that extend the checkerboard lattice D8 to the two copies of E8.

Two independent methods (house rule):
  M1: direct enumeration. Count all-odd vectors of Z^8 per norm ring,
      split by coordinate-sum mod 4 (the two candidate glue cosets),
      and independently count half-integer vectors (Z+1/2)^8 per norm,
      split by which D8-coset they glue (even/odd integer-part sum).
      Check the scaling bijection ring by ring.
  M2: classical closed form. E8's theta series is the Eisenstein series
      E4, so the E8 shell count at norm 2m is 240*sigma_3(m). The glue
      count is r_E8(2m) - r_D8(2m) with r_D8 enumerated separately
      (even-coordinate-sum integer vectors). Predicts
        A(8m) = 2 * (240*sigma_3(m) - r_D8(2m)).

Any mismatch anywhere prints FAIL and the script exits nonzero.
"""

import itertools, sys
from collections import defaultdict

NMAX = 96          # check rings |y|^2 = n for n <= NMAX (Z^8, all-odd side)
ok = True

def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)

# ---------- M1a: all-odd vectors of Z^8, meet-in-the-middle ----------
# per half (4 coords): map (norm, sum mod 4) -> count
odd_vals = [v for v in range(-9, 10) if v % 2 != 0]   # |v|<=9 covers norm<=96 easily
half = defaultdict(int)
for c in itertools.product(odd_vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= NMAX:
        half[(n, sum(c) % 4)] += 1

A = defaultdict(int)            # A[n] = all-odd count on ring n
A_split = defaultdict(lambda: defaultdict(int))   # A_split[n][sum mod 4]
for (n1, s1), c1 in half.items():
    for (n2, s2), c2 in half.items():
        n = n1 + n2
        if n <= NMAX:
            A[n] += c1 * c2
            A_split[n][(s1 + s2) % 4] += c1 * c2

# check: all-odd rings occur only at n = 0 mod 8
for n in range(1, NMAX + 1):
    if A[n] and n % 8 != 0:
        fail(f"all-odd point found on ring {n}, not divisible by 8")

# check: split is only between sum=0 mod 4 and sum=2 mod 4, and 50/50
for n in range(8, NMAX + 1, 8):
    sp = A_split[n]
    if sp[1] or sp[3]:
        fail(f"ring {n}: odd coordinate-sum residue appeared (impossible for 8 odds)")
    if sp[0] != sp[2]:
        fail(f"ring {n}: chirality halves unequal ({sp[0]} vs {sp[2]})")

# ---------- M1b: half-integer vectors (Z+1/2)^8, independent loop ----------
# x = y/2 with y all-odd; E8-norm is |x|^2 = n/4. Glue coset of E8 = D8 + g:
# x = g + v with v in Z^8, sum(v) even  <=>  sum(x_i - 1/2) even.
halfint_by_norm = defaultdict(lambda: defaultdict(int))  # [4*|x|^2][int-part-sum mod 2]
for c in itertools.product(odd_vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= NMAX:
        halfint_by_norm_key = None  # placeholder; done via convolution below
# reuse `half` but track integer-part sum parity: for y odd, (y-1)/2 parity.
half2 = defaultdict(int)  # (norm, parity of sum((y_i-1)/2)) -> count, per 4-coord half
for c in itertools.product(odd_vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= NMAX:
        p = sum((x - 1) // 2 for x in c) % 2
        half2[(n, p)] += 1
G = defaultdict(lambda: defaultdict(int))   # G[n][parity] over full 8 coords
for (n1, p1), c1 in half2.items():
    for (n2, p2), c2 in half2.items():
        n = n1 + n2
        if n <= NMAX:
            G[n][(p1 + p2) % 2] += c1 * c2

# bijection checks: each parity class = one glue coset; together = A(n);
# and parity classes must match the sum-mod-4 split (sum(y)=2*sumint+8).
for n in range(8, NMAX + 1, 8):
    if G[n][0] + G[n][1] != A[n]:
        fail(f"ring {n}: half-integer total != all-odd total")
    if G[n][0] != A_split[n][0] or G[n][1] != A_split[n][2]:
        fail(f"ring {n}: coset split mismatch between the two bookkeepings")

# ---------- M2: classical closed form ----------
def sigma3(m):
    return sum(d ** 3 for m_d in range(1, m + 1) for d in [m_d] if m % d == 0)

# r_D8(k): integer vectors, even coordinate sum, norm k -- own enumeration
int_vals = [v for v in range(-9, 10)]
halfD = defaultdict(int)   # (norm, sum mod 2) per 4 coords
for c in itertools.product(int_vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= NMAX // 4:
        halfD[(n, sum(c) % 2)] += 1
rD8 = defaultdict(int)
for (n1, s1), c1 in halfD.items():
    for (n2, s2), c2 in halfD.items():
        if (s1 + s2) % 2 == 0 and n1 + n2 <= NMAX // 4:
            rD8[n1 + n2] += c1 * c2

print(" m | ring 8m | A(8m) all-odd | per coset | 240*sigma3(m) | r_D8(2m) | 2*(E8-D8) | match")
for m in range(1, NMAX // 8 + 1):
    e8 = 240 * sigma3(m)
    pred = 2 * (e8 - rD8[2 * m])
    match = "YES" if pred == A[8 * m] else "NO"
    if pred != A[8 * m]:
        fail(f"m={m}: closed form predicts {pred}, enumeration gives {A[8*m]}")
    print(f"{m:2d} | {8*m:6d} | {A[8*m]:12d} | {A[8*m]//2:9d} | {e8:12d} | {rD8[2*m]:8d} | {pred:9d} | {match}")

# E8 shell counts sanity (the card's/classical values)
for m, expect in [(1, 240), (2, 2160), (3, 6720)]:
    got = 240 * sigma3(m)
    if got != expect:
        fail(f"E8 shell {2*m}: sigma3 form gives {got}, classical value {expect}")

print()
print("ALL CHECKS PASS" if ok else "CHECKS FAILED")
sys.exit(0 if ok else 1)
