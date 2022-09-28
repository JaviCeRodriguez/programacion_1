# Ejercicio 6.9: Empezando a plotear

import matplotlib.pyplot as plt
import numpy as np


def plotar_temperaturas():
    temperaturas = np.loadtxt('./Data/temperaturas.npy')
    plt.hist(temperaturas,bins=80)
    plt.show()

plotar_temperaturas()