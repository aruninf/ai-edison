# Vector 52: Mesh-Pinned Ice Recrystallization Arrest

**Status:** live
**Confidence:** 55%, basis: the Gibbs-Thomson depression of a 100 nm ice pore is exactly $0.52\text{ K}$ from established constants, and the curvature-limited growth past a 20 nm neck forbids coarsening above $-2.6\ ^\circ\mathrm{C}$ outright; the unproven link is the water mobility at $-10\ ^\circ\mathrm{C}$, where the arrest becomes kinetic and requires $D_{eff} \le 4.9\times10^{-16}\ \mathrm{m^2/s}$, a value not measured for any 10% hydrogel.

## 1. Name

The Mesh-Pinned Ice Recrystallization Arrest (Geometric Cap on Ice Coarsening by a Thermoreversible Extracellular Network, Without Penetrating Cryoprotectant)

## 2. Fundamental problem

Freeze and thaw living tissue without the 2 to 4 molar dimethyl sulfoxide that is cytotoxic at body temperature, that must be removed by stepwise washing, and that still fails to protect anything thicker than a few hundred micrometres because the solute cannot diffuse in before the ice does. The stripped requirement is: hold the ice crystal population below a size at which it mechanically damages cells, during the whole warming ramp, using only material that stays outside the cells.

## 3. Falsification statement

Cryomicroscopy on a 10 $\mu$L film between glass coverslips, cooled at 1 K/min from $+5\ ^\circ\mathrm{C}$ to $-10\ ^\circ\mathrm{C}$, nucleated at $-2\ ^\circ\mathrm{C}$ with an ice-seeding needle, then held at $-10.0 \pm 0.1\ ^\circ\mathrm{C}$ for 30 min:

1. In a 10% w/v agarose gel made up in phosphate-buffered saline, the mean ice crystal diameter after the 30 min hold is $\le 150\text{ nm}$ (measured by freeze-fracture transmission electron microscopy on 200 crystals per sample, or by the width of the ice Raman band at 3100 cm$^{-1}$ if optical resolution fails).
2. In the matched saline control without agarose, the mean crystal diameter is $\ge 4\ \mu\mathrm{m}$ under the identical thermal history.
3. The ratio of control mean diameter to gel mean diameter is $\ge 2$.

The hypothesis is killed if the ratio is under 2, i.e. if the gel and the saline coarsen to within a factor of two of each other. The ratio is the whole claim: a factor of 2 is the boundary between "the mesh does something" and "the mesh is a bystander".

## 4. Hypothesis

Ice in a 100 nm pore is thermodynamically penalised. Its melting point is depressed by $\Delta T = 2\sigma v_m T_m/(L\Delta H_f) = 0.52\text{ K}$, which means an ice crystal confined to that pore is in equilibrium with the surrounding liquid at $-0.52\ ^\circ\mathrm{C}$ instead of $0.00\ ^\circ\mathrm{C}$. A crystal inside the network therefore cannot lower its free energy by growing into a neighbouring pore unless the sample is cold enough to pay the curvature cost at the neck. At a 20 nm neck the cost is 2.6 K, so anywhere above $-2.6\ ^\circ\mathrm{C}$ coarsening is forbidden rather than slow. Below that temperature the cap becomes morphological: the crystal fills its pore and has nowhere to grow without expanding the network. The crystal population is therefore pinned at the mesh scale while the sample is warm (where recrystallization does its damage), and the population is bounded by the pore volume when the sample is cold.

## 5. Why convention is insufficient here

Every working cryopreservation protocol is a solute protocol. Dimethyl sulfoxide at 10% v/v is 1.4 M; the vitrification cocktails used for oocytes and embryos run 6 to 8 M in total solute (DMSO, ethylene glycol, sucrose, Ficoll). These concentrations are required because the only way to stop ice nucleation in a cell is to raise the total solute concentration until the residual liquid is glassy at achievable cooling rates. The cost is fixed by the same concentration: 1.4 M DMSO is 10% of the water's hydrogen-bond network replaced, and it denatures proteins at a rate that gives a $>90\%$ loss of colony-forming ability in haematopoietic stem cells above 1 M if the exposure exceeds 30 min at $4\ ^\circ\mathrm{C}$.

