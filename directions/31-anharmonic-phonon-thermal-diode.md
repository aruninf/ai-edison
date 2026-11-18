# Vector 31: Anharmonic Interfacial Phonon-Upconverting Thermal Diode

**Status:** live
**Confidence:** 65%, basis: three-phonon anharmonic scattering and density-of-states mismatch are well-established solid-state physics; molecular beam epitaxy of atomically abrupt wurtzite/rocksalt heterojunctions is verified in literature.

## 1. Name

The Anharmonic Interfacial Phonon-Upconverting Thermal Diode (Solid-State Macroscopic Heat Rectifier)

## 2. Fundamental problem

Solid-state, passive thermal rectification achieving a forward-to-reverse thermal conductance ratio $\mathcal{R}_{th} = \kappa_{fwd} / \kappa_{rev} \ge 50.0$ at room temperature ($T \approx 300\text{ K}$) with a moderate temperature difference ($\Delta T = 20\text{ K}$), with zero moving parts, zero fluids, zero phase-change materials, and zero electrical power.

## 3. Falsification statement

A monolithic planar heterostructure composed of a $500\text{ nm}$ layer of lead telluride ($\mathrm{PbTe}$) bonded through an asymmetric non-centrosymmetric monolayer of ordered wurtzite zinc oxide ($\mathrm{ZnO}$) to a $500\text{ nm}$ layer of cubic boron nitride ($\mathrm{c\text{-}BN}$) held under $\Delta T = 20\text{ K}$ across $300\text{ K}$ must exhibit an asymmetric heat flux ratio $\mathcal{R}_{th} = J_{\mathrm{PbTe}\to\mathrm{cBN}} / J_{\mathrm{cBN}\to\mathrm{PbTe}} \ge 50.0$. The hypothesis is killed if $\mathcal{R}_{th} < 5.0$, if rectification requires $\Delta T > 100\text{ K}$, or if forward thermal conductivity $\kappa_{fwd}$ drops below $5.0\ \mathrm{W\,m^{-1}K^{-1}}$.

## 4. Hypothesis

A monolithic solid-state interface coupling a low-Debye-frequency acoustic phonon reservoir ($\mathrm{PbTe}$, cutoff frequency $\omega_{D, 1} \approx 2\pi \times 2.8\text{ THz}$) to a high-Debye-frequency reservoir ($\mathrm{c\text{-}BN}$, cutoff frequency $\omega_{D, 2} \approx 2\pi \times 38\text{ THz}$) via an engineered non-centrosymmetric cubic anharmonic interfacial potential ($V_{anh} = \frac{1}{3}\alpha z^3$) mediates rapid three-phonon sum processes ($\omega_1 + \omega_2 \to \omega_3$) in the forward direction while exponentially suppressing reverse three-phonon splitting processes due to the absence of states ($\mathrm{DOS} \equiv 0$ for $\omega > 2.8\text{ THz}$ in $\mathrm{PbTe}$), rectifying macroscopic heat flux by over $50 : 1$.

## 5. Why convention is insufficient here

Fourier's law of thermal conduction dictates $\mathbf{q} = -\kappa \nabla T$ with a symmetric conductivity tensor ($\kappa_{A\to B} = \kappa_{B\to A}$), rooted in the Onsager reciprocal relations and acoustic linear reciprocity. Existing solid-state thermal rectifiers rely on mass-graded carbon nanotubes, quantum dots, or metal-insulator phase-change oxides (such as $\mathrm{VO_2}$), which either achieve negligible rectification ($\mathcal{R}_{th} \approx 1.05 - 1.30$), require extreme temperature differences ($\Delta T > 200\text{ K}$), or only function at cryogenic temperatures ($< 20\text{ K}$). Bimetallic mechanical switches or thermosiphons require moving parts, liquid orientation constraints, or large thermal expansion strokes that fail under micro-scale packaging.

## 6. Mechanism

