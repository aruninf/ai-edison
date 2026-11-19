# Vector 56: Hot-Carrier Extraction Beyond the Shockley-Queisser Limit

**Status:** dead
**Confidence:** 2%, basis: the failure is a conservation-law failure, not an engineering one. Charge extracted at a contact does work against that contact's potential, not against the carrier's kinetic energy, and the potential is pinned by the same Planck emission balance that produced the 33.7% limit, so excess kinetic energy is deposited in the contact as heat and no filter geometry recovers it.

## 1. Name

Hot-Carrier Extraction Beyond the Shockley-Queisser Limit (Dead Hypothesis: Energy-Selective Extraction as an Entropy-Free Sorter)

## 2. Fundamental problem

Convert one absorbed photon into more than one bandgap of electrical work in a single absorber, by collecting the photogenerated carriers before they thermalise to the lattice, so that the excess kinetic energy above the band edge is delivered to the load instead of being lost as heat.

Stripped to the bare requirement: raise the work per absorbed photon above the chemical potential that the absorption and emission equilibrium allows, which is $qV \le 1.05\ \mathrm{V}$ for a $1.34\ \mathrm{eV}$ absorber under one sun.

## 3. Falsification statement

The claim is that a hot-carrier absorber with an energy-selective contact beats the single-junction Shockley-Queisser limit of $33.7\%$ at one sun by extracting carriers inside the 1 to 10 ps thermalisation window.

**The claim is falsified by detailed balance, before any measurement.** Any energy-selective contact that accepts only carriers above the band edge must, by the same Planck emission balance that produced the original limit, re-emit at the same chemical potential, so the maximum extractable work per absorbed photon cannot exceed the chemical potential set by the absorption and emission equilibrium. Energy selectivity does not reduce the entropy of the absorbed photon distribution, which is the only route to exceeding the limit.

The mechanical reason is one sentence long: a carrier crossing a selective contact does work against the contact's potential barrier, not against its own kinetic energy. A carrier arriving with $1.90\ \mathrm{eV}$ of energy through a $1.34\ \mathrm{eV}$ barrier delivers $qV_{barrier}$ to the load and deposits the remaining $0.56\ \mathrm{eV}$ in the contact metal as heat. Raising the barrier does not help, because the barrier height is what the emission balance fixes.

**Measured form of the same statement.** A device is falsified at the moment its external electroluminescence at voltage $V$ is not enhanced by the same factor as its photocurrent, which is the Rau reciprocity test: $\phi_{EL}(V) = EQE(V)\ \phi_{bb}(V)$ must hold to within a few percent for any device whose voltage is a Fermi-level splitting and not a kinetic-energy artefact. A reported efficiency above $33.7\%$ at one sun under a calibrated AM1.5G spectrum with an independently measured EL reciprocity violation would be the only escape, and no such measurement has been reported.

## 4. Hypothesis

A semiconductor absorber with bandgap $1.34\ \mathrm{eV}$ absorbs photons at energies up to $3\ \mathrm{eV}$ and creates carriers with up to $1.7\ \mathrm{eV}$ of excess kinetic energy. Those carriers thermalise among themselves in 100 fs to a hot Fermi distribution at 1000 to 4000 K, then cool to the lattice in 1 to 10 ps by optical phonon emission. If an energy-selective contact extracts them in the first picosecond, before the phonon channel opens, the excess kinetic energy is delivered to the external circuit rather than to the lattice, and the conversion efficiency exceeds the $33.7\%$ detailed-balance limit that assumes complete thermalisation.

## 5. Why convention is insufficient here

The $33.7\%$ limit is not a material property. It is the solution of one equation: the absorbed photon flux equals the emitted photon flux plus the extracted charge flux, with the emitted flux being a Planck spectrum at the cell temperature whose chemical potential is the Fermi-level splitting $qV$. Set the current to zero and the voltage to the value that balances the two fluxes. That procedure has exactly three inputs: the solar spectrum, the bandgap, and the cell temperature. A hot-carrier device does not add a fourth input; it claims to change the second term by changing the temperature that appears in the emission spectrum of the carriers.

