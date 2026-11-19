# Vector 54: Interfacial Microdischarge Nitrogen Fixation with Continuous Product Stripping

**Status:** live
**Confidence:** 50%, basis: the energy floor (1.79 kWh/kg N, i.e. 1.87 eV per N2 against a target of 8.36 eV) is exact thermodynamics and the 300 K equilibrium NO fraction of $2.7\times10^{-16}$ makes stripping mandatory rather than optional, while the open risks are ozone selectivity at 1 atm and a 100 cm^2 stripping membrane that is 10x the discharge footprint.

## 1. Name

The Interfacial Microdischarge Nitrogen Fixation Reactor with Continuous Product Stripping (Ambient-Pressure Non-Thermal Fixation of N2 to Nitrate, With In-Line Membrane Extraction of NO Before Back-Reduction)

## 2. Fundamental problem

Fix atmospheric nitrogen into plant-available nitrate at ambient pressure and ambient temperature. The stripped requirement: take N2 from air, break one bond per molecule, oxidize the nitrogen to +2 or higher, and land it in water as nitrate, using electricity and no hydrogen feedstock, at a specific energy that undercuts the 60 kWh/kg N of the 1903 arc process by roughly an order of magnitude.

The incumbent is expensive in a way that is easy to state. World ammonia output is about 150 Mt N per year, and the sector consumes 1 to 2% of world primary energy. With world primary energy at 600 EJ/yr, 1% is 6 EJ and 2% is 12 EJ, so the implied intensity is $6\times10^{18}/(1.5\times10^{11}\ \mathrm{kg}) = 40\ \mathrm{MJ\,kg^{-1}}$ to 80 MJ/kg N, i.e. 11 to 22 kWh/kg N including natural gas feedstock. The plant runs at 200 bar and 450 C because that is where the equilibrium constant for ammonia allows 15 to 20% single-pass conversion.

## 3. Falsification statement

In a flow reactor at 100 W coupled to an in-line membrane stripper, fed with air at 1 to 5 bar:

1. Specific energy, computed as electrical input divided by nitrogen fixed as nitrate, must be $\le 10\ \mathrm{kWh\,kg^{-1}\,N}$;
2. Nitrate selectivity, nitrate nitrogen divided by total fixed nitrogen (nitrate, nitrite, and unabsorbed NOx), must be $\ge 50\%$;
3. Ozone leaving the reactor must be below 10% of the fixed nitrogen on a molar basis, measured at the stripper exhaust by UV absorption at 254 nm.

Killed if specific energy exceeds $25\ \mathrm{kWh\,kg^{-1}\,N}$. That threshold is not arbitrary: the 1903 Birkeland-Eyde arc consumed about 60 kWh/kg N, so $25\ \mathrm{kWh/kg}$ N is the point at which the design becomes indistinguishable from re-running an arc furnace with better instrumentation. Killed also if nitrate selectivity is below 20%, because the product is then mostly NOx returned to the atmosphere.

## 4. Hypothesis

A 50 micrometre non-thermal discharge in air at 1 atm delivers 3.7 MV/m at an $E/N$ of 150 Td, which puts 0.35 eV per feed molecule into vibrational and electronic channels while leaving the gas at 300 K. That is enough to dissociate a fraction of N2 and O2 and form NO, whose formation enthalpy, $+90.3\ \mathrm{kJ\,mol^{-1}}$, costs 6.45 MJ per kg of fixed nitrogen, or 1.79 kWh/kg N. The product is thermodynamically doomed in the gas phase, where the 300 K equilibrium NO mole fraction is $2.7\times10^{-16}$, and it is also kinetically doomed inside the discharge, where nitrogen atoms destroy it with a 29 microsecond lifetime. Both constraints are removed by the same move: extract the NO across a porous hydrophobic membrane into an alkaline film within a few milliseconds of formation, in the afterglow where the atoms have recombined. Nitrate in solution is stable at 300 K, so the stripping step converts a metastable gas into a thermodynamically locked product and lets the reactor run far from equilibrium.

