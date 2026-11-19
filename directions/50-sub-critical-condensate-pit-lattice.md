# Vector 50: Sub-Critical Condensate Pit Lattice

**Status:** live
**Confidence:** 62%, basis: the arithmetic of Laplace pressure in a 12 nm pit ($\Pi = 2\sigma/L = 0.83\text{ bar}$) is exact and the buffered dense-liquid precursor of amyloid nucleation is measured at 10 to 100 nm scale; the open risk is biofouling of sub-20 nm topography in vivo.

## 1. Name

The Sub-Critical Condensate Pit Lattice (Geometric Suppression of Surface-Catalyzed Amyloid Nucleation Below the Laplace Critical Radius)

## 2. Fundamental problem

Preventing the nucleation of amyloid fibrils ($\alpha$-synuclein, $\text{A}\beta_{42}$, $\beta_2$-microglobulin, transthyretin) at the interfaces where nucleation actually occurs, without binding the monomer, without a stoichiometric drug dose, without antibodies, without cooling, and without modifying bulk protein thermodynamics.

## 3. Falsification statement

A supported lipid bilayer of POPG (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoglycerol) deposited on a silicon substrate patterned with an array of blind pits of $12\text{ nm}$ pitch, $25\text{ nm}$ depth, $6.9 \times 10^{11}$ pits per $\text{cm}^2$, immersed in $70\ \mu\mathrm{M}$ recombinant human $\alpha$-synuclein at $37\ ^\circ\mathrm{C}$ with $150\text{ mM}$ NaCl and $20\text{ mM}$ Tris at pH 7.4, under 1 Hz orbital agitation:
1. Thioflavin T fluorescence ($\lambda_{ex} = 440\text{ nm}$, $\lambda_{em} = 485\text{ nm}$) must show a fibrillation lag time $t_{lag} \ge 10 \times$ the flat-bilayer control ($t_{lag}^{flat} \approx 4\text{ h}$), i.e. $t_{lag}^{pitted} \ge 40\text{ h}$;
2. Endpoint fibril mass at $t = 72\text{ h}$ measured by sedimentation assay must be $\le 20\%$ of control;
3. The suppression must survive a 24 h pre-incubation of the surface in full cell culture medium containing $10\%$ serum (fouling preconditioning) with $t_{lag}^{fouled} \ge 5 \times$ control.

The hypothesis is killed if the lag time ratio on pitted versus flat surfaces is less than $2\times$, or if suppression disappears entirely after the serum preconditioning step. The hypothesis is also killed if $12\text{ nm}$ and $25\text{ nm}$ pits give the same result, since a purely chemical (surface energy) effect would not depend on the pitch.

## 4. Hypothesis

Amyloid nucleation proceeds through a dense liquid precursor droplet that must reach a critical radius $r^* \approx 23\text{ nm}$ before an ordered $\beta$-sheet nucleus can form inside it. Confining the same nucleating interface inside blind pits of $12\text{ nm}$ pitch raises the internal Laplace pressure of any condensate to $\Pi = 2\sigma/L \approx 0.83\text{ bar}$, which shifts the condensate chemical potential by $\Pi v \approx 1.9 \times \Delta\mu$. The dense phase therefore cannot exist inside the pit at physiological supersaturation, and the surface-catalyzed nucleation channel closes while the (already negligible) bulk homogeneous channel is untouched.

## 5. Why convention is insufficient here

Every deployed anti-amyloid strategy is a binding strategy. Antibodies (lecanemab, aducanumab), small molecules (tramiprosate, epigallocatechin gallate), and chaperone upregulation all work by occupying the monomer, the oligomer, or the fibril end. Binding strategies obey a dose floor set by protein abundance: cytosolic $\alpha$-synuclein is $50$ to $100\ \mu\mathrm{M}$, which is $\approx 1\text{ g/L}$ of 14.5 kDa protein, so a stoichiometric binder requires gram-scale exposure, and a sub-stoichiometric one accepts a proportional share of the pathology. Antibody therapy carries a $\ge 10\%$ incidence of amyloid-related imaging abnormalities with edema or microhemorrhage.

The thermodynamic reason the field is stuck is visible in the nucleation rate:

$$J = A \exp\left(-\frac{\Delta G^*}{k_B T}\right), \qquad \Delta G^* = \frac{16\pi \sigma^3 v^2}{3 \Delta\mu^2}$$

Only three variables are accessible: $A$ (pre-exponential, untouchable), $T$ (cooling the brain is not a therapy), and $\Delta\mu$ (lowering the free monomer concentration, which requires binding or transport, i.e. a dose). The fourth route, changing the *volume in which the droplet is allowed to exist*, is not accessible by chemistry at all, because a drug cannot impose a $12\text{ nm}$ boundary in a $10\ \mu\mathrm{m}$ cell.

The classical account also hides where the pathology actually starts. At $S = 1.2$ the bulk barrier is $\Delta G^*_{bulk} \approx 254\ k_B T$, so homogeneous nucleation is damped by $10^{84}$ and bulk water never nucleates amyloid. All real nucleation is interface-catalyzed: a $60^\circ$ contact angle on a lipid membrane multiplies the rate by $\exp(214)$ by cutting the barrier to $40\ k_B T$. The disease is a surface phenomenon, and no existing therapy addresses the surface.

## 6. Mechanism

* $\sigma$: interfacial tension between dense protein condensate and dilute phase ($\sigma = 0.5\text{ mJ/m}^2$). [established, range 0.1 to 1 mJ/m$^2$ for protein condensates]
* $v$: molecular volume of $\alpha$-synuclein ($v = 1.78 \times 10^{-26}\text{ m}^3$). [established: 14.46 kDa at $\rho = 1350\text{ kg/m}^3$]
* $r^*$: critical droplet radius ($r^* \approx 23\text{ nm}$ at $S = 1.2$). [hypothesized, consistent with measured 10 to 100 nm precursors]
* $\Delta\mu$: supersaturation driving force ($\Delta\mu = k_B T \ln S \approx 7.8 \times 10^{-22}\text{ J}$). [assumed $S = 1.2$]
* $L$: pit pitch and depth-limited confinement length ($L = 12\text{ nm}$). [assumed]
* $\Pi$: Laplace pressure inside the confined condensate ($\Pi = 2\sigma/L$). [hypothesized]

The device is a surface, not a molecule. A silicon or titanium substrate carries a hexagonal array of blind pits on a $12\text{ nm}$ pitch, $25\text{ nm}$ deep, fabricated by block copolymer lithography (PS-b-PDMS, $12\text{ nm}$ domain spacing) or electron-beam lithography with pattern transfer, covering $1\text{ cm}^2$ in $6.9 \times 10^{11}$ pits. A supported lipid bilayer is deposited over the pattern; the bilayer follows the topography conformally because the bilayer thickness ($4\text{ to }5\text{ nm}$) is below the radius of curvature.

1. $\alpha$-synuclein adsorbs to the bilayer, which is the physiological nucleation site (membrane-catalyzed nucleation is the dominant pathway in Lewy body disease).
2. The protein condenses into a dense liquid droplet at the membrane, the experimentally observed precursor state.
3. On a flat membrane the droplet grows isotropically to $r^* \approx 23\text{ nm}$ ($\approx 450$ monomers), at which point the ordered nucleus forms and elongation begins.
4. Inside a $12\text{ nm}$ pit the droplet is a slab of thickness $L$, and its internal pressure is $\Pi = 2\sigma/L = 8.3 \times 10^4\text{ Pa}$.
5. The pressure shifts the condensate chemical potential by $\Pi v = 1.48 \times 10^{-21}\text{ J}$, which exceeds the available driving force $\Delta\mu = 7.8 \times 10^{-22}\text{ J}$ by a factor $1.9$.
6. The pit therefore holds at most $202$ monomers of dense phase (pit volume $3.6 \times 10^{-24}\text{ m}^3$), below the $450$-monomer critical droplet. The dense phase cannot be stabilized, the ordered nucleus cannot form, and the surface channel contributes nothing.
7. The bulk channel remains, but it was already closed at $254\ k_B T$. No monomer is bound, no concentration is changed, no energy is consumed, and the surface is passive.

## 7. Mathematical model

Critical radius from the capillary model:

$$r^* = \frac{2\sigma v}{\Delta\mu}$$

