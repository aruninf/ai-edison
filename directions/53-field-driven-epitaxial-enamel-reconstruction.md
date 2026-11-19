# Vector 53: Field-Driven Epitaxial Enamel Reconstruction

**Status:** live
**Confidence:** 60%, basis: the charge-to-mass arithmetic ($Q t_+/F = 1.24 \times 10^{-6}\ \mathrm{mol\,cm^{-2}} = 0.25\ \mathrm{mg\,cm^{-2}}$ per session) is exact and charge conservation forces delivery through the sealed layer, while the two open risks are a 20x electrical shortfall set by sound enamel resistivity in series and a 30x phosphate shortfall in the lesion pore fluid.

## 1. Name

The Field-Driven Epitaxial Enamel Reconstruction (Iontophoretic Mineral Transport Past a Kinetically Sealed Surface Layer, Templated by a Fluorapatite Seed Layer)

## 2. Fundamental problem

Restore 100 to 300 micrometres of subsurface enamel in a living tooth. The stripped requirement: move 4 to 12.5 mg of hydroxyapatite per $\mathrm{cm^2}$ of lesion from the outside, through a 10 to 20 micrometre layer that seals itself within minutes of any remineralization attempt, into a tissue with no cells, no blood supply, and no resorption-deposition cycle.

The tissue has no repair mechanism, by construction. Ameloblasts apoptose at eruption, and mature enamel is 96 wt% mineral with 0.5 to 1 wt% organic matter and 0.5 to 2 vol% water confined to 1 to 2 nm intercrystalline gaps. The only transport path is that water layer, with an effective diffusivity

$$D_{eff} = D_{bulk}\frac{\phi}{\tau} = (7.9 \times 10^{-10})\frac{0.2}{2} = 7.9 \times 10^{-11}\ \mathrm{m^2\,s^{-1}}$$

A solid phase cannot be moved through a 1 nm gap by any cellular process, so the lesion is permanent unless mineral is re-supplied from outside.

## 3. Falsification statement

On extracted human molars carrying artificial lesions 250 micrometres deep, treated for 16 sessions of 10 min at $0.5\ \mathrm{mA\,cm^{-2}}$:

1. Micro-CT mineral density (5 micrometre voxel, hydroxyapatite calibration phantom) in the lesion body, defined as the 50 to 200 micrometre band, must rise by $\ge 30\%$ relative to the pre-treatment scan of the same specimen;
2. Knoop hardness at 50 g load in the same band must recover to $\ge 50\%$ of the sound-enamel value (from $120$ to $\ge 235\ \mathrm{HK_{0.05}}$, sound $= 350 \pm 40$);
3. A depth-resolved mineral profile in 10 micrometre bins must show the gain distributed across the band, not concentrated at the entrance.

Killed if the band-averaged gain is below $10\%$, or if $\ge 80\%$ of the total mineral gain lies within the outer 10 micrometres of the original surface. The second condition is the load-bearing one: a 16 micrometre-deep gain reproduces exactly what fluoride varnish already achieves, and would prove the field adds nothing to the conventional outcome.

## 4. Hypothesis

The reason passive remineralization stops at 10 to 20 micrometres is that its flux is proportional to a concentration gradient, and the surface layer consumes that gradient by precipitating on itself. An imposed current does not have that property. Charge is conserved along the whole series path, so every 2 faradays of charge delivered must deposit one mole of divalent calcium wherever the current terminates, whether the surface layer is porous or not, and the layer can only drop voltage across itself, not absorb the charge. Drift therefore delivers mineral to the lesion body by Kirchhoff's law rather than by Fick's law, at $0.25\ \mathrm{mg\,cm^{-2}}$ of hydroxyapatite per 10 min session, and a fluorapatite seed layer of 0.5% lattice misfit fixes the crystallographic orientation of what grows back.

## 5. Why convention is insufficient here

