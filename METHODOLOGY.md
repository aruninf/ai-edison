# Research Methodology and Physical Validation Protocols

This document defines the formal engineering principles, hypothesis structures, and validation rules governing all work in this repository.

## 1. First-Principles Decomposition

When addressing an engineering challenge, break the system down to physical invariants:

1. **State the Conservation Laws:**
   * Conservation of Mass-Energy ($\sum \dot{E}_{in} = \sum \dot{E}_{out} + \frac{dE_{sys}}{dt}$)
   * Conservation of Linear and Angular Momentum ($\sum \mathbf{F} = \frac{d\mathbf{p}}{dt}$)
   * Entropy Production ($\Delta S_{universe} \ge 0$)
2. **Isolate Intrinsic vs. Extrinsic Limitations:**
   * *Intrinsic limitations* are dictated by nature (e.g., speed of light in medium, Carnot efficiency, Landauer limit).
   * *Extrinsic limitations* are artifacts of current fabrication or legacy design choices (e.g., bearing friction, copper winding resistance, silicon gate oxide leakage).
3. **Target Extrinsic Bottlenecks with Novel Physics:**
   * Seek alternatives in neglected physical phenomena (e.g., elastocaloric effects, streaming potentials, topological acoustic metamaterials, magneto-rheological coupling).

## 2. Hypothesis Formulation Standard

Every proposed hardware mechanism must be formalized using the template in [experiment-template.md](file:///Users/arunkumar/Downloads/inf-research/frameworks/experiment-template.md) before any fabrication or simulation begins.

A valid hypothesis must answer:
* **Mechanism:** What specific physical property or field interaction produces the effect?
* **Governing Equation:** What mathematical model describes the phenomenon?
* **Falsification Threshold:** What measurable threshold determines that the mechanism is ineffective or non-viable?
* **Comparison Baseline:** What is the gold-standard conventional hardware mechanism, and what is its quantified efficiency or performance?

## 3. Benchmarking Against the State of the Art

Never evaluate an invention in isolation. Every measurement must compare directly against existing electromechanical counterparts:
* **Specific Energy (Wh/kg or J/kg):** Compared against lithium-ion, ultracapacitors, and compressed pneumatic storage.
* **Power Density (W/kg or W/m3):** Compared against standard brushless DC motors and hydraulic actuators.
* **Specific Force / Torque Density (N/kg or Nm/kg):** Compared against electromagnetic gearmotors and shape memory alloys.
* **Thermodynamic Efficiency ($\eta$):** Measured as output useful work divided by total input energy, accounting for ambient losses.

## 4. Integrity and Falsification Rules

* Negative results are documented with the exact same rigor as successful outcomes.
* If an experiment violates established laws (e.g. over-unity energy, reactionless propulsion), the primary assumption must always be instrumentation error, calibration drift, or unmeasured boundary leakage until validated independently.