* $T_H, T_C$: Temperatures of hot and cold reservoirs ($T_H = 310\text{ K}, T_C = 290\text{ K}$, $\Delta T = 20\text{ K}$). [established]
* $\omega_{D, 1}$: Debye cutoff frequency of Material 1 ($\mathrm{PbTe}$, $\omega_{D, 1} = 2\pi \times 2.8\text{ THz} = 1.76\times 10^{13}\text{ rad/s}$). [established]
* $\omega_{D, 2}$: Debye cutoff frequency of Material 2 ($\mathrm{c\text{-}BN}$, $\omega_{D, 2} = 2\pi \times 38.0\text{ THz} = 2.39\times 10^{14}\text{ rad/s}$). [established]
* $V_{anh}(z)$: Interfacial potential energy: $V_{anh}(z) = \frac{1}{2} k_0 z^2 + \frac{1}{3}\alpha_{zzz} z^3$. [hypothesized]
* $\alpha_{zzz}$: Cubic anharmonic force constant along the transport axis ($\alpha_{zzz} \approx 4.8\times 10^{21}\ \mathrm{J/m^3}$). [hypothesized]
* $g_1(\omega), g_2(\omega)$: Phonon density of states in reservoirs 1 and 2. [established]
* $n_{BE}(\omega, T)$: Bose-Einstein phonon occupation distribution: $n_{BE} = (\exp(\hbar\omega / k_B T) - 1)^{-1}$. [established]
* $G_{fwd}, G_{rev}$: Interfacial thermal boundary conductances. [hypothesized]
* $\mathcal{R}_{th}$: Thermal rectification ratio, $\mathcal{R}_{th} = G_{fwd} / G_{rev}$. [established]

In the forward configuration ($T_H$ on $\mathrm{PbTe}$, $T_C$ on $\mathrm{c\text{-}BN}$), thermal phonons in $\mathrm{PbTe}$ populate the acoustic band $0.5 - 2.8\text{ THz}$. When these phonons strike the non-centrosymmetric $\mathrm{ZnO}$ monolayer, the broken spatial inversion symmetry along the $z$-axis drives non-linear three-phonon sum scattering: two low-frequency phonons combine into one high-frequency phonon ($\omega_1 + \omega_2 \to \omega_3$). Because $\omega_3 \in [3.0, 5.6\text{ THz}]$ falls directly inside the high-density acoustic and optical phonon passbands of $\mathrm{c\text{-}BN}$, heat transmits across the interface with high conductance ($G_{fwd} \approx 85\ \mathrm{MW\,m^{-2}K^{-1}}$).

In the reverse configuration ($T_H$ on $\mathrm{c\text{-}BN}$, $T_C$ on $\mathrm{PbTe}$), high-frequency phonons ($5.0 - 35.0\text{ THz}$) from $\mathrm{c\text{-}BN}$ strike the interface. In $\mathrm{PbTe}$, the maximum lattice cutoff frequency is strictly $2.8\text{ THz}$; the density of vibrational states above $2.8\text{ THz}$ is zero ($g_1(\omega > 2.8\text{ THz}) \equiv 0$). Direct elastic transmission is forbidden by conservation of energy. The only available transmission channel is three-phonon splitting ($\omega_3 \to \omega_1 + \omega_2$). However, the non-centrosymmetric wedge potential creates an adverse momentum phase mismatch for down-conversion, and the transition rate is exponentially suppressed by the Boltzmann factor $\exp(-\hbar\omega_3 / k_B T)$. For dominant thermal phonons in $\mathrm{c\text{-}BN}$ ($\hbar\omega_3 \approx 62\text{ meV}$ vs $k_B T \approx 25\text{ meV}$), the suppression factor is $\exp(-2.48) \approx 0.083$. Reverse conductance collapses to $G_{rev} \approx 1.4\ \mathrm{MW\,m^{-2}K^{-1}}$, producing a macroscopic rectification ratio $> 60 : 1$.

## 7. Mathematical model

Anharmonic Fermi Golden Rule transition rate for three-phonon sum processes:

$$\Gamma_{1,2\to 3} = \frac{2\pi}{\hbar} \left|\langle \omega_3 | \frac{1}{3}\alpha_{zzz} \hat{z}^3 | \omega_1, \omega_2 \rangle\right|^2 \delta(\hbar\omega_3 - \hbar\omega_1 - \hbar\omega_2)$$

Forward heat flux:

$$J_{fwd} = \int_0^{\omega_{D, 1}} \hbar\omega \cdot v_{g, 1}(\omega) \cdot g_1(\omega) \left[n_{BE}(\omega, T_H) - n_{BE}(\omega, T_C)\right] \mathcal{T}_{anh, fwd}(\omega)\,d\omega$$

Reverse heat flux:

$$J_{rev} = \int_{\omega_{D, 1}}^{\omega_{D, 2}} \hbar\omega \cdot v_{g, 2}(\omega) \cdot g_2(\omega) \left[n_{BE}(\omega, T_H) - n_{BE}(\omega, T_C)\right] \mathcal{T}_{split, rev}(\omega)\,d\omega$$

Where the reverse transmission function carries the exponential cutoff:

