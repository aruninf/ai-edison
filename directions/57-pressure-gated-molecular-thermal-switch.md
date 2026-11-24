# Vector 57: Pressure-Gated Molecular Thermal Switch

**Status:** live
**Confidence:** 58%, basis: the free-molecular conductance of air is fixed by kinetic theory at $1.17\times10^{5}\ \mathrm{W/m^2K}$ and every number below follows from established gas constants, so the on-state is not in doubt; the load-bearing uncertainty is the mechanical support, which short-circuits the evacuated state at about $5.9\ \mathrm{W/m^2K}$ and therefore caps the switching ratio near $1.9\times10^{3}$ rather than the $10^{5}$ that the vacuum alone would allow.

## 1. Name

The Pressure-Gated Molecular Thermal Switch (A Solid-State Heat Switch Whose Off State Is Vacuum and Whose On State Is Air, With No Moving Part in the Thermal Path, and the Corollary That a Micrometre Air Gap Is a Better Thermal Interface Than a Bolted Joint)

## 2. Fundamental problem

Turn heat flow on and off between two bodies that must not be mechanically connected, must not wear, and must not conduct when off. The stripped requirement is a thermal conductance that changes by three orders of magnitude between two states, with no sliding surface, no working fluid loop, and no pump in the heat path.

## 3. Falsification statement

Two polished silicon plates, $1\ \mathrm{cm^2}$ each, separated by a $2.0 \pm 0.05\ \mu\mathrm{m}$ gap held by a $20\ \mathrm{mm}$ long, $25\ \mu\mathrm{m}$ wall stainless tube, measured on a guarded hot plate at a $5.0 \pm 0.1\ \mathrm{K}$ mean difference with the plate edges at $300\ \mathrm{K}$:

1. With air at $1.01\times10^{5}\ \mathrm{Pa}$ in the gap, the measured conductance is $\ge 8\times10^{3}\ \mathrm{W/m^2K}$.
2. With the gap at $\le 1\ \mathrm{Pa}$, the measured conductance is $\le 20\ \mathrm{W/m^2K}$.
3. The ratio of the two measurements is $\ge 400:1$.

The hypothesis is killed if the ratio is below $400:1$, because a commercial loop heat pipe with a mechanical bypass valve delivers $100:1$ and has twenty years of field reliability. A switch that cannot beat that by $4\times$ is a laboratory curiosity, not a device. The experiment measures the ratio directly rather than confirming the kinetic theory, because the theory is not the risk.

## 4. Hypothesis

Air at atmospheric pressure conducts heat across a gap by molecular collision, and once the gap is shorter than the molecular mean free path the conductance stops depending on the gap width and becomes a fixed kinetic ceiling. At $300\ \mathrm{K}$ and $1\ \mathrm{atm}$ that ceiling is $1.17\times10^{5}\ \mathrm{W/m^2K}$, reached at any gap below roughly $200\ \mathrm{nm}$, and a $2\ \mu\mathrm{m}$ gap still delivers $1.18\times10^{4}\ \mathrm{W/m^2K}$. That is $2.4\times$ a bolted aluminium joint at $1\ \mathrm{MPa}$ contact pressure. Evacuating the same gap to $1\ \mathrm{Pa}$ removes the molecular channel entirely, leaving radiation at $0.16\ \mathrm{W/m^2K}$ for low-emissivity plates. The switch is therefore a pressure valve acting on a gas, not an actuator acting on a gap, so nothing moves, nothing wears, and the gap never has to be controlled to nanometres.

## 5. Why convention is insufficient here

The near-field photonic route to the same problem is the one that gets funded, and it is the weaker channel. A $100\ \mathrm{nm}$ vacuum gap between silica surfaces at $300\ \mathrm{K}$ transfers about $6\times10^{3}\ \mathrm{W/m^2K}$ by evanescent photon tunnelling, a $10^{3}\times$ enhancement over the far-field blackbody value of $6.1\ \mathrm{W/m^2K}$. The same $100\ \mathrm{nm}$ gap filled with air conducts $8.1\times10^{4}\ \mathrm{W/m^2K}$. The photon channel is $13\times$ below the molecular channel it is competing with, and any leak that admits air destroys the photonic enhancement while simultaneously switching the device fully on. A near-field switch must therefore be packaged to a vacuum standard that its own on-state would violate.

