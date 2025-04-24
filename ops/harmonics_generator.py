from __future__ import  annotations
import numpy as np
import dataclasses
import functools
from typing import NamedTuple


def hamming(n):
    """ Hamming window of size N for smoothing the edges of sound waves """
    return 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(n) / (n-1))


@dataclasses.dataclass
class SinusoidalHarmonics:
    freq: float
    duration: float
    resolution: float

    def generate_harmonics(self) -> np.ndarray:
        ln = self.duration * self.resolution
        sound = np.sin(np.arange(ln) * 2 * np.pi * self.freq / self.resolution)
        return sound * hamming(ln)


class LocationBasedHarmonics(NamedTuple):
    location: float
    harmonics: SinusoidalHarmonics


def compose_harmonics(harmonic_tune: np.ndarray, loc_harmonics: list[LocationBasedHarmonics]) -> np.ndarray:
    def reduction_op(accum: np.ndarray, item: LocationBasedHarmonics) -> np.ndarray:
        step = item.harmonics.duration * item.harmonics.resolution
        print(f"{accum.shape=}")
        print(f"{item.harmonics.generate_harmonics().shape=}")
        accum[item.location: step] += item.harmonics.generate_harmonics()
        return accum
    return functools.reduce(reduction_op, loc_harmonics, harmonic_tune)
