# Research Vector 12: Static Mechanical Diodes (Non-Betti Topological Force Rectifiers)

## Objective
Design monolithic solid-state metamaterials that break the 150-year-old Maxwell-Betti reciprocity theorem in static mechanics, enabling unidirectional static force transmission ($F_{A \to B} > 0$ with rigid structural coupling, while $F_{B \to A} \approx 0$ with reaction forces diverted into closed-loop internal toroidal hoop tension), without moving linkages, ratchets, clutches, external power, or sensors.

---

## 1. Physical Principles and Governing Laws

In classical linear elasticity, the Maxwell-Betti reciprocal work theorem (1872) establishes that for any elastic body subjected to two distinct load systems:
$$\int_{\partial V} \mathbf{t}^{(1)} \cdot \mathbf{u}^{(2)} dA = \int_{\partial V} \mathbf{t}^{(2)} \cdot \mathbf{u}^{(1)} dA$$

This theorem enforces reciprocal force transmission: pushing Point A causes a reaction at Point B identical to pushing Point B causing a reaction at Point A.

Vector 12 breaks this symmetry by designing non-linear, pre-stressed chiral micropolar continua where the tangent elastic stiffness tensor is non-symmetric:
$$C_{ijkl}^{tangent} \ne C_{klij}^{tangent}$$

```text
[FORWARD LOADING: Port A to Port B]
Port A Axial Load -> Axial Micro-Strut Compression -> Rigid Load Transmission -> Port B (T_fwd ~ 1.0)

[BACKWARD LOADING: Port B to Port A]
Port B Reaction -> Chiral Nodal Asymmetry -> Bifurcation into Toroidal Hoop Ring -> Zero Axial Force at Port A (T_bwd ~ 0.0)
```

### A. Chiral Micropolar Constitutive Law with Pre-Stress
In a micropolar continuum with internal rotational degrees of freedom $\boldsymbol{\phi}$ and pre-stress $\boldsymbol{\sigma}_0$:
$$\boldsymbol{\sigma} = \mathbf{C} : \boldsymbol{\epsilon} + \mathbf{B} : (\nabla \boldsymbol{\phi}) + \boldsymbol{\sigma}_0$$
$$\mathbf{m} = \mathbf{B}^T : \boldsymbol{\epsilon} + \mathbf{D} : (\nabla \boldsymbol{\phi})$$

Where:
* $\mathbf{B}$ is the chiral cross-coupling tensor breaking spatial-inversion symmetry ($B_{ijk} \ne 0$).
* When an axial load is applied at Port A, the pre-stress state locks the micro-rotation ($\boldsymbol{\phi} \to 0$), producing maximum effective axial Young's modulus $E_{eff}^{fwd} \approx E_0$.
* When an opposing load is applied at Port B, the chiral coupling tensor induces spontaneous non-linear nodal rotation, triggering an asymmetric snap-buckling bifurcation into an orthogonal hoop ring.

### B. Internal Self-Equilibrating Hoop Tension
The backward reaction force $F_{bwd}$ does not propagate axially to Port A. Instead, it is converted into internal circumferential hoop stress $\sigma_\theta$ within the closed toroidal geometry of each unit cell:
$$\oint_{unit\_cell} \sigma_\theta r d\theta = F_{bwd}$$

Because the hoop stress equilibrates entirely within the closed boundary of the unit cell, the net axial reaction force transmitted across the terminal boundary to Port A vanishes:
$$\lim_{N \to \infty} \frac{F_A(F_B)}{F_B} \to 0$$

### C. The Mechanical Diode Rectification Ratio
The performance of a static mechanical diode is defined by the rectification ratio $\mathcal{R}$:
$$\mathcal{R} = \frac{T_{fwd}}{T_{bwd}} = \frac{F_B / F_A \big|_{forward}}{F_A / F_B \big|_{backward}}$$

For an ideal mechanical diode, $T_{fwd} \to 1.0$, $T_{bwd} \to 0.0$, yielding $\mathcal{R} \to \infty$.

---

## 2. Unprecedented Applications

1. **Zero-Reaction Armor and Blast Shields:** An impact barrier that provides total rigid resistance against frontal loads, but diverts 99% of kinetic impact shock into internal hoop stress, protecting the underlying vehicle or human body from transmitted momentum.
2. **One-Way Penetration Tools and Surgery:** Needles, trocars, and micro-actuators that push forward with high rigidity, but cannot be pushed backward by tissue pressure or patient reflex.
3. **Seismic Isolation Foundations:** Structural columns that support millions of kilograms of vertical gravity load with complete stiffness, but block horizontal earthquake shear waves from propagating into the building superstructure.

---

## 3. High-Priority Research Hypotheses

1. **EXP-20261117-003: Monolithic Chiral-Cosserat Static Mechanical Diode:**
   A 3D-printable titanium or polymer lattice demonstrating rectification ratio $\mathcal{R} \ge 100$ under quasi-static mechanical loading.
