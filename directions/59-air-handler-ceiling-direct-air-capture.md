# Vector 59: The Air-Handler Ceiling on Direct Air Capture

**Status:** live
**Confidence:** 72%, basis: the fan work is $V\Delta p/\eta$ with $V = 1.31\times10^{6}\ \mathrm{m^3}$ of air per tonne of CO2 and no free parameter except the pressure drop, and the reversible separation work is a fixed $0.44\ \mathrm{GJ/t}$ from the 420 ppm mixing ratio; the two numbers are within $1.3\times$ of each other, so the comparison holds for any contactor in the $100$ to $500\ \mathrm{Pa}$ range. The uncertainty is in the amine coating thickness and the number of passes, not in the comparison.

## 1. Name

The Air-Handler Ceiling on Direct Air Capture (the observation that at 420 ppm the fans cost more than the reversible separation work, and the laminar-channel contactor that removes the ceiling)

## 2. Fundamental problem

Remove one tonne of CO2 from air at 420 ppm using a sorbent, and do it with the least energy. The stripped requirement is a separation that works from a $6.4\times10^{-4}$ mass fraction, on a gas that arrives at ambient pressure and must be moved through the device.

The separation itself is cheap: $0.44\ \mathrm{GJ/t}$ of reversible work. If the plant cannot get within $3\times$ of that, the obstacle is somewhere else, and the obstacle is moving the air.

## 3. Falsification statement

A $0.5\ \mathrm{m^2}$ face contactor of $2.3\ \mathrm{mm}$ parallel channels, $0.3\ \mathrm{m}$ deep, walls washcoated with $60\ \mathrm{g/m^2}$ of a supported amine, is run on ambient air at $1.0 \pm 0.1\ \mathrm{m/s}$ face velocity and $20 \pm 3\ ^\circ\mathrm{C}$:

1. The pressure drop is $\le 20\ \mathrm{Pa}$ at $1.0\ \mathrm{m/s}$ (Reynolds number $305$ on the hydraulic diameter $2d$).
2. The single-pass CO2 removal is $\ge 20\%$ at $0.3\ \mathrm{s}$ residence, measured by two nondispersive infrared analysers upstream and downstream.
3. The sorbent captures $\ge 1.0\ \mathrm{mmol/g}$ and releases it at $80$ to $100\ ^\circ\mathrm{C}$ with $\le 2.5\ \mathrm{GJ/t}$ of heat.
4. The fan work per tonne is $\le 0.15\ \mathrm{GJ/t}$ computed from (1) and (2).

The hypothesis is killed if the pressure drop at $1.0\ \mathrm{m/s}$ exceeds $50\ \mathrm{Pa}$ with the sorbent applied, because the wallcoating then adds more resistance than the clean channel and the $25\times$ saving collapses to $6\times$. A second kill is a single-pass removal below $10\%$, which forces more than eight passes and puts the fan back above $0.2\ \mathrm{GJ/t}$.

## 4. Hypothesis

At 420 ppm, one tonne of CO2 is carried by $1.31\times10^{6}\ \mathrm{m^3}$ of air, and moving that volume through a packed contactor at $300\ \mathrm{Pa}$ costs $0.56\ \mathrm{GJ}$ of fan work, which is $1.3\times$ the $0.44\ \mathrm{GJ}$ of reversible separation work at the same concentration. The fan is therefore not a parasitic load on the chemistry: it is larger than the chemistry's thermodynamic floor, and it is the number that decides whether a plant can ever reach $1\ \mathrm{GJ/t}$. A contactor of straight $2.3\ \mathrm{mm}$ channels at $12\ \mathrm{Pa}$ drops the fan to $0.09\ \mathrm{GJ/t}$ at four passes, which is below the separation work and below $1\%$ of a present plant's total energy, so the regeneration heat becomes the only entry that matters.

## 5. Why convention is insufficient here