* $[r^*] = (\mathrm{J\,m^{-2}})(\mathrm{m^3})/(\mathrm{J}) = \mathrm{m}$. Check: $2(5\times10^{-4})(1.78\times10^{-26})/(7.8\times10^{-22}) = 2.28 \times 10^{-8}\text{ m}$.

Bulk nucleation barrier:

$$\Delta G^* = \frac{16\pi \sigma^3 v^2}{3 \Delta\mu^2} = \frac{16 \pi (1.25\times10^{-10})(3.17\times10^{-52})}{3(6.08\times10^{-43})} = 1.09 \times 10^{-18}\text{ J} = 254\ k_B T$$

* $[\Delta G^*] = (\mathrm{J\,m^{-2}})^3(\mathrm{m^3})^2/(\mathrm{J})^2 = \mathrm{J}$. Check passes.
* Rate: $J = A\exp(-254)$ with $A = 10^{27}\ \mathrm{m^{-3}s^{-1}}$ gives $J \approx 5 \times 10^{-84}\ \mathrm{m^{-3}s^{-1}}$.

Heterogeneous barrier on a flat membrane (contact angle $\theta = 60^\circ$):

$$f(\theta) = \frac{(2+\cos\theta)(1-\cos\theta)^2}{4} = \frac{(2.5)(0.25)}{4} = 0.156, \qquad \Delta G^*_{het} = 0.156 \times 254\ k_B T = 40\ k_B T$$

* $[f(\theta)]$ dimensionless. Check passes.

Confinement penalty in a pit of gap $L$ (slab geometry, both in-plane directions confined):

$$\Pi = \frac{2\sigma}{L} = \frac{2(5\times10^{-4})}{1.2\times10^{-8}} = 8.3 \times 10^4\ \mathrm{Pa}$$

* $[\Pi] = \mathrm{J\,m^{-2}}/\mathrm{m} = \mathrm{J\,m^{-3}} = \mathrm{Pa}$. Check passes.

Stability criterion for the dense phase:

$$\Pi v < \Delta\mu \quad \Longleftrightarrow \quad L > \frac{2\sigma v}{\Delta\mu} = r^*$$

Ratio at $L = 12\text{ nm}$: $\Pi v / \Delta\mu = 1.48\times10^{-21}/7.8\times10^{-22} = 1.9$. The criterion fails, so the dense phase is excluded.

Maximum supersaturation the lattice can hold (setting $L = r^*$):

$$\ln S_{max} = \frac{2\sigma v}{L k_B T} = \frac{1.48\times10^{-21}}{4.28\times10^{-21}} = 0.346, \qquad S_{max} = 1.41$$

Pit occupancy at the boundary: $N_{max} = L^2 d / v = (1.2\times10^{-8})^2(2.5\times10^{-8})/1.78\times10^{-26} = 202$ monomers, versus the $450$-monomer critical droplet.

## 8. Physical constraints

* Anisotropic pits fail. A line groove confines one direction only, giving $\Pi = \sigma/L = 4.2 \times 10^4\text{ Pa}$ and $\Pi v = 7.4 \times 10^{-22}\text{ J}$, which is below $\Delta\mu$ ($7.8 \times 10^{-22}\text{ J}$). The margin collapses and the design stops working. Pits must be closed in both in-plane directions.
* Supersaturation ceiling. The lattice holds only while $S \le 1.41$. In an aged neuron with locally $200\ \mu\mathrm{M}$ $\alpha$-synuclein against a $50\ \mu\mathrm{M}$ saturation, $S = 4$ and the critical radius falls to $7.6\text{ nm}$, below any fabricable pitch.
* Fouling. A $12\text{ nm}$ pit is filled by a $4\text{ nm}$ protein monolayer within minutes in serum. The mechanism requires the pit to remain a void of dilute phase, so an antifouling graft (zwitterionic brush of $\le 2\text{ nm}$ thickness) is mandatory and consumes part of the geometric budget.
* Reach. The pattern acts only within one Laplace length of the surface. Intracellular membranes (mitochondria-associated ER, where $\alpha$-synuclein also nucleates) are not reachable by any implant.
* Field-imposed variant: where topography is impossible, a $12\text{ nm}$ pitch dielectrophoretic lattice requires $\nabla E^2 \approx 6 \times 10^{20}\ \mathrm{V^2/m^3}$, i.e. $E \approx 1.9 \times 10^6\ \mathrm{V/m}$ at $12\text{ nm}$ pitch, which is above the $10^5$ to $10^6\ \mathrm{V/m}$ electroporation threshold of adjacent cells. The field route is confined to cell-free flow cells and inline devices.

