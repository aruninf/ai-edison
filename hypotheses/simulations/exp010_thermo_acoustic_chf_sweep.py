#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261125-010
Self-Synchronized Thermo-Acoustic Vapor-Jet Diode Lattice (TAVJ-DL)

Coupled Multi-Physics Solver:
1. Clausius-Clapeyron vapor-generation overpressure inside micro-cavities
2. Solid-substrate conduction drop (Cu, k = 385 W/(m*K)) and microlayer evaporation limit
3. Vapor-jet ejection velocity through vertical nozzles (Mach <= 0.45 shear-stability cap)
4. Poiseuille + inertial Tesla-diode liquid return pressure balance
5. Jet-penetration Weber number (We_jet >= 8.0) and Kutateladze-Zuber CHF baseline (1.109 MW/m^2)

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
from typing import Dict, Any, List


# Physical constants for saturated water at P_amb = 101.325 kPa, T_sat = 373.15 K [established]
P_AMB_PA = 101325.0
T_SAT_K = 373.15
H_FG_J_KG = 2.257e6
RHO_L_KG_M3 = 958.4
RHO_V_KG_M3 = 0.598
MU_L_PA_S = 2.82e-4
MU_V_PA_S = 1.23e-5
K_L_W_MK = 0.679
SIGMA_N_M = 0.0589
G_M_S2 = 9.81
GAMMA_V = 1.33
R_V_J_KG_K = 461.5
C_SOUND_V_M_S = math.sqrt(GAMMA_V * R_V_J_KG_K * T_SAT_K)  # ~ 478.6 m/s

# Copper substrate thermal conductivity [established] and microlayer thickness [assumed]
K_CU_W_MK = 385.0
DELTA_MICRO_M = 0.65e-6

# Kutateladze-Zuber pool-boiling CHF baseline (W/m^2)
Q_CHF_KZ_W_M2 = (
    0.131
    * H_FG_J_KG
    * math.sqrt(RHO_V_KG_M3)
    * (SIGMA_N_M * G_M_S2 * (RHO_L_KG_M3 - RHO_V_KG_M3)) ** 0.25
)


