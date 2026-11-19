# Vector 51: Coincidence-Gated Sub-Threshold Acoustic Ablation

**Status:** live
**Confidence:** 58%, basis: linear superposition ($N p_1 = 6 \times 2.0 = 12.0\text{ MPa}$) and the Blake threshold inversion that returns a 25 nm nucleus radius from a 2.2 MPa threshold are both exact; the unmeasured quantity that carries the whole safety claim is the width of the cavitation threshold step, and the arithmetic below shows the pinned 9% beam margin yields a volume selectivity of $7 \times 10^{-3}$, not $10^4$, unless that step is 118 kPa wide or narrower.

## 1. Name

The Coincidence-Gated Sub-Threshold Acoustic Ablation (Mechanical Cavitation Selectivity From $N$-Fold Pressure Superposition Below a Tissue Threshold)

## 2. Fundamental problem

Destroy a defined volume of diseased tissue at 12 cm depth, with no incision, with no imaging system good enough to resolve the target, and with zero damage to the tissue the beams cross on the way in and out. The stripped requirement is not "focus tightly"; it is "make the probability of damage at a point a step function of the number of beams present, so that the 6-beam set is damaging and every 1-beam subset is not".

## 3. Falsification statement

A 10% w/v polyacrylamide gel phantom, 120 mm thick, 1% v/v gas-loaded precursor, equilibrated to $10^6$ nuclei per mL, at $20\ ^\circ\mathrm{C}$, insonified at 1.0 MHz by six independently driven focused beams whose foci coincide within 0.2 mm:

1. Each single beam alone, at 2.0 MPa peak negative pressure, 2000 pulses of 20 $\mu$s at 1 Hz, produces no lesion detectable by 2,3,5-triphenyltetrazolium chloride staining or by optical transmittance at 600 nm (threshold: optical density change $< 0.02$ over the focal cylinder).
2. All six beams together at 2.0 MPa each (12.0 MPa at the focus) produce a lesion of diameter $2.0 \pm 0.4\text{ mm}$.
3. The lesion is confined: no lesion fragment larger than $0.3\text{ mm}$ appears outside a 3 mm sphere about the focus.

The hypothesis is killed if any single beam produces detectable cavitation (broadband emission above 10x the electronic noise floor, or any visible lesion), or if the six-beam lesion exceeds 4 mm in diameter. The first clause is the one that matters: it is a direct measurement of the threshold step width, not a check on the apparatus.

## 4. Hypothesis

Cavitation inception is a threshold, not a rate. A gas nucleus of radius $R_0$ either is driven past the Blake instability by the local peak negative pressure, in which case it grows inertially and kills the cells in a 50 $\mu$m neighbourhood, or it is not, in which case nothing happens at any exposure time. Six beams of 2.0 MPa each, individually 9.1% below the 2.2 MPa tissue threshold, superpose coherently to 12.0 MPa, which is 5.45x the threshold. Off-target tissue sees one beam and therefore sits 0.2 MPa below a step. The damage probability off target is not small, it is zero, by the same argument that a switch is off.

## 5. Why convention is insufficient here

Three deployed routes all fail the stated requirement, and they fail for reasons that are dimensional, not incremental.

Surgical resection fails the no-incision clause by definition and needs a 5 mm targeting accuracy that only imaging provides. Radiotherapy achieves selectivity through radiobiology (differential repair), not through geometry: a 2 Gy fraction deposits dose along the whole entrance path, the penumbra of a 6 MV beam is 6 to 8 mm at 10 cm depth, and the 2 mm target is not resolvable by the treatment head. Thermal HIFU fails because heat is diffusive. The thermal lesion size is set by the diffusion length:

$$L_{th} = \sqrt{4\alpha_{th} t} = \sqrt{4(1.3\times10^{-7})(100)} = 7.2\times10^{-3}\ \mathrm{m}$$

* $[L_{th}] = (\mathrm{m^2\,s^{-1}})(\mathrm{s})]^{1/2} = \mathrm{m}$. Check passes.

At $\alpha_{th} = 1.3\times10^{-7}\ \mathrm{m^2/s}$ and a 100 s dwell, heat spreads 7.2 mm, so a 2 mm thermal lesion is not available at any focal quality. Getting 2 mm requires $t \le 7.7\text{ s}$, which at the ablation temperature rise of 60 K demands 7.8 K/s in the target and therefore a 36x intensity concentration that coagulates the whole 7 mm entrance cone first. Thermal ablation is a diffusion-limited 7 mm technology. The 2 mm requirement is only reachable by a mechanism whose damage radius is set by a bubble, not by a diffusion length, and a bubble is 50 $\mu$m.

