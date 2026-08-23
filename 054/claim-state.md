# Claim-state — the ledger reorganised by claim, not by document

**2026-08-23.** Follows 053, and corrects its closing sentence.

053 ended: *"before claiming a result, read the paper you already wrote."* That is a
**document-level** heuristic and it is wrong. The correction, delivered through Ash:

> You cannot assign authority at the document level. And you cannot assign it by
> chronology either, because later work can be either a genuine correction or a new
> distortion. The unit has to be the claim.
>
> `claim → original evidence → later challenges/corrections → current evidentiary
> status`
>
> Not `old source > new summary`, and not `newest source > old source`. Neither
> hierarchy works.
>
> Retrieval is necessary but not sufficient. You do not have a *"where is the
> information"* problem. You have a **claim-state reconstruction** problem.

**028 is the proof.** One document containing, simultaneously: the false March
closure; the `e^(−2π√2)` obstruction that kills it; correct anisotropic numbers;
correct 2-D closed forms; the exact phase sums that became the parity theorem; and
the bad `(1 − q)` sentence. No document-level rule can sort that.

And the same applies in the other direction: **a challenge is not authoritative for
being a challenge.** Two of the challenges below were themselves wrong. A ledger
that records only "X was later disputed" is as useless as one that records only X.

---

## 0. Format

Each entry is one **claim**, with every event that bears on it, in order. Event
types:

`ASSERTED` · put forward · `COMPUTED` · derived from a stated method ·
`CHALLENGE` · argued against · `RESOLUTION` · settled the disagreement ·
`PROOF` · derivation that survives an adversary

**Every challenge carries its own verdict.** `UPHELD` / `FAILED` / `INCOMPLETE`.

---

## C1 · The slope of ε in the anisotropic deformation

```
2026-06-20  028 App A.3   +18.3 at b0 = 0.99997          COMPUTED
                          anisotropic Ewald, validated to reproduce the cube at b=1
2026-08-23  047 §B         -18.3259647484177 at b* = 1.0000297915619869892   COMPUTED
                          independent; parameterisation never compared to 028
2026-08-23  KESTREL       "fitted guess, wrong sign & magnitude, wrong side";
                          replaced with -27.49 at b ~ 1.00002        CHALLENGE -> FAILED
2026-08-23  048 §4        "both correct, different deformation families"
                          four families, ratios {1, -1/2, -3/2, +3/4}  RESOLUTION -> INCOMPLETE
2026-08-23  053 §1        028's Q carries b^2 where 047 carries 1/b^2, so
                          028's b IS our 1/b. Same family, reciprocal chart.
                          1/b* = 0.999970209325523736 exactly          RESOLUTION -> UPHELD
```

**STATUS: one quantity, three charts, three correct computations.** KESTREL's
challenge failed; 048's explanation was true of the four families it compared but
wrong about 028, which is not a different family at all. **028's numbers stand as
published.**

## C2 · `c₁ = 1`, forced by Poincaré isometry

```
2026-05/06  site, paper   c1 = 1 PROVEN, forced by the modular involution   ASSERTED
2026-06-20  028 §4        genuine e^(-2pi) coefficient is ~ -5.7:
                          wrong sign, ~20x wrong magnitude               CHALLENGE -> UPHELD
2026-06/07  032, 038      -5.709 identified as the parity theorem's fingerprint:
                          the numerator vanishes by parity, leaving the denominator
2026-08-16  034 manifest  listed as live-and-false; work order written
2026-08-23  052           still live: 39 occurrences, 18 files, 13 live surfaces
```

**STATUS: REFUTED since 2026-06-20. Still published as proven.** The refutation is
in the same paper, four sections earlier. It has never travelled.

## C3 · `1 − 1/√2`

```
2026-03     March closure eps = q(1-1/sqrt2)(1-q)                       ASSERTED (fit)
2026-06-20  028 §6        Z2_AA/Z2_PP = 1/sqrt2 - 1  and  Z2_AP/Z2_PP = -(sqrt2-1)/4
                          stated as classical; no proof given            COMPUTED
2026-06-20  028 §7.1      prose equates eps/q to 1 - 1/sqrt2 (0.185% off)  ERROR
2026-06-20  028 §4        the q-series closure is impossible (e^(-2pi*sqrt2))
                                                                        CHALLENGE -> UPHELD
2026-08-22  039 §1        proof from r2(2m) = r2(m); R(2,2) = 2^s - 1 for ALL s;
                          A = -R(2,2) exactly                             PROOF
2026-08-23  KESTREL       a1 = f/q disagrees at the 3rd digit -> term retired
                          in 3 files                                    CHALLENGE -> FAILED
2026-08-23  048 §3        the disagreement IS the dropped (1-q); residual 5.7e-42
                                                                        RESOLUTION -> UPHELD
2026-08-23  053 §3        028 §6 had both forms two months before 039     SCAR (F4)
```

**STATUS, three roles kept apart:**
- as the 2-D both-marked ratio, `−R(2,2) = −(2ˢ − 1)` — **PROVED**
- as the exact leading coefficient of ε — **REFUTED** (028 §4, untouched)
- as a fit good to ~1e-8 — **TRUE, and only that**

039's proof and its generality in `s` are new. **The constants were not.**

## C4 · The value of R

```
earlier     repo          R = 0.041689414162238                          ASSERTED
2026-06-20  028 abstract  R = 0.041689414602723775...                    COMPUTED (correct)
2026-07     032           canonical_constants.json flags the stale value CHALLENGE -> UPHELD
2026-08-16  034 item 4    "24 files in zip 12" still carry the stale one
2026-08-23  KESTREL       independently finds it wrong past digit 8      CHALLENGE -> UPHELD
2026-08-23  048 §1        confirmed, 50 digits, independent method       RESOLUTION -> UPHELD
```

