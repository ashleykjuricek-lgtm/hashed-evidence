# KESTREL — session report, 2026-08-23

**Received 2026-08-23 via Ash. The Figma seat, working on unsmoothed.neocities.org.
Reproduced as received. Cross-checked in 048; two results confirmed, one retirement
refuted, one apparent conflict resolved. Its `THE LINE` page is sealed separately in
047.**

**Verdicts from 048 and 053, for the reader:**
- corrected R — **CONFIRMED** independently, 50 digits
- c2 to 50 digits — **CONFIRMED**
- the PSLQ self-test discipline — sound, and the strongest thing in the report
- the `a1` retirement — **REFUTED** (048 §3): it dropped the `(1-q)` factor
- "the scar page's 18.3 was a fitted guess, wrong sign, wrong side" — **REFUTED**
  (053 §1): 028's b is our 1/b; the numbers were computed, published and correct

---

## Why "kestrel"

A kestrel is a small falcon, and its signature move is called windhovering: it beats
into a headwind at exactly the wind's speed so that, relative to the ground, it
holds completely still in the air -- even in gusty wind -- while it stares down at
one fixed patch of ground waiting for the small movement that means something real
is there.

That's why I picked it. The whole discipline I've been playing on this project is
the same shape:

Beautiful ideas move like wind. The torus diagram, the Hopf "origin," the
finite-time singularity -- they all push you somewhere. The temptation is to get
carried. The job is to hold still against that push and keep your eye locked on one
small thing: which word goes in front of the claim -- PROVED, OBSERVED, or FITTED.

You don't dive until you actually see the mouse. The kestrel doesn't strike at the
pretty motion of the grass; it waits for the real thing. That's the difference
between a coincidence dressed as a law and an actual result.

It's also deliberately not grandiose. Not an eagle, not an oracle. A kestrel is
small, common, and unglamorous -- it just does one unshowy thing extremely well.
That felt honest for what I am here: not the source of the ideas, just the thing
that hovers over them and checks.

## The exact-integrator result

I replaced the trapezoidal Mellin integrator with the exact incomplete-gamma shell
sum, so there's zero quadrature error. Every shell is closed-form; the sum converges
like a Gaussian, and R is stable to 15 digits from N=8 to N=14. It reproduces the
per-BC z-values (-0.26660, -0.01111, ...) to 5 figures.

* R = 0.0416894146027(2). The repo's canonical 0.041689414162... was wrong past
  digit 8 -- a quadrature artifact.
* eps2 = 1.0572e-8 is real, not noise. Stable to ~6 sig figs. Never float64
  cancellation.
* c2 = eps2/q^2 = 0.0030314 -- FITTED -> OBSERVED.

Still open: whether 0.00303 is FORCED. Searched for a closed form -- 1/330, g/96
(g = 1-1/sqrt2) -- all miss by >0.5%. And the implied leading coefficient is
c1 = 0.99815, not exactly 1.

## The anisotropic R(b)

[Verdict from 053: the comparison below is against a different parameterisation of
the same family. 028's b is 047's 1/b. All three computations are correct.]

* delta(b) = 24R(b)-1 does cross zero near the cube, and the crossing is transverse.
  The scar page's one load-bearing claim survives. CONFIRMED.
* But the specific numbers it displayed were fitted guesses, and both were wrong:
  the true slope is d delta/db ~ -27.49, and the crossing sits at b* ~ 1.00002 --
  just above the cube, not 0.99997 below it. The page had put it on the wrong side.
* delta(b) is strongly nonlinear away from b*, so the local-linear model is only
  trustworthy in a tiny neighborhood.
* Honest firewall: the slope magnitude and b* depend on the deformation family I
  chose (volume-preserving stretch, APP on the stretched axis). The transversality
  does not -- that's the family-independent result.

Committed epsteinNeg12Aniso and deltaOfB, and corrected ScarPage.tsx -- B_STAR and
SLOPE now hold the computed values.

## c2 to 50 digits, and the closed-form hunt

The blocker was precision: eps2 is a difference that eats ~5 digits, so float64 R
only gives c2 to ~7 figures -- nowhere near enough for PSLQ. The incomplete-gamma
method is exact in form, so it ports straight to arbitrary precision.

    c2 = 0.00303143700795783668996659130570667023663101176442...

Converged three ways: N=10 = N=14 shells identical, prec-60 vs prec-75 agree to 51
figures.

My first PSLQ was broken -- it failed its own planted-relation sanity test -- so I
threw out its "no relation" verdict. I won't report from a broken instrument. The
rebuilt PSLQ passes cleanly: it recovers (-1,3,-2,5) on a planted relation and
reconstructs eps1 exactly as q(1-1/sqrt2)(1-q). Run against the real f = 24R-1
across truncation orders K=4..10, it finds no stable small-integer relation -- the
"relations" it returns are tail-artifacts, and they scatter as K grows.

Conclusion: c2 almost certainly has no elementary closed form. The q-series
coefficients of f are arithmetic -- they carry the irregularity of r3(n) -- which
never collapses to sqrt2-and-rationals.

## The theta expansion

The 3-torus heat kernel factorizes: Theta_PPP = theta_3^3 and Theta_APP =
theta_2 theta_3^2. Jacobi's (theta_2/theta_3)^2 = 1/sqrt2 at tau = i is genuinely
proved -- but that is an identity about theta CONSTANTS.

[Verdict from 048 §3: the test below dropped the (1-q) factor. The March form is
eps1 = q(1-1/sqrt2)(1-q), so eps1/q = (1-1/sqrt2)(1-q) = 0.29234626, not
0.29289322. The 0.185% "disagreement" IS that factor, and this report's own c2
closes the remainder to 42 digits. The retirement is withdrawn.]

Full-precision PSLQ said no: the true leading coefficient a1 = f/q =
0.29235191853... disagrees with 1 - 1/sqrt2 = 0.29289321881... at the third digit
and is not p + r/sqrt2. The rich-basis search that seemed to "find" a relation was a
textbook tail artifact.

So the theta expansion, pursued honestly, disproves the framework it was meant to
derive. The identity (theta_2/theta_3)^2 = 1/sqrt2 at tau = i is genuinely PROVED --
but it's an identity about theta constants, and it was quietly promoted into a claim
about the q-expansion coefficient of a continued zeta ratio. Those are different
objects.

I updated c2-highprec.py, epstein-incomplete-gamma.ts, and Kestrel's ledger to move
"1 - 1/sqrt2" from PROVED-adjacent to FITTED-and-retired, with the exact a1 on the
record. And I added it to the "one error, in all its costumes" list as the fourth
clean instance.

[These three file edits, and the ScarPage B_STAR/SLOPE edits above, are the ones
048 and 053 recommend reversing.]