The reason the field believed this was open is that the thermalisation loss is enormous and visible. Of the $100\ \mathrm{mW/cm^2}$ in the AM1.5G spectrum, $33.7\ \mathrm{mW/cm^2}$ is the most a $1.34\ \mathrm{eV}$ single junction can deliver, and the difference is almost entirely carriers that arrived with excess kinetic energy and left it in the lattice. The gap looks like a loss, and a loss looks recoverable.

The reason it is not recoverable is that the loss is not a leak around the device. It is the entropy disposal channel. A photon gas at 6000 K carries $2.7\ k_B$ of entropy per photon more than it needs to deliver its energy reversibly at 300 K, and the excess kinetic energy of the photogenerated carriers is the only place that entropy can be parked while the carrier is in the absorber. Thermalising the carriers to the lattice is how the absorber rejects that entropy. A device that keeps the carriers hot has to reject the same entropy somewhere else, and the somewhere else is the contact, which is at 300 K.

The one legitimate route past $33.7\%$ is spectral, not kinetic: split the spectrum between two absorbers so that each photon is absorbed by a gap matched to its energy. That is a tandem, it reaches 42 to 45% in three-terminal and monolithic designs, and it is legitimate precisely because it reduces the entropy per absorbed photon by sorting photons, not by sorting carriers after absorption.

## 6. Mechanism

The proposed device, stated as it was specified, then the point at which the accounting breaks:

* $E_g$: absorber bandgap, $1.34\ \mathrm{eV}$. [established, the one-sun optimum]
* $T_s$: source temperature, 6000 K effective. [established]
* $T_c$: cell and contact temperature, 300 K. [established]
* $T_h$: hot carrier temperature, 1000 to 4000 K after 100 fs of carrier-carrier scattering. [hypothesized]
* $\tau_{th}$: carrier-phonon thermalisation time, 1 to 10 ps in bulk. [established]
* $\tau_{col}$: collection time through the contact and circuit, 100 ps to 1 ns. [established]
* $V$: Fermi-level splitting, the only voltage a contact can present. [established]
* $T(E)$: contact transmission probability, the energy-selective filter. [hypothesized]

1. A photon of $2.0\ \mathrm{eV}$ is absorbed, creating an electron-hole pair with $0.66\ \mathrm{eV}$ of excess kinetic energy shared between them.
2. Carrier-carrier scattering distributes that excess over the whole carrier gas in about 100 fs, producing a Fermi-Dirac distribution at $T_h$ with a single chemical potential $\mu$.
3. In 1 to 10 ps the gas cools to $T_c$ by longitudinal optical phonon emission, and the excess energy goes to the lattice.
4. The energy-selective contact is supposed to remove the carriers at step 2, transmitting only those above a threshold $E_{th} > E_g$.
5. The contact transmits with probability $T(E)$ and, by Kirchhoff reciprocity, emits with the same probability $T(E)$ into the same channels.
6. A carrier that crosses the contact emerges into a metal at $T_c$ with whatever kinetic energy it had left, and that kinetic energy is scattered into the electron gas of the metal in 10 to 100 fs. The only quantity that appears at the terminals is the electrochemical potential difference across the contact.
7. Therefore the device does work $qV$ per carrier, where $V$ is pinned by the balance of transmitted and emitted fluxes at the contact. The kinetic energy is not a term in the terminal equation at all.

The step that fails is step 4. Extraction does not preserve kinetic energy as work; it converts the carrier's electrochemical potential into work and discards the rest. The contact is not a ramp that the carrier slides down into the load. It is a barrier that the carrier climbs, and the height of the barrier is $qV$.

## 7. Mathematical model

**(a) Detailed balance at the absorber, the equation that produces the limit.**

$$J(V) = q\left[N_{abs} - N_0 \exp\left(\frac{qV}{k_BT_c}\right)\right]$$

* $[q][N] = \mathrm{C}\cdot\mathrm{m^{-2}s^{-1}} = \mathrm{A/m^2}$. Check passes.
* $N_{abs} = 2.2\times10^{21}\ \mathrm{m^{-2}s^{-1}}$ for $E_g = 1.34\ \mathrm{eV}$ under AM1.5G, i.e. $J_{sc} = 35\ \mathrm{mA/cm^2}$. [established]
* $N_0 = 6.3\times10^{3}\ \mathrm{m^{-2}s^{-1}}$ at 300 K for this gap in a $2\ \mu\mathrm{m}$ absorber, equivalent to $J_0 \approx 1\times10^{-19}\ \mathrm{A/cm^2}$, the radiative limit from $R = Bn_i^2$ with $B = 10^{-10}\ \mathrm{cm^3/s}$ and $n_i = 2\times10^{6}\ \mathrm{cm^{-3}}$. [established]