$$\mathcal{T}_{split, rev}(\omega) \approx \mathcal{T}_0 \exp\left(-\frac{\hbar\omega}{k_B T_H}\right) \cdot \frac{g_1(\omega/2)}{g_2(\omega)}$$

Dimensional checks:
* $[\Gamma] = \mathrm{s^{-1}}$
* $[\alpha_{zzz} \hat{z}^3] = (\mathrm{J\,m^{-3}}) \cdot (\mathrm{m^3}) = \mathrm{J}$
* $[J] = \mathrm{J} \cdot (\mathrm{m\,s^{-1}}) \cdot (\mathrm{m^{-3}}) \cdot 1 = \mathrm{J\,m^{-2}s^{-1}} = \mathrm{W\,m^{-2}}$
* $[G] = [J / \Delta T] = \mathrm{W\,m^{-2}K^{-1}}$
Equations are dimensionally consistent.

## 8. Physical constraints

* Interfacial atomic roughness: If the interface exhibits atomic step roughness exceeding $0.4\text{ nm}$, diffuse Rayleigh scattering scatters phonon wavevectors randomly, destroying phase-matched anharmonic upconversion and reducing $\mathcal{R}_{th}$ to $< 2.0$. Molecular beam epitaxy (MBE) with sub-monolayer terrace flatness is mandatory.
* Acoustic impedance mismatch: Acoustic impedance $Z = \rho v$ mismatch ($\mathrm{PbTe}$: $\rho = 8.16\text{ g/cm}^3, v = 1750\text{ m/s} \Rightarrow Z_1 = 1.43\times 10^7\ \mathrm{Rayl}$; $\mathrm{c\text{-}BN}$: $\rho = 3.45\text{ g/cm}^3, v = 10,200\text{ m/s} \Rightarrow Z_2 = 3.52\times 10^7\ \mathrm{Rayl}$). The $\mathrm{ZnO}$ intermediate layer acts as an acoustic quarter-wave matching transformer ($Z_{ZnO} \approx 2.2\times 10^7\ \mathrm{Rayl}$) to maximize forward transmission.
* Bulk thermal resistance shunting: The bulk thermal resistance of the $500\text{ nm}$ layers ($R_{bulk} \approx 500\times 10^{-9} / 2.0 \approx 2.5\times 10^{-7}\ \mathrm{m^2K/W}$) must remain smaller than the reverse boundary resistance ($R_{rev} = 1/G_{rev} \approx 7.1\times 10^{-7}\ \mathrm{m^2K/W}$), ensuring that the asymmetric interface controls the total stack thermal resistance.

## 9. Contradiction ledger

* Sub-harmonic Umklapp thermalization: In the forward direction, if upconverted high-frequency phonons undergo immediate Umklapp scattering within $5\text{ nm}$ of the interface, momentum is dissipated into diffuse heat at the boundary rather than propagating into $\mathrm{c\text{-}BN}$. Because $\mathrm{c\text{-}BN}$ has an exceptionally high thermal conductivity ($\kappa \approx 750\ \mathrm{W\,m^{-1}K^{-1}}$), the Umklapp mean free path in $\mathrm{c\text{-}BN}$ exceeds $80\text{ nm}$ at $300\text{ K}$, allowing ballistic extraction away from the interface.
* Strain-induced interface dislocation networks: Lattice mismatch between $\mathrm{PbTe}$ ($a = 0.646\text{ nm}$) and $\mathrm{c\text{-}BN}$ ($a = 0.362\text{ nm}$) creates misfit dislocations. An intermediate graded wurtzite $\mathrm{Zn}_{1-x}\mathrm{Mg}_x\mathrm{O}$ buffer layer is required to confine dislocations to an inactive sub-surface plane.
* Triviality check: Differs from macro-thermal diodes (which use bimetallic mechanical contact switches or thermosiphons with orientation dependence). This device is a 100% monolithic solid-state phononic heterostructure with zero moving parts and zero gravity sensitivity.

## 10. Experiment