The mechanical route is the one in commercial use. A loop heat pipe with a bypass valve gives $100:1$, and a bimetallic or shape-memory contact switch gives $20:1$ with a sliding interface that wears. Both put a moving part in the heat path, which sets a cycle life of $10^{5}$ to $10^{6}$ operations. The pressure-gated device has no part in the heat path at all: the only moving component is gas, and gas has no fatigue limit.

The third conventional option, a thermal interface material, is not a switch but is the reason the on-state number matters. Bolted bare aluminium joints at $1\ \mathrm{MPa}$ reach $5\times10^{3}\ \mathrm{W/m^2K}$; solder at a $25\ \mu\mathrm{m}$ bond line reaches $2\times10^{6}$; thermal paste at $50\ \mu\mathrm{m}$ and $3\ \mathrm{W/mK}$ reaches $6\times10^{4}$. Air at a $5\ \mu\mathrm{m}$ gap reaches $5.0\times10^{3}$, exactly the bolted joint value. The crossover is the useful number: **any air gap thinner than $5\ \mu\mathrm{m}$ conducts heat better than a bolted metal joint**, at zero contact pressure.

## 6. Mechanism

* $k_a$: thermal conductivity of air at $300\ \mathrm{K}$ ($0.0262\ \mathrm{W/(m\,K)}$). [established]
* $\lambda$: molecular mean free path of air at $300\ \mathrm{K}$, $1\ \mathrm{atm}$ ($68\ \mathrm{nm}$). [established]
* $\gamma$: ratio of specific heats for air ($1.4$). [established]
* $Pr$: Prandtl number for air ($0.71$). [established]
* $\alpha$: thermal accommodation coefficient on a clean oxide surface ($0.9$ to $1.0$). [established, surface dependent]
* $g$: temperature jump length ($112\ \mathrm{nm}$ at $1\ \mathrm{atm}$, derived below). [hypothesized]
* $d$: plate separation ($2.0\ \mu\mathrm{m}$). [assumed]
* $A$: plate area ($1\times10^{-4}\ \mathrm{m^2}$). [assumed]
* $h_{on}$: on-state conductance ($1.18\times10^{4}\ \mathrm{W/m^2K}$). [hypothesized, derived]
* $h_{off}$: off-state conductance ($6.2\ \mathrm{W/m^2K}$). [hypothesized, derived]
* $h_s$: support conductance per unit plate area. [unknown, the load-bearing number]

1. Two silicon plates are polished to $\lambda/10$ flatness over $1\ \mathrm{cm^2}$ and bonded to the ends of a thin-walled stainless tube, leaving a $2\ \mu\mathrm{m}$ gap. The tube is the only solid connection, so the plates are thermally in series with $20\ \mathrm{mm}$ of $25\ \mu\mathrm{m}$ steel.
2. Air is admitted through a microvalve. Molecules cross the gap ballistically, since $2\ \mu\mathrm{m}$ is $29\times$ the mean free path, and the conductance is set by the kinetic flux rather than by diffusion.
3. The conductance is $k_a/(d + 2g)$ with $g = 112\ \mathrm{nm}$, giving $1.18\times10^{4}\ \mathrm{W/m^2K}$. Because $2g = 224\ \mathrm{nm}$ is $11\%$ of $d$, the gap is already deep into the transition regime: halving $d$ to $1\ \mu\mathrm{m}$ gains only $1.8\times$, and no gap however thin exceeds $1.17\times10^{5}$.
4. A $1\ \mathrm{mL/s}$ micro-pump evacuates the $2\ \mu\mathrm{L}$ gap volume to $1\ \mathrm{Pa}$ in about $2\ \mathrm{ms}$. The molecular channel falls to $1.2\times10^{-1}\ \mathrm{W/m^2K}$ because free-molecular conductance is linear in pressure, and radiation at $\varepsilon = 0.05$ adds $1.6\times10^{-1}$.
5. The plates are now pushed together by $1\ \mathrm{atm}$ external pressure. A $0.5\ \mathrm{mm}$ silicon plate clamped at a $10\ \mathrm{mm}$ perimeter deflects $0.57\ \mu\mathrm{m}$ at the centre, which is why the gap is specified at $2\ \mu\mathrm{m}$ and not at $1\ \mu\mathrm{m}$: the evacuated state is the loaded state.
6. The support is the floor on performance. Twenty millimetres of $25\ \mu\mathrm{m}$ stainless steel conducts $5.9\times10^{-4}\ \mathrm{W/K}$, which is $5.9\ \mathrm{W/m^2K}$ referred to the plate area. That is $37\times$ the radiation leak and it sets the off-state, so the ratio is $1.9\times10^{3}$ and not the $10^{5}$ that the gas alone would give.
7. Switching on is the reverse: a microvalve admits $2\ \mu\mathrm{L}$ of air and the conductance returns in the time it takes the gas to fill, which is microseconds.