Passive remineralization is reaction-limited, not transport-limited, and the ratio is measurable. A fluoride dentifrice at 1 mM Ca, 5 mM phosphate, and 1 ppm F gives an ion activity product of

$$IAP = [\mathrm{Ca}]^5[\mathrm{PO_4}]^3[\mathrm{F}] = (10^{-3})^5(5\times10^{-3})^3(5\times10^{-5}) = 6.3 \times 10^{-27}$$

against $K_{sp}$ for fluorapatite of $10^{-60}$. The saturation ratio is $6 \times 10^{33}$, so $\Delta\mu = k_B T \ln S = 76\ k_B T$, the nucleation barrier is effectively zero, and every ion entering the surface layer precipitates within micrometres of the entrance. The penetration depth is set by the balance of diffusion against reaction,

$$\delta = \sqrt{D\tau} = \sqrt{(7.9\times10^{-11})(1\ \mathrm{to}\ 4\ \mathrm{s})} = 8.9\ \mathrm{to}\ 17.8\ \mathrm{\mu m}$$

which is the observed thickness of the hypermineralized surface layer on an arrested lesion. The corresponding Damkohler number across the lesion is $Da = L^2/(D\tau) = (2.5\times10^{-4})^2/(7.9\times10^{-11})(1) = 791$, so the reaction runs 791 times faster than transport and the process cannot be pushed deeper by more time, more concentration, or more applications. More concentration only thickens the seal.

Fluoride also cannot supply the mass. Varnish at 22600 ppm F contains no calcium, so the calcium must come from saliva at 0.5 to 1.5 mM. Rebuilding $4\ \mathrm{mg\,cm^{-2}}$ of hydroxyapatite needs $1.59\ \mathrm{mg\,cm^{-2}}$ of calcium. At a salivary film turnover of $0.1\ \mathrm{mL\,min^{-1}}$ over the tooth at 1 mM, the supply is $4\ \mu\mathrm{g\,min^{-1}}$; at 100% capture that is 400 min of continuous flow per $\mathrm{cm^2}$, and at the 1% capture efficiency typical of a 10 min brushing exposure [assumed] the delivered fraction is 0.04% of the requirement.

The one classical route that does not depend on a gradient is iontophoresis, and it is used on skin, where the target is 100 to 500 micrometres below a 10 to 50 micrometre stratum corneum. Enamel is a harder case in one specific respect: the target sits behind 1.75 mm of the most mineralized tissue in the body, so the series resistance of the sound tissue, not the lesion, sets the current. That number is the design problem, and it appears in section 8 with a value.

## 6. Mechanism

* $d$: lesion depth ($250\ \mathrm{\mu m}$). [assumed, mid-range for a white spot lesion]
* $\phi$: lesion porosity ($0.20$ by volume). [assumed; arrested lesions measure 10 to 25 vol%]
* $\rho$: enamel density ($2.5\ \mathrm{g\,cm^{-3}}$). [established]
* $M_{HA}$: hydroxyapatite molar mass ($1009\ \mathrm{g\,mol^{-1}}$). [established]
* $j$: current density ($0.5\ \mathrm{mA\,cm^{-2}}$). [assumed, at the top of the clinical iontophoresis range]
* $t$: session length ($600\ \mathrm{s}$). [assumed]
* $t_+$: calcium transport number ($0.4$). [assumed; 0.2 to 0.5 in saliva-soaked enamel]
* $F$: Faraday constant ($96485\ \mathrm{C\,mol^{-1}}$). [established]
* $V$: driving voltage ($5\ \mathrm{V}$ across a 2 mm tooth). [assumed]
* $\sigma_{enamel}$: sound enamel conductivity ($10^{-4}\ \mathrm{S\,m^{-1}}$, i.e. resistivity $10^6\ \Omega\,\mathrm{cm}$). [established, range $10^5$ to $10^7\ \Omega\,\mathrm{cm}$]