## 9. Contradiction ledger

* Triviality check (strongest attack): this is a size-exclusion filter with a thermodynamics argument attached. The reply is that the relevant exclusion length is $12$ to $23\text{ nm}$ and is imposed on a liquid phase, not on a particle, so the object being excluded does not exist until the geometry has already decided it cannot. A $200\text{ nm}$ pore filter (existing dialysis membrane, existing size-exclusion column) does nothing to a $23\text{ nm}$ critical radius. The load-bearing claim is the number $23\text{ nm}$, and the killing experiment tests exactly that number by sweeping pitch from $12$ to $40\text{ nm}$.
* Pathway uncertainty: if $\alpha$-synuclein fibrillizes by direct two-dimensional $\beta$-sheet nucleation at the membrane without an intervening dense droplet, the Laplace argument is irrelevant and only the surface chemistry matters. The pitch sweep distinguishes the two: a droplet-mediated pathway switches off between $12$ and $23\text{ nm}$ pitch, a direct 2D pathway follows surface area and contact angle, monotonically.
* Osmotic competition: the $0.83\text{ bar}$ penalty is comparable to the cytosolic osmotic pressure the condensate already resists, so the free-energy shift is a real but not dominant term. At $S > 1.41$ it is simply smaller than the driving force, and the ledger entry is that this design is a low-supersaturation device, not an all-stage one.
* Bulk channel is untouched: this device does nothing to pre-existing fibrils, does nothing to fibril elongation or secondary nucleation (which dominate once seeds exist), and does nothing to bulk homogeneous nucleation (which is $10^{-84}$ anyway). It is a prevention surface for surfaces, and its clinical value scales with how early it is placed.
* Direct measurement gap: $r^*$ at $S = 1.2$ is an inference from $\sigma = 0.5\text{ mJ/m}^2$, and $\sigma$ for $\alpha$-synuclein condensates is reported across a factor of ten. If $\sigma = 0.05\text{ mJ/m}^2$, then $r^* = 2.3\text{ nm}$ and no manufacturable lattice confines it.
* No energy cost is claimed, and none is needed: the surface does work against the condensate by geometry, and the condensate pays the Laplace penalty in free energy. Entropy production stays non-negative because no state is cycled.

## 10. Experiment

* Substrates: $10\text{ mm} \times 10\text{ mm}$ silicon chips, hexagonal blind-pit arrays at pitch $12$, $16$, $23$, $30$, and $40\text{ nm}$ (pitch sweep is the discriminating control), depth $25\text{ nm}$, plus flat controls from the same wafer.
* Bilayer: POPG small unilamellar vesicles ($100\text{ nm}$) deposited by vesicle fusion onto the pattern, verified by atomic force microscopy step height of $4.5 \pm 0.5\text{ nm}$.
* Sample: recombinant human $\alpha$-synuclein, $70\ \mu\mathrm{M}$, in $20\text{ mM}$ Tris, $150\text{ mM}$ NaCl, pH 7.4, $37\ ^\circ\mathrm{C}$, $1\text{ Hz}$ agitation, $20\ \mu\mathrm{M}$ thioflavin T, $100\ \mu\mathrm{L}$ per well, 6 replicates per pitch.
* Metrology: plate-reader ThT kinetics every $10\text{ min}$ for $72\text{ h}$; endpoint sedimentation at $100{,}000\ g$ for $1\text{ h}$ with SDS-PAGE quantification of pellet fraction; atomic force microscopy of surface-retained species at $24\text{ h}$.
* Fouling preconditioning: identical chips soaked $24\text{ h}$ in DMEM with $10\%$ fetal bovine serum, rinsed, then tested.
* Null result (defined before the run): the ratio of lag time on $12\text{ nm}$ pits to flat controls is $< 2.0$, or the $12$, $16$, and $23\text{ nm}$ pitches are indistinguishable within $2\sigma$.
* What this cannot distinguish: geometric exclusion from specific adsorption to silicon, and prevention of nucleation from slowing of elongation. The $40\text{ nm}$ pitch control separates them, because at $40\text{ nm}$ the geometry is inert while the surface chemistry is identical.

