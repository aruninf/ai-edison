# Vector 58: Thermo-Osmotic Liquid-State Drying

**Status:** live, wounded on the entropy of transfer
**Confidence:** 55%, basis: the linkage between the pressure head and the heat demand is an exact Carnot identity with no free parameter, so the two numbers cannot disagree; the single load-bearing unknown is the entropy of transfer for water in a hydrophobic nanopore, which spans 0.05 to 1.5 $k_B$ in principle, and the desalination corollary dies below 0.9 $k_B$ while the drying claim survives down to 0.2 $k_B$.

## 1. Name

The Thermo-Osmotic Liquid-State Drying Sheet (Removing Water from a Porous Solid as a Liquid at a 5 K Difference, With the Corollary That 13 K of Waste Heat Delivers the 55 bar That a Seawater Reverse-Osmosis Plant Needs)

## 2. Fundamental problem

Remove water from a wet solid without turning it into vapour. The stripped requirement is a mass flux of water out of a porous body at ambient pressure, with no air flow (no dust, no oxidation, no product entrainment), no compressor, no refrigerant, and no heat above $100\ ^\circ\mathrm{C}$.

Evaporation is the only route industry uses, and it charges the full $2.26\ \mathrm{MJ/kg}$. Any process that keeps the water liquid avoids that charge by construction. The question is whether a liquid-state process can have a driving force at all without a mechanical press, and what that force costs.

## 3. Falsification statement

A $25\ \mathrm{mm}$ disc of track-etched polycarbonate, $10\ \mu\mathrm{m}$ thick, $5\ \mathrm{nm}$ pore radius, $20\%$ porosity, made hydrophobic by a perfluorodecyltrichlorosilane monolayer (contact angle $110^\circ$), is clamped between two $10\ \mathrm{mL}$ water cells and pre-wetted by ethanol exchange. A Peltier holds one cell $5.0 \pm 0.1\ \mathrm{K}$ above the other. The pressure difference is read on a $0$ to $10\ \mathrm{bar}$ differential transducer with the far cell vented, and the crossover flow is read by weighing.

1. The thermo-osmotic head at $5.0\ \mathrm{K}$ is $\ge 5\ \mathrm{bar}$ (that is $\ge 1\ \mathrm{bar/K}$).
2. The head is linear in $\Delta T$ to $10\%$ over $2$ to $10\ \mathrm{K}$.
3. The head does not appear when the same stack is run with a $10\ \mu\mathrm{m}$ non-porous film, which is the artefact control.
4. With the membrane against a $10\ \mathrm{mm}$ saturated silanized alumina slab whose free face is sealed against evaporation, the slab loses $\ge 3\%$ of its water mass per day at $5.0\ \mathrm{K}$.

The hypothesis is killed if the head is below $1\ \mathrm{bar}$ at $5\ \mathrm{K}$ (below $0.2\ \mathrm{bar/K}$). At that coefficient, drying needs $100\ \mathrm{K}$ and desalination needs $135\ \mathrm{K}$, both outside any ambient source, and the device is a laboratory curiosity.

## 4. Hypothesis

Water confined in a hydrophobic nanopore has a different entropy from bulk water, because it makes fewer hydrogen bonds and keeps more translational freedom. That entropy difference, $\Delta s$ per molecule, does three things with one parameter: it generates a pressure head $\Delta p = (\Delta s/v_w)\Delta T$ across the membrane when a temperature difference is applied, it fixes the heat that each kilogram of transported water carries as $Q = T\Delta s/M_w$, and it fixes the work as $W = \Delta p/\rho$. Their ratio is exactly $\Delta T/T$, so the process is a Carnot-reversible heat engine and the second law decides both numbers at once. At $\Delta s = 0.9\ k_B$ the head is $4.16\ \mathrm{bar/K}$, so $5\ \mathrm{K}$ gives $21\ \mathrm{bar}$ and moves water as a liquid at $125\ \mathrm{kJ/kg}$ of ambient heat and $2.1\ \mathrm{kJ/kg}$ of work, which is $18\times$ below the latent heat. At $13\ \mathrm{K}$ the head is $54\ \mathrm{bar}$, which is the pressure a seawater reverse-osmosis train runs to produce flux against a $27\ \mathrm{bar}$ osmotic load. The water never enters the vapour phase, so the latent heat is never paid; the heat that is paid is low-grade heat that any $5\ \mathrm{K}$ ambient gradient supplies.

