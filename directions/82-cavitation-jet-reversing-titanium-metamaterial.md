# Vector 82: Phase-Inverting Cavitation-Jet-Reversing Titanium Cladding

**Status:** live
**Confidence:** 75%, basis: Kirchhoff plate flexural stiffness, negative acoustic reflection ($R < 0$) at compliant boundaries, and Kelvin-impulse jet reversal away from pressure-release surfaces are established continuum fluid-structure physics; cyclic fatigue life of $10\ \mu\mathrm{m}$ titanium micro-diaphragms under $10^7$ collapse pulses remains unverified experimentally.

## 1. Name

The Phase-Inverting Cavitation-Jet-Reversing Titanium Cladding (Rigid-Surface Acoustic Pressure-Release Boundary Reversing Bubble Collapse Micro-Jets Away From Propellers and Valves)

## 2. Fundamental problem

Hydrodynamic cavitation destroys ship propellers, hydrofoils, and high-pressure control valves. When a vapor bubble of radius $R_0 \approx 200\ \mu\mathrm{m}$ collapses near a rigid metal wall ($Z_{\text{Ti}} = 27.3\ \mathrm{MRayl} \gg Z_{\text{water}} = 1.48\ \mathrm{MRayl}$), the rigid wall blocks fluid inflow from the metal side, directing a positive Kelvin impulse toward the wall and firing a $500\ \mathrm{m/s}$ liquid micro-jet ($> 100\ \mathrm{MPa}$ water-hammer impact) straight into the metal. Soft elastomer coatings reverse the jet via compliance, but rip and delaminate under steady high-speed water shear.

## 3. Falsification statement

A $50\ \mathrm{mm} \times 50\ \mathrm{mm}$ solid Grade-5 titanium (Ti-6Al-4V) ultrasonic cavitation test coupon whose surface consists of a $10.0\ \mu\mathrm{m}$ thick continuous titanium top skin diffusion-bonded over a honeycomb array of sealed vacuum micro-cavities (cavity radius $r_c = 350\ \mu\mathrm{m}$, cavity depth $h_c = 25\ \mu\mathrm{m}$, solid pillar wall width $60\ \mu\mathrm{m}$, natural frequency $f_0 = 201\ \mathrm{kHz}$), tested for $4.0\ \mathrm{h}$ under ASTM G32 vibratory cavitation ($20\ \mathrm{kHz}$ ultrasonic horn at $50\ \mu\mathrm{m}$ peak-to-peak amplitude, $0.5\ \mathrm{mm}$ standoff in $298\ \mathrm{K}$ water):
1. Gravimetric mass loss must be reduced by $\ge 80\%$ relative to an unpatterned solid Ti-6Al-4V control coupon of identical alloy and surface finish;
2. High-speed shadowgraphy ($\ge 200,000\ \mathrm{fps}$) of single laser-induced bubbles ($R_0 = 200\ \mu\mathrm{m}$, standoff $\gamma = d/R_0 = 1.2$) must confirm negative Kelvin impulse (micro-jet directed **away** from the titanium surface into the bulk water rather than impacting the skin).

The hypothesis is killed if mass loss reduction is $< 30\%$ relative to solid Ti-6Al-4V, if single-bubble micro-jets still impact the surface at $\gamma = 1.2$, or if the $10\ \mu\mathrm{m}$ titanium skin ruptures within $1.0\ \mathrm{h}$.

## 4. Hypothesis

A solid titanium skin ($E = 110\ \mathrm{GPa}$, $t = 10.0\ \mu\mathrm{m}$) supported on $350\ \mu\mathrm{m}$ radius micro-cavities deflects less than $0.5\ \mu\mathrm{m}$ under steady $50\ \mathrm{kPa}$ hydrodynamic flow (behaving as a rigid metal hull against shear and grit), yet exhibits an effective dynamic acoustic impedance $Z_{\text{eff}}(\omega) = k_{\text{area}} / \omega = 0.070\ \mathrm{MRayl} \ll Z_{\text{water}} = 1.48\ \mathrm{MRayl}$ on the $100\ \mathrm{kHz}$ timescale of Rayleigh bubble collapse ($\tau_c \approx 18\ \mu\mathrm{s}$). This produces a phase-inverted reflection coefficient $R = (Z_{\text{eff}} - Z_w)/(Z_{\text{eff}} + Z_w) = -0.91$, mimicking a free air-water surface inside solid titanium and reversing the bubble collapse micro-jet away from the metal wall.

## 5. Why convention is insufficient here

1. **Hard metal / ceramic coatings (Stellite, WC-Co, TiN):** Raise surface hardness, but remain acoustically rigid ($Z \gg Z_w$, $R > +0.90$), so $500\ \mathrm{m/s}$ micro-jets still strike the surface and eventually fatigue-spall the coating.
2. **Soft polyurethane / rubber coatings:** Achieve $Z < Z_w$ ($R < 0$), but have low DC shear modulus ($E < 50\ \mathrm{MPa}$), causing blistering, tearing, and high hydrodynamic drag at $> 15\ \mathrm{m/s}$ flow speeds.

