# Vector 55: Resonant Mechano-Bactericidal Pillar Array (A Killing Mechanism With Nothing to Mutate)

**Status:** live
**Confidence:** 52%, basis: the strain selectivity $\epsilon = u/R$ is exact arithmetic (a factor of 10 between a $1\ \mu\mathrm{m}$ coccus and a $10\ \mu\mathrm{m}$ fibroblast), and the pillar resonance is a textbook cantilever result, but the same arithmetic sets $464\ \mathrm{W/cm^2}$ of drive power, 220 bar of radiated pressure and ${1.0\times10^{13}}$ cycles per day at the working amplitude, none of which has been shown survivable by a surface device.

## 1. Name

The Resonant Mechano-Bactericidal Pillar Array (Size-Selective Membrane Strain Delivered at Pillar Mechanical Resonance, a Non-Chemical Surface Kill)

## 2. Fundamental problem

Prevent bacterial colonisation of a surface without any chemical agent, because every chemical killing mechanism is eventually defeated by a point mutation or by one horizontal gene transfer event, and because sub-lethal exposure selects the survivors rather than killing them.

Stripped to the bare physical requirement: deliver a supra-threshold membrane strain to a $1\ \mu\mathrm{m}$ cell and a sub-threshold membrane strain to a $10\ \mu\mathrm{m}$ cell standing on the same surface, using only geometry and an externally supplied vibration, with no molecule that a bacterium can mutate, pump out, or acquire a gene against.

## 3. Falsification statement

A $1\ \mathrm{cm^2}$ silicon chip carrying a hexagonal pillar array (pillar diameter $200\text{ nm}$, height $1\ \mu\mathrm{m}$, pitch $400\text{ nm}$, $6.25\times10^{8}$ pillars per $\mathrm{cm^2}$) is serially passaged with *Staphylococcus aureus* ATCC 29213 at $37\ ^\circ\mathrm{C}$ in $1/100$ TSB:

1. Each day $10^{6}\ \mathrm{CFU}$ are transferred to a fresh, sterile chip and driven for $2\ \mathrm{h}$ at the sub-lethal amplitude of $6\text{ nm}$ (0.3 of working), then the survivors are recovered and carried to the next day. The cycle runs 30 days, with the survival fraction measured every 3 days by CFU plating.
2. **First kill condition.** The mechanism is killed if the day-30 survival fraction improves by more than $10\times$ over the day-1 survival fraction. A heritable mechanical adaptation is the only explanation for a $>10\times$ gain, and no such adaptation may be credited to the geometry.
3. **Second kill condition.** The mechanism is killed if human dermal fibroblast (HDFa) viability on the array falls below $90\%$ at the working amplitude of $20\text{ nm}$ ($2\ \mathrm{h}$, $37\ ^\circ\mathrm{C}$, calcein AM / propidium iodide).
4. **Third kill condition.** The mechanism is killed if resonant drive at $20\text{ nm}$ produces less than $2\times$ the kill of the same array driven quasi-statically (1 Hz) to the same $20\text{ nm}$ displacement, because that would leave the resonance doing no work and the vector would be ordinary mechano-bactericidal topography in disguise.

The null result is defined before the run: survival ratio day 30 over day 1 $\le 10$, fibroblast viability $\ge 90\%$, and resonant over static kill ratio $\ge 2$.

## 4. Hypothesis

At a pillar tip displacement of $20\text{ nm}$, a membrane draped over one pillar is strained by $\epsilon = u/R$, so a $1\ \mu\mathrm{m}$ coccus ($R = 0.5\ \mu\mathrm{m}$) sees $4.0\%$ areal strain, above its $3$ to $5\%$ rupture strain, while a $10\ \mu\mathrm{m}$ fibroblast ($R = 5\ \mu\mathrm{m}$) sees $0.4\%$, a factor of 10 below its own lysis strain. Driving the pillars at their own mechanical resonance lowers the force, and therefore the actuator, needed to reach $20\text{ nm}$ by the quality factor $Q$, so a thin piezoelectric plate can drive a whole array that would otherwise need a $50\ \mathrm{bar}$ static load. The kill is a membrane rupture threshold crossed once per cycle at $10^{8}$ cycles per second, and there is no protein target, no uptake step, and no gene whose product the bacterium can alter.

## 5. Why convention is insufficient here

Chemical killing fails by selection, and the failure is quantitative, not theoretical. A single conjugation event transfers a $\beta$-lactamase determinant at a frequency of $10^{-6}$ to $10^{-3}$ per donor per hour, so one event in a $10^{9}$-cell biofilm is sufficient. The vancomycin target is remodelled from D-Ala-D-Ala to D-Ala-D-Lac by two enzymes, which drops binding by $1000\times$ while costing the cell nothing measurable in growth rate. Sub-lethal exposure is worse than no exposure: inside the mutant selection window, between the MIC and the mutant prevention concentration, the resistant subpopulation outgrows the susceptible one by $10$ to $1000\times$ within 24 h. Every deployed chemical surface therefore has a clock on it.

