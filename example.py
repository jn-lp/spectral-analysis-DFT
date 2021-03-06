import matplotlib
import matplotlib.pyplot as plt
import rsg
from dft import dft

HARMONICS = 8
FREQUENCY = 1200
N = 1024

sigs = rsg.generate(HARMONICS, FREQUENCY, N)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(sigs)
ax1.set_xlim(0, int(N/4))
ax1.set(xlabel='time', ylabel='signal',
        title='Random generated signals')

ax2.plot(dft(sigs))
ax2.set_xlim(0, int(N/4))
ax2.set(xlabel='time', ylabel='frequency',
        title='Frequency spectrum using DFT')

fig.savefig("example.png")
plt.show()
