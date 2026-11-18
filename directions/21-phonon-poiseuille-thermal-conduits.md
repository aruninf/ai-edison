# Vector 21: Phonon-Poiseuille Thermal Conduits

**Status:** wounded (operating window 50–150 K only)
**Confidence:** 65%, basis: Guyer–Krumhansl hydrodynamic phonon transport is established in graphite; the width-dependence signature has not been measured as a device spec.

## 1. Falsification statement

In suspended graphite ribbons at 60–120 K, measure in-plane $\kappa$ versus ribbon width $L$. The hypothesis dies if $\kappa(L)$ rises monotonically with log–log slope $1.0 \pm 0.2$, or if the Knudsen-minimum dip at $L \approx \lambda_N$ is shallower than 10% of the Matthiessen prediction.

## 2. Fundamental problem

Moving heat through a solid without a working fluid, with less material than Fourier conduction allows.

## 3. Mechanism

Below ~150 K in graphite, momentum-conserving normal (N) phonon scattering dominates momentum-destroying Umklapp and defect scattering. In a ribbon of width $\lambda_N \ll L < \lambda_U$, phonon momentum relaxes only at the walls, so the phonon gas develops a viscous parabolic drift with slip. Wall loss rates as $1/L^2$, not $1/L$, and apparent conductivity runs above the Matthiessen value.

## 4. Mathematical model

Matthiessen (what a Fourier + diffuse-boundary solver predicts):

$$1/\Lambda = 1/\lambda_N + 1/L + 1/\lambda_U \;\Rightarrow\; \kappa_M = \tfrac{1}{3}Cv\Lambda$$

Hydrodynamic (Poiseuille, clip at Umklapp):

$$\Lambda_P = \min\left(L^2/\lambda_N,\ \lambda_U\right) \;\Rightarrow\; \kappa_P = \tfrac{1}{3}Cv\Lambda_P$$

Dimensions: $[L^2/L] = \mathrm{m}$; $\kappa$ in $\mathrm{W\,m^{-1}K^{-1}}$. Checked.

## 5. Magnitudes at 100 K

$C \approx 4\times10^5\ \mathrm{J\,m^{-3}K^{-1}}$, $v \approx 1.5\times10^4\ \mathrm{m\,s^{-1}}$ [UNVERIFIED, Debye estimate] $\Rightarrow \tfrac{1}{3}Cv = 2\times10^9\ \mathrm{W\,m^{-2}K^{-1}}$ per metre of mean free path.

$\lambda_N \approx 0.7\ \mu m$, $\lambda_U \approx 2\ \mu m$ [UNVERIFIED, scaled to $\kappa_{bulk}\approx 4000\ \mathrm{W\,m^{-1}K^{-1}}$].

| Width $L$ | $\kappa_M$ | $\kappa_P$ | Ratio |
| --- | --- | --- | --- |
| 0.3 µm | 430 | 257 | 0.6 |
| 0.7 µm | 700 | 700 | 1.0 |
| 2.0 µm | 1040 | 4000 | 3.8 |

Signature: a 40% dip at $L \approx \lambda_N$, then $L^2$ rise to a 3.8× excess at $L = 2\ \mu m$. Fourier-with-boundaries cannot produce a dip.

At 300 K $\lambda_N \approx 100$–$200\ \mathrm{nm}$; the window requires sub-300 nm ribbons where etch damage dominates. Room-temperature operation is not claimed.

## 6. Contradiction ledger

- Wall specularity: specular reflection preserves momentum and collapses the slip term. Roughness must stay below ~1 nm; unproven for FIB-cut graphite.
- Out-of-plane coupling in graphite can shunt the in-plane drift; thin ($<50$ nm) ribbons reduce this.
- $\lambda_N$ and $\lambda_U$ values above are estimates from one conductivity anchor. The predicted dip position inherits that error: ±40%.
- Triviality check: second sound and phonon Poiseuille flow are published physics (1960s Gurzhi; graphite 2017+). The unclaimed item is the conduit specification — a width-tuned heat strap at 2–4× the Fourier conductance for its mass. Originality scores accordingly.
- Prior art not checked (protocol lock 1). Highest-risk existing work: cryogenic phononic heat guides.

## 7. Experiment and null result

Suspended graphite ribbons, widths 0.3/0.5/0.7/1/2/4/8 µm, fixed 20 µm length, 3 samples each. $\kappa$ by Raman thermometry, 50–200 K, tolerance ±12%. Controls: bulk crystal (no dip), amorphous carbon film (no dip).

Null result: monotone $\kappa(L)$, no minimum, slope 1.0. Success branch: dip at 0.5–1 µm and slope 2.0 above it.

Cannot distinguish: viscous drift from a specularity artifact at a single width — the width series is the discriminator.

Cost: USD 30–60 k (cryostat, Raman bench, 21 samples).

## 8. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| --- | --- | --- | --- | --- | --- |
| 3 | 4 | 4 | 5 | 3 | 4 |

Total 23/30.

## 9. Applications

Near-term: 3–4× mass reduction in 77–150 K heat straps for superconducting magnets and IR detectors. Long-horizon: width-programmed thermal circuits where conductance is set by geometry instead of material choice.

## 10. Unresolved

Whether any commercial graphite foil holds a 1 nm wall finish after patterning. If not, the effect survives only in exfoliated crystals and the device claim fails while the physics claim stands.
