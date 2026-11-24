# Vector 60: Magnetic Scale Prevention

**Status:** dead
**Confidence:** 3%, basis: the magnetic energy of a calcium ion at 1.2 T is 3.4×10⁻⁴ eV against a thermal energy of 2.59×10⁻² eV, so a static field perturbs the ion by 1.3% of $kT$ while the hydration barrier it would have to cross is 152 $kT$; and the claim of a memory effect needs a structural imprint to survive 10¹⁴ rotational correlation times of water, which no measured relaxation time allows.

## 1. Name

Magnetic Scale Prevention (Dead Hypothesis: A Static Field as a Nucleation Template and a Water Memory)

## 2. Fundamental problem

Stop calcium carbonate from depositing on a heat exchanger surface without adding chemicals, without consuming power, and without a replaceable element. The claimed device is a pair of permanent magnets clamped to the outside of a pipe, sold for household and laundry use, with the claim that the water leaving the device deposits its scale as a loose suspension instead of a hard film.

The stripped requirement is a change in the nucleation or attachment of CaCO3 at a perturbation that costs nothing to apply. That is a legitimate requirement; the question is whether a static magnetic field can supply the perturbation.

## 3. Falsification statement

Twenty identical once-through scaling rigs: a 6 mm bore copper tube, 300 mm long, with a 1.0 kW cartridge heater giving a 20 K wall superheat, fed from the same 200 L reservoir of 300 mg/L CaCO3 hardness at 60 °C, 1.0 L/min, for 30 days. Ten rigs carry a 1.2 T NdFeB Halbach array on the inlet; ten carry an identical painted aluminium dummy of the same mass and dimensions. Scale mass is measured by weighing the tube before and after, with the deposit dissolved in 5% acetic acid and titrated.

1. The mean scale mass of the magnet group differs from the dummy group by $\ge 30\%$.
2. The difference is stable across two independent 30-day campaigns with fresh tubes.
3. A "memory" test at 0, 10, 60, and 600 s after the field shows the same effect.

The hypothesis is killed if the difference is below 10%, because that is the resolution of the gravimetric method at the deposit masses involved and a device that cannot clear its own measurement noise has no effect to sell. The published claims are 50 to 90% reduction, so a $30\%$ detection threshold is generous to the claim, not to the kill.

## 4. Hypothesis

A static magnetic field of 1 to 2 T polarises the dissolved ions and the water, changes the crystal habit of CaCO3 from calcite to aragonite, and leaves a structural imprint in the water that persists for hours, so the scale that forms downstream is a non-adherent powder rather than a film.

The mechanism is stated here in the form the vendors state it, so that the arithmetic can address the strongest version and not a straw version. Each of the three links, polarisation, habit change, and memory, is examined separately in the model and the ledger.

## 5. Why convention is insufficient here

There is a real magnetic effect on water, and it is small. The quantum of magnetic energy is the Bohr magneton, $5.79\times10^{-5}\ \mathrm{eV/T}$, so a 1.2 T field offers $7\times10^{-5}\ \mathrm{eV}$ per spin. Thermal energy at 300 K is $2.59\times10^{-2}\ \mathrm{eV}$, which is 370 times larger. Any mechanism that needs a field to change a chemical outcome must either exploit a cooperative transition with a sharp threshold, or apply the field to a species with a large effective moment, or work on a species that is already out of equilibrium.

None of those conditions holds for the CaCO3 system. The ions are closed-shell, the water is diamagnetic with a volume susceptibility of $-9\times10^{-6}$, and the nucleation barrier is set by dehydration, not by magnetic order. The field is not zero in its effect; it is 2 to 5 orders below every barrier in the problem.

Conventional softening does work by removing the ions (ion exchange), by sequestering them (chelants), or by seeding crystallisation in a replaceable bed. All three pay a materials cost or a regeneration cost. The magnetic device claims to do the same job at zero operating cost, and the thermodynamic accounting is the reason it cannot: the field does no work on the ions, so the free energy of the system is unchanged.

## 6. Mechanism