## 7. Mathematical model

Transition-regime gas conductance between parallel plates, using the temperature jump length:

$$h_{gas}(d) = \frac{k_a}{d + 2g}, \qquad g = \frac{2-\alpha}{\alpha}\,\frac{2\gamma}{\gamma+1}\,\frac{\lambda}{Pr}$$

* $[g] = (\mathrm{dimensionless})(\mathrm{dimensionless})(\mathrm{m}) = \mathrm{m}$. Check passes.
* $[h_{gas}] = (\mathrm{W\,m^{-1}K^{-1}})/(\mathrm{m}) = \mathrm{W\,m^{-2}K^{-1}}$. Check passes.
* Evaluation of $g$ at $\alpha = 1$: $(1)(1.167)(68/0.71)\ \mathrm{nm} = 112\ \mathrm{nm}$.
* Evaluation of $h_{gas}$: $d = 2\ \mu\mathrm{m}$ gives $0.0262/(2.0\times10^{-6} + 2.24\times10^{-7}) = 1.18\times10^{4}\ \mathrm{W/m^2K}$.
* Limits: $d \to 0$ gives $1.17\times10^{5}$, the kinetic ceiling; $d = 100\ \mathrm{nm}$ gives $8.1\times10^{4}$; $d = 10\ \mu\mathrm{m}$ gives $2.56\times10^{3}$. The function is bounded above and that bound is a property of the gas, not the gap.

Free-molecular limit and its pressure scaling:

$$h_{fm} = \frac{1}{4}n\bar{v}\,c_v = \frac{p}{\sqrt{2\pi m k T}}\,\frac{c_v}{k}\,k \quad\Longrightarrow\quad h_{fm} \propto p$$

* Evaluation at $1\ \mathrm{atm}$: $n = 2.45\times10^{25}\ \mathrm{m^{-3}}$, $\bar{v} = 468\ \mathrm{m/s}$, $c_v = \tfrac{5}{2}k$, giving $1.1\times10^{5}\ \mathrm{W/m^2K}$, which agrees with the jump-length limit to $6\%$. Two independent routes to the same ceiling is the reason the on-state number is trusted.
* At $1\ \mathrm{Pa}$ the pressure ratio is $1.0\times10^{-5}$, so $h_{fm} = 1.2\times10^{-1}\ \mathrm{W/m^2K}$.

Radiation between two grey plates:

$$h_{rad} = \frac{\sigma(T_1^2+T_2^2)(T_1+T_2)}{1/\varepsilon_1 + 1/\varepsilon_2 - 1}$$

* At $300\ \mathrm{K}$ and $\varepsilon_1 = \varepsilon_2 = 0.05$: $6.12/39 = 1.57\times10^{-1}\ \mathrm{W/m^2K}$. Check passes on units of $\mathrm{W/m^2K}$.

Support leak referred to plate area:

$$h_s = \frac{k_{ss}\,2\pi r w}{L\,A}$$

