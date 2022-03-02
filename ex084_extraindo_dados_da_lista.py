num = []
while True:
    num.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in 'NS':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break
print('--' * 30)
print(f'Você digitou {len(num)} números.')
num.sort(reverse=True)
print(f'Valores digitados em ordem decrescente: {num}')
if 5 in num:
    print(f'O número 5 foi digitado {num.count(5)} vezes.')
else:
    print('O 5 não foi digitado nenhuma vez.')