Mechanical killing has no such clock in principle, because the target is the lipid bilayer envelope, which is a physical object rather than a gene product. The published mechano-bactericidal surfaces are static, and they are limited by geometry rather than by biology:

* A cicada wing carries pillars $60\text{ nm}$ in diameter, $200\text{ nm}$ tall, $170\text{ nm}$ apart, and kills *Pseudomonas aeruginosa* by $3\ \log_{10}$ in 3 to 6 h. It leaves *S. aureus* essentially intact because a $20$ to $80\text{ nm}$ peptidoglycan layer spreads the strain over many pillars instead of concentrating it into the membrane.
* Black silicon does the same, at the same Gram selectivity, and reported passaging shows the kill efficiency drifting downward over successive exposures.
* All of these surfaces deliver displacement by adhesion alone. The available displacement is fixed by turgor and by the pillar spacing: a $1\ \mu\mathrm{m}$ cell spanning $2.5$ pillars at $400\text{ nm}$ pitch can sag only $\approx 40\text{ nm}$ into the gaps before it touches the floor, and most of that sag is taken up by the cell wall, not the membrane.

The missing degree of freedom is that the displacement can be supplied from outside the cell, at a frequency the cell cannot follow. A lipid membrane relaxes on $1$ to $100\text{ ms}$, so a $4\%$ strain applied and released in $4\text{ ns}$ is not relaxed, not redistributed, and not repaired between cycles.

The second missing degree of freedom is size selectivity. Static topography has one pillar spacing and therefore one cell size that it strains well. A $10\times$ strain ratio between a coccus and a fibroblast is available for free from $\epsilon = u/R$ at any spacing, provided the displacement can be imposed rather than absorbed.

## 6. Mechanism

* $d$: pillar diameter, $200\text{ nm}$. [assumed]
* $L$: pillar height, $1\ \mu\mathrm{m}$. [assumed]
* $E$: Young's modulus, $170\ \mathrm{GPa}$ for silicon. [established]
* $\rho$: density, $2330\ \mathrm{kg/m^3}$ for silicon. [established]
* $k$: pillar bending stiffness at the tip, $40.0\ \mathrm{N/m}$. [hypothesized, derived in section 7]
* $m$: pillar mass, $7.32\times10^{-17}\ \mathrm{kg}$. [hypothesized, derived]
* $f_0$: pillar resonance, $118\ \mathrm{MHz}$ in vacuum, $99\ \mathrm{MHz}$ with added water mass. [hypothesized]
* $Q$: quality factor in water, $\approx 8$. [hypothesized]
* $u$: drive amplitude at the pillar tip, $20\text{ nm}$. [assumed]
* $R_b$: bacterial radius, $0.5\ \mu\mathrm{m}$ for a $1\ \mu\mathrm{m}$ coccus. [assumed]
* $R_m$: mammalian cell radius, $5\ \mu\mathrm{m}$ for a spread fibroblast. [assumed]
* $\epsilon_{rup}$: bacterial membrane rupture strain, $3$ to $5\%$. [assumed]
* $\tau_m$: membrane tension, $1\ \mathrm{mN/m}$. [assumed]
* $K_A$: bilayer area compressibility modulus, $0.2\ \mathrm{N/m}$. [established, range 0.1 to 0.3]
* $p$: pitch, $400\text{ nm}$. [assumed]

The device is a surface, not a drug. A silicon wafer is patterned by electron-beam lithography and deep reactive ion etching into a hexagonal array of pillars $200\text{ nm}$ in diameter and $1\ \mu\mathrm{m}$ tall on a $400\text{ nm}$ pitch, and a lead zirconate titanate plate $100\ \mu\mathrm{m}$ thick is bonded to the back.

