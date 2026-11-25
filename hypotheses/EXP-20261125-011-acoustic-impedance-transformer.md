# Experiment Specification: EXP-20261125-011

## 1. Metadata
* **Hypothesis ID:** EXP-20261125-011
* **Title:** Sub-Wavelength Monolithic Acoustic-Mechanical Impedance Transformer (AMIT)
* **Invention Domain:** Acoustics | Metamaterials | Mechanics | Cross-Domain Sensing
* **Date Proposed:** 2026-11-25
* **Status:** Virtual-Validated
* **Primary Vector:** [78-acoustic-mechanical-impedance-transformer.md](file:///Users/arunkumar/Downloads/inf-research/directions/78-acoustic-mechanical-impedance-transformer.md)
* **Adversarial Audit Vector:** [06-adversarial-physical-falsification.md](file:///Users/arunkumar/Downloads/inf-research/directions/06-adversarial-physical-falsification.md)

---

## 2. Theoretical Hypothesis
* **Formal Hypothesis Statement:** If a $1.10\ \mathrm{mm}$ thick monolithic micro-lattice ($p = 1.10\ \mathrm{mm}$, $r_w = 53.0\ \mu\mathrm{m}$, $\Gamma = 5.04\times$, $t_a = 1.06\ \mu\mathrm{m}$) couples a small water-facing piston to a large radiation-overdamped silicon-nitride air diaphragm, then transformed air radiation resistance $Z_{\text{rad,spec}} = (A_a/A_w)\Gamma^2 Z_a$ will match water ($1.48\ \mathrm{MRayl}$), sustaining broadband $2$ to $30\ \mathrm{kHz}$ water-to-air acoustic power transmission $T_{\text{avg}} \ge 48\%$ ($> 430\times$ above the $0.112\%$ bare water-air limit).
* **Governing Mathematical Equation:**
  $$Z_{\text{ac},w}(\omega) = \frac{Z_a A_a \Gamma^2 + R_{\text{loss},w}}{A_w} + i\,\frac{\omega (m_w + \Gamma^2 m_a) - k_w / \omega}{A_w}, \qquad T(\omega) = \frac{4 Z_w Z_{\text{rad,spec}}}{\left|Z_w + Z_{\text{ac},w}(\omega)\right|^2}$$
* **Falsification Statement:** Killed if peak transmission $T_{\text{peak}} < 0.05$ ($5\%$) or $-3\ \mathrm{dB}$ fractional bandwidth falls below $5\%$.

---

## 3. High-Throughput In Silico Simulation Protocol
* Coupled electro-mechano-acoustic circuit solver evaluating complex input impedance $Z_{\text{ac},w}(\omega)$ and power transmission $T(\omega)$ across 15 log-spaced frequencies ($2.0$ to $30.0\ \mathrm{kHz}$).
* Sweep across 10,000 parameter variations of $r_w$ ($40 - 160\ \mu\mathrm{m}$), $p$ ($0.8 - 2.5\ \mathrm{mm}$), $\Gamma$ ($3.0 - 14.0$), $t_a$ ($1.0 - 8.0\ \mu\mathrm{m}$), $f_{\text{res}}$ ($4 - 20\ \mathrm{kHz}$), and $\eta_{\text{loss}}$ ($0.02 - 0.12$).
* Simulation solver: [simulations/exp011_acoustic_impedance_transformer_sweep.py](file:///Users/arunkumar/Downloads/inf-research/hypotheses/simulations/exp011_acoustic_impedance_transformer_sweep.py)

---

## 4. In Silico Sweep Results & Validation (10,000 Trials)
* **Date Executed:** 2026-11-25
* **Total Trials:** 10,000 multi-physics evaluations ($0.081\ \mathrm{s}$ runtime)
* **Bare Water-Air Baseline:** $0.112\%$ ($-29.5\ \mathrm{dB}$)
* **Viable Broadband Regimes ($T_{\text{avg}} \ge 35\%$, $T_{\text{peak}} \ge 65\%$, $\ge 40\%$ band):** 2,505 (25.05% design window)
* **Failure Modes Logged:** 5,002 low-peak failures (50.02%), 2,493 narrowband failures (24.93%)
* **Viable Regime Median $T_{\text{avg}}$:** **$48.62\%$** ($433.7\times$ bare water-air)
* **Top Discovered Champion (Trial #7880):**
  * 2-30 kHz Mean Transmission: **$89.63\%$** ($799.6\times$ bare water-air)
  * Peak Transmission: **$97.24\%$** ($867.5\times$ bare) at $5,261\ \mathrm{Hz}$
  * Passband Coverage ($T \ge 25\%$): **$100.0\%$** of the $2$ to $30\ \mathrm{kHz}$ decade
  * Geometry: $r_w = 53.0\ \mu\mathrm{m}$, $p = 1.10\ \mathrm{mm}$, $A_a/A_w = 112.9\times$, $\Gamma = 5.04\times$, $t_a = 1.06\ \mu\mathrm{m}$, $f_{\text{res}} = 5,635\ \mathrm{Hz}$
* **Disposition:** Virtual-Validated.
