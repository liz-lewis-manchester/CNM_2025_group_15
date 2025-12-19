import sys
import matplotlib.pyplot as plt

sys.path.append('./CNM_2025_group_15/src')
sys.path.append('./CNM_2025_group_15/Tests')

from Test_Cases import plot_snapshots, run_simulation, run_test_case

###Specify your own test case, model domain and resolution here###
test_case =  1     #enter 1, 2, 3, 4, or 5

L = 20.0           # river length (m)
dx = 0.2           # spatial resolution (m)

T = 300.0          # total time (s)
dt = 10            # temporal resolution (s)

U = 0.2            # velocity (float) OR array of length len(x)

BC = "zero_gradient" 


print(f"\n=== Running Test Case {test_case} ===\n")
run_test_case(test_case, L=L, dx=dx, T=T, dt=dt)
