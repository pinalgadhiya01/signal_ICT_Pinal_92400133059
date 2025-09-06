import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    shifted = np.roll(signal, k)
    return shifted

def time_scale(signal, k):
    scaled = signal[::k] if k > 0 else signal
    return scaled

def signal_addition(signal1, signal2):
    min_len = min(len(signal1), len(signal2))
    return signal1[:min_len] + signal2[:min_len]

def signal_multiplication(signal1, signal2):
    min_len = min(len(signal1), len(signal2))
    return signal1[:min_len] * signal2[:min_len]