The physical reason a solute is the only tool in use is that the classical route to ice control is thermodynamic and homogeneous: suppress the melting point everywhere at once. That route is a bulk concentration, and bulk concentration does not scale with thickness. Loading 2 M DMSO into a 1 cm tissue slab by diffusion takes

$$t_{load} = \frac{L^2}{2D_{DMSO}} = \frac{(1\times10^{-2})^2}{2(1\times10^{-9})} = 5\times10^{4}\ \mathrm{s} = 14\ \mathrm{h}$$

* $[t_{load}] = \mathrm{m^2/(m^2\,s^{-1})} = \mathrm{s}$. Check passes.

Fourteen hours at $4\ ^\circ\mathrm{C}$ in 2 M DMSO is not a survivable exposure for most tissue. Every vitrification protocol for organs is therefore a race between loading and toxicity, and the race is lost above roughly 1 mm in a few minutes.

The size argument is the second failure. Damage in frozen tissue is dominated by crystals comparable to or larger than a cell, so the damaging crystal is 5 to 50 $\mu$m. Recrystallization during warming coarsens a 5 $\mu$m population to 50 $\mu$m in minutes at $-10\ ^\circ\mathrm{C}$ to $-5\ ^\circ\mathrm{C}$. The available countermeasures are solutes (toxic), antifreeze glycoproteins (not obtainable at scale, and immunogenic in the concentrations needed), and ice-nucleating agents (which make the problem worse by starting more crystals). Nothing in the deployed set targets the crystal *size* directly without also changing the bulk chemistry. A mesh does exactly that: it is a geometry, it is extracellular, it is not consumed, and it acts on size rather than on concentration.

## 6. Mechanism

* $\sigma$: ice/water interfacial tension ($29\ \mathrm{mJ/m^2}$). [established]
* $\Delta H_f$: molar heat of fusion of ice ($6.01\times10^{3}\ \mathrm{J/mol}$). [established]
* $v_m$: molar volume of ice ($1.965\times10^{-5}\ \mathrm{m^3/mol}$). [established]
* $T_m$: bulk melting point ($273.15\ \mathrm{K}$). [established]
* $L$: pore radius of curvature of the network ($100\ \mathrm{nm}$). [assumed]
* $2L$: mesh pitch ($200\ \mathrm{nm}$). [assumed]
* $r_n$: radius of the neck between adjacent pores ($20\ \mathrm{nm}$). [assumed]
* $c_\infty$: water concentration available for transport ($5.55\times10^{4}\ \mathrm{mol/m^3}$). [established for pure water, assumed for a 10% gel]
* $D_{eff}$: effective water diffusivity through the frozen gel. [unknown, the load-bearing number]
* $\Delta T$: melting point depression in the pore ($0.52\ \mathrm{K}$). [hypothesized, derived below]

1. A 10% w/v agarose solution is warmed to $60\ ^\circ\mathrm{C}$, perfused into the tissue extracellular space, and gelled on cooling to about $35\ ^\circ\mathrm{C}$. The result is a 200 nm pitch network whose pores are water and whose strands are agarose helices; the network is continuous and entirely outside the cells.
2. On cooling, ice nucleates in the pores. The crystal cannot exceed the pore, so the population is set by the pore count: $1/(2L)^3 = 1.25\times10^{14}$ crystals per mL, against $8\times10^{9}$ per mL for a 5 $\mu$m population. The same ice is redistributed into $1.6\times10^{4}$ times as many crystals.
3. Each crystal is 100 nm, which is 200x smaller than a 20 $\mu$m cell, so it cannot puncture a membrane. The membrane area strain from an included crystal of radius $r$ in a cell of radius $R$ is $\varepsilon \approx (r/R)^2$, giving $\varepsilon = 1\times10^{-4}$ at 100 nm against $0.25$ at 5 $\mu$m: a factor of $6\times10^{6}$ in strain energy, which is the whole mechanical argument.
4. On warming from $-10\ ^\circ\mathrm{C}$, the crystals try to coarsen. Growth requires water to move from a small crystal to a large one, which requires the large one to bulge through the neck between pores. The neck radius is 20 nm, so the bulge costs a curvature penalty 5x the pore penalty, i.e. 2.6 K.
5. Above $-2.6\ ^\circ\mathrm{C}$ the available undercooling is less than 2.6 K, so the bulge is thermodynamically forbidden and coarsening stops dead. This window, from $-2.6\ ^\circ\mathrm{C}$ to the pore melting point of $-0.52\ ^\circ\mathrm{C}$, is 2.1 K wide and it sits exactly where the bulk control does its worst coarsening.
6. Below $-2.6\ ^\circ\mathrm{C}$ the arrest is morphological (the pore caps the size) plus kinetic (the water pathway through the frozen gel is restricted), and it is the kinetic part that the falsification experiment at $-10\ ^\circ\mathrm{C}$ actually tests.

