# Ejercicio 6.6: Gaussiana
# Ejercicio 6.8: Guardar temperaturas

from random import normalvariate
import numpy as np


def medir_temp(n: int) -> np.ndarray:
    mu = 0
    sigma = 0.2
    temp = 37.5
    temperaturas = np.array([temp + normalvariate(mu, sigma) for _ in range(n)])
    np.savetxt('./Data/temperaturas.npy', temperaturas)
    return temperaturas

def resumen_temp(n: int) -> tuple[float]:
    mediciones = medir_temp(n)

    # Sin numpy
    # largo = len(mediciones)
    # max_temp = max(mediciones)
    # min_temp = min(mediciones)
    # prom_temp = sum(mediciones) / largo
    # mediana_temp = None
    # if largo % 2 == 0:
    #     mediana_temp = sum([mediciones[largo // 2], mediciones[(largo // 2) - 1]]) / 2
    # else:
    #     mediana_temp = mediciones[largo // 2]
    max_temp = mediciones.max()
    min_temp = mediciones.min()
    prom_temp = mediciones.mean()
    mediana_temp = np.median(mediciones)

    
    return (max_temp, min_temp, prom_temp, mediana_temp)


# print(resumen_temp(n=200)) # (38.048744155699694, 37.03249088300422, 37.50394647346953, 37.539343533697405)
# print(resumen_temp(n=333)) # (38.0794355114447, 36.86868493319394, 37.49354571669419, 37.578515461205306)

resumen_temp(n=999)