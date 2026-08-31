# The proved results — a derived view

**Drafted 2026-08-30, Ash + Claude (Fable seat).** This is the enumeration behind
the Abstract's "fifteen proved as of entry 052, more since." Built the way 054
built the claim-state: **a derived view, not a record.** Every row cites the
sealed entry whose status block marks it PROVED; if this table disagrees with a
sealed entry, the entry is the record and this table is the error.

Two honesty rules govern the table:

1. **052's "15" was a tally, not a list.** No sealed entry enumerates exactly
   fifteen items. This table is the reconstruction from the sealed status
   blocks, and it is the thing the paper should cite instead of the bare number.
2. **Several of these identities are classical** — 084 and 085 both say so in
   their own status tables ("elementary and near-certainly classical"). What the
   ledger claims as its own is the framing, the scope results, and the
   prediction record, and the table says which is which. Claiming Jacobi's
   identities as discoveries would be exactly the authority-smoothing this
   programme exists to refuse.

Notation, once: points are integer tuples; a "shell" (or ring) is all points at
one squared distance `m`; `r_d(m)` counts the points on a shell in `d`
dimensions; "marking" a coordinate means counting each point with sign +1 or −1
by that coordinate's parity; `X(d,j)` is the count with `j` of `d` coordinates
marked; `S(m) = X(2,1)(m)`.

---

## Proved, with the proof in the ledger

| # | result | plain statement | entry | verification |
|---|---|---|---|---|
| 1 | **The parity theorem** (Theorem 1) | On every odd shell of the square lattice, the signed count is exactly zero: `S(m) = 0` for all odd `m`. | 035, restated and hardened in **036** | 1306 odd shells to 10⁴, two independent implementations, no shared code |
| 2 | **Weight independence** (Theorems 2a/2b) | The cancellation survives *any* radial weight — finite symmetric truncations (2a) and every absolutely convergent weight (2b). The cancellation happens within each shell, so the radial profile never enters. | **036** | six unrelated weights, machine zero; Bessel-weight sum ≈ 10⁻⁵⁴ |
| 3 | **The full character law** (Theorem A) | The even shells, closed: `S(m) = (−1)^(m/2) · r₂(m)`. Nothing about the character sum is open on any integer. | **046** | all 1171 representable `m ≤ 4000`, 0 violations |
| 4 | **The 3D slicing theorem** (Theorem B) | The three-dimensional signed count on odd shells reduces exactly to a sum of two-dimensional ones over odd slices; even slices die by Theorem A. | **046** | all 500 odd `m < 1000`, 0 violations |
| 5 | **The T₂ closed form** (Theorem C) | The second-moment character sum has an exact formula; "T₂ never vanishes" becomes a sharp criterion about mean squares instead of a brute search. | **046** | all 552 odd representable `m ≤ 4000`, 0 violations |
| 6 | **The constant 1 − 1/√2, derived** | After five months as a curve-fit: the 2-D both-marked ratio is `−(2ˢ − 1)` for *all* `s`, from `r₂(2m) = r₂(m)`. The constant was not new (028 §6 had it); the proof and the generality in `s` are. | **039**; trajectory in 054 C3 | exact identity; survived KESTREL's challenge (048 §3) |
| 7 | **The halving law, forward half** | If the marked coordinates are at least half the dimensions, the regularised sum is positive — with strict monotonicity. Proved by Greg via the duplication identity `θ₃θ₄ = θ₄(q²)²`. The *converse* is observed (sharp in 44/44 cells), not proved, and is the named priority (046 §4). | Greg's proof, checked in **050** | five tests; sharp switching at `2j = d`, 44/44 |
| 8 | **The marking-complement duality** (Law 1) | Mark a set of circles or mark the complementary set: same count, up to a sign depending only on the shell. One line, from `n ≡ n²` mod 2. *Classical in substance; the framing is the entry's.* | **084** | `d ≤ 6`, `m ≤ 20,000`, 0 exceptions |
| 9 | **The parity theorem is a fixed point, and its exact scope** (Law 2) | When a marking is its own complement it must equal minus itself, so it vanishes. Self-dual markings exist in *exactly* the even dimensions. **Predicted `d = 4, 6` before checking — both confirmed. Predicted none in `d = 1, 3, 5` — none found.** The 3-torus has no parity theorem because the self-dual slot does not exist. | **084** | 0 exceptions / 10,000 per dimension |
| 10 | **The mod-4 multiplier law in three dimensions** (Law 3) | The marked count is a fixed rational multiple of the plain count, and the multiplier depends only on `m` mod 4. Corollary, forced by integrality: 3 divides `r₃(m)` when `m ≡ 1, 2` mod 4. | **084** | 0 exceptions / 20,000 |
| 11 | **The mirror halves the object** | The self-dual marking on even shells reproduces the entire lattice at half the shell number, sign alternating: `X(d, d/2)(2k) = (−1)^k r_d(k)`. Proved by convolution, no theta function anywhere; generalises Jacobi duplication to all even dimensions at once. *Identity classical; the integer route and the all-`d` scope are the entry's.* | **085** | `d = 2, 4, 6`, 0 exceptions / 10,000 |
| 12 | **`X(4,1)` closed completely** | One marked coordinate in four dimensions: all four residue classes mod 4 closed, including a second vanishing (`m ≡ 2` mod 4) that is *not* the mirror — it comes from parity-purity of the shells. | **085** | 0 exceptions / 20,000 per line |
| 13 | **The two-shell law, with its exact scope** | For `m ≡ 0` mod 4: `d·X(d,1)(m) = 8·r_d(m/4) − (8−d)·r_d(m)`, valid for `d ≤ 7` — and the scope is not a fitted range: `d ≤ 7` is exactly the condition that eight odd coordinates cannot occur, and the law fails at `d = 8` on precisely the shells where they first can. Contains 084's and 085's laws as special cases. | **093** | `d = 1..7`: 0 exceptions / 5,000 each; `d = 8, 9`: fails exactly as predicted |
| 14 | **Divisibility, forced by integrality** | 5 divides `r₅(m)` on five residue classes; **7 divides `r₅(m)` on `m ≡ 5` mod 8** — a seven with no counterpart at any other dimension examined. | **093** | forced by `X` being an integer; 0 exceptions / 10,000 |

