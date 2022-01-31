d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}KM'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da passagem será R${:.2f}'.format(preço))