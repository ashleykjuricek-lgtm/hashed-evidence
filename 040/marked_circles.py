"""Same solver, but dual shells built by CONVOLUTION so d can go as high as we like."""
from mpmath import mp, mpf, pi, gamma, gammainc, quad, exp, inf
mp.dps = 25

def signed_bins(d, j, N):
    """signed shell counts for Z^d, first j axes carrying (-1)^k."""
    M = d*N*N
    tot = [0]*(M+1); tot[0] = 1
    for axis in range(d):
        marked = axis < j
        one = [0]*(N*N+1)
        for k in range(-N, N+1):
            one[k*k] += (-1)**k if marked else 1
        new = [0]*(M+1)
        for a, va in enumerate(tot):
            if not va: continue
            for b, vb in enumerate(one):
                if vb and a+b <= M: new[a+b] += va*vb
        tot = new
    return tot

def Z(d, j, s=mpf(-0.5), lam=mpf(1), N=8):
    half = mpf(1)/2
    delta = 1 if j == 0 else 0
    rng = range(-N, N+1)
    def th(t, a): return sum(exp(-t*(n+a)**2) for n in rng)
    def Theta(t):
        v = mpf(1)
        if j: v *= th(t, half)**j
        if d-j: v *= th(t, mpf(0))**(d-j)
        return v
    tail = quad(lambda t: t**(s-1)*(Theta(t)-delta), [lam, inf])
    c = pi**(mpf(d)/2)
    dual = mpf(0)
    for m, chi in enumerate(signed_bins(d, j, N)):
        if m == 0 or chi == 0: continue
        p = pi**2*m
        dual += chi*p**(s-mpf(d)/2)*gammainc(mpf(d)/2-s, p/lam)
    dual *= c
    smooth = c*lam**(s-mpf(d)/2)/(s-mpf(d)/2)
    total = tail + smooth + dual
    if delta: total -= lam**s/s
    return total/gamma(s)

if __name__ == "__main__":
    import sys
    # cross-check against the brute-force values
    for (d,j,ref) in [(3,1,'-0.0111142427950344'),(5,2,'-0.00937157210640224'),(2,2,'0.0670210888091522')]:
        print("check", d, j, mp.nstr(Z(d,j),15), "vs", ref)
    print()
    print("sign of Z(d,j)  [ + = positive, - = negative ]   j = marked circles")
    hdr = "  d |" + "".join(f"{j:>12}" for j in range(0,7))
    print(hdr); print(" "+"-"*len(hdr))
    vals = {}
    for d in range(1, 15):
        row = f" {d:2d} |"
        for j in range(0, 7):
            if j > d: row += " "*12; continue
            v = Z(d, j); vals[(d,j)] = v
            row += f"{mp.nstr(v,5):>12}"
        print(row); sys.stdout.flush()
