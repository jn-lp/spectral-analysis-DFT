import time
import rsg
from dft import dft
from fft import fft, real

HARMONICS = 8
FREQUENCY = 1200
N = 1024

sigs = rsg.generate(HARMONICS, FREQUENCY, N)

start = time.time()
dft(sigs)
print("discrete Fourier transform time: {}".format(time.time() - start))


start = time.time()
fft(sigs)
print("fast Fourier transform time: {}".format(time.time() - start))