**(b) Open-circuit voltage.**

$$V_{oc} = \frac{k_BT_c}{q}\ln\frac{N_{abs}}{N_0} = 0.0259 \times \ln(3.5\times10^{17}) = 0.0259 \times 40.4 = 1.05\ \mathrm{V}$$

* $[(k_BT_c/q)] = \mathrm{V}$, times a dimensionless logarithm. Check passes.
* Concentration adds $(k_BT_c/q)\ln(X)$ with $X$ the concentration ratio: $0.0259\ln(46200) = 0.278\ \mathrm{V}$ at the $46{,}200$-sun maximum.

**(c) The limit itself.**

$$\eta_{SQ} = \frac{J_{mp}V_{mp}}{P_{in}} = \frac{(0.033)(0.96)}{0.100} = 0.337$$

* $[J V/P] = (\mathrm{A/cm^2})(\mathrm{V})/(\mathrm{W/cm^2})$, dimensionless. Check passes.
* Fill factor $0.90$ at $V_{mp} = 0.96\ \mathrm{V}$ and $J_{mp} = 33\ \mathrm{mA/cm^2}$.
* Ultimate efficiency, the same bookkeeping with emission deleted, is $44\%$ at its $1.1\ \mathrm{eV}$ optimum. [established]
* At maximum concentration (46,200 suns for a 6000 K disc), $V_{oc}$ rises by $(k_BT_c/q)\ln(46200) = 0.278\ \mathrm{V}$ and the limit becomes $40.7\%$. [established]

**(d) What an energy-selective contact can do, computed.**

A contact with transmission $T(E)$ carries

$$J = q\int T(E)\left[\Theta(E;T_s,0) - \Theta(E;T_c,qV)\right]dE$$

* $[\Theta] = \mathrm{m^{-2}s^{-1}eV^{-1}}$, times $[T]$ dimensionless and $dE$ in eV, times $q$: $\mathrm{A/m^2}$. Check passes.
* $T(E)$ appears in both terms with the same coefficient, so it cancels from the condition $J = 0$. Filtering cannot change the balancing voltage; it can only reduce the current at every voltage.

For a narrow window at $E_0$ in the Boltzmann limit, the balance reads $E_0/k_BT_s = (E_0 - qV)/k_BT_c$, so

$$qV = E_0\left(1 - \frac{T_c}{T_s}\right) = 1.34(1 - 0.05) = 1.27\ \mathrm{V}$$

* $[E_0]$ in eV times a dimensionless bracket gives V. Check passes.
* The voltage does rise, to $1.27\ \mathrm{V}$, and the current falls with the window. A window of $0.13\ \mathrm{eV}$ ($0.1\ E_0$) at the band edge passes $1.1\times10^{17}\ \mathrm{cm^{-2}s^{-1}}$, i.e. $11\ \mathrm{mA/cm^2}$, giving $11 \times 1.27 = 14\ \mathrm{mW/cm^2}$, or $14\%$. Widening the window returns the unfiltered case; narrowing it loses more current than it gains voltage. The maximum of the family is the unfiltered $33.7\%$.

**(e) The kinetic energy term, and why it never reaches the terminals.**

$$W_{term} = qV_{barrier}, \qquad Q_{contact} = (E_{carrier} - qV_{barrier})$$

* Both terms in J per carrier, hence $[W] = \mathrm{J}$. Check passes.
* For a carrier at $1.90\ \mathrm{eV}$ crossing a $1.34\ \mathrm{eV}$ barrier: $W_{term} = 1.34\ \mathrm{eV}$, $Q_{contact} = 0.56\ \mathrm{eV}$.
* At $J = 35\ \mathrm{mA/cm^2}$ the heat deposited in the contact is $0.035 \times 0.56 = 20\ \mathrm{mW/cm^2}$ against $33.7\ \mathrm{mW/cm^2}$ of electrical output, so $37\%$ of the delivered energy is dumped at the contact as heat. Raising the barrier to collect more work per carrier shrinks the current by the same Boltzmann factor that the emission balance applies, which is why the product cannot exceed $\eta_{SQ}$.

