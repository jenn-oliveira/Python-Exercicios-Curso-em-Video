s = float(input('Qual o salário do funcionário? R$ '))
s1 = s * 0.15
s2 = s * 0.10
if s <= 1250:
    print('Com aumento de 15% seu salário será: R${:.2f}'.format(s+s1))
else:
    print('Com aumento de 10% seu salário será: R${:.2f}'.format(s+s2))