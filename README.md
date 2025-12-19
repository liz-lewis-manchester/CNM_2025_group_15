# CNM_2025_group_15
This project simulates the evolution of pollutant concentration in a river using numerical methods learnt in CIVL20471.
### Description
This simulation models the pollutant concentration at any time and point in the model domain with the following advection equation:
```math
$$\frac{\partial \theta}{\partial t} = -U\frac{\partial \theta}{\partial x}$$
```
where:
- θ = pollutant concentration (µg/m³)
- t = time (s)
- x = distance along the river (m)
- U = velocity (ms⁻¹)

An explicit first-order upwind finite difference scheme is used with appropriate boundary conditions and CFL stability control. Optional exponential decay and 10% perturbation can also be tested within the simulation.

The code allows users to:
- Specify the model domain and resolution,
- Read and interpolate initial condition data from a CSV file,

### Output
This simulation produces the following figures:
- Space-time contour plots stored in the results folder
- Snapshots of concentration against distance graphs stored in the results folder
- Concentration against distance graph displayed in the output

### Executing program
Open run_model.py and edit the user input section below the comment:
"###Specify your own test case, model domain and resolution here###"

After running the model, relevant figures will be displayed in the results folder and the output of the code.

### Test Case
Five different test cases can be run using this simulation:

1. Constant inflow
θ = 250 µg/m³ imposed at x = 0
Default settings: L = 20 m, T = 300 s, dt = 10 s, U = 0.1 m s⁻¹

2. CSV initial condition
Initial pollutant concentration read from initial_conditions.csv

3. Sensitivity analysis
Tests the sensitivity of the model to velocity, spatial resolution, and timestep

4. Exponential decay
Initial concentration undergoes first-order exponential decay during advection

5. Perturbed velocity field
A spatially varying velocity profile created by adding a 10% perturbation

### Code Structure
run_model.py – main entry point for running simulations

src/ – numerical methods and plotting functions

Tests/ – definitions of test cases

Data/ – input CSV files

results/ – generated output figures

### Authors
Group 15

Abel Arnold

Sage Bidwell

Jansara Klinsukont

Hannah Twiddle

Hannah Whitby