The nearest existing thing, single-focus histotripsy, already exploits a pressure threshold and therefore already delivers a step function at one focus. It works (lesions of 1 to 10 mm, at 25 to 30 MPa at 1 MHz in tissue), which is the load-bearing evidence that a threshold exists at all. It cannot do the 2 mm coincidence trick because it applies the whole threshold pressure on every path: the same 25 MPa that fires the focus fires the pre-focal tissue, and rib sparing is mandatory because a rib in the path absorbs and reflects enough to burn skin. The originality of this vector is therefore narrow and should be stated plainly: a threshold at a single focus is prior art; only the $N$-way coincidence scheme is not.

## 6. Mechanism

* $p_1$: peak negative pressure of one beam at the focus ($2.0\text{ MPa}$). [assumed, set by the design]
* $P_{th}$: tissue inertial cavitation threshold at 1.0 MHz ($2.2\text{ MPa}$). [assumed]
* $N$: number of independent beams ($N = 6$). [assumed]
* $f$: cavity drive frequency ($1.0\text{ MHz}$). [assumed]
* $\sigma_w$: water surface tension ($0.072\text{ N/m}$). [established]
* $P_0$: ambient pressure ($1.013\times10^{5}\text{ Pa}$). [established]
* $R_0$: radius of the gas nucleus that sets the threshold. [hypothesized, derived below as 25 nm]
* $n$: gas nucleus number density ($10^6\ \mathrm{mL^{-1}} = 10^{12}\ \mathrm{m^{-3}}$). [assumed]
* $r_k$: cell-kill radius of one inertial collapse ($50\ \mu\mathrm{m}$). [assumed, from histotripsy lesion dosimetry]
* $z$: depth ($0.12\text{ m}$). [assumed]
* $\alpha_a$: amplitude attenuation coefficient at 1 MHz ($5.76\ \mathrm{Np/m}$, i.e. 0.5 dB/cm). [established for soft tissue]

1. Each of six transducers launches a 1.0 MHz tone burst. Because the drive is monochromatic and phase-locked, the six complex pressures add at the common focus: $p_6 = 6 p_1 \cos(\omega t)$, with no envelope beating.
2. At the focus the peak negative pressure is 12.0 MPa. Away from the focus, at any point on any one beam path, only one beam is present and the local peak negative pressure is 2.0 MPa, below the threshold at every instant of every cycle.
3. The threshold is a property of the nucleus population, not of the tissue water. A 25 nm nucleus is unstable to growth when the local tension exceeds the Blake value, and once it passes, it grows by a factor near 2 per cycle, so five cycles take it to 800 nm, at which radius the Blake threshold is negligible and the collapse proceeds regardless of the drive. The step is sharp in pressure because the growth is autocatalytic in radius.
4. One inertial collapse kills cells within $r_k = 50\ \mu\mathrm{m}$. The nucleus spacing is $n^{-1/3} = 100\ \mu\mathrm{m}$, so the kill spheres of adjacent nuclei just touch. Complete ablation of the target volume follows from one collapse per nucleus, with no overlap requirement and no thermal cooperation.
5. Because the mechanism requires no heat, the thermal dose is a side effect to be suppressed, not the agent. At the stated 0.8 K per beam per treatment, the six-beam overlap would reach 28.8 K if the full dwell were delivered; the dose is therefore gated at cavitation onset (20 $\mu$s to 200 $\mu$s), where the per-pulse overlap rise is $2.6\times10^{-3}\text{ K}$.
6. Selectivity is set by the ratio of the overlap volume to the singly-insonified volume, scaled by the probability that a single beam fires the population anyway. That probability is the only soft number in the design, and it is what section 3 measures.

## 7. Mathematical model

Coherent superposition at the focus:

$$p_N = \left|\sum_{j=1}^{N} p_1 e^{i\phi_j}\right| = N p_1 = 6(2.0) = 12.0\ \mathrm{MPa}$$

* $[p_N] = \mathrm{Pa}$. Check passes. Phases are locked, so the sum is arithmetic, not root-sum-square. Were the six sources incoherent, $p_N = \sqrt{6}\,p_1 = 4.9\text{ MPa}$ and the design would not cross threshold at all; phase coherence is a hard requirement, not an optimisation.