## 5. Why convention is insufficient here

Every industrial dryer converts water to vapour. A direct-fired rotary dryer pays $3$ to $6\ \mathrm{MJ/kg}$ of water. A heat-pump dryer with a $2.5$ coefficient of performance pays $1.2$ to $1.5\ \mathrm{MJ/kg}$ of electricity. Freeze drying pays $2.8\ \mathrm{MJ/kg}$ plus the vacuum load. The floor for all of them is the latent heat, and no amount of heat recovery removes it, because the water genuinely leaves as gas.

Mechanical dewatering does keep the water liquid, and it stops at $20$ to $30\%$ solids. A filter press or a decanter centrifuge cannot go further because the remaining water is held in pores smaller than the cake's own permeability and the hydraulic gradient becomes enormous. That is the gap this mechanism fills: the same liquid-state transport, driven by an entropy gradient instead of a pressure gradient, in pores a press cannot reach.

The membrane processes that do keep water liquid, reverse osmosis and forward osmosis, need $55$ to $70\ \mathrm{bar}$ of hardware for seawater, and $10$ to $30\ \mathrm{bar}$ even for brackish water. That is a pressure vessel, a high-pressure pump, and an energy-recovery turbine. A $6.5\ \mathrm{K}$ temperature difference generates the same $27\ \mathrm{bar}$ if the entropy of transfer is $0.9\ k_B$, and a $13\ \mathrm{K}$ difference generates the $54\ \mathrm{bar}$ that produces flux. The pump is replaced by a heat exchanger, which is a flat plate rather than a coded vessel.

## 6. Mechanism

* $\Delta s$: entropy of transfer of one water molecule from bulk liquid into the pore, $0.9\ k_B$. [hypothesized, the load-bearing number]
* $k_B$: Boltzmann constant ($1.381\times10^{-23}\ \mathrm{J/K}$). [established]
* $v_w$: molecular volume of liquid water ($2.99\times10^{-29}\ \mathrm{m^3}$). [established]
* $M_w$: molar mass of water ($0.018\ \mathrm{kg/mol}$). [established]
* $\rho$: density ($1000\ \mathrm{kg/m^3}$). [established]
* $T$: mean temperature ($300\ \mathrm{K}$). [assumed]
* $\Delta T$: applied difference ($5\ \mathrm{K}$ drying, $13\ \mathrm{K}$ desalination). [assumed]
* $\Delta H_{vap}$: latent heat of vaporization at $300\ \mathrm{K}$ ($2.26\ \mathrm{MJ/kg}$). [established]
* $r$: pore radius ($5\ \mathrm{nm}$). [assumed]
* $\varphi$: porosity ($0.20$). [assumed]
* $d$: membrane thickness ($10\ \mu\mathrm{m}$). [assumed]
* $\mu$: water viscosity ($1.0\ \mathrm{mPa\,s}$ at $300\ \mathrm{K}$). [established]
* $b$: slip length on a hydrophobic wall ($20\ \mathrm{nm}$). [hypothesized, range $5$ to $50\ \mathrm{nm}$]
* $k_{eff}$: effective conductivity of the wetted sheet ($0.28\ \mathrm{W/(m\,K)}$). [assumed]
* $q$: available heat flux ($1\ \mathrm{kW/m^2}$). [assumed]
* $J$: water mass flux per unit area. [hypothesized, derived]
* $\theta$: contact angle of the pore wall ($110^\circ$). [assumed]
* $\gamma$: surface tension ($0.072\ \mathrm{N/m}$). [established]
* $P_{entry}$: capillary entry pressure of a dry pore. [hypothesized, derived]

