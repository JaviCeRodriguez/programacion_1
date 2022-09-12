# Ejercicio 1.18: Geringoso rústico

cadena = input('Ingrese una cadena: ')
capadepenapa = ''

if not bool(cadena):
    cadena = 'Geringoso'

for c in cadena:
    capadepenapa += c
    if c in 'aeiou':
        capadepenapa += 'p' + c

print(capadepenapa)

# Input: boligoma
# Output: bopolipigopomapa