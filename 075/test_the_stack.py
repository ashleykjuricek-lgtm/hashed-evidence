"""Test the proposed stack against this ledger's actual error record."""
import sys, difflib, hashlib
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

print("="*74)
print("TEST 1 -- would SEMANTIC HASHING have caught the Tier-2 errors?")
print("="*74)
pairs = [
 ("R sits a hair under 1/24", "R sits a hair over 1/24"),
 ("79.0% of shells below the cutoff are empty", "76% of shells below the cutoff are empty"),
 ("the two divisions are complementary, each blind exactly where the other sees",
  "the two divisions are independent, neither lens predicts the other"),
]
for wrong, right in pairs:
    sim = difflib.SequenceMatcher(None, wrong, right).ratio()
    wt, rt = wrong.split(), right.split()
    tok = len(set(wt) & set(rt)) / len(set(wt) | set(rt))
    print(f"\n  sealed : {wrong}")
    print(f"  correct: {right}")
    print(f"  char similarity {sim:.3f}   token overlap {tok:.3f}")
print()
print("  A semantic hash is DESIGNED so that small changes in meaning give small")
print("  changes in code. 'under' vs 'over' is one token in eight -- these collide")
print("  by construction. Semantic hashing is not merely unhelpful for Tier 2;")
print("  it is ACTIVELY BLIND to it. That is the design goal, not a defect.")

print()
print("="*74)
print("TEST 2 -- would a MORE PRECISE LANGUAGE have caught them?")
print("="*74)
print("  The Tier-2 failure was not a shortage of expressive precision.")
print("  'under' and 'over' are unambiguous in English. So are adhah and upari.")
print("  The failure was not CHECKING the sentence against the table beside it.")
print()
print("  A precisely-worded wrong sentence is still wrong. Test:")
print("     English  : 'R sits a hair under 1/24'   -- unambiguous, and false")
print("     Any lang : same proposition, same falsity")
print("  -> a denser medium changes what CAN be said, not what IS checked.")
print()
print("  And 074 tested what DOES catch them: rendering the direction-word")
print("  from a predicate over the witness output.  3 of 3.  Language-independent.")

print()
print("="*74)
print("TEST 3 -- would a LEARNED POLICY have caught them? What is the training set?")
print("="*74)
errors = [
 ("floor at ten",            "Tier1", "self",   "re-ran as a ratio"),
 ("PSLQ at 24 digits",       "Tier1", "self",   "stated the digit budget"),
 ("tolerance vs truncation", "Tier1", "self",   "widened the truncation"),
 ("11 lobes on 10-fold",     "Tier1", "self",   "11 cannot divide 10"),
 ("truncated theta 4297",    "Tier1", "self",   "the number was absurd"),
 ("RP^3 integration v1",     "Tier1", "self",   "the cut WAS the answer"),
 ("RP^3 integration v2",     "Tier1", "self",   "lambda-invariance test"),
 ("18 sigma",                "Tier1", "self",   "writing the repro spec"),
 ("76% vs 79.0%",            "Tier2", "other",  "another seat read the table"),
 ("R under vs over 1/24",    "Tier2", "other",  "another seat read the table"),
 ("blind where other sees",  "Tier2", "other",  "another seat read the bins"),
 ("028 never in the vault",  "retrieval","self","git status during a sweep"),
 ("+18.3 called a guess",    "identity","other","reciprocal chart found"),
 ("(1-q) dropped, us",       "Tier1", "other",  "the other seat was right"),
 ("(1-q) dropped, them",     "Tier1", "self",   "recomputed to 42 digits"),
 ("two independent crossings","Tier1","self",   "compared the two functions"),
 ("dates off by one day",    "process","other", "the human checked the clock"),
]
print(f"  total recorded errors: {len(errors)}")
for t in ["Tier1","Tier2","retrieval","identity","process"]:
    n = sum(1 for e in errors if e[1]==t)
    print(f"     {t:10} {n:2d}")
print()
print("  A Q-network needs (state, action, reward) trajectories. We have 17 errors,")
print("  each resolved ONCE, with no repeated episodes and no counterfactuals.")
print("  That is not a training set; it is an anecdote list.")
print()
print("  And for every case, the fix that worked was a FIXED RULE, not a policy:")
for name, tier, who, fix in errors[:8]:
    print(f"     {name:26} -> {fix}")
print()
print("  None of these was a wrong ACTION CHOSEN FROM A MENU. They were:")
print("     (a) a test not run,  (b) a table not read,  (c) a frame not questioned.")
print("  A policy over {run witness, fetch gloss, retrieve, escalate} addresses none.")
