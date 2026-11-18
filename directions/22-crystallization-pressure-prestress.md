# Vector 22: Crystallization-Pressure Prestress Lattices

**Status:** wounded (kinetics; needs a persistent liquid film)
**Confidence:** 55%, basis: the Correns/Weyl pressure equation is textbook and salt heave is documented; cyclic net work is not.

## 1. Falsification statement

A porous ceramic saturated with NaCl solution, loaded by a rigid platen and cycled between 40% and 90% RH at 25 °C, must generate ≥5 MPa blocked stress at supersaturation ratio $S = 1.2$. It dies if blocked stress stays below 1 MPa, or if net mechanical work over 50 cycles is ≤ 0.

## 2. Fundamental problem

Generate megapascal static force and slow stroke from an ambient humidity swing, with no compressor, no electrical input, and no liquid reservoir to leak.

## 3. Mechanism

A crystal growing in a pore smaller than the crystal pushes on the walls with a pressure set by the chemical potential difference between the supersaturated pore liquid and the stressed solid. It keeps growing until the mechanical pressure raises the solid's chemical potential to match the solution. Reversing the humidity dissolves the crystal and unloads the pore. A percolating pore network converts this into bulk prestress.

## 4. Mathematical model

Correns equation:

$$p = \frac{RT}{V_m}\ln S$$

with $V_m(\mathrm{NaCl}) = 2.7\times10^{-5}\ \mathrm{m^3\,mol^{-1}}$, $RT/V_m = 9.2\times10^{7}\ \mathrm{Pa}$ at 298 K. Dimensionally $\mathrm{J\,mol^{-1}}/\mathrm{m^3\,mol^{-1}} = \mathrm{Pa}$. Checked.

| $S$ | $p$ |
| --- | --- |
| 1.05 | 4.5 MPa |
| 1.10 | 8.7 MPa |
| 1.20 | 16.7 MPa |
| 1.50 | 37 MPa |

Work per cycle: $W = p\,\Delta V_s$. With 25% porosity and 20% of pore volume exchanging per cycle, $\Delta V_s/V_{total} = 0.05$:

$$W/V = 10\ \mathrm{MPa}\times0.05 = 5\times10^{5}\ \mathrm{J\,m^{-3}}$$

0.5 MJ/m³ per cycle. Skeletal muscle is ~0.1 MJ/m³ per contraction; lithium-ion is ~$10^9\ \mathrm{J\,m^{-3}}$. This is an actuator, not an energy store. Cycle 2–8 h ⇒ 20–70 W/m³.

## 5. Contradiction ledger

- Not dry. Ion transport needs a connected liquid film; a sealed dry pore produces no growth. The "no fluid" framing is false at pore scale.
- Creep: a matrix that yields under 10 MPa dissipates the prestress it is meant to hold. Cementitious or alumina matrix required (creep rate must stay under 1%/year at 10 MPa).
- Dissolution hysteresis: the unloading branch runs at lower pressure than loading; round-trip loss estimated 40–60% [SPECULATION, no measurement basis].
- Kinetics are diffusion-limited: hours per cycle, and the 20% exchange figure assumes full pore refill.
- Triviality check: salt and frost heave have been documented for a century as a damage mechanism. The unclaimed item is the deliberate prestress cycle with a stated work bound. Originality 2 is scored on that basis.
- Prior art not checked (protocol lock 1).

## 6. Experiment and null result

Alumina or white-cement discs, 25% porosity, 20 mm diameter, saturated with NaCl at $S = 1.2$; rigid platen with a 20 kN load cell; RH chamber 40–90%, 25 °C, 50 cycles. Controls: salt-free disc (zero stress), pore-free disc, and a disc with pores >50 µm where growth pressure relaxes.

Null: blocked stress <1 MPa, or cycle 50 work equal to cycle 1 (no accumulation). Success: 8–17 MPa at $S=1.2$, which also validates the equation in confinement.

Cannot distinguish: pore pressure from thermal expansion of the cell — run a matched thermal-only control.

Cost: USD 2–5 k.

## 7. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| --- | --- | --- | --- | --- | --- |
| 2 | 4 | 4 | 5 | 2 | 5 |

Total 22/30.

## 8. Applications

Near-term: self-prestressing anchors and post-tensioned clamps that recover torque loss without maintenance access. Long-horizon: humidity-driven actuators for structures that must hold megapascal loads for years at zero power.

## 9. Unresolved

Whether a real cement matrix survives 50 loading cycles at 10 MPa without microcracking that short-circuits the pore network. That single failure mode decides the vector.