def evaluate_chf_trial(
    delta_T_base_K: float,       # Base-wall superheat above T_sat (K, 5 - 45)
    d_nozzle_m: float,           # Vapor nozzle diameter (m, 40e-6 - 160e-6)
    pitch_m: float,              # Unit cell pitch (m, 250e-6 - 850e-6)
    h_wall_m: float,             # Nozzle/artery height (m, 150e-6 - 600e-6)
    d_artery_m: float,           # Liquid return artery hydraulic diameter (m, 30e-6 - 110e-6)
    diodicity: float,            # Tesla-diode rectification ratio (1.5 - 4.5)
) -> Dict[str, Any]:
    """
    Evaluates one thermo-acoustic vapor-jet diode unit cell across thermodynamic,
    conductive, hydrodynamic, and shear-stability bounds.
    """
    A_cell = pitch_m * pitch_m
    A_nozzle = 0.25 * math.pi * d_nozzle_m * d_nozzle_m
    phi_v = A_nozzle / A_cell

    # Reject geometrically invalid cells
    if phi_v >= 0.35 or d_nozzle_m >= 0.60 * pitch_m or d_artery_m >= 0.45 * pitch_m:
        return {"status": "FAIL_GEOMETRY", "q_MW_m2": 0.0}

    # Solid fraction available for vertical heat conduction
    phi_solid = 1.0 - phi_v
    R_cond_m2K_W = h_wall_m / (K_CU_W_MK * phi_solid)

    # 3D internal chamber evaporative area ratio (sidewalls + floor)
    d_chamber_m = 0.65 * pitch_m
    A_evap_ratio = (math.pi * d_chamber_m * (0.6 * h_wall_m) + 0.25 * math.pi * d_chamber_m * d_chamber_m) / A_cell
    R_evap_m2K_W = DELTA_MICRO_M / (K_L_W_MK * A_evap_ratio)

    # Coupled iteration to solve interface superheat delta_T_int = delta_T_base - q * R_cond
    dP_dT = (H_FG_J_KG * RHO_V_KG_M3) / T_SAT_K
    K_loss = 2.4 + 0.05 * (h_wall_m / d_nozzle_m)
    v_v_cap = 0.45 * C_SOUND_V_M_S  # Shear-entrainment and Mach <= 0.45 stability cap (~215.4 m/s)

    L_art = 0.5 * pitch_m
    A_art_total = 2.0 * (0.25 * math.pi * d_artery_m * d_artery_m)
    delta_P_cap = (4.0 * SIGMA_N_M * math.cos(math.radians(35.0))) / d_artery_m
    R_visc = (32.0 * MU_L_PA_S * L_art) / (d_artery_m * d_artery_m)
    K_art = 1.8

    delta_T_int = 0.7 * delta_T_base_K
    q_sustained_W_m2 = 0.0
    v_v = 0.0
    choked = False

    for _ in range(12):
        delta_P_drive = max(0.0, dP_dT * delta_T_int)
        v_v_incomp = math.sqrt((2.0 * delta_P_drive) / (RHO_V_KG_M3 * K_loss))
        choked = v_v_incomp > v_v_cap
        v_v = min(v_v_incomp, v_v_cap)

        # Vapor mass flux limit
        q_vapor_W_m2 = RHO_V_KG_M3 * v_v * phi_v * H_FG_J_KG

        # Liquid return supply limit through lateral Tesla-diode arteries
        delta_P_liq_avail = delta_P_cap + 0.15 * delta_P_drive * (1.0 - 1.0 / diodicity)
        a_q = 0.5 * K_art * RHO_L_KG_M3
        b_q = R_visc
        c_q = -delta_P_liq_avail
        disc = b_q * b_q - 4.0 * a_q * c_q
        v_l_max = (-b_q + math.sqrt(max(0.0, disc))) / (2.0 * a_q)
        q_liq_limit_W_m2 = ((RHO_L_KG_M3 * v_l_max * A_art_total) / A_cell) * H_FG_J_KG

        # Microlayer conduction limit
        q_micro_limit_W_m2 = max(0.0, delta_T_int / R_evap_m2K_W)

        q_new = min(q_vapor_W_m2, q_liq_limit_W_m2, q_micro_limit_W_m2)
        delta_T_int_new = max(0.5, delta_T_base_K - q_new * R_cond_m2K_W)
        delta_T_int = 0.5 * delta_T_int + 0.5 * delta_T_int_new
        q_sustained_W_m2 = q_new

    We_jet = (RHO_V_KG_M3 * v_v * v_v * d_nozzle_m) / SIGMA_N_M
    Re_v = (RHO_V_KG_M3 * v_v * d_nozzle_m) / MU_V_PA_S
    htc_W_m2K = q_sustained_W_m2 / delta_T_base_K
    q_MW_m2 = q_sustained_W_m2 / 1e6
    enhancement_ratio = q_sustained_W_m2 / Q_CHF_KZ_W_M2

    # Falsification / viability gates:
    # 1. Jet Weber number We_jet >= 8.0 (clears vapor off surface without coalescence)
    # 2. Must exceed 10x Kutateladze-Zuber (> 11.09 MW/m^2)
    if We_jet < 8.0:
        return {
            "status": "FAIL_COALESCENCE",
            "q_MW_m2": q_MW_m2,
            "We_jet": We_jet,
            "enhancement": enhancement_ratio,
        }
    if enhancement_ratio < 10.0:
        return {
            "status": "FAIL_BELOW_10X_KZ",
            "q_MW_m2": q_MW_m2,
            "We_jet": We_jet,
            "enhancement": enhancement_ratio,
        }

    return {
        "status": "SUCCESS_CHF_BREAKTHROUGH",
        "q_MW_m2": q_MW_m2,
        "enhancement": enhancement_ratio,
        "v_v_m_s": v_v,
        "We_jet": We_jet,
        "Re_v": Re_v,
        "htc_kW_m2K": htc_W_m2K / 1e3,
        "delta_T_int_K": delta_T_int,
        "choked": choked,
        "phi_v": phi_v,
    }