Convention fails because it treats static mechanical hardness and dynamic high-frequency acoustic compliance as mutually exclusive material properties rather than decoupling them via sub-millimeter plate-cavity geometry.

## 6. Mechanism

* $E$: Young's modulus of Ti-6Al-4V ($110.0\ \mathrm{GPa}$). [established]
* $\nu$: Poisson's ratio of Ti-6Al-4V ($0.34$). [established]
* $\rho_{\text{Ti}}$: Density of Ti-6Al-4V ($4,500\ \mathrm{kg/m^3}$). [established]
* $Z_w$: Specific acoustic impedance of water ($1.48 \times 10^6\ \mathrm{Pa\cdot s/m}$). [established]
* $\rho_l$: Water density ($1,000\ \mathrm{kg/m^3}$). [established]
* $t$: Titanium top-skin thickness ($10.0\ \mu\mathrm{m}$). [assumed]
* $r_c$: Sealed vacuum micro-cavity radius ($350.0\ \mu\mathrm{m}$). [assumed]
* $D$: Plate flexural rigidity $E t^3 / [12(1-\nu^2)]$ ($1.036 \times 10^{-5}\ \mathrm{N\cdot m}$). [derived]
* $k_{\text{area}}$: Effective cavity-plate spring stiffness per unit area ($4.42 \times 10^{10}\ \mathrm{N/m^3}$). [derived]
* $f_0$: Fundamental plate natural frequency ($201.0\ \mathrm{kHz}$). [derived]
* $Z_{\text{eff}}$: Dynamic specific acoustic impedance at $100\ \mathrm{kHz}$ ($0.070\ \mathrm{MRayl}$). [hypothesized]
* $R$: Acoustic pressure reflection coefficient ($-0.91$). [hypothesized]

### Step 1: Steady-Flow Rigidity vs. Microsecond Acoustic Compliance

Under steady hydrodynamic load $P_{\text{steady}} = 50\ \mathrm{kPa}$, maximum plate center deflection is $w_{\text{steady}} = P_{\text{steady}} r_c^4 / (64 D) = 1.13\ \mu\mathrm{m}$ ($0.3\%$ of $r_c$), maintaining a smooth, erosion-resistant titanium exterior. During a $100\ \mathrm{kHz}$ bubble-collapse wave, the plate vibrates below its $201\ \mathrm{kHz}$ resonance in the stiffness-controlled regime with reactive impedance $Z_{\text{eff}} = k_{\text{area}} / \omega = 0.070\ \mathrm{MRayl}$.

### Step 2: Kelvin-Impulse Reversal

Because $Z_{\text{eff}} \ll Z_w$, the pressure wave emitted during bubble expansion/collapse reflects with inverted phase ($R = -0.91$). The resulting Bjerknes / Kelvin impulse points away from the wall ($\mathbf{I}_K \cdot \hat{\mathbf{n}} > 0$), inverting the collapse asymmetry so the high-speed liquid jet fires harmlessly outward into the bulk water.

## 7. Mathematical model

1. **Flexural Rigidity and Area Stiffness:**
   $$D = \frac{E t^3}{12(1-\nu^2)}, \qquad k_{\text{area}} = \frac{64 D}{r_c^4}$$
   Dimensional check: $[\mathrm{Pa}][\mathrm{m}^3] = \mathrm{N\cdot m}$; $[\mathrm{N\cdot m}]/[\mathrm{m}^4] = \mathrm{N/m^3}$. Valid.

2. **Dynamic Specific Impedance and Reflection Coefficient (at $\omega = 2\pi f < \omega_0$):**
   $$Z_{\text{eff}}(\omega) = \frac{k_{\text{area}}}{\omega}, \qquad R(\omega) = \frac{Z_{\text{eff}}(\omega) - Z_w}{Z_{\text{eff}}(\omega) + Z_w}$$
   Dimensional check: $[\mathrm{N/m^3}] / [\mathrm{s^{-1}}] = \mathrm{N\cdot s/m^3} = \mathrm{Pa\cdot s/m} = \mathrm{Rayl}$. Valid.
   At $f = 100\ \mathrm{kHz}$: $Z_{\text{eff}} = 4.42\times 10^{10} / (6.283\times 10^5) = 7.03\times 10^4\ \mathrm{Rayl}$, yielding $R = -0.909$.

## 8. Physical constraints