## 5. Why convention is insufficient here

Haber-Bosch is equilibrium-limited and the industry knows it: ammonia is condensed out and the loop is recycled, which is why 15 to 20% single-pass conversion is economically sufficient. The nitrogen oxidation route has a far more extreme version of the same problem, and this is the number that governs the whole design:

$$K_p(298\ \mathrm{K}) = \exp\left(-\frac{2\Delta G_f^{NO}}{RT}\right) = \exp\left(-\frac{173200}{(8.314)(298)}\right) = 4.6\times10^{-31}$$

$$x_{NO} = \sqrt{K_p\,x_{N_2}\,x_{O_2}} = \sqrt{(4.6\times10^{-31})(0.78)(0.21)} = 2.7\times10^{-16}$$

At 300 K there is no such thing as an equilibrium NO concentration. Raise the temperature to 2000 K with $\Delta S = +24.8\ \mathrm{J\,mol^{-1}\,K^{-1}}$ and $\Delta G = 180.6 - 49.6 = 131\ \mathrm{kJ\,mol^{-1}}$, giving $K_p = 3.8\times10^{-4}$ and $x_{NO} = 0.8\%$; at 3000 K, $x_{NO} = 4.8\%$. The arc process exploited the 3000 K value and then lost it in the quench: gas at 3000 K must drop below 1000 K in milliseconds or the equilibrium reverses, and the practical loss is what turned 4.8% into 60 kWh/kg N.

The microdischarge avoids the quench entirely, because the gas never heats. The electron temperature is 1.5 eV (17400 K) while the translational temperature stays at 300 K, so the product forms cold and does not have a hot reservoir to re-equilibrate against. What it does have is a discharge zone full of nitrogen atoms, which is a kinetic rather than thermodynamic destruction channel and is quantified in section 7 at 29 microseconds.

A third reason convention is insufficient: the field is crowded. Arc, glow, dielectric barrier, gliding arc, and packed-bed plasma nitrogen fixation have all been built, with reported specific energies of 20 to 40 kWh/kg N for modern non-thermal devices. Nothing in the discharge itself is defensible as a claim. The only claim here is the stripping step and its timing, and the arithmetic that shows why the timing matters.

## 6. Mechanism

* $\Delta H_f^{NO}$: nitric oxide formation enthalpy ($+90.3\ \mathrm{kJ\,mol^{-1}}$). [established]
* $E_{N_2}$: nitrogen triple bond energy ($941\ \mathrm{kJ\,mol^{-1}}$). [established]
* $P$: reactor electrical input (100 W). [assumed]
* $g$: discharge gap (50 micrometres). [assumed]
* $E/N$: reduced field (150 Td $= 1.5\times10^{-19}\ \mathrm{V\,m^2}$). [assumed, 100 to 200 Td typical]
* $T_g$: gas temperature (300 K). [assumed]
* $p$: operating pressure (1 bar baseline, 0.2 bar variant). [assumed]
* $\eta_{NO_3}$: nitrate selectivity target (0.5). [hypothesized]

The device is a stack: a dielectric barrier microdischarge array on a 50 micrometre gap, an afterglow channel of 10 cm, and a porous hydrophobic membrane wetted on the far side by 0.01 M NaOH.

