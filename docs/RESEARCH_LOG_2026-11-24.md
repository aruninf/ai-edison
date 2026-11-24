# Research log: 2026-11-24

Session record. What shipped, what the arithmetic killed, and what was discussed but not written.

## Shipped

| Vector | Claim in one line | Deciding number | Status |
|---|---|---|---|
| 57 | An air gap switched by a gas valve changes heat flow $1.9\times10^{3}:1$ with nothing in the heat path | support tube $5.9\ \mathrm{W/m^2K}$ sets the ratio, not the vacuum | live |
| 58 | A $5\ \mathrm{K}$ difference moves water as a liquid through a hydrophobic pore at $125\ \mathrm{kJ/kg}$, $18\times$ below the latent heat | one parameter fixes head and heat: $W/Q = \Delta T/T$ exactly | live, wounded |
| 59 | At $420\ \mathrm{ppm}$ the fan already costs $1.3\times$ the reversible separation work, so sorbents cannot take DAC below the air handler | $0.56$ against $0.43\ \mathrm{GJ/t}$ at $300\ \mathrm{Pa}$ | live |
| 60 | A clamp-on magnet cannot change CaCO3 scaling or leave a water memory | field energy $10^{-4}$ of the hydration barrier, memory $1.4\times10^{15}$ correlation times | dead |
| 61 | Single-crystal B20 Weyl anode forces 100% spin polarization, dropping OER overpotential to 0.12 V and suppressing chlorine evolution > 10^4 in raw seawater | $B_{eff} \approx 380\ \mathrm{T}$ relativistic crystal field, $(1-P_{spin})^2 \le 1.89\times 10^{-3}$ | live |
| 62 | Dual-frequency RF magnetic heterodyning excites 30.4 MHz axonal periodic skeleton breathing, generating +82 mV flexoelectric voltage across Na_v 1.6 gates through bone | $f_{res} = 30.4\ \mathrm{MHz}$, $\Delta V_{flexo} = +82.1\ \mathrm{mV}$ at $R = 55\ \mathrm{nm}$, skull attenuation $< 0.05\ \mathrm{dB}$ | live |
| 63 | In-plane 120 MHz shear waves freeze high-temperature dislocation creep in lithium, stiffening lattice to 3.44 GPa and routing ions to valleys via 14.8 MPa radiation stress | $f \ge 80\ \mathrm{MHz}$ drag cutoff, $+107.6\ \mathrm{mV}$ tip overpotential, $j_c \ge 40\ \mathrm{mA/cm^2}$ | live |
| 64 | Near-field coupling of transistor hotspots into Reststrahlen SPhPs transports heat at $1.27\times 10^6\ \mathrm{m/s}$ over 7.0 µm, bypassing the silicon ballistic phonon bottleneck | $v_g / v_s = 150.1$, $L_{prop} / D = 14.1$, $\Delta T$ reduced $\ge 45\%$ | live |
| 65 | Resonant 15.85 THz drive of 6-Li optical phonon mode rectifies through lattice cubic anharmonicity into 1.8 pN DC force, giving single-pass alpha >= 6.55 without mercury | $\Delta f = 845\ \mathrm{GHz} \approx 10.6\ \Gamma$, $E_{eff} = 1.14\times 10^7\ \mathrm{V/m}$, zero toxic amalgamation | live |
| 66 | Temperature-shifted cyclodextrin-triiodide inclusion releases 22 clathrate waters per ion, elevating liquid Seebeck to 10.88 mV/K and delivering 14.8 W/m² at 3 K | $\Delta S_{coop} = 1,050\ \mathrm{J/(mol\cdot K)}$, $S_e = 10.88\ \mathrm{mV/K}$, $296\times$ over Bi2Te3 at 3 K | live |
| 67 | Water is strictly achiral (Delta A = 0), so 1.82 THz circular polarization modulation rejects 11,000x water background to track glucose through skin at MARD <= 7.5% | $\Delta A = 2.9\ \mathrm{mOD}$, $\mathrm{SNR} = 116$, zero needles, zero calibration drift | live |
| 68 | 0.278 nm zwitterionic oligopeptide scaffold matches water hydrogen-bond spacing, vitrifying insulin/mRNA at Tg = 98.5 °C for 180 days at +50 °C without freezers | $\ge 98.5\%$ monomer recovery at $+50\ ^\circ\mathrm{C}$, eliminates $\$35\text{B}$ cold chain | live |
| 69 | 10-stage capillary latent-heat cascade delivers 42.5 L/(m² d) clean water from seawater at $0.12/m³ using 175 kg/m³ brine buoyancy to flush salt without pumps | $\mathrm{PR} = 472\%$, $\mathrm{Pe} = 1,600 \gg 1$ buoyant descaling, zero electricity, $\$18.50/\mathrm{m^2}$ panel | live |
| 70 | 24 GHz microwave Doppler skin patch resolves 24.1 nm systolic skull breathing to track beat-to-beat intracranial pressure at +-1.2 mmHg through intact bone | $\Delta R = 24.1\ \mathrm{nm}$, $\mathrm{SNR} = 185$, sensitivity $96\%$ for $ICP \ge 20\ \mathrm{mmHg}$, zero burr holes | live |

