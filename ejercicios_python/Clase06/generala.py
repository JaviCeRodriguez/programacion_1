# Ejercicio 6.1: Generala servida
# Ejercicio 6.2: Generala no necesariamente servida

from collections import Counter
from random import randint


def tirar(dados: int) -> list[int]:
    return [randint(1, 6) for _ in range(dados)]


def es_generala(dados: list[int]) -> bool:
    return len(set(dados)) == 1


def prob_generala(N: int) -> float:
    G = 0
    for _ in range(N):
        mano = 0
        dado = {
            "target": None,
            "cantidad": 0
        }
        while mano < 3 and dado['cantidad'] != 5:
            dados = tirar(dados=5 - dado['cantidad'])
            dados_counter = Counter(dados)
            if mano == 0 and dado['target'] is None:
                dado_mc = dados_counter.most_common(1)
                dado['target'] = dado_mc[0][0]
                dado['cantidad'] += dado_mc[0][1]
            else:
                cant = dados_counter.get(dado['target'])
                if cant is not None:
                    dado['cantidad'] += cant
            mano += 1
        if dado['cantidad'] == 5:
            G += 1
    return G/N


N = 100000
G = sum([es_generala(tirar(dados=5)) for _ in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.\n')

prob_3manos = prob_generala(N=N)
print(f'Probabilidad con hasta 3 manos, con {N} tiros: {prob_3manos:.6f}.')