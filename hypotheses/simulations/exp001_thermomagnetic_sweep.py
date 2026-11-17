#!/usr/bin/env python3
"""
AI Edison In Silico Simulation Sweep: EXP-20261117-001
Thermomagnetic Cantilever Oscillator for Ambient Micro-Gradient Harvesting

Coupled Magneto-Thermo-Mechanical State-Machine Model:
1. ATTRACTING: Cold alloy (T < Tc) attracted toward hot magnet.
2. HOT_DWELL: Contact with hot source; heat conducts into alloy until T >= Tc.
3. RELEASING: Magnetization drops; spring restoring force pulls cantilever away.
4. COLD_COOLING: Convective heat loss to ambient air until T < Tc, restoring magnetization.

Pure Python standard library (zero external dependencies).
"""

import math
import random
import time
import sys
from typing import Dict, Any, List

# Physical Constants
BETA_EXP = 0.36                   # Critical exponent for Curie magnetization drop
RHO_GD = 7900.0                  # Density of Gadolinium (kg/m^3)
CP_GD = 230.0                    # Specific heat capacity of Gadolinium (J/kg*K)
E_SPRING_STEEL = 205e9           # Young's modulus of spring steel (Pa)
M0_GD = 1.6e6                    # Saturation magnetization at 0K (A/m)


