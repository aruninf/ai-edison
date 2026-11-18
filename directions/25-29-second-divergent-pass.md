# Vectors 25–29: Second Divergent Pass

Five entries, each with the example, the advantages, and the use case stated plainly. Same rules: falsification first, magnitudes mandatory, prior art unchecked (protocol lock 1).

---

## Vector 25: Thermoradiative Night Cells

**Falsification:** A 0.15 eV bandgap diode held 60 K above a 250 K sink must deliver ≥1 W/m² at 0.1 V. It dies below 0.1 W/m².
**Mechanism:** A diode hotter than its surroundings emits more photons than it absorbs. Those photons carry energy away; the electron-hole pairs they create are extracted at a lower voltage than the gap, so the cell converts a radiator's waste heat into DC current instead of dumping it.
**Magnitudes:** $\sigma T^4$ at 350 K is 850 W/m²; radiated at 250 K sink, 630 W/m² net. Ideal conversion 2–8% ⇒ 12–50 W/m². Real diodes: 1–5 W/m² [UNVERIFIED].
**Example:** a satellite radiator panel that already exists for thermal control, now also producing housekeeping power.
**Pros:** no fuel, no moving parts, no sunlight required, works in eclipse, and it converts heat you must reject anyway.
**How useful:** 10 m² of radiator gives 10–50 W — enough for sensors, clocks, and standby radios on smallsats, not for propulsion. On Earth it needs a clear sky and only pays off where dumping heat is already the cost.
**Status:** wounded (diode quality below 0.2 eV is the binding constraint). Score 21/30. Confidence 55%.

---

## Vector 26: Anisotropic-Expansion Peristaltic Pump

**Falsification:** A laminated channel with 20 ppm/K CTE mismatch, cycled 30–100 °C at 1 Hz, must move ≥0.1 µL/min against 1 kPa. It dies below 10 nL/min or if flow reverses sign with drive phase.
**Mechanism:** Two bonded materials with different expansion coefficients bend a channel wall as temperature swings. A channel whose cross-section is asymmetric along its length squeezes in a travelling wave, so fluid is dragged one way. No valves, no membranes, no electricity.
**Magnitudes:** $\Delta\alpha\,\Delta T = 2\times10^{-6}\times100 = 2\times10^{-4}$ strain. A 50 µm channel wall deflects ~2 µm. Channel of 1 mm × 50 µm × 1 mm holds 50 nL; at 1 Hz with 10% net transport, 5 nL/s = 0.3 µL/min. Head 1–10 kPa.
**Example:** a sampling loop bolted to a hot machine housing that draws a few microlitres per minute into a test strip, with no battery.
**Pros:** no valves to clog, no seals, chemically inert if built from glass and metal, tolerant of dirty fluid, and the energy source is a temperature oscillation you already have.
**How useful:** point-of-care and field sampling where electricity is absent; also heat-driven dosing for lubrication and irrigation. Flow is microlitres, not litres — this is instrumentation, not plumbing.
**Status:** live on paper, wounded on fabrication (bonded laminate fatigue at 10⁶ cycles). Score 20/30. Confidence 45%.

---

## Vector 27: Ice-Bonded Reversible Joints

**Falsification:** A 100 cm² steel-to-concrete ice joint at −10 °C must hold ≥5 kN in shear and release in under 5 min. It dies below 1 kN or if release leaves bonded residue.
**Mechanism:** A thin water layer freezes between two surfaces and acts as the adhesive; a resistive film or a warm-water channel melts it on demand. The joint is a structural connection with no fasteners, no epoxy, and no torque specification.
**Magnitudes:** ice shear strength 0.5–1.5 MPa at −10 °C [UNVERIFIED] ⇒ 5–15 kN on 0.01 m². Melting a 5 mm layer takes 1.65 kJ/m²; at 13 kW/m² heat flux, 0.13 s of contact heating, so seconds in practice.
**Example:** temporary shoring and reusable formwork that is assembled wet, holds load while frozen, and releases without leaving anchors in the concrete.
**Pros:** works underwater and on wet surfaces (where adhesives fail), zero residue, fully reversible, materials cost near zero, and no skilled labour for the connection.
**How useful:** temporary structures, modular rigs, arctic and marine assembly, reusable molds. Limit: it only works below 0 °C, so it is a cold-climate and cryogenic tool, not a general fastener.
**Status:** live (mechanism is ordinary physics; the claim is the designed release path). Score 22/30. Confidence 60%.

