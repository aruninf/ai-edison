# Experiment Specification: EXP-20261117-001

## 1. Metadata
* **Hypothesis ID:** EXP-20261117-001
* **Title:** Room-Temperature Solid-State Thermomagnetic Cantilever Oscillator for Micro-Gradient Energy Harvesting
* **Invention Domain:** Energy | Mechanics | Materials
* **Date Proposed:** 2026-11-17
* **Status:** In-Simulation
* **Primary Vector:** [01-environmental-gradient-machines.md](file:///Users/arunkumar/Downloads/inf-research/directions/01-environmental-gradient-machines.md)
* **Adversarial Audit Vector:** [06-adversarial-physical-falsification.md](file:///Users/arunkumar/Downloads/inf-research/directions/06-adversarial-physical-falsification.md)

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If a ferromagnetic cantilever composed of a low-Curie-point alloy ($T_c \approx 295\text{ to }305\text{ K}$, e.g. Gadolinium or Heusler alloy $\text{Ni}_{50}\text{Mn}_{34}\text{In}_{16}$) is positioned between a permanent neodymium magnet with heat source and a passive ambient heat sink, then continuous sustained mechanical oscillation ($f \ge 2\text{ Hz}$) will occur under micro-thermal gradients ($\Delta T \le 3.0\text{ K}$) via cyclic magnetization loss and conductive cooling, generating continuous kinetic work density $\ge 50\,\mu\text{W/cm}^3$ without external battery power or electronic switching.
* **Governing Mathematical Equation:**
  * Magnetization temperature dependence:
    $$M(T) \approx M_0 \left(1 - \frac{T}{T_c}\right)^\beta \quad (T < T_c), \quad M(T) \approx 0 \quad (T \ge T_c)$$
  * Mechanical equation of motion:
    $$m_{eff} \ddot{x} + c \dot{x} + k x = F_{mag}(x, T) = \frac{\mu_0 M(T) V \cdot \nabla |\mathbf{B}(x)|^2}{2}$$
  * Lumped thermal balance during cycle:
    $$m c_p \frac{dT}{dt} = h_{contact} A_{contact} (T_{hot} - T) - h_{conv} A (T - T_{sink})$$
* **Expected Transformation / Output:**
  * Input: Ambient natural convective draft and low-grade micro-thermal gradient ($\Delta T = 1.0\text{ to }3.0\text{ K}$).
  * Output: Sustained periodic oscillation for electromagnetic or piezoelectric impulse generation.
  * Theoretical Upper Bound: Carnot efficiency bound $\eta_{Carnot} = 1 - \frac{T_C}{T_H} \approx \frac{3\text{ K}}{300\text{ K}} = 1.0\%$.

---

## 3. High-Throughput In Silico Simulation Protocol (10,000+ Trials)
* **Simulation Engine & Methodology:** 
  * Coupled 4th-order Runge-Kutta numerical integration of dynamic magneto-thermo-mechanical ODEs.
  * Monte Carlo sweep over 10,000 variations in geometry, spring stiffness, contact thermal resistance, and ambient boundary conditions.
* **Parameter Sweep Dimensions:**
  1. Cantilever length $L$: $10.0\text{ mm}$ to $50.0\text{ mm}$ (step $0.5\text{ mm}$)
  2. Alloy thickness $t$: $50\,\mu\text{m}$ to $500\,\mu\text{m}$ (step $10\,\mu\text{m}$)
  3. Spring stiffness $k$: $0.5\text{ N/m}$ to $20.0\text{ N/m}$
  4. Temperature gradient $\Delta T$: $0.5\text{ K}$ to $5.0\text{ K}$
  5. Magnetic gap $d_0$: $0.5\text{ mm}$ to $5.0\text{ mm}$
* **Total In Silico Runs Planned:** 10,000 parameter points.
* **Computational Falsification Criteria:**
  * System settles to a static equilibrium state (oscillation terminates due to damping or magnetic latching).
  * Net mechanical energy generated per cycle $\le 0$.
  * Required contact thermal conductance violates physical interface contact limits ($h_{contact} > 50,000\text{ W/m}^2\text{K}$).

---

## 4. Physical / Real-World Validation Setup
*(Executed only after surviving in silico sweeps)*
* **Synthesis / Fabrication Specification:** High-purity Gadolinium foil ($99.9\%$, $100\,\mu\text{m}$ thickness) micro-welded to a high-yield spring steel substrate.
* **Instrumentation & Measurement Sensors:** High-speed laser displacement vibrometer (Keyence LK-G5000), synchronized with FLIR infrared thermal camera and calibrated Hall effect magnetometer.
* **Control Baseline:** Equivalent non-magnetic dummy cantilever of identical thermal mass and mechanical stiffness under the same temperature gradient.

---

## 5. Success and Falsification Thresholds
* **Virtual Milestone (Proceed to Lab):** At least $0.5\%$ of simulated configurations achieve limit-cycle stability with continuous output power density $\ge 50\,\mu\text{W/cm}^3$ under $\Delta T \le 2.0\text{ K}$.
* **Real-World Confirmation:** Fabricated oscillator achieves within $\pm 20\%$ of predicted oscillation frequency and amplitude in an environmental chamber.
* **Kill Criteria:** Cantilever sticks permanently to the hot magnet face (magnetic lockup) due to insufficient cooling rate in air under natural convection.

---

## 6. Simulation Code & Logs
* Simulation sweep script: [simulations/exp001_thermomagnetic_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp001_thermomagnetic_sweep.py)