Direct air capture is argued as a sorbent problem. The published comparisons are between amine-grafted silica, amine-functionalised polymers, moisture-swing ion-exchange resins, and Ca(OH)2 loops, and the metric is the regeneration enthalpy per mole of CO2. That comparison is real but it is not the binding one at 420 ppm, because the air is 2,500 times more dilute than a flue gas and the volume per tonne is 2,500 times larger.

At a power plant the CO2 is 10 to 15 percent, so one tonne is $5\times10^{3}\ \mathrm{m^3}$ and the fan is $0.002\ \mathrm{GJ/t}$, which is why flue-gas capture is correctly treated as a chemistry and heat problem. The same arithmetic at 420 ppm gives $1.31\times10^{6}\ \mathrm{m^3}$ and a fan of $0.2$ to $0.6\ \mathrm{GJ/t}$, and the entire literature scales the flue-gas intuition without re-running the volume.

The second convention is the contactor geometry. Structured packings and honeycombs are chosen for surface area per volume, which favours small channels, and small channels raise the pressure drop as $1/d^{2}$ in the laminar regime. The two objectives pull against each other, and the usual resolution, a $1$ to $2\ \mathrm{mm}$ pitch, sits at $100$ to $300\ \mathrm{Pa}$. A parallel-plate stack at $2.3\ \mathrm{mm}$ with a $0.3\ \mathrm{m}$ depth sits at $12\ \mathrm{Pa}$ for the same surface area, because the surface-to-volume ratio of parallel plates is $4/d$ and the hydraulic diameter is $2d$, so the pressure drop for a fixed area falls as $d^{3}$ while the area falls only as $d$.

## 6. Mechanism

* $x$: CO2 mole fraction ($4.20\times10^{-4}$). [established]
* $M_{CO2}$: molar mass ($0.044\ \mathrm{kg/mol}$). [established]
* $M_{air}$: molar mass ($0.029\ \mathrm{kg/mol}$). [established]
* $\rho_{air}$: density ($1.20\ \mathrm{kg/m^3}$ at $20\ ^\circ\mathrm{C}$). [established]
* $c_m$: CO2 mass concentration ($7.65\times10^{-4}\ \mathrm{kg/m^3}$). [hypothesized, derived]
* $V_t$: air volume per tonne ($1.31\times10^{6}\ \mathrm{m^3}$). [hypothesized, derived]
* $W_{min}$: reversible separation work ($0.44\ \mathrm{GJ/t}$). [established]
* $\Delta p$: contactor pressure drop ($300\ \mathrm{Pa}$ conventional, $12\ \mathrm{Pa}$ laminar). [assumed]
* $\eta$: fan efficiency ($0.70$). [assumed]
* $\mu$: air viscosity ($1.81\times10^{-5}\ \mathrm{Pa\,s}$). [established]
* $d$: channel spacing ($2.3\ \mathrm{mm}$). [assumed]
* $L$: channel depth ($0.30\ \mathrm{m}$). [assumed]
* $v$: face velocity ($1.0\ \mathrm{m/s}$). [assumed]
* $N$: passes over the sorbent ($4$). [hypothesized]
* $q_s$: sorbent capacity ($1.0\ \mathrm{mmol/g} = 0.044\ \mathrm{kg/kg}$). [assumed]
* $\Delta H_{reg}$: regeneration heat ($2.0\ \mathrm{GJ/t}$). [assumed, range $1.5$ to $2.5$]
* $A_f$: face area per tonne per day ($61\ \mathrm{m^2}$). [hypothesized, derived]

