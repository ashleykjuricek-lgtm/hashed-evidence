# Greg — half the halving law, from Jacobi duplication

**Received 2026-08-23 via Ash. Verbatim (notation normalised from the original
rendering; no wording changed). Verified in 050 by five independent tests.**

---

I went after item 1. There's a real result here.

The full halving law is not proved yet, but it just got dramatically smaller. Your
ledger currently has

    Z(d,j) > 0  <=>  2j >= d

as 152/152 observed cells. One entire direction is actually provable now:

    2j >= d  ==>  Z(d,j) > 0

for every integer d >= 1, 0 <= j <= d.

Here's the trick. At s = -1/2, the functional equation sends your shifted Epstein
zeta to an absolutely convergent dual character sum. Up to an overall negative
constant,

    Z(d,j) ~ - SUM_{m != 0}  (-1)^(m_1 + ... + m_j) / |m|^(d+1)

Its theta kernel is

    theta_4(q)^j * theta_3(q)^(d-j)

Now use the duplication identity

    theta_3(q) theta_4(q) = theta_4(q^2)^2

That identity is standard Jacobi machinery.

When marks are at least half the dimensions, j >= d-j, pair every plain circle with
one marked circle:

    theta_4^j theta_3^(d-j) = (theta_3 theta_4)^(d-j) theta_4^(2j-d)
                            = theta_4(q^2)^(2(d-j)) theta_4(q)^(2j-d)

And for 0 < q < 1,  0 < theta_4(q) < 1.  Therefore

    theta_4(q)^j theta_3(q)^(d-j) < 1

pointwise whenever 2j >= d. So the entire dual Mellin integrand is negative. The
functional-equation prefactor at s = -1/2 contains 1/Gamma(-1/2) < 0, which flips
the sign back:

    Z(d,j) > 0

That isn't numerical. That's the theorem.

And holy shit, this gives an exact meaning to your sentence "a marked circle carries
exactly two dimensions." The mechanism is literally

    theta_3(q) theta_4(q) = theta_4(q^2)^2

One marked + one plain direction pair off and become two marked factors at the
doubled nome. That is why the threshold is organized around 2j versus d. The "two
dimensions" were sitting in the Jacobi duplication identity the whole goddamn time.

---

There is a second result too. Marks are strictly monotone.

For j > 0, subtract neighboring cases before analytic continuation. The divergent
common piece cancels:

    Z(d,j+1) - Z(d,j)
      = (1/Gamma(-1/2)) INT_0^inf t^(-3/2) theta_2(t)^j theta_3(t)^(d-j-1) [theta_2(t) - theta_3(t)] dt

But Jacobi's identity gives  theta_3^4 = theta_2^4 + theta_4^4,  so  theta_3 >
theta_2 > 0. Thus the integrand before the gamma factor is strictly negative, while
Gamma(-1/2) = -2 sqrt(pi) < 0. Therefore

    Z(d,j+1) > Z(d,j)

Every additional mark moves the energy strictly upward. Not 152 cells. Every one.

Your real-d, real-j continuation already factorizes as Theta(t) = theta_A(t)^j
theta_P(t)^(d-j), which is exactly what makes this monotonicity argument available.
The continuation also reproduces the integer lattice cases, which is the right
sanity check before using it this way.

---

So the giant alleged theorem has now collapsed to one remaining obstruction.

We know: Z(d,0) < 0 from the ordinary functional equation; Z(d,j) increases strictly
with j; and Z(d,d/2) > 0 -- and indeed every j >= d/2 is now proved positive.

Therefore the only thing left is to prove that the zero doesn't cross the last
sub-half integer. Using your real-j continuation, that can be expressed as one clean
lemma:

    Z(d, (d-1)/2) < 0

If that lemma is proved, monotonicity immediately gives  j < d/2 ==> Z(d,j) < 0,
and combined with the result above:

    Z(d,j) > 0  <=>  2j >= d

So I would change the ledger now. Do not move the whole halving law to PROVED yet.
Split it:

    PROVED:   2j >= d ==> Z(d,j) > 0, plus strict monotonicity in j.
    OBSERVED / remaining lemma:  2j < d ==> Z(d,j) < 0.

And the next target is no longer "prove the halving law." It is: prove the
one-half-under boundary is negative. That is a much smaller animal.

Also, the pairing theorem gives the conceptual mechanism the ledger was missing:
this isn't "half" because the table numerically likes halves. A P-A pair literally
undergoes a theta duplication into two A's. Your "one marked circle carries two
dimensions" line at present is still listed as merely observed. Part of that
statement has just stopped being an observation. It has an equation.
