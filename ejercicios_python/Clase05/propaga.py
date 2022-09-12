# Ejercicio 5.6: Propagación

def recorrer_lista(lista: list) -> tuple:
    lista_base = []
    propaga = False
    for idx, l in enumerate(lista):
        if len(lista_base) == 0: # Primer elemento
            lista_base.append(l)
        elif idx == len(lista) - 1: # Último elemento
            lista_base.append(l)
        else: # Elementos del medio
            if l == 1 and lista_base[-1] == 0: # Chequeo si el anterior es 0 y el actual es 1
                lista_base = lista_base[:-1] + [1] + [l]
                propaga = True
            else:
                lista_base.append(l)
    return (lista_base, propaga)

def propagar(lista: list) -> list:
    new_lista = lista
    listo = True
    while listo:
        (new_lista, propaga_1) = recorrer_lista(new_lista)
        (new_lista, propaga_2) = recorrer_lista(new_lista[::-1])
        new_lista = new_lista[::-1]
        listo = propaga_1 or propaga_2
    return new_lista

print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])) # [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0, 1, 0, 0])) # [ 1, 1, 1, 1, 1, 1]