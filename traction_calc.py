#!/usr/bin/env python3
"""
Traction Calculator — interactive REPL for COTT algebra.

Usage:
    python3 traction_calc.py

Type any traction expression at the prompt. Supports:
    0, w (omega), null
    +, -, *, /, ^ (power)
    log0(x), logw(x), sqrt(x)
    traction_simplify(expr), resolve(expr)
    project_complex(expr) — map to standard complex numbers
    Any SymPy expression (sin, cos, pi, I, Rational, etc.)

Examples:
    >>> 0^w
    -1
    >>> 0^(0^5)
    5
    >>> 0 * w
    1
    >>> log0(w^3)
    -3
    >>> traction_simplify(z**2 * w**3)
    w
    >>> project_complex(0^(w/2))
    I
"""

import os
import sys
import readline
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from sympy import (
    S, Pow, Rational, Symbol, Integer, Add, Mul, I, pi, sqrt,
    sin, cos, tan, exp, log, oo, zoo, simplify, factor, expand,
    symbols, Abs
)
from traction import (
    Zero, Omega, Null, Log0, LogW, z, w, null,
    traction_simplify, log0, logw, zpow, wpow,
    resolve, resolve_log, project_complex, W_CONST
)

BANNER = """
╔══════════════════════════════════════════════╗
║         Traction Calculator (COTT)           ║
║  Type expressions using 0, w, null           ║
║  Use ^ for powers, log0/logw for logs        ║
║  project_complex(expr) to map to C           ║
║  Type 'help' for examples, 'quit' to exit    ║
╚══════════════════════════════════════════════╝
"""

HELP_TEXT = """
─── Basics ───────────────────────────────────
  z or 0_       traction zero (use z or 0_ to avoid Python int 0)
  w             omega
  null          traction null

─── Operators ────────────────────────────────
  z**w          0^w = -1
  z**(z**5)     0^(0^5) = 5
  z * w         0 * w = 1
  z / z         0 / 0 = 1
  w**(-2)       w^(-2) = 0^2

─── Functions ────────────────────────────────
  log0(x)       base-0 logarithm
  logw(x)       base-w logarithm
  traction_simplify(expr)   simplify compound expressions
  project_complex(expr)     project to complex numbers
  resolve(x)                identity resolution

─── Shorthand (in input only) ────────────────
  0^w           rewritten to z**w before eval
  w^(0^3)       rewritten to w**(z**3)
  Use ^ instead of ** if you prefer

─── Examples ─────────────────────────────────
  z**w                        → -1
  z**(z**7)                   → 7
  w**(w**2)                   → -1/2
  log0(Integer(3))            → 0^3
  traction_simplify(z**5 * w**2)  → 0^3
  project_complex(z**(w/2))   → I
  (z**(w/2))**2               → -1
"""


def preprocess(line):
    """Rewrite user-friendly syntax to valid Python."""
    # Replace ^ with ** (but not inside strings or **already)
    # Simple approach: replace ^ that isn't part of ^^
    line = re.sub(r'(?<!\*)\^(?!\*)', '**', line)

    # Replace standalone 0 used in traction context with z
    # Match 0 when followed by ** or * or / or when it's a base
    # But not inside numbers like 10, 20, 0.5, etc.
    # Strategy: replace 0** with z**, 0* with z*, etc.
    line = re.sub(r'(?<![0-9.])0(?=\*)', 'z', line)
    line = re.sub(r'(?<![0-9.])\(0\)', '(z)', line)

    # 0_ as explicit alias
    line = line.replace('0_', 'z')

    return line


def main():
    print(BANNER)

    # Build eval namespace
    ns = {
        'z': z, 'w': w, 'null': null,
        'Zero': Zero, 'Omega': Omega, 'Null': Null,
        'log0': log0, 'logw': logw, 'zpow': zpow, 'wpow': wpow,
        'traction_simplify': traction_simplify, 'ts': traction_simplify,
        'resolve': resolve, 'resolve_log': resolve_log,
        'project_complex': project_complex, 'pc': project_complex,
        'W_CONST': W_CONST,
        'S': S, 'Pow': Pow, 'Rational': Rational, 'Integer': Integer,
        'Symbol': Symbol, 'symbols': symbols,
        'Add': Add, 'Mul': Mul,
        'I': I, 'pi': pi, 'sqrt': sqrt, 'Abs': Abs,
        'sin': sin, 'cos': cos, 'tan': tan,
        'exp': exp, 'log': log, 'ln': log,
        'oo': oo, 'zoo': zoo,
        'simplify': simplify, 'factor': factor, 'expand': expand,
    }

    # History file
    histfile = os.path.expanduser('~/.traction_calc_history')
    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass

    while True:
        try:
            line = input('\033[36m>>> \033[0m').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nBye!')
            break

        if not line:
            continue
        if line.lower() in ('quit', 'exit', 'q'):
            print('Bye!')
            break
        if line.lower() == 'help':
            print(HELP_TEXT)
            continue

        processed = preprocess(line)

        try:
            result = eval(processed, {"__builtins__": {}}, ns)
            if result is not None:
                print(f'\033[33m{result}\033[0m')
                ns['_'] = result  # store last result
        except SyntaxError:
            try:
                exec(processed, {"__builtins__": {}}, ns)
            except Exception as e:
                print(f'\033[31mError: {e}\033[0m')
        except Exception as e:
            print(f'\033[31mError: {e}\033[0m')

    # Save history
    try:
        readline.write_history_file(histfile)
    except OSError:
        pass


if __name__ == '__main__':
    main()
