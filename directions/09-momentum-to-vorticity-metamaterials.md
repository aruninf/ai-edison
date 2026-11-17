# Research Vector 09: Momentum-to-Vorticity Metamaterials

## Objective
Engineer monolithic acoustic metamaterials with broken spatial-inversion symmetry and chiral phononic bandgaps that geometrically refract incoming linear impact momentum into closed-loop internal rotational acoustic vorticity, preventing shockwave transmission, back-translation, or structural collapse without plastic sacrificial deformation.

---

## 1. Physical Principles and Governing Laws

Traditional armor, crumple zones, and seismic dampers rely on dissipative plastic work:
$$\Delta E_{plastic} = \int \boldsymbol{\sigma} : d\boldsymbol{\epsilon}_{plastic}$$
This mechanism permanently destroys the material and transfers residual momentum to the underlying structure.

Vector 09 eliminates sacrificial destruction by redirecting translational momentum into localized topological acoustic vortices:

```text
[External Linear Kinetic Shockwave: p_linear = m * v_0]
                           |
                           v
[Chiral Phononic Interface with Broken Inversion Symmetry]
                           |
                           v
[Wavevector Refraction into Evanescent Micro-Vorticity Modes]
                           |
                           v
[Trapped Acoustic Angular Momentum: L_local = r x p_wave]
                           |
                           v
[Low-Grade Uniform Thermal Dissipation via Phonon-Phonon Scattering]
```

### A. Non-Reciprocal Chiral Constitutive Relations
In a chiral micropolar (Cosserat) elastic continuum, translational displacement $\mathbf{u}$ is coupled directly to local micro-rotation $\boldsymbol{\phi}$:
$$\boldsymbol{\sigma} = \mathbf{C} : \boldsymbol{\epsilon} + \mathbf{B} : \boldsymbol{\kappa}$$
$$\mathbf{m} = \mathbf{B}^T : \boldsymbol{\epsilon} + \mathbf{D} : \boldsymbol{\kappa}$$

Where:
* $\boldsymbol{\sigma}$ is the standard stress tensor (non-symmetric).
* $\mathbf{m}$ is the couple-stress tensor.
* $\boldsymbol{\kappa} = \nabla \boldsymbol{\phi}$ is the curvature-twist tensor.
* $\mathbf{B}$ is the chiral coupling tensor describing translation-rotation interconversion.

### B. Topological Vortex Trapping (Acoustic Angular Momentum)
When an impinging linear acoustic wave with wavevector $\mathbf{k} = (k_x, 0, 0)$ strikes the chiral boundary, the non-zero cross-coupling components $B_{ijk}$ force the group velocity $\mathbf{v}_g = \nabla_\mathbf{k} \omega$ into a closed spiral trajectory:
$$\frac{d\mathbf{r}}{dt} = \mathbf{v}_g(\mathbf{k}) = \boldsymbol{\Omega} \times \mathbf{r} - \gamma \mathbf{r}$$

The linear momentum $\mathbf{p} = \hbar \mathbf{k}$ is continuously exchanged with local angular momentum:
$$\frac{d\mathbf{L}}{dt} = \mathbf{r} \times \mathbf{F}_{linear} \to \text{rotational standing modes}$$

The wave is trapped in sub-millimeter unit cells, spinning at ultrasonic frequencies until natural phonon-phonon scattering thermalizes the energy uniformly without structural displacement.

---

## 2. Unprecedented Characteristics

1. **Non-Sacrificial Armor:** An impact barrier that absorbs repeated high-velocity ballistic or shock impacts without cracking, shattering, or flexing backward.
2. **True Inertial Decoupling:** Structures protected by this metamaterial experience near-zero base shear during seismic ground motion, as horizontal ground displacements are converted into internal microscopic rotations.

---

## 3. High-Priority Research Hypotheses

1. **Topological Chiral Honeycomb Shock Absorber:** 3D multi-material lattice demonstrating greater than 90% suppression of transmitted linear momentum under high-g projectile impact.
2. **Sub-Wavelength Seismic Vortex Foundation:** Metamaterial civil engineering foundation blocks that trap low-frequency (0.5 - 10 Hz) earthquake S-waves and Rayleigh waves into localized rotational modes.
