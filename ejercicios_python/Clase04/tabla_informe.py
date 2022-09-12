# Ejercicio 2.2: Lectura de un archivo de datos
# Ejercicio 2.6: Transformar un script en una función
# Ejercicio 2.9: Funciones de la biblioteca <--- hasta acá era costo_camion.py
# Ejercicio 3.1: Lista de tuplas
# Ejercicio 3.2: Lista de diccionarios
# Ejercicio 4.4: La función zip()
# Ejercicio 4.8: Recolectar datos
# Ejercicio 4.9: Imprimir una tabla con formato
# Ejercicio 4.10: Agregar encabezados
# Ejercicio 4.11: Un desafío de formato

import csv

def leer_precios(path: str) -> dict:
    precios = dict()
    file = open(path)
    rows = csv.reader(file)

    for row in rows:
        try:
            [nombre, precio] = row
            precios[nombre] = float(precio)
        except ValueError: # La linea no tiene el formato esperado
            pass
    
    file.close()
    return precios


def buscar_precio(precios: dict, fruta: str) -> float:
    precio_fruta = None

    for key, value in precios.items():
        if key.lower() == fruta.lower():
            precio_fruta = value

    if precio_fruta is None:
        print(f'{fruta} no figura en el listado de precios.')
        return 0
    else:
        # print(f'El precio de un cajón de {fruta} es ${precio_fruta}')
        return precio_fruta


def leer_camion(path: str) -> list[dict]:
    camion: list[dict] = []
    file = open(path)
    rows = csv.reader(file)
    headers = next(rows) # Headers: nombre, cajones, precio

    for idx, row in enumerate(rows):
        try:
            camion.append(dict(zip(headers, row)))
        except ValueError:
            print(f'Fila {idx + 1}: No puede interpretar: {row}')

    file.close()
    return camion


def costo_camion(informe: list[dict]) -> float:
    total = 0.0

    for row in informe:
        try:
            total += int(row.get('cajones')) * float(row.get('precio'))
        except ValueError:
            print(f'Formato inválido {row}, no se tendrá en cuenta para el cálculo...')

    return total


def hacer_informe(camion: list[dict], precios: list[dict]):
    rows_informe: list[tuple] = list()
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    for fruta in camion:
        precio_venta = buscar_precio(precios=precios, fruta=fruta.get('nombre'))
        if precio_venta != 0:
            [nombre, cajones, precio, cambio] = [
                fruta.get('nombre'), 
                int(fruta.get('cajones')), 
                float(fruta.get('precio')), 
                precio_venta - float(fruta.get('precio'))
            ]
            rows_informe.append((nombre, cajones, precio, cambio))
    
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10} ')
    print('---------- ---------- ---------- ----------')
    for row in rows_informe:
        print(f'{row[0]:>10s} {row[1]:>10d} {"$"+str(round(row[2], 2)):>10} {row[3]:>10.2f}')


# Precios de venta
precios = leer_precios(path='./Data/precios.csv')

# Precios del camión
informe = leer_camion(path='./Data/fecha_camion.csv')

hacer_informe(camion=informe, precios=precios)
