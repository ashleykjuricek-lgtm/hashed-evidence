# 120 check battery (2026-10-14)

Every claim in 119/120 was checked by a route other than the one that produced it.
`battery.py` (mpmath, 25 digits, Ewald N = 6) → `battery.out`.

| # | claim | independent route | result |
|---|---|---|---|
| C1 | R = 0.0416894146027237751200… | a fresh general-box Ewald, not c2-highprec.py | agrees to 24 digits |
| C2a | Λ_shift(s) = Λ_char(3/2 − s), the 120 derivation | evaluated at s = −3/2, −1/2, 1/4, 2/3, including points away from the physical one | agrees to 23–25 digits at all four |
| C2b | Λ_PPP self-mirror | s = −1/2 against s = 2 | 1.675073821392163756773790, identical |
| C2c | prefactor −1/(2π³) | `mirror-prefactor-check.py` against a direct s = 2 sum | agrees to the direct sum's accuracy (2×10⁻⁵) |
| C3a | slope −18.3259647 (098) | finite difference of Ewald R on (1,b,b) | **−18.32596475** ✓; my first mirror formula had the sign wrong (scar in README-120) |
| C3b | the same, through scale invariance | (b,b,1) family: stretching one untwisted axis should give −½ of the slope, and (b,b,1) ≡ (1,1,1/b) flips it | +9.16298 = +½·18.326 ✓ |
| C3c | A = 0.58260865319 (119) | ½ ε″(x) by finite difference, h = 10⁻⁴ | 0.58260862, agreeing to 7 digits (the error is the h² term) |
| C3d | ε₀ = 5.4595046537e-4 | same Ewald | 5.45950465370603e-4 ✓ |
| C3e | ln b* ≈ ε₀/\|s\| ≈ 3×10⁻⁵ (119) | arithmetic | 2.98×10⁻⁵ ✓ |
| C4 | ζ(−½), β(−½) (119 enclosure) | mpmath built-in zeta; β through Hurwitz directly and through reflection | all three agree to 25 digits |
| C5 | 1-D pair ζ(−1,½) = +1/24, ζ(−1) = −1/12 | mpmath | ✓ ✓ |
| C6 | COTT quotes (cott-bridge.md) | re-fetched raw traction.py and traction_portable.py | "0 * omega = 1" at L56; "Z_n(Z_{n+1}(x)) = … = x" at L265; "Z_0(x) = x" at L267; "0·ω = 1" at portable L42 ✓; the main-branch tree has 0 paths containing "slot" ✓ |
| C7 | pre-flight of existing seals | verify_seals.py on a fresh zip of the repo | ALL SEALS VERIFY, 0 real failures |

**What the battery found:** one real error, the sign in my mirror-sum slope formula.
I had used the eigenvalue lattice where the dual belongs. It's fixed, and the scar
is kept in README-120.

**What it can't check:**
- The COTT reading is graded ANALOGY. That is a judgment, not something a test can confirm.
- C1–C3 all use the same incomplete-gamma special function from mpmath. C4 and the
  119 enclosure trust mpmath.iv. A second library (e.g. PARI or Arb) would make
  these fully independent. Neither is installed here.