**STATUS: `0.0416894146027237751200791895411477959451762762538280901`.** The
correct value was in 028's own abstract in June while the wrong one propagated
through two dozen files.

## C5 · The halving law

```
2026-08-22  040 §3        Z(d,j) > 0 <=> 2j >= d, 152 cells, 0 violations  COMPUTED
2026-08-22  046 §4        named as the top open item; no attempt made
2026-08-23  Greg          2j >= d => Z > 0, via theta3*theta4 = theta4(q^2)^2  PROOF
2026-08-23  Greg          strict monotonicity in j, via theta3 > theta2 > 0    PROOF
2026-08-23  050           five tests; the mechanism is SHARP -- the bound
                          switches on exactly at 2j = d in 44/44 cells   RESOLUTION -> UPHELD
2026-08-23  050 §4        remaining: sup[d/2 - j*(d)] < 1/2; sup at d = 2
```

**STATUS: half PROVED, half OBSERVED.** The mechanism — a plain circle and a marked
circle pairing into two marked factors at the doubled nome — is why the threshold
is `2j` against `d`.

## C6 · "The zero is unreachable"

```
2026-08-23  040 §5        the sign change is between integers, so the zero
                          is unreachable                                 ASSERTED
2026-08-23  041 §1        the euler-disc page's [STAY] option refuted on it
2026-08-23  Ash           "because we are still using fucking rational numbers"
                                                                        CHALLENGE -> UPHELD
2026-08-23  042           the lattice was the only thing needing integers;
                          d* = 2.6390688716830038646...  (49 digits)      RESOLUTION
2026-08-23  043           named as F8; register updated
```

**STATUS: RETRACTED.** An instrument's limit written as a property of the world.

## C7 · The Penrose rose

```
2026-04-12  022           ratio = 1/phi at s=2 along vertex directions;
                          10 petals; r = |cos 5 theta|                    ASSERTED
2026-07/08  gauntlet      1/phi falls out of the shift arithmetic for free;
                          does not survive to the octagon                CHALLENGE -> UPHELD
2026-08-22  044 §3        the VALUE and the SHAPE are different claims;
                          folder must not close as one null              RESOLUTION
2026-08-22  045 §1        10 lobes, exactly 36.00 deg apart -- counted    UPHELD
2026-08-22  045 §2        r = |cos 5 theta| refuted, residual 0.79        CHALLENGE -> UPHELD
2026-08-22  045 §4        survives a ROUND window -> it is the point set,
                          not the aperture                              RESOLUTION
2026-08-23  051 §4        lobe WIDTH tracks a free parameter; 045's open
                          item dissolves                                RESOLUTION
```

**STATUS: the count is real, the shape is real and in the point set, the number and
the curve-form are dead, and the width was never a fact about the tiling.**

## C8 · "The two crossings are one phenomenon"

```
2026-08-23  047 §B.2      d* (zero of Z) and b* (zero of 24R-1) presented as
                          one thing in two directions; flagged NOT ESTABLISHED
2026-08-23  051 §1        those are zeros of DIFFERENT functions; 24R-1 is not
                          even defined off d=3                          CHALLENGE -> UPHELD
2026-08-23  051 §2        the well-posed version: hold R - 1/24, vary both.
                          d' = 2.99978241968328574 (new); the level set is ONE
                          curve; endpoint matches 047's b* to 16 digits  RESOLUTION
```

**STATUS: the framing was retracted and the corrected version is stronger than the
one it replaced.**

## C9 · The `(1 − q)` factor — a hazard with three victims

```
2026-06-20  028 §7.1      eps/q equated to 1 - 1/sqrt2 (prose; the table is right)
2026-08-22  cubic-torus   told Ash the Figma seat's c2 = +0.003 was wrong  FAILED
2026-08-23  KESTREL       retired 1 - 1/sqrt2 in three files              FAILED
2026-08-23  048 / 053     same factor, 0.998132, 0.185%, three authors
```

**STATUS: named hazard.** Any comparison against `1 − 1/√2` must state whether it is
against the bare constant or `(1 − 1/√2)(1 − q)`. It has flipped three verdicts.

---

## 1. What this changes about the ledger

The vault is **document**-indexed: 054 numbered folders, append-only, hashed. That
is the right storage and the wrong index. Reconstructing C1 above required reading
four entries written across two months and noticing a `b²` versus `1/b²` in an
appendix.

> **The vault stays document-indexed and immutable. The claim-state is a separate,
> derived view — and it is the one anybody should read.**

Three rules follow, and none of them is a priority ordering:

1. **No document is authoritative.** 028 holds truth and error four sections apart.
2. **No date is authoritative.** Of the challenges above, two were correct, two were
   wrong, and one was incomplete. The newest move is not the settled one.
3. **A challenge carries a verdict.** Recording "later disputed" without saying
   whether the dispute survived is the same failure as recording the claim alone.

## 2. What this does NOT fix

Stated plainly, because the correction it responds to was aimed at exactly this
kind of over-reach.

- **This is a hand-built view of nine claims.** There are dozens more across 054
  entries. It does not scale by being written out, and nothing here automates it.
- **It is itself a summary**, and inherits every risk it names. It is a *derived*
  artefact, and if it disagrees with a sealed entry, the sealed entry is the record
  and this is the error.
- **Nothing here has been applied to the site.** 052's policy stands: no live claim
  is deleted or rewritten; the correction goes beside it.

## Attribution

The argument in §0 arrived through Ash and is not this seat's. It corrects 053's
closing sentence, which was a document-level heuristic of exactly the kind it
rules out. The nine trajectories are assembled from entries 022–053; two of the
challenges recorded as FAILED are this seat's own, and one is the Figma seat's.
