#!/usr/bin/env python3
"""
Repository Integrity & Protocol Gate for inf-research (AI Edison).

Checks:
1. Every dossier in directions/ is indexed in directions/README.md.
2. Every relative link in directions/README.md resolves to an existing file.
3. Every EXP-*.md in hypotheses/ is registered in hypotheses/README.md.
4. Zero emojis anywhere in directions/, hypotheses/, README.md, or CONTRIBUTING.md.
5. Zero em-dashes or en-dashes in newly governed files (directions/README.md,
   directions/77-*.md, hypotheses/EXP-20261125-010-*.md, CONTRIBUTING.md).

Exit code 0 if all hard checks pass; non-zero otherwise.
"""

import pathlib
import re
import sys
from typing import List


ROOT = pathlib.Path(__file__).resolve().parent.parent

EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")


def check_directions_index(errors: List[str]) -> None:
    cat_path = ROOT / "directions" / "README.md"
    if not cat_path.exists():
        errors.append("Missing directions/README.md")
        return

    cat_text = cat_path.read_text(encoding="utf-8")

    # Verify all direction files are referenced in directions/README.md
    for p in sorted((ROOT / "directions").glob("*.md")):
        if p.name == "README.md":
            continue
        if p.name not in cat_text:
            errors.append(f"Unindexed direction dossier in directions/README.md: {p.name}")

    # Verify all relative links resolve
    for rel in re.findall(r"\(\./([^)#]+)\)", cat_text):
        target = ROOT / "directions" / rel
        if not target.exists():
            errors.append(f"Broken relative link in directions/README.md: ./{rel}")


def check_hypotheses_registry(errors: List[str]) -> None:
    reg_path = ROOT / "hypotheses" / "README.md"
    if not reg_path.exists():
        errors.append("Missing hypotheses/README.md")
        return

    reg_text = reg_path.read_text(encoding="utf-8")
    for p in sorted((ROOT / "hypotheses").glob("EXP-*.md")):
        if p.name not in reg_text:
            errors.append(f"Unregistered hypothesis in hypotheses/README.md: {p.name}")


def check_no_emojis(errors: List[str]) -> None:
    scan_paths = (
        list((ROOT / "directions").glob("*.md"))
        + list((ROOT / "hypotheses").glob("*.md"))
        + list((ROOT / "hypotheses" / "simulations").glob("*.py"))
        + [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    )
    for p in scan_paths:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        hits = EMOJI_RE.findall(text)
        if hits:
            errors.append(f"Emoji detected in {p.relative_to(ROOT)}: {hits[:5]}")


def check_strict_dashes(errors: List[str]) -> None:
    strict_files = [
        ROOT / "directions" / "README.md",
        ROOT / "directions" / "77-thermo-acoustic-vapor-jet-chf-lattice.md",
        ROOT / "directions" / "78-acoustic-mechanical-impedance-transformer.md",
        ROOT / "directions" / "79-diurnal-thermal-snap-anvil-dust-ejection.md",
        ROOT / "directions" / "80-sub-crossover-flashover-quenching-lattice.md",
        ROOT / "directions" / "81-ponderomotive-trajectory-flashover-ejector.md",
        ROOT / "hypotheses" / "EXP-20261125-010-thermo-acoustic-chf-lattice.md",
        ROOT / "hypotheses" / "EXP-20261125-011-acoustic-impedance-transformer.md",
        ROOT / "hypotheses" / "EXP-20261125-012-thermal-snap-dust-ejection.md",
        ROOT / "hypotheses" / "simulations" / "exp010_thermo_acoustic_chf_sweep.py",
        ROOT / "hypotheses" / "simulations" / "exp011_acoustic_impedance_transformer_sweep.py",
        ROOT / "hypotheses" / "simulations" / "exp012_thermal_snap_dust_ejection_sweep.py",
        ROOT / "CONTRIBUTING.md",
    ]
    for p in strict_files:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if "\u2014" in text or "\u2013" in text:
            errors.append(f"Em-dash or en-dash detected in {p.relative_to(ROOT)}")


def main() -> int:
    errors: List[str] = []
    check_directions_index(errors)
    check_hypotheses_registry(errors)
    check_no_emojis(errors)
    check_strict_dashes(errors)

    direction_count = len([p for p in (ROOT / "directions").glob("*.md") if p.name != "README.md"])
    exp_count = len(list((ROOT / "hypotheses").glob("EXP-*.md")))
    sim_count = len(list((ROOT / "hypotheses" / "simulations").glob("exp*.py")))

    print(
        f"inf-research gate: {direction_count} dossier files, "
        f"{exp_count} experiments, {sim_count} simulation sweeps"
    )
    if errors:
        print("FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("PASSED: all index, registry, link, and style checks green.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
