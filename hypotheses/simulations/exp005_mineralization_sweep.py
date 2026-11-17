#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261117-005
Piezocatalytic Self-Mineralizing Concrete Composite for Autonomous Carbon Capture

Coupled Multi-Physics Solver:
1. Piezoelectric voltage generation from mechanical cyclic traffic stress
2. Electrochemical catalytic activation of dissolved ambient CO2 (Butler-Volmer)
3. CaCO3 precipitation kinetics and crack volume closure
4. Annual atmospheric carbon sequestration yield (kg CO2 / m^3 / year)
5. Compressive strength increase through crack healing

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
import sys
from typing import Dict, Any, List

# Physical & Chemical Constants
FARADAY_CONST = 96485.33        # C/mol
R_GAS = 8.314462               # J/(mol*K)
EPSILON_0 = 8.8541878e-12      # F/m
M_CO2 = 0.04401                # kg/mol
M_CACO3 = 0.10009              # kg/mol
RHO_CACO3 = 2710.0             # Density of calcite (kg/m^3)
OMEGA_CACO3 = 3.69e-5          # Molar volume of CaCO3 (m^3/mol)
V_THRESHOLD_CATALYSIS = 1.23   # Minimum potential for water-splitting / CO2 activation (V)


def evaluate_mineralization_trial(
    d33_pC_N: float,           # Piezoelectric coefficient (pC/N, 50 - 350)
    wire_length_um: float,     # Piezoelectric nanowire/chain length (um, 5 - 80)
    eps_r: float,              # Relative dielectric permittivity (80 - 400)
    phi_piezo_vol: float,      # Volume fraction of piezo dopant (0.01 - 0.10)
    sigma_traffic_MPa: float,  # Traffic cyclic stress amplitude (MPa, 2 - 25)
    f_traffic_Hz: float,       # Traffic frequency (Hz, 0.2 - 5.0)
    w_crack_init_um: float,    # Initial crack width to heal (um, 50 - 300)
    ca_conc_mol_L: float,      # Pore solution Ca2+ reserve concentration (mol/L, 0.01 - 0.10)
    co2_ppm: float,            # Ambient atmospheric CO2 level (ppm, 350 - 550)
    T_amb: float,              # Ambient temperature (K, 280 - 315)
) -> Dict[str, Any]:
    """
    Evaluates one continuous self-mineralization configuration.
    """
    d33 = d33_pC_N * 1e-12
    wire_length = wire_length_um * 1e-6
    sigma_stress = sigma_traffic_MPa * 1e6

    # 1. Piezocatalytic Voltage Generation
    # High-aspect-ratio nanowire / percolated chain: V = d33 * sigma * L / (eps_r * eps_0)
    eps_eff = eps_r * EPSILON_0
    V_piezo = (d33 * sigma_stress * wire_length) / eps_eff

    # Voltage must exceed catalytic overpotential threshold (~1.23 V)
    if V_piezo < V_THRESHOLD_CATALYSIS:
        return {
            "status": "FAIL_LOW_VOLTAGE",
            "reason": "Generated piezocatalytic voltage below electrochemical threshold (< 1.23 V)",
            "V_piezo": V_piezo,
        }

    # 2. Catalytic Hydration & Precipitation Rate
    # Butler-Volmer electrochemical acceleration
    overpotential = V_piezo - V_THRESHOLD_CATALYSIS
    alpha_transfer = 0.5
    f_activation = math.exp(min(12.0, (alpha_transfer * FARADAY_CONST * overpotential) / (R_GAS * T_amb)))

    # Dissolved CO2 equilibrium (Henry's law: k_H ~ 0.034 mol/(L*atm))
    P_co2_atm = (co2_ppm * 1e-6)
    c_co2_aq = 0.034 * P_co2_atm  # mol/L

    # Base reaction rate k0 ~ 1e-5 mol/(m^2*s)
    k0 = 1.2e-5
    # Specific surface area of nanowires per m^3 of composite (diameter ~ 100 nm)
    d_wire = 100e-9
    specific_area = (4.0 * phi_piezo_vol) / d_wire  # m^2/m^3

    # Electrochemical reaction rate (mol / (m^3 * s))
    r_reaction_kinetics = k0 * f_activation * (ca_conc_mol_L * 1000.0) * (c_co2_aq * 1000.0) * (specific_area * 1e-4) * (f_traffic_Hz / 2.0)

    # Physical Mass-Transfer Diffusion Limit (Fickian limit through porous matrix)
    # D_eff ~ 1e-8 to 5e-8 m^2/s for concrete
    D_eff_co2 = 2.5e-8
    diff_length = 0.02  # 2 cm penetration depth
    c_co2_gas = (co2_ppm * 1e-6) * (101325.0 / (R_GAS * T_amb))  # mol/m^3
    r_diffusion_ceiling = (D_eff_co2 * c_co2_gas / (diff_length ** 2))  # mol/(m^3 * s)

    # Actual rate is bounded by whichever is slower: kinetics or diffusion
    r_actual_vol = min(r_reaction_kinetics, r_diffusion_ceiling)

    # 3. Annual Carbon Sequestration Rate
    seconds_per_year = 3.1536e7
    annual_co2_kg_per_m3 = (r_actual_vol * M_CO2 * seconds_per_year)

    # 4. Crack Closure Rate
    w_crack_init_m = w_crack_init_um * 1e-6
    growth_rate_m_s = (r_actual_vol * OMEGA_CACO3) / 2.0
    
    t_heal_seconds = (w_crack_init_m / 2.0) / max(1e-15, growth_rate_m_s)
    t_heal_days = t_heal_seconds / 86400.0

    if t_heal_days > 90.0:
        return {
            "status": "FAIL_SLOW_HEALING",
            "reason": "Crack closure time exceeds 90 days",
            "t_heal_days": t_heal_days,
        }

    if annual_co2_kg_per_m3 < 1.0:
        return {
            "status": "FAIL_LOW_SEQUESTRATION",
            "reason": "Carbon capture rate below threshold (< 1.0 kg CO2/m^3/year)",
            "annual_kg": annual_co2_kg_per_m3,
        }

    # 5. Compressive Strength Gain
    strength_gain_pct = min(35.0, 5.0 + 1.2 * annual_co2_kg_per_m3)

    return {
        "status": "SUCCESS_MINERALIZATION",
        "V_piezo": V_piezo,
        "annual_co2_kg_m3": annual_co2_kg_per_m3,
        "t_heal_days": t_heal_days,
        "strength_gain_pct": strength_gain_pct,
        "sigma_traffic_MPa": sigma_traffic_MPa,
        "d33_pC_N": d33_pC_N,
    }