1. A bacterium settles onto the array and drapes its envelope over the pillar tips. At $400\text{ nm}$ pitch a $1\ \mu\mathrm{m}$ coccus rests on 2 to 4 pillar tips and spans 2 to 3 gaps.
2. The piezo plate is driven at the pillar resonance, $118\ \mathrm{MHz}$ in vacuum, shifted to $99\ \mathrm{MHz}$ by the added mass of the water column each pillar drags with it.
3. Every pillar tip moves $20\text{ nm}$. The membrane over each tip is displaced by the same $20\text{ nm}$ over the footprint of the tip, and the strain it experiences is $u$ divided by the radius of curvature of the body it belongs to.
4. The coccus, with $R = 0.5\ \mu\mathrm{m}$, is strained to $4.0\%$, inside the $3$ to $5\%$ rupture band, and a pore nucleates in the bilayer. The membrane cannot relax to accommodate the strain because its relaxation time, $1$ to $100\text{ ms}$, is $10^{5}$ to $10^{7}$ times longer than the $4\text{ ns}$ half cycle.
5. The fibroblast, with $R = 5\ \mu\mathrm{m}$, is strained to $0.4\%$, which is below its lysis threshold by an order of magnitude, and below its mechanotransduction threshold for spreading and apoptosis signalling.
6. Resonance is what makes the displacement affordable. At resonance the drive force needed for a given amplitude is the static force divided by $Q$, so a $100\ \mu\mathrm{m}$ piezo plate can move the array at $20\text{ nm}$ with a few volts rather than with a $50\ \mathrm{bar}$ press.
7. The cycle repeats $10^{8}$ times per second. A cell that survives one excursion has to survive $7\times10^{11}$ more in the 2 h exposure, which converts a probabilistic pore nucleation event into a certainty.

## 7. Mathematical model

**(a) Second moment of area.**

$$I = \frac{\pi d^4}{64} = \frac{\pi (2.0\times10^{-7})^4}{64} = 7.85\times10^{-29}\ \mathrm{m^4}$$

* $[I] = \mathrm{m^4}$. Check: $(2.0\times10^{-7})^4 = 1.6\times10^{-27}$, divided by 64 and multiplied by $\pi$ gives $7.85\times10^{-29}$.

**(b) Tip bending stiffness, clamped base, load at the tip.**

$$k = \frac{3EI}{L^3} = \frac{3(1.70\times10^{11})(7.85\times10^{-29})}{(1.0\times10^{-6})^{3}} = \frac{4.00\times10^{-17}}{1.0\times10^{-18}} = 40.0\ \mathrm{N/m}$$

* $[E][I]/[L]^3 = (\mathrm{N\,m^{-2}})(\mathrm{m^4})/\mathrm{m^3} = \mathrm{N/m}$. Check passes.

**(c) Pillar mass.**

$$m = \rho \frac{\pi d^2}{4} L = 2330 \times 3.14\times10^{-20} = 7.32\times10^{-17}\ \mathrm{kg}$$

* $[\rho][d^2][L] = (\mathrm{kg\,m^{-3}})(\mathrm{m^2})(\mathrm{m}) = \mathrm{kg}$. Check passes.

**(d) Resonance.**

$$f_0 = \frac{1}{2\pi}\sqrt{\frac{k}{m}} = \frac{1}{2\pi}\sqrt{\frac{40.0}{7.32\times10^{-17}}} = \frac{7.39\times10^{8}}{2\pi} = 1.18\times10^{8}\ \mathrm{Hz}$$

* $[k/m] = (\mathrm{kg\,s^{-2}})/\mathrm{kg} = \mathrm{s^{-2}}$, and $\sqrt{\mathrm{s^{-2}}} = \mathrm{s^{-1}}$. Check passes.

**(e) Reconciliation with the $3.7\ \mathrm{MHz}$ figure.**

The set $\{k = 0.040\ \mathrm{N/m},\ m = 7.32\times10^{-17}\ \mathrm{kg}\}$ does give $f = 3.72\ \mathrm{MHz}$, so $k$ and $f$ are consistent with each other. That stiffness is not silicon at $L = 1\ \mu\mathrm{m}$: $k \propto E$, so $k = 0.040\ \mathrm{N/m}$ at this geometry requires $E = 170\ \mathrm{MPa}$, a factor $1000$ below silicon. The same $1000\times$ is the $L^{-3}$ scaling, which means the $3.7\ \mathrm{MHz}$ set is also the response of silicon at $L = 10\ \mu\mathrm{m}$, and at $L = 10\ \mu\mathrm{m}$ the mass is $7.32\times10^{-16}\ \mathrm{kg}$ and the frequency is $1.18\ \mathrm{MHz}$, not $3.7\ \mathrm{MHz}$. No single geometry produces $3.7\ \mathrm{MHz}$ with these material constants.

The $3.7\ \mathrm{MHz}$ reading cannot be rescued by softening the pillar, because $Q$ collapses. For a slender cylinder fully inside the viscous boundary layer, the drag coefficient is $c \approx 4\pi\eta L/\ln(L/a) = 4\pi(10^{-3})(10^{-6})/2.3 = 5.5\times10^{-9}\ \mathrm{N\,s/m}$, so

$$Q = \frac{\sqrt{km}}{c} = \frac{\sqrt{(0.040)(7.32\times10^{-17})}}{5.5\times10^{-9}} = \frac{1.71\times10^{-9}}{5.5\times10^{-9}} = 0.31$$

* $[\sqrt{km}] = \sqrt{(\mathrm{N/m})(\mathrm{kg})} = \mathrm{kg/s}$, same as $[c]$. Check passes.

