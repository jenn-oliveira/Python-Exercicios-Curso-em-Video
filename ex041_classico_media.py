print(' ----- Descubra se foi aprovado(a) ----- ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
print('Sua média foi: {}'.format(m))
if m < 5.0:
    print('Você está reprovado(a)!')
elif m == 5.0 or m <= 6.9:
    print('Você está de recuperação!')
elif m > 6.9:
    print('Você está aprovado(a)!')