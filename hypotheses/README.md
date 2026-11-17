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

---

## Guidelines for Filing
1. Copy the structure from [experiment-template.md](file:///Users/arunkumar/Downloads/inf-research/frameworks/experiment-template.md).
2. Name the file according to its hypothesis ID (e.g. `EXP-YYYYMMDD-00X-<descriptor>.md`).
3. Place all simulation scripts, CAD models, or sensor logs into `hypotheses/simulations/` or a dedicated experiment subdirectory.
4. Execute at least 10,000 parameter variations in simulation before advancing a candidate to physical fabrication or laboratory testing.
