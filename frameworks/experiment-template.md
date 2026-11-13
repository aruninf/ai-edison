# Template: Physical Experiment Specification

Use this document template when filing a new experimental test plan in the `hypotheses/` directory.

---

## 1. Metadata
* **Hypothesis ID:** EXP-YYYYMMDD-00X
* **Title:** Concise mechanism description
* **Research Vector:** Environmental-Gradient | Material-Computation | Integrated-Machines
* **Date Proposed:** YYYY-MM-DD
* **Status:** Proposed | Active | Validated | Falsified | Archived

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If [physical condition/input] is applied to [material/geometry/substrate], then [measurable physical response] will occur via [physical mechanism], achieving [quantified metric] compared to baseline [legacy benchmark].
* **Governing Mathematical Equation:**
  $$\dots$$
* **Expected Energy / Work Transformation:**
  * Input energy type:
  * Output work type:
  * Theoretical upper efficiency limit:

---

## 3. Physical Apparatus Design
* **BOM (Bill of Materials):**
  1. Component A (Material, Specification, Supplier)
  2. Component B
* **CAD / Geometric Layout:** Schematic or sketch of the test setup.
* **Key Controlled Variables:**
  * Temperature ($T \pm \dots$)
  * Pressure / Atmospheric condition
  * Mechanical boundary conditions / Constraints

---

## 4. Measurement & Instrumentation
* **Sensors and Acquisition Equipment:**
  * Primary sensor (type, sampling rate, precision):
  * Secondary / control sensor:
* **Calibration Protocol:** How zero-drift and environmental noise are subtracted.
* **Control Baseline:** What identical apparatus is tested concurrently without the active mechanism?

---

## 5. Success / Falsification Criteria
* **Validation Threshold (Go):** Output metric exceeds $X$ under conditions $Y$.
* **Falsification Threshold (Kill):** Output metric fails to exceed $Z$ or parasitics exceed $W$, proving non-viability.
* **Decision Date:** Specific milestone by which the experiment must produce conclusive numbers.

---

## 6. Empirical Results & Conclusion
*(Completed post-experiment)*
* **Measured Data:** Summary table or plot.
* **Error Analysis:** Sources of uncertainty.
* **Disposition:** Validated -> Proceed to V2 Prototype | Falsified -> Document root cause and archive.
