# Hypotheses and Experiment Registry

This directory stores all active, validated, and falsified experimental logs across the AI Edison engine.

---

## Active Hypotheses Table

| ID | Title | Primary Vector | Status | Date Created | Last Result / Artifact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EXP-20261117-001** | Room-Temperature Solid-State Thermomagnetic Oscillator | Vector 01 & 06 | In-Simulation | 2026-11-17 | [EXP-001 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-001-thermomagnetic-oscillator.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp001_thermomagnetic_sweep.py) |
| **EXP-20261117-002** | Monolithic Nanoporous Evaporative Cavitation-Snap Oscillator (NECSO) | Vector 07 & 06 | Virtual-Validated | 2026-11-17 | [EXP-002 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-002-evaporative-cavitation-oscillator.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp002_cavitation_sweep.py) |
| **EXP-20261117-003** | Monolithic Chiral-Cosserat Static Mechanical Diode | Vector 12 & 06 | Virtual-Validated | 2026-11-17 | [EXP-003 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-003-static-mechanical-diode.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp003_mechanical_diode_sweep.py) |
| **EXP-20261117-004** | Monolithic Bistable Auxetic Water Generator (BAWG) | Vector 13 & 06 | Virtual-Validated | 2026-11-17 | [EXP-004 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-004-mechanochemical-water-generator.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp004_water_generator_sweep.py) |
| **EXP-20261117-005** | Piezocatalytic Self-Mineralizing Concrete Composite | Vector 14 & 06 | Virtual-Validated | 2026-11-17 | [EXP-005 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-005-mechanocatalytic-carbon-mineralizer.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp005_mineralization_sweep.py) |
| **EXP-20261117-006** | Monolithic Flexogalvanic Solid-State Redox Engine | Vector 17 & 06 | Proposed | 2026-11-17 | [EXP-006 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-006-flexogalvanic-redox-engine.md) |
| **EXP-20261117-007** | Monolithic Topological Acoustic Soliton Flywheel | Vector 18 & 06 | Proposed | 2026-11-17 | [EXP-007 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-007-topological-soliton-flywheel.md) |
| **EXP-20261117-008** | Smectic Topological Hydrostatic Pressure Decoupler | Vector 19 & 06 | Virtual-Validated | 2026-11-17 | [EXP-008 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-008-smectic-hydrostatic-decoupler.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp008_hydrostatic_decoupler_sweep.py) |
| **EXP-20261117-009** | Cooperative Spin-State Solid-State Latent Heat Capacitor | Vector 20 & 06 | Virtual-Validated | 2026-11-17 | [EXP-009 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-009-dislocation-latent-heat-capacitor.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp009_dislocation_heat_sweep.py) |
| **EXP-20261125-010** | Self-Synchronized Thermo-Acoustic Vapor-Jet Diode Lattice (TAVJ-DL) | Vector 77 & 06 | Virtual-Validated | 2026-11-25 | [EXP-010 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-20261125-010-thermo-acoustic-chf-lattice.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp010_thermo_acoustic_chf_sweep.py) |
| **EXP-20261125-011** | Sub-Wavelength Monolithic Acoustic-Mechanical Impedance Transformer (AMIT) | Vector 78 & 06 | Virtual-Validated | 2026-11-25 | [EXP-011 Dossier](file:///Users/arunkumar/Downloads/inf-research/hypotheses/EXP-20261125-011-acoustic-impedance-transformer.md) & [10,000-Trial Sweep](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp011_acoustic_impedance_transformer_sweep.py) |

---

## Guidelines for Filing
1. Copy the structure from [experiment-template.md](file:///Users/arunkumar/Downloads/inf-research/frameworks/experiment-template.md).
2. Name the file according to its hypothesis ID (e.g. `EXP-YYYYMMDD-00X-<descriptor>.md`).
3. Place all simulation scripts, CAD models, or sensor logs into `hypotheses/simulations/` or a dedicated experiment subdirectory.
4. Execute at least 10,000 parameter variations in simulation before advancing a candidate to physical fabrication or laboratory testing.
