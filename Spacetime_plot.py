import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def plot_spacetime(
    x,
    t,
    theta,
    output_dir="results",
    filename="spacetime_theta.png",
    cmap="viridis",
    show=False
):
    """
    Create and save a spacetime diagram of theta(x, t).

    Parameters
    ----------
    x : 1D numpy array
        Spatial grid (m)
    t : 1D numpy array
        Time grid (s)
    theta : 2D numpy array
        Pollutant concentration with shape (nt, nx)
    output_dir : str
        Directory to save figure
    filename : str
        Output image filename
    cmap : str
        Matplotlib colormap
    show : bool
        Whether to display the figure
    """

    # Check that the solution array has the expected shape
    # This helps catch indexing or solver errors early
    if theta.shape != (len(t), len(x)):
        raise ValueError(
            f"theta shape {theta.shape} does not match (len(t), len(x))"
        )

    # Ensure the output directory exists
    # parents=True allows nested directories (e.g. results/figures/)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create the matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # pcolormesh requires grid *edges* rather than grid centres
    # These edges are constructed assuming a uniform grid
    x_edges = np.linspace(x[0], x[-1], len(x) + 1)
    t_edges = np.linspace(t[0], t[-1], len(t) + 1)

    # Create the spacetime heatmap
    # x is plotted horizontally, t vertically
    mesh = ax.pcolormesh(
        x_edges,
        t_edges,
        theta,
        shading="auto",
        cmap=cmap
    )

    # Add a colorbar to show concentration magnitude
    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("Concentration θ (µg m⁻³)")

    # Label axes with physical units
    ax.set_xlabel("Distance along river (m)")
    ax.set_ylabel("Time (s)")

    # Add a descriptive title
    ax.set_title("Spacetime Evolution of Pollutant Concentration")

    # Adjust layout to prevent label clipping
    fig.tight_layout()

    # Save the figure to disk at high resolution
    save_path = output_dir / filename
    fig.savefig(save_path, dpi=300)

    # Close the figure to avoid memory leaks in batch runs
    plt.close(fig)

    # Optionally display the figure interactively
    if show:
        plt.show()

    # Return the path to the saved figure (useful for testing/logging)
    return save_path

from plotting import plot_spacetime

plot_spacetime(
    x=x,
    t=t,
    theta=theta,
    output_dir="results",
    filename="theta_spacetime.png"
)