## 7. Mathematical model

Gibbs-Thomson melting point depression for ice in a pore of radius of curvature $L$:

$$\Delta T = \frac{2\sigma v_m T_m}{L\,\Delta H_f}$$

* $[2\sigma v_m T_m/(L\Delta H_f)] = (\mathrm{J\,m^{-2}})(\mathrm{m^3\,mol^{-1}})(\mathrm{K})/(\mathrm{m})(\mathrm{J\,mol^{-1}}) = \mathrm{K}$. Check passes.
* Evaluation: $2(0.029)(1.965\times10^{-5})(273.15) = 3.113\times10^{-4}\ \mathrm{J\,m^2\,mol^{-1}\,K}$, divided by $(1.0\times10^{-7})(6.01\times10^{3}) = 6.01\times10^{-4}\ \mathrm{J\,m\,mol^{-1}}$, giving $0.518\ \mathrm{K}$.
* Scaling: $\Delta T \propto 1/L$, so a 20 nm neck gives $0.518\times(100/20) = 2.59\ \mathrm{K}$, and a 5 $\mu$m bulk crystal gives $0.518\times(0.1/5) = 0.0104\ \mathrm{K}$. The bulk curvature penalty is 10 mK and is invisible; the pore penalty is 0.52 K; the neck penalty is 2.6 K.

Arrest criterion. Coarsening past the mesh requires the bulge curvature at the neck, so the growth of a crystal of radius $r > L$ needs an undercooling

$$\Delta T_{needed}(r) = \frac{2\sigma v_m T_m}{r_n \Delta H_f} \approx 2.6\ \mathrm{K}$$

and the available undercooling at temperature $T$ is $T_m - T$. Arrest holds while

$$T_m - T < \frac{2\sigma v_m T_m}{r_n \Delta H_f} \quad \Longleftrightarrow \quad T > -2.59\ ^\circ\mathrm{C}$$

* Both sides in K. Check passes. At $-10\ ^\circ\mathrm{C}$ the available 9.5 K exceeds the 2.6 K penalty by 3.7x, so the thermodynamic cap is inactive and only the kinetics remain. At $-3\ ^\circ\mathrm{C}$ the available 2.5 K is below the penalty and the cap is absolute. The window of absolute protection is 2.1 K wide.

Ripening rate. Water moves to the crystal through a shell of thickness of order $r$; the flux is diffusion-limited, so

$$\frac{dr}{dt} = \frac{D_{eff} v_m \Delta c}{r}, \qquad \Delta c = c_\infty \frac{2\sigma v_m}{R T r}$$

$$\frac{dr}{dt} = \frac{2 D_{eff}\sigma v_m^2 c_\infty}{R T r^2} \equiv \frac{K_{rip}}{r^2}$$

* $\Delta c/c_\infty$: $(\mathrm{J\,m^{-2}})(\mathrm{m^3\,mol^{-1}})/((\mathrm{J\,mol^{-1}K^{-1}})(\mathrm{K})(\mathrm{m}))$ dimensionless. Check passes.
* $[dr/dt]$: $(\mathrm{m^2\,s^{-1}})(\mathrm{m^3\,mol^{-1}})(\mathrm{J\,m^{-2}})(\mathrm{m^6\,mol^{-2}})(\mathrm{mol\,m^{-3}})/((\mathrm{J\,mol^{-1}K^{-1}})(\mathrm{K})(\mathrm{m^2})) = \mathrm{m/s}$. Check passes.

With $D_{eff} = 1\times10^{-13}\ \mathrm{m^2/s}$ (unfrozen water in a hydrogel at $-10\ ^\circ\mathrm{C}$) and $T = 263\ \mathrm{K}$:

$$K_{rip} = \frac{2(1\times10^{-13})(0.029)(3.861\times10^{-10})(5.55\times10^{4})}{8.314(263)} = 5.69\times10^{-23}\ \mathrm{m^3/s}$$

* At $r = 100\text{ nm}$: $\dot r = 5.7\times10^{-9}\ \mathrm{m/s}$, so the crystal doubles in 18 s.
* At $r = 5\ \mu\mathrm{m}$: $\dot r = 2.3\times10^{-12}\ \mathrm{m/s}$, so the crystal doubles in 25 days.
* The ratio is $(5000/100)^2 = 2500$, which is the pinned rate figure.

Note the direction of that ratio. The 100 nm population ripens 2500x *faster* than the 5 $\mu$m population at equal $D_{eff}$, because $\dot r \propto r^{-2}$. Small crystals are the fast ones. The mesh therefore cannot buy protection from crystal size alone; it buys it from the cap on $r$ (nothing can grow past $L$) and from the reduction of $D_{eff}$ that the network and the frozen state impose. The 2500x is a handicap the pinned population pays, and the protection must be large enough to overcome it. That gives a hard requirement rather than a prediction:

$$D_{eff} \le \frac{\dot r_{max} R T r^2}{2\sigma v_m^2 c_\infty} = \frac{(2.78\times10^{-11})(8.314)(263)(1\times10^{-14})}{2(0.029)(3.861\times10^{-10})(5.55\times10^{4})} = 4.9\times10^{-16}\ \mathrm{m^2/s}$$

* $[\dot r R T r^2/(\sigma v_m^2 c_\infty)] = (\mathrm{m\,s^{-1}})(\mathrm{J\,mol^{-1}K^{-1}})(\mathrm{K})(\mathrm{m^2})/((\mathrm{J\,m^{-2}})(\mathrm{m^6\,mol^{-2}})(\mathrm{mol\,m^{-3}})) = \mathrm{m^2/s}$. Check passes.
* The target $\dot r_{max} = 50\text{ nm}/1800\text{ s} = 2.78\times10^{-11}\ \mathrm{m/s}$ is the falsification threshold expressed as a rate.

So the design needs three orders of magnitude of water-mobility reduction relative to a hydrogel ($10^{-13}$ to $5\times10^{-16}$), and that reduction must come from the frozen state, not from the agarose.

Crystal population and coverage. One crystal per pore:

$$N_{xtal} = \frac{1}{(2L)^3} = \frac{1}{(2\times10^{-7})^3} = 1.25\times10^{14}\ \mathrm{mL^{-1}}$$

* $[N] = \mathrm{m^{-3}}$, converted at $10^{6}\ \mathrm{cm^3/m^3}$. Check passes. The bulk 5 $\mu$m control carries $1/(5\times10^{-6})^3 = 8\times10^{9}\ \mathrm{mL^{-1}}$, a ratio of $1.6\times10^{4}$, which is the same ice volume redistributed.

Membrane strain. Area strain from an included crystal:

$$\varepsilon = \left(\frac{r}{R}\right)^2, \qquad U = \frac{1}{2}K_A\varepsilon^2$$

* $\varepsilon$ dimensionless; $[U] = (\mathrm{J\,m^{-2}})$. Check passes. With $K_A = 0.2\ \mathrm{J/m^2}$: at $r = 5\ \mu\mathrm{m}$, $R = 10\ \mu\mathrm{m}$, $\varepsilon = 0.25$ and $U = 6.3\times10^{-3}\ \mathrm{J/m^2}$, which is 63% of the $10^{-2}\ \mathrm{J/m^2}$ lysis energy. At $r = 100\text{ nm}$, $\varepsilon = 1\times10^{-4}$ and $U = 1\times10^{-9}\ \mathrm{J/m^2}$, which is $10^{-7}$ of lysis. The mesh moves the crystal from the edge of lysis to seven orders below it.

## 8. Physical constraints

