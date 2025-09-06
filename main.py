import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_Pinal_92400133059 import *

#1. Generate and plot a unit step & unit impulse (length 20)
n = np.arange(-10, 10)
step = unit_step(n)
impulse = unit_impulse(n)

#2. Generate a sine wave
t = np.linspace(0, 1, 1000)
sine = sine_wave(2, 5, 0, t)

#3. Time shifting 
shifted_sine = time_shift(sine, 5)
plt.plot(t, sine, label="Original Sine")
plt.plot(t, shifted_sine, label="Shifted Sine (+5)")
plt.legend()
plt.title("Time Shifting of Sine Wave")
plt.show()

#4. Addition 
ramp = ramp_signal(n)
added = signal_addition(step, ramp)
plt.stem(n[:len(added)], added)
plt.title("Unit Step + Ramp Signal")
plt.show()

#5. Multiplication
cos = cosine_wave(2, 5, 0, t)
multiplied = signal_multiplication(sine, cos)
plt.plot(t[:len(multiplied)], multiplied)
plt.title("Sine × Cosine")
plt.show()