# Ejercicio 6.13: Crear
# Ejercicio 6.14: Incompleto
# Ejercicio 6.15: Comprar
# Ejercicio 6.16: Cantidad de compras
# Ejercicio 6.17
# Ejercicio 6.18
# Ejercicio 6.19
# Ejercicio 6.20
# Ejercicio 6.21
# Ejercicio 6.22
# Gráfico



import random
import numpy as np
import matplotlib.pyplot as plt


def crear_album(figus_total):
    return np.zeros(figus_total)


def album_incompleto(album):
    return not album.all()


def comprar_figu(figus_total):
    return random.randint(0, figus_total)


def cuantas_figus(figus_total):
    compradas = 0
    album = crear_album(figus_total=figus_total)

    while album_incompleto(album):
        figu = comprar_figu(figus_total=figus_total)
        album[figu - 1] = 1
        compradas += 1
    
    return compradas


def experimento_figus(n_repeticiones, figus_total):
    albums = [cuantas_figus(figus_total=figus_total) for _ in range(n_repeticiones)]
    return np.mean(albums)


def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total=figus_total) for _ in range(figus_paquete)]


def cuantos_paquetes(figus_total, figus_paquete):
    compradas = 0
    album = crear_album(figus_total=figus_total)

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total=figus_total, figus_paquete=figus_paquete)
        for figu in paquete:
            album[figu - 1] = 1
        compradas += 1

    return compradas


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop() - 1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


figus_total = 670
figus_paquete = 5
n_repeticiones = 100

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()


# repeticiones = [cuantas_figus(figus_total=6) for _ in range(n_repeticiones)]
# print(f'[En album de 6 figus] Se deben comprar {np.mean(repeticiones):.2f} figuritas en promedio')

# experimento = experimento_figus(n_repeticiones=100, figus_total=figus_total)
# print(f'[En album de {figus_total} figus] Se deben comprar {experimento:.2f} figuritas en promedio')

# paquetes = [cuantos_paquetes(figus_total=figus_total, figus_paquete=5) for _ in range(100)]
# print(f'[En album de {figus_total} figus y pack de 5] Se deben comprar {np.mean(paquetes):.2f} paquetes en promedio')