1. The sheet is wetted by ethanol exchange and kept full. Its pore walls are hydrophobic, so the water in the pore has lost roughly one hydrogen bond per molecule relative to bulk, which is the origin of $\Delta s$.
2. A $5\ \mathrm{K}$ difference is applied. The pore water at the warm face has chemical potential $\mu = \mu_0 - T\Delta s$, so raising $T$ lowers it further and the water prefers the pore. The result is a pressure difference across the sheet of $\Delta p = (\Delta s/v_w)\Delta T = 4.16\ \mathrm{bar/K} \times 5\ \mathrm{K} = 20.8\ \mathrm{bar}$.
3. That head is $212\ \mathrm{m}$ of water column. It is not a pump on the water; it is a pump on the chemical potential, and it exists with no moving part, no rotor, and no seal.
4. Water crosses the sheet. Each kilogram carries $Q = T\Delta s/M_w = 125\ \mathrm{kJ}$ of heat from the warm face to the cold face, which is $18\times$ below the $2.26\ \mathrm{MJ}$ that evaporation would charge.
5. For drying, the wet solid is the cold side: the water leaves the solid as liquid, crosses the sheet, and is drained from the warm side into a sump. The solid's own pore water never becomes vapour, so the solid does not lose its structure to a receding meniscus front.
6. For desalination, the head must exceed the osmotic pressure. At $27\ \mathrm{bar}$ the required $\Delta T$ is $6.5\ \mathrm{K}$ at zero flux; at the $54\ \mathrm{bar}$ that a real train runs, it is $13\ \mathrm{K}$.
7. Salt is excluded from the pore by the dielectric barrier. The Born energy of a sodium ion in a pore of dielectric constant $2$ against water's $80$ is $135\ kT$ at $300\ \mathrm{K}$, so the ion concentration inside the pore is lower than outside by $\mathrm{e}^{-135}$.
8. The rate is set by the heat flux, not by the pore permeability. At $1\ \mathrm{kW/m^2}$ the sheet moves $q/Q = 29\ \mathrm{kg/m^2\,h}$, and the viscous resistance of the pores is two orders below that limit.

## 7. Mathematical model

Thermo-osmotic pressure from the entropy of transfer:

$$\Delta p = \frac{\Delta s}{v_w}\,\Delta T, \qquad \frac{\Delta p}{\Delta T} = \frac{0.9(1.381\times10^{-23})}{2.99\times10^{-29}} = 4.16\times10^{5}\ \mathrm{Pa/K}$$

* $[\Delta s/v_w] = (\mathrm{J/K})/\mathrm{m^3} = \mathrm{Pa/K}$. Check passes.
* $5\ \mathrm{K}$ gives $2.08\ \mathrm{MPa}$; $13\ \mathrm{K}$ gives $5.41\ \mathrm{MPa}$.

Heat carried per unit mass, from the same parameter:

$$Q = \frac{T\,\Delta s\,N_A}{M_w} = \frac{300(0.9)(1.381\times10^{-23})(6.022\times10^{23})}{0.018} = 1.25\times10^{5}\ \mathrm{J/kg}$$

* $[T\Delta s N_A/M_w] = \mathrm{J/mol}/(\mathrm{kg/mol}) = \mathrm{J/kg}$. Check passes.
* Ratio to latent heat: $2.26\times10^{6}/1.25\times10^{5} = 18.1$.

Work per unit mass and the Carnot identity:

$$W = \frac{\Delta p}{\rho} = \frac{2.08\times10^{6}}{1000} = 2.08\times10^{3}\ \mathrm{J/kg}, \qquad \frac{W}{Q} = \frac{2.08\times10^{3}}{1.25\times10^{5}} = 1.66\times10^{-2} = \frac{5}{300}$$

* The ratio equals $\Delta T/T$ exactly, so the model saturates the Carnot bound and no efficiency term is available to hide an error. This is the reason the two numbers are trusted together: they are one number.

Heat-limited flux:

$$J = \frac{q}{Q} = \frac{1.0\times10^{3}}{1.25\times10^{5}} = 8.0\times10^{-3}\ \mathrm{kg/(m^2\,s)} = 29\ \mathrm{kg/(m^2\,h)}$$

* $[\mathrm{W/m^2}]/[\mathrm{J/kg}] = \mathrm{kg/(m^2\,s)}$. Check passes.

