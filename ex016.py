d = int(input('Por quantos dias alugou o carro? '))
km = float(input("Quantos km você percorreu com o carro? "))
total = (d * 60) + (km * 0.15)
print('Você deve pagar R${}'.format(total))