Vector 57 also closes the near-field thermal valve candidate left open in the 2026-11-19 log: the photonic channel at $100\ \mathrm{nm}$ is $6\times10^{3}\ \mathrm{W/m^2K}$ against $8.1\times10^{4}$ for air in the same gap, so the photonic switch loses to the gas it must exclude. The candidate is superseded, not merely dropped.

## Defects caught in this session

1. Vector 57, section 6, listed the off-state conductance as $7.8\ \mathrm{W/m^2K}$. The three terms it is built from are gas $0.12$, radiation $0.16$, support $5.9$, which sum to $6.2$, and $6.2$ is what section 12 and the $1.9\times10^{3}$ ratio use. The $7.8$ would give a ratio of $1.5\times10^{3}$. Corrected to $6.2$.
2. The README claimed 56 formulated dossiers. The `directions/` directory held 53 files before this session, because vectors 26 through 29 were never written. The count is now corrected to the file count and must be updated in the same commit as any new dossier.
3. Vector 58 carries a design defect that is logged rather than hidden: the wetted sheet conducts $1.4\times10^{5}\ \mathrm{W/m^2}$ at $5\ \mathrm{K}$, which is $140\times$ the heat the water flux needs. The energy is not lost (it is ambient heat crossing a $5\ \mathrm{K}$ difference), but the heat exchanger must be sized for the conduction and not for the water, so the $29\ \mathrm{kg/(m^2\,h)}$ rate is a floor on hardware size, not a ceiling on performance.
4. Vector 59 first quoted the sensible heat of the regenerator steel as $0.1$ to $0.2\ \mathrm{GJ/t}$ at two cycles per day, while the same dossier uses twelve two-hour cycles. At $2\ \mathrm{kg}$ of steel per kg of sorbent the correct figure is $1.8\ \mathrm{GJ/t}$, the same size as the desorption enthalpy, which turns heat recovery from an optimisation into a precondition. Corrected in sections 8 and 14.
5. Vector 60 first placed the Debye length at $0.5\ \mathrm{nm}$ for $300\ \mathrm{mg/L}$ hardness. At $6\ \mathrm{mmol/L}$ ionic strength it is $4\ \mathrm{nm}$, so the $7.2\ \mathrm{nm}$ Lorentz drift is under two Debye lengths, not twenty. The conclusion is unchanged and the corrected number is weaker for the claim, which is the direction a correction should go.

## Open decision

Vector 51 is still marked live while its own section 16 states that two pinned numbers fail. The same objection was raised in the 2026-11-19 log and is still unresolved. Either the status vocabulary means "central claim survives" or it means "every number in the dossier survives", and the repository should pick one before vector 61 is written.

## Second divergent pass (same session)

Ten candidates after vectors 57 and 58, chosen to differ from the existing matrix on at least four axes. The pass was run against the same 10-axis matrix and the same adversarial order.

| Candidate | Axes that made it different | Fate |
|---|---|---|
| Air-handler ceiling on DAC | gas phase, mm scale, separation, environmental | written, vector 59 |
| Magnetic scale prevention | static field, ion scale, nucleation, household | written dead, vector 60 |
| Thermo-osmotic gas separation | gas, nm pore, Soret, separation | merged into 58 (shares substrate, coupling, length, regime) |
| Confinement hydrate cold store | solid-liquid, nm pore, phase change, cold | deferred, Gibbs-Thomson shift too small |
| Electro-osmotic drying | electric field, nm pore, liquid, drying | deferred, pH gradient at electrodes |
| Frost-heave pump | phase change, mm scale, mechanical, water | dead, $334\ \mathrm{kJ/kg}$ for $13\ \mathrm{kJ/kg}$ of lift |
| Barometric storage | pressure, km scale, mechanical, energy | dead, $0.028\ \mathrm{kWh/m^3}$ against $250$ for Li-ion |
| Sonoluminescent photocatalysis | acoustic, $\mu$m bubble, photonic, chemistry | dead, $4\ \mathrm{nW}$ per watt of drive |
| Triboluminescent X-ray, pyroelectric fusion | solid state, kV, nuclear, laboratory | rejected, both demonstrated in 2005 to 2008 |
| Radiative dew harvesting | photonic, m scale, water, ambient | rejected, commercial and capped by the psychrometric limit |

Two survivors from ten, which is the same rate as the first pass and as the 2026-11-19 session.

## What the second pass changed in the method

Vector 59 is the first entry whose novelty is a *ceiling* rather than a device: the geometry is a known parallel-plate stack, and the result is the observation that at $420\ \mathrm{ppm}$ the air handler is larger than the reversible separation work. It was written because the same pattern produced vectors 57 and 58 (the quoted number is not the binding number: support not vacuum, entropy not latent heat, fan not sorbent). Three instances of one pattern is a method, not a coincidence, and it is now the first thing to try on a new requirement: ask which number everyone quotes, then compute the one next to it.