1. Air at 420 ppm carries $7.65\times10^{-4}\ \mathrm{kg}$ of CO2 per cubic metre. A tonne therefore needs $1.31\times10^{6}\ \mathrm{m^3}$ of air, which is the volume of a $110\ \mathrm{m}$ cube for every tonne.
2. A packed contactor at $300\ \mathrm{Pa}$ moves that volume for $0.56\ \mathrm{GJ}$. The reversible separation work from 420 ppm to 1 bar is $0.44\ \mathrm{GJ}$. The fan is already larger than the floor.
3. A parallel-plate stack with $2.3\ \mathrm{mm}$ spacing has a hydraulic diameter of $2d = 4.6\ \mathrm{mm}$, a Reynolds number of $153$ at $1\ \mathrm{m/s}$, and a Darcy pressure drop of $12\ \mathrm{Pa}$ over $0.3\ \mathrm{m}$.
4. The $0.3\ \mathrm{m}$ depth gives $0.3\ \mathrm{s}$ of residence, which is about one quarter of the contact time a supported amine needs for $50\%$ removal, so the air passes four times and the fan is $0.09\ \mathrm{GJ}$ per tonne.
5. The face area for one tonne per day is $61\ \mathrm{m^2}$ at $1\ \mathrm{m/s}$, in a bed of $18\ \mathrm{m^3}$. Parallel plates at $2.3\ \mathrm{mm}$ give $1.74\times10^{3}\ \mathrm{m^2}$ of wall per cubic metre, so the bed holds $3.2\times10^{4}\ \mathrm{m^2}$ of sorbent surface.
6. At $60\ \mathrm{g/m^2}$ that is $1.9\ \mathrm{t}$ of amine, which at $1.0\ \mathrm{mmol/g}$ captures $84\ \mathrm{kg}$ per two-hour cycle, or $1.0\ \mathrm{t/day}$. The inventory closes on itself, which is the check that the geometry is not arbitrary.
7. The regeneration heat at $2.0\ \mathrm{GJ/t}$ is then $95\%$ of the plant's energy and the fan is $4\%$. The ceiling has moved from the air to the sorbent, which is where the chemistry literature already is.
8. A present plant at $7$ to $10\ \mathrm{GJ/t}$ spends $0.2$ to $0.4\ \mathrm{GWh}$ per tonne on electricity, of which the fans are $40$ to $70\%$. Removing that load is a $3\times$ cut in total energy with no change to the sorbent.

## 7. Mathematical model

CO2 concentration from the mixing ratio:

$$c_m = x\,\frac{M_{CO2}}{M_{air}}\,\rho_{air} = 4.20\times10^{-4}\left(\frac{0.044}{0.029}\right)(1.20) = 7.65\times10^{-4}\ \mathrm{kg/m^3}$$

* $[x][M/M][\rho] = (\text{mol/mol})(\text{kg/mol}/\text{kg/mol})(\mathrm{kg/m^3}) = \mathrm{kg/m^3}$. Check passes.

Air volume per tonne:

$$V_t = \frac{10^{3}}{7.65\times10^{-4}} = 1.31\times10^{6}\ \mathrm{m^3}$$

Reversible separation work, ideal mixture, capture to 1 bar:

$$W_{min} = \frac{RT}{M_{CO2}}\ln\frac{1}{x} = \frac{(8.314)(293)}{0.044}\ln\frac{1}{4.20\times10^{-4}} = \frac{2436}{0.044}(7.78) = 4.3\times10^{5}\ \mathrm{J/kg} = 0.43\ \mathrm{GJ/t}$$

* $[(J/(mol\,K))(K)/(kg/mol)] = \mathrm{J/kg}$. Check passes.
* At 1 bar and $20\ ^\circ\mathrm{C}$, $0.43\ \mathrm{GJ/t}$ is $120\ \mathrm{kWh/t}$.

Fan work:

$$W_{fan} = \frac{V_t\,\Delta p}{\eta} = \frac{1.31\times10^{6}(300)}{0.70} = 5.6\times10^{8}\ \mathrm{J} = 0.56\ \mathrm{GJ/t}$$

* $[\mathrm{m^3}][\mathrm{Pa}] = \mathrm{J}$. Check passes.
* At $100\ \mathrm{Pa}$: $0.19\ \mathrm{GJ/t}$. At $500\ \mathrm{Pa}$: $0.94\ \mathrm{GJ/t}$.
* Ratio to the separation floor: $0.56/0.43 = 1.30$.

Laminar pressure drop in a parallel-plate channel:

$$\Delta p = \frac{12\mu L v}{d^{2}} = \frac{12(1.81\times10^{-5})(0.30)(1.0)}{(2.3\times10^{-3})^{2}} = 12.3\ \mathrm{Pa}$$

