# Experiment Specification: EXP-20261125-012

## 1. Metadata
* **Hypothesis ID:** EXP-20261125-012
* **Title:** Passive Diurnal-Thermal Snap-Anvil Dust-Ejection Lattice (DTSA-DL)
* **Invention Domain:** Mechanics | Optics | Space Systems | Materials
* **Date Proposed:** 2026-11-25
* **Status:** Virtual-Validated
* **Primary Vector:** [79-diurnal-thermal-snap-anvil-dust-ejection.md](file:///Users/arunkumar/Downloads/inf-research/directions/79-diurnal-thermal-snap-anvil-dust-ejection.md)
* **Adversarial Audit Vector:** [06-adversarial-physical-falsification.md](file:///Users/arunkumar/Downloads/inf-research/directions/06-adversarial-physical-falsification.md)

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If an optically transparent $\mathrm{SiO_2/CaF_2}$ bilayer micro-dome array ($r_d = 2.32\ \mathrm{mm}$, $t_d = 24.6\ \mu\mathrm{m}$, rigid anvil stop clearance $\Delta x_{\text{stop}} = 0.26\ \mu\mathrm{m}$) is subjected to a passive diurnal temperature swing ($\Delta T = 15$ to $95\ \mathrm{K}$), saddle-node snap-through and micro-anvil impact will generate $a_{\text{peak}} \ge 49,743\,g$ (median $466,796\,g$) while keeping peak stress $\le 172\ \mathrm{MPa}$, detaching dry silicate dust down to $0.35\ \mu\mathrm{m}$ with zero electricity and zero water.
* **Governing Mathematical Equation:**
  $$v_{\text{snap}} = \Delta\alpha\,\Delta T \sqrt{\frac{\eta_{\text{snap}} E_{\text{eff}}}{\rho_d}}, \qquad a_{\text{peak}} = \frac{v_{\text{snap}}^2}{2 \Delta x_{\text{stop}}} \ge \frac{A_H}{4 \pi z_0^2 \rho_p d_p^2}$$
* **Falsification Statement:** Killed if LDV-measured snap acceleration stays below $10,000\,g$ or dust mass clearance is $< 20\%$ per thermal cycle.

---

## 3. High-Throughput In Silico Simulation Protocol
* Coupled thermo-elastic-impact solver evaluating thermal mismatch strain, bending stress, snap kinetic velocity, anvil deceleration, and van der Waals particle detachment diameter.
* Sweep across 10,000 parameter variations of $\Delta T$ ($15 - 100\ \mathrm{K}$), $\Delta \alpha$ ($10 - 24\ \mathrm{ppm/K}$), $t_d$ ($15 - 80\ \mu\mathrm{m}$), $r_d$ ($0.5 - 3.0\ \mathrm{mm}$), $\eta_{\text{snap}}$ ($0.15 - 0.45$), and $\Delta x_{\text{stop}}$ ($0.25 - 1.50\ \mu\mathrm{m}$).
* Simulation solver: [simulations/exp012_thermal_snap_dust_ejection_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp012_thermal_snap_dust_ejection_sweep.py)

---

## 4. In Silico Sweep Results & Validation (10,000 Trials)
* **Date Executed:** 2026-11-25
* **Total Trials:** 10,000 multi-physics evaluations ($0.020\ \mathrm{s}$ runtime)
* **Adhesion Thresholds:** $10\ \mu\mathrm{m} = 12,436\,g$ | $5\ \mu\mathrm{m} = 49,743\,g$
* **Viable $5\ \mu\mathrm{m}$ Ejection Regimes:** 9,330 (93.30% design window)
* **Partial ($10\ \mu\mathrm{m}$ only) / Weak / Fracture:** 650 (6.50%) / 20 (0.20%) / 0 (0.00%)
* **Viable Regime Median Acceleration:** **$466,796\,g$**
* **Top Discovered Champion (Trial #7877):**
  * Peak Impact Acceleration: **$10,322,754\,g$**
  * Minimum Detachable Dust: **$0.35\ \mu\mathrm{m}$**
  * Snap Velocity: **$7.27\ \mathrm{m/s}$**
  * Peak Bending Stress: **$172.0\ \mathrm{MPa}$** ($< 350\ \mathrm{MPa}$ fatigue limit)
  * Geometry: $\Delta T = 94.5\ \mathrm{K}$, $\Delta\alpha = 22.6\ \mathrm{ppm/K}$, $t_d = 24.6\ \mu\mathrm{m}$, $r_d = 2.32\ \mathrm{mm}$, $\Delta x_{\text{stop}} = 0.26\ \mu\mathrm{m}$
* **Disposition:** Virtual-Validated.
