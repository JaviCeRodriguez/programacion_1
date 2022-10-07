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
# Ejercicio 7.1: Estructurar un programa como una colección de funciones
# Ejercicio 7.2: Crear una función de alto nivel para la ejecución del programa.
# Ejercicio 7.8: Usemos tu módulo
from fileparse import parse_csv

def leer_precios(path: str) -> dict:
    precios_informe = parse_csv(nombre_archivo=path, has_headers=False)
    precios = {nombre: float(precio) for nombre, precio in precios_informe}
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
        return precio_fruta


def leer_camion(path: str) -> list[dict]:
    camion = parse_csv(nombre_archivo=path, types=[str, int, float])
    return camion


def costo_camion(informe: list[dict]) -> float:
    total = 0.0

    for row in informe:
        try:
            total += int(row.get('cajones')) * float(row.get('precio'))
        except ValueError:
            print(f'Formato inválido {row}, no se tendrá en cuenta para el cálculo...')

    return total


def imprimir_informe(informe):
    headers = informe[0]
    print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10} ')
    print('---------- ---------- ---------- ----------')
    for row in informe[1:]:
        print(f'{row[0]:>10s} {row[1]:>10d} {"$"+str(round(row[2], 2)):>10} {row[3]:>10.2f}')


def hacer_informe(camion: list[dict], precios: list[dict]):
    rows_informe: list[tuple] = list()
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    for fruta in camion:
        precio_venta = buscar_precio(precios=precios, fruta=fruta.get('nombre'))
        if precio_venta != 0:
            [nombre, cajones, precio, cambio] = [
                fruta.get('nombre'), 
                fruta.get('cajones'), 
                fruta.get('precio'), 
                precio_venta - fruta.get('precio')
            ]
            rows_informe.append((nombre, cajones, precio, cambio))
    
    return [headers] + rows_informe
    

def informe_camion(path_camion, path_precios):
    precios = leer_precios(path=path_precios)
    camion = leer_camion(path=path_camion)
    informe = hacer_informe(camion=camion, precios=precios)
    imprimir_informe(informe=informe)



informe_camion(path_camion='./Data/camion.csv', path_precios='./Data/precios.csv')