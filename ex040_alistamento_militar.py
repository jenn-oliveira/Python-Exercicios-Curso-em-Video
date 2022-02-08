from datetime import date
print('----- DESCUBRA SE VOCÊ PRECISA SE ALISTAR -----')
n1 = int(input('Digite o ano de nascimento: '))
idade = date.today().year - n1
if idade <= 17:
    print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(18 - idade + date.today().year))
elif idade == 18:
    print('Aliste-se IMEDIATAMENTE!')
elif idade >= 19:
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(date.today().year - (idade - 18)))