* With $k_{ss} = 15\ \mathrm{W/(m\,K)}$, $r = 5\ \mathrm{mm}$, $w = 25\ \mu\mathrm{m}$, $L = 20\ \mathrm{mm}$, $A = 1\times10^{-4}\ \mathrm{m^2}$: $h_s = 15(2\pi)(5\times10^{-3})(25\times10^{-6})/(2\times10^{-2})(1\times10^{-4}) = 5.9\ \mathrm{W/m^2K}$. Check passes.
* This term, not the vacuum, is the binding constraint. Setting $h_s \le 1.2\ \mathrm{W/m^2K}$ for a $10^{4}:1$ ratio requires either $L = 100\ \mathrm{mm}$ or $w = 5\ \mu\mathrm{m}$, and a $5\ \mu\mathrm{m}$ wall will not survive $1\ \mathrm{atm}$ over $1\ \mathrm{cm^2}$ without buckling. The design is therefore capped at about $1.9\times10^{3}:1$ by mechanics.

Plate deflection in the evacuated state, clamped circular plate:

$$\delta = \frac{p a^4}{64 D}, \qquad D = \frac{E t^3}{12(1-\nu^2)}$$

* $D = 150\times10^{9}(5\times10^{-4})^3/(12)(0.91) = 1.72\ \mathrm{Pa\,m^3}$. Check: $[\mathrm{Pa}][\mathrm{m^3}] = \mathrm{N\,m}$. Passes.
* $\delta = 10^{5}(5\times10^{-3})^4/(64)(1.72) = 5.7\times10^{-7}\ \mathrm{m}$. The $2\ \mu\mathrm{m}$ gap survives with $71\%$ clearance at the centre.

Pump work per actuation, isothermal:

$$W = p_1 V \ln\frac{p_1}{p_2} = (1.01\times10^{5})(2\times10^{-9})\ln(1.01\times10^{5}) = 2.3\times10^{-3}\ \mathrm{J}$$

* $[\mathrm{Pa\,m^3}] = \mathrm{J}$. Check passes. The switch costs $2.3\ \mathrm{mJ}$ per cycle, which is $10^{4}\times$ below the heat it gates in one second at $1\ \mathrm{W/cm^2}$.

Crossover with a bolted joint, solving $h_{gas}(d) = 5.0\times10^{3}$:

$$d_{cross} = \frac{k_a}{5000} - 2g = 5.24\ \mu\mathrm{m} - 0.224\ \mu\mathrm{m} = 5.0\ \mu\mathrm{m}$$

* Any air gap thinner than $5.0\ \mu\mathrm{m}$ outperforms a $1\ \mathrm{MPa}$ bolted aluminium joint.

## 8. Physical constraints

* The on-state is capped at $1.17\times10^{5}\ \mathrm{W/m^2K}$ at $1\ \mathrm{atm}$ and $300\ \mathrm{K}$. Raising the pressure to $10\ \mathrm{atm}$ raises the ceiling $10\times$, but the plate load rises to $100\ \mathrm{N/cm^2}$ and the deflection to $57\ \mu\mathrm{m}$, which closes any practical gap. The practical ceiling is one atmosphere.
* The off-state is capped by the support at about $5.9\ \mathrm{W/m^2K}$, so the ratio cannot exceed roughly $1.9\times10^{3}$ with a tube support. A pillar support is worse: carrying $1\ \mathrm{atm}$ at $1\ \mathrm{GPa}$ needs $0.01\%$ of the area, and a compressed silicon contact at $10^{7}\ \mathrm{W/m^2K}$ contributes $10^{3}\ \mathrm{W/m^2K}$, which is $10^{2}\times$ the radiation leak. Sparse pillars do not help, because the load sets their area fraction, not their pitch.
* Vacuum hold: $1\ \mathrm{Pa}$ in a $2\ \mu\mathrm{L}$ volume for one year requires a leak and outgassing rate below $6\times10^{-17}\ \mathrm{Pa\,m^3/s}$, which no static seal reaches. A non-evaporable getter is therefore mandatory, and $2\ \mu\mathrm{L}$ of air is $4.9\times10^{16}$ molecules, which needs about $5\ \mathrm{mg}$ of a $1\ \mathrm{m^2/g}$ porous getter per fill, regenerated at $350\ ^\circ\mathrm{C}$.
* The plates must not touch in the evacuated state. The $0.57\ \mu\mathrm{m}$ deflection is linear in $a^4/t^3$, so scaling to $4\ \mathrm{cm^2}$ doubles the span and multiplies the deflection $16\times$: the same $0.5\ \mathrm{mm}$ plate needs a $9.1\ \mu\mathrm{m}$ gap, and the on-state drops to $2.8\times10^{3}\ \mathrm{W/m^2K}$.

