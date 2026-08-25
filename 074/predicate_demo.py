"""Does (witness, predicate) actually make the Tier-2 error unwritable?

Test set: the three Tier-2 errors this ledger has recorded. Each is an emphasised
sentence contradicted by a table on the same page. For each: build the witness,
state the predicate, RENDER the direction-word from the predicate, and compare
against what was actually sealed."""
import sys
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import numpy as np, math, json, hashlib

def sieve(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.nonzero(s)[0]

RESULTS = []

# ---------------------------------------------------------------- W1 : 066
def w_R_vs_24():
    R = 0.0416894146027237751200791895411477959451762762538280901
    return {"R": R, "eps": 24*R - 1}
def p_R_vs_24(o):  return "over" if o["eps"] > 0 else "under"
RESULTS.append(("066 sec.1", "R sits a hair ___ 1/24",
                w_R_vs_24, p_R_vs_24, "under"))

# ---------------------------------------------------------------- W2 : 067
def w_empty_fraction():
    M = 2_000_000; N = int(math.isqrt(M))+1
    r2 = np.zeros(M+1, np.int64)
    for x in range(N+1):
        x2 = x*x
        if x2 > M: break
        y = np.arange(0, int(math.isqrt(M-x2))+1, dtype=np.int64)
        s = x2 + y*y
        mult = np.where((x>0)&(y>0),4,np.where((x>0)|(y>0),2,0))
        np.add.at(r2, s, mult)
    r2[0] = 0
    empty = int(np.count_nonzero(r2[1:M+1] == 0))
    return {"cutoff": M, "empty": empty, "pct": 100.0*empty/M}
def p_empty_fraction(o): return f"{o['pct']:.1f}%"
RESULTS.append(("067 sec.2", "___ of shells below the cutoff are empty",
                w_empty_fraction, p_empty_fraction, "76%"))

# ---------------------------------------------------------------- W3 : 070
def w_two_lenses():
    P = sieve(3000)
    f4 = lambda p: p==2 or p%4==1
    f5 = lambda p: p==5 or p%5 in (1,4)
    b  = sum(1 for p in P if f4(p) and f5(p))
    nn = sum(1 for p in P if not f4(p) and not f5(p))
    return {"both": b, "neither": nn, "total": int(len(P))}
def p_two_lenses(o):
    return ("complementary -- each blind exactly where the other sees"
            if o["both"] == 0 and o["neither"] == 0
            else f"independent -- they agree on {o['both']+o['neither']}/{o['total']}")
RESULTS.append(("070 sec.2", "the two divisions are ___",
                w_two_lenses, p_two_lenses,
                "complementary -- each blind exactly where the other sees"))

print("="*74)
print("(witness, predicate) against the three recorded Tier-2 errors")
print("="*74)
killed = 0
for tag, template, w, p, sealed in RESULTS:
    out = w(); rendered = p(out)
    match = (rendered == sealed)
    killed += (not match)
    print()
    print(f"  {tag}   template: {template}")
    print(f"     witness output : {json.dumps(out)[:110]}")
    print(f"     predicate says : {rendered}")
    print(f"     what was sealed: {sealed}")
    print(f"     -> {'AGREES' if match else 'CONTRADICTS -- the wrong sentence is UNWRITABLE'}")
print()
print("="*74)
print(f"Tier-2 errors caught by rendering the predicate: {killed} of {len(RESULTS)}")
print("="*74)
print()
print("  All three were emphasised sentences that survived multiple rereads by")
print("  their author and were caught only by another seat. A rendered predicate")
print("  catches all three MECHANICALLY -- the direction word is no longer typed.")
print()
print("  What it does NOT touch: Tier 3. There is no witness for")
print("  'is R the right object?' or 'is the integer requirement ours or the world's?'")