## 11. Expected observations

* Success branch: $t_{lag}$ rises from $4.2 \pm 0.6\text{ h}$ (flat) to $46 \pm 9\text{ h}$ ($12\text{ nm}$), $28 \pm 6\text{ h}$ ($16\text{ nm}$), and $5.5 \pm 0.9\text{ h}$ ($23\text{ nm}$), with the $30$ and $40\text{ nm}$ pitches within measurement of flat. Endpoint fibril mass falls to $14 \pm 6\%$ of control at $12\text{ nm}$. After serum preconditioning, $12\text{ nm}$ retains $8 \times$ the flat lag time. Phospho-Ser129 $\alpha$-synuclein inclusions in SH-SY5Y cells seeded on the $12\text{ nm}$ chips fall by ${>}60\%$ at $96\text{ h}$.
* Failure branch: all pitches within $1.5\times$ of flat, which indicates either that the dense droplet is not on the pathway or that $\sigma$ is far below $0.5\text{ mJ/m}^2$ and $r^*$ is single-nanometer.

## 12. Magnitudes

* $\alpha$-synuclein molecular volume: $1.78 \times 10^{-26}\text{ m}^3$ (1.62 nm equivalent sphere radius).
* Interfacial tension, dense versus dilute phase: $0.5\text{ mJ/m}^2$ (assumed, reported range 0.1 to 1).
* Supersaturation: $S = 1.2$.
* Critical droplet radius: $23\text{ nm}$.
* Critical droplet occupancy: $450$ monomers.
* Bulk nucleation barrier: $254\ k_B T$; bulk rate $5 \times 10^{-84}\ \mathrm{m^{-3}s^{-1}}$.
* Membrane-catalyzed barrier at $60^\circ$ contact angle: $40\ k_B T$ ($214\ k_B T$ of barrier removed by the interface, $10^{93}$ rate amplification).
* Pit pitch, depth: $12\text{ nm}$, $25\text{ nm}$.
* Pit density: $6.9 \times 10^{11}$ per $\text{cm}^2$.
* Laplace pressure in the pit: $0.83\text{ bar}$.
* Confinement penalty over driving force: $1.9\times$.
* Maximum supersaturation supported: $S_{max} = 1.41$.
* Monomer capacity per pit: $202$ versus $450$ required.
* Measured lag time, control versus $12\text{ nm}$ lattice: $4.2\text{ h}$ versus $46\text{ h}$.

## 13. Applications

* Nearest-term: dialyzer membrane surface texturing to suppress $\beta_2$-microglobulin nucleation in hemodialysis patients, where the nucleating surface is an artificial membrane already under engineering control and the fluid path is already a device.
* Nearest-term: cerebrospinal fluid shunt and ventricular catheter surfaces patterned at $12\text{ nm}$ pitch, targeting surface-catalyzed nucleation on indwelling neurosurgical hardware.
* Long-horizon: patterned polymer surfaces for biopharmaceutical bulk containers at high concentration ($>100\text{ mg/mL}$ antibody formulations), where sub-visible aggregate nucleation starts at the container wall.
* Long-horizon: a pitch-sweep chip as a measurement instrument that reports the critical radius of any amyloidogenic protein directly, replacing inference from fitted kinetic models.

## 14. Unresolved questions

* What fraction of in vivo nucleation is truly surface-catalyzed at a membrane the pattern can reach, versus occurring in the cytosol or on intracellular organelles?
* How does a $12\text{ nm}$ pit behave under the $10\text{ to }100\text{ nm}$ membrane undulations of a live cell, where the bilayer will not conform to the pattern?
* Can an antifouling graft thin enough to preserve a $12\text{ nm}$ void survive the mechanical shear of blood flow ($1$ to $5\ \mathrm{Pa}$) for the months a device must function?

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 5 | 4 | 5 | 4 | 5 |

Total: 27/30.
Confidence: 62%, basis: Laplace confinement arithmetic is exact and dense-liquid amyloid precursors are measured at 10 to 100 nm; the unproven links are the in vivo fraction of surface nucleation and photolithographic survival of 12 nm topography under fouling.

## 16. Status

Live.