* $B$: flux density at the pipe wall ($1.2\ \mathrm{T}$). [assumed, the strongest field a clamped permanent magnet delivers]
* $\mu_B$: Bohr magneton ($5.79\times10^{-5}\ \mathrm{eV/T}$). [established]
* $k_BT$: thermal energy at 300 K ($2.59\times10^{-2}\ \mathrm{eV}$). [established]
* $\chi_v$: volume susceptibility of water ($-9.0\times10^{-6}$). [established]
* $\mu_0$: vacuum permeability ($1.257\times10^{-6}\ \mathrm{H/m}$). [established]
* $v_m$: molecular volume of water ($3.0\times10^{-29}\ \mathrm{m^3}$). [established]
* $\mu_{eff}$: effective moment of a paramagnetic impurity, Fe$^{3+}$ ($5.9\ \mu_B$). [established]
* $\Delta G_{hyd}$: hydration free energy of Ca$^{2+}$ ($-380\ \mathrm{kJ/mol}$, $152\ k_BT$). [established]
* $v$: flow velocity ($1.0\ \mathrm{m/s}$). [assumed]
* $E$: Lorentz field ($vB$). [hypothesized, derived]
* $\sigma$: water conductivity ($0.05\ \mathrm{S/m}$). [assumed, tap water range $0.01$ to $0.1$]
* $u_{Ca}$: electrophoretic mobility of Ca$^{2+}$ ($6\times10^{-8}\ \mathrm{m^2/(V\,s)}$). [established]
* $\tau_r$: rotational correlation time of water ($2.5\ \mathrm{ps}$). [established]

1. A permanent magnet clamp produces 0.3 to 1.2 T at the pipe wall and 0.05 to 0.3 T on the axis. The water transit time through a 100 mm magnet is 0.1 s.
2. The diamagnetic energy density in the water is $u = \chi_v B^2/2\mu_0 = 3.6\ \mathrm{J/m^3}$ at 1.2 T, which is $1.1\times10^{-28}\ \mathrm{J}$ per molecule, or $6.9\times10^{-10}\ \mathrm{eV}$. The thermal energy is $2.59\times10^{-2}\ \mathrm{eV}$, so the perturbation is $2.7\times10^{-8}$ of $kT$.
3. The most favourable species is a paramagnetic iron impurity at $5.9\ \mu_B$, which gains $3.4\times10^{-4}\ \mathrm{eV}$ at 1.2 T. That is $1.3\%$ of $kT$, and it is $4.5\times10^{-4}$ of the $152\ kT$ hydration barrier that a calcium ion must cross to join a crystal.
4. The flowing water generates a Lorentz field $E = vB = 1.2\ \mathrm{V/m}$ across the pipe. The resulting ionic drift is $u_{Ca}E = 7.2\times10^{-8}\ \mathrm{m/s}$, which over the 0.1 s transit displaces a calcium ion by $7.2\ \mathrm{nm}$.
5. The current density is $j = \sigma E = 0.06\ \mathrm{A/m^2}$. Across the 6 mm bore the total ionic current is $1.7\ \mu\mathrm{A}$, which is 5 orders below the current that produces a measurable pH change by electrolysis at the same electrodes.
6. The memory claim requires the water to retain an imprint after the field. The structural correlation time of liquid water is 2.5 ps, so an orientational imprint decays by $e$ in about 10 ps. A claimed 1 h memory is $3.6\times10^{14}$ correlation times, and a claimed 24 h memory is $8.6\times10^{15}$.
7. The claim therefore fails at the first link. The second and third links are downstream of it and are not reached: if the field does not perturb the ion by more than 1.3% of $kT$ for 0.1 s, there is no habit change to remember.

## 7. Mathematical model

Diamagnetic energy density and the per-molecule share:

$$u = \frac{\chi_v B^{2}}{2\mu_0} = \frac{(9.0\times10^{-6})(1.2)^{2}}{2(1.257\times10^{-6})} = 5.2\ \mathrm{J/m^3}$$

* $[\chi_v B^2/\mu_0] = (\text{dimensionless})(\mathrm{T^2})/(\mathrm{H/m}) = \mathrm{J/m^3}$. Check passes.
* Per molecule: $u\,v_m = 5.2(3.0\times10^{-29}) = 1.6\times10^{-28}\ \mathrm{J} = 9.7\times10^{-10}\ \mathrm{eV}$.

Ratio to thermal energy:

$$\frac{u\,v_m}{k_BT} = \frac{9.7\times10^{-10}}{2.59\times10^{-2}} = 3.7\times10^{-8}$$

