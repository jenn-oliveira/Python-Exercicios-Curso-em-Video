from random import choice
n = int(0)
n1 = int(1)
n2 = int(2)
n3 = int(3)
n4 = int(4)
n5 = int(5)
lista = [n,n1,n2,n3,n4,n5]
escolhido = choice(lista)
n6 = int(input('Descubra entre 0 a 5 o número escolhido pelo computador: '))
if escolhido == n6:
    print('O número escolhido pelo computador foi: {} \nPARABÉNS, VOCÊ VENCEU!'.format(escolhido))
else:
    print('O número escolhido pelo computador foi: {} \nNÃO FOI DESSA VEZ, VOCÊ PERDEU!'.format(escolhido))
