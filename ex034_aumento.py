s = float(input('Qual o salário do funcionário? R$ '))
if s <= 1250:
    n = s + (s * 15 / 100)
    print('Com aumento de 15% seu salário será: R${:.2f}'.format(n))
else:
    n2 = s + (s * 10 / 100)
    print('Com aumento de 10% seu salário será: R${:.2f}'.format(n2))