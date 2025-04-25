import numpy as np

from ops.harmonics_generator import generate_simple_signal
from ops.plotting_ops_matplotlib import Plotter

if __name__ == "__main__":
    Plotter.plot_simple_harmonics(signal=generate_simple_signal(signal_resolution=10000))