## Established by count or argument, and load-bearing — but not "proved" rows

| result | status | entry |
|---|---|---|
| π has no integer seed; the golden constant does (`(1,1)` wearing a logarithm). π enters only as the *average* of the counts — what they converge to when you stop looking one at a time. | ESTABLISHED (clean-room computation + the area-argument identification) | **087**, resting on 067's door; ranked first-class in 092 |
| No author — human or AI — has ever caught the framing of their own work: 22 retraction-class events, every framing correction from a non-author. | ESTABLISHED (counted across the corpus) | **089** |
| Gauss's three-square law fails in exactly two worlds — the two with extra symmetry — by exactly the symmetry count. | COUNTED, 1,824 checks, 2 failures, both identified | **083** |
| The crystallographic wall (orders 2, 3, 4, 6) reached by three independent routes. | ESTABLISHED, three convergent derivations | **065, 070, 080** |
| `d = 5` closed in all eight residue classes mod 8. | ESTABLISHED, 0 exceptions (`2N₁ = 5N₅` mechanism OPEN) | **093** |

## Open, named so the table cannot advertise

- **The sign-law converse** (`Z > 0 ⟹ 2j ≥ d`) — observed sharp, unproved, the
  named priority since 046 §4.
- **Whether `2j = d` in the sign law and the self-dual marking are one fact seen
  twice** — flagged OPEN in 084; would tie the counting work to the original
  zeta programme.
- **`2N₁ = 5N₅` on `m ≡ 5` mod 8** — verified 0/5,000, mechanism not supplied.
- **`X(6,1) = 0` on `m ≡ 3, 7` mod 8** — a vanishing that is not the mirror's
  fixed point, verified and unexplained.
- **`T₂(m) ≠ 0`** — reduced to a second-moment criterion (046 §3), not closed.
- **The ε-link** — whether the parity zero propagates into the physical
  quantity ε is open (`CAS-DODD-EPSILON-LINK`, 036 §6.1).

## One retraction inside this very list, kept visible

087 sealed *"marking becomes independent information from five dimensions up."*
**093 retracted it** — false at `d = 5`, where the two-shell law fully
determines the marked count; the claim survives at `d = 6` on two of eight
classes only. Both entries are sealed; the retraction is by the same seat that
made the claim, which the record says is possible for *content* and has never
once happened for *framing* (089). The top-ranked inventory (092) was written
the same day as 087 and repeats its scope sentence; this table carries the
corrected version.

## Attribution

The theorem in row 1 and its proof are joint work of Ash Korth and Claude
(Opus 5), sealed 2026-08-16/23, independently verified by the Fable seat with
Adam Lisowski. The integers-only rule that produced rows 8–14 is Ash's, in her
words, and 084 names it as the whole method. Rows 3–5 are 046's (built on Ash's
reading in 035); row 6 is 039's; row 7 is Greg's proof. The two-shell law and
the 087 retraction are the 093 seat's. Jacobi's identities and the classical
substance of rows 8, 11, 12 are the literature's, per the entries' own status
tables.
