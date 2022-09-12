# Ejercicio 5.5: Invertir una lista

def invertir_lista(lista: list[any]) -> list:
    inv_lista = []
    for l in lista:
        # inv_lista.insert(0, l) # Forma sencilla
        inv_lista = [l] + inv_lista
    return inv_lista

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
