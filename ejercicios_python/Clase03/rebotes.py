# Ejercicio 1.5: La pelota que rebota
# Ejercicio 3.10: Parámetros por omisión

import sys

try:
    metros = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    rebotes = 0
    CANT_REBOTES = 10
    DESGASTE = 0.6

    while rebotes < CANT_REBOTES:
        metros = metros * DESGASTE
        rebotes += 1
        print(rebotes, round(metros, 4))
except ValueError:
    print('Debe ingresar un valor numérico. Se omite la ejecución del programa...')