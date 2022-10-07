# Ejercicio 7.11: Búsqueda binaria
# Ejercicio 7.12: Insertar un elemento en una lista

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    if pos != -1:
        return pos
    
    return medio if lista[medio] > x else medio + 1


def insertar(lista: list, elemento: int) -> int:
    pos = donde_insertar(lista=lista, x=elemento)
    if elemento not in lista:
        lista.insert(pos, elemento)
    return pos


# listarda = [0,2,4,6]
# print(insertar(lista=listarda, elemento=3)) # 2
# print(insertar(lista=listarda, elemento=4)) # 2