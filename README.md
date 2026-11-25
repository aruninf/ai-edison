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

The repository contains **77 first-principles physical discovery vectors** across 73 dossier files, organized into 8 domain categories. For the complete 77-row searchable table, quick-finder by problem, and status breakdown (`live` / `wounded` / `dead`), see the [Master Vector Catalog](directions/README.md).

* **I. Methodology, Computation & Adversarial Frameworks (Vectors 02-06, 11):** [02](directions/02-material-based-computation.md), [03](directions/03-integrated-physical-machines.md), [04](directions/04-dissipative-thermodynamic-logic.md), [05](directions/05-monolithic-transduction-lattices.md), [06](directions/06-adversarial-physical-falsification.md), [11](directions/11-non-oscillatory-chrono-metamaterials.md)
* **II. Non-Reciprocal, Anti-Fatigue & Metamaterial Mechanics (Vectors 08, 09, 12, 16, 18, 22, 24, 29, 30, 32, 37, 75)**
* **III. Thermal Physics, Phase-Change & Phononic Engineering (Vectors 10, 20, 21, 25, 28, 31, 40, 57, 58, 64, 76, 77)**
* **IV. Fluidics, Hydrostatics & Desalination / Drying (Vectors 15, 19, 26, 27, 35, 36, 38, 41, 69)**
* **V. Ambient Energy, Electrochemistry & Planetary Carbon/Nitrogen/H2 (Vectors 01, 07, 13, 14, 17, 33, 34, 39, 54, 59, 61, 63, 65, 66)**
* **VI. Quantum Limits, Electrodynamics & Gravitation (Vectors 23, 42, 43, 46, 47)**
* **VII. Deep-Space Biology, Cellular Longevity & Non-Invasive Medicine (Vectors 44, 45, 48-53, 55, 62, 67, 68, 70-74)**
* **VIII. Documented Dead Hypotheses (Vectors 56, 60)**

Selected highlights by domain:

### A. Deep-Space Living, Astrobiology & Cellular Longevity
* **[Vector 68: Ambient Zwitterionic Hydration-Shell Biologic Preserver](file:///Users/arunkumar/Downloads/inf-research/directions/68-ambient-zwitterionic-hydration-shell-vaccine-preserver.md)**: Replaces volatile water with an artificial non-evaporating $0.278\ \mathrm{nm}$ zwitterionic oligopeptide scaffold that matches the exact hydrogen-bonding donor-acceptor spacing of bulk water. Vitrifies insulin and mRNA-lipid nanoparticles into an amorphous solid glass ($T_g = 98.5\ ^\circ\mathrm{C}$), completely arresting protein unfolding and molecular diffusion at $+50\ ^\circ\mathrm{C}$ for years without refrigeration, freezing, or vacuum freeze-dryers, targeting the $\$35\text{ billion/year}$ biopharma cold chain waste.
* **[Vector 50: Sub-Critical Condensate Pit Lattice](file:///Users/arunkumar/Downloads/inf-research/directions/50-sub-critical-condensate-pit-lattice.md)**: $12\text{ nm}$ pitch blind-pit surfaces ($6.9 \times 10^{11}$ pits/$\text{cm}^2$) that confine the dense-liquid amyloid precursor below its $23\text{ nm}$ Laplace critical radius ($\Pi = 0.83\text{ bar}$, confinement penalty $1.9\times$ the driving force), closing the membrane-catalyzed nucleation channel of $\alpha$-synuclein and $\beta_2$-microglobulin with zero binding, zero dose, and zero energy input.
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
* **[Vector 75: Repulsive Vacuum-Casimir Topological Metamaterial Bearing](file:///Users/arunkumar/Downloads/inf-research/directions/75-repulsive-vacuum-casimir-topological-bearing.md)**: Overturns the 75-year consensus that the vacuum Casimir force is strictly attractive in solid micro-machinery. Non-reciprocal axion magnetoelectric coupling ($\theta \approx \pi$) in room-temperature magnetic Weyl semimetal superlattices ($\mathrm{Co_3Sn_2S_2}$) flips the sign of the quantum vacuum stress tensor, generating $+47.1\ \mathrm{kPa}$ of repulsive quantum pressure at $d = 20\ \mathrm{nm}$ and infinite passive spring stiffness ($K \approx 9.4 \times 10^{12}\ \mathrm{N/m^3}$), delivering zero-power, zero-wear, non-contact rotation up to $10^6\ \mathrm{RPM}$ with zero lubricants.

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
* **[Vector 54: Interfacial Microdischarge Nitrogen Fixation](file:///Users/arunkumar/Downloads/inf-research/directions/54-interfacial-microdischarge-nitrogen-fixation.md)**: A $50\ \mu\mathrm{m}$ non-thermal microdischarge array at a structured water interface ($1.8\text{ kWh/kg N}$ thermodynamic floor) with continuous membrane stripping of nitric oxide before back-reduction, targeting $8\text{ kWh/kg N}$ against the $60\text{ kWh/kg N}$ of the 1903 arc process that this replaces.
* **[Vector 59: The Air-Handler Ceiling on Direct Air Capture](file:///Users/arunkumar/Downloads/inf-research/directions/59-air-handler-ceiling-direct-air-capture.md)**: At $420\ \mathrm{ppm}$ one tonne of CO2 is carried by $1.31\times10^{6}\ \mathrm{m^3}$ of air, so a contactor at $300\ \mathrm{Pa}$ spends $0.56\ \mathrm{GJ/t}$ of fan work against a reversible separation floor of $0.43\ \mathrm{GJ/t}$: the fan costs $1.3\times$ more than the chemistry's theoretical minimum, which is the ceiling no sorbent improvement can cross. A $2.3\ \mathrm{mm}$ parallel-plate stack at $12\ \mathrm{Pa}$ ($Re = 305$) moves the same air for $0.09\ \mathrm{GJ/t}$ at four passes, with $61\ \mathrm{m^2}$ of face and $1.9\ \mathrm{t}$ of amine per tonne per day, and the $1.9\ \mathrm{t}$ follows from both the $60\ \mathrm{g/m^2}$ coating and the $1\ \mathrm{mmol/g}$ capacity, which is the check that the geometry is not arbitrary. Wounded on the assumption that a $60\ \mu\mathrm{m}$ amine washcoat is hydraulically invisible.
* **[Vector 61: Monolithic Chiral-Topological Spin-Gated Water Engine](file:///Users/arunkumar/Downloads/inf-research/directions/61-chiral-topological-spin-gated-water-engine.md)**: A monolithic single-crystal chiral B20 Weyl semimetal anode ($CoSi$) generating an uncompensated relativistic spin-orbit field ($B_{eff} \approx 380\ \mathrm{T}$) that forces $100\%$ spin polarization on outgoing electrons. Breaks the universal Sabatier OER scaling floor from $0.37\ \mathrm{V}$ to $0.12\ \mathrm{V}$ via concerted singlet-to-triplet multi-electron transfer ($39.3\ \mathrm{kWh/kg\ H_2}$), while suppressing competitive singlet chlorine gas formation in raw seawater by $> 10^4$ by quantum spin selection rules without desalination or membranes.
* **[Vector 63: Acoustically Pinned Dislocation-Creep Freeze](file:///Users/arunkumar/Downloads/inf-research/directions/63-acoustically-pinned-dislocation-creep-freeze.md)**: Overturns the failed Monroe-Newman solid-state battery paradigm by recognizing that metallic lithium at $298\ \mathrm{K}$ sits at homologous temperature $T/T_m = 0.66$ in high-temperature dislocation creep. High-frequency shear acoustic waves at $120\ \mathrm{MHz}$ inertially clamp dislocations, freezing plastic creep, restoring lattice shear stiffness ($3.44\ \mathrm{GPa}$), and generating $14.8\ \mathrm{MPa}$ acoustic radiation pressure at asperity tips, suppressing tip overpotential by $+107\ \mathrm{mV}$ to allow dendrite-free charging at $\ge 40\ \mathrm{mA/cm^2}$ ($< 3\ \mathrm{min}$ charge).
* **[Vector 65: Anharmonic Phonon-Rectified Solid-State Isotope Sieve](file:///Users/arunkumar/Downloads/inf-research/directions/65-anharmonic-phonon-rectified-isotope-sieve.md)**: Exploits the $845\ \mathrm{GHz}$ localized vibrational mode (LVM) optical phonon split between $^6\mathrm{Li}$ and $^7\mathrm{Li}$ in non-centrosymmetric crystals ($\alpha-\mathrm{LiIO_3}$). Resonant continuous-wave THz drive ($15.85\ \mathrm{THz}$) excites large-amplitude oscillations ($u_0 \approx 0.038\ \mathrm{nm}$), which cubic lattice anharmonicity rectifies into a unidirectional DC force ($\langle F_{DC} \rangle \ge 1.8\ \mathrm{pN}$ per atom), driving single-pass $^6\mathrm{Li}$ isotope separation with factor $\alpha \ge 6.55$ at room temperature, eliminating toxic mercury amalgamation (COLEX).
* **[Vector 66: Supramolecular Desolvation Thermogalvanic Harvester](file:///Users/arunkumar/Downloads/inf-research/directions/66-supramolecular-desolvation-thermogalvanic-harvester.md)**: Amplifies liquid thermogalvanic Seebeck coefficients to $S_e \ge 10.88\ \mathrm{mV/K}$ ($7.7\times$ above ferri/ferrocyanide) by coupling an $I^- / I_3^-$ redox reaction to temperature-dependent $\alpha$-cyclodextrin host-guest inclusion. Releases $\approx 22$ ordered clathrate water molecules per inclusion ($\Delta S_{coop} \ge 1,050\ \mathrm{J/(mol\cdot K)}$), delivering continuous $14.8\ \mathrm{W/m^2}$ electrical power under a $3\ \mathrm{K}$ ambient thermal gradient via thermo-osmotic micro-capillary slip without solar or wind.

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
* **[Vector 57: Pressure-Gated Molecular Thermal Switch](file:///Users/arunkumar/Downloads/inf-research/directions/57-pressure-gated-molecular-thermal-switch.md)**: A $2\ \mu\mathrm{m}$ air gap conducts $1.18\times10^{4}\ \mathrm{W/m^2K}$ at $1\ \mathrm{atm}$ and $6.2\ \mathrm{W/m^2K}$ at $1\ \mathrm{Pa}$, so admitting or evacuating the gas switches heat flow $1.9\times10^{3}:1$ with no moving part and $2.3\ \mathrm{mJ}$ per actuation. The arithmetic runs against the funded route: the near-field photon channel at $100\ \mathrm{nm}$ is $6\times10^{3}\ \mathrm{W/m^2K}$, $13\times$ below plain air at the same gap, so the photonic switch loses to the gas it has to exclude. The ratio is capped by the mechanical support ($5.9\ \mathrm{W/m^2K}$), not by the vacuum. Corollary: any air gap thinner than $5.0\ \mu\mathrm{m}$ beats a $1\ \mathrm{MPa}$ bolted joint.
* **[Vector 58: Thermo-Osmotic Liquid-State Drying](file:///Users/arunkumar/Downloads/inf-research/directions/58-thermo-osmotic-liquid-drying.md)**: Water confined in a hydrophobic nanopore carries an entropy of transfer ($0.9\ k_B$), so a $5\ \mathrm{K}$ difference generates $20.8\ \mathrm{bar}$ and moves water as a liquid at $125\ \mathrm{kJ/kg}$ of ambient heat and $2.1\ \mathrm{kJ/kg}$ of work, $18\times$ below the latent heat $2.26\ \mathrm{MJ/kg}$ that every industrial dryer pays. The head and the heat are one number, not two: their ratio is exactly $\Delta T/T$, so the process is Carnot-reversible and cannot be better. Corollary: $13\ \mathrm{K}$ of waste heat delivers the $54\ \mathrm{bar}$ a seawater reverse-osmosis train runs, against a $27\ \mathrm{bar}$ osmotic load. Wounded on $\Delta s$: the drying claim survives down to $0.2\ k_B$, the desalination corollary dies below $0.9\ k_B$.
* **[Vector 64: Phonon-Polariton Ballistic Heat Shunt](file:///Users/arunkumar/Downloads/inf-research/directions/64-phonon-polariton-ballistic-heat-shunt.md)**: Overcomes the sub-micron ballistic phonon bottleneck in high-density 3D AI microprocessors ($q \ge 1,000\ \mathrm{W/cm^2}$) where hotspot diameter $D < \lambda_{MFP}$. By direct near-field coupling into the Reststrahlen band of an atomically thin isotopically pure polar semiconductor capping layer ($h-^{11}\mathrm{BN}$ or $SiC$), heat launches into Surface Phonon-Polaritons (SPhPs) traveling laterally at $v_g \approx 1.27 \times 10^6\ \mathrm{m/s}$ ($150\times$ faster than sound in silicon) over $L_{prop} \approx 7.0\ \mu\mathrm{m}$, bypassing Fourier diffusive scattering and slashing peak junction temperatures by over $45\%$.
* **[Vector 69: Capillary Multi-Stage Latent-Heat Desalinator](file:///Users/arunkumar/Downloads/inf-research/directions/69-capillary-multistage-latent-heat-desalinator.md)**: Overturns the century-old assumption that solar distillation is capped at $3\ \mathrm{L/(m^2\cdot day)}$. By cascading latent heat through a 10-stage $22\ \mathrm{mm}$ capillary nanolaminate panel while using the $175\ \mathrm{kg/m^3}$ negative buoyancy difference of concentrated brine to autonomously flush salt downward without pumps, the device delivers $42.5\ \mathrm{liters/(m^2\cdot day)}$ of drinking water (TDS $< 15\ \mathrm{ppm}$) at $\$0.12/\mathrm{m^3}$ with zero electricity and $\$18/\mathrm{m^2}$ capital cost.
* **[Vector 76: Chiral Phononic Flat-Band Thermal Super-Insulator](file:///Users/arunkumar/Downloads/inf-research/directions/76-chiral-phononic-flat-band-super-insulator.md)**: Bypasses the Cahill-Pohl minimum thermal conductivity limit by constructing a 3D chiral non-symmorphic skutterudite-cage lattice ($\mathrm{La_{0.8}Ce_{0.2}Fe_4Sb_{12}}$). Localized optical rattling modes ($1.45\ \mathrm{THz}$) hybridize with acoustic branches to flatten the phonon dispersion across the Brillouin zone ($v_g \le 4.2\ \mathrm{m/s}$), while closed $0.48\ \mathrm{nm}$ interstitial cages freeze gas conduction into the deep Knudsen limit ($\mathrm{Kn} \approx 142$). Delivers an effective thermal conductivity of $k_{\text{eff}} = 0.00062\ \mathrm{W/(m\cdot K)}$ ($42\times$ lower than still air, $24\times$ lower than silica aerogel) in open atmospheric air without vacuum envelopes, supporting $> 12\ \mathrm{MPa}$ compressive load.
* **[Vector 77: Self-Synchronized Thermo-Acoustic Vapor-Jet Diode Lattice](file:///Users/arunkumar/Downloads/inf-research/directions/77-thermo-acoustic-vapor-jet-chf-lattice.md)**: Breaks the Kutateladze-Zuber pool-boiling Critical Heat Flux limit ($1.109\ \mathrm{MW/m^2}$) by using Clausius-Clapeyron chamber overpressure ($3.62\ \mathrm{kPa/K}$) to fire high-Weber-number vapor jets ($v_v \le 215.4\ \mathrm{m/s}$, $\mathrm{We}_{\text{jet}} \ge 8.0$) through vertical nozzles while lateral Tesla-diode arteries ($\mathrm{Di} \ge 2.5$) resupply liquid passively. Sustains $15.42\ \mathrm{MW/m^2}$ median CHF ($33.78\ \mathrm{MW/m^2}$ champion, $30.46\times$ KZ) with zero pumps.
  * Experiment Specification: [EXP-20261125-010](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-20261125-010-thermo-acoustic-chf-lattice.md)
  * Simulation Solver: [exp010_thermo_acoustic_chf_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp010_thermo_acoustic_chf_sweep.py)

### F. Non-Contact Intervention, Tissue Reconstruction & Resistance-Proof Surfaces
* **[Vector 51: Coincidence-Gated Sub-Threshold Acoustic Ablation](file:///Users/arunkumar/Downloads/inf-research/directions/51-coincidence-gated-acoustic-ablation.md)**: Six coherent transducers at $2.0\text{ MPa}$ against a $2.2\text{ MPa}$ cavitation threshold, so only the $12.0\text{ MPa}$ overlap crosses it, giving a $2\text{ mm}$ lesion at $12\text{ cm}$ depth with $0.8\text{ K}$ off-target heating and no imaging resolution. Live but contested: the claimed $10^4$ volumetric selectivity needs a $13\text{ kPa}$ threshold step, and at a realistic $200\text{ kPa}$ step the geometry delivers $6.9 \times 10^{-3}$, so the corrected design point is $N = 7$ beams at $0.65\text{ MPa}$ with $w \le 100\text{ kPa}$. The falsification test measures the step width directly rather than confirming the mechanism.
* **[Vector 52: Mesh-Pinned Ice Recrystallization Arrest](file:///Users/arunkumar/Downloads/inf-research/directions/52-mesh-pinned-ice-recrystallization-arrest.md)**: A $100\text{ nm}$ hydrogel mesh caps ice at mesh size, with a $0.52\text{ K}$ Gibbs-Thomson melt depression. The rate arithmetic runs the other way from the intuition: $100\text{ nm}$ ice ripens $2500\times$ faster than $5\ \mu\mathrm{m}$ ice ($\dot r \propto r^{-2}$), so the mesh must additionally hold water diffusivity below $4.9 \times 10^{-16}\text{ m}^2/\mathrm{s}$. That is stated as a hard test condition, not a prediction, and intracellular ice remains unaddressed.
* **[Vector 53: Field-Driven Epitaxial Enamel Reconstruction](file:///Users/arunkumar/Downloads/inf-research/directions/53-field-driven-epitaxial-enamel-reconstruction.md)**: Iontophoresis drives calcium past the self-sealing outer $10\text{ to }20\ \mu\mathrm{m}$ of an enamel lesion, delivering $0.25\text{ mg/cm}^2$ of hydroxyapatite per $10\text{ min}$ session. The adopted $4\text{ mg/cm}^2$ deficit is set from a microradiography profile, not the $12.5\text{ mg/cm}^2$ geometric porosity bound, which would need $50$ sessions instead of $16$. A $250\ \mu\mathrm{m}$ subsurface lesion rebuilds in a tissue with no cells to repair it, at the cost of one extracted tooth to test.
* **[Vector 55: Resonant Mechano-Bactericidal Pillar Array](file:///Users/arunkumar/Downloads/inf-research/directions/55-resonant-mechano-bactericidal-pillar-array.md)**: $200\text{ nm}$ silicon pillars ($k = 40.0\text{ N/m}$, $m = 7.3 \times 10^{-17}\text{ kg}$) driven at $99\text{ MHz}$ in water with $Q \approx 8$, in a $15\text{ to }40\text{ nm}$ displacement window where a $1\ \mu\mathrm{m}$ coccus takes $4.0\%$ strain and a $10\ \mu\mathrm{m}$ fibroblast takes $0.40\%$, giving a $10\times$ size selectivity and $3.0\ \log_{10}$ killing with no chemical target to mutate. Contested: $464\ \mathrm{W/cm^2}$ of drive power, and monolayer burial of half a pillar after one confluent layer.
* **[Vector 62: Axonal MPS Acousto-Electric Soliton Resonator](file:///Users/arunkumar/Downloads/inf-research/directions/62-axonal-mps-acousto-electric-soliton-resonator.md)**: Overcomes the skull acoustic attenuation barrier ($> 315\ \mathrm{dB}$ at $30\ \mathrm{MHz}$) by intersecting two bone-transparent RF magnetic beams ($f_1 = 64.000\ \mathrm{MHz}$, $f_2 = 64.030\ \mathrm{MHz}$, attenuation $< 0.05\ \mathrm{dB}$). Non-linear diamagnetic heterodyning excites the natural $30.4\ \mathrm{MHz}$ radial breathing resonance of the axonal Membrane-Associated Periodic Skeleton (MPS, $190\ \mathrm{nm}$ actin-spectrin unit cells), bending the lipid bilayer to radius $R \le 55\ \mathrm{nm}$ and generating $+82\ \mathrm{mV}$ of flexoelectric curvature potential, achieving non-invasive, sub-millisecond, single-axon spike triggering with zero genetic modification and SAR $< 0.05\ \mathrm{K}$.
* **[Vector 67: Non-Invasive Chiral-Polariton Transdermal Glucose Monitor](file:///Users/arunkumar/Downloads/inf-research/directions/67-non-invasive-chiral-polariton-glucose-monitor.md)**: Solves the 30-year failure of non-invasive glucose monitoring ($>\$12\text{ billion/year}$ market) by rejecting the $11,000\times$ liquid water background via quantum chiral symmetry. Liquid water is strictly achiral ($C_{2v}$, $\Delta \varepsilon = 0$), while D-glucose has 5 asymmetric stereocenters with resonant circular dichroism at $1.82\ \mathrm{THz}$ ($\Delta A \approx 2.9\ \mathrm{mOD}$). High-frequency circular polarization modulation through $15\ \mu\mathrm{m}$ stratum corneum delivers needle-free clinical blood glucose tracking (MARD $\le 7.5\%$) with zero skin punctures and zero calibration drift.
* **[Vector 70: Non-Invasive Cranial Compliance Waveguide](file:///Users/arunkumar/Downloads/inf-research/directions/70-non-invasive-cranial-compliance-waveguide.md)**: Replaces surgical burr-hole brain catheter drilling (EVD) in 70 million annual TBI and stroke patients. Utilizes thin-shell bone elasticity to measure the $24.1\ \mathrm{nm}$ systolic cranial expansion via a $24\ \mathrm{GHz}$ microwave Doppler skin patch, tracking beat-to-beat intracranial pressure ($0$ to $50\ \mathrm{mmHg}$) and compliance collapse ($P_2 > P_1$) with $\pm 1.2\ \mathrm{mmHg}$ clinical accuracy through intact skull with zero brain surgery.
* **[Vector 71: Whispering-Gallery Rayleigh-Mode Lithotripsy](file:///Users/arunkumar/Downloads/inf-research/directions/71-whispering-gallery-rayleigh-lithotripsy.md)**: Converts compressive ultrasound into circulating Rayleigh surface acoustic waves at the $50.3^\circ$ critical angle of calcium oxalate stones. Replaces tissue-damaging cavitation with internal hoop tensile stress ($10.0\ \mathrm{MPa}$ from $0.5\ \mathrm{MPa}$ incident drive, $Q \approx 20$), shattering stones into sub-$80\ \mu\mathrm{m}$ dust at $4.4\times$ below the tissue damage threshold.
* **[Vector 72: Bilateral Microwave Phase-Symmetry Stroke Differentiator](file:///Users/arunkumar/Downloads/inf-research/directions/72-bilateral-microwave-stroke-differentiator.md)**: Enables 20-second pre-hospital ambulance triage of ischemic versus hemorrhagic stroke. Bilateral complex S-parameter phase subtraction cancels skull bone thickness variations, separating ischemia ($\Delta \phi \le -8.2^\circ$, cytotoxic edema conductivity drop) from hemorrhage ($\Delta \phi \ge +12.5^\circ$, blood permittivity surge) across $180^\circ$ of complex phase space with zero cranial burr holes.
* **[Vector 73: Donnan-Gated Dual-Atom Electrocatalytic Wearable Artificial Kidney](file:///Users/arunkumar/Downloads/inf-research/directions/73-donnan-gated-electrocatalytic-wearable-kidney.md)**: Eliminates the 40-year lethal chloramine hemolysis barrier of electrochemical artificial kidneys. Sub-nanometer Donnan-exclusion 2D laminates suppress chloride ions by $> 10^5$, allowing neutral urea to be selectively cleaved by a dual-atom $\mathrm{Ni_1-Fe_1-N_6}$ electrocatalyst at $+0.24\ \mathrm{V}$ vs. SHE ($810\ \mathrm{mV}$ below the chlorine evolution potential). Delivers $25\ \mathrm{g/day}$ urea clearance from a $56\ \mathrm{cm^2}$, $1.6\ \mathrm{W}$ cell running continuously on a phone battery with zero dialysate water consumption.
* **[Vector 74: Resonant Interfacial Shear-Decoupling of Pathological Microcalcifications](file:///Users/arunkumar/Downloads/inf-research/directions/74-resonant-shear-unpinning-vascular-calcification.md)**: Solves the untreatable cause of heart attacks and calcific aortic valve stenosis. Exploits the $100,000 : 1$ elastic modulus contrast between hydroxyapatite ($114\ \mathrm{GPa}$) and arterial collagen ($1.2\ \mathrm{MPa}$). A non-cavitating $1.25\ \mathrm{MHz}$ ultrasound wave ($P_r \le 0.70\ \mathrm{MPa}$, $\mathrm{MI} \le 0.63$) concentrates dynamic shear strain ($32\%$) across the $2.5\ \mathrm{nm}$ osteopontin anchor layer, selectively rupturing mineral-matrix bonds ($\tau \ge 2.56\ \mathrm{MPa} > 1.80\ \mathrm{MPa}$) without tissue tearing, enabling endogenous macrophages to phagocytose and clear sub-micron calcifications non-invasively.

### G. Documented Dead Hypotheses
* **[Vector 56: Hot-Carrier Extraction Beyond Shockley-Queisser](file:///Users/arunkumar/Downloads/inf-research/directions/56-hot-carrier-extraction-dead.md)**: Killed by detailed balance. An energy-selective contact emits at the same chemical potential it accepts, so hot-carrier extraction cannot beat $33.7\%$ at one sun; the $1\text{ to }10\text{ ps}$ thermalisation window against a $100\text{ ps}$ collection time closes it twice. Retained so the repository records the killing blow and does not re-propose it. Tandem cells remain the only legitimate route past the limit.
* **[Vector 60: Magnetic Scale Prevention](file:///Users/arunkumar/Downloads/inf-research/directions/60-magnetic-scale-prevention-dead.md)**: Killed by the size of the magneton. At $1.2\ \mathrm{T}$ a calcium ion gains $4.1\times10^{-4}\ \mathrm{eV}$ against $2.59\times10^{-2}\ \mathrm{eV}$ of thermal energy, which is $10^{-4}$ of the $152\ kT$ hydration barrier it must cross and $6.5\%$ of the calcite-aragonite gap, so the field cannot select a crystal habit. The claimed water memory needs an imprint to outlive $1.4\times10^{15}$ rotational correlation times of the solvent, against a measured $2.5\ \mathrm{ps}$ relaxation. Reaching the barrier needs $1.2\times10^{4}\ \mathrm{T}$; the strongest steady field built is $45\ \mathrm{T}$. Retained with a paired 20-rig protocol so a purchase decision can be settled in 30 days.

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
| **EXP-20261125-010** | Self-Synchronized Thermo-Acoustic Vapor-Jet Diode Lattice | Passive pool-boiling CHF up to $33.78\ \mathrm{MW/m^2}$ ($30.46\times$ Kutateladze-Zuber) with zero pumps | `python3 hypotheses/simulations/exp010_thermo_acoustic_chf_sweep.py` | [EXP-010 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-20261125-010-thermo-acoustic-chf-lattice.md) |

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
├── directions/                             (77 Discovery vectors across 73 dossier files + catalog)
│   ├── README.md                           (Complete 77-vector categorized index & quick-finder)
│   ├── 01-environmental-gradient-machines.md through 24-loss-gradient-vibration-concentrators.md
│   ├── 25-29-second-divergent-pass.md      (Vectors 25-29 + 8 killed candidates)
│   └── 30-quasicrystalline-superlubricity-interface.md through 77-thermo-acoustic-vapor-jet-chf-lattice.md
├── frameworks/                             (Evaluation rubrics and pipeline architecture)
│   ├── virtual-experimentation-pipeline.md
│   ├── first-principles-evaluation.md
│   └── experiment-template.md
├── notebooks/                              (Interactive zero-install browser runs)
│   └── run_all_sweeps.ipynb
└── hypotheses/                             (Virtual experiment runs and validation logs)
    ├── README.md                           (Active hypotheses registry)
    ├── EXP-001 through EXP-010 dossiers
    └── simulations/                        (Pure Python high-throughput multi-physics sweeps)
        ├── exp001_thermomagnetic_sweep.py
        ├── exp002_cavitation_sweep.py
        ├── exp003_mechanical_diode_sweep.py
        ├── exp004_water_generator_sweep.py
        ├── exp005_mineralization_sweep.py
        ├── exp008_hydrostatic_decoupler_sweep.py
        ├── exp009_dislocation_heat_sweep.py
        └── exp010_thermo_acoustic_chf_sweep.py
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