* $[\mathrm{Pa\,s}][\mathrm{m}][\mathrm{m/s}]/\mathrm{m^2} = \mathrm{Pa}$. Check passes.
* Reynolds number $Re = \rho v (2d)/\mu = (1.20)(1.0)(4.6\times10^{-3})/(1.81\times10^{-5}) = 305$, below the $2\,300$ transition, so the laminar form is valid. The factor $12$ is for a slit, and the hydraulic diameter used in $Re$ is $2d$, which is the convention that makes the two consistent.

Fan with four passes:

$$W_{fan,4} = \frac{4(1.31\times10^{6})(12.3)}{0.70} = 9.2\times10^{7}\ \mathrm{J} = 0.09\ \mathrm{GJ/t}$$

Face area for one tonne per day:

$$A_f = \frac{N V_t}{v\,t_{day}} = \frac{4(1.31\times10^{6})}{(1.0)(86\,400)} = 61\ \mathrm{m^2}$$

* $[\mathrm{m^3}]/[\mathrm{m/s}][\mathrm{s}] = \mathrm{m^2}$. Check passes.

Sorbent inventory closure:

$$m_{sorb} = \frac{10^{3}}{q_s\,n_{cycles}} = \frac{10^{3}}{(0.044)(12)} = 1.9\times10^{3}\ \mathrm{kg}$$

* Twelve two-hour cycles per day, $0.044\ \mathrm{kg}$ CO2 per kg sorbent per cycle. Check passes.
* The bed surface $3.2\times10^{4}\ \mathrm{m^2}$ at $60\ \mathrm{g/m^2}$ gives $1.9\ \mathrm{t}$, which is the same number from two directions.

## 8. Physical constraints

* The laminar form holds to $Re \approx 2\,300$, which at $2.3\ \mathrm{mm}$ spacing is $7.5\ \mathrm{m/s}$. Above that the pressure drop rises as $v^{1.8}$ and the $\times25$ advantage narrows to $\times8$.
* The surface-to-volume ratio of parallel plates is $4/d$, so doubling the spacing halves the sorbent area and halves the sorbent mass per cubic metre. The $2.3\ \mathrm{mm}$ choice is a compromise between area and pressure drop, not an optimum: the pressure drop falls as $d^{-2}$ in the slit formula for fixed $L$ and $v$, but the area and the capture per pass also fall, so the real trade is $d$ against residence time.
* The $0.3\ \mathrm{s}$ residence is below the $1$ to $2\ \mathrm{s}$ that a supported amine needs for $50\%$ capture. Four passes buy the contact time at the cost of four times the fan work, which is why the design is stated at $0.09$ and not at $0.02\ \mathrm{GJ/t}$.
* Water co-adsorption on an amine is $1$ to $5\ \mathrm{kg}$ per kg CO2 at $50\%$ relative humidity, and that water must be desorbed before the CO2. The heat is not free, and it can exceed the CO2 desorption enthalpy. This is the reason field plants use a dry sorbent or a water-tolerant one, and it is not addressed by the contactor.
* Dust at $20\ \mu\mathrm{g/m^3}$ deposits $26\ \mathrm{g}$ per tonne of CO2 in the front layer. Over a year at one tonne per day that is $9.6\ \mathrm{kg}$, which is small in mass and large in effect: a $10\ \mu\mathrm{m}$ dust layer on a $2.3\ \mathrm{mm}$ channel is $0.4\%$ of the gap and adds little pressure, but it blinds the sorbent behind it.
* The bed must be regenerated in place, so the $18\ \mathrm{m^3}$ is also a $100\ ^\circ\mathrm{C}$ vessel with thermal mass. At $2\ \mathrm{kg}$ of steel per kg of sorbent, $0.5\ \mathrm{kJ/(kg\,K)}$ and $80\ \mathrm{K}$, the sensible load is $1.8\ \mathrm{GJ/t}$, which is the same size as the desorption enthalpy itself. That is not a small correction: it is why real plants recover heat between cycles, and it means the contactor and the regenerator must be designed together or the $3\times$ saving is eaten by the vessel.

