from random import randint
v = 0
while True:
    n = int(input('Escolha um número: '))
    pc = randint(0, 10)
    s = n + pc
    tipo = ' '
    while tipo not in "IP":
        tipo = str(input('Par ou Impar? [P ou I] ')).upper().strip()[0]
    print(f'Você escolheu {n} e o computador {pc}\nTOTAL: {s}', end=' ')
    print('É PAR' if s % 2 == 0 else 'É IMPAR')
    if tipo == 'P':
        if s % 2 == 0:
            print('*** VOCÊ VENCEU *** ')
            v += 1
        else:
            print('--- VOCÊ PERDEU ---')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('*** VOCÊ VENCEU *** ')
            v += 1
        else:
            print('--- VOCÊ PERDEU ---')
            break
    print('Vamos jogar novamente...')
print(f'     GAME OVER\nNúmeros de vitórias: {v}')