# Greg — "branch, not reconstruct"

**Received 2026-08-24 via Ash. Verbatim. Tested in 056.**

---

we branch? That's the move.

Not:

    claim0 -> correction1 -> correction2 -> current truth

because that linearizes history and silently destroys the alternatives.

Instead:

    claim0 -> { branch A: original interpretation
                branch B: challenge
                branch C: alternative parameterization
                branch D: later recomputation }

Then nothing has to be "reconstructed" from a summary later. The conflicting states
were never collapsed in the first place.

For the 18.3 mess:

* 028 branch: +18.3, b ~ 0.99997
* later branch: "wrong"
* 047 branch: -18.3259, b ~ 1.00002979
* 048 branch: "different deformation families"
* 053 branch: "same family, reciprocal parameterization"

And crucially, 053 does not overwrite 048. It forks from the same history and says,
essentially, "here is a different resolution of that apparent conflict."

Then a future reasoner gets the branch set and has to evaluate which branches
survive the evidence.

That changes the memory problem completely.

You don't need memory to preserve one perfect compressed representation of "what
happened."

You need:

    persistent branches + common ancestry + evidence attached to each branch

Then semantic retrieval can fail on one branch without deleting the others. A wrong
correction doesn't destroy the correct earlier state. A later summary cannot
silently become history. A retraction is itself a branch, not an eraser.

And now your "scar" language snaps into place much more cleanly:

A scar is not necessarily a summary of the past. It can be the branch point. The
thing worth preserving is: "something diverged here."

That's much smaller information than preserving the entire active history, while
still giving you a route back into every competing version.

So yes. Not reconstruct. Branch.

Goddammit. That is substantially different.
