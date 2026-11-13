# Universal Research Methodology and Discovery Protocols

This document defines the formal scientific principles, simulation standards, hypothesis structures, and validation rules governing all work in the AI Edison discovery repository.

## 1. The Universal In Silico Discovery Standard

Historically, an inventor proposed a single hypothesis, manually synthesized a material or fabricated a device, and tested it serially. This trial-and-error loop is replaced by automated computational search across 10,000+ virtual trials:

1. **Broad Domain Agnosticism:** The AI Edison framework applies to any inventive problem that can be simulated: novel materials, chemical catalysts, alternative thermodynamic cycles, kinetic mechanisms, or computing substrates.
2. **First-Principles Constraints:** Every simulation is strictly bound by fundamental physical laws:
   * Mass and Energy Conservation ($\sum \dot{E}_{in} = \sum \dot{E}_{out} + \frac{dE_{sys}}{dt}$)
   * Momentum Conservation ($\sum \mathbf{F} = \frac{d\mathbf{p}}{dt}$)
   * The Second Law of Thermodynamics ($\Delta S_{universe} \ge 0$)
   * Quantum and continuum governing equations (Schrodinger, Navier-Stokes, Maxwell, Fourier, Arrhenius kinetics)
3. **High-Throughput In Silico Testing (10,000+ Runs):** Rather than building a physical prototype that takes weeks and costs capital, the virtual model is stressed across 10,000+ variations in composition, geometry, boundary loads, and ambient temperatures.
4. **Falsification Velocity:** 99.9 percent of candidates will fail or exhibit unphysical numerical artifacts. The engine identifies and discards non-viable variants automatically in seconds.
5. **Physical / Real-World Transfer:** Only candidates that achieve verified theoretical stability, superior performance metrics over current state of the art, and realistic synthesis or fabrication viability graduate to physical production.

## 2. Hypothesis Formulation Standard

Every proposed invention must be formalized using the template in [experiment-template.md](file:///Users/arunkumar/Downloads/inf-research/frameworks/experiment-template.md) before executing virtual sweeps.

A valid hypothesis must define:
* **Mechanism:** What specific physical, chemical, or informational principle produces the effect?
* **Governing Model:** What mathematical or computational equations describe the system?
* **Falsification Threshold:** What quantified metric determines that the candidate is ineffective or non-viable?
* **State of the Art Baseline:** What is the gold-standard legacy benchmark, and what is its quantified performance?

## 3. Benchmarking Against the State of the Art

Never evaluate an invention in isolation. Every measurement must compare directly against existing solutions:
* **Materials and Chemistry:** Yield strength, thermal stability, ionic conductivity, catalytic turnover frequency, and synthesis complexity compared to commercial benchmarks.
* **Energy Systems:** Specific energy (Wh/kg), power density (W/kg), and thermodynamic round-trip efficiency ($\eta$) compared to current lithium-ion, combustion, or fuel-cell technology.
* **Mechanical Systems:** Force density, power-to-weight ratio, wear lifecycle, and friction coefficient compared to brushless electric motors and hydraulic actuators.
* **Computing and Information:** Operations per joule (energy efficiency), latency, silicon area, or material footprint compared to CMOS silicon baselines.

## 4. Integrity and Scientific Rigor

* Negative results are documented with the exact same rigor as successful outcomes.
* If a virtual simulation displays anomalous performance (e.g. apparent over-unity energy, infinite conductivity, or frictionless motion), the primary assumption must always be numerical divergence, mesh instability, or boundary leakage until independently proven otherwise.
