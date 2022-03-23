galera = list()
dado = list()
p = maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    p += 1
    cont = ' '
    while cont not in "SN":
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break

print(f'Pessoas cadastradas {p}')
print(f'A pessoa mais pesada tem {maior}kg', end=' ')
for pe in galera:
    if pe[1] == maior:
        print(f'{pe[0]}', end=' ')
print()
print(f'A pessoa mais leve tem {menor}kg', end=' ')
for pe in galera:
    if pe[1] == menor:
        print(f'{pe[0]}', end=';')
print()