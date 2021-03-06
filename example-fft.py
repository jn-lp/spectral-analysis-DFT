import matplotlib
import matplotlib.pyplot as plt
import rsg
from fft import fft, real

HARMONICS = 8
FREQUENCY = 1200
N = 1024

sigs = rsg.generate(HARMONICS, FREQUENCY, N)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(sigs)
ax1.set_xlim(0, int(N/4))
ax1.set(xlabel='time', ylabel='signal',
        title='Random generated signals')

ax2.plot(real(fft(sigs)))
ax2.set_xlim(0, int(N/4))
ax2.set(xlabel='time', ylabel='frequency',
        title='Frequency spectrum using FFT')

fig.savefig("example-fft.png")
plt.show()
