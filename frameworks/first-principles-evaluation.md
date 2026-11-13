# Framework: First-Principles Evaluation Rubric

Every candidate invention concept must pass this questionnaire before resources are dedicated to hardware fabrication or formal simulation.

## Gate 1: Physical Mechanism Clarity
1. **Underlying Law:** Which established equation or law of physics describes the core mechanism?
2. **Energy Conservation:** Can you draw a complete Sankey energy flow diagram accounting for all inputs, outputs, dissipation, and entropy increases?
3. **No Magic Assumptions:** Does the proposal rely on any unverified assumptions (e.g. room-temperature ambient superconductors, infinite thermal conductivity, zero-viscosity fluids at STP)?

## Gate 2: Differentiation from Legacy Machinery
1. **The Legacy Baseline:** What existing machine or assembly performs this function today?
2. **The Fundamental Limit:** What exact limit (friction, Carnot bound, inertia, material fatigue, switching heat) does the legacy design hit?
3. **Why Now / Why Different:** Is this truly a new mechanical principle, or merely an old machine with sensors and microcontrollers attached? If this principle was known 100 years ago, what specific barrier previously prevented its deployment?

## Gate 3: Thermodynamic & Scaling Viability
1. **Dimensional Scaling ($L^1, L^2, L^3$):** How does the mechanism scale from 1 mm to 10 cm to 1 meter?
   * *Surface area vs Volume scaling:* If relying on surface tension ($L^1$) or surface charge ($L^2$), does the mechanism collapse when scaled to mass-dominant regimes ($L^3$)?
2. **Theoretical Efficiency Upper Bound:** What is the theoretical maximum thermodynamic efficiency?
3. **Cycle Lifetime:** What physical wear or degradation mode will cause the mechanism to fail after $10^3$, $10^5$, or $10^7$ cycles?

## Gate 4: Falsification Protocol
1. **The Fatal Flaw Test:** What is the most likely reason this mechanism will not work in practice?
2. **Minimal Falsification Experiment:** What is the simplest, cheapest benchtop experiment that can test the validity of the hypothesis within 7 to 14 days?
3. **Quantified Go / No-Go Threshold:** At what precise measured value is the hypothesis declared dead and archived?