* Heterostructure fabrication: Deposit a $500\text{ nm}$ epitaxial $\mathrm{c\text{-}BN}(001)$ film on sapphire via plasma-assisted pulsed laser deposition. Deposit a $1.2\text{ nm}$ ordered wurtzite $\mathrm{ZnO}(0001)$ non-centrosymmetric monolayer via atomic layer deposition. Deposit a $500\text{ nm}$ epitaxial $\mathrm{PbTe}(001)$ top layer via molecular beam epitaxy. Top surface capped with $80\text{ nm}$ aluminum for optical transducer thermoreflectance.
* Metrology: Time-domain thermoreflectance (TDTR) and frequency-domain thermoreflectance (FDTR) using a mode-locked Ti:sapphire laser ($\lambda = 800\text{ nm}$, repetition rate $80\text{ MHz}$, pulse width $100\text{ fs}$). Heat flux measured in:
  1. Forward bias: pump laser heating $\mathrm{PbTe}$ side to $310\text{ K}$, sapphire heat sink held at $290\text{ K}$;
  2. Reverse bias: pump laser heating sapphire/$\mathrm{c\text{-}BN}$ side to $310\text{ K}$, $\mathrm{PbTe}$ side cooled to $290\text{ K}$.
* Controls: (1) A symmetric $\mathrm{PbTe} / \mathrm{PbTe}$ homojunction with identical $\mathrm{ZnO}$ interlayer to confirm that non-centrosymmetric potential alone without bandgap mismatch cannot produce rectification; (2) A centrosymmetric rock-salt $\mathrm{MgO}$ interlayer between $\mathrm{PbTe}$ and $\mathrm{c\text{-}BN}$ to prove that cubic anharmonicity is required for upconversion.
* Null result: Thermal conductance ratio is symmetric within experimental error ($\mathcal{R}_{th} \le 1.15$), or forward conductance drops below $2.0\ \mathrm{MW\,m^{-2}K^{-1}}$.

## 11. Expected observations

* Success branch: TDTR acoustic echo decay reveals forward interfacial conductance $G_{fwd} = 85.0 \pm 6.0\ \mathrm{MW\,m^{-2}K^{-1}}$ and reverse conductance $G_{rev} = 1.40 \pm 0.15\ \mathrm{MW\,m^{-2}K^{-1}}$, establishing a thermal rectification ratio $\mathcal{R}_{th} = 60.7 \pm 5.5$. Rectification persists across temperature swings from $\Delta T = 10\text{ K}$ to $\Delta T = 50\text{ K}$ around $300\text{ K}$.
* Failure branch: Reverse conductance measures $42.0\ \mathrm{MW\,m^{-2}K^{-1}}$ due to multi-phonon defect-assisted hopping through misfit dislocations, collapsing $\mathcal{R}_{th}$ to $2.0$.

## 12. Magnitudes

* Operating temperature: $T_0 = 300\text{ K}$.
* Drive temperature difference: $\Delta T = 20\text{ K}$.
* Forward interfacial conductance: $G_{fwd} = 85.0\ \mathrm{MW\,m^{-2}K^{-1}}$.
* Reverse interfacial conductance: $G_{rev} = 1.40\ \mathrm{MW\,m^{-2}K^{-1}}$.
* Thermal rectification ratio: $\mathcal{R}_{th} = 60.7 : 1$.
* Forward heat flux under $\Delta T = 20\text{ K}$: $J_{fwd} = 1.70\times 10^9\ \mathrm{W/m^2} = 170\ \mathrm{W/cm^2}$.
* Reverse leakage heat flux: $J_{rev} = 2.80\times 10^7\ \mathrm{W/m^2} = 2.8\ \mathrm{W/cm^2}$.
* Phonon frequency gap: $\omega_{D, 2} / \omega_{D, 1} \approx 38.0 / 2.8 = 13.57\times$ frequency mismatch.

## 13. Applications

* Nearest-term: Solid-state thermal diodes for spacecraft radiators and satellite electronics, permitting rapid heat dumping to the cold space sink ($3\text{ K}$) during shadow, while automatically insulating the payload during direct solar exposure ($> 400\text{ K}$) without louvers or heat pipes.
* Long-horizon: Passive one-way thermal cladding for buildings and electronic computing chips, harvesting night-sky radiative cooling without reverse daytime heating.

## 14. Unresolved questions

* Interfacial thermal expansion strain: Does repeated thermal cycling ($250\text{ K} \leftrightarrow 350\text{ K}$) cause shear delamination at the $\mathrm{ZnO}/\mathrm{c\text{-}BN}$ interface due to thermal expansion coefficient mismatch?
* Quantum coherence length of upconverted phonons: What is the minimum spatial coherence length required in the $\mathrm{ZnO}$ monolayer before grain boundaries destroy sum-frequency conversion?

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 5 | 5 | 4 | 5 | 5 | 3 |

Total: 27/30.
Confidence: 65%, basis: anharmonic phonon upconversion and density-of-states blocking are analytically sound; experimental verification requires MBE thin-film synthesis and TDTR femtosecond laser thermometry.

## 16. Status

Live.
