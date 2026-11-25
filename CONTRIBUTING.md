# Contributing & Discovering New Innovations

This guide defines the end-to-end standard for proposing, deriving, stress-testing, and registering a new uncatalogued physical invention in this repository.

---

## 1. Before You Start: The Hard Locks

Every new discovery must obey the operational locks in [RESEARCH_PROTOCOL.md](./RESEARCH_PROTOCOL.md) and [SKILL.md](./SKILL.md):

1. **Start from the bare physical requirement, not existing devices.** Strip away inherited and decorative assumptions (Phase 1).
2. **Diverge across the 10-Axis Matrix.** A new mechanism must differ from prior vectors on at least 4 of: *substrate, length scale, time scale, energy scale, coupling type, topology, information carrier, thermodynamic regime, symmetry used, interacting bodies* (Phase 2).
3. **Falsification-First Order.** State the exact measurable condition that kills the hypothesis (Section 3) before describing the mechanism (Section 6).
4. **Tag every physical variable.** Label each parameter as `[established]`, `[assumed]`, `[derived]`, `[hypothesized]`, or `[unknown]`.
5. **Magnitude obligation.** Every quantitative claim requires a number, an order-of-magnitude derivation, or an explicit statement of why it cannot be calculated.
6. **Anti-Hedge & Style Gates.**
   * **Zero emojis** anywhere in dossiers, code, comments, or commits.
   * **Zero em-dashes or en-dashes**; use hyphens (`-`), colons (`:`), commas (`,`), or parentheses (`()`).
   * **Banned phrases:** Never use *further research is needed, it remains to be seen, promising, exciting, cutting-edge, paradigm-shifting, game-changer, revolutionary, groundbreaking, delve, tapestry, fascinating, robust, novel approach, in conclusion, at the end of the day.*
   * **Numeric confidence:** Report confidence as an integer percentage with a one-line factual basis.
7. **Publish the Contradiction Ledger.** Document every failure mode, scaling breakdown, and unresolved tension. If a hypothesis violates conservation laws or fails adversarial checks, mark its status `dead` and preserve the killing blow.

---

## 2. Step-by-Step Submission Workflow

### Step 1: Assign the Next Vector Number and Create the Dossier
Create `directions/<NN>-<kebab-case-descriptor>.md` using the next sequential integer (`78`, `79`, ...).
Include all **16 canonical sections** in exact order:
1. `## 1. Name`
2. `## 2. Fundamental problem`
3. `## 3. Falsification statement`
4. `## 4. Hypothesis`
5. `## 5. Why convention is insufficient here`
6. `## 6. Mechanism`
7. `## 7. Mathematical model` (with explicit SI dimensional checks)
8. `## 8. Physical constraints`
9. `## 9. Contradiction ledger`
10. `## 10. Experiment` (instruments, tolerances, controls, null result)
11. `## 11. Expected observations` (success branch and failure branch)
12. `## 12. Magnitudes` (summary table)
13. `## 13. Applications` (nearest-term and long-horizon)
14. `## 14. Unresolved questions`
15. `## 15. Score card` (6 integers 0-5, total / 30, numeric confidence %)
16. `## 16. Status` (`live`, `wounded`, or `dead`)

### Step 2: Build a 10,000-Trial In Silico Sweep (Pure Python Standard Library)
If the mechanism admits a lumped-parameter, thermodynamic, or continuum model:
1. Create `hypotheses/simulations/exp<NNN>_<snake_case>_sweep.py` using **only the Python standard library** (zero `numpy`, `scipy`, or external packages).
2. Run at least `10,000` Monte Carlo or boundary-value parameter variations.
3. Enforce explicit falsification gates inside the solver and print exact failure/success counts and champion parameters.
4. Create the matching experiment dossier `hypotheses/EXP-YYYYMMDD-<NNN>-<descriptor>.md` following [frameworks/experiment-template.md](./frameworks/experiment-template.md).

### Step 3: Register and Index Your Discovery
1. Add the new vector to the appropriate domain table and Quick Navigation section in [directions/README.md](./directions/README.md).
2. If you added an experiment/simulation, register it in [hypotheses/README.md](./hypotheses/README.md) and [.github/workflows/verify_sweeps.yml](./.github/workflows/verify_sweeps.yml).
3. Update the vector count and highlights in [README.md](./README.md).

### Step 4: Run the Automated Repository Gate
Before committing, run the integrity and protocol gate:

```bash
python3 scripts/verify_repo.py
```

Verify that all links resolve, all vectors are indexed, all simulations execute cleanly, and zero style violations are reported.
