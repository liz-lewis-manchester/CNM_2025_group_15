###This code should loop time steps, save results to a history to use for graphs, allow users to test an initial exponential decay (test case 4), and allow users to add a variable stream velocity with a 10% perturbation 

import numpy as np

def run_simulation (theta, U, dx, dt, nt, apply_boundary_conditions, upstream_step, apply_decay=False, decay_rate=0.0, apply_perturbation=False):

### Define N and U 
  N = len(theta)
  U_input = U #to ensure U is always defined
  
### Allowing exponentially decaying initial concentration (Test Case 4)
  if apply_decay:
    decay = np.exp(-decay_rate * np.arange(nt) * dt)
  else:
    decay = np.ones(nt)
  
### Allowing a variable stream velocity profile (Test Case 5)
  if apply_perturbation: #check if perturbation has already been created in other files
    perturb = 0.10 
    noise = perturb*np.random.randn(N)
    U_input = U_input*(1 + noise) #applies the 10% perturbation 
  
### Creating an array of results to save concentration for graphs
  theta_result = np.zeros((nt, N))
  theta_result[0] = theta.copy()
  
### Time Step Loop
  for n in range(1, nt):
    theta[0] = theta[0] * decay[n] 
    theta = apply_boundary_conditions(theta) 
    theta, _ = upstream_step(theta, U_input, dx, dt) #change solver variable name
    theta_result[n] = theta.copy()

  return theta_result, U_input
