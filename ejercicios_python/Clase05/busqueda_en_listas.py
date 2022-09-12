# Ejercicio 5.3: Búsquedas de un elemento
# Ejercicio 5.4: Búsqueda de máximo y mínimo

def buscar_u_elemento(lista: list, elemento: any) -> int:
    ultima = -1
    for idx, l in enumerate(lista):
        if l == elemento:
            ultima = idx
    return ultima


def buscar_n_elemento(lista: list, elemento: any) -> int:
    veces = 0
    for l in lista:
        if l == elemento:
            veces += 1
    return veces


def maximo(lista: list) -> int:
    max = lista[0]
    for l in lista:
        if l > max:
            max = l
    return max if max >= 0 else 0


def minimo(lista: list) -> int:
    min = lista[0]
    for l in lista:
        if l < min and min >= 0:
            min = l
    return min if min >= 0 else 0

print(f"\nPosición de última aparición")
print(buscar_u_elemento([1,2,3,2,3,4], 1)) # 0
print(buscar_u_elemento([1,2,3,2,3,4], 2)) # 3
print(buscar_u_elemento([1,2,3,2,3,4], 3)) # 4
print(buscar_u_elemento([1,2,3,2,3,4], 5)) # -1

print(f"\nCantidad de apariciones")
print(buscar_n_elemento([1,2,3,2,3,4], 1)) # 1
print(buscar_n_elemento([1,2,3,2,3,4], 2)) # 2
print(buscar_n_elemento([1,2,3,2,3,4], 3)) # 2
print(buscar_n_elemento([1,2,3,2,3,4], 5)) # 0

print(f"\nMaximo")
print(maximo([1,2,7,2,3,4])) # 7
print(maximo([1,2,3,4])) # 4
print(maximo([-5,4])) # 4
print(maximo([-5,-4])) #0

print(f"\nMínimo")
print(minimo([1,2,7,2,3,4])) # 7
print(minimo([1,2,3,4])) # 4
print(minimo([-5,4])) # 4
print(minimo([-5,-4])) #0