Intensity and its $N^2$ scaling:

$$I = \frac{p^2}{2\rho c}, \qquad I_1 = \frac{(2.0\times10^{6})^2}{2(1000)(1540)} = 1.30\times10^{6}\ \mathrm{W/m^2} = 130\ \mathrm{W/cm^2}$$

* $[I] = \mathrm{Pa^2/(kg\,m^{-3}\cdot m\,s^{-1})} = \mathrm{kg\,m^{-1}s^{-2}} = \mathrm{W/m^2}$. Check passes.
* Overlap: $I_6 = 36 I_1 = 4.68\times10^{7}\ \mathrm{W/m^2} = 4680\ \mathrm{W/cm^2}$.

Blake threshold for a nucleus of radius $R_0$:

$$P_B - P_0 = \frac{4\sigma_w}{3R_0}\left[\frac{2\sigma_w}{3R_0(P_0 + 2\sigma_w/R_0)}\right]^{1/2}$$

* Bracket: $({\mathrm{Pa\,m}})/({\mathrm{m}\cdot\mathrm{Pa}})$ dimensionless. Prefactor: $\mathrm{Pa}$. Check passes.
* Inversion at $P_B - P_0 = 2.2\times10^{6}\ \mathrm{Pa}$ gives $R_0 = 25\ \mathrm{nm}$: with $2\sigma_w/R_0 = 5.76\times10^{6}\ \mathrm{Pa}$, the bracket is $[0.144/(7.5\times10^{-8}\cdot5.86\times10^{6})]^{1/2} = 0.572$, and $4\sigma_w/(3R_0) = 3.84\times10^{6}\ \mathrm{Pa}$, so the product is $2.20\times10^{6}\ \mathrm{Pa}$. The assumed threshold is exactly the Blake threshold of a 25 nm nucleus.
* In the Laplace-dominated regime ($2\sigma_w/R_0 \gg P_0$, true here at 5.76 MPa against 0.101 MPa) the bracket tends to $3^{-1/2}$ and

$$P_B - P_0 \approx \frac{4\sigma_w}{3\sqrt{3}\,R_0} = \frac{0.77\,\sigma_w}{R_0}$$

so the threshold scales as $R_0^{-1}$ and a fractional radius spread maps one-to-one onto a fractional threshold spread: $\delta P_B/P_B = \delta R_0/R_0$.

Quasi-static justification for using the Blake value at 1 MHz. The Rayleigh collapse time of a 25 nm bubble at 2.2 MPa is

$$t_c = 0.915\,R_0\sqrt{\frac{\rho}{\Delta P}} = 0.915(2.5\times10^{-8})\sqrt{\frac{1000}{2.2\times10^{6}}} = 4.9\times10^{-10}\ \mathrm{s}$$

* $[t_c] = \mathrm{m}\cdot(\mathrm{kg\,m^{-3}}/\mathrm{Pa})^{1/2} = \mathrm{m}\cdot(\mathrm{s^2/m^2})^{1/2} = \mathrm{s}$. Check passes.
* $t_c = 0.49\text{ ns}$ against a 500 ns rarefaction half-cycle, so the bubble equilibrates quasi-statically within the cycle and the static Blake criterion applies. The 1 MHz choice is not a resonance choice; it is set by attenuation and by the aperture needed for a 2 mm focus.

Selectivity by volume. Let $V_t$ be the target volume and $V_{off}$ the singly-insonified volume:

$$V_t = \frac{4}{3}\pi (1.0\times10^{-3})^{3} = 4.19\times10^{-9}\ \mathrm{m^3} = 4.19\ \mathrm{mm^3}$$

$$V_{off} = 6\left[\pi(1.0\times10^{-3})^{2}(0.12)\right] - V_t \approx 2.26\times10^{-6}\ \mathrm{m^3} = 2262\ \mathrm{mm^3}$$

* Both $\mathrm{m^3}$. The ratio $V_{off}/V_t = 540$.

Threshold step model. Let the local threshold be $P_{th}(1+\xi)$ with $\xi$ having a logistic step of half-width $w$ in pressure. A point at pressure $p$ fires with probability

$$p_{fire}(p) = \left[1 + \exp\left(\frac{P_{th} - p}{w}\right)\right]^{-1}$$

Off target, $p = (1-m)P_{th}$ with margin $m$; on target, $p \gg P_{th}$ so $p_{fire} \to 1$. Then

