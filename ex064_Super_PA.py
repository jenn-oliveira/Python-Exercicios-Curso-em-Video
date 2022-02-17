print('PROGRESSÃO ARITMÉTICA')
print('=' * 22)
t = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
