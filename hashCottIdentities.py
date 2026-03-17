#!/usr/bin/env python3
"""
hashCottIdentities.py — Evaluate all COTT identities via the Python traction solver
and SHA-256 hash every result for tamper-evident evidence.

Usage:
    python3 hashCottIdentities.py [output-dir]
    If output-dir is given, writes cott-identity-hashes.txt there.
    Otherwise prints to stdout.

Engine: sibarum/cott solver/traction.py (SymPy-based)
"""

import hashlib
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from sympy import S, Pow, Rational, Symbol, Integer, I, pi, exp as sp_exp
from traction import (
    Zero, Omega, Null, z, w, null,
    traction_simplify, log0, logw, zpow, wpow,
    resolve, project_complex, W_CONST
)


def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def fmt(val):
    """Format a SymPy result to a canonical string."""
    return str(val)


def check(label, expr, expected_str=None):
    """Evaluate and record one identity. Optionally verify against expected."""
    result = fmt(expr)
    passed = True
    if expected_str is not None and result != expected_str:
        passed = False
    return {'label': label, 'result': result, 'passed': passed, 'expected': expected_str}


# ═══════════════════════════════════════════════════════════════════
# Build all identities
# ═══════════════════════════════════════════════════════════════════

results = []

# ── Section 1: Base-zero exponentiation ─────────────────────────

results.append(check('0^0 = 1',       z**0,       '1'))
results.append(check('0^1 = 0',       z**1,       '0'))
results.append(check('0^(-1) = w',    z**(-1),    'w'))
results.append(check('0^w = -1',      z**w,       '-1'))

# Higher integer powers stay irreducible
results.append(check('0^2 = 0^2',     z**2,       '0**2'))
results.append(check('0^3 = 0^3',     z**3,       '0**3'))
results.append(check('0^4 = 0^4',     z**4,       '0**4'))

# Negative exponents flip to omega
results.append(check('0^(-2) = w^2',  z**(-2),    'w**2'))
results.append(check('0^(-3) = w^3',  z**(-3),    'w**3'))

# ── Section 2: Base-omega exponentiation ────────────────────────

results.append(check('w^0 = 1',       w**0,       '1'))
results.append(check('w^1 = w',       w**1,       'w'))
results.append(check('w^(-1) = 0',    w**(-1),    '0'))
results.append(check('w^w = -1',      w**w,       '-1'))
results.append(check('w^(-2) = 0^2',  w**(-2),    '0**2'))
results.append(check('w^(-3) = 0^3',  w**(-3),    '0**3'))

# ── Section 3: Identity resolution (tower rules) ───────────────

results.append(check('0^(0^2) = 2',   z**(z**2),  '2'))
results.append(check('0^(0^3) = 3',   z**(z**3),  '3'))
results.append(check('0^(0^5) = 5',   z**(z**5),  '5'))
results.append(check('0^(0^7) = 7',   z**(z**7),  '7'))

# Omega tower: 0^(w^n) = -n
results.append(check('0^(w^2) = -2',  z**(w**2),  '-2'))
results.append(check('0^(w^3) = -3',  z**(w**3),  '-3'))

# Omega base towers: w^(0^n) = -n
results.append(check('w^(0^2) = -2',  w**(z**2),  '-2'))
results.append(check('w^(0^3) = -3',  w**(z**3),  '-3'))

# w^(w^n) = -1/n
results.append(check('w^(w^2) = -1/2', w**(w**2), '-1/2'))
results.append(check('w^(w^3) = -1/3', w**(w**3), '-1/3'))

# Symbolic tower
x = Symbol('x')
results.append(check('0^(0^x) = x',   z**(z**x),  'x'))
results.append(check('0^(w^x) = -x',  z**(w**x),  '-x'))

# ── Section 4: Multiplication table ────────────────────────────

results.append(check('0 * w = 1',     z * w,      '1'))
results.append(check('w * 0 = 1',     w * z,      '1'))
results.append(check('0 * 0 = 0^2',   z * z,      '0**2'))
results.append(check('w * w = w^2',   w * w,      'w**2'))

# ── Section 5: Division table ──────────────────────────────────

results.append(check('0/0 = 1',       z / z,      '1'))
results.append(check('w/w = 1',       w / w,      '1'))
results.append(check('1/0 = w',       S.One / z,  'w'))
results.append(check('1/w = 0',       S.One / w,  '0'))
results.append(check('0/w = 0^2',     z / w,      '0**2'))
results.append(check('w/0 = w^2',     w / z,      'w**2'))

# ── Section 6: Reciprocals ─────────────────────────────────────

results.append(check('1/(1/0) = 0',   S.One / (S.One / z), '0'))
results.append(check('1/(1/w) = w',   S.One / (S.One / w), 'w'))

# ── Section 7: Logarithms ──────────────────────────────────────

results.append(check('log_0(1) = 0',     log0(S.One),     '0'))
results.append(check('log_0(0) = 1',     log0(z),         '1'))
results.append(check('log_0(w) = -1',    log0(w),         '-1'))
results.append(check('log_0(0^3) = 3',   log0(z**3),      '3'))
results.append(check('log_0(w^2) = -2',  log0(w**2),      '-2'))
results.append(check('log_0(3) = 0^3',   log0(Integer(3)),'0**3'))
results.append(check('log_0(-3) = w^3',  log0(Integer(-3)),'w**3'))
results.append(check('logw(1) = 0',      logw(S.One),     '0'))
results.append(check('logw(w) = 1',      logw(w),         '1'))
results.append(check('logw(0) = -1',     logw(z),         '-1'))
results.append(check('logw(w^5) = 5',    logw(w**5),      '5'))
results.append(check('logw(0^3) = -3',   logw(z**3),      '-3'))

