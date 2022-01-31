km = float(input('Quantos km terá sua viagem? '))
p1 = km * 0.50
p2 = km * 0.45
if km <= 200:
    print('O valor da passagem será R${:.2f}.'.format(p1))
else:
    print('O valor da passagem será R${:.2f}.'.format(p2))