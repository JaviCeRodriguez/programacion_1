# Ejercicio 1.18: Geringoso rústico
# Ejercicio 2.13: Diccionario geringoso.

lista_palabras = ['banana', 'manzana', 'mandarina']

def geringoso(lista_palabras: list) -> dict:
    capadepenapas = dict()

    for palabra in lista_palabras:
        capadepenapa = ''
        for c in palabra:
            capadepenapa += c
            if c in 'aeiou':
                capadepenapa += 'p' + c
        capadepenapas[palabra] = capadepenapa

    print(capadepenapas)

geringoso(lista_palabras)