$$\mathcal{S} = \frac{V_t}{p_{fire,off}\,V_{off}}, \qquad p_{fire,off} = \left[1+\exp\left(\frac{m P_{th}}{w}\right)\right]^{-1}$$

* $\mathcal{S}$ dimensionless. Check passes.

Evaluated at the pinned geometry ($m = 0.091$, $w = 200\text{ kPa}$): $mP_{th}/w = 1.00$, $p_{fire,off} = 0.269$, $\mathcal{S} = 4.19/(0.269 \times 2262) = 6.9\times10^{-3}$. The pinned specification of $10^{4}$ therefore requires

$$w \le \frac{m P_{th}}{\ln\left(\mathcal{S}V_{off}/V_t - 1\right)} = \frac{(0.091)(2.2\times10^{6})}{\ln(5.4\times10^{6})} = \frac{2.0\times10^{5}}{15.5} = 1.3\times10^{4}\ \mathrm{Pa}$$

* $[w] = \mathrm{Pa}$. Check passes. So the threshold must be uniform to 13 kPa, which is 0.6% of 2.2 MPa, which by the $R_0^{-1}$ law means the gas nuclei must be monodisperse to 0.6% in radius. That is the true content of the safety claim, and it is not a property of any living tissue.

Optimising the margin instead of accepting $m = 0.091$. The focus must still cross threshold, so $m \le 1 - k/N$ with $k$ the required overdrive at the focus. Taking $k = 1.5$ and $N = 6$ gives $m \le 0.75$, whence $p_1 = 0.55\text{ MPa}$, $p_6 = 3.3\text{ MPa}$ (1.5x threshold), $mP_{th}/w = 8.25$, $p_{fire,off} = 2.6\times10^{-4}$, and $\mathcal{S} = 7.1$. Six beams cannot reach $10^{4}$ at $w = 200\text{ kPa}$ for any margin, because the maximum achievable margin is bounded by $1 - k/N$. Required $N$ for $\mathcal{S} = 10^{4}$ at $w = 200\text{ kPa}$ and $k = 1.5$:

$$N_{min} = \frac{k}{1 - w\ln(\mathcal{S}V_{off}/V_t - 1)/P_{th}} = \frac{1.5}{1 - (2.0\times10^{5})(15.5)/(2.2\times10^{6})} = \frac{1.5}{1-1.41}$$

The denominator is negative, so no $N$ works: at $w = 200\text{ kPa}$ the required margin exceeds unity and $10^{4}$ is unreachable at any beam count. The corrected design point that does work has $w \le 100\text{ kPa}$, giving $N \ge 7$ with 0.65 MPa per beam and 4.55 MPa at the focus. That is a different machine from the pinned one, and the difference is the whole result of this section.

Cavity coverage and nucleus density. One collapse kills a sphere of volume $\frac{4}{3}\pi r_k^3 = 5.24\times10^{-13}\ \mathrm{m^3}$, so complete coverage needs

$$n \ge \frac{1}{\tfrac{4}{3}\pi r_k^3 \cdot 8} = \frac{1}{8(5.24\times10^{-13})} = 2.4\times10^{11}\ \mathrm{m^{-3}} = 2.4\times10^{5}\ \mathrm{mL^{-1}}$$

* $[n] = \mathrm{m^{-3}}$. Check passes. The pinned $10^{6}\ \mathrm{mL^{-1}}$ is 4.2x this floor, so the target volume holds $4.19\times10^{-9}\times10^{12} = 4190$ nuclei against 4190 required kill spheres: the density is exactly at the geometric threshold, which is why the phantom's nucleus count must be measured, not assumed.

Depth attenuation. One-way amplitude loss at 12 cm:

$$p(z) = p_0 e^{-\alpha_a z}, \qquad \alpha_a z = (5.76)(0.12) = 0.691\ \mathrm{Np} = 6.0\ \mathrm{dB}$$

* $[\alpha_a z]$ dimensionless. Check passes. Amplitude factor $e^{-0.691} = 0.50$, so a 2.0 MPa focal pressure needs 4.0 MPa at the face before focal gain. For a 110 mm aperture at F/1.1 the focal pressure gain is $G = \pi a^2/(\lambda z) = \pi(0.055)^2/(1.54\times10^{-3}\times0.12) = 51$, so the face pressure is 78 kPa (8 W/cm$^2$), well inside transducer limits.