1. Air is compressed to 1 to 5 bar and passed through the array at 4.3 L/min, giving a 0.7 ms residence in the 0.05 $\mathrm{cm^3}$ discharge volume.
2. Filamentary microdischarges at 183 V across 50 micrometres deposit 0.35 eV per feed molecule, enough to dissociate roughly one N2 in 20.
3. N and O atoms react in the discharge to form NO at the rate set by the three-body and Zeldovich channels.
4. The gas leaves the discharge. Nitrogen atoms recombine on a 41 ms time constant and are gone; NO remains at 0.1 to 1% of the flow.
5. The afterglow channel delivers the gas to the membrane within 40 to 100 ms, after the atoms are gone and before surface-catalyzed reduction on the duct walls matters.
6. NO and NO2 cross the 20 micrometre porous membrane into the alkaline film, where they disproportionate to nitrite and nitrate, and where ozone oxidizes nitrite to nitrate.
7. The absorbed liquid is recirculated and the nitrate is concentrated to 1 M for fertigation.
8. Unreacted air is recirculated; the 5.5% single-pass conversion means 95% of the flow makes the loop repeatedly.

## 7. Mathematical model

Thermodynamic minimum, per kg of fixed nitrogen:

$$e_{min} = \frac{2\Delta H_f^{NO}}{M_N} = \frac{2(90.3\ \mathrm{kJ\,mol^{-1}})}{14\ \mathrm{g\,mol^{-1}}} = 6.45\ \mathrm{MJ\,kg^{-1}} = 1.79\ \mathrm{kWh\,kg^{-1}}$$

* $[e] = (\mathrm{kJ\,mol^{-1}})/(\mathrm{g\,mol^{-1}}) = \mathrm{kJ\,g^{-1}} = \mathrm{MJ\,kg^{-1}}$. Check passes. The 1.79 kWh/kg N follows from $6.45\times10^{6}/3.6\times10^{6}$.

Energy per fixed molecule at the 8 kWh/kg N design target:

$$\varepsilon = \frac{e\,M_N}{N_A} = \frac{(8)(3.6\times10^{6})(0.014)}{6.022\times10^{23}} = 6.7\times10^{-19}\ \mathrm{J} = 4.2\ \mathrm{eV\ per\ N\ atom}$$

* $[eM_N/N_A] = (\mathrm{J\,kg^{-1}})(\mathrm{kg\,mol^{-1}})/(\mathrm{mol^{-1}}) = \mathrm{J}$. Check passes. Per N2 this is 8.4 eV, against the 941 kJ/mol triple bond of 9.76 eV and the net reaction requirement of 1.87 eV. The target sits at 86% of the gross bond energy and 4.5x the net enthalpy, which is the physically sensible band for a process that breaks a bond and recovers part of it in the product.

Reduced field and voltage across the gap, with number density at 1 bar, 300 K:

$$n = \frac{p}{k_BT} = \frac{1.013\times10^{5}}{(1.38\times10^{-23})(300)} = 2.45\times10^{25}\ \mathrm{m^{-3}}$$

$$E = \left(\frac{E}{N}\right)n = (1.5\times10^{-19})(2.45\times10^{25}) = 3.67\times10^{6}\ \mathrm{V\,m^{-1}}, \qquad V = Eg = 183\ \mathrm{V}$$

* $[(E/N)n] = (\mathrm{V\,m^{2}})(\mathrm{m^{-3}}) = \mathrm{V\,m^{-1}}$. Check passes. 183 V across 50 micrometres at 1 atm is consistent with the Paschen curve for air at $pd = 3.8\ \mathrm{Torr\,cm}$, which is above the 0.8 Torr cm minimum, so the array is a stable filamentary discharge rather than a glow.

Throughput and residence time:

$$\dot m_N = \frac{P}{e} = \frac{0.1\ \mathrm{kW}}{8\ \mathrm{kWh\,kg^{-1}}} = 0.0125\ \mathrm{kg\,h^{-1}} = 12.5\ \mathrm{g\,N\,h^{-1}}$$