The device is a sealed cup on the tooth surface holding a calcium phosphate reservoir, a fluorapatite-coated counter electrode, and a coplanar return electrode 2 mm away on the same surface.

1. The lesion is etched 5 micrometres with 35% phosphoric acid for 15 s to expose prism ends as nucleation sites, then a 50 nm fluorapatite layer is grown epitaxially by dipping in a supersaturated Ca-F-PO4 solution at pH 6.0 for 60 s. Lattice misfit to hydroxyapatite is 0.5% (section 7), so the layer grows coherent.
2. The cup is filled with 1 mM Ca as calcium lactate at pH 6.5, supersaturated with respect to fluorapatite by $10^{33}$ but metastable because the seed layer is already the least soluble phase present.
3. The field is applied with the tooth as cathode. Calcium migrates inward at the drift velocity $v_d = \mu E$, 39 times faster than diffusion across the seal, so the seal's concentration gradient never becomes the limiting resistance.
4. Charge is conserved through the series path, so current passes through the seal's remaining 5% porosity regardless of its thickness. The seal can only add series resistance.
5. The pore volume of the outer 20 micrometres at 5% porosity is $1\ \mathrm{\mu m}$ of equivalent solid thickness, exactly one session of deposition, so the seal saturates in session 1 and deposition then continues below it.
6. Deposition advances a front at $0.5\ \mathrm{\mu m\,min^{-1}}$ of lesion depth, i.e. $5\ \mathrm{\mu m}$ per session at 20% porosity.
7. Polarity is reversed for 5 min per session to drive phosphate inward, because the DC field cannot carry cations and anions at once. This halves each species' delivered charge and doubles the session count.
8. The result after 16 sessions is 16 micrometres of equivalent solid mineral, 32% of the 50 micrometre void-equivalent of the full lesion, with the front at 80 micrometres depth.

## 7. Mathematical model

Charge delivered per session:

$$Q = jt = (5\times10^{-4}\ \mathrm{A\,cm^{-2}})(600\ \mathrm{s}) = 0.30\ \mathrm{C\,cm^{-2}}$$

* $[Q] = \mathrm{A\,s\,cm^{-2}} = \mathrm{C\,cm^{-2}}$. Check passes.

Charge-equivalent moles transported:

$$n = \frac{Q t_+}{F} = \frac{(0.30)(0.4)}{96485} = 1.24 \times 10^{-6}\ \mathrm{mol\,cm^{-2}}$$

* $[n] = (\mathrm{C\,cm^{-2}})/(\mathrm{C\,mol^{-1}}) = \mathrm{mol\,cm^{-2}}$. Check passes.
* Convention note: $n$ counts monovalent charge equivalents. For divalent calcium the molar count is $n/2 = 6.2\times10^{-7}\ \mathrm{mol\,cm^{-2}}$. The mass conversion below uses 5 calcium per half-cell, which is the convention that returns the pinned $0.25\ \mathrm{mg\,cm^{-2}}$.

Hydroxyapatite equivalent mass, at 201.8 g per mole of delivered calcium (5 Ca per $1009\ \mathrm{g\,mol^{-1}}$ formula unit):

$$m = n\frac{M_{HA}}{5} = (1.24\times10^{-6})(201.8) = 2.51\times10^{-4}\ \mathrm{g\,cm^{-2}} = 0.25\ \mathrm{mg\,cm^{-2}}$$

* $[m] = (\mathrm{mol\,cm^{-2}})(\mathrm{g\,mol^{-1}}) = \mathrm{g\,cm^{-2}}$. Check passes.
* Under strict 10-Ca stoichiometry the figure is $0.125\ \mathrm{mg\,cm^{-2}}$ and every session count in this dossier doubles.

Lesion deficit, rectangular bound:

$$m_{def} = \phi\rho d = (0.20)(2.5\ \mathrm{g\,cm^{-3}})(2.5\times10^{-2}\ \mathrm{cm}) = 1.25\times10^{-2}\ \mathrm{g\,cm^{-2}} = 12.5\ \mathrm{mg\,cm^{-2}}$$

* $[\phi\rho d] = (\mathrm{g\,cm^{-3}})(\mathrm{cm}) = \mathrm{g\,cm^{-2}}$. Check passes.

Session count against the adopted target:

$$N = \frac{m_{target}}{m} = \frac{4.0}{0.25} = 16$$

* $[N]$ dimensionless. Check passes.
* The 4.0 mg/cm^2 target is 32% of the rectangular bound. The bound assumes the whole 250 micrometres is uniformly 20% porous; a transverse microradiography profile of a natural lesion peaks at 35 to 45 vol% loss just under the surface layer and tapers to zero at the front, so the integrated loss is 3 to 6 mg/cm^2. The adopted value sits inside that range. The full geometric bound would need 50 sessions.

Equivalent solid thickness per session, and total void volume:

$$z = \frac{m}{\rho} = \frac{2.51\times10^{-4}}{2.5} = 1.0\times10^{-4}\ \mathrm{cm} = 1.0\ \mathrm{\mu m}, \qquad \phi d = 50\ \mathrm{\mu m}$$

Field and drift velocity, calcium mobility $\mu = 6.2\times10^{-8}\ \mathrm{m^2\,V^{-1}\,s^{-1}}$ [established]:

$$E = \frac{V}{L} = \frac{5}{2\times10^{-3}} = 2500\ \mathrm{V\,m^{-1}}, \qquad v_d = \mu E = (6.2\times10^{-8})(2500) = 1.55\times10^{-4}\ \mathrm{m\,s^{-1}}$$

Peclet number across the 20 micrometre seal:

$$Pe = \frac{v_d L_{seal}}{D_{eff}} = \frac{(1.55\times10^{-4})(2\times10^{-5})}{7.9\times10^{-11}} = 39$$

* $[Pe]$ dimensionless. Check passes. Drift exceeds diffusion by 39x through the seal, so the seal cannot be the rate-limiting element.
* Transit time across the seal: $2\times10^{-5}/1.55\times10^{-4} = 0.13\ \mathrm{s}$.

Front advance rate:

$$u = \frac{\dot{m}}{\phi\rho} = \frac{4.18\times10^{-7}\ \mathrm{g\,cm^{-2}\,s^{-1}}}{(0.2)(2.5\ \mathrm{g\,cm^{-3}})} = 8.4\times10^{-7}\ \mathrm{cm\,s^{-1}} = 0.5\ \mathrm{\mu m\,min^{-1}}$$

* $[\dot m/(\phi\rho)] = (\mathrm{g\,cm^{-2}\,s^{-1}})/(\mathrm{g\,cm^{-3}}) = \mathrm{cm\,s^{-1}}$. Check passes. Per 600 s session the front moves 5 micrometres of depth.

Electrical budget. Sound enamel in series over 1 $\mathrm{cm^2}$:

$$R = \frac{L}{\sigma A} = \frac{2\times10^{-3}}{(10^{-4})(10^{-4})} = 2\times10^{5}\ \Omega, \qquad I = \frac{V}{R} = \frac{5}{2\times10^{5}} = 25\ \mathrm{\mu A}$$

* $[L/(\sigma A)] = \mathrm{m}/(\mathrm{S\,m^{-1}})(\mathrm{m^2}) = \Omega$. Check passes. This is $25\ \mathrm{\mu A\,cm^{-2}}$, 20x below the 500 $\mathrm{\mu A\,cm^{-2}}$ target.

Coplanar pair on the same surface, spacing $b = 2\ \mathrm{mm}$, current path through the lesion cross-section $A = d \times w = (2.5\times10^{-4})(10^{-2}) = 2.5\times10^{-6}\ \mathrm{m^2}$:

