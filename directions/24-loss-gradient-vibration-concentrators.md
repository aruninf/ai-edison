# Vector 24: Loss-Gradient Vibration Concentrators

**Status:** wounded (no power gain in a linear chain; value sits in threshold crossing and damping per mass)
**Confidence:** 40%, basis: non-Hermitian skin effect in mechanical lattices is published (2022+); this device framing is not.

## 1. Falsification statement

A 12-cell passive lattice with coupling ratio $r = 1.6$ must show ≥50× local velocity amplitude at the designated port versus a uniform lattice under the same broadband input (20–800 Hz). It dies if measured concentration is below 5×, or if harvested power never exceeds the uniform-lattice baseline at any rectifier threshold.

## 2. Fundamental problem

Get broadband ambient vibration above a rectifier's turn-on threshold, or absorb it, using a structure that is lighter than the equivalent tuned mass.

## 3. Mechanism

Break the symmetry of coupling between neighbouring cells — cell $n$ drives $n+1$ harder than the reverse. In an open, lossy chain this pushes every eigenmode into one edge: the non-Hermitian skin effect. A small change of one coupling ratio moves all mode weight to a chosen port, with the concentration factor set by $r^N$ rather than by resonance quality. That gives broadband concentration with no tuning.

## 4. Mathematical model

Hatano–Nelson chain, mode amplitude ratio between edge and bulk:

$$A_{edge}/A_{bulk} \approx r^{N}, \qquad r = t_{L}/t_{R}$$

For $N = 12$, $r = 1.6$: $1.6^{12} = 280$. Dimensionless; the physical amplitude follows from power conservation. Checked.

Damping per unit mass: concentrating a fixed loss $\eta$ into a volume fraction $\phi = r^{-N}$ multiplies the effective structural loss factor by $1/\phi$ at fixed total mass, so a 2% lossy insert in a 5 kg lattice behaves as a 100× larger damper at the port mode [SPECULATION, linear model only].

## 5. Contradiction ledger

- No power gain. A passive chain cannot amplify; it redistributes. Harvested power at the port equals harvested power distributed, unless the rectifier is threshold-limited. The energy claim survives only for sub-threshold inputs, and the magnitude of that gain is set by the rectifier's nonlinearity, not by the lattice.
- Realization needs asymmetric coupling, which in practice means active or parametric elements, or asymmetric geometry that also changes stiffness and therefore passbands. Passive realization at $r = 1.6$ is a fabrication, not an analysis, problem.
- Damping claim collides with the lossy-insert bandwidth: concentration is broadband only for the skin modes, not for all modes.
- Triviality check: the skin effect is published; vibration concentration and damping-per-mass devices are engineering variations on it. Originality is scored 2 for that reason.
- Prior art not checked (protocol lock 1).

## 6. Experiment and null result

12-cell aluminium lattice, machined asymmetric ligaments, 0.4 kg, shaker input 0.1 g RMS swept 20–800 Hz, laser vibrometry at 6 points across the chain, 5 coupling ratios (1.1 to 1.6). Controls: symmetric lattice, and a lattice with the port terminated in a matched load.

Null: concentration <5× at every ratio, or port power within ±10% of baseline across thresholds. Success: 30–100× amplitude at $r = 1.4$–1.6, with port power exceeding baseline only for inputs below the rectifier threshold.

Cannot distinguish: skin localization from a bandgap edge effect — sweep $r$ through unity and watch continuity.

Cost: USD 8–20 k.

## 7. Score card

| originality | math consistency | physical plausibility | testability | impact if true | cost to test |
| --- | --- | --- | --- | --- | --- |
| 2 | 4 | 3 | 4 | 2 | 3 |

Total 18/30.

## 8. Applications

Near-term: damping inserts for machine-tool and airframe panels where added mass is the binding constraint. Long-horizon: passive wake-up circuits for sensors that must survive below-threshold vibration for years.

## 9. Unresolved

Whether a purely passive lattice reaches $r > 1.3$ without gain elements. If it cannot, the vector reduces to a damping trick already covered by lossy metamaterial work, and the honest outcome is a carcass.
