import math


def w(k, N):
    expression = 2.0 * math.pi * k / N
    return complex(math.cos(expression), math.sin(expression))


def fft(signals):
    N = len(signals)
    if N == 1:
        return signals

    spectrum = [0] * N

    evens = fft(signals[::2])
    odds = fft(signals[1::2])

    l = N/2
    for k in range(l):
        expression = odds[k] * w(k, N)

        spectrum[k] = evens[k] + expression
        spectrum[k + l] = evens[k] - expression

    return spectrum


def real(ispectrum):
    return [abs(x) for x in ispectrum]