def run_10000_mineralization_sweep(num_trials: int = 10000) -> None:
    random.seed(42)
    start_time = time.time()

    success_list: List[Dict[str, Any]] = []
    failure_counts: Dict[str, int] = {}

    print("=" * 80)
    print("AI EDISON IN SILICO DISCOVERY ENGINE: EXP-20261117-005")
    print("Piezocatalytic Self-Mineralizing Concrete Composite")
    print(f"Beginning {num_trials:,} Virtual Multi-Physics Trials...")
    print("=" * 80)

    for i in range(num_trials):
        d33_pC_N = random.uniform(80.0, 350.0)
        wire_length_um = random.uniform(5.0, 80.0)
        eps_r = random.uniform(80.0, 350.0)
        phi_piezo_vol = random.uniform(0.01, 0.08)
        sigma_traffic_MPa = random.uniform(3.0, 25.0)
        f_traffic_Hz = random.uniform(0.5, 4.0)
        w_crack_init_um = random.uniform(50.0, 250.0)
        ca_conc_mol_L = random.uniform(0.02, 0.08)
        co2_ppm = random.uniform(380.0, 520.0)
        T_amb = random.uniform(283.0, 310.0)

        res = evaluate_mineralization_trial(
            d33_pC_N=d33_pC_N,
            wire_length_um=wire_length_um,
            eps_r=eps_r,
            phi_piezo_vol=phi_piezo_vol,
            sigma_traffic_MPa=sigma_traffic_MPa,
            f_traffic_Hz=f_traffic_Hz,
            w_crack_init_um=w_crack_init_um,
            ca_conc_mol_L=ca_conc_mol_L,
            co2_ppm=co2_ppm,
            T_amb=T_amb,
        )

        status = res["status"]
        if status == "SUCCESS_MINERALIZATION":
            res["trial_idx"] = i
            success_list.append(res)
        else:
            failure_counts[status] = failure_counts.get(status, 0) + 1

    elapsed = time.time() - start_time
    total_success = len(success_list)
    success_rate = (total_success / num_trials) * 100.0

    print(f"\nSimulation complete in {elapsed:.2f} seconds ({num_trials / elapsed:,.0f} trials/sec).")
    print(f"Total Trials: {num_trials:,}")
    print(f"Successful Self-Mineralizing Regimes: {total_success:,} ({success_rate:.2f}%)")
    print("\nFalsification / Failure Breakdown:")
    for mode, count in sorted(failure_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / num_trials) * 100.0
        print(f"  * {mode:32s}: {count:6,d} ({pct:5.1f}%)")

    sorted_by_carbon = sorted(success_list, key=lambda x: x["annual_co2_kg_m3"], reverse=True)
    best = sorted_by_carbon[0]

    print("\n" + "=" * 80)
    print("PARETO FRONTIER: CHAMPION CARBON-SEQUESTERING COMPOSITE (Trial #%d)" % best["trial_idx"])
    print("=" * 80)
    print("   * Annual CO2 Sequestration:      %.2f kg CO2 / m^3 / year" % best["annual_co2_kg_m3"])
    print("   * Piezocatalytic Voltage:        %.2f V (Overpotential: +%.2f V)" % (best["V_piezo"], best["V_piezo"] - 1.23))
    print("   * Crack Healing Duration:        %.1f days to seal crack" % best["t_heal_days"])
    print("   * Strength Increase:             +%.1f%% compressive gain" % best["strength_gain_pct"])
    print("   * Operating Traffic Stress:      %.1f MPa" % best["sigma_traffic_MPa"])
    print("   * Energy Consumed:               Zero (Passive Traffic-Driven)" )
    print("=" * 80)


if __name__ == "__main__":
    trials = 10000
    if len(sys.argv) > 1:
        try:
            trials = int(sys.argv[1])
        except ValueError:
            pass
    run_10000_mineralization_sweep(trials)
