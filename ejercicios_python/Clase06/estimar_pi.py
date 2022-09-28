# Ejercicio 6.5: Calcular pi

from random import random


def generar_punto() -> dict[str, float]:
    return { "x": random(), "y": random() }

def is_unitary(point: dict[str, float]) -> bool:
    return pow(point["x"], 2) + pow(point["y"], 2) < 1


N = 100_000
points = [generar_punto() for _ in range(N)]
points_in_circle = [point for point in points if is_unitary(point)]
M = len(points_in_circle)
pi = 4 * M / N

print(f'Generando N={N} puntos, M={M} entran en un círculo unitario. Entonces, 4 * M / N ~ {pi}')
