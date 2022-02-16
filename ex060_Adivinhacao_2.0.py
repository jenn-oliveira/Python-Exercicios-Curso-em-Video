from random import randint
pc = randint(0, 10)
print('---- SOU SEU COMPUTADOR ----\nACABEI DE PENSAR EM UM NÚMERO \nTE DESAFIO A ADIVINHAR, HAHA!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites +=1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('AUMENTAAAAAAA ESSE PALPITE, HAHAHA')
        if jogador > pc:
            print('DIMINUIIIIIII ESSE PALPITE, HAHAHA')
print('ACERTOU COM {} TENTATIVAS.\n***** PARABÉNS *****'.format(palpites))