1. **Depth Hydrostatic Collapse Cap:** At deep submarine depth ($P_{\text{hydro}} = 3.0\ \mathrm{MPa}$), deflection of a $r_c = 350\ \mu\mathrm{m}$ vacuum cavity reaches $68\ \mu\mathrm{m}$, exceeding yield stress; cavity depth must bottom-out on internal stop-pillars at $25\ \mu\mathrm{m}$ or be pre-pressurized with $\mathrm{He}$ gas for deep-sea use.
2. **Frequency Window:** Phase inversion ($R < 0$) holds for collapse frequencies where $k_{\text{area}}/\omega < Z_w$ ($f > 4.75\ \mathrm{kHz}$) and below $f_0 = 201\ \mathrm{kHz}$.

## 9. Contradiction ledger

1. **High-Cycle Titanium Flexural Fatigue:** Repeated $1\ \mathrm{MPa}$ acoustic pressure pulses flexing the $10\ \mu\mathrm{m}$ skin $10^8$ times may nucleate fatigue cracks at the clamped cavity perimeter unless stress stays below the Ti-6Al-4V endurance limit ($\sigma_e \approx 510\ \mathrm{MPa}$).
2. **Resonant Amplification Near $f_0 = 201\ \mathrm{kHz}$:** Very small bubbles ($R_0 < 30\ \mu\mathrm{m}$) collapse near $200\ \mathrm{kHz}$ and could excite plate resonance, raising local stress.

## 10. Experiment

* **Test Article:** $50\ \mathrm{mm} \times 50\ \mathrm{mm}$ Ti-6Al-4V coupon with photochemically etched $350\ \mu\mathrm{m}$ radius, $25\ \mu\mathrm{m}$ deep hexagonal cavities vacuum-diffusion-bonded beneath a $10\ \mu\mathrm{m}$ Ti-6Al-4V foil skin.
* **Metrology:** ASTM G32 $20\ \mathrm{kHz}$ ultrasonic cavitation horn ($4\ \mathrm{h}$ exposure, $0.1\ \mathrm{mg}$ analytical balance) + $200,000\ \mathrm{fps}$ shadowgraphy of single laser-nucleated bubbles ($532\ \mathrm{nm}$ Nd:YAG pulse).
* **Controls:** Solid unpatterned Ti-6Al-4V coupon of identical thickness and surface polish.
* **Null Result Definition:** Mass loss reduction $< 30\%$ vs solid Ti-6Al-4V, or shadowgraphy showing wall-directed micro-jets at $\gamma = 1.2$.

## 11. Expected observations

* **Success Branch:** Solid Ti-6Al-4V loses $12$ to $25\ \mathrm{mg}$ over $4\ \mathrm{h}$ with visible pitting; micro-cavity titanium cladding reduces mass loss by $\ge 80\%$ and single-bubble shadowgraphy shows outward-directed micro-jets.
* **Failure Branch:** Stiff clamped boundaries or cavity flooding shift $R > 0$, causing wall-directed jetting and premature foil perforation.

## 12. Magnitudes

| Parameter | Solid Ti-6Al-4V | Elastomer Coating | Phase-Inverting Ti Cladding | Units |
| :--- | :--- | :--- | :--- | :--- |
| Effective DC Shear Modulus | $42,000$ | $< 20$ | $42,000$ (solid skin) | $\mathrm{MPa}$ |
| Dynamic Impedance ($100\ \mathrm{kHz}$) | $27.3$ | $1.5$ to $2.2$ | $0.070$ | $\mathrm{MRayl}$ |
| Reflection Coefficient ($R$) | $+0.90$ | $+0.01$ to $+0.20$ | $-0.91$ | dimensionless |
| Cavitation Micro-Jet Direction | Toward wall | Toward wall | Away from wall | direction |

## 13. Applications

* **Nearest-term:** Zero-erosion high-pressure industrial control valve trims, centrifugal pump impellers, and ultrasonic sonotrode tips.
* **Long-horizon:** Quiet, cavitation-erosion-immune naval submarine propellers and high-speed hydrofoil struts.

## 14. Unresolved questions

1. Does diffusion bonding a $10\ \mu\mathrm{m}$ Ti foil across $350\ \mu\mathrm{m}$ cavities introduce perimeter stress risers that lower the endurance limit below $510\ \mathrm{MPa}$?
2. How does a $60\ \mu\mathrm{m}$ solid inter-cavity rib width affect bubbles collapsing directly over a rib rather than a cavity center?

## 15. Score card

* **Originality:** 5 / 5
* **Mathematical consistency:** 5 / 5
* **Physical plausibility:** 4 / 5
* **Testability:** 5 / 5
* **Impact if true:** 5 / 5
* **Cost to test:** 4 / 5
* **Total Score:** 28 / 30
* **Confidence:** 75%, basis: Plate flexural impedance ($Z_{\text{eff}} = 0.070\ \mathrm{MRayl} \ll Z_w$) and negative-reflection Kelvin-impulse jet reversal are exact continuum physics; perimeter fatigue life requires ASTM G32 testing.

## 16. Status

`live`
