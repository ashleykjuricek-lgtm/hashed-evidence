# π is in the road, not in the object

**2026-08-25.** Ash: *"so pi. we gotta figure out pi."*

062 narrowed it to one question: π enters this programme only through Gaussian
machinery — heat kernel, Γ, Ewald, Poisson. **So is π in the object, or only in the
method?**

**Answer: only in the method. And it cancels identically.**

---

## 1. The cancellation is structural, not lucky

The functional equation gives, at `s = −1/2`:

    Z(d,j) = PREFACTOR(d) * SUM'_m chi_j(m) |m|^-(d+1)
    PREFACTOR(d) = pi^(-1-d/2) * Gamma((d+1)/2) / Gamma(-1/2)

**The prefactor depends on `d` and `s` only. The marking `j` does not appear in
it.** So in any ratio at fixed `d` and `s` it cancels exactly:

> **R(d,j) = [ Σ′ χ_j(m) |m|^(−(d+1)) ] / [ Σ′ |m|^(−(d+1)) ]**

Two integer-lattice sums. No π, no Γ, no Gaussian, no regularisation. This holds for
**every** `d` and `j` — it is not special to d = 3.

## 2. Verified

```
   N=120  |m|^2 <= 14400   R = 0.0416890752
   N=200  |m|^2 <= 40000   R = 0.0416893627
   N=300  |m|^2 <= 90000   R = 0.0416894161

   reference (50-digit, 044)  0.0416894146027237751...
```

Converging, from a π-free expression, to the number this programme has been about
since March. The residual is the denominator's tail approximation `4π/√M`, not the
identity.

The denominator independently checks out:

```
   this computation, N=300:   16.5323156
   028 section 5, by the functional equation:  Z_PPP(2) = 16.5323159598
```

**Not new as an identity.** 028 §5 already states *"the identity
R = Z*_APP(2)/Z_PPP(2) holds."* What is new is the consequence, which 028 does not
draw: **π cancels, so it was never in R.**

## 3. What this settles

```
   Z_PPP(-1/2) = -0.2665962787...     an individual energy    pi-LADEN
   Z_APP(-1/2) = -0.0111142427...     an individual energy    pi-LADEN
   R = Z_APP / Z_PPP                  the programme's object  pi-FREE
```

**The individual energies carry π. The ratio does not.** And 028 chose the ratio —
so the central object of the programme has been π-free the whole time, while every
computation of it went through Gaussian machinery that put π back in the arithmetic.

This also explains 039 §1 retrospectively. `R(2,2) = 2^s − 1` and
`R(2,1) = (2^(2s) − 2^s)/2` came out π-free, and that was not luck: **ratios are
always π-free.** d = 2 is special only in also being *algebraically closed*.

And it composes with 062: every PROVED result is π-free or π-inert; every OBSERVED
result looked π-laden. **The OBSERVED results look π-laden because of how we compute
them, not because of what they are.**

> **Every π seen in five months of computing R was in the road. The object is a
> ratio of two sums over the integers.**

## 4. The consequence for the whole c₁ / c₂ / closure saga

If R is a ratio of integer-lattice sums, where does `q = e^(−2π)` come from at all?

**From the method.** The `q`-expansion of `ε = 24R − 1` is produced by the
Chowla–Selberg / Ewald decomposition, and `e^(−2π)` is the natural scale of the
*Poisson dual*: `exp(−π²k²/t)` at `t ~ π`. The nome is Gaussian-derived.

So `c₁`, `c₂`, and the March closure are **coefficients of a representation, not
properties of the object.** They are well-defined once you fix the expansion, but
there is no reason an integer-lattice ratio should have tidy coefficients in a
Gaussian-derived nome.

**Which is exactly what KESTREL found** — `c₂` to 50 digits, no elementary closed
form, PSLQ null across bases. Its diagnosis was that the coefficients inherit the
irregularity of `r₃(n)`. §1 gives the sharper version: **they inherit it because the
object IS a sum over `r₃`, and the `q`-expansion is a coordinate system laid over it
by the method.**

Five months were spent asking what the coefficients of the road are.

## 5. What this does NOT show

- **π-free is not simple.** R is still a ratio of two convergent lattice series, and
  044's bounded nulls stand: not in ℚ[√2] to coefficients 10¹⁰, not algebraic of
  degree ≤ 4 to 10⁹, at 50 digits.
- **The q-expansion is not illegitimate.** It is a valid asymptotic representation
  and 028's refutation of the closure stands on its own terms. The point is only
  that its coefficients belong to the representation.
- **It does not make R easier to compute.** The π-free form converges like `M^(−1/2)`;
  the Gaussian machinery converges geometrically. **The road is faster than the
  object.** That is why it was built.
- **Circle-π and Gaussian-π remain the same constant** (062 §2). Nothing here
  separates them.

## 6. So: what π is, in this programme

Not a villain, not a constant of nature, and not absent.

> **π is the exchange rate for using Gaussians.** It appears the moment you
> regularise, and it cancels the moment you take the ratio the regularisation was
> built to produce. The results that survive audit are the ones it never touched
> — and now we know why they were available to be found: **the object never had it.**

That is the π-rejection, arrived at from inside the arithmetic rather than asserted:
π is what the smoothing charges, and the thing being smoothed does not contain it.

## 7. Status

| claim | status |
|---|---|
| the FE prefactor is independent of the marking `j` | **PROVED** — inspection of the functional equation |
| therefore π cancels in `R(d,j)` for every d, j | **PROVED** |
| `R(3,1)` computed π-free converges to the 50-digit value | **VERIFIED**, 8 digits at N=300 |
| denominator matches 028's `Z_PPP(2) = 16.5323159598` | **VERIFIED** |
| the identity `R = Z*_APP(2)/Z_PPP(2)` | **ALREADY IN 028 §5** — the consequence is new |
| individual `Z(−1/2)` values remain π-laden | **TRUE** — the prefactor does not cancel there |
| `c₁`, `c₂` are coefficients of the method's expansion | **ESTABLISHED** — the nome is Gaussian-derived |
| R is simple / algebraic / in ℚ[√2] | **NO** — 044's bounded nulls unaffected |
| the π-free form is practical | **NO** — `M^(−1/2)` convergence; the Gaussian road is faster |

## Attribution

The question is Ash's, and it is the founding one. The identity in §2 is 028's. The
cancellation argument, its generality, and §§3–4 are this seat's, run because Ash
asked the question directly instead of accepting 062's "π is a marker" as the end of
it. 062 said π marks where we smoothed. **This says what it marks is a road, and the
place it leads has no π in it.**
