#!/usr/bin/env python3
"""Generate LEDGER-INDEX.md -- a COMPUTED one-line-per-entry view of the ledger.

Never hand-edit the output. Every line is extracted mechanically from each
sealed folder: the first '#' heading of its first README*.md (or the first
file's first heading), plus the file count. A view no hand writes cannot
drift from the record it summarizes (082's computed-prose principle).
Regenerate any time:  python generate_index.py
"""
import os, re, io

folders = sorted(d for d in os.listdir('.') if re.fullmatch(r'\d{3}', d) and os.path.isdir(d))
lines = ["# LEDGER-INDEX — computed view, never hand-edited",
         "# regenerate with: python generate_index.py",
         "# one line per sealed entry: number | files | first heading of its README", ""]
for d in folders:
    files = sorted(f for f in os.listdir(d) if f != 'hashes.txt' and os.path.isfile(os.path.join(d, f)))
    sealed = 'sealed' if os.path.isfile(os.path.join(d, 'hashes.txt')) else 'OPEN'
    heading = ''
    readmes = [f for f in files if f.lower().startswith('readme') and f.endswith('.md')]
    for cand in (readmes or [f for f in files if f.endswith('.md')]):
        for line in io.open(os.path.join(d, cand), encoding='utf-8', errors='replace'):
            if line.startswith('#'):
                heading = line.lstrip('#').strip(); break
        if heading: break
    lines.append(f"{d} | {len(files):2d} files | {sealed:6s} | {heading}")
with io.open('LEDGER-INDEX.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(lines) + '\n')
print(f"wrote LEDGER-INDEX.md: {len(folders)} entries")