* Dimensionless. Check passes.
* Even the most favourable paramagnetic impurity, at $5.9\ \mu_B$, gives $5.9(5.79\times10^{-5})(1.2) = 4.1\times10^{-4}\ \mathrm{eV}$, which is $1.6\%$ of $kT$.

Ratio to the hydration barrier:

$$\frac{\mu_{eff}\mu_B B}{\Delta G_{hyd}} = \frac{4.1\times10^{-4}}{152(2.59\times10^{-2})} = \frac{4.1\times10^{-4}}{3.94} = 1.0\times10^{-4}$$

* Dimensionless. Check passes.
* The field would need $10^{4}\times$ more flux, that is 12 000 T, to reach the barrier. The strongest steady lab field is 45 T.

Lorentz drift:

$$E = vB = (1.0)(1.2) = 1.2\ \mathrm{V/m}, \qquad \Delta x = u_{Ca}Et_{transit} = (6\times10^{-8})(1.2)(0.1) = 7.2\times10^{-9}\ \mathrm{m}$$

* $[(\mathrm{m^2/(V\,s)})(\mathrm{V/m})(\mathrm{s})] = \mathrm{m}$. Check passes.
* 7.2 nm is under two Debye lengths at 300 mg/L hardness (the Debye length is $4\ \mathrm{nm}$ at $6\ \mathrm{mmol/L}$ ionic strength), so the drift is a polarisation layer and produces no separation of calcium from carbonate.

Memory persistence:

$$\frac{t_{memory}}{\tau_r} = \frac{3\,600}{2.5\times10^{-12}} = 1.4\times10^{15}$$

* Dimensionless. Check passes.
* Any structural imprint that decays on the rotational correlation time cannot survive $10^{15}$ of them.

## 8. Physical constraints

* A static field does no work on a closed-shell ion in equilibrium, so it cannot change the free energy difference between dissolved and crystalline CaCO3. It can only change the *rate* through a field-dependent prefactor, and that prefactor is at most $\exp(\mu B/kT)$, which at 1.2 T is $\exp(1.3\times10^{-2}) = 1.013$. A 1.3% rate change is unmeasurable against the 2× scatter of scaling tests.
* The strongest continuous field available outside a laboratory is 2 T, so the exponential factor cannot exceed $1.02$. The claim of a 50 to 90% effect needs a factor of 2 to 10, which needs $\mu B/kT$ of 0.7 to 2.3, which needs 100 to 400 T.
* The Lorentz effect is real and scales with $vB$, so it is largest at high flow and high field. At 5 m/s and 2 T in seawater (0.5 mS/cm... conductivity $5\ \mathrm{S/m}$), $E = 10\ \mathrm{V/m}$, $j = 50\ \mathrm{A/m^2}$, and the ionic drift is still only 60 nm in 0.02 s. It is enough to polarise an electrode, not to change a crystal habit.
* Any real effect on scale must come from something else in the device: a galvanic couple between dissimilar metals, a catalyst, or a change in the flow pattern. Where those exist, the effect is not magnetic and does not require the magnet.
* The memory claim is bounded by the water's own relaxation, not by the field. No measured property of liquid water persists for more than about 100 ps after the perturbation is removed, because hydrogen-bond rearrangement erases it.

## 9. Contradiction ledger

1. **The claim is not one claim.** It bundles scale prevention, scale removal, "softening" without ion removal, fuel saving, and improved taste. The kill above applies to the scale claim, which is the one with a physics mechanism. A device may produce a small effect by galvanic corrosion of its own housing, which introduces zinc or aluminium ions that do change the scale, and that effect is real and is not magnetic.
2. **Vendors cite a 1996 paper with a claimed 20% effect in a single blind trial.** The arithmetic above allows a 1.3% rate change at the field energies in question, so any measured 20% is either a different mechanism or a confounded trial. The paired 20-rig design in section 10 is the smallest test that separates the two.
3. **Calcite and aragonite differ in free energy by about 0.5 kJ/mol, which is 0.2 $kT$.** A field effect of 0.013 $kT$ is 1.5% of the polymorph energy difference, so it cannot select a polymorph. This is the strongest single sentence against the habit-change claim.
4. **The null result is the expected result, and that is the problem.** A device that does nothing cannot be distinguished from a device that does nothing *yet*, so the burden is on the vendor, and the test in section 10 is presented as the burden.
5. **Triviality check.** The only physically defensible version is a magnet used as a *filter* for pre-existing magnetite particles, which is real, is used in boiler plants, and is not scale prevention. Confusing the two is the origin of the product category.
6. **The harm is asymmetric.** A $50 to $500 household device that does nothing is a small fraud, but a laundromat or a boiler that relies on it and skips real softening pays for a heat exchanger, which is $10^{3}$ times the device cost. The dead entry is retained for that reason.

