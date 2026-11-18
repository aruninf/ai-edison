# Installation and Quick-Start Guide: First-Principles Discovery Skill

This guide explains how to install and activate the `first-principles-discovery` skill across different agent environments, IDEs, and local workflows.

---

## 1. Fast Setup (One-Liner)

### For Google Antigravity / Gemini CLI (`agy`)

To install globally for all Antigravity sessions:

```bash
mkdir -p ~/.gemini/skills/first-principles-discovery
curl -sSL https://raw.githubusercontent.com/aruninf/ai-edison/main/SKILL.md -o ~/.gemini/skills/first-principles-discovery/SKILL.md
```

Or clone the entire repository directly into your local agent skills folder:

```bash
git clone https://github.com/aruninf/ai-edison.git ~/.gemini/skills/first-principles-discovery
```

Once installed, Antigravity automatically detects `first-principles-discovery` upon startup.

---

### For Claude Code (`claude`)

Install the skill into your user-level or project-level Claude configuration:

```bash
# Project-level installation
mkdir -p .claude/skills/first-principles-discovery
curl -sSL https://raw.githubusercontent.com/aruninf/ai-edison/main/SKILL.md -o .claude/skills/first-principles-discovery/SKILL.md

# Global user-level installation
mkdir -p ~/.claude/skills/first-principles-discovery
curl -sSL https://raw.githubusercontent.com/aruninf/ai-edison/main/SKILL.md -o ~/.claude/skills/first-principles-discovery/SKILL.md
```

---

### For Cursor, VS Code, or Windsurf

Clone the repository into your project workspace:

```bash
git clone https://github.com/aruninf/ai-edison.git
```

The repository includes pre-configured skill paths:
* `.agents/skills/first-principles-discovery/SKILL.md`
* `.gemini/skills/first-principles-discovery/SKILL.md`
* `SKILL.md`

Any agent workspace pointed to this directory will immediately index the discovery skill and protocols.

---

## 2. Verifying Installation

Verify that the skill is active by asking your agent:

```text
What skills are currently available, and how does first-principles-discovery operate?
```

The agent should report `first-principles-discovery` as active, referencing its 8-phase pipeline and 16-point canonical output template.

---

## 3. How to Prompt the Agent

Once installed, trigger the discovery engine by providing a bare physical requirement or boundary condition.

### Example Prompts

#### Space Living & Radiation
```text
Activate the first-principles-discovery skill. Formulate an uncatalogued physical device that protects biological cells from 1 GeV/nucleon cosmic rays without passive mass shielding or high-power magnetic fields. Follow the full 16-point protocol.
```

#### Cellular Longevity & Senescence
```text
Use first-principles-discovery to derive a non-enzymatic, non-chemical mechanism that reverses the topological knotting of genomic chromatin in senescent cell nuclei. Include exact dimensional checks and a falsification experiment.
```

#### Thermodynamics & Metamaterials
```text
Apply the first-principles-discovery engine: design a monolithic mechanical diode that breaks Maxwell-Betti reciprocity in static mechanics. Document the contradiction ledger and compute the forward-to-backward transmission ratio.
```

---

## 4. Running In Silico Simulation Sweeps Locally

The skill comes with high-throughput multi-physics simulation solvers built purely on Python standard library modules (zero pip installs required):

```bash
# Clone the repository
git clone https://github.com/aruninf/ai-edison.git
cd ai-edison

# Run a 10,000-trial Monte Carlo sweep for the Static Mechanical Diode
python3 hypotheses/simulations/exp003_mechanical_diode_sweep.py 10000

# Run a 10,000-trial sweep for the Cavitation-Snap Evaporative Harvester
python3 hypotheses/simulations/exp002_cavitation_sweep.py 10000

# Run a 10,000-trial sweep for the Smectic Hydrostatic Decoupler
python3 hypotheses/simulations/exp008_hydrostatic_decoupler_sweep.py 10000
```

---

## 5. Summary of Agent Hard Locks

When this skill runs, the agent adheres to these strict locks:
1. No retrieval during discovery (no searching Google, patents, or literature papers to copy existing gadgets).
2. Explicit variable tags: `[established]`, `[assumed]`, `[hypothesized]`, `[unknown]`.
3. Anti-hedge enforcement: Zero fluff phrases, mandatory numerical magnitudes.
4. Falsification statement stated before mechanism description.
5. 16-point output format in exact sequential order.