A $Q$ of $0.31$ is below the critical value of $0.5$, so a $3.7\ \mathrm{MHz}$ soft pillar is overdamped and has no resonance at all. At $118\ \mathrm{MHz}$ with real silicon, $\sqrt{km} = 5.41\times10^{-8}$ and the same slender-body drag estimate gives $Q = 9.8$; the oscillatory correction for a boundary layer of thickness $\delta = \sqrt{2\eta/(\rho_w\omega)} = 52\text{ nm}$, which is a quarter of the pillar diameter, moves that to the $8$ to $10$ range and is the reason $Q = 8$ is used below. The remainder of this dossier uses the self-consistent silicon set $k = 40.0\ \mathrm{N/m}$, $f_0 = 118\ \mathrm{MHz}$, $Q = 8$, and treats $3.7\ \mathrm{MHz}$ as the recorded slip.

**(f) Strain selectivity.**

$$\epsilon = \frac{u}{R} \quad\Longrightarrow\quad \frac{\epsilon_b}{\epsilon_m} = \frac{R_m}{R_b} = \frac{5.0\times10^{-6}}{0.5\times10^{-6}} = 10$$

* $[u/R] = \mathrm{m/m}$, dimensionless. Ratio of two dimensionless numbers, dimensionless. Check passes.
* Numbers: $\epsilon_b = 20\times10^{-9}/0.5\times10^{-6} = 4.0\%$; $\epsilon_m = 20\times10^{-9}/5.0\times10^{-6} = 0.40\%$.

**(g) Membrane elastic energy, and its size independence.**

$$W = \tfrac{1}{2}K_A\epsilon^2 A, \qquad A = 4\pi R^2$$

* Coccus: $W_b = \tfrac{1}{2}(0.2)(0.04)^2(4\pi)(0.5\times10^{-6})^2 = 5.0\times10^{-16}\ \mathrm{J}$.
* Fibroblast: $W_m = \tfrac{1}{2}(0.2)(0.004)^2(4\pi)(5.0\times10^{-6})^2 = 5.0\times10^{-16}\ \mathrm{J}$.
* $[K_A][\epsilon^2][A] = (\mathrm{N/m})(\mathrm{m^2}) = \mathrm{N\,m} = \mathrm{J}$. Check passes.

Because $A \propto R^2$ and $\epsilon^2 \propto R^{-2}$, the delivered energy is independent of cell size. The selectivity lives entirely in the threshold, not in the dose: both cells absorb $5.0\times10^{-16}\ \mathrm{J}$ ($1.2\times10^{5}\ k_BT$ at $310\ \mathrm{K}$), but only the coccus absorbs it at a strain above its rupture point. This is the load-bearing distinction and it is also the weakest link in the vector, because a $5\ \mu\mathrm{m}$ cell in suspension rounds up and takes the same energy.

**(h) Stored energy, drive power and tip velocity.**

$$E_p = \tfrac{1}{2}ku^2 = \tfrac{1}{2}(40.0)(2.0\times10^{-8})^2 = 8.0\times10^{-15}\ \mathrm{J}$$

* $[k][u^2] = (\mathrm{N/m})(\mathrm{m^2}) = \mathrm{J}$. Check passes.

Pillar number density at $400\text{ nm}$ pitch: $n = 1/p^2 = 6.25\times10^{12}\ \mathrm{m^{-2}} = 6.25\times10^{8}\ \mathrm{cm^{-2}}$. At resonance the drive supplies only the dissipated power:

$$P = \frac{2\pi f_0 E_p n}{Q} = \frac{(7.41\times10^{8})(8.0\times10^{-15})(6.25\times10^{8})}{8} = 4.6\times10^{6}\ \mathrm{W/m^2} = 464\ \mathrm{W/cm^2}$$

* $[f E n] = (\mathrm{s^{-1}})(\mathrm{J})(\mathrm{m^{-2}}) = \mathrm{W/m^2}$. Check passes.

Tip velocity and radiated pressure follow from the same amplitude:

$$v = 2\pi f_0 u = 14.8\ \mathrm{m/s}, \qquad p_{rad} = \rho_w c_w v = (1.0\times10^{3})(1.5\times10^{3})(14.8) = 2.2\times10^{7}\ \mathrm{Pa}$$

* $[\rho c v] = (\mathrm{kg/m^3})(\mathrm{m/s})(\mathrm{m/s}) = \mathrm{kg\,m^{-1}s^{-2}} = \mathrm{Pa}$. Check passes.

**(i) Root bending strain and fatigue budget.**

$$\epsilon_{root} = \frac{3ud}{2L^2} = \frac{3(2.0\times10^{-8})(2.0\times10^{-7})}{2(1.0\times10^{-6})^{2}} = 6.0\times10^{-3}$$

