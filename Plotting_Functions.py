import matplotlib.pyplot as plt #for graph plots
import numpy as np 

def function_snapshot (x, theta_history, t_grid, snapshot_times, save_dir="results"):  #function "function_snapshot" to create graph
  #x = spatial grid
  #theta_history = 2D matrix of polutant concentrations over select time
  #t_grid = time values selected
  #snapshot_times = the paticular times plotted
  #save_dir = folder results is saved in (results)

  colors = plt.cm.plasma(np.linspace(0, 1, len(snapshot_times))) #introducing colours to be used in plots
  
  for i, t_target in enumerate(snapshot_times): #loop time values that will be plotted
    
    index = np.abs(t_grid - t_target).argmin()  #finding closest target time index in time grid
    
    plt.figure(figsize=(9,5))  
    plt.plot(x, theta_history[index, :], color=colors[i], linewidth=2.5) #plotting concentration vs distance
    plt.title(fr"Pollutant concentration at $t = {t_grid[index]:.1f}\,\mathrm{{s}}$", fontsize=14, weight="bold")  #fr to accomodate LaTeX and and formatted text
    plt.xlabel(r"Distance downstream $x\,(\mathrm{m})$", fontsize=12)  #r for avoiding escaping issues
    plt.ylabel(r"Concentration $\theta\,(\mathrm{\mu g\,m^{-3}})$", fontsize=12)
    plt.grid(True, alpha=0.5) #adding grid lines
    plt.tight_layout()  #avoiding clipping titles
    filename = f"{save_dir}/snapshot_t{int(t_grid[index])}.png"  #what the snapshot is saved as in "results"
    plt.savefig(filename, dpi=250, bbox_inches="tight")  #saves plot as PNG image
    plt.close()
