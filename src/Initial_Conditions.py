import numpy as np 
import pandas as pd 

def generate_initial_conditions(x_grid, mode='csv',file=None, pulse_location=None, pulse_strength=None): #defines a function
    #csv mode test case 2
    if mode == 'csv': #checks if CSV is being used
        if file is None:
            raise ValueError("CSV mode requires file='path/to/file.csv'") #if CSV is not used, stops this mode with a message
        df = pd.read_csv(file) #read the CSV 
        x_data = df["Distance"].values #extract data from CSV and returns a panda series which is then converted into a NumPy array
        theta_data = df["Concentration"].values # extract concentration data from CSV
        theta_initial = np.interp(x_grid, x_data, theta_data) #interpolates data onto the grid
        return theta_initial
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

