# Ejercicio 4.12: Tablas de multiplicar

stop = 10

print(' ' * 2, end=' ')

for x in range(stop):
    print(f'{x:>4d}', end='')

print('\n', '-' * 44)

for i in range(stop):
    print(f'{str(i)+":":>3}', end=' ')
    sum_aux = 0
    for j in range(stop):
        print(f'{sum_aux:>3d}', end=' ')
        sum_aux += i
    print('')