## 9. Contradiction ledger

1. **The fan is not the largest cost today.** Regeneration heat at $1.5$ to $2.5\ \mathrm{GJ/t}$ is $20$ to $35\%$ of a $7\ \mathrm{GJ}$ plant, and the fans are $5$ to $10\%$. The claim is about the floor, not about today's bill: at any sorbent below $0.5\ \mathrm{GJ/t}$ of regeneration heat, the fan becomes the binding term. Stated as a ceiling, it is correct; stated as a today's-cost claim, it would be wrong.
2. **The comparison uses a reversible floor for an irreversible device.** $0.43\ \mathrm{GJ/t}$ is the work of an isothermal reversible separation, and no amine process is reversible. The fan is compared against the floor only to show that the two are the same order, which is the point: an engineering loss of the size of the theoretical minimum is the binding constraint.
3. **The laminar advantage depends on the sorbent surviving a thin coating.** At $60\ \mathrm{g/m^2}$ on a $2.3\ \mathrm{mm}$ plate, the coating is about $60\ \mu\mathrm{m}$ thick at unit density, which is $2.6\%$ of the gap and adds $2.6\%$ to the pressure drop, not $50$. If the coating swells with water it can close the gap, and that is the real kill test.
4. **Four passes is a guess.** It assumes $25\%$ removal per $0.3\ \mathrm{s}$, which is $k = 0.96\ \mathrm{s^{-1}}$. Published amine kinetics at 420 ppm span $0.2$ to $2\ \mathrm{s^{-1}}$ depending on loading and humidity, so the pass count is $2$ to $10$ and the fan is $0.05$ to $0.23\ \mathrm{GJ/t}$. The conclusion survives the whole range.
5. **The dust result is a mass number, not a mass-transfer number.** $26\ \mathrm{g}$ per tonne sounds trivial, and it is; the damage is in surface coverage, which is not calculable from the mass without a particle size distribution.
6. **Triviality check.** Low-pressure-drop DAC contactors exist and are sold. What is not in the literature, as far as first-principles accounting can tell, is the sentence: the fan work at 420 ppm is $1.3\times$ the reversible separation work, so the concentration itself sets an energy floor that sorbent chemistry cannot cross. The device is a known geometry; the ceiling is the result.
7. **The $1\ \mathrm{GJ/t}$ figure is a floor for the separation only.** A plant that reaches it still has to pay for compression to $100\ \mathrm{bar}$ if the CO2 is to be stored, which is $0.3$ to $0.4\ \mathrm{GJ/t}$, and for the sensible heat of its own hardware. The floor of the whole chain is $1.4$ to $1.6\ \mathrm{GJ/t}$, not $1.0$.

## 10. Experiment

Contactor: $0.5\ \mathrm{m^2}$ face, $2.3\ \mathrm{mm}$ parallel polypropylene plates at $0.3\ \mathrm{m}$ depth, $61$ plates, assembled in a $0.71\ \mathrm{m}$ square frame with a $0.1\ \mathrm{m}$ inlet plenum and a $0.1\ \mathrm{m}$ outlet plenum. Washcoat: $60\ \mathrm{g/m^2}$ of a commercial supported amine (polyethyleneimine on fumed silica, $1.0\ \mathrm{mmol/g}$) in a $5\ \mathrm{wt\%}$ methanol slurry, dried at $60\ ^\circ\mathrm{C}$, weighed before and after.

Air: a $0.75\ \mathrm{kW}$ centrifugal blower through a variable-frequency drive, $0.5$ to $1.5\ \mathrm{m/s}$ face velocity, ambient air at $20 \pm 3\ ^\circ\mathrm{C}$ and $40$ to $60\%$ relative humidity. Pressure drop by a $0$ to $100\ \mathrm{Pa}$ differential transducer at $0.25\%$ full scale, with $10\ \mathrm{mm}$ static taps in the two plenums. CO2 by two nondispersive infrared analysers, $0$ to $2\,000\ \mathrm{ppm}$, $\pm 2\%$ of reading, one upstream and one downstream, cross-checked by swapping them at the start and end of every run.