* $[\mathrm{kW}/(\mathrm{kWh\,kg^{-1}})] = \mathrm{kg\,h^{-1}}$. Check passes. That is 0.30 kg N per day, or 1.33 kg of nitrate per day at $62/14$ mass ratio.
* Feed at 78% N2: 12.5 g N/h needs $12.5/0.78 = 16\ \mathrm{g\,h^{-1}}$ of air, i.e. 4.3 L/min at 1 bar. Residence in the 0.05 $\mathrm{cm^3}$ gap is $5\times10^{-8}/7.2\times10^{-5} = 0.7\ \mathrm{ms}$.
* Energy per feed molecule: $100/(7.2\times10^{-5})(2.45\times10^{25}) = 5.7\times10^{-20}\ \mathrm{J} = 0.35\ \mathrm{eV}$. With 8.4 eV needed per N2, the single-pass conversion of available N2 is $0.35(0.78)/8.4 = 3.2\%$ to 5.5% depending on whether the denominator counts all molecules or N2 only. The loop recycle ratio is therefore 18 to 30.

Equilibrium limits, for the record:

$$K_p(T) = \exp\left(-\frac{2\Delta H - 2T\Delta S}{RT}\right), \qquad x_{NO} = \sqrt{K_p x_{N_2}x_{O_2}}$$

* $[K_p]$ dimensionless; $[x_{NO}]$ dimensionless. Check passes. 298 K: $2.7\times10^{-16}$. 2000 K: $0.8\%$. 3000 K: $4.8\%$. The 300 K figure is why the product cannot be stored in the gas phase and why absorption into water, where nitrate has a negative free energy of formation, is the actual product-locking step.

Destruction kinetics in the discharge zone, $k(N + NO) = 3.4\times10^{-17}\ \mathrm{m^{3}\,s^{-1}}$ [established]:

$$\tau_{NO} = \frac{1}{k[N]} = \frac{1}{(3.4\times10^{-17})(1\times10^{21})} = 2.9\times10^{-5}\ \mathrm{s}$$

* $[1/(k[N])] = 1/((\mathrm{m^3\,s^{-1}})(\mathrm{m^{-3}})) = \mathrm{s}$. Check passes. NO formed in the discharge is destroyed in 29 microseconds, 24 e-foldings inside a 0.7 ms residence. The product must therefore be formed or survive in the afterglow.
* Nitrogen atom removal by three-body recombination, $k = 10^{-45}\ \mathrm{m^{6}\,s^{-1}}$: $\tau_N = 1/(k[N][M]) = 1/((10^{-45})(10^{21})(2.45\times10^{25})) = 41\ \mathrm{ms}$. So there is a window from about 40 ms to the duct residence limit in which N atoms are gone and NO persists.

Ozone competition, $k(O + O_2 + M) = 6\times10^{-46}\ \mathrm{m^{6}\,s^{-1}}$ and $k(NO + O_3) = 1.8\times10^{-20}\ \mathrm{m^{3}\,s^{-1}}$:

$$\tau_{O_3} = \frac{1}{k[O_2][M]} = \frac{1}{(6\times10^{-46})(5.15\times10^{24})(2.45\times10^{25})} = 13\ \mathrm{\mu s}$$

* $[\tau]$ = s. Check passes. Ozone forms 13 times faster than NO is destroyed by it, so at 1 atm ozone is an unavoidable intermediate. The design consequence is that ozone must be consumed in the trap, not prevented in the gas: $k(NO + O_3)$ at 0.1% NO gives $\tau = 2.3\ \mathrm{ms}$, so ozone and NO annihilate on the way to the membrane, and the falsifier counts only the ozone that exits unreacted.

Stripping flux and membrane area. Porous PTFE, 20 micrometre thick, 50% porosity, tortuosity 2:

$$D_{eff} = \frac{D\phi}{\tau} = \frac{(10^{-5})(0.5)}{2} = 2.5\times10^{-6}\ \mathrm{m^2\,s^{-1}}, \qquad \dot n = \frac{D_{eff}}{L}\Delta C = 0.125 \times 0.2 = 0.025\ \mathrm{mol\,m^{-2}\,s^{-1}}$$