---

## Vector 28: Capillary-Condensation Thermal Switches

**Falsification:** A 100 nm pore membrane spanning a 10 µm gap must change heat conductance by ≥10× between 80% and 98% RH. It dies below 3× or if the wet state does not recover after 1000 cycles.
**Mechanism:** At a fixed relative humidity, pores below the Kelvin radius fill with condensate. A filled gap conducts through water; a dry gap conducts through air. The switch is humidity, the actuator is capillary condensation, and there is nothing to power or sense.
**Magnitudes:** air in a 10 µm gap: $h = 0.026/10^{-6} = 2600\ \mathrm{W\,m^{-2}K^{-1}}$. Water-filled: $0.6/10^{-6} = 60{,}000$. Ratio 23×. Pore radius 50 nm closes at ~98% RH (Kelvin equation, $2\gamma V_m/rRT = 0.021$). Gap conductance 2600 → 60,000 W/m²K.
**Example:** an electronics enclosure that only dumps heat through the humid-air path when condensation is imminent, keeping the inside above dew point without a controller.
**Pros:** zero power, no sensor, no moving parts, fails safe, and it self-triggers at the condition it is protecting against.
**How useful:** outdoor cabinets, greenhouse glazing, camera housings, cold-climate battery boxes. The magnitude is real (23×) and the failure mode is graceful: if the pores foul, the switch stays partially closed.
**Status:** live. Score 22/30. Confidence 60%. Main risk: fouling and salt creep closing the pores permanently.

---

## Vector 29: Recoverable Prestress

**Falsification:** A 25 m³ precast element with 1% tendon volume, tensioned to 1000 MPa, must return ≥200 kJ through a hydraulic ram on release. It dies below 50 kJ or if the concrete crushes before the tendon work is recovered.
**Mechanism:** Prestress is stored elastic energy in the steel and the concrete. Standard practice throws it away on demolition. A sequenced release, tendon by tendon, into a ram captures it.
**Magnitudes:** $u = \sigma^2/2E = (10^9)^2/(2\times1.95\times10^{11}) = 2.56\ \mathrm{MJ\,m^{-3}}$ in steel. 0.25 m³ of tendon = 640 kJ; 60% recovery = 380 kJ = 0.1 kWh.
**Example:** modular precast slabs whose tendons are re-tensioned into the next structure instead of being cut and scrapped.
**Pros:** the energy was already paid for, no new material, no new process, and it converts a demolition hazard (stored energy released violently) into a controlled output.
**How useful:** 0.1 kWh per element is small against its 25 m³ of material, so the value is safety and material reuse, not energy. Worth it where tendons are cut anyway and the release must be controlled.
**Status:** wounded (energy density low; the real product is controlled demolition). Score 17/30. Confidence 50%.

---

## Killed in this pass

| Candidate | Why it died |
| --- | --- |
| Ferrofluid pressure intensifier | Saturation magnetisation caps magnetic pressure at ~1 kPa — three orders short |
| Mechanochemical hydrogen compressor | Reaching 700 bar needs 9.5 GPa of hydrostatic stress |
| Regelation (pressure-melting) thermal valve | 1 K shift needs 135 atm; a thermostat that costs more than it saves |
| Ortho/para hydrogen storage | Merges with Vector 20 on four axes |
| Phononic Thouless pump | Merges with Vector 11 (phase-front timekeeping) |
| Passive electret levitation | Earnshaw's theorem — dead on symmetry, not on engineering |
| Streaming-potential 100 kV source | Needs a 1.4 GPa water head |
| Granular cyclic-shear memory | Published; nothing left to claim |