Viscous ceiling, Hagen-Poiseuille with slip:

$$J_{visc} = \rho\varphi\frac{r^2}{8\mu}\left(1+\frac{4b}{r}\right)\frac{\Delta p}{d}$$

* $r^2/8\mu = 2.5\times10^{-17}/8.0\times10^{-3} = 3.1\times10^{-15}\ \mathrm{m^3/(N\,s)}$.
* $(1+4b/r) = 1+16 = 17$.
* $\Delta p/d = 2.08\times10^{6}/1.0\times10^{-5} = 2.08\times10^{11}\ \mathrm{Pa/m}$.
* $J_{visc} = 1000(0.20)(3.1\times10^{-15})(17)(2.08\times10^{11}) = 2.2\ \mathrm{kg/(m^2\,s)}$.
* The heat limit is $8.0\times10^{-3}$, which is $275\times$ below the viscous ceiling, so the sheet is thermally limited and the pore geometry is not the constraint.

Capillary entry pressure of a dry pore:

$$P_{entry} = -\frac{2\gamma\cos\theta}{r} = \frac{2(0.072)(0.34)}{5\times10^{-9}} = 9.8\times10^{6}\ \mathrm{Pa}$$

* The negative sign is the reason the sheet must be pre-wetted: a dry start needs $98\ \mathrm{bar}$, which is $5\times$ the available head. Ethanol exchange wets it at $0.03\ \mathrm{bar}$.

Net driving pressure for desalination at $13\ \mathrm{K}$:

$$\Delta p_{net} = 54.1 - 27 = 27.1\ \mathrm{bar}$$

* A real reverse-osmosis train runs at $55$ to $70\ \mathrm{bar}$ against the same osmotic load, so the second term of this device reproduces the operating pressure with heat instead of a pump.

## 8. Physical constraints

* $\Delta s$ is capped near $2\ k_B$ by the number of hydrogen bonds a water molecule can lose (one bond is about $0.2\ \mathrm{eV} = 4.6\ k_B$, and only a fraction of that is recovered as translational entropy). Above that, the pore water is not water.
* $\Delta s$ is zero on a hydrophilic wall and negative if the wall orders the water. This is why wood, clay, and concrete do not dry by this mechanism at an observable rate: their pores are hydrophilic, their $\Delta s$ is near zero, and the null result is the reason the effect was never noticed in those materials.
* The sheet must stay wetted. If a pore dries, the entry barrier is $98\ \mathrm{bar}$ and the device is dead until it is re-primed.
* The head is independent of pore radius while the flux scales as $r^2$, so the pore size is a throughput choice and not a strength choice. This is a testable signature, not an assumption.
* The sheet is pressure-balanced, because both faces sit at the same pressure, so the $21\ \mathrm{bar}$ appears across the pore rims and at the perimeter clamp rather than as a tensile load on the sheet. The clamp is the only structural seal and is specified at $0.2\ \mathrm{MPa}$.
* Dissolved air comes out of solution on the warm face, because air solubility in water falls about $2\%$ per kelvin. At $5\ \mathrm{K}$ the release is $10\%$ of the dissolved gas, and a bubble blocks a pore permanently. Degassing the feed is mandatory and is not free.

## 9. Contradiction ledger