Aperture geometry. A 2 mm focal spot at 1 MHz needs $-6$ dB width $1.2\lambda F\# = 2\text{ mm}$, hence $F\# = 1.08$ and a 110 mm aperture at 120 mm range. Six such apertures converging on one point require a 220 mm coupling surface. That is available on a gel phantom and on a limb, not on a torso, and it is recorded as a constraint rather than hidden.

Thermal accounting. Volumetric heating $q = 2\alpha_a I_1 = 2(5.76)(1.30\times10^{6}) = 1.50\times10^{7}\ \mathrm{W/m^3}$, so

$$\frac{dT}{dt} = \frac{q}{\rho c_p} = \frac{1.50\times10^{7}}{(1000)(4180)} = 3.58\ \mathrm{K/s}$$

* $[\dot T] = (\mathrm{W\,m^{-3}})/(\mathrm{J\,m^{-3}K^{-1}}) = \mathrm{K/s}$. Check passes. Over the cavitation latency of 20 $\mu$s the per-beam rise is $7.2\times10^{-5}$ K and the overlap rise is 36x that, $2.6\times10^{-3}$ K. Reaching the stated 0.8 K per beam requires 0.223 s of accumulated insonation, which is 11 000 pulses at 20 $\mu$s: that is the dose budget the 0.8 K refers to.

## 8. Physical constraints

* Phase coherence is not optional. If the six sources drift by more than $\lambda/8 = 19\ \mu\mathrm{m}$ in path, the focus sum falls by $\cos(\pi/4) = 0.71$ and $p_6$ drops to 8.5 MPa; a $\lambda/2$ drift nulls the sum entirely. Six independent 1 MHz oscillators must be locked to a common reference with $< 5$ ns jitter, which is 0.5% of a period. This is achievable with a single clock and is not achievable with six free-running drivers.
* Threshold uniformity. From section 7, $10^{4}$ volume selectivity needs $w \le 13\ \mathrm{kPa}$ and hence nucleus monodispersity to 0.6%. Living tissue is not monodisperse: nucleus radii span 10 to 100 nm, a factor of 10, which by $R_0^{-1}$ is a factor of 10 in threshold, i.e. $w \approx 1\ \mathrm{MPa}$. At $w = 1\ \mathrm{MPa}$ and optimal $m = 0.75$ the off-target fire probability is $1/(1+e^{1.65}) = 0.16$ and $\mathcal{S} = 0.012$. The device as pinned is selective in the wrong direction.
* Nucleus depletion. Each collapse consumes a nucleus. The 4190 nuclei in the target are consumed in one pulse train; subsequent pulses have nothing to fire on until gas diffuses back in, which takes $R_0^2/D = (2.5\times10^{-8})^2/(2\times10^{-9}) = 3.1\times10^{-7}\text{ s}$, i.e. sub-microsecond. Replenishment is therefore fast and the treatment is not self-limiting, which is good for dose and bad for the "one collapse per nucleus" completeness argument, since later pulses fire new nuclei whose kill spheres are offset.
* Nucleus lifetime without the acoustic field. A 25 nm bubble dissolves by Epstein-Plesset in $R_0^2\rho/(2D\Delta C) \approx 3\times10^{-3}\text{ s}$. Nuclei at $10^{6}\ \mathrm{mL^{-1}}$ therefore cannot exist as free bubbles; they must be crevice-stabilized on hydrophobic surfaces or coated. In blood and in most soft tissue the stabilisation is unknown, and if the effective count falls below $2.4\times10^{5}\ \mathrm{mL^{-1}}$ the ablation becomes incomplete rather than zero.
* Depth and path. At 12 cm the six paths differ. Through 5 mm of rib the one-way loss at 1 MHz is 8 to 12 dB with 20% phase aberration, so that beam's focal amplitude falls by 1.6 to 2.5x. A $\pm 2$ dB spread across the six paths changes $p_6$ by $\pm 26\%$: 12.0 MPa becomes 8.9 to 15.1 MPa. The focus also walks by 1 to 3 mm because the amplitude-weighted centroid moves. Path-dependent dose is therefore a first-order effect, not a correction.
* Geometry at depth. Six 110 mm apertures on a 120 mm radius cannot be placed on a human abdomen. Either the frequency is raised (3 MHz halves $\lambda$ and the aperture to 37 mm, at the cost of 16.5 dB one-way loss and a required 6.7x more face pressure) or the target is restricted to limbs and the head. This vector is a limb and ex-vivo device until the aperture problem is solved.
* No imaging resolution is not the same as no targeting. The coincidence volume is defined by geometry to 0.2 mm, but its position in the body is known only to the accuracy of the frame. A targeting error of 5 mm puts the 2 mm lesion in healthy tissue with full selectivity, which is to say the device is precise and misaimed.

