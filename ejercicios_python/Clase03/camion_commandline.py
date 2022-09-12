# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca
# Ejercicio 3.11: Ejecución desde la línea de comandos con parámetros

import csv
import sys

class Console:
    def __init__(self):
        pass

    def log(self, *values):
        print(values)

def costo_camion(path: str) -> float:
    console = Console()
    file = open(path)
    rows = csv.reader(file)
    _ = next(rows) # Headers: nombre, cajones, precio
    
    costo_total = 0
    for row in rows:
        try:
            console.log('row', row)
            [_, cajones, precio] = row
            costo_total += int(cajones) * float(precio)
        except ValueError:
            print('El archivo no tiene el formato esperado.')

    file.close()
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = './Data/camion.csv'

costo = costo_camion(path=nombre_archivo)
print(f'El costo total del camion es: ${costo}')