# ── Section 8: traction_simplify composites ─────────────────────

results.append(check('2*0*3*w = 6',
    traction_simplify(2 * z * 3 * w), '6'))

results.append(check('0*0*0 = 0^3',
    traction_simplify(z * z * z), '0**3'))

results.append(check('(-1)*0 = 0 [sign absorbed]',
    traction_simplify(S.NegativeOne * z), '0'))

results.append(check('(-2)*0 = 2*0 [sign absorbed]',
    traction_simplify(Integer(-2) * z), '2*0'))

results.append(check('(-1)*0^2 = 0^2 [sign absorbed]',
    traction_simplify(S.NegativeOne * z**2), '0**2'))

results.append(check('0^2 * 0^3 = 0^5',
    traction_simplify(z**2 * z**3), '0**5'))

results.append(check('w^2 * w^3 = w^5',
    traction_simplify(w**2 * w**3), 'w**5'))

results.append(check('0^5 * w^2 = 0^3',
    traction_simplify(z**5 * w**2), '0**3'))

results.append(check('0^3 * w^3 = 1',
    traction_simplify(z**3 * w**3), '1'))

results.append(check('0^(w/2) * 0^(w/2) = -1',
    traction_simplify(z**(w / 2) * z**(w / 2)), '-1'))

# ── Section 9: Subtraction / erasure ───────────────────────────

from sympy import Add
results.append(check('x - x = null',
    traction_simplify(Add(x, -x, evaluate=False)), 'null'))

results.append(check('5 - 5 = null',
    traction_simplify(Add(Integer(5), Integer(-5), evaluate=False)), 'null'))

# ── Section 10: Universal power-of-power ───────────────────────

results.append(check('(x^2)^(1/2) = x',
    traction_simplify((x**2)**Rational(1, 2)), 'x'))

results.append(check('(x^4)^(1/4) = x',
    traction_simplify((x**4)**Rational(1, 4)), 'x'))

a, b = Symbol('a'), Symbol('b')
results.append(check('(x^a)^b = x^(a*b)',
    traction_simplify(Pow(Pow(x, a), b)), 'x**(a*b)'))

results.append(check('(0^a)^b = 0^(a*b)',
    traction_simplify(Pow(Pow(z, a), b)), '0**(a*b)'))

# ── Section 11: Derived identities ─────────────────────────────

results.append(check('log_0(-1) = w',
    log0(S.NegativeOne), 'w'))

results.append(check('(0^(w/2))^2 = -1 [i^2 = -1]',
    traction_simplify((z**(w / 2))**2), '-1'))

results.append(check('0^(0^(0^3)) = 0^3 [triple tower]',
    z**(z**(z**3)), '0**3'))

# ── Section 12: Complex projection ─────────────────────────────

results.append(check('C(0^w) = -1',
    project_complex(z**w), '-1'))

results.append(check('C(0^(w/2)) = I [projects to i]',
    project_complex(z**(w / 2)), 'I'))

results.append(check('C(w^(w/2)) = -I [projects to -i]',
    project_complex(w**(w / 2)), '-I'))

results.append(check('C(3 * 0^(w/2)) = 3*I',
    project_complex(3 * z**(w / 2)), '3*I'))

results.append(check('C(5) = 5',
    project_complex(Integer(5)), '5'))

results.append(check('C(null) = 0',
    project_complex(null), '0'))

results.append(check('W^2 = -i*pi',
    str(W_CONST**2 + I * pi == 0), None))  # just record it

# ── Section 13: Resolve (identity resolution function) ──────────

results.append(check('resolve(5) = 5',
    resolve(5), '5'))

results.append(check('resolve(w) = w',
    resolve(w), 'w'))

results.append(check('resolve(0^2) = 0^2',
    resolve(z**2), '0**2'))


# ═══════════════════════════════════════════════════════════════════
# Format + hash
# ═══════════════════════════════════════════════════════════════════

timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

lines = []
lines.append('# COTT Identity Hashes — Python Traction Solver')
lines.append(f'# Generated: {timestamp}')
lines.append(f'# Engine: sibarum/cott solver/traction.py (SymPy {__import__("sympy").__version__})')
lines.append(f'# Total identities evaluated: {len(results)}')
lines.append('')

passed = sum(1 for r in results if r['passed'])
failed = sum(1 for r in results if not r['passed'])
lines.append(f'# Verification: {passed} passed, {failed} failed')
lines.append('')
lines.append('# Each line: identity | engine_result | sha256(result) | status')
lines.append('')

max_label  = max(len(r['label']) for r in results)
max_result = max(len(r['result']) for r in results)

for r in results:
    h = sha256(r['result'])
    status = 'OK' if r['passed'] else f"FAIL (expected: {r['expected']})"
    lines.append(f"{r['label'].ljust(max_label + 2)}| {r['result'].ljust(max_result + 2)}| {h} | {status}")

lines.append('')

# Master hash of all results
all_results = '\n'.join(r['result'] for r in results)
master = sha256(all_results)
lines.append(f'# Master hash (SHA-256 of all results concatenated): {master}')
lines.append('')

output = '\n'.join(lines)

# ═══════════════════════════════════════════════════════════════════
# Write or print
# ═══════════════════════════════════════════════════════════════════

out_dir = sys.argv[1] if len(sys.argv) > 1 else None

if out_dir:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, 'cott-identity-hashes.txt')
    with open(path, 'w') as f:
        f.write(output)
    print(f'Written to {path}')
else:
    print(output)