* Mesh size is a hard ceiling on the benefit but also on the ice. At 100 nm the depression is 0.52 K and the pore holds an ice crystal of volume $\frac{4}{3}\pi(10^{-7})^3 = 4.2\times10^{-21}\ \mathrm{m^3}$. A 10% agarose gel holds about 0.9 mL water per mL, so the ice volume fraction at $-10\ ^\circ\mathrm{C}$ (about 90% of water frozen) is 0.81, and the pore is nearly full. There is no headroom for the crystal to grow inside the pore, which is the point, but it also means the network is under 5.8 bar of crystallisation pressure ($2\sigma/L = 5.8\times10^{5}\ \mathrm{Pa}$) at every pore. A 10% agarose gel has a compressive modulus of about 10 kPa, so the network is deformed by a factor of 58 and the mesh pitch is not 200 nm under load. The mesh must be crosslinked to above 1 MPa, or the geometry is nominal only.
* Neck radius must be small. The 2.1 K protection window exists only because the neck is 20 nm. A network with no neck constriction (a sponge, a foam with open windows) has $r_n \approx L$ and the window collapses to the 0.52 K pore depression, which is inside the noise of a cryomicroscope stage. The neck is the mechanism.
* Intracellular ice is not addressed. The gel is extracellular, and the cell interior is unmeshed. A cell cooled at 1 K/min dehydrates and survives the ice; a cell cooled at 100 K/min supercools and freezes internally, and the internal crystals are unpinned and 1 to 10 $\mu$m. The gel changes nothing about that. Every tissue that this vector claims to protect still needs either a penetrating agent or a cooling rate slow enough to dehydrate, and the dehydration route has its own ceiling (below).
* Solution effects ceiling. Cooling slowly enough to avoid intracellular ice concentrates the extracellular solutes. At $-20\ ^\circ\mathrm{C}$ the unfrozen water fraction in 0.15 M NaCl is about 10%, so the salt concentrates tenfold to 1.5 M and the cell shrinks to about 10% of isotonic volume, well inside the range that triggers apoptotic volume decrease. The classic two-factor wedge (fast cooling kills by intracellular ice, slow cooling kills by solution effects) is not removed by a mesh. It is narrowed, because the mesh bounds the crystal size, but the solute axis is untouched.
* Nutrient and cryoprotectant diffusion through the gel. Glucose in 10% agarose has $D \approx 4\times10^{-10}\ \mathrm{m^2/s}$, so a 1 mm slab equilibrates in $L^2/(2D) = 1250\text{ s} = 21$ min, which is acceptable, and a 1 cm slab in 35 h, which is not. The gel is therefore a device for thin tissue, cell suspensions in a thin layer, and engineered constructs, and it becomes a diffusion barrier for anything thicker than about 2 mm.
* Warming rate ceiling. If the arrest holds above $-2.6\ ^\circ\mathrm{C}$, the warming ramp through the damaging zone can be slow (1 K/min) without coarsening, which is the practical benefit: slow warming is what a large tissue can actually achieve, since its thermal diffusion length at 1 K/min is $\sqrt{4\alpha t} = \sqrt{4(1.3\times10^{-7})(300)} = 12.5\text{ mm}$. The device converts a warming-rate problem into a warming-rate irrelevance, but only inside a 2.1 K window.

## 9. Contradiction ledger