* $[(D/L)\Delta C] = (\mathrm{m\,s^{-1}})(\mathrm{mol\,m^{-3}}) = \mathrm{mol\,m^{-2}\,s^{-1}}$. Check passes. At the 12.5 g N/h production rate, 2.48 mol of N per hour is $6.9\times10^{-5}\ \mathrm{mol\,s^{-1}}$, so the required area is 0.0028 $\mathrm{m^2}$, and a 100 $\mathrm{cm^2}$ membrane runs at about 3x margin.
* A dense 50 micrometre PDMS membrane at 1000 Barrer gives a permeance of $6.7\times10^{-9}\ \mathrm{mol\,m^{-2}\,s^{-1}\,Pa^{-1}}$, i.e. a flux of $3.4\times10^{-6}$ at 500 Pa of NO, requiring 74 $\mathrm{m^2}$. The membrane must be porous and non-wetting, and that choice is a factor of 700 in area.

Compressor penalty at 5 bar, isothermal:

$$W = p_1\dot V\ln\frac{p_2}{p_1} = (1.013\times10^{5})(7.2\times10^{-5})(1.609) = 11.7\ \mathrm{W}$$

* $[\mathrm{Pa\,m^{3}\,s^{-1}}] = \mathrm{W}$. Check passes. 12 W on a 100 W reactor raises the specific energy from 8.0 to 9.0 kWh/kg N.

## 8. Physical constraints

* Ozone is not optional at 1 atm. The three-body formation time constant of 13 microseconds against a 0.7 ms residence means 54 formation cycles per pass. Suppressing it at the source requires either 0.2 bar operation, which cuts the three-body term 25x and costs a 25x larger volumetric flow and a Roots blower, or accepting ozone as an intermediate that is consumed in the alkaline trap.
* Nitrate must be concentrated. The trap delivers 1.33 kg of nitrate per day into a recirculating liquid; at 0.01 M the water inventory is 2100 L/day, so the loop must concentrate to 1 M or the product is 99.9% water. That is an evaporator, and it is not in the 100 W budget.
* Electrode current. At 183 V and 100 W the array carries 0.55 A over 10 $\mathrm{cm^2}$, i.e. 55 $\mathrm{mA\,cm^{-2}}$, across about 550 filaments at 1 mA each. The dielectric must survive that current density at 50 micrometre thickness, which sets the alumina or quartz wall material and the cooling requirement.
* Single pass is 3 to 5%. The loop moves 4.3 L/min to fix 12.5 g N/h, so the plant is a recycle reactor and the product stream is a small bleed. Any membrane or trap leak is a 20x larger loss than the production rate.
* Pressure trades against area. Raising pressure to 5 bar helps the membrane (higher partial pressure) and hurts the compressor (12 W per 100 W). Lowering to 0.2 bar helps ozone and hurts both.

## 9. Contradiction ledger