Desorption: the stack is enclosed in a $0.2\ \mathrm{mm}$ stainless box, purged with $1\ \mathrm{L/min}$ of nitrogen, heated at $2\ \mathrm{K/min}$ to $100\ ^\circ\mathrm{C}$ with four $100\ \mathrm{W}$ cartridge heaters, and the CO2 released is integrated on the downstream analyser. The heat is metered at the heater terminals, corrected for the box loss by a blank run.

Controls: an empty frame of the same dimensions (pressure drop), the same stack with no amine (uptake), and the same stack run at $0\ ^\circ\mathrm{C}$ dew point (water co-adsorption).

Null result: pressure drop above $50\ \mathrm{Pa}$ at $1\ \mathrm{m/s}$ with the coating applied, or single-pass removal below $10\%$, or a regeneration heat above $3.0\ \mathrm{GJ/t}$.

What the experiment cannot distinguish: it cannot separate the coating's hydraulic resistance from the plate edge effects at $0.5\ \mathrm{m^2}$ scale, so the pressure result is a lower bound on a full-size module; and it cannot measure the $10$-year coating life, which is the number that decides whether the $60\ \mathrm{g/m^2}$ survives thermal cycling.

## 11. Expected observations

Success branch: pressure drop $11$ to $18\ \mathrm{Pa}$ at $1.0\ \mathrm{m/s}$, single-pass removal $20$ to $28\%$ at $0.3\ \mathrm{s}$, capacity $0.9$ to $1.1\ \mathrm{mmol/g}$, regeneration heat $1.8$ to $2.4\ \mathrm{GJ/t}$, and a computed fan of $0.09$ to $0.13\ \mathrm{GJ/t}$ at four passes.

Failure branch: pressure drop $40$ to $80\ \mathrm{Pa}$, which is the signature of a swollen or uneven coating closing the gap; or single-pass removal below $10\%$, which is the signature of channeling at the plenum; or a capacity below $0.5\ \mathrm{mmol/g}$, which means the washcoat lost its amine in the slurry.

The decisive signature is the ratio of pressure drop with and without the coating. A ratio of $1.03$ confirms the coating is $60\ \mu\mathrm{m}$ and conformal; a ratio above $1.5$ means the coating is bridging the plates and the geometry is not what the model assumes.

## 12. Magnitudes

| Quantity | Value | Basis |
| :--- | :--- | :--- |
| CO2 concentration, 420 ppm | $7.65\times10^{-4}\ \mathrm{kg/m^3}$ | mixing ratio |
| Air per tonne of CO2 | $1.31\times10^{6}\ \mathrm{m^3}$ | derived |
| Reversible separation work | $0.43\ \mathrm{GJ/t}$ | $RT\ln(1/x)$ |
| Fan work at $300\ \mathrm{Pa}$ | $0.56\ \mathrm{GJ/t}$ | $V\Delta p/\eta$ |
| Fan work at $100\ \mathrm{Pa}$ | $0.19\ \mathrm{GJ/t}$ | same |
| Fan work at $500\ \mathrm{Pa}$ | $0.94\ \mathrm{GJ/t}$ | same |
| Fan / separation floor at $300\ \mathrm{Pa}$ | $1.30$ | ratio |
| Laminar pressure drop, $2.3\ \mathrm{mm}$, $0.3\ \mathrm{m}$ | $12.3\ \mathrm{Pa}$ | slit formula |
| Reynolds number at $1\ \mathrm{m/s}$ | $305$ | laminar |
| Fan work, four passes | $0.09\ \mathrm{GJ/t}$ | derived |
| Face area per tonne per day | $61\ \mathrm{m^2}$ | derived |
| Bed volume | $18\ \mathrm{m^3}$ | derived |
| Sorbent surface in the bed | $3.2\times10^{4}\ \mathrm{m^2}$ | $4/d$ |
| Amine inventory | $1.9\ \mathrm{t}$ | $60\ \mathrm{g/m^2}$ |
| Sorbent capacity | $1.0\ \mathrm{mmol/g}$ | assumed |
| Regeneration heat | $2.0\ \mathrm{GJ/t}$ | $1.5$ to $2.5$ |
| Present plant total energy | $7$ to $10\ \mathrm{GJ/t}$ | $2\,000$ to $2\,800\ \mathrm{kWh/t}$ |
| Compressor to 100 bar | $0.3$ to $0.4\ \mathrm{GJ/t}$ | isothermal, $60\%$ |
| Dust deposit | $26\ \mathrm{g/t}$ | $20\ \mu\mathrm{g/m^3}$ |

