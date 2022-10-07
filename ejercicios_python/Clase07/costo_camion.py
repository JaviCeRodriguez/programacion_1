# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca
# Ejercicio 4.3: Un ejemplo práctico de enumerate()
# Ejercicio 4.4: La función zip()
# Ejercicio 7.9: Un poco más allá

from informe_funciones import leer_camion

def costo_camion(path: str) -> float:
    camion = leer_camion(path=path)
    total = 0.0

    for row in camion:
        total += row.get('cajones') * row.get('precio')

    return total

costo = costo_camion(path='./Data/camion.csv')
print(f'El costo total del camion es: ${costo}')