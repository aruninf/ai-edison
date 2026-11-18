# Vector 23: Critical-Casimir Tunable Springs

**Status:** wounded (critical slowing; van der Waals background)
**Confidence:** 50%, basis: the critical Casimir force was measured at the pN level; a stiffness specification at 1 mm² scale is unmeasured.

## 1. Falsification statement

In a sealed cell of 2,6-lutidine/water at fixed plate gap $d = 100$ nm, sweep $\Delta T = T - T_c$ from 0.5 K to 2 mK and measure sphere–plate force. The hypothesis dies if $|dF/dT|$ stays below 5 nN per mK at 1 mm² effective area, or if the force is attractive at every $\Delta T$.

## 2. Fundamental problem

Set mechanical stiffness without wires, without a magnetic field, and without touching the object.

## 3. Mechanism

A binary liquid near its demixing point develops order-parameter fluctuations with correlation length $\xi$. Confining that fluid between two plates excludes fluctuation modes longer than the gap, which produces a measurable pressure — the critical Casimir force. $\xi$ is set by temperature alone, so temperature becomes a stiffness knob: 2 mK changes $\xi$ by a factor of two.

## 4. Mathematical model

$$\xi = \xi_0\,\left|\frac{T-T_c}{T_c}\right|^{-\nu},\qquad
P = \frac{k_BT}{d^3}\,\vartheta(d/\xi),\qquad
k = \left|\frac{\partial F}{\partial d}\right| \approx \frac{F}{d}$$

With $\xi_0 = 0.2$ nm, $\nu = 0.63$, $T_c = 307$ K [UNVERIFIED]:

| $t=(T_c-T)/T_c$ | $\xi$ |
| --- | --- |
| $10^{-3}$ | 16 nm |
| $10^{-4}$ | 66 nm |
| $10^{-5}$ | 280 nm |

$k_BT/d^3$ at $d = 100$ nm is 4.1 Pa. With $\vartheta \sim 0.3$–1 at $d/\xi \sim 1.5$: $P = 1$–4 Pa. On 1 mm²: $F = 1$–4 µN. Stiffness $k = F/d = 10$–40 N/m — the range of a MEMS cantilever.

Sensitivity: $\partial F/\partial T = F\nu/(tT_c)$. At $t = 10^{-4}$: $3\ \mu N \times 0.63/(10^{-4}\times307) = 6\times10^{-5}$ N/K, i.e. 60 nN/mK.

Response time: $\tau = \tau_0 t^{-\nu z}$ with $\nu z \approx 1.9$, $\tau_0 = 10^{-8}$–$10^{-10}$ s ⇒ 5 ms to 0.5 s at $t = 10^{-4}$. Dimensionless checks: $t^{-\nu}$ dimensionless, $\vartheta$ dimensionless, $k_BT/d^3$ in Pa. Checked.

## 5. Contradiction ledger

- Van der Waals background at 100 nm is ~0.5 Pa for $A = 10^{-20}$ J — comparable to the signal. Discriminate by $\Delta T$ scaling, not by absolute force.
- Refractive index anomaly near $T_c$ moves the optical lever calibration; force must be read by a second, non-optical channel.
- Critical slowing: at $t = 10^{-4}$ a 0.5 s response is plausible; at $t = 10^{-5}$ it exceeds 10 s. Fast switching and high gain are mutually exclusive.
- Viscosity divergence adds damping that grows with the same variable as the stiffness, so a resonance-based readout self-detunes.
- Gap must be held to 1% to know $P$ to 3%; thermal drift of the holder at mK level over 1 µm is the practical limit.
- Triviality check: the force itself is published. The unclaimed item is a sealed, wire-free, temperature-addressed spring with a stated stiffness and slew rate.
- Prior art not checked (protocol lock 1).

## 6. Experiment and null result

AFM colloidal probe (10 µm sphere) against a gold plate in a sealed lutidine/water cell, $d = 100$–300 nm, $T$ from 25 to 34 °C, control ±3 mK, force resolution 10 pN. Controls: pure water cell (no criticality), and a cell at fixed $T$ far from $T_c$ to bound drift.

Null: $\partial F/\partial T < 5$ nN/mK, or force sign independent of $\Delta T$. Success: 20–80 nN/mK at $t = 10^{-4}$, with a force that inverts when one surface's adsorption preference is switched.

Cannot distinguish: Casimir from solvation or patch-charge forces at gaps below 30 nm — stay above 80 nm.

Cost: USD 15–40 k.

## 7. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| --- | --- | --- | --- | --- | --- |
| 3 | 4 | 3 | 4 | 3 | 3 |

Total 20/30.

## 8. Applications

Near-term: thermally addressed stiffness trim for MEMS resonators in sealed packages, where feedthroughs are the failure point. Long-horizon: a force standard transferable by temperature rather than by mass.

## 9. Unresolved

Whether the effect survives at engineering scale: extrapolating to 1 cm² raises force to 40 µN but multiplies gap-flatness error, and flatness at 100 nm over 1 cm² is the deciding fabrication problem.
