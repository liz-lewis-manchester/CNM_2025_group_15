from Boundary_Conditions import apply_boundary_conditions 
def run_one_timestep(theta, U, dx, dt, upstream_step, BC, fixed_value=None): #runs one timestep
  theta_new, cfl = upstream_step(theta, U, dx, dt) #calls the solver to compute theta_new and cfl
  theta_new = apply_boundary_conditions(theta_new, BC, fixed_value) #applys boundary conditions
  return theta_new, cfl
