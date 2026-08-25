#!/usr/bin/env python3
"""Verify every sealed folder in the vault.

Written after three of its own bugs each produced a FALSE "seal chain broken"
report. Handles, because each of these broke it once:
  1. both hashes.txt column orders  (001-021 are "<sha>  <name>", 022+ are "<name>  <sha>")
  2. filenames containing SPACES     (002/"eddy_space_record_001 (1).md", 001/*.png)
  3. one folder counted once         (a glob matched 0NN twice)
Also reports CRLF-only mismatches separately: those are a stale working tree,
not tampering -- .gitattributes "* -text" fixes future checkouts but not this one.
"""
import os, re, sys, hashlib, io

HEX = re.compile(r'[0-9a-f]{64}')
tot = crlf = bad = 0
folders = sorted(d for d in os.listdir('.')
                 if re.fullmatch(r'\d{3}', d) and os.path.isfile(os.path.join(d, 'hashes.txt')))

for d in folders:
    for line in io.open(os.path.join(d, 'hashes.txt'), encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if not line.strip() or line.lstrip().startswith('#'): continue
        m = HEX.search(line)
        if not m: continue
        h = m.group(0)
        name = (line[:m.start()] + line[m.end():]).strip()   # everything that is not the hash
        if not name: continue
        p = os.path.join(d, name)
        tot += 1
        if not os.path.isfile(p):
            print(f"MISSING  {d}/{name}"); bad += 1; continue
        raw = open(p, 'rb').read()
        if hashlib.sha256(raw).hexdigest() == h: continue
        if hashlib.sha256(raw.replace(b'\r\n', b'\n')).hexdigest() == h:
            print(f"CRLF     {d}/{name}   (content intact; stale working tree)"); crlf += 1
        else:
            print(f"BROKEN   {d}/{name}"); print(f"           sealed {h}"); bad += 1

print()
print(f"folders checked      : {len(folders)}")
print(f"files checked        : {tot}")
print(f"CRLF-only (benign)   : {crlf}")
print(f"REAL failures        : {bad}")
print("ALL SEALS VERIFY" if bad == 0 and crlf == 0 else
      ("CONTENT INTACT, working tree stale" if bad == 0 else "*** SEAL CHAIN BROKEN ***"))
sys.exit(1 if bad else 0)
