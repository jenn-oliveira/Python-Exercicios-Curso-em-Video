from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n = 0
while n != 5:
    n = int(input('''    OPÇÕES:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ESCOLHA UMA FUNÇÃO: '''))
    if n == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif n == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif n == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif n == 4:
        n1 = int(input('Informe o números novamente\nDigite um número: '))
        n2 = int(input('Digite outro número: '))
    elif n == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('-*-' * 10)
    sleep(1)
print('Fim do programa!')