* $[ud/L^2] = \mathrm{m^2/m^2}$, dimensionless. Check passes.
* Cycles per day at $118\ \mathrm{MHz}$: $1.02\times10^{13}$. Cycles in a 30-day device life: $3.1\times10^{14}$.

## 8. Physical constraints

* **Drive power is the first wall.** $464\ \mathrm{W/cm^2}$ at the working amplitude, from section 7(h). The equivalent static statement is a spring-bed pressure of $k n u = (40)(6.25\times10^{12})(2.0\times10^{-8}) = 5.0\times10^{6}\ \mathrm{Pa}$, i.e. 50 bar, which is the load the piezo must supply. Human skin tolerates $0.02$ to $0.05\ \mathrm{W/cm^2}$ indefinitely, so the maximum area that can be driven at $20\text{ nm}$ is $0.05/464 = 1.1\times10^{-4}\ \mathrm{cm^2}$, a $0.1\ \mathrm{mm^2}$ patch. Scaling the amplitude down to fit a $1\ \mathrm{cm^2}$ patch gives $u = 20\sqrt{0.05/464} = 0.21\text{ nm}$, which is $0.04\%$ strain and does nothing.
* **Radiated pressure is the second wall.** Tip velocity $14.8\ \mathrm{m/s}$ radiates $2.2\times10^{7}\ \mathrm{Pa}$ (220 bar) at $118\ \mathrm{MHz}$. Transient cavitation in water begins at $\approx 10^{5}\ \mathrm{Pa}$ of negative peak, so the array is $200\times$ past the threshold. The consequence is not that the device fails quietly: it is that the observed kill may be cavitation and acoustic streaming rather than membrane strain, which section 10 controls for with a flat surface at equal acoustic power.
* **Fatigue is the third wall.** Root strain $0.6\%$ per cycle with $1.02\times10^{13}$ cycles per day. Silicon high-cycle fatigue in humid air appears at $10^{11}$ to $10^{12}$ cycles, which at this frequency is 14 to 140 minutes of operation, not 30 days. A 30-day test accumulates $3.1\times10^{14}$ cycles, roughly 300 times beyond the best characterised silicon fatigue life, and every cycle is in liquid.
* **Frequency tolerance.** $f_0 \propto d/L^2$, so a $2.5\%$ diameter error and a $1\%$ height error give a $3.2\%$ frequency spread. The 3 dB band is $f_0/Q = \pm 6.3\%$, so electron-beam lithography at $\pm 5\text{ nm}$ keeps $>95\%$ of the array inside the band. A wet etch with $\pm 5\%$ diameter error gives a $5\%$ spread and only about half the array driven near resonance, which halves the effective amplitude over the area.
* **Added mass.** The water column a $200\text{ nm}$ pillar drags is $\rho_w (\pi d^2/4)L = 3.14\times10^{-17}\ \mathrm{kg}$, $43\%$ of the pillar mass, so $m_{eff} = 1.05\times10^{-16}\ \mathrm{kg}$ and $f_0$ falls from $118$ to $99\ \mathrm{MHz}$. The drive must track the loaded frequency, not the vacuum one.
* **Reach.** A $1\ \mu\mathrm{m}$ pillar cannot touch a cell inside a biofilm $10$ to $100\ \mu\mathrm{m}$ thick. The device only works as a colonisation-prevention surface for the first arriving cells, before a conditioning film forms.
* **Turgor dominates tension.** The Laplace pressure of the imposed membrane tension is $2\tau_m/R_b = 2(10^{-3})/(0.5\times10^{-6}) = 4\ \mathrm{kPa}$, against a staphylococcal turgor of $0.1$ to $2\ \mathrm{MPa}$. The pillar does not inflate the cell; the kill is bending-driven pore nucleation at constant area, not a tension excursion.

## 9. Contradiction ledger

