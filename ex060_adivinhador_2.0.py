from random import randint
pc = randint(0, 10)
r = int(input('Digite um número entre 0 e 10: '))
palpites = 1
while r != pc:
    r = int(input('Você ainda não adivinhou. Tente outro número: '))
    palpites += 1
    if r < pc:
        print('MAAAAAIS... Tente novamente!')
    elif r > pc:
        print('MENOOOOOS... Tente novamente!')
print('O número sorteado foi {} e você escolheu {}. Parabéns você adivinhou com {} tentativas!'.format(pc,r, palpites))
