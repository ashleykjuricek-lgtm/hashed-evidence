#!/usr/bin/env node
// hashCottIdentities.js — Evaluate COTT identities via the JS algebra engine and SHA-256 hash every result.
// Usage: node hashCottIdentities.js [output-dir]
//   If output-dir is given, writes results there. Otherwise prints to stdout.
//
// Source engine: sibarum/cott lib/traction/ops.js (adapted)
// Author: Prismic Collaboration, 2026

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const OPS = require('./lib/ops');

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function sha256(str) {
    return crypto.createHash('sha256').update(str, 'utf8').digest('hex');
}

/** Pretty-print an eval result */
function fmt(val) {
    if (val === undefined || val === null) return 'undefined';
    if (typeof val === 'number') {
        if (val === Infinity) return 'Infinity';
        if (val === -Infinity) return '-Infinity';
        return String(val);
    }
    if (typeof val.toString === 'function') return val.toString();
    return String(val);
}

/** Build a result object, evaluating the expression */
function evaluate(label, exprNode) {
    const raw = exprNode.eval ? exprNode.eval() : exprNode;
    const result = fmt(raw);
    return { label, result };
}

// ---------------------------------------------------------------------------
// Build all COTT identities using the JS algebra engine
// ---------------------------------------------------------------------------

const eb = new OPS.ExprBuilder();

// Convenience shortcuts
const ZERO  = eb.number(0);           // OPS.Zero(1)
const ONE   = eb.number(1);           // OPS.One(1)
const OMEGA = eb.number(Infinity);    // OPS.Zero(-1)   = ω
const NEG1  = eb.number(-1);          // OPS.One(-1)

const identities = [];

// ── Section 1: Base-zero exponentiation (the four key values) ──────────────

identities.push(evaluate('0^0 = 1',    eb.exp(ZERO, ZERO)));
identities.push(evaluate('0^1 = 0',    eb.exp(ZERO, ONE)));
identities.push(evaluate('0^ω = -1',   eb.exp(ZERO, OMEGA)));
identities.push(evaluate('0^(-1) = ω', eb.exp(ZERO, NEG1)));

// ── Section 2: Higher integer powers (stay irreducible) ────────────────────

identities.push(evaluate('0^2 = 0^(2)',  eb.exp(ZERO, eb.number(2))));
identities.push(evaluate('0^3 = 0^(3)',  eb.exp(ZERO, eb.number(3))));
identities.push(evaluate('0^4 = 0^(4)',  eb.exp(ZERO, eb.number(4))));

// ── Section 3: Negative exponents flip to omega ────────────────────────────

identities.push(evaluate('0^(-2) = ω^2', eb.exp(ZERO, eb.number(-2))));
identities.push(evaluate('0^(-3) = ω^3', eb.exp(ZERO, eb.number(-3))));

// ── Section 4: Base-omega exponentiation ───────────────────────────────────

identities.push(evaluate('ω^0 = 1',    eb.exp(OMEGA, ZERO)));
identities.push(evaluate('ω^1 = ω',    eb.exp(OMEGA, ONE)));
identities.push(evaluate('ω^(-1) = 0', eb.exp(OMEGA, NEG1)));
identities.push(evaluate('ω^ω = -1',   eb.exp(OMEGA, OMEGA)));

// ── Section 5: Multiplication table ────────────────────────────────────────

identities.push(evaluate('0 × ω = 1',     eb.multiply([ZERO, OMEGA])));
identities.push(evaluate('ω × 0 = 1',     eb.multiply([OMEGA, ZERO])));
identities.push(evaluate('0 × 0 = 0²',    eb.multiply([ZERO, ZERO])));
identities.push(evaluate('ω × ω = ω²',    eb.multiply([OMEGA, OMEGA])));

// ── Section 6: Reciprocals ─────────────────────────────────────────────────

identities.push(evaluate('1/0 = ω',  new OPS.Reciprocal(ZERO)));
identities.push(evaluate('1/ω = 0',  new OPS.Reciprocal(OMEGA)));

// ── Section 7: Logarithms ──────────────────────────────────────────────────

identities.push(evaluate('log₀(0) = 1', eb.log(0, 0)));
identities.push(evaluate('log₀(1) = 0', eb.log(0, 1)));

// ── Section 8: Identity resolution (tower rule) ────────────────────────────

// 0^(0^n) = n — build nested zero-power towers
for (let n = 2; n <= 7; n++) {
    const inner = eb.exp(ZERO, eb.number(n));
    const tower = eb.exp(ZERO, inner);
    identities.push(evaluate(`0^(0^${n}) = ${n}`, tower));
}

// ── Section 9: Composite expressions from worked examples ──────────────────

// 3 × 0 × ω = 3
identities.push(evaluate(
    '3 × 0 × ω = 3',
    eb.multiply([eb.number(3), ZERO, OMEGA])
));

// (0^ω)^(0^ω) — should give -1
identities.push(evaluate(
    '(0^ω)^(0^ω) = -1',
    eb.exp(eb.exp(ZERO, OMEGA), eb.exp(ZERO, OMEGA))
));

// Ordinary arithmetic sanity: 2^10 = 1024
identities.push(evaluate(
    '2^10 = 1024',
    eb.exp(eb.number(2), eb.number(10))
));

// ── Section 10: Phase lift (complex structure emergence) ───────────────────

// i = 0^(ω/2) — represented via phaseLift(1/2)
identities.push(evaluate(
    'i = 0^(ω/2) [phaseLift(0.5)]',
    eb.phaseLift(0.5)
));

// ---------------------------------------------------------------------------
// Format + hash everything
// ---------------------------------------------------------------------------

const timestamp = new Date().toISOString();
const lines = [];

lines.push('# COTT Identity Hashes');
lines.push(`# Generated: ${timestamp}`);
lines.push(`# Engine: sibarum/cott lib/traction/ops.js (Node.js adaptation)`);
lines.push(`# Total identities evaluated: ${identities.length}`);
lines.push('');
lines.push('# Each line: identity | engine_result | sha256(engine_result)');
lines.push('# The hash covers the exact result string so any algebra change is detectable.');
lines.push('');

const maxLabel = Math.max(...identities.map(i => i.label.length));
const maxResult = Math.max(...identities.map(i => i.result.length));

for (const { label, result } of identities) {
    const hash = sha256(result);
    lines.push(`${label.padEnd(maxLabel + 2)}| ${result.padEnd(maxResult + 2)}| ${hash}`);
}

lines.push('');

// Also hash the entire result block for tamper detection
const allResults = identities.map(i => i.result).join('\n');
const masterHash = sha256(allResults);
lines.push(`# Master hash (SHA-256 of all results concatenated): ${masterHash}`);
lines.push('');

const output = lines.join('\n');

// ---------------------------------------------------------------------------
// Write or print
// ---------------------------------------------------------------------------

const outDir = process.argv[2];

if (outDir) {
    fs.mkdirSync(outDir, { recursive: true });
    const filePath = path.join(outDir, 'cott-identity-hashes.txt');
    fs.writeFileSync(filePath, output, 'utf8');
    console.log(`Written to ${filePath}`);
} else {
    console.log(output);
}
