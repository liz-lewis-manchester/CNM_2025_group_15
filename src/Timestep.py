def run_one_timestep(theta, U, dx, dt, solver_func, BC, fixed_value=None): #runs one timestep
  theta_new, cfl = solver_func(theta, U, dx, dt) #calls the solver to compute theta_new and cfl
  theta_new = apply _boundary_conditions(theta_new, BC, fixed_value) #applys boundary conditions
  return theta_new, cfl
