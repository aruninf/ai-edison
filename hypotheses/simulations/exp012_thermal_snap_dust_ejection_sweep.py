#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261125-012
Passive Diurnal-Thermal Snap-Anvil Dust-Ejection Lattice (DTSA-DL)

Coupled Thermo-Elastic-Impact Solver:
1. Diurnal temperature swing (Delta T) builds mismatch strain in an optically
   transparent bilayer micro-dome (SiO2 / CaF2 or Al2O3 / MgF2).
2. Saddle-node bistable snap-through converts stored elastic energy into kinetic
   velocity v_snap.
3. Rigid micro-anvil end-stop converts v_snap into sub-micron impact deceleration
   a_peak = v_snap^2 / (2 * dx_stop).
4. Compares a_peak against van der Waals adhesion acceleration a_detach(d_p) for
   5.0 um and 10.0 um silicate dust particles, while enforcing fatigue-safe
   peak bending stress (sigma_max <= 350 MPa).

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
from typing import Dict, Any, List


# Physical constants [established]
A_HAMAKER_J = 6.5e-20       # Silicate-on-silica Hamaker constant in air/vacuum (J)
Z0_CONTACT_M = 0.40e-9      # Effective rough-contact separation (m)
RHO_DUST_KG_M3 = 2650.0     # Silicate/regolith particle density (kg/m^3)
E_EFF_PA = 75.0e9           # Effective biaxial modulus of SiO2/CaF2 bilayer (Pa)
RHO_DOME_KG_M3 = 2600.0     # Bilayer average density (kg/m^3)
SIGMA_FATIGUE_PA = 350.0e6  # Safe cyclic tensile stress limit (Pa)
G_EARTH = 9.81


def adhesion_accel_m_s2(d_p_m: float) -> float:
    """
    Returns required detachment acceleration (m/s^2) to overcome van der Waals
    adhesion for a spherical silicate grain of diameter d_p_m.
    F_vdW = A_H * R / (6 * z0^2); m_p = (4/3)*pi*R^3*rho_p
    """
    return A_HAMAKER_J / (4.0 * math.pi * (Z0_CONTACT_M ** 2) * RHO_DUST_KG_M3 * (d_p_m ** 2))


def evaluate_dtsa_trial(
    delta_T_K: float,        # Diurnal temperature swing (K, 15 - 100)
    delta_alpha_K: float,    # Bilayer CTE mismatch (1/K, 10e-6 - 24e-6)
    t_dome_m: float,         # Bilayer dome thickness (m, 15e-6 - 80e-6)
    r_dome_m: float,         # Dome radius (m, 0.5e-3 - 3.0e-3)
    eta_snap: float,         # Snap kinetic energy conversion efficiency (0.15 - 0.45)
    dx_stop_m: float,        # Anvil-stop deceleration distance (m, 0.25e-6 - 1.5e-6)
) -> Dict[str, Any]:
    """
    Evaluates one transparent diurnal-thermal snap-anvil cell.
    """
    # 1. Thermal mismatch strain and stored elastic energy per unit area (J/m^2)
    eps_th = delta_alpha_K * delta_T_K
    # Peak membrane/bending stress during snap
    sigma_peak_Pa = E_EFF_PA * eps_th * (1.0 + 0.35 * (t_dome_m / r_dome_m) * 20.0)

    if sigma_peak_Pa > SIGMA_FATIGUE_PA:
        return {
            "status": "FAIL_FRACTURE_STRESS",
            "sigma_MPa": sigma_peak_Pa / 1e6,
            "a_peak_g": 0.0,
        }

    # Stored elastic energy per unit area (J/m^2)
    u_stored_J_m2 = 0.5 * E_EFF_PA * (eps_th ** 2) * t_dome_m

    # 2. Snap velocity (m/s)
    m_areal_kg_m2 = RHO_DOME_KG_M3 * t_dome_m
    v_snap_m_s = math.sqrt((2.0 * eta_snap * u_stored_J_m2) / m_areal_kg_m2)

    # 3. Impact acceleration at rigid micro-anvil end-stop (m/s^2 and g)
    a_peak_m_s2 = (v_snap_m_s ** 2) / (2.0 * dx_stop_m)
    a_peak_g = a_peak_m_s2 / G_EARTH

    # 4. Minimum detachable particle diameter (m)
    # a_peak = A_H / (4*pi*z0^2*rho_p*d_min^2) => d_min = sqrt(...)
    d_min_m = math.sqrt(
        A_HAMAKER_J / (4.0 * math.pi * (Z0_CONTACT_M ** 2) * RHO_DUST_KG_M3 * a_peak_m_s2)
    )
    d_min_um = d_min_m * 1e6

    a_req_5um = adhesion_accel_m_s2(5.0e-6)
    a_req_10um = adhesion_accel_m_s2(10.0e-6)

    if a_peak_m_s2 < a_req_10um:
        return {
            "status": "FAIL_WEAK_IMPULSE",
            "a_peak_g": a_peak_g,
            "d_min_um": d_min_um,
        }
    if a_peak_m_s2 < a_req_5um:
        return {
            "status": "PARTIAL_10UM_ONLY",
            "a_peak_g": a_peak_g,
            "d_min_um": d_min_um,
        }

    return {
        "status": "SUCCESS_5UM_EJECTION",
        "a_peak_g": a_peak_g,
        "v_snap_m_s": v_snap_m_s,
        "d_min_um": d_min_um,
        "sigma_MPa": sigma_peak_Pa / 1e6,
        "u_stored_J_m2": u_stored_J_m2,
    }


