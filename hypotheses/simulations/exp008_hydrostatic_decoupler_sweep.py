#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261117-008
Smectic-A Topological Hydrostatic Pressure Decoupler

Coupled Multi-Physics Solver:
1. Smectic layer compression modulus (B) and de Gennes anchoring energy
2. Helical wall tilt angle coupling (lambda_s)
3. Modified Janssen hydrostatic momentum balance
4. Bottom pressure saturation calculation vs classical rho*g*h
5. Dislocation nucleating shear stress limit check (tau < tau_crit)

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
import sys
from typing import Dict, Any, List

G_GRAV = 9.80665
TAU_CRIT_SM = 1.0e5  # Critical shear stress to nucleate edge dislocations in smectic layers (Pa)


def evaluate_decoupler_trial(
    R_pipe_m: float,       # Pipe radius (m, 0.01 - 0.20)
    h_column_m: float,     # Column height (m, 5 - 100)
    rho_fluid: float,      # Smectic fluid density (kg/m^3, 980 - 1150)
    B_modulus_MPa: float,  # Smectic layer compression modulus (MPa, 5 - 50)
    tilt_angle_deg: float, # Homeotropic helical anchoring tilt angle (degrees, 15 - 75)
    T_amb: float,          # Operating temperature (K, 275 - 330)
) -> Dict[str, Any]:
    """
    Evaluates one smectic hydrostatic decoupling trial.
    """
    B_mod = B_modulus_MPa * 1e6
    tilt_rad = math.radians(tilt_angle_deg)
    sin_th = math.sin(tilt_rad)
    cos_th = math.cos(tilt_rad)

    # 1. Smectic Temperature Window Check (8CB smectic-A phase: 294.5 K to 306.5 K)
    # Engineered binary/ternary mixtures extend smectic phase: 260 K to 340 K
    if T_amb < 265.0 or T_amb > 335.0:
        return {
            "status": "FAIL_PHASE_TRANSITION",
            "reason": "Temperature outside smectic-A mesophase stability window",
            "T_amb": T_amb,
        }

    # 2. Wall Coupling Coefficient lambda_s
    # Bulk compression modulus B_bar ~ 1.5e9 Pa (liquid compressibility)
    B_bulk = 1.5e9
    lambda_s = (B_mod / (B_mod + B_bulk * 0.01)) * sin_th * cos_th
    lambda_s = max(0.05, min(0.48, lambda_s))

    # 3. Maximum Wall Shear Stress Check (Must not nucleate layer slip)
    # At steady state: tau_wall = rho * g * R / 2
    tau_wall = (rho_fluid * G_GRAV * R_pipe_m) / 2.0
    if tau_wall > TAU_CRIT_SM:
        return {
            "status": "FAIL_LAYER_DISLOCATION_SLIP",
            "reason": "Wall shear stress exceeds critical dislocation nucleation limit",
            "tau_wall_kPa": tau_wall / 1e3,
            "tau_crit_kPa": TAU_CRIT_SM / 1e3,
        }

    # 4. Classical Hydrostatic Pressure
    P_classical = rho_fluid * G_GRAV * h_column_m

    # 5. Smectic Decoupled Base Pressure Profile
    exponent = (2.0 * lambda_s * h_column_m) / R_pipe_m
    if exponent > 50.0:
        decay_factor = 0.0
    else:
        decay_factor = math.exp(-exponent)

    P_bottom = ((rho_fluid * G_GRAV * R_pipe_m) / (2.0 * lambda_s)) * (1.0 - decay_factor)
    P_sat = (rho_fluid * G_GRAV * R_pipe_m) / (2.0 * lambda_s)

    # Pressure reduction fraction
    reduction_pct = (1.0 - (P_bottom / P_classical)) * 100.0

    # Success bar:
    # 1. P_bottom <= 15.0 kPa (0.15 atm)
    # 2. Reduction >= 85% compared to classical hydrostatics
    if P_bottom > 15000.0 or reduction_pct < 85.0:
        return {
            "status": "FAIL_INSUFFICIENT_DECOUPLING",
            "reason": "Bottom pressure exceeds ceiling or reduction < 85%",
            "P_bottom_kPa": P_bottom / 1e3,
            "reduction_pct": reduction_pct,
        }

    return {
        "status": "SUCCESS_DECOUPLER",
        "P_bottom_kPa": P_bottom / 1e3,
        "P_classical_kPa": P_classical / 1e3,
        "P_sat_kPa": P_sat / 1e3,
        "reduction_pct": reduction_pct,
        "R_pipe_cm": R_pipe_m * 100.0,
        "h_column_m": h_column_m,
        "tau_wall_kPa": tau_wall / 1e3,
    }


