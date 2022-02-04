from random import randint
from time import sleep
pc = randint(0, 5)
print('-*-' * 15)
print('Estou pensando em um número entre 0 e 5. \nTente adivinhar')
print('-*-' * 15)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI HAHA! Eu pensei no número {} e não no {}.'.format(pc,jogador))