def run_simulation_sweep(num_trials: int = 10000, seed: int = 20261125) -> None:
    rng = random.Random(seed)
    t0 = time.time()

    counts = {
        "SUCCESS_5UM_EJECTION": 0,
        "PARTIAL_10UM_ONLY": 0,
        "FAIL_WEAK_IMPULSE": 0,
        "FAIL_FRACTURE_STRESS": 0,
    }

    best_trial: Dict[str, Any] = {}
    best_a_g = 0.0
    all_success_g: List[float] = []

    for i in range(1, num_trials + 1):
        delta_T = rng.uniform(15.0, 100.0)
        delta_alpha = rng.uniform(10.0e-6, 24.0e-6)
        t_dome = rng.uniform(15.0e-6, 80.0e-6)
        r_dome = rng.uniform(0.5e-3, 3.0e-3)
        eta_snap = rng.uniform(0.15, 0.45)
        dx_stop = rng.uniform(0.25e-6, 1.5e-6)

        res = evaluate_dtsa_trial(
            delta_T, delta_alpha, t_dome, r_dome, eta_snap, dx_stop
        )
        status = res["status"]
        counts[status] += 1

        if status == "SUCCESS_5UM_EJECTION":
            ag = res["a_peak_g"]
            all_success_g.append(ag)
            if ag > best_a_g:
                best_a_g = ag
                best_trial = {
                    "trial_id": i,
                    "delta_T_K": delta_T,
                    "delta_alpha_ppm": delta_alpha * 1e6,
                    "t_dome_um": t_dome * 1e6,
                    "r_dome_mm": r_dome * 1e3,
                    "eta_snap": eta_snap,
                    "dx_stop_um": dx_stop * 1e6,
                    **res,
                }

    elapsed = time.time() - t0
    a_5um_g = adhesion_accel_m_s2(5.0e-6) / G_EARTH
    a_10um_g = adhesion_accel_m_s2(10.0e-6) / G_EARTH
    print("=" * 72)
    print("AI Edison In Silico Sweep: EXP-20261125-012 (DTSA-DL)")
    print("=" * 72)
    print(f"Total Trials: {num_trials} | Elapsed: {elapsed:.3f} s")
    print(f"Adhesion Thresholds: 10 um = {a_10um_g:,.0f} g | 5 um = {a_5um_g:,.0f} g")
    print("-" * 72)
    for k, v in counts.items():
        pct = 100.0 * v / num_trials
        print(f"  {k:<24}: {v:>5} ({pct:5.2f}%)")
    if all_success_g:
        all_success_g.sort()
        median_g = all_success_g[len(all_success_g) // 2]
        print("-" * 72)
        print(f"Viable Regime Median Accel: {median_g:,.0f} g")
        print("-" * 72)
        print(f"Top Champion (Trial #{best_trial['trial_id']}):")
        print(f"  Peak Impact Accel       : {best_trial['a_peak_g']:,.0f} g")
        print(f"  Min Detachable Dust     : {best_trial['d_min_um']:.2f} um")
        print(f"  Snap Velocity (v_snap)  : {best_trial['v_snap_m_s']:.2f} m/s")
        print(f"  Peak Bending Stress     : {best_trial['sigma_MPa']:.1f} MPa (< 350 MPa limit)")
        print(f"  Diurnal Swing (dT)      : {best_trial['delta_T_K']:.1f} K")
        print(f"  CTE Mismatch (d_alpha)  : {best_trial['delta_alpha_ppm']:.1f} ppm/K")
        print(f"  Dome Thickness / Radius : {best_trial['t_dome_um']:.1f} um / {best_trial['r_dome_mm']:.2f} mm")
        print(f"  Anvil Stop Distance     : {best_trial['dx_stop_um']:.2f} um")
    print("=" * 72)


if __name__ == "__main__":
    run_simulation_sweep()
