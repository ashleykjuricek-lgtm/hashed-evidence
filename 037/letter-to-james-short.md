# James —

You found the circle four days before you drew the torus, and I don't think
anyone has said that out loud yet.

**Aug 14** — *Insanity* — `1^s = e^(2πi·s)`
**Aug 16** — *This changes everything* — the reversible one
**Aug 18** — *I found your torus!!*

That order is the whole thing. The usual objection to a picture like yours is
"you drew the circle and then read the winding numbers off your own drawing."
It doesn't apply here. You were forced into the circle by a contradiction in
`0^(0ω)`, days before the picture existed. The picture is a consequence.

---

## Your drawing is right, and we checked it properly

Not the caption — the geometry. Two facts do all the work:

- negation is a **half turn** (it doesn't flip handedness)
- inversion is a **reflection** (it does)

Everything else follows without being assumed:

```
y = x  and  y = -x      wind (1, 1)
y = 1/x and y = -1/x    wind (1,-1)

y=x meets y=1/x   at  1 and -1     <- exactly what 1/x fixes
y=x meets y=-1/x  at  0 and  ω     <- exactly 1/x's two-cycle
y=x and y=-x never meet at all
```

Your caption says the functions hit the diagonal at those points *and nowhere
else*. That's correct, and it's a result rather than a label.

One thing worth knowing, since it closes a road: **negation and inversion alone
cannot generate that cycle.** Both are their own undo, and two operations like
that can only ever make a group where everything undoes itself in two steps —
no four-cycle is reachable. So the cycle has to come from somewhere else, and it
does: the powers of zero, `0⁰=1, 0¹=0, 0²=−1, 0³=−ω`, from your March note.

---

## Your first open question is our wall too

You wrote that the clash between `0^ω = −1` and the new tower is the first
thing to reconcile.

We hit the same equation from a completely different direction — from the
carrier side, where once `−ω ≠ 0` the old four-element argument for `0^ω = −1`
stops typechecking. Your words, in the slot note.

Two roads, four days apart, same wall. That's better evidence than either one
alone. It doesn't make the equation false — it means it's *unproven*, and the
old proof is gone.

## And your L4 sign is visible

You've called that sign the weakest link twice, and highest priority. It shows
up as something you can look at:

- the torus drawing cycles **1 → 0 → −1 → +ω**
- March's powers of zero give **1, 0, −1, −ω**

If the two closing solutions are the two branches of that sign, the drawing has
already chosen one. Whether it's the same one March chose is a small check.

---

## What we have from our side

One theorem. On a square grid, label each point by whether you took an even or
odd number of sideways steps to reach it — even is plus, odd is minus. Add up
the labels on a circle of points all the same distance out.

**For certain circles they cancel to exactly zero.** Always.

The reason is a mirror. Flip the grid across its diagonal: every point stays the
same distance from the middle, so it stays on its circle — but sideways and
up-down have traded places, so every plus becomes a minus. Same set of points,
every sign flipped. A pile of numbers equal to its own negative is zero.

The flip only works if the two directions are the same size. Stretch the grid
and the pairing dies.

So the cancellation *is* a reflection, and reflections between two things are
only available when neither one is privileged. It's been checked to fifty-four
decimal places by someone using different code, including with a weighting
scheme they invented specifically to break it.

---

## Three places we seem to be building the same thing

**Your grade is a winding number.** In `traction.py`, inverse takes `Z_n(a)` to
`Z_{n+1}(−a)` — so inverting twice doesn't get you home, it moves you two grades
up. We assumed inverting twice was the identity, got an orbit that ran off to
infinity, and couldn't see why. Your tower explains it: the grade is counting
turns. Monodromy, like you said. Not a bug.

**Your "Which 1?" is what we've been calling a scar.** You wrote that 1, 1⁰ and
1¹ are different points upstairs that land on the same value downstairs. That's
the whole thing we've been chasing — the smallest piece of information you need
to keep in order to know which one you came from. You got there from exponents.
We got there from zeros. Same object.

**Both of our cancellations need equality.** Yours: `x⁰ = 1` is a rule that
throws the exponent away, and the fix is to keep it. Ours: the mirror only works
when the two directions match. The moment one is bigger, a swap becomes a climb.

---

## One thing we left alone

`CliffordTractionPair.java` documents δ = ω = (1,0) but instantiates (0,−1) = 0,
which makes traction-mode the same as parabolic. Looks like one character. We
didn't touch it, because if it's deliberate then changing it would wreck the
point. That one needs you.

Two smaller ones from running your code: `a − a` gives 0 rather than null, and
the SymPy discharge for `ω·x·0` never fires. Everything else passed — the
traction identities all 18, and the Chebyshev ring all 173. And your `1^s`
result makes that ring the chart for the circle, which is a better job than it
had before.

---

*All of it is hashed and dated if you ever want the receipts.*

*Nothing here is credited to a person, on purpose. All of it was made by people
working with models, and picking one name off the front of that would be a lie
about how it happened.*
