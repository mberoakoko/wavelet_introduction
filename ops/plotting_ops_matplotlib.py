import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import  Axes
from matplotlib.figure import Figure

matplotlib.use("TkAgg")
plt.rcParams.update({"font.size": 8})
plt.style.use("dark_background")


class Plotter:
    @staticmethod
    def plot_simple_harmonics(signal: np.ndarray) -> None:
        fig: Figure = plt.figure(figsize=(16//2, 9//2))
        ax: Axes = fig.add_subplot()
        ax.plot(signal, color="C1", label="harmonic signal")
        ax.set_title("Simple Harmonic Signal")
        ax.legend()
        plt.tight_layout()
        plt.show()