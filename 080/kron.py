"""Fast Kronecker symbol, VALIDATED against sympy before use.

v1 of pi_is_one_row.py hand-rolled this and got the prime 2 wrong --
kronecker(-4,2) returned 1 where it must return 0 -- so every EVEN discriminant
came out exactly 2x too large. Structured discrepancy; that is what exposed it.
Never trust a hand-rolled number-theory primitive without an oracle."""
def kron(a, n):
    if n == 0: return 1 if a in (1, -1) else 0
    if a % 2 == 0 and n % 2 == 0: return 0
    t = 1
    while n % 2 == 0:
        n //= 2
        if a % 8 in (3, 5): t = -t
    a %= n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: t = -t
        a %= n
    return t if n == 1 else 0

if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    from sympy import kronecker_symbol as ks
    bad = 0; tot = 0
    for d in [-3,-4,-7,-8,-11,5,8,12,13]:
        for n in range(1, 3001):
            tot += 1
            if kron(d, n) != int(ks(d, n)):
                bad += 1
                if bad < 6: print(f"  MISMATCH chi_{d}({n}): fast={kron(d,n)} sympy={int(ks(d,n))}")
    print(f"validated against sympy on {tot} values, 9 discriminants: {bad} mismatches")
    print("SAFE TO USE" if bad == 0 else "*** DO NOT USE ***")
