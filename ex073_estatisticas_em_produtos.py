from time import sleep
c = menor = p = s = 0
barato = ''
while True:
    print('''--------------------------------
       CADASTRE SEUS PRODUTOS
 --------------------------------''')
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    p += 1
    s += preço
    cont = ' '
    while cont not in "SN":
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if preço > 1000:
        c += 1
    if p == 1 or preço < menor:
        menor = preço
        barato = prod
    if cont in 'N':
        break
print('\nFinalizando...')
sleep(1)
print('--------------------------------')
print(f'Total da compra: R${s:.2f} ')
print(f'{c} produtos custam mais de R$1000,00')
print(f'O produto mais barato é: {barato} custando R${menor:.2f}')
