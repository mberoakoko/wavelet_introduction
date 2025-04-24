import numpy as np

from ops.harmonics_generator import SinusoidalHarmonics, compose_harmonics, LocationBasedHarmonics

if __name__ == "__main__":
    sig_resolution=1000
    result = compose_harmonics(
        harmonic_tune=np.zeros(15000),
        loc_harmonics=[
            LocationBasedHarmonics(
                location=1000,
                harmonics=SinusoidalHarmonics(freq=1, duration=10, resolution=sig_resolution)),
            LocationBasedHarmonics(
                location=2000,
                harmonics=SinusoidalHarmonics(freq=1, duration=10., resolution=sig_resolution)),
            LocationBasedHarmonics(
                location=3000,
                harmonics=SinusoidalHarmonics(freq=1, duration=10, resolution=sig_resolution)),
        ]
    )