## 9. Contradiction ledger

1. **The near-field candidate is superseded, not killed.** Vector 46 of the 2026-11-19 log proposed a $100\ \mathrm{nm}$ near-field valve at $6\times10^{3}\ \mathrm{W/m^2K}$ with a claimed $10^{3}:1$ ratio against far-field radiation. That ratio is correct in vacuum and irrelevant in air: the molecular channel at the same $100\ \mathrm{nm}$ is $8.1\times10^{4}$, and a single pinhole switches the device fully on while destroying the enhancement. The photonic channel only wins when the gap is evacuated, and once evacuated the molecular channel is gone, so the two mechanisms cannot be combined. This vector replaces the actuator with a valve.
2. **The ratio is set by the support, not the vacuum.** Every popular account of gas-gap switches quotes the pressure ratio, which is unbounded, and omits the support. The support is a fixed $5.9\ \mathrm{W/m^2K}$ and it is the number that decides whether the device is worth building.
3. **Accommodation coefficient.** The $112\ \mathrm{nm}$ jump length assumes $\alpha = 1$. On a contaminated or adsorbed-layer surface $\alpha$ falls to $0.3$, $g$ rises to $373\ \mathrm{nm}$, and the $2\ \mu\mathrm{m}$ on-state falls to $9.5\times10^{3}$. The design survives that, but the bolted-joint crossover moves from $5.0$ to $4.5\ \mu\mathrm{m}$, so the corollary holds and the switch does not.
4. **Gas species.** The ceiling scales as $p/\sqrt{M}$ in the free-molecular regime and as $k$ in the continuum. Xenon at $1\ \mathrm{atm}$ gives $2.6\times10^{3}\ \mathrm{W/m^2K}$ at $2\ \mu\mathrm{m}$, $4.5\times$ worse than air, so a xenon-filled on-state is strictly worse. Air is the optimal on-state gas, which is convenient and not accidental.
5. **Gravity orientation.** A $2\ \mu\mathrm{m}$ gap in a horizontal orientation with a cold upper plate is stable against convection because the Rayleigh number is zero at that spacing. A vertical orientation with a $10\ \mathrm{K}$ difference gives $Ra = g\beta\Delta T d^3/(\nu\alpha) = 8\times10^{-9}$, still far below the $1708$ onset. Convection is not a failure mode at this scale, and that is a property of the gap, not of the device.
6. **The corollary is not free.** A $1\ \mu\mathrm{m}$ air gap beats a bolted joint only if both surfaces are flat to better than $1\ \mu\mathrm{m}$ over the contact area. Real machined surfaces are flat to $5$ to $20\ \mu\mathrm{m}$, which is why the corollary is a statement about polished silicon and not about ordinary hardware.

## 10. Experiment

Two $10\ \mathrm{mm}$ diameter, $0.5\ \mathrm{mm}$ thick silicon wafers, polished to $< \lambda/10$ over the central $8\ \mathrm{mm}$, sputter-coated with $100\ \mathrm{nm}$ of gold on the outer faces for isothermal boundary conditions and left bare on the inner faces. A $2.0\ \mu\mathrm{m}$ layer of thermal oxide is grown on one wafer and patterned into a $200\ \mu\mathrm{m}$ wide perimeter ring, then etched back so the ring is the only spacer; the ring is the bond line and the gap is set by the oxide thickness. The pair is anodically bonded at $400\ ^\circ\mathrm{C}$ and $1\ \mathrm{kV}$ to a $20\ \mathrm{mm}$ length of $25\ \mu\mathrm{m}$ wall stainless tube with a $1\ \mathrm{mm}$ bore, and the tube is connected to a turbomolecular pump through a leak valve and a $1\ \mathrm{Pa}$ capacitive gauge.

