#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
# Ejercicio 3.5: Semántica
"""
Comentario: El error estaba en el condicional. Es suficiente con un 'if' que retorne
True si detecta el caracter 'a'. Solo debería devolver False si hace todas las
iteraciones posibles en el while (o sea, no existe 'a')
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.6: Sintaxis
"""
Comentario: Había varios errores:
    - Faltaban los ':' en el def, while e if
    - En el condicional if, faltaba un '='
    - El segundo return tenía un typo, era 'False', no 'Falso'
"""
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.7: Tipos
"""
Comentario: 1984 no es del tipo string. Se soluciona agregando un try-except, 
imprimiendo en consola información al respecto.
"""
def tiene_uno(expresion):
    try:
        n = len(expresion)
        i = 0
        tiene = False
        while (i < n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print(f'El argumento {repr(expresion)} no es del tipo str:', type(expresion))


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
# Ejercicio 3.8: Alcances
"""
Comentario: La variable 'c' dentro de 'suma' no es global. Se retorna y se guarda en
la variable 'c' que está fuera de 'suma'
"""
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.9: Pisando memoria
"""
Comentario: Lo que sucede acá es que al appendear la variable registro en
la lista camion, siempre lo hace contra la propia variable registro, no con
los nuevos valores. Esto pasa porque 'registro' está asignado en algún lugar
de memoria y solo se actualizaba.

O sea, sucedía esto:
camion = [registro, registro, registro, registro, registro]
y cada registro es el mismo. Se soluciona con cambiar el lugar de asignación
dentro del while.
"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('./Data/camion.csv') # Ojo con la ruta!
pprint(camion)