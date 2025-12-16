import numpy as np

#####
#Creating a spatial grid for the model domain where L is the length of the river and dx is the spatial resolution
def model_spatial_grid (L, dx):
  if dx <= 0:
    raise ValueError("dx must be a positive value and cannot be zero")
    
  if dx > L / 5:
    raise ValueError("dx is too large compared to the domain length")

  if dx < L / 1000:
    raise ValueError("dx is too small compared to the domain length")
    
  nx = int(np.round(L / dx)) + 1 #Number of grid points along the river
  x = np.linspace(0, L, nx) #Spatial grid that starts at zero and ends at L

  
  #Dictionary of the grid properties
  grid_properties = {
    "L": L,
    "dx": dx,
    "nx": nx
  }

  return x, grid_properties

#####
#Creating a time grid where T is the total time of the resolution and dt is the temporal resolution
def model_time_grid (T, dt):

  if dt <= 0:
    raise ValueError("dt must be a positive value and cannot be zero")

  nt = int(np.round(T / dt)) + 1 #Number of time points
  t = np.linspace(0, T, nt) #Temporal grid that starts at zero

  grid_properties = {
    "T": T,
    "dt": dt,
    "nt": nt
  }

  return t, grid_properties
