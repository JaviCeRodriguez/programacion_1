# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca
# Ejercicio 4.3: Un ejemplo práctico de enumerate()
# Ejercicio 4.4: La función zip()

import csv

def costo_camion(path: str) -> float:
    total = 0.0
    file = open(path)
    rows = csv.reader(file)
    headers = next(rows) # Headers: nombre, cajones, precio
    
    for idx, row in enumerate(rows):
        try:
            row_zip = dict(zip(headers, row))
            total += int(row_zip.get('cajones')) * float(row_zip.get('precio'))
        except ValueError:
            print(f'Fila {idx + 1}: No puede interpretar: {row}')

    file.close()
    return total

costo = costo_camion(path='./Data/fecha_camion.csv')
print(f'El costo total del camion es: ${costo}')