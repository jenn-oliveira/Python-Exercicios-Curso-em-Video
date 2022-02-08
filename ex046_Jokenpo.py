from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''ESCOLHA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j1 = int(input('Sua escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print('O computador escolheu {}'.format(itens[pc]))
print('Você escolheu {}'.format(itens[j1]))
print('-=' * 15)
if pc == 0:
    if j1 == 0:
        print('EMPATE!')
    elif j1 == 1:
        print('VOCÊ VENCEU!')
    elif j1 == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1:
    if j1 == 0:
        print('COMPUTADOR VENCEU!')
    elif j1 == 1:
        print('EMPATE')
    elif j1 == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:
    if j1 == 0:
        print('VOCÊ VENCEU!')
    elif j1 == 1:
        print('COMPUTADOR VENCEU!')
    elif j1 == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')