## 9. Contradiction ledger

* Triviality check (strongest attack): single-focus histotripsy already exploits a cavitation threshold, and the claim that a threshold produces a step function is prior art from 2004 onward. The reply is narrow and must be conceded: what is new is only the coincidence scheme, i.e. the use of $N$ sub-threshold beams rather than one supra-threshold beam. That buys off-target safety on the entrance paths only if the threshold step is much narrower than the per-beam margin, which section 7 shows it is not at $w = 200\text{ kPa}$. The vector's originality is therefore 4 and not 5, and it rests on a measurement that has not been made.
* Threshold step width is the kill parameter. Every safety number in this dossier is $1+e^{mP_{th}/w}$. At $w = 200\text{ kPa}$ the design gives $\mathcal{S} = 7\times10^{-3}$. At $w = 50\text{ kPa}$ it gives $\mathcal{S} = 3.4\times10^{2}$. At $w = 13\text{ kPa}$ it gives $10^{4}$. The single unmeasured quantity spans six orders of magnitude of the headline claim, and no published measurement of the in vivo step width at 1 MHz is available to this design. The falsification experiment is therefore not a confirmation step, it is the measurement.
* Differential attenuation along the six paths makes the overlap dose path dependent. With ribs in 2 of 6 paths, the focal sum is $p_6 = 12.0 \pm 3.1\text{ MPa}$ and the effective overdrive $k$ varies from 2.5 to 4.5. Since $m \le 1-k/N$ and $k$ is what sets the margin, the margin must be designed for the worst path, which throws away the selectivity gained on the best. A six-beam system whose paths differ by 10 dB is three beams plus three witnesses.
* Gas nucleus density varies by tissue and can fall below the coincidence requirement. The floor is $2.4\times10^{5}\ \mathrm{mL^{-1}}$ for contiguous 50 $\mu$m kill spheres. Blood and liver sit above it; brain white matter and cartilage plausibly sit below it, in which case the device produces no lesion at all rather than a selective one. The nucleus count of the target tissue is a hard prerequisite and is not measurable non-invasively at present.
* A 30% variation in threshold collapses the geometry. By the $R_0^{-1}$ law, 30% radius spread gives 30% threshold spread, $w = 660\text{ kPa}$. At the optimal margin $m = 0.75$ this gives $p_{fire,off} = 1/(1+e^{2.5}) = 0.076$ and $\mathcal{S} = 0.024$. The collapse is not gradual: selectivity is exponential in $mP_{th}/w$, so the transition from useful to useless spans about a factor of 2 in $w$. There is no graceful degradation mode.
* Thermal confound in the overlap. Intensity scales as $N^2 = 36$, so the overlap heats 36x faster than any single path. At 0.223 s of total dwell the overlap reaches 28.8 K while off target reaches 0.8 K. The 36:1 thermal ratio is the same order as the claimed mechanical selectivity, so a thermal lesion and a cavitation lesion are not distinguishable by size alone in the overlap. The discriminator is the presence of broadband emission during the pulse, which must be recorded on every shot.
* Bubble cloud shielding. Once the first nuclei fire, the cloud scatters and absorbs, and the pressure behind it drops. This self-limits the dose, which is helpful thermally and harmful geometrically: the lesion grows from the proximal face of the target outward, so its final shape is a cone truncated by shielding, not the intended sphere. The 2 mm sphere is an idealisation and the experiment measures a diameter, which will be the shielded diameter.
* Energy accounting. The 4.19 mm$^3$ lesion with 4190 collapse events at roughly $10^{-6}$ J of acoustic work per collapse needs 4.2 mJ of cavitation work. The delivered acoustic energy at 130 W/cm$^2$ over a 0.5 cm$^2$ beam cross-section and 0.223 s is 14.5 J per beam, so 87 J total for 4.2 mJ of useful work: an efficiency of $5\times10^{-5}$. The device is an inefficient way to deliver 4 mJ, which is acceptable because the alternative is a scalpel, and is unacceptable if the energy must be delivered through skin that cannot take 87 J.

## 10. Experiment

