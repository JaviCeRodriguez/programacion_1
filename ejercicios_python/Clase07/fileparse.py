# Ejercicio 7.3: Parsear un archivo CSV
# Ejercicio 7.4: Selector de Columnas
# Ejercicio 7.5: Conversión de tipo
# Ejercicio 7.6: Trabajando sin encabezados
# Ejercicio 7.7: Importar módulos

import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''

    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows) # Lee los encabezados

        if select:
            indices = [headers.index(name_col) for name_col in select]
        else:
            indices = []

        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[idx] for idx in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            registro = dict(zip(headers, row)) if has_headers else tuple(row)
            registros.append(registro)

    return registros