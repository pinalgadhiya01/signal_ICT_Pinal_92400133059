1.	unitary_signals.py
Implement the following functions:
	unit_step(n) – Generates a unit step signal.
	unit_impulse(n) – Generates a unit impulse signal.
	ramp_signal(n) – Generates a ramp signal.
Each function should return a NumPy array and plot the signal using matplotlib.
2.	trigonometric_signals.py
Implement the following functions:
	sine_wave(A, f, phi, t) – Generates a sine wave with amplitude A, frequency f, phase phi, and time vector t.
	cosine_wave(A, f, phi, t) – Generates a cosine wave with similar parameters.
	exponential_signal(A, a, t) – Generates an exponential signal.
3.	operations.py
Implement the following signal operations:
	time_shift(signal, k) – Shifts the signal by k units.
	time_scale(signal, k) – Scales the time axis of the signal by factor k.
	signal_addition(signal1, signal2) – Performs addition of two signals.
	signal_multiplication(signal1, signal2) – Performs point-wise multiplication of two signals.