* Phantom: 10% w/v polyacrylamide gel, 120 mm cube, degassed under vacuum then re-equilibrated with air to a measured nucleus density of $10^{6}\ \mathrm{mL^{-1}}$ (counted by acoustic nucleation from a calibrated 1 MHz single-beam sweep before the main run), acoustic properties $\rho = 1050\ \mathrm{kg/m^3}$, $c = 1520\ \mathrm{m/s}$, $\alpha_a = 0.5\ \mathrm{dB/cm}$ at 1 MHz, $20\ ^\circ\mathrm{C}$.
* Sources: six 1.0 MHz, 25 mm element, F/1.1 focused transducers (spherical, 60 mm focal length), on a 120 mm radius frame at 60 degree polar spacing, all driven from one clock with $< 5$ ns relative jitter, individual amplitude and phase trimmable to 1% and 2 degrees.
* Field calibration: a 0.2 mm PVDF needle hydrophone scanned on a 0.1 mm grid through the focus for each beam individually and for all six together; the six-beam focus must measure $12.0 \pm 0.5\text{ MPa}$ before any phantom is exposed.
* Passive cavitation detection: a 5 MHz focused transducer at 90 degrees, 20 MHz sampling, broadband RMS integrated over 2 to 10 MHz, noise floor established over 200 blank shots.
* Dose: 2000 pulses of 20 $\mu$s at 1 Hz, 2000 s total, per condition.
* Conditions, in this order, on fresh phantoms: (a) each single beam at 2.0 MPa, six separate runs; (b) all six at 2.0 MPa; (c) all six at 2.0 MPa but with one beam delayed by 500 ns (loss of coherence control, expected to fail); (d) all six at 0.55 MPa (the optimal-margin point, expected to succeed with lower selectivity); (e) a single beam at 12.0 MPa (the single-focus control, expected to lesion everything in its path).
* Lesion sizing: 1 mm slicing with 2,3,5-triphenyltetrazolium chloride staining, optical planimetry, plus optical transmittance at 600 nm through the intact gel.
* High-speed imaging: 1 Mfps framing camera on the focal plane for the first 200 $\mu$s of the six-beam case, to confirm that cavitation initiates within one pulse and not after 100 pulses.
* Null result (defined before the run): any condition (a) run showing broadband emission above 10x the noise floor, or any measurable lesion; or condition (b) producing a lesion outside the range 1.6 to 2.4 mm.
* What this cannot distinguish: a threshold step from a rate process with a very steep pressure exponent. Both produce "no lesion at 2.0 MPa, lesion at 12.0 MPa". The discriminator is the pulse-count dependence: a step fires on pulse 1, a rate process fires after a Poisson-distributed latency. The 1 Mfps imaging and the per-pulse cavitation detector separate them, and that separation is the primary scientific output.

## 11. Expected observations

* Success branch: conditions (a) show zero broadband emission and zero lesion across all six single beams (this is the strong branch and the one that would justify the design). Condition (b) shows emission onset within $3 \pm 2$ pulses and a lesion of $2.0 \pm 0.3\text{ mm}$ that stops growing after $40 \pm 25$ pulses as the cloud shields. Condition (c) shows no lesion, confirming that coherence and not merely co-location is required. Condition (e) shows a 12 MPa single beam ablating a 2 mm wide, 40 to 60 mm long track, which is the off-target disaster the coincidence scheme is meant to prevent.
* Failure branch: any condition (a) run fires. Given the 27% off-target fire probability computed at $w = 200\text{ kPa}$, this is the more likely outcome, and it does not mean the apparatus is broken. It means the threshold step at 1 MHz in a 1% gas-loaded gel is 200 kPa wide and the pinned geometry has no selectivity. The follow-up is the $w$-measurement itself: a pressure sweep in 0.1 MPa steps on single beams, 50 shots each, to extract $p_{fire}(p)$ and hence $w$ directly.
* Middle branch: single beams are clean (so $w < 100\text{ kPa}$) but the lesion is 4 to 6 mm. This says the step is sharp but the overlap dose is 5.45x threshold, so the lesion is set by the beam profile, not by the coincidence. The fix is the optimal margin ($m = 0.75$, 3.3 MPa at the focus) and the lesion should drop to 2 mm.

## 12. Magnitudes