def simulate_oscillator_trial(
    L: float,           # Cantilever length (m)
    w: float,           # Cantilever width (m)
    t_substrate: float, # Spring substrate thickness (m)
    t_alloy: float,     # Active Curie alloy thickness (m)
    d_gap: float,       # Equilibrium magnetic gap distance (m)
    Tc: float,          # Curie temperature of alloy (K)
    T_hot: float,       # Heat source temperature (K)
    T_sink: float,      # Ambient sink temp (K)
    h_contact: float,   # Contact thermal conductance at hot magnet (W/m^2*K)
    h_conv: float,      # Convective cooling coefficient in air (W/m^2*K)
    B_rem: float,       # Remanent flux density of permanent magnet (Tesla)
    dt: float = 0.001,  # Time step (s)
    sim_time: float = 5.0  # Total simulation time (s)
) -> Dict[str, Any]:
    """
    Simulates coupled physical dynamics using dynamic state machine.
    """
    t_total = t_substrate + t_alloy
    vol_alloy = L * w * t_alloy
    m_alloy = vol_alloy * RHO_GD
    m_substrate = L * w * t_substrate * 7850.0
    total_mass = m_alloy + m_substrate
    effective_mass = 0.24 * total_mass

    # Euler-Bernoulli beam stiffness
    k = (E_SPRING_STEEL * w * (t_total ** 3)) / (4.0 * (L ** 3))

    area_contact = w * (0.20 * L)  # Contact tip area
    area_conv = 2.0 * L * w

    c_damping = 2.0 * 0.08 * math.sqrt(k * effective_mass)

    # Initial state: cold resting at neutral
    x = 0.0
    v = 0.0
    T = T_sink
    state = "ATTRACTING"

    steps = int(sim_time / dt)
    cycles_completed = 0
    stuck_time = 0.0
    R_pole = 0.003

    for step in range(steps):
        # 1. Magnetization calculation
        if T < Tc:
            m_ratio = max(0.0, 1.0 - (T / Tc))
            M_T = M0_GD * math.pow(m_ratio, BETA_EXP)
        else:
            M_T = 0.0

        current_gap = max(1e-5, d_gap - x)
        B_local = B_rem / ((1.0 + (current_gap / R_pole)) ** 2)
        grad_B = (2.0 * B_local) / (R_pole + current_gap)

        # SI Kelvin body force: F = M * grad(B) * V (in Newtons)
        F_mag = M_T * grad_B * vol_alloy
        F_spring = -k * x
        F_damp = -c_damping * v

        # State transitions and dynamics
        if state == "ATTRACTING":
            F_net = F_spring + F_damp + F_mag
            a = F_net / effective_mass
            v += a * dt
            x += v * dt
            q_out = h_conv * area_conv * (T - T_sink)
            T -= (q_out * dt) / (m_alloy * CP_GD)

            if x >= d_gap:
                x = d_gap
                v = 0.0
                state = "HOT_DWELL"

        elif state == "HOT_DWELL":
            q_in = h_contact * area_contact * (T_hot - T)
            q_out = h_conv * area_conv * (T - T_sink)
            dT_dt = (q_in - q_out) / (m_alloy * CP_GD)
            T += dT_dt * dt

            # Alloy demagnetizes as T approaches and crosses Tc
            restoring_force = k * d_gap
            if F_mag < restoring_force or T >= Tc:
                state = "RELEASING"
                v = -0.05
            else:
                x = d_gap
                v = 0.0
                stuck_time += dt

        elif state == "RELEASING":
            F_net = F_spring + F_damp + F_mag
            a = F_net / effective_mass
            v += a * dt
            x += v * dt
            q_out = h_conv * area_conv * (T - T_sink)
            T -= (q_out * dt) / (m_alloy * CP_GD)

            if x <= 0.0:
                state = "COLD_COOLING"

        elif state == "COLD_COOLING":
            F_net = F_spring + F_damp + F_mag
            a = F_net / effective_mass
            v += a * dt
            x += v * dt
            q_out = h_conv * area_conv * (T - T_sink)
            T -= (q_out * dt) / (m_alloy * CP_GD)

            if x < -d_gap:
                x = -d_gap
                v = -0.2 * v

            if T < (Tc - 0.15) and F_mag > abs(F_spring):
                state = "ATTRACTING"
                cycles_completed += 1

    freq_hz = cycles_completed / sim_time
    is_stuck = (stuck_time >= 0.7 * sim_time)
    is_damped = (freq_hz < 0.2) and not is_stuck
    is_oscillating = (freq_hz >= 0.2) and not is_stuck

    # Work per thermal cycle = 0.5 * k * d_gap^2 * frequency
    work_per_cycle = 0.5 * k * (d_gap ** 2)
    power_watts = work_per_cycle * freq_hz
    total_vol_cm3 = (vol_alloy + (L * w * t_substrate)) * 1e6
    power_density_uW_cm3 = (power_watts * 1e6) / total_vol_cm3 if total_vol_cm3 > 0 else 0.0

    delta_T = T_hot - T_sink
    carnot_pct = (delta_T / max(T_hot, 1.0)) * 100.0

    return {
        "oscillating": is_oscillating,
        "stuck": is_stuck,
        "damped": is_damped,
        "frequency_hz": round(freq_hz, 3),
        "power_density_uW_cm3": round(power_density_uW_cm3, 3),
        "delta_T": round(delta_T, 2),
        "carnot_pct": round(carnot_pct, 3),
        "stiffness_N_m": round(k, 3)
    }


