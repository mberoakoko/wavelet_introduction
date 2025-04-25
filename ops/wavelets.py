import numpy as np


def mexican_hat(x: np.ndarray, mu: float, sigma: float):
    return 2 / (np.sqrt(3 * sigma) * np.pi**0.25) * (1 - x**2 / sigma**2) * np.exp(-x**2 / (2 * sigma**2) )


def gauss(x: np.ndarray, mu: float, sigma: float):
    return 1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))
