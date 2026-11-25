#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261125-011
Sub-Wavelength Monolithic Acoustic-Mechanical Impedance Transformer (AMIT)

Coupled Electro-Mechano-Acoustic Circuit Solver:
1. Transforms airborne acoustic impedance (Z_a = 415 Rayl) to water (Z_w = 1.48 MRayl)
   via coupled area ratio (A_a / A_w) and monolithic flexural lever ratio (Gamma).
2. Accounts for reflected air-diaphragm mass (Gamma^2 * m_a), water piston mass (m_w),
   flexural hinge stiffness (k_w), and internal structural/viscous damping (eta_loss).
3. Evaluates broadband power transmission T(f) from 2 kHz to 30 kHz against the
   classical bare water-air transmission floor (T_bare = 0.00112, or 0.112%).

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
from typing import Dict, Any, List


# Physical constants [established]
Z_WATER_RAYL = 1.48e6       # Specific acoustic impedance of water (Pa*s/m)
Z_AIR_RAYL = 415.0          # Specific acoustic impedance of air (Pa*s/m)
T_BARE_WATER_AIR = (4.0 * Z_WATER_RAYL * Z_AIR_RAYL) / ((Z_WATER_RAYL + Z_AIR_RAYL) ** 2)
RHO_SI3N4 = 3100.0          # Silicon nitride / SiC diaphragm density (kg/m^3)
RHO_TI = 4500.0             # Titanium piston/lever density (kg/m^3)


def evaluate_amit_trial(
    r_water_m: float,       # Water-side piston radius (m, 40e-6 - 160e-6)
    pitch_m: float,         # Unit cell pitch (m, 0.8e-3 - 2.5e-3)
    gamma_lever: float,     # Flexural lever velocity ratio v_a / v_w (3.0 - 14.0)
    t_diaph_m: float,       # Air-side membrane thickness (m, 1.0e-6 - 8.0e-6)
    f_res_Hz: float,        # Tuned mechanical natural frequency (Hz, 4000 - 20000)
    loss_factor: float,     # Structural + hinge loss factor (0.02 - 0.12)
) -> Dict[str, Any]:
    """
    Evaluates broadband (2 kHz to 30 kHz) acoustic power transmission across a
    water-air interface using a monolithic area-lever impedance transformer.
    """
    A_cell = pitch_m * pitch_m
    A_w = math.pi * r_water_m * r_water_m
    # Air-side diaphragm occupies 82% of unit cell area
    A_a = 0.82 * A_cell

    # Geometric validity: water piston must be much smaller than cell
    if A_w >= 0.15 * A_cell:
        return {"status": "FAIL_GEOMETRY", "T_band_avg": 0.0}

    # Effective masses referred to the water-side piston
    m_a = RHO_SI3N4 * A_a * t_diaph_m
    # Water piston + lever arm + radiation-added water mass (8/3 * rho_w * r_w^3)
    m_w = RHO_TI * A_w * 150e-6 + (8.0 / 3.0) * 1000.0 * (r_water_m ** 3)
    m_eff_w = m_w + (gamma_lever ** 2) * m_a

    # Tuned hinge stiffness referred to water piston: k_w = (2*pi*f_res)^2 * m_eff_w
    omega_res = 2.0 * math.pi * f_res_Hz
    k_w = (omega_res ** 2) * m_eff_w

    # Transformed radiation resistance into air (referred to water piston)
    R_rad_w = Z_AIR_RAYL * A_a * (gamma_lever ** 2)
    # Internal structural + viscous damping resistance
    R_loss_w = loss_factor * omega_res * m_eff_w

    # Sweep frequency band from 2 kHz to 30 kHz (15 log-spaced points)
    freqs = [2000.0 * ((30000.0 / 2000.0) ** (i / 14.0)) for i in range(15)]
    T_vals: List[float] = []
    T_peak = 0.0
    f_peak = f_res_Hz

    for f in freqs:
        omega = 2.0 * math.pi * f
        Z_real = (R_rad_w + R_loss_w) / A_w
        Z_imag = (omega * m_eff_w - k_w / omega) / A_w
        Z_rad_spec = R_rad_w / A_w

        denom = (Z_WATER_RAYL + Z_real) ** 2 + (Z_imag ** 2)
        T_f = (4.0 * Z_WATER_RAYL * Z_rad_spec) / denom
        T_vals.append(T_f)
        if T_f > T_peak:
            T_peak = T_f
            f_peak = f

    T_band_avg = sum(T_vals) / len(T_vals)
    # Fractional bandwidth where T(f) >= 0.25 (25% transmission, >220x bare water-air)
    pass_count = sum(1 for t in T_vals if t >= 0.25)
    bandwidth_frac = pass_count / len(T_vals)

    enhancement_avg = T_band_avg / T_BARE_WATER_AIR
    enhancement_peak = T_peak / T_BARE_WATER_AIR
    Z_matched_ratio = (R_rad_w / A_w) / Z_WATER_RAYL

    # Falsification / viability gates:
    # 1. Band-averaged transmission T_band_avg >= 0.35 (35%, >310x bare water-air)
    # 2. Peak transmission T_peak >= 0.65 (65%)
    # 3. Passband coverage >= 40% of the 2-30 kHz decade
    if T_peak < 0.65:
        return {
            "status": "FAIL_LOW_PEAK",
            "T_band_avg": T_band_avg,
            "T_peak": T_peak,
            "enhancement_avg": enhancement_avg,
        }
    if T_band_avg < 0.35 or bandwidth_frac < 0.40:
        return {
            "status": "FAIL_NARROWBAND",
            "T_band_avg": T_band_avg,
            "T_peak": T_peak,
            "bandwidth_frac": bandwidth_frac,
            "enhancement_avg": enhancement_avg,
        }

    return {
        "status": "SUCCESS_BROADBAND_MATCH",
        "T_band_avg": T_band_avg,
        "T_peak": T_peak,
        "f_peak_Hz": f_peak,
        "bandwidth_frac": bandwidth_frac,
        "enhancement_avg": enhancement_avg,
        "enhancement_peak": enhancement_peak,
        "Z_matched_ratio": Z_matched_ratio,
        "area_ratio": A_a / A_w,
    }


