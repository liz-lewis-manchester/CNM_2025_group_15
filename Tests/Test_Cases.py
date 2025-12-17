#import functions for spatial grid, time grid, upstream step, boundary conditions, load and interpolate initial conditions 
import matplotlib.pyplot as plt
from src.solver_functions import model_spatial_grid, model_time_grid, upstream_step, apply_boundary_conditions, generate_intial_conditions 

#using plot_snapshots to create consistent plots without repeating lots of code
def plot_snapshots(results, x, dt, title):
    nt = results.shape[0]
    times = [0, nt//3, 2*nt//3, nt-1] #choosing times at 1/3 intervals

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
def run_simulation(theta0, u, x, t, BC="zero_gradient"):
    dx = x[1] - x[0]   
    dt = t[1] - t[0]
    nt = len(t)

    results = np.zeros((nt, len(x)))
    results[0] = theta0.copy()
    theta = theta0.copy()
    
    for n in range(1, nt):
        theta, _ = upstream_step(theta, u, dx, dt)
        theta = apply_boundary_conditions(theta, BC, fixed_value=None)
        results[n] = theta.copy()
    
    return results

#for test cases 1,4,5
theta0 = np.zeros_like(x)
theta0[0] = 250

#test case one
x, g = model_spatial_grid(20, 0.2)
t, ti = model_time_grid(300, 10)

C1 = run_simulation(theta0, u=0.1, x=x, t=t)
plot_snapshots(C1, x, dt=10, title="Test Case 1: Delta Initial Condition")
        
#test case two
theta0_csv = generate_intial_conditions("data/initial_conditions.csv", x)

C2 = run_simulation(theta0_csv, u=0.1, x=x, t=t)
plot_snapshots(C2, x, dt=10, title="Test Case 2: CSV Initial Condition")

#test case three
u_values = [0.05, 0.1, 0.2]
dx_values = [0.1, 0.2]
dt_values = [5, 10]

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

#test case 4
tau = 100
decay = np.exp(-t / tau)
theta0[0] *= decay[0]

C4 = run_simulation(theta0, u=0.1, x=x, t=t)
C4[:, 0] *= decay
plot_snapshots(C4, x, dt=10, title="Test Case 4: Exponential Decay")

#test case 5
rng = np.random.default_rng(123)
u_pert = 0.1 * (1 + 0.1 * rng.standard.normal(len(x)))

C5 = run_simulation(theta0, u_pert, x=x, t=t)
plot_snapshots(C5, x, dt=10, title="Test Case 5: Perturbed Velocity")












