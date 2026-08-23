"""KESTREL claims: a1 = f/q = 0.29235191853581987768 disagrees with 1-1/sqrt2 =
0.29289321881 'at the third digit', therefore 1-1/sqrt2 was 'never the leading
term' -- and retired it in three files.

But the March form is  eps1 = q(1-1/sqrt2)(1-q).  So

    eps1/q = (1-1/sqrt2)*(1-q)   NOT   (1-1/sqrt2)

Check whether the entire 'disagreement' is the (1-q) factor."""
from mpmath import mp, mpf, exp, pi, sqrt, nstr
mp.dps = 40

q   = exp(-2*pi)
g   = 1 - 1/sqrt(2)                       # 1 - 1/sqrt2
eps = mpf('0.000545950465370602881900548987547102684230630092')   # our 50-digit value

print("q            =", nstr(q, 25))
print("1 - 1/sqrt2  =", nstr(g, 25))
print()
a1 = eps/q
print("f/q                       =", nstr(a1, 22), "   <- KESTREL's 'a1'")
print("KESTREL reported          =  0.29235191853581987768")
print()
print("(1-1/sqrt2)               =", nstr(g, 22))
print("(1-1/sqrt2)*(1-q)         =", nstr(g*(1-q), 22), "   <- what eps1/q ACTUALLY is")
print()
d_naive = a1 - g
d_right = a1 - g*(1-q)
print("f/q  -  (1-1/sqrt2)       =", nstr(d_naive, 8), "   <- KESTREL's 'disagreement'")
print("f/q  -  (1-1/sqrt2)(1-q)  =", nstr(d_right, 8), "   <- what is actually left over")
print()
print("ratio of the two          =", nstr(d_naive/d_right, 8))
print()
c2 = mpf('0.003031437007957836689966591305706670236631011764')
print("KESTREL's own c2          =", nstr(c2, 22))
print("c2 * q                    =", nstr(c2*q, 12))
print("leftover f/q-(1-1/s2)(1-q)=", nstr(d_right, 12))
print("   these match?           ", abs(c2*q - d_right) < mpf(10)**-12)
print()
print("so:  f/q = (1-1/sqrt2)(1-q) + c2*q  =", nstr(g*(1-q) + c2*q, 22))
print("     f/q                            =", nstr(a1, 22))
print("     residual                       =", nstr(a1 - (g*(1-q)+c2*q), 6))
