n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', \
    'dezesseis', 'dezssete', 'dezoito', 'dezenove', 'vinte'
while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número: {n[n1]}')
    cont = ' '
    while cont not in "SN":
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('Obrigada por utilizar nosso programa.\nVolte sempre!')