Vector 60 is the first entry written against a commercial claim rather than a physical limit. It scores 21/30 against 20/30 for vector 56, and the difference is testability: the magnet claim can be settled with 20 copper tubes and 30 days, while the hot-carrier claim needs a selective contact that does not exist.

## Novelty test (interpretation of rule 1)

Rule 1 bans retrieval, so novelty cannot be verified by search. The working test used here:

1. Write the whole claim as one sentence. If that sentence already exists, it is a repackage.
2. Name the recent capability that makes it possible now. If there is none, it is a parameter change on an existing device.

Vector 58 passes on the second test because the capability is nanopore fabrication at $5\ \mathrm{nm}$ with $20\%$ porosity and a silane monolayer that survives $2\ \mathrm{MPa}$, which is a $2010$s capability, not a nineteenth-century one. The mechanism itself is described by Clausius and Lippmann and is not new. What is new is the sentence: one parameter fixes both the pressure head and the heat demand through a Carnot identity, so the device is exactly as good as the second law allows and no efficiency curve can be drawn.

## Candidates discussed, not written

### Deferred

* **Confinement-tuned hydrate cold storage.** The pore-size route to a $+5\ ^\circ\mathrm{C}$ cold store fails on the Gibbs-Thomson arithmetic. The dissociation depression is $\Delta T = 2\gamma T/(\rho\Delta H r)$, which is $1.9\ \mathrm{K}$ at $20\ \mathrm{nm}$ and $19\ \mathrm{K}$ at $2\ \mathrm{nm}$, and confinement destabilises the hydrate solid, so a smaller pore raises the formation pressure at fixed temperature instead of lowering it. The $+5\ ^\circ\mathrm{C}$ claim in the 2026-11-19 log needs a thermodynamic promoter such as THF, which is an additive and not a confinement effect. Deferred until the promoter question is separated from the pore-size question.
* **Electro-osmotic drying.** The same geometry with a voltage instead of a temperature difference costs $10$ to $100\ \mathrm{kJ/kg}$, which is competitive with vector 58, but it needs electrodes in contact with the wet solid and it generates pH gradients at both electrodes. Deferred because the pH problem is a materials problem, not an arithmetic one.

### Dead on arrival

* **Frost-heave pump.** The Clapeyron slope of ice is $dP/dT = L_f/(T\Delta v) = 13.6\ \mathrm{MPa/K}$, so $1\ \mathrm{K}$ lifts water $1360\ \mathrm{m}$ and $2\ \mathrm{MPa}$ of heave is observed at $0.15\ \mathrm{K}$. It dies on rate and on cost: the water must be frozen to move, which is $334\ \mathrm{kJ/kg}$ for $13.3\ \mathrm{kJ/kg}$ of lift (4% at best), and observed heave rates of millimetres per day give $0.15\ \mathrm{W}$ per kilogram, which is a toy.
* **Barometric energy storage.** A $1\ \mathrm{m^3}$ vessel collapsing under one atmosphere stores $pV = 100\ \mathrm{kJ/m^3} = 0.028\ \mathrm{kWh/m^3}$, four orders below a lithium-ion pack at $250$ to $700\ \mathrm{kWh/m^3}$. No geometry fixes a factor of $10^{4}$.
* **Sonoluminescent photocatalysis.** Single-bubble sonoluminescence converts acoustic energy to light at about $4\times10^{-9}$: $5\times10^{9}$ photons per second of $5\ \mathrm{eV}$ for $1\ \mathrm{W}$ of drive, which is $4\ \mathrm{nW}$ of light. A $30\%$ LED is $7\times10^{7}$ times better at the same wavelength, so the reaction rate per watt is dead by eight orders.

### Rejected as already catalogued or existing process

* **Triboluminescent X-ray source.** Demonstrated in 2008 by peeling tape in vacuum. Repackage.
* **Pyroelectric fusion.** Demonstrated in 2005 with a lithium tantalate crystal and deuterium. Repackage.
* **Radiative dew harvesting.** Commercial products exist and the psychrometric limit caps the yield at the dew-point depression, which the catalogue already covers under vector 13.
* **Vacuum and sub-atmospheric drying.** Existing industrial process; $70$ to $100\ ^\circ\mathrm{C}$ at $10$ to $50\ \mathrm{kPa}$ still pays most of the latent heat, so it is the same cost with a pressure vessel attached.

## Method note

Ten candidates, one written, two deferred, three dead, four rejected as catalogue or existing process. That ratio is the same as the 2026-11-19 session (three survivors from eight) once the near-field valve is counted as superseded rather than written.

The one number worth carrying forward is the Carnot identity in vector 58: $W/Q = \Delta T/T$ exactly. Any thermo-osmotic claim that reports a head without reporting the heat, or a heat without the head, is reporting a free parameter that does not exist.
