# Research log: 2026-11-19

Session record. What shipped, what the arithmetic killed, and what was discussed but not written.

## Shipped

| Vector | Claim in one line | Deciding number | Status |
|---|---|---|---|
| 50 | 12 nm pits confine the amyloid dense-liquid precursor below its Laplace critical radius | 0.83 bar confinement penalty at $1.9\times$ the driving force | live |
| 51 | Six sub-threshold beams ablate only where they overlap | $6.9\times10^{-3}$ selectivity unless the threshold step is 13 kPa wide | live, contested |
| 52 | 100 nm hydrogel mesh caps ice at mesh size | $D_{eff} \le 4.9\times10^{-16}\ \mathrm{m^2/s}$ | live, contested |
| 53 | Iontophoresis rebuilds a subsurface enamel lesion | 0.25 mg/cm$^2$ per session, 16 sessions | live |
| 54 | Microdischarge plus stripping fixes nitrogen at 8 kWh/kg N | 1.79 kWh/kg N thermodynamic floor | live, weak |
| 55 | Resonant pillars kill bacteria by strain scaling | 10x size selectivity, 464 W/cm$^2$ of drive | live, contested |
| 56 | Hot carriers cannot beat Shockley-Queisser | detailed balance | dead |

## Defects caught in this session

Four numbers supplied in the writing briefs did not survive their own derivation. Each is recorded in the relevant dossier rather than corrected silently.

1. Vector 51: the claimed $10^4$ volumetric selectivity requires a 13 kPa threshold step. At a realistic 200 kPa step the geometry delivers $6.9\times10^{-3}$. Corrected design point is $N = 7$, 0.65 MPa per beam, $w \le 100$ kPa.
2. Vector 52: the 2500x ripening ratio runs the wrong way. Small crystals ripen faster ($\dot r \propto r^{-2}$), so 100 nm ice ripens 2500x faster than 5 $\mu$m ice. The mesh must therefore also suppress diffusivity, which converts a prediction into a test condition.
3. Vector 55: the resonance was off by $10^3$. The correct set is $k = 40.0$ N/m at $L = 1\ \mu$m, giving 118 MHz in vacuum and 99 MHz in water with $Q \approx 8$. The original 3.7 MHz figure implies a soft pillar with $Q = 0.31$, which is overdamped and has no resonance at all.
4. Vector 53: the 4 mg/cm$^2$ lesion deficit is 32 percent of the geometric porosity bound of 12.5 mg/cm$^2$. Reconciled against a transverse microradiography profile; the full bound would need 50 sessions, not 16.

## Open decision

Vector 51 is marked live, but its own section 16 states that two pinned numbers fail. If the repository only keeps claims that survive their own arithmetic, it should be downgraded to wounded.

## Novelty test (interpretation of rule 1)

Rule 1 bans retrieval, so novelty cannot be verified by search. The working test used here:

1. Write the whole claim as one sentence. If that sentence already exists, it is a repackage.
2. Name the recent capability that makes it possible now. If there is none, it is a parameter change on an existing device.

Every mechanism is built from known pieces. Laplace pressure is two centuries old. What makes vector 50 a discovery is the sentence, not the ingredients.

## Candidates discussed, not written

### Live

* **Thermo-osmotic drying.** Remove liquid water through a hydrophobic nanopore membrane on a 5 K difference, so the 2.26 MJ/kg latent heat is never paid. Gain is 3x, not 10x, because the desorption enthalpy sets the floor at 0.55 to 1.7 MJ/kg. Kill test: kilos of water per kWh on wet sand, 0.15 kg/kWh threshold. Cost $10k.
* **Confinement-triggered hydrate cold storage.** Use pore size, not additives, to set gas hydrate formation temperature, giving 300 to 400 kJ/kg at +5 C. Kill test: induction time in 20 nm versus 200 nm pores; above 10 minutes and it is dead.
* **Near-field thermal valve.** A 100 nm vacuum gap conducts 6,000 W/m$^2$K, comparable to a bolted joint, with a 1,000:1 switching ratio and no contact wear. With radio-frequency modulation the same structure moves heat against the gradient, powered by the clock rather than a compressor. Kill test: net flow reversal at zero temperature difference, measured on a piezo stage.

### Dead on arrival

* **Hydrogen trapping in steel.** Holding 100 wppm of hydrogen needs about $5 \times 10^{26}$ trap sites per m$^3$ against $10^{24}$ for a 1 percent volume fraction of 5 nm precipitates. Short by 470x at any precipitate size.
* **Spin-Seebeck de-icing.** Microvolts and microwatts against the watts per square centimetre de-icing requires.
* **Thermoelectric cooling at 30 percent efficiency.** Carnot ceiling at 100 C to 30 C is 21 percent. Not hard, impossible.

### Rejected as already catalogued

Time-modulated antennas past the Chu limit (published field), near-field thermophotovoltaics (published field), acoustic microplastic separation (commercial for cells, so plastic is a parameter change), radiative-cooling vaccine fridges (existing products).

## Method note

Eight attempts produced three candidates that pass the novelty test. That is the normal rate. The two live candidates in the phase-change family share one insight: do the job without paying for the phase change that normally pays for it. Industrial drying, freeze drying, and desalination all sit in that family and none of them are in the repository.