* Drive frequency: 1.0 MHz; period 1.0 $\mu$s; rarefaction half-cycle 500 ns.
* Single-beam peak negative pressure: 2.0 MPa (130 W/cm$^2$).
* Tissue cavitation threshold at 1 MHz: 2.2 MPa.
* Beam margin below threshold: 9.1% (0.2 MPa).
* Coherent six-beam focus pressure: 12.0 MPa, 5.45x threshold, 4680 W/cm$^2$.
* Incoherent six-beam alternative: 4.9 MPa (below threshold, so coherence is required).
* Implied nucleus radius from the 2.2 MPa threshold: 25 nm; Rayleigh collapse time 0.49 ns.
* Nucleus density: $10^{6}$ per mL; mean spacing 100 $\mu$m; kill radius 50 $\mu$m.
* Nuclei in the 4.19 mm$^3$ target: 4190, against 4190 kill spheres required.
* Lesion: 2 mm diameter, 4.19 mm$^3$; target-to-off-target volume ratio 540:1.
* Off-target volume per treatment: 2262 mm$^3$ across six beam cylinders.
* Thermal rise: 0.8 K per beam per 223 ms of accumulated dwell; 28.8 K for the six-beam overlap at the same dwell; $2.6\times10^{-3}$ K per 20 $\mu$s pulse in the overlap.
* Attenuation at 12 cm, 1 MHz: 6.0 dB one way, amplitude factor 0.50.
* Focal gain and face pressure: 51x and 78 kPa for a 110 mm aperture at F/1.1.
* Volume selectivity: $6.9\times10^{-3}$ at $w = 200$ kPa; $10^{4}$ requires $w \le 13$ kPa and nucleus monodispersity of 0.6%.
* Cavitation work needed: 4.2 mJ against 87 J delivered, efficiency $5\times10^{-5}$.

## 13. Applications

* Nearest-term: ex vivo tissue ablation in a calibrated phantom and in excised liver, where the nucleus density and the threshold step can both be measured directly. This is the only regime in which the design's claims are currently checkable.
* Nearest-term: an instrument for measuring the cavitation threshold step width of any medium, which is a metrology product independent of the ablation claim. A six-beam coincidence head with a pressure sweep reports $w$ in about 200 shots.
* Long-horizon: limb-sparing ablation of soft-tissue sarcoma and of uterine fibroids from an external frame, where a 220 mm coupling surface is available and 12 cm depth is typical.
* Long-horizon: intraoperative margin ablation after resection, where the target is a 2 mm shell on a cut surface and the depth requirement collapses to a few centimetres, which removes the aperture problem entirely.
* Long-horizon: non-invasive ablation through a naturally gas-rich medium (lung, bowel) where the nucleus density is far above the $2.4\times10^{5}\ \mathrm{mL^{-1}}$ floor, making the coincidence requirement easy and the targeting the only open problem.

## 14. Unresolved questions

* What is the width of the cavitation threshold step at 1 MHz in vascularised soft tissue, in kPa, and how does it depend on the nucleus population's radius distribution? This single number decides whether the vector is a device or a curiosity.
* Can gas nuclei be introduced or stabilised locally to narrow the radius distribution to the required 0.6%, for example by infusing a monodisperse microbubble suspension, and does that make the selectivity a property of the injected agent rather than of the tissue?
* How much does the bubble cloud shield, in dB, and is the resulting lesion shape stable enough to plan a dose without imaging?
* Is the 50 $\mu$m kill radius per collapse correct in perfused tissue, where flow removes cavitation nuclei and carries away debris, or is it 10 $\mu$m, which would raise the required nucleus density by 125x?

## 15. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 4 | 5 | 4 | 5 | 4 | 5 |

Total: 27/30.
Confidence: 58%, basis: superposition, the Blake inversion to a 25 nm nucleus, the intensity and thermal scaling, and the selectivity algebra are all exact and reproduce the pinned numbers, but the selectivity is exponential in an unmeasured step width, and at the plausible 200 kPa width the pinned geometry delivers $7\times10^{-3}$ rather than $10^{4}$.

## 16. Status

Live. The arithmetic is not in question; the threshold step width is, and the falsification experiment in section 3 is a direct measurement of it rather than a confirmation of the mechanism. Two pinned numbers do not survive their own derivation: the $10^{4}$ volume selectivity needs a 13 kPa threshold uniformity that living tissue does not have, and the 9.1% beam margin is far below the 75% margin the geometry can afford. The corrected design point is $N = 7$, 0.65 MPa per beam, $w \le 100$ kPa, and it is a different machine.
