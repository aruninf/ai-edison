# Research Vector 13: Mechanochemical Self-Squeezing Vapor Engines

## Objective
Design monolithic, bistable auxetic metamaterials that extract liquid drinking water continuously from low-humidity ambient air ($\text{RH} \ge 20\%$) using swelling-induced mechanical snap-through and steric contact-angle inversion, expelling liquid water without photothermal heating, compressors, or electrical power supplies.

---

## 1. Physical Principles and Governing Laws

Traditional atmospheric water harvesting relies on either refrigeration cooling (condensation below dew point) or photothermal desiccant baking (heating metal-organic frameworks or silica gels to $70\text{ to }90^\circ\text{C}$ to vaporize water out).

Vector 13 replaces thermal desorption with isothermal mechanical snap-squeezing:

```text
[Ambient Air: RH = 20 - 50%]
               |
               v (Spontaneous Capillary Adsorption)
[Hydrophilic Nanopores (r_p ~ 2 nm): Delta G_ads < 0]
               |
               v (Swelling Osmotic Pressure: P_swell > 15 MPa)
[Elastic Strain Energy Accumulation in Bistable Ribs]
               |
               v (Critical Strain: Euler Snap-Through)
[Abrupt Pore Volume Collapse (75% volume reduction)]
               |
               v (Steric Reorientation of Surface Ligands)
[Contact-Angle Inversion: Hydrophilic (theta < 20 deg) -> Hydrophobic (theta > 120 deg)]
               |
               v (Zero Liquid Affinity)
[Bulk Liquid Water Expulsion through One-Way Micro-Drain]
               |
               v (Tension Released)
[Spontaneous Elastic Recovery -> Open Ground State]
```

### A. Adsorption Swelling Pressure Formulation
The chemical potential difference driving capillary condensation into hydrophilic nanopores is:
$$\Delta \mu = \frac{R T}{V_m} \ln(\text{RH})$$

The corresponding volumetric osmotic swelling pressure exerted against the pore elastic boundary is governed by the Flory-Rehner / Kelvin relation:
$$\Pi_{swell} = -\frac{R T}{V_m} \left[ \ln(1 - \phi_p) + \phi_p + \chi \phi_p^2 \right] - \frac{R T \rho_0}{M_c} \phi_p^{1/3} \approx 15\text{ to }30\text{ MPa}$$

### B. Mechanochemical Contact-Angle Inversion
In the relaxed state, grafted zwitterionic/silane chains expose hydrophilic head groups ($\theta < 20^\circ$). Under high shear strain during structural snap-through ($\gamma_{shear} > 0.40$), steric hindrance forces ligand reorientation, burying hydrophilic moieties and exposing hydrophobic fluorocarbon or alkyl tails ($\theta > 120^\circ$).

With the pore volume collapsed and the walls rendered hydrophobic, the capillary Laplace pressure reverses sign:
$$\Delta P = \frac{2 \gamma \cos\theta}{r_p} \implies \text{Positive expulsion pressure pushing water out}$$

---

## 2. Unprecedented Characteristics

1. **24/7 Day-and-Night Operation:** Operates in complete darkness, indoors, or underground without sunlight or heat sources.
2. **Zero Parasitic Energy:** Driven exclusively by the chemical potential of unsaturated ambient water vapor.

---

## 3. High-Priority Research Hypotheses

1. **EXP-20261117-004: Monolithic Bistable Auxetic Water Generator (BAWG):**
   A micro-patterned elastomeric lattice producing continuous liquid water output ($\ge 1.0\,\text{L/m}^2/\text{day}$) under ambient conditions ($35\%\text{ RH}$, $295\text{ K}$) with zero electrical or thermal energy input.