* Triviality check (strongest attack): ice recrystallization inhibition by hydrogels and polymers is measured, and the literature attributes it to adsorption of the polymer to ice faces (the antifreeze-protein-like route) at least as often as to a mesh. If adsorption is the mechanism, the mesh size is irrelevant, the effect scales with polymer concentration and not with pore geometry, and this vector is an expensive way to rediscover a known polymer effect. The discriminator is a mesh sweep at constant polymer mass: if the arrest is mesh-dependent it is geometric, if it is mesh-independent it is adsorptive. The experiment must include a 2% and a 20% agarose arm at matched total polymer.
* Intracellular ice is not addressed and still kills cells, so DMSO or a penetrating agent is still required for any cell that supercools. The honest statement of scope is that this vector replaces the *extracellular* half of the cryoprotectant burden, which is the half that sets the loading time and the osmotic shock, and leaves the intracellular half intact. For cells in suspension, where the extracellular volume is most of the sample, the saving is small. For tissue, where the extracellular space is 20% of the volume, the saving is at most 20% of the solute dose, and the toxicity reduction is proportional.
* The hydrogel is extracellular only, which is the property that makes it non-toxic and the property that makes it incomplete. A 200 nm network cannot enter a 100 nm gap junction, cannot cross a capillary wall with a 5 nm cleft, and cannot reach the cytosol. Perfusion into a tissue therefore stops at the first capillary bed, so the 12 cm depth ambition of a whole-organ protocol becomes a 100 to 500 $\mu$m penetration depth set by vessel spacing. Numbers: capillary spacing in muscle is 40 to 80 $\mu$m, so perfusion reaches about 2 to 4 cell diameters.
* The mesh must not block nutrient diffusion. At 10% w/v the agarose occupies a volume fraction of about 0.01 (agarose density 1.6 g/cm$^3$ gives 0.0625 mL polymer per mL), so the porosity is 0.94 and the tortuosity is about 1.4, which reduces $D$ by a factor 1.9 for a small solute. That is acceptable. At 20% w/v the tortuosity rises and the gel becomes a barrier for anything above 10 kDa, which excludes its use in serum-containing media without a wash step.
* The ceiling imposed by cryoprotectant-free intracellular freezing is the real bound on this vector. Without a penetrating agent the maximum cooling rate that avoids intracellular ice is roughly 1 to 10 K/min for a 10 $\mu$m cell, and at that rate the solution-effects injury at $-20\ ^\circ\mathrm{C}$ is near-lethal for most cell types. The vector can therefore claim, at best, to make the slow-cooling branch survivable by removing crystal damage, and that claim depends on the solution-effects branch being survivable, which it usually is not. The realistic target is tissue that tolerates 1.5 M solute at $-20\ ^\circ\mathrm{C}$, which is a narrow set.
* The 2500x rate figure runs the wrong way. $\dot r \propto r^{-2}$ means the pinned population is the fast one at equal $D_{eff}$, so the pinned rate reduction is not a consequence of the geometry and cannot be quoted as one. The number that survives is the requirement: $D_{eff} \le 4.9\times10^{-16}\ \mathrm{m^2/s}$ at $-10\ ^\circ\mathrm{C}$. Bulk ice self-diffusion is about $10^{-15}\ \mathrm{m^2/s}$, so the requirement is a factor of 2 below the ice lattice value, which is a very narrow margin and is the reason confidence is 55% and not 70%.
* Crystallisation pressure deforms the network. $2\sigma/L = 5.8$ bar against a 10 kPa gel modulus is a 58x overload, so the nominal 100 nm mesh closes to a smaller effective pore and the crystal is squeezed. That raises the pore depression (good) and raises the stress on any cell in contact (bad, since the cell now sees the full 5.8 bar through a thin water layer). The net mechanical effect on a cell at $-10\ ^\circ\mathrm{C}$ is not obviously favourable and is not calculable without a network model.
* Energy and entropy accounting. The mesh does no work on the ice; it raises the ice chemical potential by the curvature term, and the ice pays in surface free energy. No state is cycled, so $dS/dt \ge 0$ is trivially satisfied. The only dissipation is the water transport during any coarsening that does occur, which is the $K_{rip}$ term.

## 10. Experiment

* Samples: 10 $\mu$L films between 12 mm glass coverslips, 20 $\mu$m spacer, four arms: (a) 10% w/v low-melting agarose in phosphate-buffered saline; (b) 2% w/v agarose in PBS (mesh control at lower concentration); (c) 20% w/v agarose in PBS (adsorption control at equal mesh-relevant concentration); (d) PBS alone. Six replicates per arm.
* Thermal programme: Linkam BCS196 stage, $+5\ ^^\circ\mathrm{C}$ hold for 5 min, cool at 1 K/min to $-2.0\ ^\circ\mathrm{C}$, seed with a chilled needle, hold 2 min, cool at 1 K/min to $-10.0\ ^\circ\mathrm{C}$, hold 30 min, then warm at 1 K/min to $+5\ ^\circ\mathrm{C}$. A second programme repeats the run with the 30 min hold at $-3.0\ ^\circ\mathrm{C}$ instead of $-10.0\ ^\circ\mathrm{C}$; that arm is the one that tests the 2.1 K thermodynamic window and is the scientifically decisive condition.
* Metrology, primary: freeze-fracture replicas at the end of the hold, transmission electron microscopy at 20 000x, 200 crystals measured per sample by a thresholded particle analyser calibrated against a 200 nm polystyrene standard. Metrology, secondary: confocal reflectance microscopy through the coverslip for crystals above 500 nm, and Raman band width at 3100 cm$^{-1}$ for the sub-200 nm population.
* Calibration of the stage: a 0.1 K accuracy check against a thermocouple in a matched film, and a coarsening check against a published ice-in-sucrose standard.
* Null result (defined before the run): ratio of control mean diameter (arm d) to gel mean diameter (arm a) below 2.0 at either hold temperature.
* What this cannot distinguish: geometric pinning from polymer adsorption to ice faces. The 2% and 20% agarose arms at constant mesh are the discriminator: adsorption scales with polymer mass, pinning scales with pore size, and the two arms separate them. It also cannot distinguish a real arrest from a slowed nucleation rate, since both give small crystals at the end of the hold; the time-resolved Raman measurement over the 30 min gives the trajectory and separates them.

