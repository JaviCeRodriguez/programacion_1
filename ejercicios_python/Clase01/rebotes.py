# Ejercicio 1.5: La pelota que rebota

metros = 100
rebotes = 0
CANT_REBOTES = 10
DESGASTE = 0.6

while rebotes < CANT_REBOTES:
    metros = metros * DESGASTE
    rebotes += 1
    print(rebotes, round(metros, 4))