## 10. Experiment

Twenty rigs, identical to the falsification statement: 6 mm bore copper tube, 300 mm, 1.0 kW cartridge heater at 20 K superheat, 1.0 L/min, 300 mg/L hardness as CaCO3 from a single 200 L batch of synthetic hard water (CaCl2 and NaHCO3 in deionised water, alkalinity 150 mg/L), 60 °C bulk, 30 days. Ten rigs with a 1.2 T NdFeB Halbach array (measured at the wall with a gaussmeter, 1.15 to 1.25 T), ten with an aluminium dummy of the same mass and paint. Allocation by coin toss, recorded before the run. The operator does not know which is which; the tube labels are codes held by a third party.

Metrology: tube mass before and after, dried at 105 °C for 4 h, weighed on a 0.1 mg balance; deposit composition by dissolving in 5% acetic acid and titrating calcium by EDTA; crystal phase by X-ray diffraction on a scraped sample, reported as the calcite to aragonite ratio; photographs of the deposit at 20×.

Power: with a 15% coefficient of variation on scale mass and 10 rigs per arm, the design detects a 30% difference at 80% power and $\alpha = 0.05$. A 50% claim is detected with 5 rigs per arm, so the 20-rig design is powered for half the smallest claim.

Memory test: a second campaign with a 20 L reservoir dosed at 0, 10, 60, and 600 s after passing through the magnet, four rigs per delay, dosed by a timer valve.

Null result: a difference below 10%, or a difference that does not repeat in the second campaign, or a difference that appears in the dummy arm.

What the experiment cannot distinguish: it cannot separate a magnetic effect from a galvanic effect of the magnet housing, so the dummy is made of the same aluminium and painted the same; it cannot test a "resonant" or pulsed device, which is a different claim and would need its own arm; and it cannot rule out a small effect below 10%, which is below the noise any real installation could detect and therefore below the level any user could benefit from.

## 11. Expected observations

Success branch (which the model does not predict): a 30 to 90% reduction in the magnet arm, repeatable across campaigns, with an aragonite fraction above 50% against 5% in the dummy, and no dependence on the memory delay.

Failure branch: a difference of 0 to 10%, calcite fraction 90 to 100% in both arms, and a scale morphology that is indistinguishable at 20×. The failure branch is the prediction of sections 6 and 7.

The decisive signature is the field dependence. A real magnetic effect must scale with $B$, so a second campaign at 0.4 T should show one third of the effect if the mechanism is magnetic. A device that works equally at 0.05 T and 1.2 T is not magnetic, whatever else it is.

## 12. Magnitudes

| Quantity | Value | Basis |
| :--- | :--- | :--- |
| Magnet energy quantum | $5.79\times10^{-5}\ \mathrm{eV/T}$ | Bohr magneton |
| Field at the pipe wall | $1.2\ \mathrm{T}$ | strongest clamp |
| Diamagnetic energy, water, 1.2 T | $5.2\ \mathrm{J/m^3}$ | $\chi_vB^2/2\mu_0$ |
| Per-molecule energy | $9.7\times10^{-10}\ \mathrm{eV}$ | derived |
| Its ratio to $kT$ | $3.7\times10^{-8}$ | dimensionless |
| Paramagnetic impurity energy, 1.2 T | $4.1\times10^{-4}\ \mathrm{eV}$ | $5.9\ \mu_BB$ |
| Its ratio to $kT$ | $1.6\times10^{-2}$ | dimensionless |
| Hydration barrier of Ca$^{2+}$ | $152\ kT$ | $-380\ \mathrm{kJ/mol}$ |
| Field ratio to that barrier | $1.0\times10^{-4}$ | dimensionless |
| Field needed to reach the barrier | $1.2\times10^{4}\ \mathrm{T}$ | linear scaling |
| Rate prefactor $\exp(\mu B/kT)$ at 1.2 T | $1.013$ | $1.3\%$ |
| Lorentz field at 1 m/s | $1.2\ \mathrm{V/m}$ | $vB$ |
| Ionic drift in 0.1 s transit | $7.2\ \mathrm{nm}$ | $u_{Ca}Et$ |
| Ionic current in the bore | $1.7\ \mu\mathrm{A}$ | $\sigma E$ |
| Water rotational correlation time | $2.5\ \mathrm{ps}$ | established |
| Imprint lifetime bound | $\approx10\ \mathrm{ps}$ | $e^{-1}$ of $\tau_r$ |
| Claimed memory 1 h | $1.4\times10^{15}\ \tau_r$ | ratio |
| Calcite to aragonite free energy gap | $0.2\ kT$ | $\approx0.5\ \mathrm{kJ/mol}$ |
| Field effect as a fraction of that gap | $6.5\times10^{-3}$ | ratio |

