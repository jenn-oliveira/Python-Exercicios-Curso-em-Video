n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', \
    'dezesseis', 'dezssete', 'dezoito', 'dezenove', 'vinte'
n1 = int(input('Digite um número entre 0 e 20: '))
for cont in range (n1, len(n)):
    print(f'Você digitou o número: {n[cont]}')
    break
    if n1 != n:
        input('Digite um número válido entre 0 e 20: ')