## 11. Expected observations

* Success branch: arm (a) at $-10\ ^\circ\mathrm{C}$ gives a mean diameter of $120 \pm 25\text{ nm}$ that is flat in time after 5 min, against $6.2 \pm 1.8\ \mu\mathrm{m}$ in arm (d): a ratio of 52. At $-3.0\ ^\circ\mathrm{C}$ arm (a) shows no measurable growth at all over 30 min, while arm (d) coarsens from 4 to 11 $\mu\mathrm{m}$, a ratio above 100. Arm (b) at 2% shows 400 to 800 nm, consistent with its larger mesh, and arm (c) at 20% shows 90 to 110 nm, a modest further improvement: geometry, not adsorption, dominates.
* Failure branch: arms (a), (b), and (c) all give 3 to 6 $\mu\mathrm{m}$, indistinguishable from arm (d) within a factor of 1.5. That means the mesh does not pin at 200 nm pitch, most likely because the crystallisation pressure has closed the pores or because the ice grows as a continuous network through the pores rather than as isolated crystals. A partial failure, with (b) at 800 nm and (a) at 150 nm, is the mesh-dependent outcome and supports the mechanism while leaving the adsorption contribution unresolved.
* Middle branch: arm (a) reaches $150\text{ nm}$ at $-10\ ^\circ\mathrm{C}$ but coarsens to $400\text{ nm}$ at $-3.0\ ^\circ\mathrm{C}$. That would say the thermodynamic window is not where the calculation puts it, and the neck radius is larger than 20 nm in the loaded state.

## 12. Magnitudes

* Ice/water interfacial tension: $29\ \mathrm{mJ/m^2}$; heat of fusion 6.01 kJ/mol; molar volume of ice $1.965\times10^{-5}\ \mathrm{m^3/mol}$; $T_m = 273.15\ \mathrm{K}$.
* Pore radius of curvature: 100 nm; mesh pitch 200 nm; neck radius 20 nm.
* Melting point depression in the pore: 0.518 K (melts at $-0.52\ ^\circ\mathrm{C}$).
* Curvature penalty at the neck: 2.59 K, which sets an absolute arrest window from $-2.59$ to $-0.52\ ^\circ\mathrm{C}$, 2.1 K wide.
* Curvature penalty at a 5 $\mu$m bulk crystal: 0.0104 K, i.e. 10 mK, invisible.
* Crystal number density: $1.25\times10^{14}$ per mL in the mesh against $8\times10^{9}$ per mL in the 5 $\mu$m control, a ratio of $1.6\times10^{4}$.
* Ripening rate at $-10\ ^\circ\mathrm{C}$, $D_{eff} = 10^{-13}\ \mathrm{m^2/s}$: 5.7 nm/s at 100 nm, 2.3 pm/s at 5 $\mu$m, ratio 2500.
* Required water diffusivity for the 150 nm falsification target: $4.9\times10^{-16}\ \mathrm{m^2/s}$, against $10^{-13}$ for unfrozen hydrogel water and $10^{-15}$ for the ice lattice.
* Crystallisation pressure in the pore: $2\sigma/L = 5.8\times10^{5}\ \mathrm{Pa}$ (5.8 bar) against a 10 kPa gel modulus, a 58x overload.
* Membrane area strain energy from a 5 $\mu$m crystal: $6.3\times10^{-3}\ \mathrm{J/m^2}$, 63% of lysis; from a 100 nm crystal: $1\times10^{-9}\ \mathrm{J/m^2}$, $10^{-7}$ of lysis.
* Crystallisation pressure energy per unit volume of ice: $P\Delta V = 5.8\times10^{5}\ \mathrm{J/m^3} = 0.58\ \mathrm{J/cm^3}$.
* Diffusion through 10% agarose: glucose $4\times10^{-10}\ \mathrm{m^2/s}$; 1 mm slab 21 min; 1 cm slab 35 h.
* Solute concentration at $-20\ ^\circ\mathrm{C}$ after 90% of water freezes: 1.5 M NaCl against 0.15 M isotonic, a tenfold concentration with cell volume at 10% of isotonic.

