from datetime import date
print('----- Descubra sua classificação Nacional -----')
n1 = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - n1
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua classificação é: MIRIM!')
elif idade <= 14:
    print('Sua classificação é: INFANTIL!')
elif idade <= 19:
    print('Sua classificação é: JUNIOR!')
elif idade <= 25:
    print('Sua classificação é: SÊNIOR!')
else:
    print('Sua classificação é: MASTER!')