## 13. Applications

* **Contactor retrofit.** A $3\times$ cut in plant electricity with the same sorbent, which is the fastest route to a lower capture cost because the biggest single line item is the electric load and the fans are half of it.
* **Passive and wind-driven contactors.** At $12\ \mathrm{Pa}$ the driving pressure is inside the dynamic pressure of a $4.5\ \mathrm{m/s}$ wind, so a passive stack becomes possible without a fan at all; the design constraint moves to the sorbent's uptake rate, not the air supply.
* **Indoor air.** The same geometry at $1\,000$ to $2\,000\ \mathrm{ppm}$ needs $5\times$ less air per kilogram of CO2 and its fan is $0.002\ \mathrm{GJ/t}$, so a $2.3\ \mathrm{mm}$ stack is a room-scale scrubber with no ductwork.
* **Submarine and spacecraft life support.** The volume per kilogram is the same order as a plant, and the electric load is the scarce resource, so the laminar stack wins on the metric that matters there.
* **Flue gas, as a sanity check.** At $12\%$ CO2 the air handler is $0.002\ \mathrm{GJ/t}$ even at $300\ \mathrm{Pa}$, which reproduces the published result that flue-gas capture is a heat problem and confirms the model is not DAC-specific.

## 14. Unresolved questions

* Does a $60\ \mu\mathrm{m}$ amine washcoat survive $1\,000$ thermal cycles between $20$ and $100\ ^\circ\mathrm{C}$ without spalling? The whole $3\times$ claim depends on a coating that is $2.6\%$ of the channel gap and does not move.
* What is the real contactor pressure drop at $420\ \mathrm{ppm}$ with water co-adsorbing? A wet amine film can double the effective roughness, and no published number separates the wet and dry resistance.
* Can the $18\ \mathrm{m^3}$ bed be regenerated without heating its steel? At $2\ \mathrm{kg}$ of steel per kg of sorbent the sensible load is $1.8\ \mathrm{GJ/t}$, larger than the fan it is trying to save and the same size as the desorption enthalpy, so heat recovery between cycles is not an optimisation but a precondition for the $3\times$ claim.
* Is the $1.3\times$ ratio stable as the concentration falls? At $300\ \mathrm{ppm}$ the volume per tonne rises to $1.8\times10^{6}\ \mathrm{m^3}$ and the fan rises to $0.78\ \mathrm{GJ/t}$ against a floor of $0.46$, so the ceiling gets worse as the air gets cleaner, which is the wrong direction for a technology that must run for a century.
* Is a fan at $70\%$ efficiency realistic at $12\ \mathrm{Pa}$? Small blowers lose efficiency below $50\ \mathrm{Pa}$, and a $40\%$ efficient fan at $12\ \mathrm{Pa}$ doubles the fan work, still small but no longer negligible.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 5 | 4 | 4 | 4 | 4 |

Total: 24/30.
Confidence: 72%, basis: the fan work and the separation work are both closed-form and differ by $1.3\times$, so the comparison is arithmetic rather than an estimate; the $4$-pass and coating assumptions move the fan between $0.05$ and $0.23\ \mathrm{GJ/t}$, which does not change the conclusion.

## 16. Status

Live. The contactor is a known geometry; the result is the ceiling, not the hardware. Wounded on the assumption that the coating is hydraulically invisible, which is what the pressure-drop ratio in the falsification statement measures directly.