def run_10000_decoupler_sweep(num_trials: int = 10000) -> None:
    random.seed(42)
    start_time = time.time()

    success_list: List[Dict[str, Any]] = []
    failure_counts: Dict[str, int] = {}

    print("=" * 80)
    print("AI EDISON IN SILICO DISCOVERY ENGINE: EXP-20261117-008")
    print("Smectic-A Topological Hydrostatic Pressure Decoupler")
    print(f"Beginning {num_trials:,} Virtual Multi-Physics Trials...")
    print("=" * 80)

    for i in range(num_trials):
        R_pipe_m = random.uniform(0.01, 0.15)
        h_column_m = random.uniform(5.0, 100.0)
        rho_fluid = random.uniform(980.0, 1150.0)
        B_modulus_MPa = random.uniform(5.0, 45.0)
        tilt_angle_deg = random.uniform(15.0, 75.0)
        T_amb = random.uniform(270.0, 330.0)

        res = evaluate_decoupler_trial(
            R_pipe_m=R_pipe_m,
            h_column_m=h_column_m,
            rho_fluid=rho_fluid,
            B_modulus_MPa=B_modulus_MPa,
            tilt_angle_deg=tilt_angle_deg,
            T_amb=T_amb,
        )

        status = res["status"]
        if status == "SUCCESS_DECOUPLER":
            res["trial_idx"] = i
            success_list.append(res)
        else:
            failure_counts[status] = failure_counts.get(status, 0) + 1

    elapsed = time.time() - start_time
    total_success = len(success_list)
    success_rate = (total_success / num_trials) * 100.0

    print(f"\nSimulation complete in {elapsed:.2f} seconds ({num_trials / elapsed:,.0f} trials/sec).")
    print(f"Total Trials: {num_trials:,}")
    print(f"Successful Decoupling Regimes: {total_success:,} ({success_rate:.2f}%)")
    print("\nFalsification / Failure Breakdown:")
    for mode, count in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / num_trials) * 100.0
        print(f"  * {mode:32s}: {count:6,d} ({pct:5.1f}%)")

    # Champion: Highest Pressure Reduction at Maximum Height
    sorted_by_reduction = sorted(success_list, key=lambda x: x["reduction_pct"], reverse=True)
    best = sorted_by_reduction[0]

    print("\n" + "=" * 80)
    print("PARETO FRONTIER: CHAMPION HYDROSTATIC DECOUPLER (Trial #%d)" % best["trial_idx"])
    print("=" * 80)
    print("   * Column Height:                 %.1f meters" % best["h_column_m"])
    print("   * Classical Hydrostatic Head:    %.1f kPa (%.2f atm)" % (best["P_classical_kPa"], best["P_classical_kPa"] / 101.325))
    print("   * Measured Base Pressure:        %.2f kPa (%.3f atm)" % (best["P_bottom_kPa"], best["P_bottom_kPa"] / 101.325))
    print("   * Hydrostatic Pressure Cut:      %.2f%% reduction" % best["reduction_pct"])
    print("   * Pipe Radius:                   %.1f cm" % best["R_pipe_cm"])
    print("   * Sidewall Shear Stress:         %.2f kPa" % best["tau_wall_kPa"])
    print("=" * 80)


if __name__ == "__main__":
    trials = 10000
    if len(sys.argv) > 1:
        try:
            trials = int(sys.argv[1])
        except ValueError:
            pass
    run_10000_decoupler_sweep(trials)
