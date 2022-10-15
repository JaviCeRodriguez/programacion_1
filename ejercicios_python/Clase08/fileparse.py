# Ejercicio 7.3: Parsear un archivo CSV
# Ejercicio 7.4: Selector de Columnas
# Ejercicio 7.5: Conversión de tipo
# Ejercicio 7.6: Trabajando sin encabezados
# Ejercicio 7.7: Importar módulos
# Ejercicio 8.1: Lancemos excepciones
# Ejercicio 8.2: Atrapemos excepciones
# Ejercicio 8.3: Errores silenciados
# Ejercicio 8.6: De archivos a "objetos cual archivos"
# Ejercicio 8.7: Arreglemos las funciones existentes

import csv
import gzip

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''

    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados')

    # Hago la lectura de archivos de esta forma para evitar
    # modificar las funciones de otros archivos. Me parece mejor 👉🏽👈🏽
    file = open(nombre_archivo, 'rt')
    if nombre_archivo.endswith('.gz'):
        file = gzip.open(nombre_archivo, 'rt')
        
    rows = csv.reader(file)
    if has_headers:
        headers = next(rows) # Lee los encabezados

    if select:
        indices = [headers.index(name_col) for name_col in select]
    else:
        indices = []

    registros = []
    for idx, row in enumerate(rows):
        if not row:    # Saltea filas sin datos
            continue
        if indices:
            row = [row[idx] for idx in indices]
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {idx + 1}: No pude convertir {row}')
                print(f'Fila {idx + 1}: Motivo: {e}')
        registro = dict(zip(headers, row)) if has_headers else tuple(row)
        registros.append(registro)
    
    file.close()
    return registros