**(f) The hot-distribution variant, and where it dies.**

If the carrier gas is held at $T_h$ while the contact is at $T_c$, the balance becomes a heat engine between the two, and the idealised construction reports efficiencies up to $66\%$ at full concentration. That construction requires the extraction plane to be at $T_h$ and the contact to be at $T_c$ at the same place, which is the contradiction: the contact is a solid, it is the coldest thing the carrier touches, and it is where the work is extracted. A carrier entering the contact thermalises in 10 to 100 fs in the metal, and the barrier crossing itself, at a saturated drift velocity of $10^{7}\ \mathrm{cm/s}$ over a 10 nm barrier, takes 100 fs. Holding $T_h \ne T_c$ across a 10 nm interface at a thermal conductance of $10^{9}\ \mathrm{W\,m^{-2}K^{-1}}$ requires a heat flux of $10^{9}(2000-300) = 1.7\times10^{12}\ \mathrm{W/m^2}$, which is $1.7\times10^{8}\ \mathrm{W/cm^2}$, five orders of magnitude above the $4620\ \mathrm{W/cm^2}$ a 46,200-sun concentrator delivers.

## 8. Physical constraints

* **The extraction plane and the work plane are the same plane, and it is cold.** Work is extracted where the electrochemical potential changes, which is inside the contact, which is at $T_c$. There is no geometry in which a carrier is at $T_h$ at the point where it does work.
* **Time mismatch.** $1$ to $10\ \mathrm{ps}$ of thermalisation against $100\ \mathrm{ps}$ to $1\ \mathrm{ns}$ of collection: a factor of $10$ to $100$. To close it the absorber must be thinner than $v_{sat}\tau_{th} = 10^{7} \times 10^{-12} = 10\ \mathrm{nm}$, which is thinner than the depletion width and thinner than the absorption depth ($1/\alpha \approx 700\ \mathrm{nm}$ at $1.34\ \mathrm{eV}$), so $70\times$ of the light passes straight through.
* **Reciprocity is not negotiable at the contact.** $T(E)$ multiplies absorption and emission with one coefficient. Any contact that filters by energy filters both directions, and the balance condition $J=0$ is independent of $T(E)$.
* **Even perfect concentration gives $40.7\%$.** The one-sun limit is $33.7\%$; the maximum-concentration limit is $40.7\%$. Neither number moves under energy selectivity, and the concentration itself is bounded at $46{,}200$ suns by the angular size of the solar disc.
* **The $44\%$ ultimate efficiency is not a target.** It is the same calculation with emission deleted, and it is a violation of the second law by construction, since a cell that does not emit cannot reject entropy. It is a bookkeeping upper bound, useful for separating emission losses from transport losses, not reachable.
* **The multi-exciton route is separate and also capped.** Impact ionisation yields at most $2$ electron-hole pairs per photon above $2E_g$, best-reported external quantum yield is $1.3$ at $3E_g$, and the corresponding detailed-balance limit for a single threshold absorber with perfect multi-exciton generation is below the $40.7\%$ concentration limit once the threshold energy is accounted for. It does not rescue the kinetic-energy route.

## 9. Contradiction ledger

This section is the full ledger of the failure, not a list of open risks.