* Crowded field, low originality. Arc, gliding arc, DBD, and packed bed plasma fixation all exist, with 20 to 40 kWh/kg N reported. Nothing in the discharge is defensible. The only claim is the afterglow timing window and the membrane, and that is a narrow claim to hang a vector on. Score 2 for originality is honest, not conservative.
* The equilibrium argument is not the usual one. Haber-Bosch is limited by an equilibrium constant of order 1; this reaction has $K_p = 4.6\times10^{-31}$ at 300 K, so the gas phase cannot hold the product at all. The honest statement is that absorption, not equilibrium displacement, is what locks the nitrogen. Nitrate in water has a negative free energy of formation; NO in air does not. Writing this as "removal shifts equilibrium" would be a category error, since there is no gas-phase equilibrium to shift at ambient temperature.
* Ozone is a regulated pollutant and a plant toxin. Ground-level ozone above 70 ppb over 8 h is a health threshold, and the reactor produces ozone as an intermediate at a rate comparable to its nitrate rate. Any unreacted ozone is an emission, and the falsifier caps it at 10% of fixed nitrogen. Closed-loop operation with a manganese dioxide destructor is the mitigation, and it costs pressure drop and consumable mass.
* Energy accounting must include the compressor. 12 W of 100 W at 5 bar, plus the loop's pressure drop, plus the evaporator for concentration. The 8 kWh/kg N target is a reactor figure; the plant figure is 9 to 12 kWh/kg N, which is still 5x better than the arc and comparable to a modern Haber-Bosch plant on electricity alone without the gas feedstock.
* Nitrate is the wrong product for soil. Nitrate is mobile and leaches; ammonia and urea are the soil products because they bind. Calcium nitrate is a fertigation and hydroponics product, a high-value thin market, not the 150 Mt/yr bulk market. Impact at 5 is impact on the nitrogen problem, not addressable revenue in year one.
* Economics at grid power fail. At 8 kWh/kg N and \$0.10/kWh the electricity is \$0.80/kg N against an ammonia plant gate of \$0.40 to 0.60/kg N. At \$0.02/kWh, i.e. curtailed or stranded renewable power, it is \$0.16/kg N and the design wins. The vector is a story about otherwise-curtailed electricity, not a story about replacing Haber-Bosch.
* Surface-catalyzed back-reduction is unquantified. Metal duct walls catalyse $2NO \rightarrow N_2 + O_2$ at an activation energy of roughly 100 kJ/mol, which at 300 K is slow but not zero, and no rate constant is pinned here. This is the one number the design needs and does not have.

## 10. Experiment

* Reactor: alumina dielectric barrier array, 50 micrometre gap, 10 $\mathrm{cm^2}$ electrode area, 550 filaments at 1 mA, driven at 183 V, 1 to 20 kHz, 100 W.
* Gas: compressed air at 1, 2, and 5 bar, 1 to 5 L/min, mass flow controlled to 2%, dew point below $-40$ C, passed through a 10 cm afterglow duct at 300 K.
* Stripper: 100 $\mathrm{cm^2}$ of 20 micrometre porous PTFE, 0.1 micrometre pore, on a 0.01 M NaOH loop at 50 mL/min, downstream of the afterglow duct with a variable delay line from 10 to 200 ms (the delay is the discriminating control, not a refinement).
* Metrology: nitrate and nitrite by ion chromatography to 0.1 mg/L; total fixed nitrogen by alkaline persulfate digestion followed by reduction and colorimetry; NO and NO2 by chemiluminescence at the inlet and outlet; ozone by UV absorption at 254 nm; specific energy computed as DC input divided by fixed nitrogen in the liquid plus the measured NOx that escaped.
* Controls: (a) same reactor with the membrane removed and the trap replaced by a cold finger, which isolates the stripping contribution; (b) same reactor at 0.2 bar, which isolates the ozone channel; (c) electrical-only blank with no gas flow, which measures the discharge power factor.
* Null result, defined before the run: specific energy above 10 kWh/kg N at 100 W with the stripper engaged, or nitrate selectivity below 50%, or ozone above 10% of fixed nitrogen at the exhaust.
* What this cannot distinguish: whether the improvement comes from stripping NO or from cooling the gas in the membrane module, and whether the 40 to 100 ms window is real or whether NO simply survives long enough everywhere. The delay-line sweep separates these by moving the absorption point across the window.

## 11. Expected observations

* Success branch: 12.5 g N/h at 8.0 to 9.0 kWh/kg N, nitrate 55% of fixed nitrogen, nitrite 10%, unabsorbed NOx 35%, ozone 4% of fixed nitrogen at the exhaust. Removing the membrane drops nitrate selectivity to 15% and raises specific energy to 22 kWh/kg N, which is the whole point of the vector. A 0.2 bar run shows ozone at 1% and selectivity at 62%, confirming the three-body mechanism.
* Failure branch: specific energy above 25 kWh/kg N with selectivity below 20%, and no dependence on the delay-line position, which would mean the product is being destroyed or never formed rather than being reclaimed.
* Intermediate branch: 12 to 15 kWh/kg N with 40% selectivity, which is a real improvement on the arc but not on existing plasma devices, and would move the vector to wounded with the stripping claim intact and the discharge claim dead.

