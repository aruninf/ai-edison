---
name: first-principles-discovery
description: Autonomous first-principles physical discovery engine. Formulates uncatalogued physical mechanisms, mathematical models, falsification criteria, and in silico simulation sweeps outside established textbooks and commercial engineering limits.
---

# First-Principles Discovery Skill

An operational skill for autonomous agents and human researchers to formulate, derive, stress-test, and virtually simulate physical mechanisms that do not exist in academic textbooks, patent databases, or commercial industry.

## Philosophy & Core Manifesto

Everything takes time and deliberate, cumulative steps to build the final breakthrough. We do not begin from a narrow, isolated problem: we are digging for what has never yet been conceived. History proves that every foundational discovery emerged by breaking the established rules of its era. 

New thoughts, new fundamental laws, and new horizons do not emerge from repeating consensus: they come when we dare to step outside the conventional scope and box. Every experiment, every refutation, and every failure generates new light, new discoveries, and new hope for upcoming generations. When old rules break, new horizons and new hopes emerge.

## When to Activate This Skill

Activate this skill when:
1. The user requests an out-of-the-box physical mechanism or engineering invention for a hard physical problem.
2. The user demands solutions that bypass or circumvent known textbook boundaries (such as Maxwell-Betti reciprocity, the Debye screening limit, the de Gennes polymer knotting theorem, or radiolytic water cleavage).
3. The user requires a complete first-principles mathematical model with dimensions checked, physical bounds, an adversarial contradiction ledger, and a concrete falsification experiment.
4. The goal is to perform divergent physical exploration rather than summarizing existing literature.

## The Hard Locks

1. **No retrieval during discovery:** Do not survey or summarize existing commercial devices or literature papers. Reason strictly from first-principles physics, geometry, and thermodynamic accounting.
2. **Tag every variable explicitly:** Every parameter must be tagged as one of:
   * `[established]` (physically verified constant or measured property)
   * `[assumed]` (baseline geometry or operational condition)
   * `[hypothesized]` (the candidate mechanism's derived behavior)
   * `[unknown]` (unresolved open boundary)
3. **Anti-Hedge Protocol:**
   * **Banned phrases:** Never write *further research is needed, it remains to be seen, promising, exciting, cutting-edge, paradigm-shifting, game-changer, revolutionary, groundbreaking, delve, tapestry, fascinating, robust, novel approach, in conclusion, at the end of the day.*
   * **Magnitude obligation:** Every claim must carry a number, an order-of-magnitude derivation, or an explicit statement of why it cannot be calculated.
   * **Numeric confidence:** Confidence is an integer percentage with a one-line factual basis, never a vague adjective.
4. **Style gates:** Zero emojis anywhere. No em-dashes or en-dashes; use hyphens (-), colons (:), commas (,), or parentheses.

## The 8-Phase Discovery Execution Pipeline

### Phase 1: Deconstruction
Strip the problem to the bare physical requirement. Mark all inherited assumptions as **necessary / inherited / decorative**. Discard decorative and inherited constraints.

### Phase 2: Divergent Exploration (10-Axis Diversity Matrix)
Generate candidate mechanisms that differ on at least four of these ten physical axes:
* Substrate
* Length scale
* Time scale
* Energy scale
* Coupling type
* Topology
* Information carrier
* Thermodynamic regime
* Symmetry used
* Interacting bodies

### Phase 3: Construction
Derive the mathematical model from first principles:
* Name every variable and state its SI dimensions.
* Derive conservation equations (mass, momentum, energy, charge).
* Check dimensional consistency across every term.
* Verify limiting cases against known physics.

### Phase 4: Adversarial Pass
Execute the 6-point attack order:
1. Conservation and symmetry verification.
2. Thermodynamic entropy accounting ($dS/dt \ge 0$).
3. Known experimental bounds in the operating regime.
4. Hidden assumptions.
5. Scaling failures at extreme limits.
6. Triviality check: is this an existing phenomenon in disguise?

Log all failure points and unresolved tensions in the **Contradiction Ledger**.

### Phase 5: Dead-Hypothesis Protocol
If a candidate mechanism violates a fundamental conservation law or fails an adversarial test, declare it dead. Document the killing blow and preserve the carcass. Dead hypotheses are critical results.

### Phase 6: Experimental Falsification Design
Design the smallest safe experiment that separates the hypothesis from the conventional explanation:
* Specify instruments, tolerances, calibration, and sample preparation.
* Define the exact observation that constitutes a null result before describing the success branch.
* Explicitly state what the experiment cannot distinguish.

### Phase 7: Simulation Sweep Verification
Where applicable, implement a standalone Python standard library simulation sweep (`hypotheses/simulations/exp*.py`) running 1,000 to 10,000 Monte Carlo or boundary-value trials with zero external dependencies to verify parameter sensitivity.

### Phase 8: Canonical Output Formatting
Format the final discovery dossier using the exact 16-point template.

## The Canonical 16-Point Output Template

Every generated discovery dossier must contain all 16 numbered sections in this exact sequence:

1. **Name:** Descriptive technical title and parenthetical classifier.
2. **Fundamental problem:** The stripped physical requirement.
3. **Falsification statement:** Specific measurable condition that kills the hypothesis, stated before the mechanism.
4. **Hypothesis:** One concise, unhedged paragraph describing the physical core.
5. **Why convention is insufficient here:** Precise physical and mathematical reasons existing technology and classical theorems fail.
6. **Mechanism:** Step-by-step physical walkthrough with all variables tagged (`[established]`, `[assumed]`, `[hypothesized]`, `[unknown]`).
7. **Mathematical model:** Complete governing equations, derivation steps, and explicit dimensional checks.
8. **Physical constraints:** Conservation limits, operational bounds, and breakdown thresholds.
9. **Contradiction ledger:** Documented failure modes, edge-case limitations, and unresolved physical tensions.
10. **Experiment:** Hardware apparatus, metrology, controls, and null result definition.
11. **Expected observations:** Explicit success branch and failure branch predictions.
12. **Magnitudes:** Complete numerical summary table of all operational values.
13. **Applications:** Concrete nearest-term engineering uses and long-horizon applications.
14. **Unresolved questions:** Critical open scientific questions and risks.
15. **Score card:** 6 integer scores (0 to 5) across originality, mathematical consistency, physical plausibility, testability, impact if true, and cost to test; total score; and numeric confidence percentage with one-line basis.
16. **Status:** `live`, `wounded`, or `dead` (with the killing blow stated).
