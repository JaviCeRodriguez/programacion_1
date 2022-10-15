# Ejercicio 8.10: Funciones y documentación

def valor_absoluto(n: int) -> int:
    """
    Calcula el valor absoluto de un número
    
    ---
    - Precondicion: n es un numero entero
    - Poscondicion: devuelve el valor absoluto de n
    """

    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l: list[int]) -> int:
    """
    Suma los elementos pares de una lista

    ---
    - Precondicion: l es una lista de numeros enteros
    - Poscondicion: devuelve la suma de los elementos pares de l
    """

    res = 0 # Invariante
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

    # res es invariante


def veces(a: int, b: int) -> int:
    """
    Calcula la multiplicacion de dos numeros

    ---
    - Precondicion: a y b son numeros enteros
    - Poscondicion: devuelve el producto de a y b
    """

    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

    # res y nb son invariante


def collatz(n: int) -> int:
    """
    Calcula la secuencia de Collatz de un numero
    
    ---
    - Precondicion: n es un numero entero
    - Poscondicion: devuelve la secuencia de Collatz de n
    """

    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

    # res es invariante