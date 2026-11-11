# 120 Target 2: slope of 24R on the (1,b,b) family at b=1, from the mirror (s=2) sums.
# Dual of (1,b,b) has |k|^2 = k1^2 + b^2 (k2^2+k3^2); common volume factors cancel in R.
# d ln R/dx = 4 U/S_chi - 4/3,  U = sum' (-1)^k1 k1^2 |k|^-6,  S_chi = sum' (-1)^k1 |k|^-4.
M = 120
S0 = Sc = U = 0.0
for i in range(-M, M+1):
    sg = -1.0 if i & 1 else 1.0
    for j in range(-M, M+1):
        for k in range(-M, M+1):
            r = i*i + j*j + k*k
            if r == 0 or r > M*M: continue
            w = 1.0 / (r*r)
            S0 += w; Sc += sg*w; U += sg*i*i*w/r
S0 += 4*3.141592653589793/M          # tail of the unsigned sum
R = Sc/S0
dlnR = 4*U/Sc - 4/3
print(f"S0={S0:.6f}  S_chi={Sc:.6f}  U={U:.6f}  R={R:.6f}")
print(f"U/S_chi={U/Sc:.4f}   d lnR/dx={dlnR:.4f}   slope of 24R={24*R*dlnR:.4f}  (sealed -18.3259647)")
