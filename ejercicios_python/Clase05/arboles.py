# Ejercicio 4.13: Lectura de los árboles de un parque
# Ejercicio 4.14: Determinar las especies en un parque
# Ejercicio 4.15: Contar ejemplares por especie
# Ejercicio 4.16: Alturas de una especie en una lista
# Ejercicio 4.17: Inclinaciones por especie de una lista
# Ejercicio 4.18: Especie con el ejemplar más inclinado
# Ejercicio 4.19: Especie más inclinada en promedio
# Ejercicio 5.15: Lectura de todos los árboles
# Ejercicio 5.16: Lista de altos de Jacarandá
# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
# Ejercicio 5.18: Diccionario con medidas

import csv
from collections import Counter

def leer_arboles(nombre_archivo: str) -> list[dict]:
    with open(nombre_archivo, 'r', encoding="utf8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        return [dict(zip(headers, row)) for row in rows]

def leer_parque(nombre_archivo: str, parque: str) -> list[dict]:
    arboles: list[dict] = []
    with open(nombre_archivo, 'r', encoding="utf8") as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for row in rows:
            arbol_dict = dict(zip(headers, row))
            if arbol_dict.get('espacio_ve') == parque:
                arboles.append(arbol_dict)

        return arboles


def contar_ejemplares(lista_arboles: list[dict]) -> dict:
    especies = Counter()
    for arbol in lista_arboles:
        especies[arbol['nombre_com']] += 1
    return dict(especies.most_common(5))


def obtener_alturas(lista_arboles: list[dict], especie: str) -> list[float]:
    alturas = [float(arbol.get('altura_tot')) for arbol in lista_arboles if arbol.get("nombre_com") == especie]
    
    max_altura = max(alturas)
    prom_altura = sum(alturas) / len(alturas)

    return [max_altura, prom_altura]


def obtener_inclinaciones(lista_arboles: list[dict], especie: str) -> list[float]:
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol.get('nombre_com') == especie:
            inclinaciones.append(float(arbol.get('inclinacio')))

    return inclinaciones


def especies(lista_arboles: list[dict]) -> list[str]:
    return list(set([especie['nombre_com'] for especie in lista_arboles]))


def especimen_mas_inclinado(lista_arboles: list[dict]) -> dict:
    especie_mas_inclinada = dict({ 'dummy': 0 }) # Valor dummy para tener un valor inical
    
    for especie in especies(lista_arboles=lista_arboles):
        inclinaciones = obtener_inclinaciones(lista_arboles=lista_arboles, especie=especie)
        max_inclinacion = max(inclinaciones)
        if list(especie_mas_inclinada.values())[0] < max_inclinacion:
            especie_mas_inclinada = { especie: max_inclinacion }
    
    return especie_mas_inclinada


def especie_promedio_mas_inclinada(lista_arboles: list[dict]) -> dict:
    especie_mas_inclinada_prom = dict({ 'dummy': 0 }) # Valor dummy para tener un valor inical
    
    for especie in especies(lista_arboles=lista_arboles):
        inclinaciones = obtener_inclinaciones(lista_arboles=lista_arboles, especie=especie)
        max_inclinacion = sum(inclinaciones) / len(inclinaciones)
        if list(especie_mas_inclinada_prom.values())[0] < max_inclinacion:
            especie_mas_inclinada_prom = { especie: max_inclinacion }
    
    return especie_mas_inclinada_prom


def ejemplar_mas_x(lista_arboles: list[dict], col: str) -> dict:
    ejemplar = dict()
    
    for arbol in lista_arboles:
        if (len(ejemplar) == 0):
            ejemplar = arbol
        else:
            if ejemplar.get(col) < arbol.get(col):
                ejemplar = arbol
    
    return ejemplar


def medidas_de_especies(especies, arboleda):
    return {
        especie:
            [
                (float(arbol.get('altura_tot')), float(arbol.get('diametro')))
                for arbol in arboleda
                if arbol.get("nombre_com") == especie
            ]
        for especie in especies
    }

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
especie = 'Jacarandá'
for parque in parques:
    parque_arbolado = leer_parque(nombre_archivo='./Data/arbolado-en-espacios-verdes.csv', parque=parque)
    [max_altura, prom_altura] = obtener_alturas(lista_arboles=parque_arbolado, especie=especie)
    especie_mas_inclinada = especimen_mas_inclinado(lista_arboles=parque_arbolado)
    especie_mas_inclinada_prom = especie_promedio_mas_inclinada(lista_arboles=parque_arbolado)
    print(f'En {parque}:', contar_ejemplares(parque_arbolado))
    print(f'Máxima altura de los {especie}: {max_altura:.2f}')
    print(f'Altura promedio de los {especie}: {prom_altura:.2f}')
    print(f'Especie más inclinada es {list(especie_mas_inclinada.keys())[0]} con {list(especie_mas_inclinada.values())[0]}')
    print(f'Especie más inclinada promedio es {list(especie_mas_inclinada_prom.keys())[0]} con {list(especie_mas_inclinada_prom.values())[0]}\n')




arboleda = leer_arboles(nombre_archivo='./Data/arbolado-en-espacios-verdes.csv')
mas_inclinado = ejemplar_mas_x(lista_arboles=arboleda, col='inclinacio')
print(f'Ejemplar más inclinado: {mas_inclinado.get("nombre_com")} ({mas_inclinado.get("lat")}, {mas_inclinado.get("long")})')
mas_alto = ejemplar_mas_x(lista_arboles=arboleda, col='altura_tot')
print(f'Ejemplar más alto: {mas_alto.get("nombre_com")} ({mas_alto.get("lat")}, {mas_alto.get("long")})')


alturas_jaracaranda = [float(arbol.get('altura_tot')) for arbol in arboleda if arbol.get("nombre_com") == "Jacarandá"]
alts_incs_jaracaranda = [
    (float(arbol.get('altura_tot')), float(arbol.get('diametro')))
    for arbol in arboleda
    if arbol.get("nombre_com") == "Jacarandá"
]

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas_de_especies(especies=especies, arboleda=arboleda)