1. **The sign of $\Delta s$ is not established.** A hydrophobic pore raises the entropy of confined water, which drives flow from cold to hot. A hydrophilic pore reverses it. The design inverts if the sign is the other way, and the experiment measures the sign rather than assuming it. The magnitude claim is unaffected.
2. **The desalination corollary has a threshold.** At $\Delta s = 0.9\ k_B$ the $6.5\ \mathrm{K}$ match is arithmetic. At $0.5\ k_B$ the same $27\ \mathrm{bar}$ needs $11.7\ \mathrm{K}$ and the $54\ \mathrm{bar}$ operating point needs $23\ \mathrm{K}$, which is still available from industrial waste heat but not from ambient air. At $0.2\ k_B$ it needs $58\ \mathrm{K}$ and the corollary is dead while drying survives.
3. **Only free water wins.** Bound water in a gel or a food matrix costs its binding enthalpy to release, $0.5$ to $2\ \mathrm{MJ/kg}$, which is the same order as the latent heat. The $18\times$ claim is for water held in pores larger than about $100\ \mathrm{nm}$, which is sludge, filter cake, sand, timber free water, and brine. It is not a food-dehydration claim, and the applications section says so.
4. **Salt rejection is asserted, not measured.** The $135\ kT$ Born barrier is an electrostatic estimate for a cylindrical pore with a step dielectric profile. Real pores have a wall layer, adsorbed organics, and a Debye length of $1\ \mathrm{nm}$ at seawater strength, and the rejection can fall below $95\%$. A rejection of $95\%$ doubles the brine concentration at the wall through concentration polarisation and subtracts about $1.4\ \mathrm{bar}$ from the net driving force, which is $5\%$ of the $27\ \mathrm{bar}$ overpressure. Tolerable, but it must be measured.
5. **The conduction short-circuit is real.** The wetted sheet conducts $k_{eff}\Delta T/d = 0.28(5)/10^{-5} = 1.4\times10^{5}\ \mathrm{W/m^2}$, which is $140\times$ the $1\ \mathrm{kW/m^2}$ that the water flux needs. The excess heat is not a loss in energy terms because it is ambient heat crossing a $5\ \mathrm{K}$ difference, but it is a loss in exergy and it sets the heat-exchanger size. The mitigation is to make the thermal path longer than the flow path, which the $10\ \mu\mathrm{m}$ sheet does not do. A $1\ \mathrm{mm}$ path with lateral flow would cut the short-circuit $100\times$ and is the second-generation geometry.
6. **The 6.5 K number is a limit, not a flow.** At exactly the osmotic pressure the flux is zero, which is why the $13\ \mathrm{K}$ operating point is the honest one. Quoting $6.5\ \mathrm{K}$ alone would be the same error that gas-gap switch papers make when they quote the pressure ratio and omit the support.
7. **Triviality check.** Thermo-osmosis in capillaries was described in the nineteenth century (Clausius, Lippmann) and measured in the twentieth. What is new here is the operating point ($5$ to $13\ \mathrm{K}$ instead of tens of kelvin), the liquid-state drying application, and the observation that one parameter fixes both the head and the heat through the Carnot identity, so the device cannot be better than Carnot and does not need to be.
8. **The drying claim has no rate precedent.** Industrial dryers run at $1$ to $50\ \mathrm{kg/(m^2\,h)}$. The $29\ \mathrm{kg/(m^2\,h)}$ prediction sits inside that range, which means the device is not obviously better on rate, only on energy. A pilot that is slower than a belt dryer but uses $18\times$ less energy is a different product, not a drop-in replacement.

## 10. Experiment

Materials: track-etched polycarbonate, $10\ \mu\mathrm{m}$ thick, $5\ \mathrm{nm}$ pores, $20\%$ porosity, $25\ \mathrm{mm}$ disc. Silanize in $1\%$ perfluorodecyltrichlorosilane in toluene for $30\ \mathrm{min}$, cure at $100\ ^\circ\mathrm{C}$ for $1\ \mathrm{h}$, verify the contact angle at $110 \pm 3^\circ$ on a flat witness coupon. Wet by ethanol exchange: ethanol $30\ \mathrm{min}$, $50/50$ ethanol-water $30\ \mathrm{min}$, water $30\ \mathrm{min}$, then store under water.

Apparatus: two $10\ \mathrm{mL}$ polycarbonate cells with $6\ \mathrm{mm}$ bores, the sheet clamped between silicone gaskets at $0.2\ \mathrm{MPa}$, each cell with a $25\ \mu\mathrm{m}$ thermocouple within $2\ \mathrm{mm}$ of the sheet, one cell on a $40\ \mathrm{W}$ Peltier with a $0.1\ \mathrm{K}$ controller, the other on a $200\ \mathrm{g}$ aluminium block. Pressure read by a $0$ to $10\ \mathrm{bar}$ differential transducer (accuracy $0.25\%$ full scale) with the reference cell vented to atmosphere through a $0.2\ \mu\mathrm{m}$ filter. Flow read by weighing the reference cell on a $0.1\ \mathrm{mg}$ balance every $60\ \mathrm{s}$.