def run_simulation_sweep(num_trials: int = 10000, seed: int = 20261125) -> None:
    rng = random.Random(seed)
    t0 = time.time()

    counts = {
        "SUCCESS_BROADBAND_MATCH": 0,
        "FAIL_LOW_PEAK": 0,
        "FAIL_NARROWBAND": 0,
        "FAIL_GEOMETRY": 0,
    }

    best_trial: Dict[str, Any] = {}
    best_T_avg = 0.0
    all_success_T: List[float] = []

    for i in range(1, num_trials + 1):
        r_water = rng.uniform(40e-6, 160e-6)
        pitch = rng.uniform(0.8e-3, 2.5e-3)
        gamma_lever = rng.uniform(3.0, 14.0)
        t_diaph = rng.uniform(1.0e-6, 8.0e-6)
        f_res = rng.uniform(4000.0, 20000.0)
        loss_factor = rng.uniform(0.02, 0.12)

        res = evaluate_amit_trial(
            r_water, pitch, gamma_lever, t_diaph, f_res, loss_factor
        )
        status = res["status"]
        counts[status] += 1

        if status == "SUCCESS_BROADBAND_MATCH":
            t_avg = res["T_band_avg"]
            all_success_T.append(t_avg)
            if t_avg > best_T_avg:
                best_T_avg = t_avg
                best_trial = {
                    "trial_id": i,
                    "r_water_um": r_water * 1e6,
                    "pitch_mm": pitch * 1e3,
                    "gamma_lever": gamma_lever,
                    "t_diaph_um": t_diaph * 1e6,
                    "f_res_Hz": f_res,
                    "loss_factor": loss_factor,
                    **res,
                }

    elapsed = time.time() - t0
    print("=" * 72)
    print("AI Edison In Silico Sweep: EXP-20261125-011 (AMIT)")
    print("=" * 72)
    print(f"Total Trials: {num_trials} | Elapsed: {elapsed:.3f} s")
    print(f"Bare Water-Air Transmission: {T_BARE_WATER_AIR * 100:.3f}% (-29.5 dB)")
    print("-" * 72)
    for k, v in counts.items():
        pct = 100.0 * v / num_trials
        print(f"  {k:<26}: {v:>5} ({pct:5.2f}%)")
    if all_success_T:
        all_success_T.sort()
        median_T = all_success_T[len(all_success_T) // 2]
        print("-" * 72)
        print(f"Viable Regime Median T_avg: {median_T * 100:.2f}% ({median_T / T_BARE_WATER_AIR:.1f}x bare)")
        print("-" * 72)
        print(f"Top Champion (Trial #{best_trial['trial_id']}):")
        print(f"  2-30 kHz Avg Transmission: {best_trial['T_band_avg'] * 100:.2f}% ({best_trial['enhancement_avg']:.1f}x bare)")
        print(f"  Peak Transmission        : {best_trial['T_peak'] * 100:.2f}% ({best_trial['enhancement_peak']:.1f}x bare) at {best_trial['f_peak_Hz']:.0f} Hz")
        print(f"  Passband Coverage (>25%) : {best_trial['bandwidth_frac'] * 100:.1f}% of 2-30 kHz")
        print(f"  Water Piston Radius      : {best_trial['r_water_um']:.1f} um")
        print(f"  Unit Cell Pitch          : {best_trial['pitch_mm']:.2f} mm")
        print(f"  Area Ratio (A_a / A_w)   : {best_trial['area_ratio']:.1f}x")
        print(f"  Flexural Lever Ratio     : {best_trial['gamma_lever']:.2f}x")
        print(f"  Diaphragm Thickness      : {best_trial['t_diaph_um']:.2f} um")
        print(f"  Tuned Natural Freq       : {best_trial['f_res_Hz']:.0f} Hz")
        print(f"  Impedance Match (Z/Z_w)  : {best_trial['Z_matched_ratio']:.2f}")
    print("=" * 72)


if __name__ == "__main__":
    run_simulation_sweep()
