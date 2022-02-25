c = s = mulher = 0
while True:
    print(''' --------------------------------
       CADASTRE UMA PESSOA
 --------------------------------''')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
        cont = ' '
    while cont not in "SN":
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        c += 1
    if sexo in 'M':
        s += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    if cont in 'N':
        break
print('--------------------------------')
print(f'Maiores de 18 anos: {c} pessoas.')
print(f'Total de homens cadastrados: {s}')
print(f'Mulheres com menos de 20 anos: {mulher}')