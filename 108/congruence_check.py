"""Receipt for the congruence lemma of entry 108 (numeric side).

Lemma (proved in lemma-proof.md, elementary): for x in Z^d with |x|^2 = m and
exactly k odd coordinates, m = k (mod 4). Hence on rings divisible by 4 the
only inhabitable sectors are k = 0 (mod 4) -- in d = 8: {0, 4, 8}.

This script checks the congruence exhaustively for d = 8, all rings m <= 200,
via the same meet-in-the-middle sector census sealed in 107.
"""
import itertools, sys
from collections import defaultdict

M = 200
vals = list(range(-14, 15))
half = defaultdict(int)
for c in itertools.product(vals, repeat=4):
    n = sum(x * x for x in c)
    if n <= M:
        half[(n, sum(1 for x in c if x % 2))] += 1
N = defaultdict(lambda: defaultdict(int))
for (n1, k1), c1 in half.items():
    for (n2, k2), c2 in half.items():
        if n1 + n2 <= M:
            N[n1 + n2][k1 + k2] += c1 * c2

bad = [(m, k) for m in range(M + 1) for k, v in N[m].items() if v and (m - k) % 4]
occ = sorted({k for m in range(0, M + 1, 4) for k, v in N[m].items() if v})
print("violations of m == k (mod 4):", len(bad))
print("occupied sectors on rings 4|m:", occ)
print("PASS" if not bad and occ == [0, 4, 8] else "FAIL")
sys.exit(0 if not bad and occ == [0, 4, 8] else 1)