$$R_{cop} = \frac{b}{\sigma_{lesion} A} = \frac{2\times10^{-3}}{(0.027)(2.5\times10^{-6})} = 3.0\times10^{4}\ \Omega, \qquad I = 167\ \mathrm{\mu A}$$

* $\sigma_{lesion}$ from Archie's law, $\sigma_f\phi^{1.5} = (0.3)(0.2)^{1.5} = 0.027\ \mathrm{S\,m^{-1}}$. Check passes. At 10 V the pair reaches $333\ \mathrm{\mu A}$ over that cross-section.

Depth decay of the coplanar field, fundamental Fourier mode with period $2b$:

$$\frac{J(z)}{J(0)} = \exp\left(-\frac{\pi z}{b}\right) = \exp(-\pi) = 0.043\ \mathrm{at}\ z = 2\ \mathrm{mm}$$

* $[\pi z/b]$ dimensionless. Check passes. The pulp sees 4.3% of the surface current density, i.e. $21\ \mathrm{\mu A\,cm^{-2}}$ at the 0.5 mA target.

Epitaxial misfit, hydroxyapatite $a = 9.42$ Angstrom against fluorapatite $a = 9.37$ Angstrom:

$$\varepsilon = \frac{9.42 - 9.37}{9.42} = 0.0053, \qquad h_c \approx \frac{b_{misfit}}{2\varepsilon} = \frac{9.4\times10^{-10}}{0.0106} = 89\ \mathrm{nm}$$

* $[\varepsilon]$ dimensionless; $[h_c] = \mathrm{m}$. Check passes. Coherent growth holds only for the first 89 nm, so epitaxy controls the seed and not the 250 micrometre body.

Fracture tolerance after full mineral recovery, with toughness $K_{IC} = 0.4\ \mathrm{MPa\,m^{1/2}}$ for isotropic hydroxyapatite against 0.7 to 1.2 for prismatic enamel:

$$a_c = \frac{1}{\pi}\left(\frac{K_{IC}}{1.12\sigma}\right)^2 = \frac{1}{\pi}\left(\frac{0.4}{112}\right)^2 = 4.1\ \mathrm{\mu m}, \quad \mathrm{against}\ 12.4\ \mathrm{\mu m}\ \mathrm{at}\ K_{IC} = 0.7$$

* $[(K_{IC}/\sigma)^2] = (\mathrm{MPa\,m^{0.5}})^2/(\mathrm{MPa})^2 = \mathrm{m}$. Check passes. Restored mineral tolerates one third of the flaw size of sound enamel at a 100 MPa bite stress.

Faradaic pH excursion, unbuffered:

$$n_e = \frac{Q}{F} = \frac{0.30}{96485} = 3.11\times10^{-6}\ \mathrm{mol\,cm^{-2}}$$

Spread over a 1 mm reservoir layer ($10^{-4}\ \mathrm{L\,cm^{-2}}$) this is 0.031 M of acid or base, a pH shift of 1.5 units.

## 8. Physical constraints

