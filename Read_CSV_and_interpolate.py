import numpy as np 
import pandas as pd 

def generate_initial_conditions(x_grid, mode='csv',file=None, pulse_location=None, pulse_strength=None):
    #csv mode test case 2
    if mode == 'csv':
        if file is None:
            raise ValueError("CSV mode requires file='path/to/file.csv'")
        df = pd.read_csv(file)
        x_data = df["x"].values
        theta_data = df["concentration"].values
        theta_initial = np.interp(x_grid, x_data, theta_data)
        return theta_initial
    #for single spike test case 1 
    elif mode == "delta": 
        if pulse_location is None or pulse_strength is None:
            raise ValueError("Delta mode requires pulse_location and pulse_strength")
        theta = np.zeros_like(x_grid)
        idx = np.argmin(np.abs(x_grid - pulse_location))
        theta[idx] = pulse_strength
        return theta 

