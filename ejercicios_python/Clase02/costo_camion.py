# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca

import csv

def costo_camion(path: str) -> float:
    file = open(path)
    rows = csv.reader(file)
    _ = next(rows) # Headers: nombre, cajones, precio
    
    try:
        costo_total = 0
        for row in rows:
            [_, cajones, precio] = row
            costo_total += int(cajones) * float(precio)
    except ValueError:
        print('El archivo no tiene el formato esperado.')

    file.close()
    return costo_total

costo = costo_camion(path='./Data/camion.csv')
print(f'El costo total del camion es: ${costo}')