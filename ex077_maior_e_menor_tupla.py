from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
sorteio = (n1, n2, n3, n4, n5)
print(f'Valores sorteados: {sorteio}')

maior = n5
if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    maior = n1
if n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    maior = n2
if n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    maior = n3
if n4 >= n2 and n4 >= n3 and n4 >= n1 and n4 >= n5:
    maior = n4

menor = n5
if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
    menor = n1
if n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
    menor = n2
if n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
    menor = n3
if n4 <= n2 and n4 <= n3 and n4 <= n1 and n4 <= n5:
    menor = n4

print(f'Maior valor sorteado: {maior}')
print(f'Menor valor sorteado: {menor}')