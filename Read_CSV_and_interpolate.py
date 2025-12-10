import numpy as np 
import pandas as pd 

L=20 # length of the domain
dx=0.2 # spatial interval 
x_grid =np.arange(0, L + dx, dx) #create an array defining the start, stop and step

df=pd.read_csv("initial_conditions.csv") #read CSV
x_data = df["x"].values # extract data from CSV and returns a panda series which is then converted into a NumPy array

theta_data = df["concentration"].values # extracts concentration data from CSV
theta_initial= np.interp(x_grid, x_data, theta_data) # interpolate data onto grid producing a new NumPy array
