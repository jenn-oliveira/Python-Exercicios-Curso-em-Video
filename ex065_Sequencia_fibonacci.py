print('-' * 30)
print('SEQUENCIA FIBONACCI')
print('-' * 30)
t1 = 0
t2 = 1
t3 = int(input('Quantos termos deseja mostrar? '))
cont = 3
print('~' * 30)
print('{} → {}'.format(t1, t2), end='')
while cont <= t3:
    total = t1 + t2
    print(' → {}'.format(total), end='')
    t1 = t2
    t2 = total
    cont += 1
print(' → FIM')
print('~' * 30)

