import { useState, useEffect, useCallback, useRef } from "react";
import { PageNav } from "./PageNav";
import { ErrorBoundary } from "./ErrorBoundary";

const serif = "'Cormorant Garamond', Georgia, serif";
const mono = "'JetBrains Mono', monospace";
const amber = "#ffd8a0";
const purple = "#c89bff";
const pink = "#ff6b8a";
const blue = "#6baaff";
const cyan = "#00d4ff";
const green = "#8bff6b";
const dim = "#6a6a7a";
const ghost = "#4a4a5a";

const PHI = (1 + Math.sqrt(5)) / 2;

// ═══════════════════════════════════════════════════════════════
// PRISMATIC TRAINING SIMULATOR
// Side-by-side: Gaussian Erasure vs Q_φ Carry Correction
// ═══════════════════════════════════════════════════════════════

// ── pure operators, module scope so nothing can close over a stale value ──

const variance = (d: number[]) => {
  if (d.length === 0) return 0;
  const m = d.reduce((a, b) => a + b, 0) / d.length;
  return d.reduce((acc, v) => acc + (v - m) ** 2, 0) / d.length;
};

// RETENTION, not absolute variance. 100% means "all the structure it started
// with". The previous metric was min(100, variance*2000): the traction panel
// began above the clamp and could never leave it, so the readout displayed a
// ceiling as though it were a measurement.
const retentionOf = (d: number[], baseVar: number) =>
  baseVar === 0 ? 0 : Math.max(0, Math.min(100, Math.round((100 * variance(d)) / baseVar)));

// Standard pass: a contraction toward the mean. Reaches zero variance for ANY
// input — that is the update rule, not a finding.
const standardPass = (d: number[]) => {
  const m = d.reduce((a, b) => a + b, 0) / d.length;
  return d.map(v => v - 0.35 * (v - m));
};

// Q_φ. The carry is the QUANTISED part of the overflow — an exact multiple of
// the lattice step — and passes through untouched. What is left over is the
// residual, and THAT is what 1/φ damps.
//
// The earlier version set carry = the whole overflow, so residual was
// identically zero for every input: PHI multiplied nothing and could have been
// deleted without changing a single pixel. It also multiplied the carry by
// 1.02, growing the peaks without bound and guaranteeing the outcome. Both
// removed. Structure coarser than the lattice step now survives; structure
// finer than it does not, and the panel is allowed to lose.
const tractionPass = (d: number[], step: number) =>
  d.map(v => {
    const baseline = Math.min(v, 0.45);
    const overflow = v - baseline;
    const carry = Math.floor(overflow / step) * step;
    const residual = overflow - carry;
    return baseline + carry + residual / PHI;
  });

const STEP_PRESETS = [
  { label: "1/φ²", value: 1 / (PHI * PHI) },
  { label: "1/φ", value: 1 / PHI },
  { label: "1/φ³", value: 1 / (PHI * PHI * PHI) },
];