def run_simulation_sweep(num_trials: int = 10000, seed: int = 20261125) -> None:
    rng = random.Random(seed)
    t0 = time.time()

    counts = {
        "SUCCESS_CHF_BREAKTHROUGH": 0,
        "FAIL_COALESCENCE": 0,
        "FAIL_BELOW_10X_KZ": 0,
        "FAIL_GEOMETRY": 0,
    }

    best_trial: Dict[str, Any] = {}
    best_q = 0.0
    shear_capped_successes = 0
    all_success_q: List[float] = []

    for i in range(1, num_trials + 1):
        delta_T_base = rng.uniform(5.0, 45.0)
        d_nozzle = rng.uniform(40e-6, 160e-6)
        pitch = rng.uniform(250e-6, 850e-6)
        h_wall = rng.uniform(150e-6, 600e-6)
        d_artery = rng.uniform(30e-6, 110e-6)
        diodicity = rng.uniform(1.5, 4.5)

        res = evaluate_chf_trial(
            delta_T_base, d_nozzle, pitch, h_wall, d_artery, diodicity
        )
        status = res["status"]
        counts[status] += 1

        if status == "SUCCESS_CHF_BREAKTHROUGH":
            q_val = res["q_MW_m2"]
            all_success_q.append(q_val)
            if res["choked"]:
                shear_capped_successes += 1
            if q_val > best_q:
                best_q = q_val
                best_trial = {
                    "trial_id": i,
                    "delta_T_base_K": delta_T_base,
                    "d_nozzle_um": d_nozzle * 1e6,
                    "pitch_um": pitch * 1e6,
                    "h_wall_um": h_wall * 1e6,
                    "d_artery_um": d_artery * 1e6,
                    "diodicity": diodicity,
                    **res,
                }

    elapsed = time.time() - t0
    print("=" * 72)
    print("AI Edison In Silico Sweep: EXP-20261125-010 (TAVJ-DL)")
    print("=" * 72)
    print(f"Total Trials: {num_trials} | Elapsed: {elapsed:.3f} s")
    print(f"Kutateladze-Zuber Baseline (1 atm water): {Q_CHF_KZ_W_M2 / 1e6:.3f} MW/m^2")
    print("-" * 72)
    for k, v in counts.items():
        pct = 100.0 * v / num_trials
        print(f"  {k:<26}: {v:>5} ({pct:5.2f}%)")
    if all_success_q:
        all_success_q.sort()
        median_q = all_success_q[len(all_success_q) // 2]
        print("-" * 72)
        print(f"Viable Regime Median CHF : {median_q:.2f} MW/m^2 ({median_q / (Q_CHF_KZ_W_M2 / 1e6):.2f}x KZ)")
        print(f"Shear-Capped Successes   : {shear_capped_successes} / {len(all_success_q)}")
        print("-" * 72)
        print(f"Top Champion (Trial #{best_trial['trial_id']}):")
        print(f"  Sustained CHF          : {best_trial['q_MW_m2']:.2f} MW/m^2 ({best_trial['enhancement']:.2f}x KZ)")
        print(f"  Base Superheat (dT_b)  : {best_trial['delta_T_base_K']:.2f} K")
        print(f"  Interface Superheat    : {best_trial['delta_T_int_K']:.2f} K")
        print(f"  Nozzle Diameter        : {best_trial['d_nozzle_um']:.1f} um")
        print(f"  Unit Cell Pitch        : {best_trial['pitch_um']:.1f} um")
        print(f"  Wall/Artery Height     : {best_trial['h_wall_um']:.1f} um")
        print(f"  Liquid Artery Diam     : {best_trial['d_artery_um']:.1f} um")
        print(f"  Tesla Diodicity        : {best_trial['diodicity']:.2f}")
        print(f"  Vapor Jet Velocity     : {best_trial['v_v_m_s']:.1f} m/s")
        print(f"  Jet Weber Number       : {best_trial['We_jet']:.2f}")
        print(f"  Heat Transfer Coeff    : {best_trial['htc_kW_m2K']:.1f} kW/(m^2*K)")
    print("=" * 72)


if __name__ == "__main__":
    run_simulation_sweep()
