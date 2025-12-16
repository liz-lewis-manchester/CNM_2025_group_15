#BC = Boundary Conditions, the values at the edge of the model domain
#Left boundary (upstream) x = theta, Right boundary (downstream) x = L
#Apply BC to updated concentration array (updated_theta)
#theta is numpy array of concentration at a given time

def apply_boundary_conditions(updated_theta, BC, fixed_value=None):
	
    theta_BC = updated_theta.copy()
	
	#validation check 
	if BC in ("fixed", "inflow") and fixed_value is None:
		raise ValueError("fixed_value must be provided for fixed or inflow BC")

    if BC == "fixed":
        theta_BC[0] = fixed_value #[0] to get the first value (upstream boundary)
        theta_BC[-1] = fixed_value #[-1] to get the last value (downstream boundary)

    elif BC == "inflow":
        theta_BC[0] = fixed_value #constant upstream concentration
        theta_BC[-1] = theta_BC[-2] #downstream boundary zero gradient, pollutant flows out naturally

    elif BC == "zero_gradient": #the concentration change between two points is zero
        theta_BC[0] = theta_BC[1] #[1] to get the first value just inside the upstream boundary
        theta_BC[-1] = theta_BC[-2] #[-2] to get the last value before the downstream boundary

    else:
        raise ValueError("Unknown BC")

    return theta_BC