def run_high_throughput_sweep(total_trials: int = 10000) -> None:
    print("=" * 74)
    print("AI EDISON HIGH-THROUGHPUT IN SILICO SWEEP: EXP-20261117-001")
    print("Coupled Magneto-Thermo-Mechanical State-Machine Solver")
    print(f"Target: {total_trials:,} Trials | Micro-Gradient Window: 1.0K - 4.5K")
    print("=" * 74)

    start_time = time.time()
    valid_oscillations: List[Dict[str, Any]] = []
    stuck_failures = 0
    damped_failures = 0

    random.seed(20261117)

    for trial_idx in range(total_trials):
        # Sample parameter boundaries
        L = random.uniform(0.015, 0.035)              # 15mm - 35mm
        w = random.uniform(0.002, 0.005)              # 2mm - 5mm
        t_sub = random.uniform(0.00002, 0.00006)      # 20um - 60um spring steel
        t_alloy = random.uniform(0.00002, 0.00006)    # 20um - 60um thin alloy foil
        d_gap = random.uniform(0.0006, 0.0018)        # 0.6mm - 1.8mm gap
        delta_T = random.uniform(1.2, 4.0)            # 1.2K - 4.0K gradient
        T_sink = 293.15                               # 20 deg C ambient
        T_hot = T_sink + delta_T
        # Tc dynamically tuned to operating gradient regime
        Tc = T_sink + random.uniform(0.35, 0.65) * delta_T
        h_contact = random.uniform(5000.0, 15000.0)   # Micro-contact thermal conductance
        h_conv = random.uniform(40.0, 95.0)           # Convective air draft
        B_rem = random.uniform(0.8, 1.2)              # Neodymium magnet

        res = simulate_oscillator_trial(
            L=L, w=w, t_substrate=t_sub, t_alloy=t_alloy, d_gap=d_gap,
            Tc=Tc, T_hot=T_hot, T_sink=T_sink, h_contact=h_contact,
            h_conv=h_conv, B_rem=B_rem, dt=0.001, sim_time=5.0
        )

        if res["oscillating"]:
            res["trial_id"] = trial_idx + 1
            res["params"] = {
                "L_mm": round(L * 1000, 1),
                "w_mm": round(w * 1000, 1),
                "t_alloy_um": round(t_alloy * 1e6, 0),
                "t_sub_um": round(t_sub * 1e6, 0),
                "d_gap_mm": round(d_gap * 1000, 2),
                "k_Npm": res["stiffness_N_m"],
                "delta_T_K": res["delta_T"]
            }
            valid_oscillations.append(res)
        elif res["stuck"]:
            stuck_failures += 1
        else:
            damped_failures += 1

        if (trial_idx + 1) % 2500 == 0:
            elapsed = time.time() - start_time
            print(f"Progress: {trial_idx + 1:,} / {total_trials:,} trials completed ({elapsed:.1f}s)")

    total_time = time.time() - start_time
    success_rate = (len(valid_oscillations) / total_trials) * 100.0

    print("\n" + "=" * 74)
    print("IN SILICO SWEEP SUMMARY")
    print("=" * 74)
    print(f"Total Virtual Trials Executed: {total_trials:,}")
    print(f"Computation Time:             {total_time:.2f} seconds ({total_trials/total_time:.0f} trials/sec)")
    print(f"Sustained Limit-Cycle Winners: {len(valid_oscillations)} ({success_rate:.2f}%)")
    print(f"Falsified - Magnetic Lockup:   {stuck_failures} ({(stuck_failures/total_trials)*100:.1f}%)")
    print(f"Falsified - Damped / Insuff.:  {damped_failures} ({(damped_failures/total_trials)*100:.1f}%)")

    if valid_oscillations:
        valid_oscillations.sort(key=lambda x: x["power_density_uW_cm3"], reverse=True)
        top_candidates = valid_oscillations[:5]

        print("\n" + "-" * 74)
        print("TOP 5 PARETO CANDIDATES (SURVIVED COMPUTATIONAL FALSIFICATION)")
        print("-" * 74)
        for rank, cand in enumerate(top_candidates, 1):
            p = cand["params"]
            print(f"Rank #{rank} [Trial #{cand['trial_id']}]:")
            print(f"  Power Density:  {cand['power_density_uW_cm3']} uW/cm^3")
            print(f"  Oscillation f:  {cand['frequency_hz']} Hz")
            print(f"  Operating dT:   {cand['delta_T']} K (Carnot Bound: {cand['carnot_pct']}%)")
            print(f"  Beam Geometry:  L={p['L_mm']}mm, w={p['w_mm']}mm, t_alloy={p['t_alloy_um']}um, t_sub={p['t_sub_um']}um")
            print(f"  Spring/Gap:     k={p['k_Npm']} N/m, gap={p['d_gap_mm']}mm")
            print()
    else:
        print("\nNo candidate met all sustained oscillation criteria under this parameter bounds.")


if __name__ == "__main__":
    trials = 10000
    if len(sys.argv) > 1:
        try:
            trials = int(sys.argv[1])
        except ValueError:
            pass
    run_high_throughput_sweep(total_trials=trials)