Metrology: a guarded hot plate with a $25\ \mathrm{mm}$ copper reference block on each side, two $1\ \mathrm{k\Omega}$ platinum sensors in each block, and a $5.0 \pm 0.1\ \mathrm{K}$ difference held by a Peltier on one side. The heat flux is measured by the reference block gradient, calibrated against a $10\ \mathrm{mm}$ sample of known $k$ (borosilicate, $1.14\ \mathrm{W/mK}$) in the same stack. Edge losses are bounded by running the stack at three gap pressures and extrapolating to zero flux, and by a finite-element model of the tube.

Sequence: pump to $1\ \mathrm{Pa}$, hold $1\ \mathrm{h}$, measure; admit air to $1.01\times10^{5}\ \mathrm{Pa}$, hold $10\ \mathrm{min}$, measure; repeat five times. The null result is a ratio below $400:1$, or an on-state below $8\times10^{3}\ \mathrm{W/m^2K}$, either of which kills the switch.

What the experiment cannot distinguish: it cannot separate the support leak from the radiation leak, because both are present in the evacuated state and both are below the measurement noise at $20\ \mathrm{W/m^2K}$. It also cannot test cycle life, since a single bonded pair gives one vacuum cycle; a $10^{4}$ cycle test requires a microvalve and a getter, which is a second-generation device.

## 11. Expected observations

Success branch: on-state $1.1$ to $1.3\times10^{4}\ \mathrm{W/m^2K}$, off-state $5$ to $15\ \mathrm{W/m^2K}$, ratio $1.2\times10^{3}:1$ to $2.6\times10^{3}:1$, on-state independent of pressure above $10^{4}\ \mathrm{Pa}$ (the free-molecular signature), and a linear on-state in pressure between $10^{2}$ and $10^{4}\ \mathrm{Pa}$ with slope $1.2\times10^{-1}\ \mathrm{W/m^2K}$ per pascal. The linear region is the fingerprint: a diffusive leak would give a constant conductance, a molecular channel gives a slope.

Failure branch: on-state below $8\times10^{3}\ \mathrm{W/m^2K}$ with a slope below $10^{-1}$ per pascal, which means the plates are touching at the centre or the accommodation coefficient is far below $1$; or an off-state above $20\ \mathrm{W/m^2K}$ with no pressure dependence, which means the support or the bond line dominates and the device is a resistor with a valve attached.

## 12. Magnitudes

| Quantity | Value | Basis |
| :--- | :--- | :--- |
| Kinetic ceiling, air, $1\ \mathrm{atm}$, $300\ \mathrm{K}$ | $1.17\times10^{5}\ \mathrm{W/m^2K}$ | jump length and free-molecular flux agree to $6\%$ |
| On-state, $2\ \mu\mathrm{m}$ gap | $1.18\times10^{4}\ \mathrm{W/m^2K}$ | $k_a/(d+2g)$ |
| On-state, $100\ \mathrm{nm}$ gap | $8.1\times10^{4}\ \mathrm{W/m^2K}$ | same |
| Off-state, $1\ \mathrm{Pa}$, $\varepsilon=0.05$ | $6.2\ \mathrm{W/m^2K}$ | gas $0.12$ + rad $0.16$ + support $5.9$ |
| Switching ratio | $1.9\times10^{3}:1$ | support limited |
| Support leak, $20\ \mathrm{mm}$ tube, $25\ \mu\mathrm{m}$ wall | $5.9\ \mathrm{W/m^2K}$ | stainless at $15\ \mathrm{W/mK}$ |
| Pump work per actuation, $2\ \mu\mathrm{L}$ | $2.3\ \mathrm{mJ}$ | isothermal $pV\ln$ |
| Plate deflection, evacuated, $0.5\ \mathrm{mm}$ Si | $0.57\ \mu\mathrm{m}$ | clamped plate |
| Air gap equal to a bolted joint | $5.0\ \mu\mathrm{m}$ | $5\times10^{3}\ \mathrm{W/m^2K}$ |
| Near-field photon channel, $100\ \mathrm{nm}$ vacuum | $6\times10^{3}\ \mathrm{W/m^2K}$ | log figure, $13\times$ below air |
| Thermal paste, $50\ \mu\mathrm{m}$, $k=3$ | $6\times10^{4}\ \mathrm{W/m^2K}$ | $k/d$ |
| Solder, $25\ \mu\mathrm{m}$, $k=50$ | $2\times10^{6}\ \mathrm{W/m^2K}$ | $k/d$ |
| Getter mass per air fill | $5\ \mathrm{mg}$ | $4.9\times10^{16}$ molecules, $1\ \mathrm{m^2/g}$ |