* **The killing blow, stated as an equation.** $J = q\int T(E)[\Theta(E;T_s,0) - \Theta(E;T_c,qV)]dE$. The same $T(E)$ sits in both terms. Solving $J=0$ gives a $V$ that does not contain $T(E)$. A filter can move the current down at every voltage; it cannot move the voltage at which the current vanishes. The bound is the same Planck balance that produced $33.7\%$, and it is a bound on the voltage, not on the flux.
* **The work mechanism is not the kinetic energy.** A carrier crossing an abrupt heterojunction or a resonant tunnelling barrier exchanges energy with the barrier and emerges into a metal where it is thermalised by electron-electron scattering in 10 to 100 fs. What the external circuit sees is the difference of electrochemical potentials. Excess kinetic energy becomes heat in the contact, which is measured directly: this is the hot-electron photoelectric effect, and its signature is a photocurrent that is independent of the excess energy once the barrier is cleared. No hot-carrier photovoltaic has ever shown the opposite signature.
* **Entropy bookkeeping.** The absorbed photon distribution at 6000 K has a fixed entropy per unit energy. The only ways to extract more work per photon are to reduce that entropy per unit energy (spectral splitting, i.e. tandem) or to use a colder sink (none available; the sink is 300 K). Keeping carriers hot does not reduce the entropy per absorbed photon, it only relocates where that entropy is rejected, and the rejection point is the contact.
* **The idealised $66\%$ figure and the assumption it hides.** The construction that reports $66\%$ requires a sorter with zero entropy production, zero thermal conductance and a transmission function that is energy-selective without being energy-dissipative. Transmission and emission share one coefficient, so a sorter that passes carriers must emit them with the same spectrum; the required device is a Maxwell demon that sorts by energy and rejects entropy to nothing. The concession is recorded explicitly: if such a sorter existed, this entry would be wrong. Reciprocity forbids it, and the ledger entry stands.
* **Thermalisation mismatch.** $1$ to $10\ \mathrm{ps}$ against $100\ \mathrm{ps}$ to $1\ \mathrm{ns}$, a $10$ to $100\times$ gap. The quantum-well and polaron routes extend the thermalisation time by $10$ to $100\times$ by suppressing the LO phonon bottleneck, which closes the gap on paper and does nothing for the voltage, because the voltage was never set by the thermalisation time.
* **Impact ionisation is not a counterexample.** It converts one high-energy photon into two low-energy pairs, i.e. it trades voltage for current at fixed energy, which is the same trade the filter makes and which is bounded by the same balance.
* **Concentration does not rescue it.** At the maximum $46{,}200$ suns the limit is $40.7\%$, and a real cell at that concentration is limited by series resistance and by the $4620\ \mathrm{W/cm^2}$ thermal load long before it is limited by detailed balance.
* **Why the error was attractive.** The thermalisation loss is $50$ to $60\%$ of the absorbed power at one sun, so it is the single largest term in the loss budget, and it looks like a leak rather than like the entropy exhaust. Every failed hot-carrier design in the record fails at the same place: the selective contact is a barrier, and a barrier converts potential to work and kinetic energy to heat.
* **Triviality check.** Stripped of its vocabulary, the proposal is a thermoelectric with the hot junction at the absorber and the cold junction at the contact. A thermoelectric's efficiency is bounded by the Carnot factor times the material figure of merit, and with the lattice as the cold reservoir the Carnot factor is $(2000-300)/2000 = 0.85$ only for a $2000\ \mathrm{K}$ hot junction, which no semiconductor survives. The device is a heat engine whose heat source is sunlight at $6000\ \mathrm{K}$ and whose cold source is the same $300\ \mathrm{K}$ lattice that the $33.7\%$ limit already assumes.

## 10. Experiment

The experiment that would have tested the claim, and that defines what a valid refutation would look like:

* **Device.** A $1.34\ \mathrm{eV}$ absorber (GaAs or a $1.34\ \mathrm{eV}$ InGaAsP lattice-matched to InP), $300\ \mathrm{nm}$ to $2\ \mu\mathrm{m}$ thick, with a resonant-tunnelling energy-selective contact on the electron side and a standard contact on the hole side, and a back reflector.
* **Calibration.** AM1.5G spectrum verified against a reference cell with $1\%$ spectral mismatch correction, aperture area metered, cell temperature held at $25.0\pm0.2\ ^\circ\mathrm{C}$ on a temperature-controlled stage, four-wire measurement with a source meter calibrated to $10\ \mu\mathrm{V}$.
* **The discriminating measurement is reciprocity, not efficiency.** Measure external quantum efficiency $EQE(E)$ and absolute electroluminescence $\phi_{EL}(V)$ on the same device. Rau reciprocity requires $\phi_{EL}(V) = EQE(V)\,\phi_{bb}(V)$ with $\phi_{bb}$ the blackbody flux at $300\ \mathrm{K}$. A device that delivered work from kinetic energy would violate this relation, because the extra work would not appear as an increase in the radiative chemical potential. The relation is measurable to $2$ to $3\%$ with a calibrated integrating sphere and a silicon detector of known responsivity.
* **Secondary measurement.** Photocurrent versus contact barrier height, at fixed illumination, over five barrier heights from $0.9$ to $1.5\ \mathrm{eV}$. The claim predicts photocurrent rising with excess photon energy at fixed barrier; the conventional prediction is that photocurrent saturates once $h\nu$ exceeds the barrier and is independent of $h\nu$ above it.
* **Null result, defined before the run.** Reciprocity holds within $3\%$, and photocurrent at fixed barrier is independent of $h\nu$ above the barrier within $5\%$. Both null results are the conventional prediction; the first is the one that matters, because it is the one that is impossible to fake with a hot distribution.
* **What this cannot distinguish.** It cannot separate radiative from non-radiative recombination losses, because reciprocity holds for the radiative channel only and the non-radiative channel can mask a small violation. It also cannot resolve a carrier distribution that survives for less than the $10\ \mathrm{fs}$ the measurement integrates over.

