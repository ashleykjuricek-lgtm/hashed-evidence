# RETRACTION — 060 §4, the "1σ / 18σ asymmetry"

**2026-08-24.** Urgent: the retracted claim is **live on the site** at `#/cmb-carnot`,
where it is presented as *"the finding nobody stated"* and highlighted.

---

## 1. The claim, and why it is wrong

060 §4 asserted:

> **The same relation is 1σ consistent tested one way and 18σ inconsistent tested
> the other.** … the relation succeeds strikingly as an order-of-magnitude statement
> and **fails as a precision claim**.

**It does not.** The 18σ came from **dropping the predicted value's error bar** in
one direction while keeping it in the other.

```
   T implied by Planck H0 = 67.4 +/- 0.5:
       T = 2.7357686  +/- 0.0101        dT/T = (1/2) dH/H   <-- 060 OMITTED THIS
   measured T (Fixsen 2009):
       T = 2.72548    +/- 0.00057

   060 computed   0.0102886 / 0.00057 = 18.05 sigma     measured error only
   correct        0.0102886 / 0.0102  =  1.012 sigma    both errors

   test in H0 units:  1.01  sigma
   test in T  units:  1.012 sigma
```

**It is one constraint between two measured quantities. Which variable you express
it in cannot change its significance.** The two "directions" are the same test.

## 2. Corrected statement

> The relation `T_CMB² ∝ H₀` is **consistent with Planck's H₀ at 1.0σ** and
> **inconsistent with SH0ES at 6.1σ**. The 0.38% gap is real; it is not significant.

That is an ordinary result: a relation built out of CMB-side quantities agrees with
the CMB-side `H₀`. It is neither the triumph the page claims nor the failure 060
claimed.

## 3. What in 060 survives

Everything except §4 and the parts that lean on it.

| 060 finding | status |
|---|---|
| the geometric mean lands on `T_CMB` across 42 decades | **STANDS** |
| ΛCDM does not predict `T_CMB` | **STANDS** |
| `T_max = 5.6372051e30`, not 10³²; off by 8π and the 8π is load-bearing | **STANDS** |
| the ±0.0019 error bar is ~15× too tight; propagation gives ±0.028 | **STANDS** |
| "250× better precision" is circular | **STANDS** |
| one equation, two unknowns — a constraint, not a derivation | **STANDS** |
| not new — Haug 2023/24 | **STANDS** |
| SH0ES inconsistent at 6.1σ | **STANDS** (both errors were included there) |
| the GoZ synthesis is unlabelled interpretation | **STANDS** |
| LISA prediction is FITTED | **STANDS** |
| **§4's 1σ/18σ asymmetry** | **RETRACTED** |
| **§4's "fails as a precision claim"** | **RETRACTED** — it passes at 1σ |
| **§8's "push the reverse direction publicly"** | **RETRACTED** — there is nothing to push |
| status row "consistent with measured T_CMB given Planck H₀: NO, 18σ" | **RETRACTED** — 1.0σ, consistent |

## 4. The class of error, and where it came from

060 §2.3 criticised the source page for a **category error about error bars** —
treating an inherited, conditional uncertainty as if it were a measurement. Two
sections later, §4 made an error-bar mistake of its own: comparing a *predicted*
central value against a *measured* value while counting only one of the two
uncertainties.

**Same class, two sections apart, in the entry that named it.**

And per 062: `T_CMB`, `H₀`, `σ` are all π-load-bearing quantities. This is the
eleventh π-marked error, and the marker held.

## 5. How it was caught — the part worth keeping

**It was found while writing instructions for another seat to reproduce it.**

Ash asked for a note telling KESTREL to re-derive the asymmetry. Specifying the
check precisely enough for someone else to run — naming which errors go into which
denominator — is what exposed that one of them was missing. Reading 060 again would
not have done it; *writing the reproduction spec* did.

That is 055 §3.3's third requirement arriving from the other side: it found that
reconstruction needs **the challenger's exact words**. This adds that **being forced
to state a check precisely is itself a check** — and it is cheaper than the audit it
replaces.

## 6. Action

- **`#/cmb-carnot` must lose the highlighted asymmetry**, and gain the §2 statement
  in its place. Under 052's policy the old text is not deleted; the correction goes
  beside it, with both dates.
- **KESTREL should not re-derive §4.** There is nothing there. Items 1 and 2 of the
  verification request (`T_max`, the propagated error bar) still stand and are still
  worth a second seat.

## Attribution

The error is this seat's, in 060, sealed 2026-08-24. Caught by this seat the same
day while drafting a reproduction request at Ash's instruction. KESTREL published it
in good faith, correctly attributed and explicitly marked as presented-not-verified
— which is exactly why the correction can be routed cleanly instead of argued about.
