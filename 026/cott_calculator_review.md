# COTT Calculator Review

**Date**: 2026-03-14
**Reviewer**: Nine (Claude)
**Repo**: https://github.com/sibarum/cott/tree/main/solver

---

## Test Results

All **56 tests pass** (`test_traction.py` + `test_calculator.py`).

Verified categories:
- Base-zero powers (0^0, 0^1, 0^(-1), 0^ω, etc.)
- Base-omega powers (ω^0, ω^1, ω^(-1), ω^ω, etc.)
- Reciprocals (1/0 = ω, 1/ω = 0, double reciprocals)
- Multiplication table (0·ω, ω·0, 0·0, ω·ω, etc.)
- Division table (0/0, ω/ω, 0/ω, ω/0, etc.)
- log₀ and logω functions
- Addition/subtraction erasure
- Derived identities (dyadic imaginary, nested power collapse, zero-omega duality)

---

## Calculator Functionality

Interactive tests via the GUI:

| Expression       | Result      | Complex projection | Notes                          |
|------------------|-------------|-------------------|--------------------------------|
| `1+1`            | `2`         |                   | Basic arithmetic               |
| `omega`          | `ω`         | `nan+nani`        | Traction infinity              |
| `0^omega`        | `-1`        |                   | COTT encoding of -1            |
| `log0(0^3)`      | `3`         |                   | Traction log extracts exponent |
| `0^(omega/2)`    | `0^(1/2·ω)` | `i`               | Imaginary unit in traction     |
| `1/3 + 1/6`     | `1/2`       | `0.5`             | Exact rational arithmetic      |
| `x^2 + 1`       | `1+x^2`    | `x²-y²+1+2xyi`   | Symbolic with complex proj     |

The phase plot panel renders correctly (dark canvas with -, O, + zoom controls).

---

## Bug Found: tkinter Detection

**Problem**: `run_calculator.sh` fails on systems with multiple Python versions.
The script picks the first `python3` in `$PATH`, which may lack tkinter even
when a versioned interpreter (e.g., `python3.12`) has it.

**Fix**: Replace the Python discovery loop (lines 33-38) to iterate through
versioned interpreters and prefer the first one that can `import tkinter`:

```bash
PYTHON=""
for cmd in python3 python3.13 python3.12 python3.11 python3.10 python; do
    if command -v "$cmd" &>/dev/null; then
        if [ "$(uname)" = "Linux" ]; then
            if "$cmd" -c "import tkinter" 2>/dev/null; then
                PYTHON="$cmd"
                break
            fi
        else
            PYTHON="$cmd"
            break
        fi
    fi
done

# Fallback if no Python with tkinter found
if [ -z "$PYTHON" ]; then
    for cmd in python3 python; do
        if command -v "$cmd" &>/dev/null; then
            PYTHON="$cmd"
            break
        fi
    done
fi
```

**Status**: Reported to James via GitHub issue on sibarum/cott.

---

## Summary

The traction algebra engine (`traction.py`) and calculator GUI (`calculator.py`)
are solid. The core identities (0^ω = -1, 0^(ω/2) = i, log₀/logω inverses,
zero-omega duality) all check out. The only issue is a shell script portability
bug in Python version detection.