Controls, all in the same jig: (a) non-porous $10\ \mu\mathrm{m}$ polycarbonate film, same silanization, which isolates thermal-expansion and dissolved-gas artefacts; (b) the same sheet with a hydrophilic wall (oxygen plasma, contact angle $<20^\circ$), which should reverse or null the sign; (c) $\Delta T = 0$ with a $5\ \mathrm{K}$ absolute offset, which isolates a temperature-dependent seal leak.

Sequence: equilibrate $1\ \mathrm{h}$ at $\Delta T = 0$, ramp at $1\ \mathrm{K/min}$ to $+5\ \mathrm{K}$, hold $2\ \mathrm{h}$, record head and mass, then reverse, then repeat at $2$, $5$, $8$, $10\ \mathrm{K}$. Three sheets, three runs each.

Null result: head below $1\ \mathrm{bar}$ at $5\ \mathrm{K}$ on the hydrophobic sheet, or a head of the same size on the non-porous control, or a head that does not scale with $\Delta T$.

What the experiment cannot distinguish: it cannot separate the thermo-osmotic head from a thermoelectric (Seebeck) voltage offset in the transducer, which is why the transducer is chosen with a $1\ \mu\mathrm{V/K}$ specification and zeroed at each temperature; and it cannot measure $\Delta s$ independently, so the head is the only observable and the pore-size independence prediction is the only cross-check.

## 11. Expected observations

Success branch: head $15$ to $25\ \mathrm{bar}$ at $5\ \mathrm{K}$, linear in $\Delta T$ with slope $3$ to $5\ \mathrm{bar/K}$, independent of pore radius between $5$ and $20\ \mathrm{nm}$ while the flux scales as $r^2$, and a mass loss of $3$ to $30\%$/day from the sealed alumina slab.

Failure branch: head below $1\ \mathrm{bar}$ with a slope below $0.2\ \mathrm{bar/K}$, which means the confined water is bulk-like and $\Delta s \approx 0$; or a head that appears on the non-porous control, which means the measurement is a thermal artefact; or a head that grows with time at constant $\Delta T$, which means the seal is leaking.

The decisive signature is the slope: a thermo-osmotic head scales with $\Delta T$ and not with absolute temperature, while a vapour-pressure artefact scales as $\mathrm{d}P_{sat}/\mathrm{d}T = 2.4\ \mathrm{bar/K}$ at $300\ \mathrm{K}$. The two slopes are close enough ($2.4$ against $4.2\ \mathrm{bar/K}$) that the non-porous control is mandatory, not optional.

## 12. Magnitudes

| Quantity | Value | Basis |
| :--- | :--- | :--- |
| Entropy of transfer | $0.9\ k_B$ | hypothesized, range $0.05$ to $1.5\ k_B$ |
| Thermo-osmotic slope | $4.16\ \mathrm{bar/K}$ | $\Delta s/v_w$ |
| Head at $5\ \mathrm{K}$ (drying) | $20.8\ \mathrm{bar}$ | derived |
| Head at $13\ \mathrm{K}$ (desalination) | $54.1\ \mathrm{bar}$ | derived |
| $\Delta T$ matching $27\ \mathrm{bar}$ osmotic pressure | $6.5\ \mathrm{K}$ | zero flux limit |
| Heat carried per kg | $125\ \mathrm{kJ/kg}$ | $T\Delta s N_A/M_w$ |
| Work per kg at $5\ \mathrm{K}$ | $2.1\ \mathrm{kJ/kg}$ | $\Delta p/\rho$ |
| Ratio to latent heat | $18.1$ | $2.26\ \mathrm{MJ/kg}$ |
| Work / heat ratio | $1.66\times10^{-2}$ | Carnot, $\Delta T/T$ |
| Flux at $1\ \mathrm{kW/m^2}$ | $29\ \mathrm{kg/(m^2\,h)}$ | heat limited |
| Viscous ceiling, $5\ \mathrm{nm}$, slip $20\ \mathrm{nm}$ | $7.9\times10^{3}\ \mathrm{kg/(m^2\,h)}$ | Hagen-Poiseuille |
| Capillary entry pressure, dry pore | $98\ \mathrm{bar}$ | $2\gamma\cos\theta/r$ |
| Ion exclusion barrier, Na$^+$ | $135\ kT$ | Born, $\varepsilon_{pore}=2$ |
| Wetted sheet conduction | $1.4\times10^{5}\ \mathrm{W/m^2}$ | $k_{eff}\Delta T/d$ |
| Seawater osmotic pressure | $27\ \mathrm{bar}$ | $35\ \mathrm{g/kg}$ NaCl at $300\ \mathrm{K}$ |
| Reverse-osmosis operating pressure | $55$ to $70\ \mathrm{bar}$ | $2$ to $2.6\times$ osmotic |

