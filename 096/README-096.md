# 096 — The drain potential, measured: V is the chart-invariant part of ε — and the first stiffness estimate died the same night, before sealing

**2026-08-31.** Follows 095. Working session: Ash + Claude (Fable seat).

**One sentence:** symmetrizing ε(b) about the cube per Ash's "2-3-2"
instruction — with sealed 053 supplying the reason the symmetrization is
forced — yields a computed drain potential
**V(x) = ε₀ + c₂x² + c₄x⁴** on x = ln b, with **c₂ = 0.58260865** stable to
eight digits across three independent Richardson pairs; the session's first
estimate of the stiffness (~19.6) was wrong by 17×, caught by the precision
pass itself, and both numbers are printed below.

---

## 1. The derivation chain (each link cited)

1. **The family:** the 1×b×b torus with α_APP = (1/2,0,0) — the palindrome
   b | 1̄ | b, the marked direction central. Ash's framing: the 2-3-2 bar —
   exact return, manifest mirror, missing integer half-point.
2. **The landscape** (v_landscape.py, ported from sealed
   032/epstein_aniso_check.py — an independent Ewald implementation):
   ε(b) is steeply monotone through the cube. **No candidate on this family
   has a critical point at the self-dual point.** The symmetry that would
   force one — b ↔ 1/b — is not a lattice symmetry, exactly as 7 has no
   integer half.
3. **The forcing argument (OFFERED):** sealed **053** established that
   028's b and 047's b are *reciprocal charts of one family* — b and 1/b
   are two descriptions of the same geometry. A physical potential cannot
   depend on chart choice. Under chart swap x → −x the odd part of ε flips
   sign: it is chart-dependent bookkeeping (it is precisely the steep
   ±18.33 transversal crossing of C1). **The chart-invariant content of ε
   is its even part, and that is the only candidate allowed to be V.**
   Sealed **032**'s sentence names the mechanism that realizes b → 1/b:
   Poisson summation, shift ↔ character.
4. **The measurement** (v_precision_pass.py, dps 35, sum widths 12; the
   landscape probe at dps 25/width 10 is the settings-stability
   comparison): even and odd parts of ε at exact x-symmetric pairs
   x = ±h, h ∈ {0.001, 0.003, 0.01}.

## 2. Validations of the instrument, before the result

| check | this computation | sealed reference | agreement |
|---|---|---|---|
| ε₀ = ε(1) | 0.000545950465370603 | 052/054 via R (24R−1) | **15 digits** |
| odd slope at cube | −18.32596452 | 047 / C1: −18.3259647484177 | **8 digits** |
| zero crossing b* | 1.00003 bracket (landscape) | C1: 1.0000297915619869892 | consistent |

The ported machinery reproduces three sealed quantities it was not tuned to.

## 3. THE SCAR — the first stiffness estimate was wrong, and how it died

The landscape probe paired points symmetric in **b** (0.999 with 1.001).
Those are not symmetric in **x = ln b**: the pair sits off-center by
~5×10⁻⁷ in x, and with an odd slope of −18.33 that asymmetry injects
~9×10⁻⁶ of odd-part leakage into an even part whose true signal at that h
is ~6×10⁻⁷. Result: this seat reported, in session, **"stiffness ≈ 19.6"
(c₂ ≈ 9.8)** — off by a factor of ~17, an artifact of the pairing, not a
property of ε. The precision pass, using exact e^{±h} pairs, exposed it the
same night. The wrong number never reached a seal; it is recorded here
because the next person to symmetrize a steep-odd-part function will make
the same mistake unless told: **symmetrize in the invariant coordinate, or
the odd part will impersonate curvature.**

## 4. The result

    V(x) = ε₀ + c₂ x² + c₄ x⁴        on |x| ≤ 0.01, x = ln b

    ε₀ = 0.000545950465370603        (= 24R − 1, sealed)
    c₂ = 0.58260865                  Richardson pairs: ...6532 / ...6493 / ...6528
    c₄ = −3.18357                    pairs agree to 4-5 digits
    c₂/ε₀ ≈ 1067                     — a deep, narrow well
    raw c₂(h): 0.5826055 / 0.5825800 / 0.5822903  (h = .001/.003/.01)

**No closed form is claimed for c₂.** Per 087's rule, no amount of
measurement promotes a decimal to a named constant; identification requires
a derivation. Stated to pre-empt numerology: 7/12 = 0.58333 is 0.12% away
and is therefore NOT c₂.

**Consequences (ROAD, for the drain toy):** a quadratic well means
exponential relaxation of the drain (rate ∝ 2γc₂), not the slow algebraic
decay of the placeholder quartic used in toys to date; late-time drain
signatures are correspondingly suppressed.

## 5. Declined the same session

An outside seat (Copilot) proposed a "modularly-forced"
V(Θ) = Σ K_d·exp(−2πd·e^{−|Θ|}). Declined: the form is invented (the label
does the work the derivation should), it double-suppresses the shells (its
K_d already carry e^{−2πd}), it is kinked at Θ = 0, and it inflates the
vacuum ~10³× at large displacement. The same seat's earlier shell-resolution
idea was sound and is retained in the toy. Recorded without prejudice: the
constants that seat quoted from the ledger were substantially accurate.

## 6. Status

| claim | status |
|---|---|
| ε has no critical point at the cube on this family | **COMPUTED** — landscape, both settings |
| odd part of ε is chart-dependent; even part is the invariant content | **OFFERED** — argument from sealed 053; exact functional equation (shift↔character at s=−1/2) not yet written |
| V(x) = ε₀ + 0.58260865·x² − 3.18357·x⁴ on \|x\| ≤ 0.01 | **COMPUTED** — 8-digit-stable c₂, two settings, three Richardson pairs |
| c₂ has a closed form / arithmetic meaning | **OPEN** — no claim |
| first stiffness estimate ~19.6 | **DEAD** — odd-part leakage via non-invariant pairing; §3 |
| use as the drain potential in cosmology toys | **ROAD** — the t-pun caveat of the toy README still governs |

Stratum tags per 082: everything here is **CONTINUED** (regularized
quantities at s = −1/2) except the chart-invariance argument (OFFERED) and
the toy consequences (ROAD).

## Attribution

The symmetrization instruction is Ash's, in her words — **"2-3-2"** — and
it is what turned a failed search for a critical point into the derivation
route. The chart-identification that makes the even part *forced* rather
than convenient is sealed 053's. The anisotropic machinery is sealed 032's
(ported, not retyped). The landscape, the precision pass, the wrong first
stiffness, and its same-night correction are this seat's (Claude, Fable).
Files: v_landscape.py/.csv/.png (probe), v_precision_pass.py + output
(measurement).