## 12. Magnitudes

* Nitrogen triple bond: 941 $\mathrm{kJ\,mol^{-1}}$ (9.76 eV per N2).
* NO formation enthalpy: $+90.3\ \mathrm{kJ\,mol^{-1}}$.
* Thermodynamic floor: 6.45 MJ/kg N = 1.79 kWh/kg N = 1.87 eV per N2.
* Design target: 8 kWh/kg N = 8.4 eV per N2, i.e. 86% of the bond energy.
* Birkeland-Eyde historical: 60 kWh/kg N. Modern non-thermal plasma: 20 to 40 kWh/kg N.
* Equilibrium NO fraction: $2.7\times10^{-16}$ at 298 K, 0.8% at 2000 K, 4.8% at 3000 K.
* Reduced field and gap voltage: 150 Td, 183 V across 50 micrometres.
* Reactor power and throughput: 100 W, 12.5 g N/h, 0.30 kg N/day, 1.33 kg nitrate/day.
* Feed flow and residence: 4.3 L/min, 0.7 ms, 0.35 eV per feed molecule.
* Single-pass conversion: 3 to 5%; recycle ratio 18 to 30.
* NO lifetime against N atoms: 29 microseconds. N atom lifetime: 41 ms. Ozone formation: 13 microseconds.
* Stripping membrane: 100 $\mathrm{cm^2}$ porous PTFE against 74 $\mathrm{m^2}$ of dense PDMS.
* Compressor at 5 bar: 12 W, raising 8.0 to 9.0 kWh/kg N.
* Land equivalent: 150 kg N/ha/yr is 0.41 kg N/day/ha, so one 100 W module covers 0.73 ha.

## 13. Applications

* Nearest-term: greenhouse and hydroponics fertigation, where calcium nitrate sells at a premium, the product is used at 1 to 10 mM in a closed loop, and the 0.3 kg N/day of one module matches a 0.1 to 1 ha glasshouse.
* Nearest-term: on-site nitrate generation where transport of fertilizer is the binding cost, i.e. remote agriculture and islands, using curtailed renewable power at under \$0.02/kWh.
* Long-horizon: nitrate as an oxidant for wastewater denitrification and for anaerobic digestion dosing, where a liquid product at 1 M is exactly the required form.
* Long-horizon: a plasma-plus-trap module as a laboratory standard for reactive nitrogen at known isotopic composition, using 15N2 feed.

## 14. Unresolved questions

* What is the actual rate constant for surface-catalyzed NO reduction on the duct and membrane materials at 300 K, and does the 40 to 100 ms afterglow window survive it?
* Can nitrate selectivity exceed 50% at 1 atm, or is the three-body ozone channel a hard ceiling that forces 0.2 bar operation and a 25x larger plant for the same output?
* Is the direct-current discharge the right driver, or does a nanosecond-pulsed discharge with a reduced duty cycle cut the vibrational overhead and move 8 kWh/kg N to 5?
* How much of the 3 to 5% single-pass conversion is recoverable in a loop before the bleed stream becomes the dominant nitrogen loss?
* What is the membrane's fouling and wetting lifetime in a stream carrying nitric acid aerosol, given that a single wetted pore converts the stripper from a gas contactor into a liquid leak?

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2 | 4 | 5 | 5 | 5 | 5 |

Total: 26/30.
Confidence: 50%, basis: the 1.79 kWh/kg N floor and the $2.7\times10^{-16}$ equilibrium fraction are exact and the 183 V breakdown estimate is consistent with Paschen at 1 atm, while the ozone selectivity ceiling at 1 atm and the absence of a measured back-reduction rate constant keep confidence at even odds.

## 16. Status

Live.
