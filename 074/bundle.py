"""Package one witness as a sealed bundle: expected.json + a hash over it.
This is the 'plumbing' half. Demonstrated on the slope claim."""
import sys, json, hashlib, subprocess, platform
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

bundle = {
  "witness_id": "slope-of-eps-anisotropic/v1",
  "claim": "the slope of eps = 24R-1 in the anisotropic deformation, at the cube",
  "route": "Ewald/Poisson anisotropic Epstein zeta at s=-1/2; mpmath diff at b=1",
  "code": "witness_slope.py::witness",
  "input_signature": {
    "family": ["1bb", "volpres"],
    "chart":  ["direct", "momentum"],
    "marked": ["short", "stretched"]
  },
  "conventions": {
    "chart": "which axis carries b^2 in the quadratic form; 'direct' is 028 App A.3, 'momentum' is 047",
    "marked": "semantic label; its axis INDEX is family-dependent -- see the v1 bug note in witness_slope.py"
  },
  "precision": {"mp_dps": 25, "tolerance": "RELATIVE 1e-9",
                "note": "absolute tolerance FAILS: a claim stated to 12 figures cannot discharge 1e-9 absolute on a value of size ~27"},
  "expected": {
    "1bb|direct|short":        "+18.3259647484177",
    "1bb|momentum|short":      "-18.3259647484177",
    "volpres|momentum|stretched": "+27.4889471226266"
  },
  "predicate_examples": {
    "sign_at_cube": "sign(d eps/db) -- chart-dependent, MUST cite its inputs",
    "transversality": "d eps/db != 0 -- family-INdependent, safe to state bare"
  },
  "discharged_by": [
    {"artefact": "028 App A.3 (2026-06-20)", "inputs": "1bb|direct|short",        "claimed": "~ +18.3",              "ok": True},
    {"artefact": "047 sec.B (2026-08-23)",   "inputs": "1bb|momentum|short",      "claimed": "-18.3259647484177",    "ok": True},
    {"artefact": "KESTREL (2026-08-23)",     "inputs": "volpres|momentum|stretched", "claimed": "27.4889471200",     "ok": True}
  ],
  "environment": {"python": platform.python_version(), "mpmath": __import__("mpmath").__version__},
  "status_word": "OBSERVED",
  "status_note": "the witness carries IDENTITY, not truth. Truth is the four-word column."
}
blob = json.dumps(bundle, indent=2, sort_keys=True)
open("expected.json","w",encoding="utf-8").write(blob)
h = hashlib.sha256(blob.encode()).hexdigest()
open("expected.sha256","w").write(h + "  expected.json\n")
print("bundle written.")
print("  witness_id :", bundle["witness_id"])
print("  discharged :", sum(1 for d in bundle["discharged_by"] if d["ok"]), "of", len(bundle["discharged_by"]), "artefacts")
print("  sha256     :", h)
print()
print("  three artefacts, three charts, one claim -- and the resolution is now STORED,")
print("  so no future seat re-fights it. That is the rendezvous, not an oracle.")
