# 116 — The anaconda3 integrity audit: clean, with the residue explained

**Audit performed 2026-08-31 (Ash + Fable seat). Sealed 2026-09-09 at
Ash's word ("fill 116 with the anaconda audit").**

**Provenance, stated before the findings:** the audit ran in-session on
2026-08-31; its report was delivered to Ash that night and its scripts
lived in an ephemeral session workspace that no longer exists. This
entry preserves the findings and the method as recorded in the session's
own preserved summary, written the same night. The counts below are that
record. The scripts are NOT preserved — a rerun would rewrite them from
the method section. That gap is named here rather than smoothed; this is
an audit RECORD, sealed eight days late, not a rerunnable artifact.

## Why it ran

Suspicion began at cosmology files inside C:\Users\atoms\anaconda3 —
which turned out to be astropy's stock cosmology module, part of
Anaconda's default bundle, unconnected to the Pi work. The question
became general: has anything in the Python installation been tampered
with?

## Findings — CLEAN, zero unexplained

Pass 1 (site-packages): 79,630 files; 50,613 hash-verified against 402
dist-info manifests. All 1,411 mismatches traced to documented installer
behavior:
- Anaconda Inc. signs Windows binaries AFTER writing manifests — the
  signature block adds exactly +12,104 bytes, every time;
- conda rewrites INSTALLER files (pip -> conda);
- config files get local paths stamped over factory paths.

635 unlisted files: 619 byte-identical to the pristine pkgs cache; 1
path-stamped (verified by diff); 15 from pre-fingerprint egg-info-era
packages (appdirs, pyls_spyder), read by eye — clean.

Pass 2 (same day, because Ash challenged the hedges): all 28,949 .pyc
bytecode caches verified by recompiling every source and comparing code
objects. The 250 strict failures all resolved: 30 = pytest's
assertion-rewrite (self-identifying markers); 2 stale (unloadable);
218 = CPython compiler dialect drift (the 3.13.0-era factory compiler
omits a GET_ITER that 3.13.9 emits — same names, same constants, and
all byte-identical to the sealed pkgs crates).

**Total: 108,579 files examined across both passes. Zero unexplained.**

## The method (reusable — three ledgers plus signatures)

1. dist-info RECORD hashes (the package manager's own manifest);
2. conda-meta provenance (what the installer says it installed);
3. byte-comparison against pristine copies in anaconda3\pkgs cache;
plus Get-AuthenticodeSignature for signed binaries, and for bytecode:
recompile-and-compare code objects, treating NEW NAMES OR CONSTANTS as
the tamper signal (instruction-order drift with identical names and
constants is compiler patch-version noise).

## The two benign signatures worth remembering

- A Windows binary exactly +12,104 bytes over its manifest entry is
  carrying Anaconda's code signature, not a payload.
- Bytecode that differs in instructions but not in names or constants
  is compiler drift. Malicious bytecode essentially requires new names
  or new constants — check those first, always.

## Why this is in the ledger

The machine that verifies the seals must itself be verifiable — an
unaudited verifier is a smoothed link in the chain. This baseline means
the next suspicion starts from a sealed floor instead of from zero.

Stratum: COUNTED (the file counts and resolutions, as recorded the night
of the audit); the clean verdict is relative to the three ledgers used —
a tamper that forged all three consistently would evade them, and that
boundary is stated rather than hidden.

— Ash's challenge drove the second pass; the seat ran the audit; sealed
on her word.