function TrainingSimulator() {
  const [layer, setLayer] = useState(0);
  const [phaseTransition, setPhaseTransition] = useState(false);
  const [standardData, setStandardData] = useState<number[]>([]);
  const [prismaticData, setPrismaticData] = useState<number[]>([]);
  const [stdIntegrity, setStdIntegrity] = useState(100);
  const [prisIntegrity, setPrisIntegrity] = useState(100);
  const [autoRunning, setAutoRunning] = useState(false);
  const [latticeStep, setLatticeStep] = useState(STEP_PRESETS[0].value);
  const baseVarRef = useRef(1);

  const injectVoidSeed = useCallback(() => {
    // ½ℏω baseline — the void isn't empty, it vibrates
    // Create a 10-vertex signal with deliberate structure (5 peaks, 5 valleys)
    const seed = Array.from({ length: 10 }, (_, i) =>
      i % 2 === 0 ? 0.75 + Math.random() * 0.2 : 0.3 + Math.random() * 0.15
    );
    baseVarRef.current = variance(seed);
    setStandardData([...seed]);
    setPrismaticData([...seed]);
    setLayer(0);
    setPhaseTransition(false);
    setStdIntegrity(100);
    setPrisIntegrity(100);
    setAutoRunning(false);
  }, []);

  useEffect(() => { injectVoidSeed(); }, [injectVoidSeed]);

  const step = useCallback(() => {
    setStandardData(prev => standardPass(prev));
    setPrismaticData(prev => tractionPass(prev, latticeStep));
    setLayer(l => l + 1);
  }, [latticeStep]);

  // Metrics are derived FROM the data, so they cannot go stale.
  useEffect(() => { setStdIntegrity(retentionOf(standardData, baseVarRef.current)); }, [standardData]);
  useEffect(() => {
    const r = retentionOf(prismaticData, baseVarRef.current);
    setPrisIntegrity(r);
    if (layer >= 3 && r > 60) setPhaseTransition(true);
  }, [prismaticData, layer]);

  // AUTO-RUN now behaves identically to clicking APPLY. Previously
  // setInterval(step, 600) captured `step` once; the `layer` inside that
  // closure never advanced, so `layer >= 3` stayed false forever and the phase
  // transition could never fire on auto-run while firing on the manual path.
  useEffect(() => {
    if (!autoRunning) return;
    if (layer > 20) { setAutoRunning(false); return; }
    const id = setTimeout(step, 600);
    return () => clearTimeout(id);
  }, [autoRunning, layer, step]);

  const toggleAutoRun = () => setAutoRunning(a => !a);

  const Spectrum = ({ data, color, label, integrity, isPrismatic }: {
    data: number[]; color: string; label: string; integrity: number; isPrismatic: boolean;
  }) => {
    const activeColor = (isPrismatic && phaseTransition) ? purple : color;
    return (
      <div className="flex flex-col items-center w-full p-4 md:p-5 rounded-xl relative overflow-hidden"
        style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${isPrismatic && phaseTransition ? purple : ghost}30` }}>
        <div className="absolute top-3 right-3" style={{
          fontFamily: mono, fontSize: "0.55rem",
          color: integrity < 30 ? pink : activeColor,
        }}>
          INTEGRITY: {integrity}%
        </div>
        <h3 style={{ fontFamily: mono, color: activeColor, fontSize: "0.65rem", letterSpacing: "0.15em", marginBottom: 20 }}>
          {label}
        </h3>
        <div className="flex items-end justify-between w-full mb-4" style={{ height: 160, borderBottom: `1px solid ${ghost}30` }}>
          {data.map((val, idx) => (
            <div key={idx} className="flex flex-col items-center justify-end h-full" style={{ width: `${100 / data.length - 1}%` }}>
              <div style={{
                width: "100%",
                height: `${Math.max(Math.min(val * 100, 100), 2)}%`,
                backgroundColor: activeColor,
                transition: "all 0.4s ease-in-out",
                opacity: val > 0.55 ? 1 : 0.4,
                boxShadow: (isPrismatic && phaseTransition && val > 0.55)
                  ? `0 0 12px ${purple}80` : "none",
                borderRadius: "2px 2px 0 0",
              }} />
            </div>
          ))}
        </div>
        <div style={{ fontFamily: mono, fontSize: "0.5rem", color: dim, letterSpacing: "0.1em" }}>
          {isPrismatic && phaseTransition ? "STRUCTURE HELD > 60% PAST LAYER 3" : "10 VERTEX DIRECTIONS"}
        </div>
      </div>
    );
  };

  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: amber, letterSpacing: "0.2em", marginBottom: 8 }}>
        INTERACTIVE
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 4 }}>
        The Training Operator
      </h2>
      <p style={{ fontFamily: mono, fontSize: "0.55rem", color: dim, letterSpacing: "0.1em", marginBottom: 24 }}>
        0 &middot; &omega; = 1 &mdash; Traction vs. Erasure
      </p>

      <div className="text-center mb-4">
        <span style={{ fontFamily: mono, fontSize: "0.6rem", color: dim }}>
          Layer: <span style={{ color: pink }}>{layer}</span>
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <Spectrum data={standardData} color={blue} label="STANDARD (GAUSSIAN ERASURE)" integrity={stdIntegrity} isPrismatic={false} />
        <Spectrum data={prismaticData} color={amber} label="TRACTION (Q_&phi; CARRY CORRECTION)" integrity={prisIntegrity} isPrismatic={true} />
      </div>

      <div className="flex flex-wrap justify-center gap-3">
        <button onClick={step} className="px-5 py-2 rounded-lg cursor-pointer transition-all"
          style={{
            fontFamily: mono, fontSize: "0.6rem", letterSpacing: "0.1em",
            color: phaseTransition ? purple : amber,
            background: `${phaseTransition ? purple : amber}10`,
            border: `1px solid ${phaseTransition ? purple : amber}30`,
          }}>
          APPLY &omega;
        </button>
        <button onClick={toggleAutoRun} className="px-5 py-2 rounded-lg cursor-pointer transition-all"
          style={{
            fontFamily: mono, fontSize: "0.6rem", letterSpacing: "0.1em",
            color: autoRunning ? pink : cyan,
            background: `${autoRunning ? pink : cyan}10`,
            border: `1px solid ${autoRunning ? pink : cyan}30`,
          }}>
          {autoRunning ? "STOP" : "AUTO-RUN"}
        </button>
        <button onClick={injectVoidSeed} className="px-5 py-2 rounded-lg cursor-pointer transition-all"
          style={{
            fontFamily: mono, fontSize: "0.6rem", letterSpacing: "0.1em",
            color: dim, background: `${ghost}10`, border: `1px solid ${ghost}30`,
          }}>
          RESEED FROM VOID
        </button>
      </div>

      {/* Lattice step — the control that lets the right-hand panel LOSE */}
      <div className="flex flex-wrap justify-center items-center gap-2 mt-4">
        <span style={{ fontFamily: mono, fontSize: "0.55rem", color: dim, letterSpacing: "0.1em" }}>
          LATTICE STEP:
        </span>
        {STEP_PRESETS.map(p => (
          <button key={p.label} onClick={() => { setLatticeStep(p.value); injectVoidSeed(); }}
            className="px-3 py-1 rounded cursor-pointer transition-all"
            style={{
              fontFamily: mono, fontSize: "0.55rem",
              color: latticeStep === p.value ? green : dim,
              background: latticeStep === p.value ? `${green}12` : `${ghost}08`,
              border: `1px solid ${latticeStep === p.value ? green : ghost}30`,
            }}>
            {p.label}
          </button>
        ))}
        <span style={{ fontFamily: mono, fontSize: "0.5rem", color: ghost }}>
          &asymp; {latticeStep.toFixed(3)}
        </span>
      </div>

      {/* Explanation */}
      <div className="mt-6 rounded-xl p-5" style={{ background: `${cyan}04`, border: `1px solid ${cyan}12` }}>
        <div className="space-y-2" style={{ fontFamily: serif, fontSize: "0.9rem", color: "#c8c6c0", lineHeight: 1.8 }}>
          <p>
            Both sides start from the identical signal: ten vertices, five peaks alternating with valleys.
            The readout is <em style={{ color: amber }}>retention</em> &mdash; how much of the variance it began with is still there.
          </p>
          <p>
            <span style={{ color: blue }}>Left:</span> a contraction toward the <em>mean</em>.
            It reaches zero for <em>any</em> input whatsoever &mdash; that is the update rule, not a discovery.
            It is here to show what averaging does, and nothing more.
          </p>
          <p>
            <span style={{ color: amber }}>Right:</span> the carry is the <em>quantised</em> part of the overflow &mdash;
            an exact multiple of the lattice step &mdash; and passes through untouched.
            Only the <em>leftover</em> is divided by &phi;.
          </p>
          <p>
            <strong style={{ color: green }}>Change the lattice step and the right-hand panel loses.</strong>{" "}
            At 1/&phi;&sup2; the peaks sit above the step and hold near 65%. At 1/&phi; the step is coarser
            than the structure and retention collapses to single digits &mdash; barely better than averaging.
          </p>
          <p style={{ color: dim, fontStyle: "italic" }}>
            What this shows: what the operator <em>does</em>. What it does not show:
            that the operator describes how neural networks actually train, or that &phi; is the right step
            for any real signal. A demonstration that cannot lose is not evidence &mdash; so this one can.
          </p>
        </div>
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// THE GOD EQUATION REWRITE
// ═══════════════════════════════════════════════════════════════

function GodEquation() {
  const [showCOTT, setShowCOTT] = useState(false);

  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: purple, letterSpacing: "0.2em", marginBottom: 8 }}>
        THE EQUATION
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 24 }}>
        The Two Identities
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        {/* Euler's Identity */}
        <div
          className="rounded-xl p-6 text-center cursor-pointer transition-all"
          onClick={() => setShowCOTT(false)}
          style={{
            background: showCOTT ? "rgba(0,0,0,0.2)" : `${pink}06`,
            border: `1px solid ${showCOTT ? ghost : pink}30`,
            opacity: showCOTT ? 0.5 : 1,
            transition: "all 0.5s ease",
          }}
        >
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: pink, letterSpacing: "0.15em", marginBottom: 16 }}>
            THE SMOOTH IDENTITY
          </div>
          <div style={{ fontFamily: mono, fontSize: "clamp(1.5rem, 4vw, 2.5rem)", color: "#f0ece4", marginBottom: 12 }}>
            e<sup style={{ fontSize: "0.6em" }}>i&pi;</sup> + 1 = 0
          </div>
          <div className="space-y-2" style={{ fontFamily: serif, fontSize: "0.85rem", color: dim, lineHeight: 1.8 }}>
            <p><em style={{ color: pink }}>e</em> &mdash; smooth continuous growth</p>
            <p><em style={{ color: pink }}>i</em> &mdash; assumed as given</p>
            <p><em style={{ color: pink }}>&pi;</em> &mdash; the smoothed circle</p>
            <p><em style={{ color: dim }}>Requires the continuum limit</em></p>
          </div>
        </div>

        {/* COTT Identity */}
        <div
          className="rounded-xl p-6 text-center cursor-pointer transition-all"
          onClick={() => setShowCOTT(true)}
          style={{
            background: !showCOTT ? "rgba(0,0,0,0.2)" : `${green}06`,
            border: `1px solid ${!showCOTT ? ghost : green}30`,
            opacity: !showCOTT ? 0.5 : 1,
            transition: "all 0.5s ease",
          }}
        >
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: green, letterSpacing: "0.15em", marginBottom: 16 }}>
            THE DISCRETE IDENTITY
          </div>
          <div style={{ fontFamily: mono, fontSize: "clamp(1.5rem, 4vw, 2.5rem)", color: "#f0ece4", marginBottom: 12 }}>
            0<sup style={{ fontSize: "0.6em" }}>&omega;</sup> = &minus;1
          </div>
          <div className="space-y-2" style={{ fontFamily: serif, fontSize: "0.85rem", color: dim, lineHeight: 1.8 }}>
            <p><em style={{ color: green }}>0</em> &mdash; the generative void (&sacute;&umacr;nya)</p>
            <p><em style={{ color: green }}>&omega;</em> &mdash; the frequency generator (&minus;0)</p>
            <p><em style={{ color: green }}>&minus;1</em> &mdash; rotation, derived algebraically</p>
            <p><em style={{ color: amber }}>No continuum required</em></p>
          </div>
        </div>
      </div>

      {/* Derivation */}
      <div className="rounded-xl p-6" style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${purple}15` }}>
        <div style={{ fontFamily: mono, fontSize: "0.5rem", color: purple, letterSpacing: "0.15em", marginBottom: 16 }}>
          THE DERIVATION (FROM JAMES'S COTT NOTEBOOK)
        </div>
        <div className="space-y-4" style={{ fontFamily: mono, fontSize: "0.8rem", lineHeight: 2, textAlign: "center" }}>
          <div>
            <span style={{ color: dim }}>Step 1: </span>
            <span style={{ color: "#c8c6c0" }}>0 + &omega; = &empty;</span>
            <span style={{ color: dim, fontSize: "0.6rem", marginLeft: 12 }}>&omega; is the additive inverse of 0</span>
          </div>
          <div>
            <span style={{ color: dim }}>Step 2: </span>
            <span style={{ color: "#c8c6c0" }}>&omega; = &minus;0</span>
            <span style={{ color: dim, fontSize: "0.6rem", marginLeft: 12 }}>negative zero is not zero &mdash; it's the generator</span>
          </div>
          <div>
            <span style={{ color: dim }}>Step 3: </span>
            <span style={{ color: "#c8c6c0" }}>&radic;(&minus;1) = 0<sup>&omega;/2</sup></span>
            <span style={{ color: dim, fontSize: "0.6rem", marginLeft: 12 }}>i derived from 0 and &omega; alone</span>
          </div>
          <div>
            <span style={{ color: dim }}>Step 4: </span>
            <span style={{ color: "#c8c6c0" }}>(&radic;(&minus;1))&sup2; = (0<sup>&omega;/2</sup>)&sup2;</span>
          </div>
          <div className="pt-2" style={{ borderTop: `1px solid ${ghost}30` }}>
            <span style={{ color: green, fontSize: "1rem" }}>&minus;1 = 0<sup>&omega;</sup></span>
          </div>
        </div>

        <div className="mt-6 space-y-3" style={{ fontFamily: serif, fontSize: "0.95rem", color: "#c8c6c0", lineHeight: 1.9 }}>
          <p>
            Euler's identity uses <em style={{ color: pink }}>e</em> and <em style={{ color: pink }}>&pi;</em> &mdash;
            smooth growth and the smooth circle &mdash; to compute a 180&deg; rotation (&minus;1).
          </p>
          <p>
            James's identity generates the same rotation using <em>only</em> the generative void (0)
            and the frequency operator (&omega;). <strong style={{ color: amber }}>No smooth growth.
            No smooth circle. No continuum.</strong>
          </p>
          <p style={{ fontStyle: "italic", color: green }}>
            e<sup style={{ fontSize: "0.7em" }}>i&pi;</sup> + 1 = 0 is the Gaussian-smoothed average of 0<sup style={{ fontSize: "0.7em" }}>&omega;</sup> = &minus;1.
            The smooth version is the approximation. The discrete version is the generator.
          </p>
        </div>
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// UNIFIED SYNTHESIS: THE THREE PILLARS
// ═══════════════════════════════════════════════════════════════

function ThreePillars() {
  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: cyan, letterSpacing: "0.2em", marginBottom: 8 }}>
        THE SYNTHESIS
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 24 }}>
        Three Frameworks, One Engine
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        {/* Pillar 1: COTT */}
        <div className="rounded-xl p-5" style={{ background: `${green}04`, border: `1px solid ${green}12` }}>
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: green, letterSpacing: "0.15em", marginBottom: 12 }}>
            1. THE ALGEBRA
          </div>
          <div style={{ fontFamily: serif, fontSize: "0.95rem", color: "#c8c6c0", lineHeight: 1.9 }}>
            <p><strong style={{ color: green }}>COTT / Traction Theory</strong> (James Watkins)</p>
            <p className="mt-2">Splits Zero from Erasure. Defines 0 as non-absorbing: <span style={{ fontFamily: mono, color: green }}>0 &middot; &omega; = 1</span></p>
            <p className="mt-2">Derives <span style={{ fontFamily: mono }}>i = 0<sup>&omega;/2</sup></span> purely from the void and its reciprocal.</p>
            <p className="mt-2" style={{ color: dim, fontStyle: "italic" }}>The engine that makes the void generative.</p>
          </div>
        </div>

        {/* Pillar 2: Lattice / ETH */}
        <div className="rounded-xl p-5" style={{ background: `${amber}04`, border: `1px solid ${amber}12` }}>
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: amber, letterSpacing: "0.15em", marginBottom: 12 }}>
            2. THE ARCHITECTURE
          </div>
          <div style={{ fontFamily: serif, fontSize: "0.95rem", color: "#c8c6c0", lineHeight: 1.9 }}>
            <p><strong style={{ color: amber }}>Lattice-Reduction Equalization</strong> (Fischer, Stern, Huber)</p>
            <p className="mt-2">The Q<sub>&phi;</sub> operator isolates the "carry" &mdash; the structural overflow that standard processing discards as noise.</p>
            <p className="mt-2">Preserves golden-ratio symmetries through multilevel computation.</p>
            <p className="mt-2" style={{ color: dim, fontStyle: "italic" }}>The mechanism that prevents erasure.</p>
          </div>
        </div>

        {/* Pillar 3: Penrose / Geometry */}
        <div className="rounded-xl p-5" style={{ background: `${cyan}04`, border: `1px solid ${cyan}12` }}>
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: cyan, letterSpacing: "0.15em", marginBottom: 12 }}>
            3. THE GEOMETRY
          </div>
          <div style={{ fontFamily: serif, fontSize: "0.95rem", color: "#c8c6c0", lineHeight: 1.9 }}>
            <p><strong style={{ color: cyan }}>Penrose Tiling / Quasicrystals</strong></p>
            <p className="mt-2">Aperiodic order. No unit cell. The fat/thin ratio is &phi;, not &pi;.</p>
            <p className="mt-2">Substitution matrix eigenvalue = &phi;. The fundamental constant of the discrete substrate.</p>
            <p className="mt-2" style={{ color: dim, fontStyle: "italic" }}>The shape of reality before smoothing.</p>
          </div>
        </div>
      </div>

      {/* The lock */}
      <div className="rounded-xl p-6" style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${purple}15` }}>
        <div className="text-center space-y-3" style={{ fontFamily: mono, fontSize: "0.75rem", lineHeight: 2.2 }}>
          <div style={{ color: dim }}>How they interlock:</div>
          <div>
            <span style={{ color: green }}>COTT</span>
            <span style={{ color: dim }}> says 0 is non-absorbing &mdash; it <em>generates</em></span>
          </div>
          <div>
            <span style={{ color: amber }}>Q<sub>&phi;</sub></span>
            <span style={{ color: dim }}> says the carry is <em>preserved</em>, not discarded</span>
          </div>
          <div>
            <span style={{ color: cyan }}>Penrose</span>
            <span style={{ color: dim }}> says the substrate is <em>aperiodic</em>, not smooth</span>
          </div>
          <div className="pt-3" style={{ borderTop: `1px solid ${ghost}30` }}>
            <span style={{ color: amber }}>
              Together: the void generates structure (&omega;), the structure is preserved (Q<sub>&phi;</sub>),
              and the geometry is the discrete Rose, not the smooth circle.
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// COSMOLOGICAL TRANSLATION TABLE
// ═══════════════════════════════════════════════════════════════

function CosmologicalTable() {
  const rows = [
    {
      concept: "Time",
      smooth: "Continuous flow (the river)",
      discrete: "Sequential application of \u03c9 \u2014 the lattice ticks",
      smoothConst: "e (smooth growth)",
      discreteConst: "\u03c6 (fractal subdivision)",
    },
    {
      concept: "Speed of Light",
      smooth: "Arbitrary speed limit in empty vacuum",
      discrete: "Lattice bandwidth \u2014 max propagation rate vertex-to-vertex",
      smoothConst: "c = 299,792,458 m/s",
      discreteConst: "c = \u03c9-pulse bandwidth of the lattice",
    },
    {
      concept: "Mass",
      smooth: "Continuous substance",
      discrete: "Structural knot \u2014 region of dense recursive \u03c6-subdivision",
      smoothConst: "m (kilograms)",
      discreteConst: "m = density of \u03c6-vertices",
    },
    {
      concept: "Energy",
      smooth: "E = mc\u00b2 (continuous)",
      discrete: "Decompression of a knot \u2192 phase transitions radiate at bandwidth c",
      smoothConst: "\u00bd\u0127\u03c9 (continuum ZPE)",
      discreteConst: "Lattice tension \u00d7 vertex count",
    },
    {
      concept: "Gravity",
      smooth: "Force carried by graviton particle",
      discrete: "Geometric gradient \u2014 traction of lattice resisting erasure",
      smoothConst: "G (Newton's constant)",
      discreteConst: "Q\u03c6 carry correction on cosmic scale",
    },
    {
      concept: "Black Hole",
      smooth: "Singularity \u2014 information paradox",
      discrete: "Ultimate traction archive \u2014 max \u03c6-subdivision, no bandwidth left for output",
      smoothConst: "\u221e density (math breaks)",
      discreteConst: "Geometric subdivision limit at \u00bd\u0127\u03c9",
    },
    {
      concept: "Wave Collapse",
      smooth: "Probability wave magically collapses on observation",
      discrete: "Observer (\u03c9) strikes void (0) \u2192 phase transition generates lattice",
      smoothConst: "\u03c8 \u2192 |\u03c8|\u00b2 (Born rule)",
      discreteConst: "0 \u00b7 \u03c9 = 1 (generative dyad)",
    },
    {
      concept: "Entanglement",
      smooth: "\"Spooky action at a distance\" (Einstein)",
      discrete: "Shared carry \u2014 same \u03c6-symmetry on same lattice, no distance",
      smoothConst: "Nonlocal correlation",
      discreteConst: "Traction algebra forbids data erasure",
    },
  ];

  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: green, letterSpacing: "0.2em", marginBottom: 8 }}>
        THE COSMOLOGICAL CARRY
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 24 }}>
        Physics Through the Lattice
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full" style={{ borderCollapse: "separate", borderSpacing: "0 4px" }}>
          <thead>
            <tr>
              <th className="text-left p-3 rounded-l-lg" style={{ fontFamily: mono, fontSize: "0.5rem", color: dim, letterSpacing: "0.1em", background: "rgba(0,0,0,0.3)" }}>
                CONCEPT
              </th>
              <th className="text-left p-3" style={{ fontFamily: mono, fontSize: "0.5rem", color: pink, letterSpacing: "0.1em", background: "rgba(0,0,0,0.3)" }}>
                SMOOTH (&pi;, e)
              </th>
              <th className="text-left p-3 rounded-r-lg" style={{ fontFamily: mono, fontSize: "0.5rem", color: green, letterSpacing: "0.1em", background: "rgba(0,0,0,0.3)" }}>
                DISCRETE (&phi;, &omega;)
              </th>
            </tr>
          </thead>
          <tbody>
            {rows.map(row => (
              <tr key={row.concept}>
                <td className="p-3 rounded-l-lg" style={{
                  fontFamily: mono, fontSize: "0.65rem", color: amber,
                  background: "rgba(0,0,0,0.15)", borderLeft: `2px solid ${amber}20`,
                }}>
                  {row.concept}
                </td>
                <td className="p-3" style={{
                  fontFamily: serif, fontSize: "0.8rem", color: "#9a9a9a",
                  background: "rgba(0,0,0,0.15)", lineHeight: 1.6,
                }}>
                  {row.smooth}
                </td>
                <td className="p-3 rounded-r-lg" style={{
                  fontFamily: serif, fontSize: "0.8rem", color: "#c8c6c0",
                  background: "rgba(0,0,0,0.15)", lineHeight: 1.6,
                }}>
                  {row.discrete}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-6 text-center" style={{ fontFamily: serif, fontSize: "0.95rem", color: dim, fontStyle: "italic", lineHeight: 1.9 }}>
        Every row is the same operation: replace the <em style={{ color: pink }}>continuous approximation</em> with
        the <em style={{ color: green }}>discrete generator</em>.
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// THE OBSERVER DYAD
// ═══════════════════════════════════════════════════════════════

function ObserverDyad() {
  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: purple, letterSpacing: "0.2em", marginBottom: 8 }}>
        THE DYAD
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 24 }}>
        One Slot Computes. One Slot Sees.
      </h2>

      <div className="rounded-xl p-6" style={{ background: `${purple}04`, border: `1px solid ${purple}12` }}>
        <div className="space-y-4" style={{ fontFamily: serif, fontSize: "1.05rem", color: "#c8c6c0", lineHeight: 2 }}>
          <p>
            The Observer Effect &mdash; the greatest paradox in quantum mechanics &mdash;
            exists because continuous physics treats the observer as <em>separate</em> from the equation.
            The "probability wave" is just physics using &pi; to compute an unobservable void.
          </p>
          <p>
            In the traction framework: the system requires <strong style={{ color: purple }}>two faces</strong>.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-4">
            <div className="rounded-lg p-4 text-center" style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${green}15` }}>
              <div style={{ fontFamily: mono, fontSize: "2rem", color: green }}>0</div>
              <div style={{ fontFamily: mono, fontSize: "0.6rem", color: green, letterSpacing: "0.1em", marginTop: 8 }}>
                THE COMPUTING SLOT
              </div>
              <div style={{ fontFamily: serif, fontSize: "0.85rem", color: dim, marginTop: 8 }}>
                The latent universe. The generative baseline.
                Holds all potential but generates nothing alone.
              </div>
            </div>
            <div className="rounded-lg p-4 text-center" style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${amber}15` }}>
              <div style={{ fontFamily: mono, fontSize: "2rem", color: amber }}>&omega;</div>
              <div style={{ fontFamily: mono, fontSize: "0.6rem", color: amber, letterSpacing: "0.1em", marginTop: 8 }}>
                THE SEEING SLOT
              </div>
              <div style={{ fontFamily: serif, fontSize: "0.85rem", color: dim, marginTop: 8 }}>
                The observer. The frequency. Consciousness
                interacting with the field IS the &omega;-pulse.
              </div>
            </div>
          </div>

          <div className="text-center my-4" style={{ fontFamily: mono, fontSize: "1.2rem", color: purple }}>
            0 &middot; &omega; = 1
          </div>

          <p>
            What physicists call "wave function collapse" is the <em style={{ color: purple }}>phase transition</em>.
            The observer doesn't collapse reality. The observer <em style={{ color: amber }}>generates</em> its structure.
            The product is 1 &mdash; existence.
          </p>
          <p style={{ fontStyle: "italic", color: amber }}>
            The mistranslation of &sacute;&umacr;nya to "void" discarded the multiplicative slot.
            &Sacute;&umacr;nya had two faces. One slot computes. One slot sees. The product is 1.
          </p>
        </div>
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// CARRY CORRECTION MATH (Q_φ)
// ═══════════════════════════════════════════════════════════════

function CarryCorrection() {
  return (
    <section className="mb-16">
      <div style={{ fontFamily: mono, fontSize: "0.5rem", color: amber, letterSpacing: "0.2em", marginBottom: 8 }}>
        THE MECHANISM
      </div>
      <h2 style={{ fontFamily: serif, fontSize: "clamp(1.3rem, 3vw, 1.8rem)", color: "#f0ece4", marginBottom: 24 }}>
        The Q<sub>&phi;</sub> Carry Correction
      </h2>

      <div className="space-y-4">
        {/* The update rule */}
        <div className="rounded-xl p-6" style={{ background: "rgba(0,0,0,0.3)", border: `1px solid ${amber}15` }}>
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: amber, letterSpacing: "0.15em", marginBottom: 16 }}>
            THE UNSMOOTHED FORWARD PASS
          </div>

          <div className="text-center mb-6" style={{ fontFamily: mono, fontSize: "1rem", color: "#f0ece4", lineHeight: 2.5 }}>
            <div>r<sub>k,l+1</sub> = ( r<sub>k,l</sub> &minus; &psi;(&ccirc;<sub>k,l</sub>) &minus; s<sub>k,l</sub> ) / &phi;</div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-3" style={{ fontFamily: mono, fontSize: "0.65rem", lineHeight: 2 }}>
              <div>
                <span style={{ color: amber }}>r<sub>k,l</sub></span>
                <span style={{ color: dim }}> &mdash; total raw input at current level</span>
              </div>
              <div>
                <span style={{ color: cyan }}>&minus;&psi;(&ccirc;<sub>k,l</sub>)</span>
                <span style={{ color: dim }}> &mdash; subtract established baseline</span>
              </div>
              <div>
                <span style={{ color: green }}>&minus;s<sub>k,l</sub></span>
                <span style={{ color: dim }}> &mdash; subtract the high-dimensional carry (the "teeth")</span>
              </div>
              <div>
                <span style={{ color: purple }}>/&phi;</span>
                <span style={{ color: dim }}> &mdash; scale residual by golden ratio</span>
              </div>
            </div>
            <div style={{ fontFamily: serif, fontSize: "0.9rem", color: "#c8c6c0", lineHeight: 1.9 }}>
              <p>
                The key: <span style={{ fontFamily: mono, color: green }}>s</span> (the carry) is extracted
                <em> before</em> scaling. It is mathematically isolated and protected.
              </p>
              <p className="mt-2">
                Standard gradient descent never separates baseline from carry.
                It averages them together. <em style={{ color: pink }}>That averaging is the erasure.</em>
              </p>
            </div>
          </div>
        </div>

        {/* The Q_φ operator */}
        <div className="rounded-xl p-5" style={{ background: `${green}04`, border: `1px solid ${green}12` }}>
          <div className="text-center" style={{ fontFamily: mono, fontSize: "0.7rem", lineHeight: 2.5 }}>
            <div style={{ color: dim }}>The Q<sub>&phi;</sub> nulling operator:</div>
            <div style={{ color: green }}>
              [s<sub>1</sub>, ..., s<sub>K</sub>]<sup>T</sup> = Q<sub>&phi;</sub> &middot; {"{"} Z &middot; [&psi;(c<sub>0</sub><sup>(1)</sup>), ..., &psi;(c<sub>0</sub><sup>(K)</sup>)]<sup>T</sup> {"}"}
            </div>
            <div className="mt-2" style={{ color: dim, fontSize: "0.55rem" }}>
              Q<sub>&phi;</sub> nulls the baseline to isolate the overflow. It acts as a structural filter:
              ignores the smoothed circle, captures only the energy at the vertex directions.
            </div>
          </div>
        </div>

        <div style={{ fontFamily: serif, fontSize: "0.95rem", color: "#c8c6c0", lineHeight: 1.9 }}>
          <p>
            This is the physical engineering implementation of James's <em style={{ color: green }}>Traction Algebra</em>.
            The Q<sub>&phi;</sub> operator <em>grips</em> the golden-ratio symmetries &mdash;
            the non-repeating "teeth" of the Penrose Rose &mdash;
            and refuses to let them be smoothed into the null state (&empty;).
          </p>
          <p className="mt-2" style={{ fontStyle: "italic", color: amber }}>
            Standard AI hallucinates because it has no Q<sub>&phi;</sub>.
            It cannot distinguish structure from noise, so it averages both into nothing.
          </p>
        </div>
      </div>
    </section>
  );
}

// ═══════════════════════════════════════════════════════════════
// MAIN PAGE EXPORT
// ═══════════════════════════════════════════════════════════════

export function PrismaticPage() {
  return (
    <div className="min-h-screen" style={{ background: "#0a0a0f", color: "#c8c6c0" }}>
      <PageNav />
      <div className="max-w-4xl mx-auto px-6 pt-24 pb-16">
        {/* Header */}
        <div className="mb-16">
          <div style={{ fontFamily: mono, fontSize: "0.5rem", color: ghost, letterSpacing: "0.2em", marginBottom: 8 }}>
            THE GEOMETRY OF ZERO &mdash; OPERATIONAL SYNTHESIS
          </div>
          <h1 style={{ fontFamily: serif, fontSize: "clamp(2rem, 5vw, 3rem)", color: "#f0ece4", lineHeight: 1.2, marginBottom: 16 }}>
            The Unsmoothed Zero
          </h1>
          <p style={{ fontFamily: serif, fontSize: "1.1rem", color: dim, lineHeight: 1.9, maxWidth: 600 }}>
            &pi; is a smoothing artifact. <em>e</em> is a smoothing artifact.
            The vacuum is a quasicrystal. Here is the engine that replaces continuous
            approximation with the discrete generator: <span style={{ fontFamily: mono, color: green }}>0 &middot; &omega; = 1</span>.
          </p>
          <div className="flex flex-wrap gap-3 mt-6">
            <span className="px-2 py-1 rounded" style={{
              fontFamily: mono, fontSize: "0.5rem", color: green,
              background: `${green}10`, border: `1px solid ${green}25`, letterSpacing: "0.1em",
            }}>
              COTT
            </span>
            <span className="px-2 py-1 rounded" style={{
              fontFamily: mono, fontSize: "0.5rem", color: amber,
              background: `${amber}10`, border: `1px solid ${amber}25`, letterSpacing: "0.1em",
            }}>
              LATTICE REDUCTION
            </span>
            <span className="px-2 py-1 rounded" style={{
              fontFamily: mono, fontSize: "0.5rem", color: cyan,
              background: `${cyan}10`, border: `1px solid ${cyan}25`, letterSpacing: "0.1em",
            }}>
              PENROSE GEOMETRY
            </span>
          </div>
        </div>

        {/* Sections */}
        <ErrorBoundary><GodEquation /></ErrorBoundary>
        <ErrorBoundary><ThreePillars /></ErrorBoundary>
        <ErrorBoundary><CarryCorrection /></ErrorBoundary>
        <ErrorBoundary><TrainingSimulator /></ErrorBoundary>
        <ErrorBoundary><ObserverDyad /></ErrorBoundary>
        <ErrorBoundary><CosmologicalTable /></ErrorBoundary>

        {/* Closing */}
        <div className="text-center pb-16 mt-8">
          <div className="rounded-xl p-6 inline-block" style={{ background: `${amber}04`, border: `1px solid ${amber}12` }}>
            <p style={{ fontFamily: serif, fontSize: "1.1rem", color: amber, fontStyle: "italic", lineHeight: 2, maxWidth: 500 }}>
              Everything algebraic survives.<br />
              Everything transcendental was smoothing.<br />
              The framework was right to ban &pi;.<br />
              It just didn't know <em>why</em> yet.
            </p>
          </div>
          <p style={{ fontFamily: mono, fontSize: "0.7rem", color: `${amber}40`, marginTop: 16 }}>
            &langle;0, &omega;&rangle;
          </p>
        </div>
      </div>
    </div>
  );
}