## 11. Expected observations

* **The branch the claim required.** Efficiency above $33.7\%$ at one sun, with $V_{oc}$ above $1.10\ \mathrm{V}$ at $J_{sc} = 35\ \mathrm{mA/cm^2}$, and an electroluminescence at that voltage exceeding the reciprocity prediction by the ratio of the claimed to the allowed work per photon, i.e. by $30$ to $100\%$. No such device has been reported, and the reason is not fabrication.
* **The branch that is actually observed.** $V_{oc}$ saturates at the reciprocity value, $1.05$ to $1.10\ \mathrm{V}$ for this gap, regardless of the contact design and regardless of absorber thickness between $100\ \mathrm{nm}$ and $3\ \mu\mathrm{m}$. Photocurrent is flat in photon energy above the barrier. Hot luminescence is observable as a broadening of the emission spectrum at high excitation, and it vanishes within $10\ \mathrm{ps}$ without changing the terminal voltage.
* **The measured signature of the failure.** A contact with a $0.2\ \mathrm{eV}$ barrier inserted in a $1.34\ \mathrm{eV}$ cell reduces the current by the Boltzmann factor $\exp(-0.2/0.0259) = 4\times10^{-4}$ at fixed voltage, exactly as a series barrier should, and adds no voltage. That single measurement, which takes an afternoon, contains the whole refutation.

## 12. Magnitudes

* Bandgap: $1.34\ \mathrm{eV}$, the one-sun optimum.
* One-sun input: $100\ \mathrm{mW/cm^2}$; single-junction limit $33.7\%$, i.e. $33.7\ \mathrm{mW/cm^2}$.
* Ultimate efficiency (emission deleted, $1.1\ \mathrm{eV}$ optimum): $44\%$. Not reachable; it violates the second law by construction.
* Maximum concentration: $46{,}200$ suns, $4620\ \mathrm{W/cm^2}$; limit $40.7\%$.
* Above-gap photon flux, short-circuit current: $2.2\times10^{21}\ \mathrm{m^{-2}s^{-1}}$, $35\ \mathrm{mA/cm^2}$.
* Radiative saturation current, open-circuit voltage: $1\times10^{-19}\ \mathrm{A/cm^2}$, $1.05\ \mathrm{V}$.
* Thermalisation time: $1$ to $10\ \mathrm{ps}$.
* Carrier collection time: $100\ \mathrm{ps}$ to $1\ \mathrm{ns}$.
* Mismatch between the two: $10$ to $100\times$.
* Absorber thickness that would close the mismatch at $v_{sat} = 10^{7}\ \mathrm{cm/s}$: $10\ \mathrm{nm}$; absorption depth at $1.34\ \mathrm{eV}$: $700\ \mathrm{nm}$, a $70\times$ conflict.
* Narrow-window filter at the band edge ($0.13\ \mathrm{eV}$ wide): $1.27\ \mathrm{V}$ at $11\ \mathrm{mA/cm^2}$, i.e. $14\%$. The family maximum is the unfiltered $33.7\%$.
* Excess kinetic energy per $1.90\ \mathrm{eV}$ photon: $0.56\ \mathrm{eV}$; deposited at the contact as heat at $35\ \mathrm{mA/cm^2}$: $20\ \mathrm{mW/cm^2}$, $37\%$ of the electrical output.
* Contact thermalisation time: $10$ to $100\ \mathrm{fs}$.
* Multi-exciton external quantum yield, best reported: $1.3$ at $3E_g$; cap $2.0$.
* Tandem efficiency, three-terminal or monolithic: $42$ to $45\%$. **This survives.** It is the only legitimate route past $33.7\%$, because it splits the spectrum rather than the energy of a single carrier, and its advantage comes from reducing the entropy per absorbed photon, which is the one thing energy selectivity cannot do.
* Keeping this entry rather than deleting it: the repository records what was killed and why, so that the thermalisation loss is not rediscovered as an opportunity every third year.