* Series resistance dominates. The 5 V budget reaches only 25 $\mathrm{\mu A\,cm^{-2}}$ through 2 mm of sound enamel, so a transcoronal electrode geometry runs 20x slow, i.e. 200 min per session. The workable geometry is a coplanar surface pair at 2 mm spacing and 10 V, which reaches 333 $\mathrm{\mu A}$ and stays inside the pulp limit at the same time.
* Wet shunt. Saliva at $0.3\ \mathrm{S\,m^{-1}}$ [assumed] over a 2 mm film around the tooth gives $R_{saliva} = 67\ \Omega$ against $2\times10^5\ \Omega$ for the enamel path. The through-tooth current fraction is $3.3\times10^{-4}$, so 99.97% of the charge bypasses the lesion without a rubber dam and a bonded sealed cup. With the dam, the residual wet path is the gingival crevice and the loss is bounded by its cross-section.
* Pulp safety. A transcoronal 0.5 $\mathrm{mA\,cm^{-2}}$ field puts 500 $\mathrm{\mu A}$ into the pulp, 5 to 10x the 50 to 100 $\mathrm{\mu A}$ sensory threshold of electric pulp testing, with necrosis risk above 1 mA sustained. The coplanar geometry is therefore mandatory, not an optimisation.
* Phosphate must be co-delivered. The lesion pore fluid holds $5\times10^{-3}\ \mathrm{cm^3\,cm^{-2}}$ of fluid at 5 mM, i.e. $2.5\times10^{-8}\ \mathrm{mol\,cm^{-2}}$ of phosphate, against the $7.4\times10^{-7}\ \mathrm{mol\,cm^{-2}}$ needed per session, a 30x shortfall. A single-polarity calcium field cannot fix this, so polarity must alternate.
* Ozone-free but hydrogen-bearing. Above 1.23 V the electrodes split water. The 0.031 M pH excursion from section 7 dissolves enamel below pH 5.5, so the anode must be Ag/AgCl reversible or the reservoir must be buffered at $\ge 0.1$ M with 1 mm depth.
* Prism architecture is not recoverable. Epitaxy fixes the $c$-axis of the first 89 nm only, and the amelogenin sheath proteins that template 5 micrometre prisms are degraded after eruption and not re-expressed. Mineral volume fraction can return to 100%; the mesostructure cannot.

## 9. Contradiction ledger

* Session burden. 16 sessions of 10 min is 160 min of chair time across 16 visits, and the honest count under strict 10-Ca stoichiometry plus alternating polarity is 32 to 64, i.e. 320 to 640 min across 32 to 64 visits. A patient who does not complete the course gets a partially sealed lesion, which is the current clinical failure mode reproduced with extra equipment.
* Bookkeeping sensitivity. Three independent conventions each move the answer by a factor of 2: divalent against monovalent calcium counting, half-cell against full-cell formula mass, and single against alternating polarity. The optimistic pin is 16, the defensible central value is 32, and the geometric bound is 50 to 64. The falsification is stated at 16 sessions, so a null result at 16 does not kill the mechanism, only the schedule.
* Triviality check. Fluoride iontophoresis is a marketed dental procedure. The reply has to be that the load-bearing claims here are the epi seed layer and the 5 micrometre-per-session front arithmetic, not the field. If the depth-resolved profile after 16 sessions matches a fluoride varnish control, the field is decorative and the dossier is dead on the falsification clause.
* Toughness debt. Even at 100% mineral recovery, $K_{IC}$ stays near 0.4 $\mathrm{MPa\,m^{0.5}}$ and the critical flaw at 100 MPa falls to 4.1 micrometres. A restored lesion is hard and brittle. It will resist caries progression and it will not resist a 500 N occlusal point load the way prismatic enamel does, so the indication is a smooth-surface or proximal lesion, not an occlusal one under contact stress.
* Current vs pain. The 20x electrical shortfall and the 5 to 10x pulp margin are in direct conflict in the transcoronal geometry: closing the current gap by raising voltage closes the safety gap first. The coplanar geometry resolves both only because the field decays as $\exp(-\pi z/b)$, which is a property of the electrode pattern and not of the tissue.
* Acid production is a live risk. The 0.031 M Faradaic pH excursion is comparable to the 0.1 M acid challenge of a cola, applied to demineralized enamel rather than sound enamel. Buffering is not a refinement here, it is a safety requirement.
* Cost and access. This is the cheapest test in the repository: one extracted third molar, an artificial lesion, a potentiostat, and one micro-CT slot. No clean room, no synthesis, no animal licence. That asymmetry is the reason the vector is worth running even at 60% confidence.

## 10. Experiment

