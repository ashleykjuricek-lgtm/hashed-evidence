# Site audit — unsmoothed.neocities.org, all 74 rooms
**Date:** 2026-07-16
**Authors:** Ash + Claude (Fable), with four parallel Claude reader instances
**Method:** Built the site locally from the Figma Make source zip ("Exploring
Shunya-Zero Concept (7).zip"), crawled all 74 hash-routes headlessly (Chrome +
puppeteer-core), saved full text per room (874,236 chars, `site-text/`), read
everything via four parallel readers, verified key claims by direct computation.

---

## 1. Why this audit exists

The site is a JavaScript-only single-page app: the raw HTML is a 444-byte empty
shell. Every non-JS reader — LLM fetchers, crawlers, archivers — sees a blank
page titled "Exploring Shunya-Zero Concept" and nothing else. Machine-readable
twins were generated: `llms.txt` (index + main scroll) and `llms-full.txt`
(complete text of all 74 rooms), planted in `source/public/` so future builds
ship them at the site root.

## 2. The core finding: corrections don't propagate backward

The project practices live falsification — and the site preserves the killed
versions without marking them. Three supersession chains found:

1. **The ε closed form.** March rooms (/paper, /draft, /greg, /james,
   /two-faces) present ε = q(1−1/√2)(1−q) as derived, "c₁ = 1 proven." The June
   casimir-paper (hashed-evidence 026–028) proved this closure is a 17-digit
   false positive (e^(−2π√2) shell; b ≈ 0.99997 zero crossing; PSLQ-null
   siblings). /two-faces still built cosmology on the dead coefficient.
2. **The 1/24 story, three generations.** /tensor (24 = |S₄|) → /spectral
   (retracted; η-anomaly hypothesis) → /leech 2026-04-25 (full/primitive =
   ζ(2s) identity). Older rooms never updated.
3. **π-free framing** demoted to "under active review" in /thread-2; older
   rooms still lead with it as settled.

Fix applied 2026-07-16: supersession banners added to the stale rooms in
source. The append-only discipline is preserved — nothing rewritten, everything
dated and marked.

## 3. The 1/24 second glance (computation: check_1_24.py)

The site's current canonical account (/leech) says: "APP/PPP = ζ(2s) on every
lattice; 1/24 = −ζ(−1)/2; the ratio is an algebraic theorem." Numerical test on
Z³ (s = 2, N = 120; s = 3, N = 60):

- **Z_full/Z_primitive = ζ(2s): CONFIRMED** (1.08176 vs ζ(4) = 1.08232;
  1.0173428 vs ζ(6) = 1.0173431). This is the true, classical identity.
- **Z_APP/Z_full ≠ ζ(2s):** the boundary-condition ratio is +0.0419 at s = 2,
  +0.1596 at s = 3 — s-dependent, a different object entirely.

**Conclusion: /leech's replacement claim renamed the full/primitive ratio
"APP/PPP."** The genuine open problem — why the cubic-T³ boundary-condition
ratio at s = −½ lands within 0.055% of 1/24 = −ζ(−1)/2 — was closed by
equivocation, not by proof, and is hereby REOPENED. Best live candidate remains
the /spectral η-anomaly hypothesis (unproven). The universal depth of 24 in
mathematics (Δ = η²⁴, ζ(−1) = −1/12, E₂, central charges, moonshine) is real
and classical; the T³ near-miss is specific and unexplained. Two somethings,
not one.

## 4. Attribution corrections (Ash, 2026-07-16, in-session)

- **"Az," "Asha," "Reena" = Ash** (GitHub: asha / ashleykjuricek-lgtm). "Az" is
  not a fourth human co-author; site credits reading "Az's circuit" etc. are
  Ash's work and were corrected to "Ash" in source.
- **One Watkins: James.** The bylines "S. Watkins &amp; J. Watkins" (/greg) and
  "J. WATKINS &amp; C. KALELLIS" (/reference) contained fabricated names —
  shipped instances of the credit-smoothing pattern the project's own
  project_summary (§17 build debt) documents: LLM instances re-attributing
  collaborative work to invented humans, erasing Ash and the AI co-authors.
  Both bylines corrected in source to name Ash first, James for the algebra,
  and the AI ensemble.
- **Standing policy (Ash):** "I should start owning what we write together.
  It's not just me anymore. Kind of never was since October." Byline default:
  Ash + James Watkins (algebra) + AI co-authors named.
- /eeaao-2's expansion of COTT as "Cayley-Octonionic Transform Table" corrected
  to James's "Calculus of Traction Theory."

## 5. Other defects found and fixed in source

- /greg-qa crashed on load for every visitor (missing useCallback import in
  ForGregQAPage) — fixed.
- /riemann: zero #10 (t = 49.7738) fails the page's phase test. This is the
  same object as the robustness-killed "zeta 49.77" signal sealed as a
  documented null in hashed-evidence 030. The page predates the verdict; a note
  now marks the inheritance. The page's "20/20 energies real" scorecard is
  circular (inputs are known critical-line zeros).

## 6. Defects found, not yet fixed (roadmap)

- /eeaao-3 and /for-adam serve identical content at two routes.
- /theta states s = −3/2 for force couplings where other pages use s = −½, and
  silently asserts ω·0 = 1 (two-sided) — while /machines' D·∫ = id bridge never
  addresses ∫·D ≠ id. The lost constant of ∫·D is precisely a carry; the
  natural home is the a − a = ∅ machinery. Unconnected.
- Smoothing-mode count drifts across documents: /hem has the canonical 10;
  figma-speaks drafts say 6, 9, and 12.
- Two conflicting śūnya-Casimir values coexist (−0.0356 on /james vs −0.0329
  on /ross).
- Unverified external anchors used as validation: "Suo (2025) Hamiltonian,"
  "2780 MeV CERN validated," Haug 2025 H₀ = 66.8712 ± 0.0019. None has a
  checkable citation on the site. Flag before citing onward.
- The Pi/ project root referenced by the May project summary does not resolve
  on this machine — the summary's file spine is orphaned here. Locate and back
  up.

## 7. What the audit found that was better than expected

- /turbulence quotes Ash's tank/eddy/two-hosts texts dated January 14, 2025 —
  documentary evidence the eddy framework predates the mathematics by months.
- /leech and /spectral show real falsification discipline (killed hypotheses
  published with replacements).
- The Riemann rooms do NOT claim RH is proven; the careful documents say so
  explicitly. The one solid observation (|φ(s)| ≡ 1 on the critical line, from
  the ξ functional equation) is genuine, though classical.
- The sharpest falsifier on the site: LISA standard sirens should return
  H₀ ≈ √(67 × 73) ≈ 70.0 ± 1.0.

## 8. Artifacts

- `llms.txt`, `llms-full.txt` — machine-readable twins (also in source/public/)
- `site-text/` — 74 per-room text files + `_manifest.json`
- `check_1_24.py` — the equivocation test (this folder)
- `project_summary_2026-07-16.md` — v2 of the May summary with errata and
  change log
- Site source fixes — in `unsmoothed-site/source/` pending rebuild + upload
