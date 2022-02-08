print('----- DESCUBRA SEU IMC -----')
n1 = float(input('Digite seu peso: '))
n2 = float(input('Digite sua altura: '))
imc = n1 / (n2 ** 2)
if imc < 18.5:
    print('MAGREZA')
elif imc == 18.5 or imc < 25:
#elif 18.5 <= imc < 25:
    print('NORMAL')
elif imc == 25 or imc < 30:
    print('SOBREPESO')
elif imc == 30 or imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
print('Seu IMC é:{:.2f}'.format(imc))
