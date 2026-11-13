# Template: In Silico and Real-World Experiment Specification

Use this document template when filing a new experimental test plan in the `hypotheses/` directory.

---

## 1. Metadata
* **Hypothesis ID:** EXP-YYYYMMDD-00X
* **Title:** Concise mechanism description
* **Invention Domain:** Materials | Energy | Chemistry | Mechanics | Computing | Multi-Domain
* **Date Proposed:** YYYY-MM-DD
* **Status:** Proposed | In-Simulation | Virtual-Validated | Physically-Testing | Falsified | Archived

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If [input/composition/configuration] is applied to [system/substrate], then [measurable response/property] will occur via [underlying scientific mechanism], achieving [quantified metric] compared to baseline [legacy benchmark].
* **Governing Mathematical Equation:**
  $$\dots$$
* **Expected Transformation / Output:**
  * Input type:
  * Output / Functional property:
  * Theoretical physical upper limit:

---

## 3. High-Throughput In Silico Simulation Protocol (10,000+ Trials)
* **Simulation Engine & Methodology:** (e.g. Molecular Dynamics, FEA, CFD, FDTD, Lumped Parameter Solvers)
* **Parameter Sweep Dimensions:**
  1. Parameter 1 (range, step, distribution)
  2. Parameter 2
  3. Environmental bounds (Temperature, Pressure, Fields)
* **Total In Silico Runs Planned:** (e.g. 10,000 to 50,000 variations)
* **Computational Falsification Criteria:** Threshold at which the virtual run is tagged as non-viable or unstable.

---

## 4. Physical / Real-World Validation Setup
*(Executed only after surviving in silico sweeps)*
* **Synthesis / Fabrication Specification:** Required material, synthesis protocol, or machining tolerances.
* **Instrumentation & Measurement Sensors:** Equipment used to verify physical properties against simulation curves.
* **Control Baseline:** Identical setup without the active mechanism or novel material variant.

---

## 5. Success and Falsification Thresholds
* **Virtual Milestone (Proceed to Lab):** Top candidate displays performance $> X$ with error bounds $< Y$ across 10,000 simulated conditions.
* **Real-World Confirmation:** Empirical measurement matches simulation within tolerance $Z$.
* **Kill Criteria:** Mechanism fails to outperform baseline or exhibits fatal degradation.

---

## 6. Results and Archival
* **Virtual Sweep Summary:** Pareto front plots, parameter sensitivity heatmap.
* **Empirical Validation Data:** Sensor traces and laboratory measurements.
* **Disposition:** Verified Breakthrough -> File IP / Deploy | Falsified -> Document root cause and archive.
