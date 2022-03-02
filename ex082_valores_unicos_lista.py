num = []
while True:
    n = (int(input('Digite um valor: ')))
    cont = ' '
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado.')
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]- ')).upper().strip()[0]
    if cont in 'N':
        break
num.sort()
print(f'Você digitou os valores {num}')