## 13. Applications

* **Sludge and filter-cake drying.** A wastewater plant pays $3$ to $5\ \mathrm{MJ/kg}$ of water to dry cake that a press has already taken to $25\%$ solids. The remaining water is free water in $1$ to $100\ \mu\mathrm{m}$ pores, which is the regime this sheet addresses, and the heat can be the plant's own $35\ ^\circ\mathrm{C}$ effluent.
* **Brackish-water desalination.** At $1$ to $3\ \mathrm{g/kg}$ the osmotic load is $8$ to $23\ \mathrm{bar}$, so $5$ to $13\ \mathrm{K}$ covers it. The product is a flat plate and a sump, with no pressure vessel code and no energy-recovery turbine.
* **Timber and ceramic drying without air.** No air means no dust, no oxidation, no case-hardening from a surface that dries faster than the core, because the flux is set by the sheet and not by the surface boundary layer.
* **Brine concentration ahead of a crystalliser.** The head is a pressure, so it competes only with the osmotic pressure, not with the boiling-point elevation that makes evaporative brine concentration expensive.
* **Cold-climate drying.** A $5\ \mathrm{K}$ difference exists between a $20\ ^\circ\mathrm{C}$ room and a $15\ ^\circ\mathrm{C}$ slab, and it exists in reverse between outdoor air and a building. The mechanism runs in either direction, so the same sheet is a dehumidifier in summer and a dryer in winter.

## 14. Unresolved questions

* What is the measured entropy of transfer for water in a $5\ \mathrm{nm}$ hydrophobic pore? The whole dossier rests on $0.9\ k_B$ and no derivation fixes it. The range $0.05$ to $1.5$ is a physical bound, not a measurement.
* Does the sign flip when a monolayer of adsorbed organic (a surfactant, a protein, a biofilm) coats the pore? A biofilm would make the wall hydrophilic and reverse the flow, which turns a drying sheet into a wetting sheet.
* How fast does the sheet foul, and can it be cleaned by back-flushing at the $21\ \mathrm{bar}$ the device generates itself?
* Does the $20\%$ porosity track-etched geometry survive $10^{4}$ pressure cycles at $2\ \mathrm{MPa}$, or does the pore array craze from the silane layer?
* Is the conduction short-circuit fixable by lateral flow in a $1\ \mathrm{mm}$ low-conductivity substrate, or does the hydraulic resistance then dominate? The arithmetic says the two limits cross at a flow path of about $300\ \mu\mathrm{m}$, which is a design number that has not been built.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 5 | 3 | 5 | 5 | 5 |

Total: 27/30.
Confidence: 55%, basis: the Carnot identity is exact and ties the head to the heat with one parameter, so the model cannot be internally wrong; the plausibility score is held down by the unmeasured entropy of transfer, which spans a factor of $30$ and decides whether the desalination corollary exists at all.

## 16. Status

Live, wounded on $\Delta s$. The drying claim survives the full plausible range of the entropy of transfer (down to $0.2\ k_B$); the desalination corollary needs $\ge 0.9\ k_B$ and dies at $0.5\ k_B$, where the $54\ \mathrm{bar}$ operating point needs $23\ \mathrm{K}$ instead of $13\ \mathrm{K}$. The first experiment measures the slope, not the mechanism, because the slope is the number that decides both.
