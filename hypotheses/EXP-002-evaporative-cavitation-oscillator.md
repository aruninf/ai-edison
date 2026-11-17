# Experiment Specification: EXP-20261117-002

## 1. Metadata
* **Hypothesis ID:** EXP-20261117-002
* **Title:** Monolithic Nanoporous Evaporative Cavitation-Snap Oscillator (NECSO) for Zero-Power Autonomous Telemetry
* **Invention Domain:** Materials | Physics | Fluidics | Multi-Domain Transduction
* **Date Proposed:** 2026-11-17
* **Status:** Virtual-Validated
* **Primary Vector:** [07-transpiration-cavitation-metamaterials.md](file:///Users/arunkumar/Downloads/inf-research/directions/07-transpiration-cavitation-metamaterials.md)
* **Adversarial Audit Vector:** [06-adversarial-physical-falsification.md](file:///Users/arunkumar/Downloads/inf-research/directions/06-adversarial-physical-falsification.md)

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If an enclosed micro-cavity bounded by a bistable elastic membrane and an engineered hydrophobic nucleation site is coupled to a nanoporous evaporative membrane (pore diameter $d_p \le 5\text{ nm}$), then passive evaporation into ambient unsaturated air ($\text{RH} \le 80\%$) will drive the liquid into a metastable negative pressure state ($P_L \le -20\text{ MPa}$), inducing periodic cavitation rupture ($f \ge 0.05\text{ Hz}$), high-speed membrane snap-through ($v \ge 30\text{ m/s}$), and spontaneous capillary bubble collapse/refill, generating sustained peak mechanical impulse density $\ge 200\,\text{W/m}^2$ and electromagnetic RF chirps without silicon circuits, battery storage, or ambient thermal gradients.
* **Governing Mathematical Equations:**
  1. **Kelvin-Laplace Equilibrium Vapor Pressure:**
     $$P_L = \frac{R T}{V_m} \ln(\text{RH}) = P_{sat} - \frac{2 \gamma \cos\theta_{pore}}{r_p}$$
  2. **Heterogeneous Cavitation Nucleation Rate:**
     $$J_{het} = J_0 \exp\left( -\frac{16 \pi \gamma^3 f(\theta_{defect})}{3 k_B T (P_{sat} - P_L)^2} \right)$$
     Cumulative rupture probability over time interval $\Delta t$:
     $$\mathcal{P}_{cav} = 1 - \exp\left( - V_{cav} \int_0^t J_{het}(P_L(t')) dt' \right)$$
  3. **Membrane Deflection and Elastic Energy Accumulation:**
     $$w_0(P_L) \approx \frac{c_1 |P_L| a^4}{E h^3 + c_2 \sigma_0 a^2 h}$$
     $$E_{strain} = \int_0^{w_0} F_{restoring}(w) dw$$
  4. **Snap-Through Dynamics (Rayleigh-Plesset & Post-Rupture Kinetic Energy):**
     $$m_{eff} \ddot{w} + c_{fluid} \dot{w} + \frac{\partial U(w)}{\partial w} = A_{mem} (P_{sat} - P_{atm})$$
  5. **Capillary Condensation and Refill Time:**
     $$\tau_{refill} \approx \frac{8 \mu L_{channel} \Delta V_{bubble}}{\pi r_h^4 \Delta P_{capillary}}$$
* **Expected Transformation / Output:**
  * Input: Ambient relative humidity gradient between moist soil/substrate ($\text{RH} \approx 99\%$) and open atmosphere ($\text{RH} = 20\text{ to }75\%$).
  * Output: Periodic high-g mechanical snaps ($> 10^4\,g$), acoustic shockwaves, and piezoelectric/triboelectric RF pulse radiation.
  * Theoretical Maximum Energy Density: Elastic strain energy density in nanoconfined liquid and membrane: $\mathcal{U} \approx \frac{P_{cav}^2}{2 K_w} \approx \frac{(25 \times 10^6)^2}{2 (2.2 \times 10^9)} \approx 142\text{ kJ/m}^3$ per cavitation event.

---

## 3. High-Throughput In Silico Simulation Protocol (10,000+ Trials)
* **Simulation Engine & Methodology:**
  * Coupled multi-physics solver combining Kelvin evaporative flux integration, stochastic heterogeneous nucleation kinetics (Monte Carlo Poisson process), bistable non-linear plate snap-through mechanics, and viscous Stokes-Laplace bubble collapse refill.
  * Sweep across 10,000 randomized and grid-sampled parameter configurations.
* **Parameter Sweep Dimensions:**
  1. Nanopore radius $r_p$: $1.5\text{ nm}$ to $8.0\text{ nm}$
  2. Cavity volume $V_{cav}$: $0.05\,\mu\text{L}$ to $5.0\,\mu\text{L}$
  3. Membrane thickness $h$: $5\,\mu\text{m}$ to $50\,\mu\text{m}$
  4. Membrane pre-stress $\sigma_0$: $10\text{ MPa}$ to $200\text{ MPa}$
  5. Nucleation defect contact angle $\theta_{defect}$: $95^\circ$ to $160^\circ$
  6. Ambient relative humidity $\text{RH}$: $20\%$ to $85\%$
  7. Ambient temperature $T_{amb}$: $280\text{ K}$ to $320\text{ K}$
* **Total In Silico Runs Planned:** 10,000 parameter trials.
* **Computational Falsification Criteria:**
  * **Pore Dewetting Failure:** Meniscus pulls into the pore ($r_p > \frac{2\gamma \cos\theta}{|P_L|}$), allowing atmospheric air into the cavity (vapor lock).
  * **Premature Cavitation (Zero Energy):** Cavitation triggers at $P_L > -2\text{ MPa}$, failing to store sufficient elastic strain energy ($E_{snap} < 0.1\,\mu\text{J}$).
  * **Incomplete Refill (Stall):** Bubble fails to condense within $60\text{ seconds}$ due to insufficient Laplace re-wetting pressure.
  * **Plastic Yield / Fracture:** Membrane stress exceeds material yield limit ($\sigma_{max} > \sigma_{yield}$).

---

## 4. Physical / Real-World Validation Setup
*(Executed only after surviving in silico sweeps)*
* **Synthesis / Fabrication Specification:**
  * Monolithic anodic aluminum oxide (AAO) or track-etched silicon nitride membrane ($r_p \approx 2.5\text{ nm}$, porosity $\approx 35\%$).
  * Cavity etched in fused silica or silicon-on-insulator (SOI) wafer with localized fluoropolymer (PTFE-like) hydrophobic nanodot ($\theta = 110^\circ$).
  * Buckled SiN or PVDF (polyvinylidene fluoride) piezoelectric diaphragm for direct electromechanical pulse generation.
* **Instrumentation & Measurement Sensors:**
  * Ultra-high-speed imaging (100,000 fps) to capture cavitation bubble inception and microsecond snap-through.
  * Fast hydrophone / acoustic emission sensor (0.1 - 2.0 MHz bandwidth).
  * Spectrum analyzer and broadband dipole antenna to capture radiated RF chirps.
* **Control Baseline:**
  * Identical geometry without hydrophobic nucleation site (measuring spontaneous homogeneous limit).
  * Geometry with macroscopic pores ($r_p > 100\text{ nm}$) which dry out immediately without sustaining negative pressure.

---

## 5. Success and Falsification Thresholds
* **Virtual Milestone (Proceed to Lab):** At least $1.0\%$ of simulated configurations achieve stable, sustained limit-cycle oscillation ($f \ge 0.05\text{ Hz}$) with peak snap kinetic power $\ge 500\,\mu\text{W}$ under realistic ambient humidity ($40\% \le \text{RH} \le 75\%$).
* **Real-World Confirmation:** Fabricated chip exhibits periodic audible acoustic clicks and RF pulse emission without any electrical power input when exposed to ambient room air ($RH = 50\%$).
* **Kill Criteria:** Meniscus breakdown occurs across all geometries before reaching $-10\text{ MPa}$, or bubble refilling cannot overcome residual gas stagnation.

---

## 6. Simulation Code & Logs
* Simulation sweep script: [simulations/exp002_cavitation_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp002_cavitation_sweep.py)

---

## 7. In Silico Sweep Results & Pareto Validation (10,000 Trials)

* **Date Executed:** 2026-11-17
* **Total Trials:** 10,000 multi-physics evaluations
* **Viable Limit-Cycle Oscillating Candidates:** 1,620 (16.20% discovery window)
* **Failure Modes Falsified:**
  * Membrane Yield / Fracture ($a/h > 100$ under tens of MPa): 7,508 (75.1%)
  * Premature Cavitation ($P_{cav} > -2\text{ MPa}$, low energy): 847 (8.5%)
  * Meniscus Dewetting ($r_{pore} > 4.5\text{ nm}$): 22 (0.2%)
  * Insufficient Ambient Drying ($\text{RH} > 80\%$): 3 (0.0%)

### Top Discovered Candidates (Pareto Frontier)
1. **Champion High-Power Candidate (Trial #7212):**
   * Peak Snap Mechanical Power: $365.55\text{ W}$ ($1.41 \times 10^9\,\text{W/m}^2$)
   * Cavitation Rupture Tension: $-23.29\text{ MPa}$ ($230\text{ atm}$ negative pressure)
   * Stored Snap Strain Energy: $211.44\,\mu\text{J}$
   * Peak Snap Acceleration: $9.72 \times 10^6\,g$
   * Snap Duration: $0.58\,\mu\text{s}$
   * Cycle Frequency: $0.1070\text{ Hz}$ (1 snap every 9.3 seconds)
   * Geometry: Nanopore $r_{pore} = 1.68\text{ nm}$, Membrane $a = 0.51\text{ mm}$, $h = 37.8\,\mu\text{m}$, Nucleation pit $\theta = 138.9^\circ$
   * Operating Conditions: $\text{RH} = 66.3\%$, $T = 312.3\text{ K}$

2. **Champion High-Frequency Candidate (Trial #7111):**
   * Cycle Frequency: $49.65\text{ Hz}$ (sustained acoustic chirp / rapid telemetry)
   * Peak Mechanical Power: $0.529\text{ W}$
   * Cavitation Rupture Tension: $-3.82\text{ MPa}$
   * Stored Snap Strain Energy: $0.34\,\mu\text{J}$
   * Geometry: Nanopore $r_{pore} = 1.92\text{ nm}$, Membrane $a = 0.53\text{ mm}$, Nucleation pit $\theta = 115.5^\circ$

* **Disposition:** Virtual-Validated. Candidate graduates to microfabrication layout and laboratory benchmark specification.
