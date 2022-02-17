print('PROGRESSÃO ARITMÉTICA')
print('=' * 22)
t = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
termo = t
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')