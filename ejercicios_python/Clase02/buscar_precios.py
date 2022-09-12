# Ejercicio 2.3: Precio de la naranja
# Ejercicio 2.7: Buscar precios

def buscar_precio(fruta: str):
    file = open('./Data/precios.csv')
    precio_fruta = None

    for line in file:
        try:
            [nombre, precio] = line.strip('\n').split(',')
            if nombre.lower() == fruta.lower():
                precio_fruta = float(precio)
        except ValueError: # La linea no tiene el formato esperado
            pass

    file.close()

    if precio_fruta is None:
        print(f'{fruta} no figura en el listado de precios.')
    else:
        print(f'El precio de un cajón de {fruta} es ${precio_fruta}')

buscar_precio('Frambuesa')
buscar_precio('Kale')
