"""098: check that the sealed transversal crossing b* decomposes as
gap / chirality, corrected by the well:

    ln(b*)  =  eps0 / |s_odd|  *  [1 + c2*(eps0/|s_odd|)^2/eps0 + ...]

All inputs are sealed constants: eps0 (052/054 via R), s_odd and b* (047,
claim-state C1 in 054), c2 (096).
"""
from mpmath import mp, mpf, log

mp.dps = 30
eps0  = mpf('0.00054595046537060288190')   # sealed gap (well bottom, 052/054)
slope = mpf('18.3259647484177')            # sealed chirality (odd slope, 047/C1)
bstar = mpf('1.0000297915619869892')       # sealed crossing (047/C1)
c2    = mpf('0.58260865')                  # sealed well stiffness (096)

x_pred = eps0 / slope
x_seal = log(bstar)
rel = 1 - x_pred / x_seal
well_term = c2 * x_seal ** 2 / eps0

print('x* predicted (gap/chirality):', mp.nstr(x_pred, 12))
print('x* sealed    (ln b*):        ', mp.nstr(x_seal, 12))
print('relative gap 1 - pred/sealed:', mp.nstr(rel, 6))
print('well correction c2 x*^2/eps0:', mp.nstr(well_term, 6))
print('ratio of the two:            ', mp.nstr(rel / well_term, 6))