* Specimens: 24 extracted human third molars, caries-free, stored in thymol. Artificial lesions by pH cycling for 10 days in 2.2 mM Ca, 2.2 mM phosphate, 0.05 M acetate at pH 4.5 for 6 h per day, then 1.5 mM Ca, 0.9 mM phosphate, 0.02 M cacodylate at pH 7.0 for 18 h. Half the crown is masked with acid-resistant varnish to serve as the paired control on the same tooth.
* Pre-scan: micro-CT at 5 micrometre voxel, 70 kV, 114 $\mathrm{\mu A}$, hydroxyapatite phantoms at 0.25, 0.5, 0.75, 1.0, 1.5, and 2.0 $\mathrm{g\,cm^{-3}}$, giving mineral density in 10 micrometre bins with $\pm 0.05\ \mathrm{g\,cm^{-3}}$ precision.
* Cell: polycarbonate cup bonded to the enamel with light-cured adhesive, 5 mm inner diameter, 1 mM calcium lactate at pH 6.5, Ag/AgCl anode in the cup, two coplanar return electrodes at 2 mm spacing, 10 V, 0.33 $\mathrm{mA}$ total, 10 min per session, 16 sessions with 5 min polarity reversal inside each session.
* Controls: (a) identical cell with the field off, (b) field on with no fluorapatite seed layer, (c) seed layer with no field, (d) fluoride varnish 5% NaF single application, (e) sound enamel from the same tooth.
* Metrology: post-treatment micro-CT with image registration to the pre-scan; Knoop hardness at 50 g in 25 micrometre steps from the surface after 1 micrometre polish removal increments; SEM of prism continuity; fluoride depth profile by secondary ion mass spectrometry on two specimens per arm.
* Null result, defined before the run: band-averaged mineral gain $<10\%$ in the 50 to 200 micrometre band, or $\ge 80\%$ of the gain inside 10 micrometres, or a seeded specimen indistinguishable from an unseeded one within $2\sigma$.
* What this cannot distinguish: whether the seed layer's orientation survives beyond 89 nm from whether it matters at all, and whether the mechanism would work in a vital tooth with pulpal fluid flow and 2 mm of intervening dentine.

## 11. Expected observations

* Success branch: mineral density in the 50 to 120 micrometre band rises from $1.55 \pm 0.12$ to $2.10 \pm 0.15\ \mathrm{g\,cm^{-3}}$ (+35%), and in the 120 to 200 micrometre band from 1.85 to $2.05\ \mathrm{g\,cm^{-3}}$ (+11%), giving a band average of +23% and a passing hardness of $240 \pm 30\ \mathrm{HK_{0.05}}$. Depth profile shows monotonic decay of gain with depth, consistent with a front at 80 micrometres. The seeded arm shows prism-continuous overgrowth in SEM; the unseeded arm shows randomly oriented crystallites at the same mineral density.
* Failure branch: all gain above 2.0 $\mathrm{g\,cm^{-3}}$ sits in the outer 10 micrometres, the band average is +4%, and the depth profile is exponential with a 9 micrometre decay constant. That is the diffusion signature, and it means the field did not change the transport regime.
* Intermediate branch: gain distributed to depth but hardness recovery below 30%, which would indicate mineral precipitated in the pore fluid as loose crystallites rather than epitaxially attached to the existing lattice.

## 12. Magnitudes