## 13. Applications

* Nearest-term: a cryoprotectant-sparing diluent for sperm and for zebrafish embryos, where the cell number is high, the sample is thin, and the extracellular volume dominates. Sperm tolerate 5% DMSO; an extracellular mesh that removes the crystal-damage component allows the DMSO to be cut rather than eliminated.
* Nearest-term: a slow-warming protocol for tissue-engineered constructs up to 1 mm thick, where the 21 min nutrient equilibration is acceptable and the warming rate is limited by the construct's own thermal mass.
* Long-horizon: mesh-perfused decellularised organ scaffolds, where the extracellular matrix is already a network and the added hydrogel only needs to tighten its pore size from 50 $\mu$m to 200 nm at the luminal surface.
* Long-horizon: isochoric (constant-volume) cryopreservation, where the pressure suppresses cavitation and the mesh suppresses coarsening, and the two mechanisms act on different failure modes.
* Long-horizon: a mesh-size sweep as an ice recrystallization instrument, reporting the pore radius at which arrest fails for any candidate polymer, which is a measurement product independent of the preservation claim.

## 14. Unresolved questions

* What is the effective water diffusivity in a frozen 10% agarose gel at $-10\ ^\circ\mathrm{C}$, in $\mathrm{m^2/s}$? This single number decides between arrest ($<5\times10^{-16}$) and no arrest ($>10^{-14}$), and it is measurable by pulsed-field-gradient NMR on a frozen sample.
* Does the network survive 5.8 bar of crystallisation pressure without closing, and if it closes, what is the effective pore radius under load?
* Is the neck radius in a gelled agarose network actually 20 nm, or is the network a uniform mesh with no constriction, in which case the 2.1 K window does not exist?
* How much of the observed ice recrystallization inhibition in hydrogels is geometric and how much is polymer adsorption to ice faces, and does the split depend on the polymer's hydrophobicity?
* Can the mesh be made thermoreversible in the sense required (liquid at $35\ ^\circ\mathrm{C}$ for perfusion, gelled at $20\ ^\circ\mathrm{C}$) without a sol-gel transition temperature that damages tissue on the way in?

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 5 | 4 | 5 | 4 | 5 |

Total: 26/30.
Confidence: 55%, basis: the Gibbs-Thomson arithmetic is exact from established ice constants and returns 0.52 K at 100 nm and 2.59 K at a 20 nm neck, and the neck criterion forbids coarsening above $-2.6\ ^\circ\mathrm{C}$ with no free parameters; the unproven links are the effective water mobility at $-10\ ^\circ\mathrm{C}$ and whether the inhibition is geometric or adsorptive.

## 16. Status

Live. The thermodynamic half is solid and window-limited: protection is absolute only between $-2.59$ and $-0.52\ ^\circ\mathrm{C}$, a 2.1 K band that happens to sit across the damaging part of the warming ramp. The kinetic half at $-10\ ^\circ\mathrm{C}$ requires $D_{eff} \le 4.9\times10^{-16}\ \mathrm{m^2/s}$, a factor of 2 below ice self-diffusion, which is a narrow margin and the reason confidence is 55%. The scope claim is deliberately narrowed: this is an extracellular, 1 mm-thick, slow-warming device that removes crystal damage and leaves the solute and intracellular-ice branches of the two-factor wedge intact.
