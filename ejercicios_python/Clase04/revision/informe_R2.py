import csv 
def leer_camion(nombre_archivo): 
    f = open (nombre_archivo, 'rt', encoding='utf8') 
    rows = csv.reader(f) 
    headers = next(rows)  
    camion =  []   
    for row in rows: 
        dicc = {  
              'fruta' : row[0],
              'unidades' : int(row[1]), 
              'precio' : float(row[2])
            } 
        camion.append(dicc)  
    return(camion) 
camion_archivo = leer_camion('./Data/camion.csv')   
def leer_precios(nombre_archivo): 
    f = open (nombre_archivo, 'rt', encoding='utf8') 
    rows = csv.reader(f) 
    precios = []
    try: 
        for row in rows: 
            dicc = { 'producto' : row[0],
                    'precio_venta': row[1]}  
            precios.append(dicc)
    except IndexError: 
        pass
    return(precios)        
precios_archivo = leer_precios('./Data/precios.csv')  
def balance (archivo_1, archivo_2):  
    total_comprado = 0 
    recaudado_venta = 0 
    for i in camion_archivo: 
        total_comprado = total_comprado + int(i['unidades']) * float(i['precio']) 
        for s in precios_archivo: 
            if s['producto'] == i['fruta'] :
                recaudado_venta = recaudado_venta + int(i['unidades']) * float(s['precio_venta']) 
    ganancia= round(recaudado_venta - total_comprado, 1) 
    print('el total comprado es de', total_comprado) 
    print('recaudado en ventas es de', recaudado_venta)  
    print('la ganancia es de ', ganancia) 
    return(total_comprado) 
    return(recaudado_venta) 
    return(ganancia)
balance_llamar = balance(camion_archivo, precios_archivo)  