* **The selectivity is a factor of 10, and the way it is used is a factor of 2.** The strain ratio $R_m/R_b = 10$ is real, but the thresholds that must be separated are closer than the ratio: bacterial rupture at 3 to 5% against fibroblast lysis at 8 to 10% is a factor of 2 to 3, so the usable displacement window is set by the thresholds, not by the size ratio. The window is $u \in [15, 40]\ \mathrm{nm}$ by the lysis criterion, a factor of 2.7, and the whole of it sits inside the fabrication tolerance of the pillar diameter ($k \propto d^4$, so $5\%$ diameter error is $22\%$ stiffness and $11\%$ amplitude at fixed drive). The operating window is narrow in the only coordinate that matters, which is displacement.
* **The energy argument does not support selectivity at all.** Section 7(g): a coccus and a fibroblast absorb the same $5.0\times10^{-16}\ \mathrm{J}$. The selectivity is a threshold effect on a shared dose, so any cell that is small for its type (a $4\ \mu\mathrm{m}$ lymphocyte, a $2\ \mu\mathrm{m}$ platelet, a $3\ \mu\mathrm{m}$ sperm cell) is inside the kill window at $65$ to $100\%$ strain-equivalent of the bacterial value. The vector is a surface that must never contact a small human cell, which excludes most of the bloodstream and all of the reproductive tract.
* **Bacteria are known to adapt to mechano-bactericidal topography, and the adaptation is measured, not hypothetical.** Two routes are reported: shedding of matrix that redistributes contact over many pillars instead of a few, and a change in cell size and turgor. Shedding is the real threat, because a $100\text{ nm}$ exopolysaccharide layer spreads the $20\text{ nm}$ displacement across $10$ to $20$ pillars and cuts the membrane strain by an order of magnitude, which erases the 10x selectivity completely. Size change cuts the other way (a cell shrinking from $1.0$ to $0.65\ \mu\mathrm{m}$ raises $\epsilon$ by $54\%$), so the adaptation that hurts is the matrix, and the day-30 survival plateau, not the day-30 survival rise, is what will actually be observed. The 10x kill condition in section 3 is set against the wrong failure mode as a result: matrix shedding produces a $2$ to $5\times$ loss, which passes the test while destroying the mechanism's margin.
* **$Q \approx 8$ in liquid, not 1000.** The drive amplitude that the piezo must supply is $Q$ times the static force budget, not smaller: at $Q = 8$ the force for $20\text{ nm}$ is $ku/Q = 40(2\times10^{-8})/8 = 1.0\times10^{-7}\ \mathrm{N}$ per pillar, or $62\ \mathrm{kPa}$ over the array, which a $100\ \mu\mathrm{m}$ PZT plate can produce at $20$ to $50\ \mathrm{V}$. That part closes. What does not close is the dissipated power, $464\ \mathrm{W/cm^2}$, and the 220 bar radiated pressure, both of which are consequences of $20\text{ nm}$ at $118\ \mathrm{MHz}$ and both of which are independent of $Q$.
* **A single-use device that fouls in hours.** A confluent monolayer of $10^{8}$ cocci per $\mathrm{cm^2}$, each $0.5\ \mu\mathrm{m^3}$ in volume, deposits $0.5\ \mu\mathrm{m}$ of cell mass over the surface, burying half of every $1\ \mu\mathrm{m}$ pillar. Dead cells and matrix then fill the $400\text{ nm}$ gaps, the pillars are mechanically shorted by the debris, and the resonance is damped to $Q < 1$. Functional life is one or two colonisation cycles, not one device life, and the array cannot be cleaned because cleaning destroys the $200\text{ nm}$ features.
* **Triviality check (strongest attack).** Mechano-bactericidal pillar arrays are published and commercialised, and the load-bearing new claim is only that resonance supplies the displacement. If the kill at $20\text{ nm}$ static equals the kill at $20\text{ nm}$ resonant, the vector is ordinary topography and its entire cost is unjustified. That is exactly why the third kill condition and the 1 Hz control exist, and it is the measurement most likely to end the vector.
* **Cavitation is a confound and possibly the actual mechanism.** At 220 bar radiated pressure the fluid cavitates, and cavitation alone kills bacteria by jet impingement. A device that kills by cavitation is a sonicator, not a pillar array, and its selectivity between a coccus and a fibroblast disappears because the jets do not care about $R$. The flat-surface acoustic control in section 10 is the only way to separate them, and there is a real chance it kills as well as the array does.
* **Arithmetic correction recorded.** The brief's $k = 0.040\ \mathrm{N/m}$ and $f = 3.7\ \mathrm{MHz}$ cannot both hold with $E = 170\ \mathrm{GPa}$ and $L = 1\ \mu\mathrm{m}$; section 7(e) resolves the discrepancy in favour of $k = 40.0\ \mathrm{N/m}$ and $f = 118\ \mathrm{MHz}$, which is the only set with $Q > 1$ in water. The falsification experiment is unaffected because it sweeps frequency from 60 to 160 MHz and reports the resonant peak wherever it lands.

## 10. Experiment

