# Ejercicio 6.4: Envido

import random


def contar_envido(mano: list[tuple]) -> int:
    envido = 0

    for palo in palos: # Analizo cada palo
        palito = False # Variable para detectar si hay palo en mano
        list_mano = [0] * 3 # Uso una lista para hacer operaciones con cada palo
        for idx, carta in enumerate(mano): # Analizo la mano. carta = (valor, palo)
            if carta[1] == palo and carta[0] < 10: # Chequeo si la carta es el palo a analizar y si es menor a 10
                list_mano[idx] = carta[0]
                palito = True
        if envido == 0 and palito: # Si envido es 0, tomo de referencia el palo detectado
            envido = sum(list_mano)
            if envido != 0: # Si envido sigue siendo 0, es porque hay negras
                envido += 20
        elif palito and (sum(list_mano) + 20) > envido: # De un palo, consegui 1 o 2 carta/s (1 al 7)
            envido = sum(list_mano)+20
        else:
            pass
    return envido


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
N = 10000
envidos = {
    '31': 0,
    '32': 0,
    '33': 0
}

for i in range(N):
    mazo = [(valor, palo) for valor in valores for palo in palos]
    mano = random.sample(mazo, k=3)

    envido = contar_envido(mano)
    if envido in [31, 32, 33]:
        envidos[str(envido)] += 1


sum_cant_envidos = sum(envidos.values())
print(f'De {N} muestras, con un total de {sum_cant_envidos} envidos, la probabilidad es {sum_cant_envidos/N:.6f}.')