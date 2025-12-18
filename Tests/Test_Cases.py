#import functions for running the simulation 
import numpy as np
import os
os.makedirs("results", exist_ok=True)
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parents[1] / "results"   # .../CNM_2025_group_15/results
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

import matplotlib.pyplot as plt
from Spatial_Temporal_Grid import model_spatial_grid, model_time_grid
from Initial_Conditions import generate_initial_conditions
from Upstream_Advection import upstream_step
from Boundary_Conditions import apply_boundary_conditions
from Timestep import run_one_timestep
from Spacetime_Plot import plot_spacetime
from Plotting_Functions import function_snapshot

#using plot_snapshots to create consistent plots without repeating lots of code
def plot_snapshots(results, x, dt, title):
    nt = results.shape[0]
    times_seconds = [0, 50, 100, 150]
    times = [int(ts / dt) for ts in times_seconds]

    plt.figure(figsize=(8,4))
    for ti in times:
        plt.plot(x, results[ti], label=f"t{ti*dt:.0f}s")

    plt.title(title)
    plt.xlabel("Distance (m)")
    plt.ylabel("Concentration (µg/m^3)")
    plt.grid(True)   
    plt.legend()
    plt.tight_layout()
    plt.show()

#to avoid repeating time loops
def run_simulation(theta0, u, x, t, BC="zero_gradient", fixed_value=None, tau=None):
    dx = x[1] - x[0]   
    dt_out = t[1] - t[0]
    nt = len(t)

    # compute internal timestep
    umax = np.max(np.abs(u)) if not np.isscalar(u) else abs(u)
    dt_int = 0.8 * dx / umax
    nsub = int(np.ceil(dt_out / dt_int))
    dt_int = dt_out / nsub
    
    results = np.zeros((nt, len(x)))
    results[0] = theta0.copy()
    theta = theta0.copy()
    
    for n in range(1, nt):
        for _ in range(nsub):
            theta, _ = upstream_step(theta, u, dx, dt_int)
            theta = apply_boundary_conditions(theta, BC, fixed_value=fixed_value)

            if tau is not None:
              theta *= np.exp(-dt_int / tau)

        results[n] = theta.copy()
        
    return results

def run_test_case(test_case: int, L=20.0, dx=0.2, T=300.0, dt=10.0):

  #default grid for all test cases
  x, _ = model_spatial_grid(L, dx)
  t, ti = model_time_grid(T, dt)
  dt_plot = t[1] - t[0]

  if test_case == 1:
      theta0 = np.zeros_like(x)
      theta0[0] = 250
      
      C1 = run_simulation(
          theta0,
          u=0.1,
          x=x,
          t=t,
          BC="inflow",
          fixed_value=250
      )

      plot_spacetime(x, t, C1, output_dir=str(RESULTS_DIR), filename="tc1_spacetime.png", show=False)
      snapshot_times = [0, t[len(t)//3], t[2*len(t)//3], t[-1]]
      function_snapshot(x, C1, t, snapshot_times, save_dir=str(RESULTS_DIR))
      plot_snapshots(C1, x, dt=dt_plot, title="Test Case 1: Delta Initial Condition")      

      return

#test case two
  if test_case == 2:
      theta0_csv = generate_initial_conditions(
            x_grid=x,
            mode="csv",
            file="/content/CNM_2025_group_15/Data/initial_conditions.csv"
      )
      C2 = run_simulation(theta0_csv, u=0.1, x=x, t=t, BC="inflow", fixed_value=0.0)
      plot_spacetime(x, t, C2, output_dir=str(RESULTS_DIR), filename="tc2_spacetime.png", show=False)
      snapshot_times = [0, t[len(t)//3], t[2*len(t)//3], t[-1]]
      function_snapshot(x, C2, t, snapshot_times, save_dir=str(RESULTS_DIR))
      plot_snapshots(C2, x, dt=dt_plot, title="Test Case 2: CSV Initial Condition")
      return

#test case three
  if test_case == 3:
      u_values = [0.05, 0.1, 0.2]
      dx_values = [0.1, 0.2]
      dt_values = [0.5, 1.0]
      
      fig, axs = plt.subplots(len(u_values), len(dx_values), figsize=(10,8), sharex=True, sharey=True)
      
      for i, u_val in enumerate(u_values):
          for j, dx_val in enumerate(dx_values):
              x_test, _ = model_spatial_grid(20, dx_val)
          
              for dt_val in dt_values:
                  t_test, _ = model_time_grid(300, dt_val)
                  theta0 = np.zeros_like(x_test)
                  theta0[0] = 250

                  C = run_simulation(theta0, u_val, x_test, t_test)
                  axs[i, j].plot(x_test, C[-1], label=f"dt={dt_val}")
              axs[i, j].set_title(f"u={u_val}, dx={dx_val}")
              axs[i, j].grid(True)

      plt.legend()
      plt.suptitle("Test Case 3: Sensitivity Analysis")
      plt.tight_layout()
      plt.show()
      plt.close()
      return

#test case 4
  if test_case == 4:
      theta0 = np.zeros_like(x)
      theta0[0] = 250

      tau = 100

      C4 = run_simulation(theta0, u=0.1, x=x, t=t, BC="inflow", fixed_value=250, tau=tau)
      plot_spacetime(x, t, C4, output_dir=str(RESULTS_DIR), filename=f"tc4_spacetime.png", show=False)
      snapshot_times = [0, t[len(t)//3], t[2*len(t)//3], t[-1]]
      function_snapshot(x, C4, t, snapshot_times, save_dir=str(RESULTS_DIR))
      plot_snapshots(C4, x, dt=dt_plot, title="Test Case 4: Exponential Decay")
      return

#test case 5
  if test_case == 5:
      theta0 = np.zeros_like(x)
      theta0[0] = 250

      rng = np.random.default_rng(123)
      u_pert = 0.1 * (1 + 0.1 * rng.standard_normal(len(x)))

      C5 = run_simulation(theta0, u_pert, x=x, t=t)
      plot_spacetime(x, t, C5, output_dir=str(RESULTS_DIR), filename=f"tc5_spacetime.png", show=False)
      snapshot_times = [0, t[len(t)//3], t[2*len(t)//3], t[-1]]
      function_snapshot(x, C5, t, snapshot_times, save_dir=str(RESULTS_DIR))
      plot_snapshots(C5, x, dt=dt_plot, title="Test Case 5: Perturbed Velocity")
      return

def run_all_tests():
    for tc in [1, 2, 3, 4, 5]:
        run_test_case(tc)

if __name__ == "__main__":
  run_all_tests()
