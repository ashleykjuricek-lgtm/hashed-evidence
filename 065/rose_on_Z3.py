"""Is the isotropic R a direction-average of something with a rose in it?

R = SUM' chi(n)|n|^-4 / SUM' |n|^-4  bins by |n|^2 -- i.e. it sums over SPHERES.
Deform the metric along a unit direction u:  Q_u(n) = |n|^2 + eps (n.u)^2
and sweep u. If R modulates with direction, there is angular structure under
the shell average."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np

N = 160
ax = np.arange(-N, N+1, dtype=np.int64)
X, Y, Z = np.meshgrid(ax, ax, ax, indexing='ij')
n2 = (X*X + Y*Y + Z*Z).ravel()
keep = (n2 > 0) & (n2 <= N*N)
nx = X.ravel()[keep].astype(np.float64)
ny = Y.ravel()[keep].astype(np.float64)
nz = Z.ravel()[keep].astype(np.float64)
n2 = n2[keep].astype(np.float64)
chi = (-1.0)**nx

Nn = float(np.sum(chi/n2**2)); Dn = float(np.sum(1.0/n2**2))
print(f"isotropic:  N = {Nn:.10f}   D = {Dn:.6f}   R0 = {Nn/Dn:.10f}")
print()

# first-order response matrix  M_ij = SUM f(n) n_i n_j |n|^-6
w = 1.0/n2**3
def Mmat(f):
    return np.array([[float(np.sum(f*a*b*w)) for b in (nx,ny,nz)] for a in (nx,ny,nz)])
Mnum = Mmat(chi); Mden = Mmat(np.ones_like(chi))
np.set_printoptions(precision=8, suppress=True)
print("DENOMINATOR response matrix (f = 1):")
print(Mden)
print("   isotropic?  off-diagonals ~0 and M11=M22=M33 ->",
      abs(Mden[0,0]-Mden[1,1]) < 1e-9 and abs(Mden[0,1]) < 1e-9)
print()
print("NUMERATOR response matrix (f = (-1)^n1):")
print(Mnum)
A, B = Mnum[0,0], Mnum[1,1]
print(f"   diag(A, B, B) with A = {A:.10f}, B = {B:.10f},  A - B = {A-B:.10f}")
print(f"   off-diagonal max = {np.max(np.abs(Mnum - np.diag(np.diag(Mnum)))):.3e}")
print()

# sweep direction in the x-z plane and compare to the predicted quadrupole
print("sweep u = (sin t, 0, cos t): dR/deps vs the quadrupole prediction")
print("   angle(deg)   dR/deps           B + (A-B) ux^2  form      ratio")
for deg in [0, 15, 30, 45, 60, 75, 90]:
    t = np.radians(deg); u = np.array([np.sin(t), 0.0, np.cos(t)])
    nu2 = (nx*u[0] + ny*u[1] + nz*u[2])**2
    dN = -2*float(np.sum(chi*nu2*w)); dD = -2*float(np.sum(nu2*w))
    dR = (dN*Dn - Nn*dD)/Dn**2
    quad = -2*((B + (A-B)*u[0]**2)*Dn - Nn*Mden[0,0])/Dn**2
    print(f"   {deg:8d}   {dR: .10f}    {quad: .10f}    ratio {dR/quad:.8f}")

print()
print("="*70)
print("SECOND TEST: sweep u in the y-z plane (perpendicular to the marked axis)")
print("   First order predicts a CONSTANT there (both y and z give B).")
print("   Any modulation is higher-order lattice structure. What symmetry?")
print("="*70)
def R_at(u, eps):
    Q = n2 + eps*(nx*u[0] + ny*u[1] + nz*u[2])**2
    return float(np.sum(chi/Q**2))/float(np.sum(1.0/Q**2))
for eps in [0.05, 0.3, 1.0]:
    vals = []
    for deg in range(0, 91, 5):
        t = np.radians(deg); u = np.array([0.0, np.cos(t), np.sin(t)])
        vals.append(R_at(u, eps))
    v = np.array(vals)
    print(f"  eps={eps:>4}:  min {v.min():.10f}  max {v.max():.10f}  swing {v.max()-v.min():.3e}")
    print("            ", "  ".join(f"{deg}:{val-v.mean():+.2e}" for deg, val in zip(range(0,91,20), v[::4])))
print()
print("   0 deg = the y axis, 45 deg = the y-z diagonal, 90 deg = the z axis.")
print("   Extrema at 0/45/90 = FOUR-FOLD structure about the marked axis.")
print()
print("="*70)
print("WHY IT CAN NEVER BE A ROSE")
print("="*70)
print("   Crystallographic restriction theorem: a periodic lattice in 2D or 3D")
print("   admits only 2-, 3-, 4- and 6-fold rotational symmetry.")
print("   FIVE- and TEN-fold are forbidden on Z^3, at every order, for all time.")
print("   Z^3's point group is octahedral: 48 elements, axes of order 2, 3, 4.")
print()
print("   022's ten-petal rose lives on a PENROSE lattice. Cut-and-project from")
print("   Z^5 buys exactly the thing periodicity forbids: ten-fold symmetry.")
