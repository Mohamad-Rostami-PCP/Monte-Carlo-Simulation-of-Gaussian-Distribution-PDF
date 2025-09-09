# import libraries
import numpy as np
import math
import random
import matplotlib.pyplot as plt
# Global variables
N = 100000
n = 100
r = 30
peak = 4
# calculate the bins
def bin_calculator(distribution):
    local_N = distribution.shape[0]
    min_value = np.min(distribution)
    length = (np.max(distribution) - min_value) / n
    Bin = np.zeros(n)
    Bin_breakpoints = np.zeros(n + 1)
    for i in range(n + 1):
        Bin_breakpoints[i] = min_value + i * length
    return Bin, Bin_breakpoints
# probability distribution function
def PDF(distribution, N_effective):
    Bin, breakpoints = bin_calculator(distribution)
    N_pdf = N_effective
    n_pdf = Bin.shape[0]
    for i in range(N_pdf):
        value = distribution[i]
        for j in range(n_pdf):
            if breakpoints[j] < value < breakpoints[j + 1]:
                Bin[j] += 1
                break
    X = np.zeros(n_pdf)
    for i in range(n_pdf):
        X[i] = (breakpoints[i] + breakpoints[i + 1]) / 2
    P = Bin / N_pdf
    return P, X
# Gaussian function
def Gaussian_function(x):
    y = (np.exp(1)) ** ((-1) * ((x - peak) ** 2))
    return y
# Accept and rejection
def Ac_Re():
    Gaussian_Distribution = np.zeros(N, dtype=float)
    N_effective = 0
    while N_effective < N:
        x_rand1 = random.uniform(-r, +r)
        P_G_ = Gaussian_function(x_rand1)
        p_rand2 = random.random()
        if p_rand2 <= P_G_:
            Gaussian_Distribution[N_effective] = x_rand1
            N_effective += 1
    return Gaussian_Distribution, N_effective
# Run section
#   phase_1: create gaussian distribution
Gaussian_distribution, N_eff = Ac_Re()
#   phase_2 : create probability
P_G, X = PDF(Gaussian_distribution, N_eff)
#   phase_3 : create gaussian distribution
plt.plot(X, P_G, 'o', ms=3)
plt.show()