## 13. Applications

The hypothesis is dead. Three of its components are not, and are worth separating out:

* **Hot-carrier absorbers as thermophotovoltaic emitters.** A hot carrier gas that re-emits at $T_h$ is a useful narrowband emitter when the source is a $2000\ \mathrm{K}$ thermal emitter rather than the sun, because a thermal source has no $6000\ \mathrm{K}$ quantum and no excess kinetic energy to recover. Conversion of $2000\ \mathrm{K}$ radiation by a $0.6\ \mathrm{eV}$ cell reaches $35$ to $40\%$ of the radiated power and does not need a selective contact.
* **Hot-electron photochemistry.** The $0.56\ \mathrm{eV}$ that is a loss in a photovoltaic is a usable reduction potential in a photoelectrochemical cell, where the electron is transferred to a molecule rather than to a metal contact. The distinction is that the molecule accepts the electron at its own redox potential and the excess energy drives the reaction, so the kinetic energy is not discarded.
* **Ultrafast photodetectors.** The same $1$ to $10\ \mathrm{ps}$ thermalisation time sets the bandwidth of a hot-carrier bolometer, and $100\ \mathrm{GHz}$ detection is a real product of the physics even though the efficiency claim is not.
* **What is not an application.** Any surface that claims to convert hot carrier kinetic energy into terminal voltage. The ledger in section 9 applies to every one of them, and the reciprocity measurement in section 10 is the acceptance test.

## 14. Unresolved questions

* Is there any physical structure with a transmission function that is energy-selective and entropy-free? Reciprocity says no for a passive linear element, and the question is whether an active, driven sorter could exist that pays for its own sorting work from an external supply. If it did, it would be a refrigerator, and its own power consumption is the entry that closes the accounting.
* How far can the thermalisation time be extended? The record is $100\ \mathrm{ps}$ to $1\ \mathrm{ns}$ in strongly confined quantum wells and polaron-protected materials, which does not help the voltage but does make hot-carrier spectroscopy possible.
* Does the $1.3$ multi-exciton yield at $3E_g$ survive at the current densities a concentrator needs, where Auger recombination scales as the cube of the carrier density and would eat the gain?
* Where exactly does the work get done inside a selective contact? The macroscopic answer is "at the electrochemical potential step", but the microscopic location, whether at the barrier, in the metal, or at the interface state, is not measured, and it is not needed to kill this vector.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 5 | 0 | 2 | 5 | 4 |

Total: 20/30.
Confidence: 2%, basis: the failure is a conservation-law failure, not an engineering one. The transmission coefficient appears in absorption and emission with one value, so the balancing voltage is independent of it, and no amount of fabrication, materials work or concentration moves a bound that is set by the Planck balance itself.

## 16. Status

Dead.

**The killing blow.** Detailed balance. Any energy-selective contact that accepts only carriers above the band edge must, by the same Planck emission balance that produced the original limit, re-emit at the same chemical potential, so the maximum extractable work per absorbed photon is the chemical potential set by the absorption and emission equilibrium, not the kinetic energy the carrier arrived with. The transmission coefficient cancels from the condition $J = 0$, which is why the bound is $33.7\%$ at one sun and $40.7\%$ at maximum concentration even with a perfectly hot distribution retained at a higher temperature. Energy selectivity does not reduce the entropy of the absorbed photon distribution, and that entropy reduction is the only route past the limit. The $1\ \mathrm{ps}$ thermalisation window makes the idealised construction unreachable rather than merely hard.

Carcass preserved. The tandem is the surviving route: $42$ to $45\%$, because it splits the spectrum instead of the energy of a single carrier.

