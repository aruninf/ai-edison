# Research Vector 04: Dissipative Thermodynamic Logic

## Objective
Implement computational logic and state inference powered by irreversible non-equilibrium thermodynamic fluxes (entropy production, thermal diffusion, and concentration gradients), operating without semiconductor transistors, clock trees, or external electric power grids.

---

## 1. Physical Principles and Governing Laws

Traditional electronic computation treats heat dissipation as parasitic waste (Landauer's limit $k_B T \ln 2$). Dissipative thermodynamic logic flips this paradigm: computation is driven directly by continuous entropy flow across an open system.

### A. Coupled Non-Equilibrium Transport (Onsager Relations)
* **Mechanism:** Interacting thermodynamic forces (temperature gradients $\mathbf{X}_T = -\frac{\nabla T}{T^2}$ and chemical potential gradients $\mathbf{X}_\mu = -\frac{\nabla \mu}{T}$) drive conjugated flux vectors (heat flux $\mathbf{J}_q$ and particle/charge flux $\mathbf{J}_N$):
  $$\mathbf{J}_i = \sum_{k} L_{ik} \mathbf{X}_k$$
* **Bifurcation Dynamics:** In non-linear geometric cavities, asymmetric thermal dissipation induces flow bifurcation, stabilizing binary or multistable vortex states corresponding to discrete logic symbols without solid-state gates.
* **Governing Relation:** Prigogine's minimum entropy production theorem near equilibrium, transitioning to non-linear Rayleigh-Benard / Soret-effect bifurcations far from equilibrium.

### B. Micro-Thermal and Capillary Logic Topologies
* **Mechanism:** Fluidic micro-droplets or phase-change boundaries steered along heat fluxes within micro-machined geometric channels.
* **Logic Realization:**
  * **AND / OR:** Two orthogonal thermal flux streams intersecting at a micro-nozzle; droplet or heat plume deflection represents output state.
  * **NOT / Inverter:** Thermal quenching channel where high input flux redirects working fluid away from the detection basin.

### C. Open Hardware Challenges
* **Drift & Settling Time:** Response times bounded by thermal diffusion time constants $\tau \approx \frac{L^2}{\alpha}$, requiring sub-micron fluid-thermal channels to achieve millisecond or sub-millisecond execution.
* **Ambient Thermal Noise:** Preventing ambient thermal fluctuations from corrupting delicate non-equilibrium state trajectories.

---

## 2. Legacy Failure Modes to Avoid

* **Attempting to Replicate Megahertz Binary CPUs:** Thermal/entropy logic cannot compete with silicon on clock frequency; its target niche is autonomous zero-power environmental edge classification and self-routing physical machinery.
* **Neglecting Second Law Constraints:** Any proposed gate cycle must explicitly demonstrate positive global entropy generation ($\frac{d S_{universe}}{dt} > 0$).

---

## 3. High-Priority Research Hypotheses

1. **Passive Thermally-Switched Logic Gates:** Micro-patterned porous membranes where local thermocapillary (Marangoni) forces route passive liquid pulses based on threshold thermal inputs.
2. **Phase-Change Thermal Inverters:** Utilizing sharp solid-liquid or martensitic phase boundaries as self-resetting physical binary states driven purely by cyclic environmental temperature fluctuations.
