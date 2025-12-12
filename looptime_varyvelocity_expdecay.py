###This code should loop time steps, save results to a history to use for graphs, allows users to test an initial exponential decay (test case 4), and allow users to add a variable stream velocity with a 10% perturbation 

def run_simulation (theta0, U, dx, dt, nt, boundaryconditions, advectionsolver, apply_decay=False, decay_rate=0.0, apply_perturbation=False) #recheck through other files to use the correct boundary conditions and advection solver variable name, and make sure the rest of the variables align

  theta = theta0.copy() #create copy of initial concentration at x=0 to avoid overwriting the user's input
  N = len(theta)
  
### Inputting the user's velocity into an array
  if np.isscalar (U):
    U_input = np.full(N, float(U))
  else:
    U_input = np.asarray(U, dtype=float) 

#add a warning func here if an unusable value is input by the user?? ask hannah t
  
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
  for n in range(1, nt);
    theta[0] = theta[0] * decay[n] 
    theta = boundaryconditions(theta) #change boundary conditions variable name
    theta, _ = advectionsolver(theta, U_input, dx, dt) #change solver variable name
    theta_result[n] = theta.copy()

  return theta_result, U_input


