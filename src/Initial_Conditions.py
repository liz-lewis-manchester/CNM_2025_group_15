import numpy as np  
import pandas as pd  
from pathlib import Path 
 
def generate_initial_conditions(x_grid, mode="csv",file=None, pulse_location=None, pulse_strength=None): #defines a function 
    x_grid = np.asarray(x_grid, dtype=float) 
    mode = mode.lower().strip() 
 
    #csv mode test case 2 
    if mode == "csv": #checks if CSV is being used 
        if file is None: 
            raise ValueError("CSV mode requires a file path") #if CSV is not provided, stops this mode with a message 
        df = pd.read_csv(file) #read the CSV  
        x_data = df["Distance (m)"].values #extract data from CSV and returns a panda series which is then converted into a NumPy array 
        theta_data = df["Concentration (�g/m_ )"].values # extract concentration data from CSV 
        return np.interp(x_grid, x_data, theta_data) 
 
   
    #for single spike test case 1  
    elif mode == "delta":  
        if pulse_location is None or pulse_strength is None: #ensure spike location and strength are provided 
            raise ValueError("Delta mode requires pulse_location and pulse_strength")  
        theta = np.zeros_like(x_grid) #creates an array of zeros in the shape of the grid  
        idx = np.argmin(np.abs(x_grid - pulse_location)) #finds the index of the nearest grid point to the location of the spike  
        theta[idx] = pulse_strength #puts the spike at that grid point 
        return theta  
    else: 
        raise ValueError("mode must be 'CSV' or 'delta'") 