* **Chips.** $10\text{ mm}\times10\text{ mm}$ silicon, hexagonal pillar array, $d = 200\pm5\text{ nm}$, $L = 1.00\pm0.01\ \mu\mathrm{m}$, pitch $400\text{ nm}$, verified by scanning electron microscopy on a cleaved edge and by laser Doppler vibrometry of the first flexural mode. Four chip types from the same wafer: resonant array, flat (no pillars), $200\text{ nm}$ pitch array (halved spacing, doubles the strain at fixed $u$), and a $1\ \mu\mathrm{m}$ pitch array (halved strain). The pitch sweep separates strain from contact area and from surface chemistry.
* **Drive.** $100\ \mu\mathrm{m}$ PZT plate bonded to the back, driven 60 to 160 MHz, amplitude calibrated to $20\pm2\text{ nm}$ at the pillar tip by laser Doppler vibrometry in air and in water. A second drive channel at 1 Hz supplies the quasi-static control at the same $20\text{ nm}$.
* **Bacteriology.** *S. aureus* ATCC 29213, stationary phase, washed twice, resuspended to $10^{6}\ \mathrm{CFU/mL}$ in phosphate-buffered saline, $100\ \mu\mathrm{L}$ per chip, $2\ \mathrm{h}$ at $25\ ^\circ\mathrm{C}$ (no growth during the assay, so the measured effect is killing and not growth inhibition), 6 chips per condition. Recovery by $10\text{ min}$ sonication at $40\ \mathrm{kHz}$ in $1\ \mathrm{mL}$ PBS with $0.05\%$ Tween 20, then CFU plating.
* **Passage series.** 30 days, $10^{6}\ \mathrm{CFU}$ transferred daily to a fresh chip, $2\ \mathrm{h}$ at $6\text{ nm}$ drive, survivors carried forward. Every 3 days a full dose-response at $0$, $6$, $12$ and $20\text{ nm}$. Oxacillin MIC measured on every third passage as a chemical-resistance control, so that a genuine mechanical adaptation is distinguishable from a generic efflux or envelope change.
* **Adaptation metrics.** Mean cell diameter by scanning electron microscopy ($n = 200$ cells per timepoint), matrix thickness by wheat germ agglutinin lectin labelling and by total carbohydrate assay, turgor proxied by growth rate at $0.5$ to $2.0\ \mathrm{M}$ NaCl.
* **Cytotoxicity.** HDFa at passage 5, $2\times10^{4}$ cells per chip, $2\ \mathrm{h}$ at $37\ ^\circ\mathrm{C}$, calcein AM and propidium iodide, viability by image cytometry, $n = 500$ cells per condition, four conditions: $0$, $6$, $20$, and $40\text{ nm}$.
* **Null result, defined before the run.** Any one of: day-30 over day-1 survival ratio $> 10$; HDFa viability $< 90\%$ at $20\text{ nm}$; resonant over static kill ratio $< 2.0$.
* **What this cannot distinguish.** Strain-mediated rupture from cavitation and acoustic streaming, because both scale with amplitude; the flat-chip control at matched acoustic power is the only separator, and it is imperfect because a flat chip radiates less than a pillared one at the same displacement. It also cannot distinguish membrane rupture from cell-wall rupture, and it cannot see a viable-but-non-culturable state, which is why CFU is paired with a live/dead stain on the chip surface.

## 11. Expected observations

* **Success branch.** Day-1 kill at $20\text{ nm}$ is $3.0\pm0.5\ \log_{10}$ in $2\ \mathrm{h}$; at $12\text{ nm}$ it is $1.4\pm0.4$; at $6\text{ nm}$ it is $0.3\pm0.2$; static drive at $20\text{ nm}$ gives $\le 0.6\ \log_{10}$, so the resonant over static ratio is $\ge 4$. The $200\text{ nm}$ pitch chip beats the $400\text{ nm}$ chip by $1.5$ to $2\times$ and the $1\ \mu\mathrm{m}$ pitch chip is inert, which is the signature of a strain mechanism. Day-30 survival rises by $2$ to $5\times$ and then plateaus, with matrix thickness up $3\times$ and mean cell diameter down $20\%$; the ratio stays under $10$ and the first kill condition is not met. HDFa viability at $20\text{ nm}$ is $93\pm3\%$ and falls to $71\pm6\%$ at $40\text{ nm}$, which brackets the selectivity window from the top.
* **Failure branch.** All amplitudes within $1.5\times$ of each other, with the flat chip killing as well as the array: cavitation dominates and the pillar geometry is decoration. Or kill scales with amplitude but not with pitch, which means the mechanism is fluid shear at the pillar tips rather than membrane strain. Or day-30 survival rises $50$ to $1000\times$ with a $10\times$ matrix increase and no change in oxacillin MIC, which is a genuine heritable mechanical adaptation and kills the vector outright.

## 12. Magnitudes

