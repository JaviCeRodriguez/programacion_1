#%%
# Ejercicio 3.4: Balances
import csv

def leer_camion (nombre_archivo):
    camion = []
    with open (nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in f:
            row = line.split(',')
            camion.append ((row[0], int(row[1]), float(row[2])))
        return camion    

camion = leer_camion ('./Data/camion.csv')         


import csv

def leer_precios (nombre_archivo):
    precios = dict ()
    with open (nombre_archivo , 'rt') as f:
        rows = csv.reader(f)
        for line in f:
            row = line.split(',')
            try:
                precios [row[0]] = float(row[1])
            except:
                continue                
    return precios       

precios =leer_precios ('./Data/precios.csv')
 
total_ventas = 0
total_camion= 0    
for nombre, cajones, precio in camion:
    total_camion += cajones*precio
    total_ventas += cajones*precios[nombre]


balance = total_ventas - total_camion
print (f'La ganancia total fue de: {round(balance, 2)}')

# La salida del programa es: "La ganancia total fue de: 15314.95"


