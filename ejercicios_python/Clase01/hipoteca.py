# Ejercicio 1.7: La hipoteca de David
# Ejercicio 1.8: Adelantos
# Ejercicio 1.9: Calculadora de adelantos
# Ejercicio 1.10: Tablas
# Ejercicio 1.11: Hipoteca ajustado

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = (saldo - pago_extra) * (1 + tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        pre_saldo = saldo * (1 + tasa/12) - pago_mensual
        if pre_saldo < 0:
            saldo = 0
            total_pagado = total_pagado + pago_mensual + pre_saldo
        else:
            saldo = pre_saldo
            total_pagado = total_pagado + pago_mensual
    mes += 1
    print(f'{mes:>4d} {total_pagado:>10.2f} {saldo:>10.2f}')

print(f'Total pagado {total_pagado:0.2f}')
print(f'Meses: {mes}')