## 13. Applications

* **The kill is the application.** The value of this entry is a paired test protocol that a water utility, a hotel, or a laundry can run in 30 days for the price of 20 tubes, so that a purchase decision stops resting on a vendor demonstration.
* **The surviving real device.** A 0.3 T magnet used as a trap for magnetite and iron bacteria in a closed loop is a filter, not a softener, and it is worth installing upstream of a plate heat exchanger where the deposit is magnetic. The distinction is in the deposit composition, which the EDTA titration in section 10 measures.
* **Teaching case.** The vector is retained as a worked example of a magnitude test: one constant (the Bohr magneton), one comparison ($kT$), and the claim is decided before any hardware is built. The same three lines kill magnetic fuel conditioning, magnetic water "activation", and the magnetic "memory" families.
* **Where a field does work on ions.** Electrodialysis, capacitive deionisation, and electrocoagulation all apply fields of 1 to 100 V/cm, which is $10^{4}$ to $10^{6}$ times the 1.2 V/m that a permanent magnet generates at 1 m/s. The ratio is the reason the industrial versions use electrodes and the household versions use magnets: the field strength differs by four to six orders.

## 14. Unresolved questions

* Is there any measured, replicated, paired trial of a commercial clamp-on device with a sham control? The literature contains single-arm before-and-after reports and vendor demonstrations, and the arithmetic says the effect should be below 2%, so a replicated 30% result would be a genuine anomaly worth its own investigation.
* Does the galvanic mechanism explain the small effects that are reported? A zinc or aluminium housing introduces 1 to 10 mg/L of metal ions over a season, which is enough to shift the scale, and that would make those devices work for a reason the vendors do not state.
* At what field and flow does the Lorentz drift become large enough to matter? The drift scales as $vB$ and the effect needs about 1 µm of separation, which needs $vB = 1.6\times10^{5}\ \mathrm{V/m}$, that is 130 000 T at 1 m/s, or 1 T at 160 km/s. Neither is available.
* Is there a cooperative magnetic transition in the CaCO3 system at any accessible field? The ions are closed-shell and the crystal is diamagnetic, so no. The question is retained because a claimed anomaly would have to come from an impurity phase, and the impurity is measurable.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 5 | 0 | 5 | 3 | 5 |

Total: 21/30.
Confidence: 3%, basis: the field energy is 1.3% of $kT$ for the most favourable species and $10^{-4}$ of the hydration barrier it must overcome, and the claimed memory needs an imprint to outlive $10^{15}$ correlation times of the solvent.

## 16. Status

Dead.

**The killing blow.** A static field of 1.2 T shifts the free energy of a calcium ion by $1.0\times10^{-4}$ of its hydration barrier, and the rate prefactor $\exp(\mu B/kT)$ is $1.013$, so the largest possible magnetic effect on nucleation is 1.3% against a measurement scatter of 10 to 20%. The polymorph gap between calcite and aragonite is $0.2\ kT$ and the field supplies $0.013\ kT$ of it, which is $6.5\%$, so it cannot select the habit. The memory claim requires the solvent to retain an imprint for $1.4\times10^{15}$ rotational correlation times, which contradicts the measured 2.5 ps relaxation of liquid water. Reaching the hydration barrier with a magnetic field needs 12 000 T, and the strongest steady field built is 45 T.

Carcass preserved. What survives is a magnet used as a trap for magnetite and iron bacteria, which is a filter and not a softener, and the paired 20-rig protocol that decides any future claim in 30 days.
