import numpy as np
from utlis import fourier as frr
from utlis import cmplx as cmx

from time import time
import matplotlib.pyplot as plt

fs = 512
t = np.linspace(0, 1, fs)

x_t = np.sin(2 * 100 * np.pi * t) + np.random.normal(0, scale = 0.1, size = t.shape)

print("Computing FFT of Signal using fft_ct() function ...")
start = time()
fft_sin = frr.fft_ct(x_t, sym = True)
print(f"it takes {np.round(time() - start, 4)}s to calculate FFT")

print("Computing FFT of Signal using numpy fft function ...")
start = time()
npfft_sin = np.fft.fft(x_t)
print(f"it takes {np.round(time() - start, 4)}s to calculate FFT")

print("Computing FFT of Signal using numpy fft_it function ...")
start = time()
fft_sin_i = frr.fft_it(x_t, sym = True)
print(f"it takes {np.round(time() - start, 4)}s to calculate FFT")

fig, ax = plt.subplots(1, 1)

ax.plot(np.abs(npfft_sin), label = "NumPy-FFT")
ax.plot(cmx.abs(fft_sin_i), label = "fft_it")
ax.plot(cmx.abs(fft_sin), label = 'fft_ct')

ax.set_title("Comparison of Different FFT Outputs")
ax.legend()

plt.show()