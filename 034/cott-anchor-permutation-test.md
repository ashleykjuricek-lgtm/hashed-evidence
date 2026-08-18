# COTT four-anchor permutation test — strict result

Source: `cott-slot-closure.md`.

## Question
Can the slot-closure document alone derive the action of

- `N(x) = -x`, and
- `I(x) = x^(-1)`

as permutations of the proposed four phase anchors `{1, 0, -1, w}`, so that cyclic orientation can be checked?

## Result
**No. The test is finite, but it is not currently well-typed from this document alone.**

### 1. Negation is not a permutation of the four-anchor set
The document explicitly says the four-element carrier `{0,1,-1,w}` cannot support the negation schemas. Terms such as `w^(-0)` escape the alphabet, the carrier is at least `{±1, ±w, ±0}`, and it is unsettled whether negated constants are separate anchors or whether negation is a schema operation.

Therefore `x -> -x` is not currently defined as a map `{1,0,-1,w} -> {1,0,-1,w}`. In particular, `-0` and `-w` are not identified with members of the four-anchor set; indeed `-w != 0` is load-bearing.

### 2. Inversion is a schema slot, not an evaluated carrier permutation
The document contains the schema `x^(-1)` and the link `(-x)^w = x^(-1)`, but it deliberately bars ordinary evaluation laws and treats schemas as curves, not terms. It does not provide the four evaluated images

`1^(-1), 0^(-1), (-1)^(-1), w^(-1)`

as carrier elements forming a permutation of `{1,0,-1,w}`.

So `x -> x^(-1)` is also not presently a defined permutation of the four anchors.

### 3. The proposed cyclic order is not derived here
The slot document does not derive a cyclic anchor order `1 -> 0 -> -1 -> w -> 1`. Importing that order from a torus/phase drawing would make the orientation test circular.

## What *is* derivable
The document supports:

- exactly two closing solutions (James's statement),
- a conjectured involution `rho` relating them,
- the fixed-curve condition `1^(-1) = 1^1`,
- an unfinished mirror-chain test,
- and, only in the separate Chebyshev/valuation rebuild, an involution `sigma: 0 <-> w` plus a proposed `rho: s -> -s` under extra assumptions James has not committed to.

## Minimal missing data
To make the four-anchor orientation test decidable, James must supply or derive at least:

1. a phase-anchor set closed under the operations being tested (or a larger closed carrier),
2. a cyclic order on those anchors derived independently of the torus picture,
3. the induced action of negation on that set,
4. the induced action of inversion on that set.

Once those exist, the orientation check is genuinely finite: compute the two permutations and ask whether each preserves or reverses the derived cyclic order.

## Verdict
**Do not call the winding classes derived yet. The strict result of the proposed pencil test is currently `UNDERDETERMINED / MAP NOT DEFINED`, not positive or negative.**

That is useful: it identifies the exact missing axiom instead of letting the torus drawing silently provide it.