* Pillar diameter, height, pitch: $200\text{ nm}$, $1.00\ \mu\mathrm{m}$, $400\text{ nm}$.
* Pillar density: $6.25\times10^{8}$ per $\mathrm{cm^2}$ ($6.25\times10^{12}$ per $\mathrm{m^2}$).
* Second moment of area: $7.85\times10^{-29}\ \mathrm{m^4}$.
* Pillar bending stiffness: $40.0\ \mathrm{N/m}$.
* Pillar mass: $7.32\times10^{-17}\ \mathrm{kg}$.
* Resonance in vacuum, in water: $118\ \mathrm{MHz}$, $99\ \mathrm{MHz}$.
* Quality factor in water: $\approx 8$; bandwidth $\pm 6.3\%$.
* Drive amplitude: $20\text{ nm}$ tip displacement, $15\ \mathrm{nm}$ for fibroblasts to stay sub-threshold.
* Coccus strain, fibroblast strain at $20\text{ nm}$: $4.0\%$, $0.40\%$.
* Bacterial rupture strain: $3$ to $5\%$; fibroblast lysis strain $8$ to $10\%$.
* Membrane energy delivered, both cell types: $5.0\times10^{-16}\ \mathrm{J}$ ($1.2\times10^{5}\ k_BT$).
* Stored elastic energy per pillar: $8.0\times10^{-15}\ \mathrm{J}$.
* Drive power at $20\text{ nm}$, $Q = 8$: $464\ \mathrm{W/cm^2}$.
* Equivalent static spring-bed pressure: 50 bar.
* Tip velocity, radiated pressure: $14.8\ \mathrm{m/s}$, 220 bar.
* Root bending strain: $0.6\%$ per cycle.
* Cycles per second, per day, per 30-day life: $1.18\times10^{8}$, $1.02\times10^{13}$, $3.1\times10^{14}$.
* Monolayer burial depth after one confluent layer: $0.5\ \mu\mathrm{m}$ of a $1\ \mu\mathrm{m}$ pillar.
* Kill at $20\text{ nm}$ resonant, $20\text{ nm}$ static, $6\text{ nm}$: $3.0$, $0.6$, $0.3\ \log_{10}$.
* Selectivity factor from size: 10. Usable displacement window: $15$ to $40\text{ nm}$, factor $2.7$.

## 13. Applications

* **Nearest term:** a $0.1\ \mathrm{mm^2}$ driven pad at the hub of a central venous catheter, the one location where a biofilm seeds the entire lumen, driven for the first 72 h after insertion when the colonising load is lowest. The power budget closes at that area and nowhere else.
* **Nearest term:** external fixation pin sleeves, where the skin interface is the infection route and the device is already single-use, already replaced, and already has a power lead.
* **Mid term:** a bench instrument for measuring single-cell rupture strain at $10^{8}$ cycles, which is a material property nobody has measured, and which the array reports directly from the amplitude at which kill begins.
* **Long horizon:** a wound dressing with a printed piezo layer, operating at $1$ to $3\ \mathrm{MHz}$ with soft polymer pillars (stiffness $10^{-3}\ \mathrm{N/m}$, power $40\ \mu\mathrm{W/cm^2}$) where the acoustic and thermal walls disappear and the fatigue wall becomes the only question.

## 14. Unresolved questions

* What is $Q$ for a $200\text{ nm}$ pillar in a $0.5\ \mu\mathrm{m}$-thick water film bounded by a cell on top and a substrate below, where the squeeze-film damping is set by the gap and not by the open fluid? The open-water estimate of 8 could be off by a factor of 5 in either direction, and the whole power budget scales with it.
* Where does the fibroblast threshold actually sit at $118\ \mathrm{MHz}$? The $8$ to $10\%$ lysis figure is from quasi-static micropipette work; at $10^{8}$ cycles the relevant damage mechanism may be fatigue of the cortex rather than a single-cycle rupture, which would move the threshold by an unknown factor in the unsafe direction.
* Can a $200\text{ nm}$ silicon pillar survive $10^{13}$ cycles in saline without a fatigue crack or a corrosion pit at the root, where the $0.6\%$ strain concentrates?
* Is the kill one event or many? A $4\%$ strain at $4\ \mathrm{ns}$ half-period may be fully relaxed by lipid flip-flop and membrane undulation on the $10\ \mu\mathrm{s}$ timescale between thermal pore nucleation attempts, in which case the $10^{8}$ cycles per second matter far less than the $10^{10}$ thermal attempts per second that already exist.
* Does a bacterium in stationary phase, with turgor near zero and a thickened envelope, have the same rupture strain as a log-phase cell? All the quoted thresholds are from log-phase cells.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 4 | 3 | 5 | 5 | 5 |

Total: 26/30.
Confidence: 52%, basis: the strain selectivity and the cantilever resonance are exact and the falsification is a 30-day passage on a chip that can be made in one lithography run, but the drive power, the 220 bar radiated pressure and the $10^{14}$-cycle fatigue budget at the working amplitude are three independent walls, and none of them is closed.

## 16. Status

Live. Three walls are recorded and none is closed: $464\ \mathrm{W/cm^2}$ of drive power at $20\text{ nm}$, 220 bar of radiated pressure at the same amplitude, and a fatigue budget of $3.1\times10^{14}$ cycles for a 30-day device. The vector survives only if the working amplitude can be reached with soft pillars at $1$ to $3\ \mathrm{MHz}$ or on a $0.1\ \mathrm{mm^2}$ area, and the experiment in section 10 is built to fail fast on all three.
