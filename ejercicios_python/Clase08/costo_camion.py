# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca
# Ejercicio 4.3: Un ejemplo práctico de enumerate()
# Ejercicio 4.4: La función zip()
# Ejercicio 7.9: Un poco más allá
# Ejercicio 8.4: Función principal
# Ejercicio 8.5: Hacer un script

from informe_final import leer_camion

def costo_camion(path: str) -> float:
    camion = leer_camion(path=path)
    total = 0.0

    for row in camion:
        total += row.get('cajones') * row.get('precio')

    return total

def f_principal(path: str) -> None:
    costo = costo_camion(path=path)
    print(f'El costo total del camion es: {costo}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} path_archivo_camion')
    f_principal(path=sys.argv[1])