## 13. Applications

* **Battery thermal management without a coolant loop.** A pack that must be heated to $> 5\ ^\circ\mathrm{C}$ before fast charging and cooled to $< 35\ ^\circ\mathrm{C}$ during it can switch between an insulated state and a radiator with $1.9\times10^{3}:1$ and no valve in the coolant path, so there is no coolant to leak and no pump to run in the cold state.
* **Pressureless thermal interface for stacked cells and power modules.** The corollary alone is useful: a $1\ \mu\mathrm{m}$ air gap at $2.1\times10^{4}\ \mathrm{W/m^2K}$ beats a bolted joint at $5\times10^{3}$ without the $1\ \mathrm{MPa}$ clamp that damages pouch cells and ceramics.
* **Spacecraft radiator shutters.** Variable-emittance and louvre radiators are mechanical; a gas-gap panel has no hinge, no debris risk, and $10^{3}:1$ turndown at $3\ \mathrm{mJ}$ per command.
* **Cryocooler and adiabatic demagnetisation stages.** Gas-gap switches are standard below $10\ \mathrm{K}$; the room-temperature version is the same physics with air instead of helium and a micrometre gap instead of a millimetre one.
* **Building envelope.** A wall panel whose U-value changes by $10^{3}$ between day and night, actuated by a $1\ \mathrm{mL}$ pump, is the same device with a $1\ \mathrm{mm}$ gap and a $10\ \mathrm{m^2}$ area.

## 14. Unresolved questions

* What is the real contact and support conductance of an anodically bonded silicon-to-stainless joint at $1\ \mathrm{atm}$ load? The $5.9\ \mathrm{W/m^2K}$ figure is a bulk estimate and ignores the bond line, which may dominate by $10\times$.
* Does the $2\ \mu\mathrm{m}$ oxide ring survive $10^{4}$ pressure cycles without cracking at the silicon/oxide step?
* Can a microvalve and a getter be co-packaged in $2\ \mu\mathrm{L}$ without adding more conductance than the gas they control?
* How much does water adsorption on the bare silicon inner faces change the accommodation coefficient over a year at $50\%$ relative humidity? A monolayer changes $\alpha$ from $1$ to $0.3$ and costs $22\%$ of the on-state.
* Is the $5\ \mu\mathrm{m}$ bolted-joint crossover a real, reproducible number or a folklore figure? It is the single most quotable number in this dossier and it rests on a handbook range of $1$ to $5\times10^{3}\ \mathrm{W/m^2K}$.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 5 | 4 | 5 | 3 | 5 |

Total: 26/30.
Confidence: 58%, basis: the gas conductance is exact kinetic theory with two independent derivations agreeing to $6\%$, so the on-state cannot be wrong by more than the accommodation coefficient; the switching ratio is set by a support estimate that has not been measured and could be $10\times$ worse, which is why the claim is $1.9\times10^{3}$ and not $10^{5}$.

## 16. Status

Live. Wounded on one number: the $1.9\times10^{3}$ ratio is a bulk support estimate, and a bond-line measurement could reduce it to $10^{2}$, at which point the device only ties a loop heat pipe and the case rests entirely on the wear-free argument.