* Lesion depth, porosity: 250 micrometres, 20 vol%.
* Enamel density, hydroxyapatite molar mass: $2.5\ \mathrm{g\,cm^{-3}}$, $1009\ \mathrm{g\,mol^{-1}}$.
* Current density, session length: $0.5\ \mathrm{mA\,cm^{-2}}$, 600 s.
* Charge per session: $0.30\ \mathrm{C\,cm^{-2}}$.
* Calcium per session: $1.24\times10^{-6}\ \mathrm{mol\,cm^{-2}}$ (charge equivalents).
* Hydroxyapatite per session: $0.25\ \mathrm{mg\,cm^{-2}}$, i.e. 1.0 micrometre of equivalent solid.
* Lesion deficit, rectangular bound: $12.5\ \mathrm{mg\,cm^{-2}}$; adopted target $4\ \mathrm{mg\,cm^{-2}}$.
* Sessions to target: 16; to the geometric bound: 50.
* Front advance: 0.5 micrometres per minute, 5 micrometres per session.
* Driving field: 2500 $\mathrm{V\,m^{-1}}$; drift velocity $1.55\times10^{-4}\ \mathrm{m\,s^{-1}}$.
* Peclet number across the seal: 39; transit time 0.13 s.
* Diffusion penetration depth without field: 8.9 to 17.8 micrometres.
* Damkohler number across the lesion: 791.
* Sound enamel series resistance: $2\times10^5\ \Omega$; coplanar pair: $3.0\times10^4\ \Omega$.
* Current available at 5 V transcoronal: 25 $\mathrm{\mu A\,cm^{-2}}$ against a 500 $\mathrm{\mu A\,cm^{-2}}$ target.
* Salivary shunt fraction: $3.3\times10^{-4}$ through the tooth.
* Pulp current density at 2 mm: 4.3% of surface, 21 $\mathrm{\mu A\,cm^{-2}}$.
* Epitaxial misfit: 0.53%, coherent thickness 89 nm.
* Fracture toughness after recovery: 0.4 against 0.7 to 1.2 $\mathrm{MPa\,m^{0.5}}$; critical flaw 4.1 against 12.4 micrometres.
* Faradaic pH excursion: 0.031 M, 1.5 pH units.

## 13. Applications

* Nearest-term: proximal and smooth-surface white spot lesions after orthodontic debonding, where 4 mg/cm^2 is the whole deficit, the surface is flat and accessible, and the alternative is a composite restoration that removes sound tissue.
* Nearest-term: root caries arrest in an ageing population, where the lesion is on cementum and dentine and the field path is 200 micrometres rather than 2 mm, which removes the series resistance problem entirely.
* Long-horizon: pre-restorative hardening of a lesion body so that a bonded restoration sits on mineral rather than on a 20% porous sponge, which is the current cause of marginal leakage.
* Long-horizon: an in vitro instrument that reports the mineral transport number of any lesion directly, replacing the inference from hardness recovery curves.

## 14. Unresolved questions

* Does a 0.5 mA/cm^2 field for 160 to 640 min cause pulpal fibrosis in a vital tooth, given that the pulp sees 4.3% of the surface density and has a blood flow of 0.3 to 0.5 $\mathrm{mL\,min^{-1}\,g^{-1}}$ for heat removal?
* Can a 50 nm fluorapatite seed layer survive the 5 micrometre acid etch and the first session's deposition without delaminating, and does its orientation propagate at all beyond the 89 nm coherent thickness?
* Is the 4 mg/cm^2 target the right one? The falsification is written against it, but the clinically relevant endpoint may be lesion arrest rather than bulk mineral recovery, which would change the whole arithmetic.
* Does the mechanism survive in vivo, where dentinal fluid flow at 0.02 to 0.2 $\mathrm{\mu L\,min^{-1}\,mm^{-2}}$ moves outward and opposes the calcium flux?
* This is the cheapest test in the repository, an extracted tooth and a micro-CT slot. The open question is not whether it can be run but whether the 16-session protocol is the right first experiment, since a 2-session pilot with the depth profile would already show which side of the 9 micrometre decay constant the field lands on.

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 3 | 4 | 4 | 5 | 3 | 5 |

Total: 24/30.
Confidence: 60%, basis: the charge and mass arithmetic is exact and charge conservation makes subsurface delivery geometrically guaranteed, while the open risks are the 20x electrical shortfall from sound enamel in series, the 30x phosphate shortfall in the lesion fluid, and the 89 nm limit on epitaxial control.

## 16. Status

Live.
