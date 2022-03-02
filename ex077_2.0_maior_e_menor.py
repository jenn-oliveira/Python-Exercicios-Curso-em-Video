from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Valores sorteados: {n}')
print(f'Maior valor sorteado: {max(n)}')
print(f'Menor valor sorteado: {min(n)}')