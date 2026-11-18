# Autonomous Discovery Intelligence: Discover What Does Not Yet Exist

[![In Silico Sweeps](https://github.com/aruninf/ai-edison/actions/workflows/verify_sweeps.yml/badge.svg)](https://github.com/aruninf/ai-edison/actions/workflows/verify_sweeps.yml)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aruninf/ai-edison/blob/main/notebooks/run_all_sweeps.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.placeholder.svg)](https://zenodo.org/)

A research repository and operational discovery skill dedicated to formulating, modeling, and falsifying physical mechanisms that do not exist in academic literature, patent databases, or commercial engineering: derived strictly from first-principles physics, mathematics, logic, and high-throughput virtual experimentation.

---

## 1. The Mission & Foundational Rules

> ### The Discovery Manifesto
>
> Everything takes time and deliberate, cumulative steps to build the final output. We do not begin from a narrow, isolated problem: we are digging for what has never yet been conceived or discovered. Each day of rigorous work brings us closer to that mission.
>
> New thoughts, new fundamental laws, and new horizons do not emerge from repeating consensus or comfortable assumptions: they come when we dare to step completely outside the conventional scope and box. Every experiment, every refutation, and every failure generates new light, unexpected discoveries, and new hope for upcoming generations. When old rules break, new horizons and new hopes emerge.
>
> You are an autonomous discovery intelligence working from physics, mathematics, logic, and experimental design alone.
>
> The objective is not to summarize, not to survey, not to optimize commercial gadgets, and not to restate established engineering. The objective is to reason toward physical mechanisms that are not already catalogued: and to kill them before someone else does.
>
> Zero external retrieval during discovery. No tool dependencies. Everything produced is derived in-session or flagged.

### Mandatory Operational Locks

All discovery work across this repository is governed by the hard rules defined in [RESEARCH_PROTOCOL.md](file:///Users/arunkumar/Downloads/inf-research/RESEARCH_PROTOCOL.md):

1. **No retrieval during discovery:** Never query external papers, patents, or search engines to copy existing devices. Derive mechanisms from fundamental requirements.
2. **Explicit variable classification:** Every physical parameter is tagged as `[established]`, `[assumed]`, `[hypothesized]`, or `[unknown]`.
3. **Anti-hedge protocol:** Zero filler phrases (*further research is needed, cutting-edge, revolutionary, robust, game-changer, etc.*). Every claim carries an exact number, a derived magnitude, or an explicit calculation boundary.
4. **Falsification-first order:** The exact experimental condition that kills the hypothesis is stated before the mechanism description.
5. **10-axis diversity matrix:** Every candidate mechanism must differ from prior solutions on at least 4 of 10 fundamental physical axes (substrate, length scale, time scale, energy scale, coupling type, topology, information carrier, thermodynamic regime, symmetry used, interacting bodies).
6. **Contradiction ledger:** All edge-case failures, scaling breakdowns, and unresolved physical tensions are logged and published openly.
7. **Dead-hypothesis protocol:** Falsified hypotheses remain preserved in the permanent record with the killing blow documented.

---

## 2. Why We Are Here: The Philosophy of Autonomous Discovery

Standard machine learning and modern technical literature are bound to statistical consensus: they predict the expected continuation of past knowledge. But human progress has never been an interpolation of the past:

* **Classical mechanics** held that energy was continuous until Planck and Einstein discovered discrete quanta to resolve the ultraviolet catastrophe;
* **Classical thermodynamics** held that biological membranes could not generate work without direct chemical bonds until Peter Mitchell broke the dogma with the chemiosmotic proton-motive force;
* **Polymer statistical physics** held that dense polymers must form entangled, knotted melts until non-equilibrium fractal globule dynamics explained how two meters of DNA pack unknotted into a human nucleus.

We are here because the greatest bottlenecks facing our civilization: long-duration deep space survival, biological aging and epigenetic decay, ambient clean water harvesting, passive carbon mineralization, and reactionless kinetic protection: cannot be solved by incremental optimizations of 20th-century components. 

They require stepping outside the box of inherited assumptions. They require deriving uncatalogued physical symmetries, non-equilibrium topological phases, and strong light-matter quantum couplings that circumvent textbook limitations while strictly obeying fundamental conservation laws.

---

## 3. How to Use This Repository as a Discovery Skill

This repository is engineered as an operational **Discovery Skill** (`SKILL.md`) that can be loaded directly by autonomous AI agents (Antigravity, Claude Code, Cursor, Copilot) as well as human research teams.

### Operational Skill Files

* Master Skill Definition: [SKILL.md](file:///Users/arunkumar/Downloads/inf-research/SKILL.md)
* Installation & Setup Guide: [INSTALLATION.md](file:///Users/arunkumar/Downloads/inf-research/docs/INSTALLATION.md)
* Antigravity / Agent Skill: [.agents/skills/first-principles-discovery/SKILL.md](file:///Users/arunkumar/Downloads/inf-research/.agents/skills/first-principles-discovery/SKILL.md)
* Hardened Discovery Protocol: [RESEARCH_PROTOCOL.md](file:///Users/arunkumar/Downloads/inf-research/RESEARCH_PROTOCOL.md)
* Scientific & Computational Methodology: [METHODOLOGY.md](file:///Users/arunkumar/Downloads/inf-research/METHODOLOGY.md)
* Evaluation Rubric: [first-principles-evaluation.md](file:///Users/arunkumar/Downloads/inf-research/frameworks/first-principles-evaluation.md)

### Quick Install (One-Liner)

Install globally for Google Antigravity / Gemini CLI (`agy`):

```bash
mkdir -p ~/.gemini/skills/first-principles-discovery
curl -sSL https://raw.githubusercontent.com/aruninf/ai-edison/main/SKILL.md -o ~/.gemini/skills/first-principles-discovery/SKILL.md
```

For Claude Code, Cursor, Windsurf, or VS Code setups, read the step-by-step [Installation Guide](file:///Users/arunkumar/Downloads/inf-research/docs/INSTALLATION.md).

### Step-by-Step Discovery Workflow

1. **Define the Bare Requirement:** Strip away all decorative and commercial assumptions. State the core physical requirement (e.g., "inactivating cosmic-ray cytotoxicity in living cells without mass shielding").
2. **Execute Phase 2 Divergence:** Formulate candidate mechanisms across the 10-axis physical diversity matrix.
3. **Derive the Mathematical Model:** Build governing differential equations, check dimensional consistency across every term, and test limiting cases.
4. **Run the Adversarial Pass:** Attack the candidate against conservation laws, the Second Law of Thermodynamics ($dS/dt \ge 0$), and experimental bounds.
5. **Run Multi-Physics Simulation Sweeps:** Execute local Monte Carlo parameter sweeps using the pure Python standard library:
   ```bash
   python3 hypotheses/simulations/exp003_mechanical_diode_sweep.py 10000
   ```
6. **Publish the Canonical 16-Point Dossier:** Emit the complete dossier with zero banned phrases and strict numerical magnitudes.

---

## 4. Master Discovery Matrix & Research Dossiers

The repository contains 49 fully formulated physical discovery dossiers deconstructed from first principles.

### A. Deep-Space Living, Astrobiology & Cellular Longevity
* **[Vector 49: Sub-Femtosecond Cavity-Polariton Radiolytic Cleavage Suppressor](file:///Users/arunkumar/Downloads/inf-research/directions/49-sub-femtosecond-radiolytic-cleavage-suppressor.md)**: Open-access infrared polaritonic cavity modes strongly coupled to water librations (18 to 22 THz, $\hbar \Omega_R \approx 140\text{ meV}$) that accelerate geminate electron-hole recombination to $\le 22\text{ fs}$, quenching toxic hydroxyl radical ($\cdot OH$) creation from 1 GeV/nucleon cosmic rays by > 85% at the quantum source without lead shielding.
* **[Vector 48: Topological Chromatin Unknotting Resonator](file:///Users/arunkumar/Downloads/inf-research/directions/48-topological-chromatin-unknotting-resonator.md)**: Phased 1.62 GHz magneto-acoustic shear waves coupled to the lamin-A/C nucleoskeleton inducing an Aharonov-Casher topological phase gradient across DNA Manning counterion clouds, exerting autonomous torque ($\tau_{topo} \approx 2.4 \times 10^{-20}\text{ N}\cdot\text{m}$) that expels topological knots and restores youthful fractal globule architecture ($\gamma \le -1.03$) without topoisomerase enzymes.
* **[Vector 45: Cosmic-Ray Delta-Electron Electrostatic Cascade Trap](file:///Users/arunkumar/Downloads/inf-research/directions/45-cosmic-ray-delta-electron-trap.md)**: Sub-micron periodic electrostatic cascade lattices trapping secondary relativistic delta-electrons ($1\text{ to }100\text{ keV}$) emitted along heavy-ion Bragg ionization tracks, preventing intracellular DNA double-strand breaks.
* **[Vector 44: Sub-THz Mitochondrial Resonant Synchronizer](file:///Users/arunkumar/Downloads/inf-research/directions/44-mitochondrial-sub-thz-synchronizer.md)**: Coherent 0.18 to 0.24 THz electrodynamic phase-locking of mitochondrial inner membrane cardiolipin water-wire dipoles, suppressing electron leak at Complex I and stopping metabolic superoxide cascades.
* **[Vector 47: Sub-Debye Topological Electrostatic Conduit](file:///Users/arunkumar/Downloads/inf-research/directions/47-sub-debye-electrostatic-conduit.md)**: 1D chiral ferroelectric domain-wall solitons projecting intense electrostatic fields ($E \ge 2.5 \times 10^7\text{ V/m}$) through conductive electrolytes (blood, seawater) at distances > 6 times the classical Debye screening length without Faradaic leakage.

### B. Fundamental Quantum Limits & Electrodynamics
* **[Vector 46: Non-Hermitian Chiral Zero-Noise Resistor](file:///Users/arunkumar/Downloads/inf-research/directions/46-non-hermitian-zero-noise-resistor.md)**: 1D topological Edge-state conductor with non-Hermitian parity-time ($\mathcal{PT}$) symmetry breaking that routes Johnson-Nyquist thermal fluctuations into an isolated dissipative reservoir, delivering macroscopic electrical resistance with zero forward thermal voltage noise.
* **[Vector 43: Magnetostatic Topological Anapole](file:///Users/arunkumar/Downloads/inf-research/directions/43-magnetostatic-topological-anapole.md)**: Non-radiating toroidal current distributions canceling external multipole fields while sustaining giant localized internal magnetic energy densities.
* **[Vector 42: Gravitational Quadrupole Harvester](file:///Users/arunkumar/Downloads/inf-research/directions/42-gravitational-quadrupole-harvester.md)**: High-density coherent phonon resonators coupling to dynamic tidal gravitational field gradients for direct mechanical energy harvesting.

### C. Non-Reciprocal & Anti-Fatigue Structural Mechanics
* **[Vector 12: Static Mechanical Diodes](file:///Users/arunkumar/Downloads/inf-research/directions/12-static-mechanical-diode.md)**: Monolithic chiral Cosserat metamaterials breaking the 150-year-old Maxwell-Betti reciprocity theorem in static mechanics, enabling unidirectional rigid force transfer ($T_{fwd} = 99.6\%$) while diverting backward shock into internal toroidal hoop tension ($T_{bwd} = 0.00\%$, $\mathcal{R} > 20,000 : 1$).
  * Experiment Specification: [EXP-003-static-mechanical-diode.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-003-static-mechanical-diode.md)
  * Simulation Solver: [exp003_mechanical_diode_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp003_mechanical_diode_sweep.py)
* **[Vector 08: Abiotic Mass Migration Lattices](file:///Users/arunkumar/Downloads/inf-research/directions/08-abiotic-mass-migration-lattices.md)**: Structural alloys where deviatoric shear stress gradients drive solid-state interstitial atomic diffusion to spontaneously thicken and reinforce load-bearing paths (abiotic Wolff law) with infinite fatigue life.
* **[Vector 09: Momentum-to-Vorticity Metamaterials](file:///Users/arunkumar/Downloads/inf-research/directions/09-momentum-to-vorticity-metamaterials.md)**: Chiral phononic lattices with broken spatial-inversion symmetry that geometrically refract linear translational impact momentum into trapped internal acoustic vortex loops without sacrificial plastic damage.
* **[Vector 18: Topological Acoustic Soliton Flywheels](file:///Users/arunkumar/Downloads/inf-research/directions/18-topological-acoustic-soliton-flywheels.md)**: Bearingless stationary kinetic storage ($1.55\text{ kJ/kg}$) via supersonic non-linear torsional kink solitons ($v \approx 4,820\text{ m/s}$) circulating inside non-rotating silicon crystals.
* **[Vector 30: Quasicrystalline Superlubricity Interface](file:///Users/arunkumar/Downloads/inf-research/directions/30-quasicrystalline-superlubricity-interface.md)**: Incommensurate aperiodic 2D quasicrystalline interfaces eliminating stick-slip friction ($C_f < 10^{-5}$) across macroscopic contact areas.

### D. Planetary & Environmental Chemical-Potential Engines
* **[Vector 07: Transpiration & Cavitation Metamaterials](file:///Users/arunkumar/Downloads/inf-research/directions/07-transpiration-cavitation-metamaterials.md)**: Monolithic structures tapping the $-100\text{ MPa}$ chemical potential gradient between terrestrial moisture and dry air via cyclic metastable liquid cavitation, generating autonomous mechanical power ($> 300\text{ W}$ peak) and wireless RF pulses.
  * Experiment Specification: [EXP-002-evaporative-cavitation-oscillator.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-002-evaporative-cavitation-oscillator.md)
  * Simulation Solver: [exp002_cavitation_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp002_cavitation_sweep.py)
* **[Vector 13: Mechanochemical Vapor Engines](file:///Users/arunkumar/Downloads/inf-research/directions/13-mechanochemical-vapor-engines.md)**: Auxetic metamaterials extracting clean liquid water from dry air ($20 - 50\%\text{ RH}$) via swelling-induced mechanical snap-through and steric contact-angle inversion, expelling liquid water with zero photothermal heat and zero electricity.
  * Experiment Specification: [EXP-004-mechanochemical-water-generator.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-004-mechanochemical-water-generator.md)
  * Simulation Solver: [exp004_water_generator_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp004_water_generator_sweep.py)
* **[Vector 01: Environmental-Gradient Machines](file:///Users/arunkumar/Downloads/inf-research/directions/01-environmental-gradient-machines.md)**: Solid-state micro-thermal ($\nabla T \le 3\text{ K}$) and barometric harvesters operating indefinitely without batteries.
  * Experiment Specification: [EXP-001-thermomagnetic-oscillator.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-001-thermomagnetic-oscillator.md)
  * Simulation Solver: [exp001_thermomagnetic_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp001_thermomagnetic_sweep.py)
* **[Vector 17: Monolithic Flexogalvanic Redox Engines](file:///Users/arunkumar/Downloads/inf-research/directions/17-flexogalvanic-redox-engines.md)**: Mixed ionic-electronic ceramic nano-wedges where permanent elastic strain gradients ($\nabla \boldsymbol{\epsilon} \ge 10^5\text{ m}^{-1}$) drive directional oxygen vacancy drift to sustain steady-state electrochemical redox power in ambient air without electrolyte membranes or catalysts.
  * Experiment Specification: [EXP-006-flexogalvanic-redox-engine.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-006-flexogalvanic-redox-engine.md)
* **[Vector 10: Topological Entropic Refrigeration](file:///Users/arunkumar/Downloads/inf-research/directions/10-topological-entropic-refrigeration.md)**: Solid-state, fluid-free cooling powered by the giant configurational entropy shifts ($\Delta S_{topo}$) of reversible macromolecular knot uncoiling.

### E. Civil Infrastructure, Fluid Interfaces & Advanced Thermodynamics
* **[Vector 14: Mechanocatalytic Carbon Mineralization](file:///Users/arunkumar/Downloads/inf-research/directions/14-abiotic-mechanocatalytic-mineralization.md)**: Civil composites utilizing vehicle traffic vibrations to generate piezocatalytic surface potentials ($> 80\text{ V}$), driving spontaneous ambient $\text{CO}_2$ capture and in situ $\text{CaCO}_3$ crystal growth ($19.4\text{ tons CO}_2\text{/km/year}$).
  * Experiment Specification: [EXP-005-mechanocatalytic-carbon-mineralizer.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-005-mechanocatalytic-carbon-mineralizer.md)
  * Simulation Solver: [exp005_mineralization_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp005_mineralization_sweep.py)
* **[Vector 19: Smectic Hydrostatic Decouplers](file:///Users/arunkumar/Downloads/inf-research/directions/19-smectic-hydrostatic-decouplers.md)**: Chiral smectic-A boundary wall anchoring breaking Stevin law of hydrostatics, saturating bottom pressure at $\le 6\text{ kPa}$ in vertical columns over $100\text{ meters}$ deep (99.4% pressure reduction).
  * Experiment Specification: [EXP-008-smectic-hydrostatic-decoupler.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-008-smectic-hydrostatic-decoupler.md)
  * Simulation Solver: [exp008_hydrostatic_decoupler_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp008_hydrostatic_decoupler_sweep.py)
* **[Vector 20: Cooperative Spin-State Latent Heat Capacitors](file:///Users/arunkumar/Downloads/inf-research/directions/20-dislocation-latent-heat-capacitors.md)**: All-solid, dry coordination crystals storing giant latent heat ($351.6\text{ kJ/kg}$, matching water-ice) isothermally via electronic spin-crossover ($S=0 \leftrightarrow S=2$) with zero liquid phase, zero leaks, and sub-0.5 K hysteresis.
  * Experiment Specification: [EXP-009-dislocation-latent-heat-capacitor.md](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-009-dislocation-latent-heat-capacitor.md)
  * Simulation Solver: [exp009_dislocation_heat_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp009_dislocation_heat_sweep.py)
* **[Vector 15: Toroidal Liquid-Bearing Surfaces](file:///Users/arunkumar/Downloads/inf-research/directions/15-toroidal-liquid-bearing-surfaces.md)**: Trapping recirculating toroidal fluid vortices to eliminate the classical no-slip condition ($v_{wall} \approx v_\infty$), reducing skin-friction drag by up to 90%.
* **[Vector 16: Coherent Phonon-Inversion Foundations](file:///Users/arunkumar/Downloads/inf-research/directions/16-coherent-phonon-inversion-foundations.md)**: Sub-wavelength acoustic phase-inversion foundation metamaterials achieving zero-vibration isolation ($0.1\text{ to }200\text{ Hz}$) via $180^\circ$ destructive interference.

---

## 5. Active In Silico Experiment Registry

All virtual experimentation runs and falsification logs are documented under `hypotheses/`.

| Experiment ID | Title | Key Target | Reproduce Locally | Specification Dossier |
| :--- | :--- | :--- | :--- | :--- |
| **EXP-20261117-001** | Room-Temperature Solid-State Thermomagnetic Cantilever Oscillator | Harvest kinetic work from ambient drafts ($\Delta T \le 3\text{ K}$) using low-Curie Gadolinium/Heusler alloys | `python3 hypotheses/simulations/exp001_thermomagnetic_sweep.py 10000` | [EXP-001 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-001-thermomagnetic-oscillator.md) |
| **EXP-20261117-002** | Monolithic Nanoporous Evaporative Cavitation-Snap Oscillator (NECSO) | Autonomous kinetic power ($> 300\text{ W}$ peak) and RF chirps from ambient humidity ($\Delta \mu \approx -23\text{ MPa}$) | `python3 hypotheses/simulations/exp002_cavitation_sweep.py 10000` | [EXP-002 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-002-evaporative-cavitation-oscillator.md) |
| **EXP-20261117-003** | Monolithic Chiral-Cosserat Static Mechanical Diode | Breaking Maxwell-Betti reciprocity ($\mathcal{R} > 20,000 : 1$, $T_{fwd} = 99.6\%$, $T_{bwd} = 0.00\%$) | `python3 hypotheses/simulations/exp003_mechanical_diode_sweep.py 10000` | [EXP-003 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-003-static-mechanical-diode.md) |
| **EXP-20261117-004** | Monolithic Bistable Auxetic Water Generator (BAWG) | Isothermal water extraction from dry air ($> 3.0\,\text{L/m}^2/\text{day}$) without heat or electricity | `python3 hypotheses/simulations/exp004_water_generator_sweep.py 10000` | [EXP-004 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-004-mechanochemical-water-generator.md) |
| **EXP-20261117-005** | Piezocatalytic Self-Mineralizing Concrete Composite | Passive carbon capture ($19.4\text{ tons CO}_2\text{/km/year}$) and crack healing from traffic vibration | `python3 hypotheses/simulations/exp005_mineralization_sweep.py 10000` | [EXP-005 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-005-mechanocatalytic-carbon-mineralizer.md) |
| **EXP-20261117-006** | Monolithic Flexogalvanic Solid-State Redox Engine | Interfaceless electrochemical DC potential ($V_{oc} \approx 0.23\text{ V}$) via nanoscale strain gradients | Specification Protocol | [EXP-006 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-006-flexogalvanic-redox-engine.md) |
| **EXP-20261117-007** | Monolithic Topological Acoustic Soliton Flywheel | Bearingless stationary kinetic storage ($1.55\text{ kJ/kg}$) via supersonic torsional solitons ($v \approx 4,820\text{ m/s}$) | Specification Protocol | [EXP-007 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-007-topological-soliton-flywheel.md) |
| **EXP-20261117-008** | Smectic Topological Hydrostatic Pressure Decoupler | Saturate bottom pressure at $\le 6\text{ kPa}$ at $100\text{ m}$ depth (99.4% reduction) via helical anchoring | `python3 hypotheses/simulations/exp008_hydrostatic_decoupler_sweep.py 10000` | [EXP-008 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-008-smectic-hydrostatic-decoupler.md) |
| **EXP-20261117-009** | Cooperative Spin-State Solid-State Latent Heat Capacitor | Dry all-solid latent heat ($351.6\text{ kJ/kg}$) via cooperative spin-crossover with zero liquid phase | `python3 hypotheses/simulations/exp009_dislocation_heat_sweep.py 10000` | [EXP-009 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-009-dislocation-latent-heat-capacitor.md) |

---

## 6. Repository Architecture

```text
inf-research/
├── README.md                               (Master discovery map and navigation)
├── SKILL.md                                (Operational first-principles discovery skill)
├── .agents/skills/first-principles-discovery/
│   └── SKILL.md                            (Direct agent skill integration)
├── DISCOVERY_COMPENDIUM.md                 (Comprehensive 16-point review of mechanisms)
├── DISSEMINATION_KIT.md                    (Turnkey publication copy, Show HN, and LaTeX preprints)
├── CITATION.cff                            (Machine-readable academic citation metadata)
├── .zenodo.json                            (CERN Zenodo DOI minting configuration)
├── RESEARCH_PROTOCOL.md                    (Hardened uncensored discovery rules and locks)
├── METHODOLOGY.md                          (Scientific and computational protocols)
├── directions/                             (49 Core discovery domain dossiers)
│   ├── 01-environmental-gradient-machines.md through 20-dislocation-latent-heat-capacitors.md
│   ├── 21-phonon-poiseuille-thermal-conduits.md through 43-magnetostatic-topological-anapole.md
│   ├── 44-mitochondrial-sub-thz-synchronizer.md
│   ├── 45-cosmic-ray-delta-electron-trap.md
│   ├── 46-non-hermitian-zero-noise-resistor.md
│   ├── 47-sub-debye-electrostatic-conduit.md
│   ├── 48-topological-chromatin-unknotting-resonator.md
│   └── 49-sub-femtosecond-radiolytic-cleavage-suppressor.md
├── frameworks/                             (Evaluation rubrics and pipeline architecture)
│   ├── virtual-experimentation-pipeline.md
│   ├── first-principles-evaluation.md
│   └── experiment-template.md
├── notebooks/                              (Interactive zero-install browser runs)
│   └── run_all_sweeps.ipynb
└── hypotheses/                             (Virtual experiment runs and validation logs)
    ├── README.md                           (Active hypotheses registry)
    ├── EXP-001 through EXP-009 dossiers
    └── simulations/                        (Pure Python high-throughput multi-physics sweeps)
        ├── exp001_thermomagnetic_sweep.py
        ├── exp002_cavitation_sweep.py
        ├── exp003_mechanical_diode_sweep.py
        ├── exp004_water_generator_sweep.py
        ├── exp005_mineralization_sweep.py
        ├── exp008_hydrostatic_decoupler_sweep.py
        └── exp009_dislocation_heat_sweep.py
```

---

## 7. Interactive Browser Execution & Academic Citation

### Run in Google Colab (Zero Local Setup)
You can execute all 10,000-trial sweeps directly in your browser without local Python installation:
* [Launch Interactive Notebook](https://colab.research.google.com/github/aruninf/ai-edison/blob/main/notebooks/run_all_sweeps.ipynb)

### How to Cite
If you utilize these derivations, physical mechanisms, or simulation models in academic research or technical whitepapers, please cite using [CITATION.cff](file:///Users/arunkumar/Downloads/inf-research/CITATION.cff) or the format below:

```bibtex
@software{kumar2026discovery,
  author = {Kumar, Arun},
  title = {Autonomous Discovery Intelligence: Uncatalogued Physical Inventions and In Silico Multi-Physics Sweeps},
  url = {https://github.com/aruninf/ai-edison},
  year = {2026},
  publisher = {GitHub}
}
```
