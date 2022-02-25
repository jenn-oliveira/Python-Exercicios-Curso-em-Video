print('=' * 30)
print('{:^30}'.format('BANCO AMORA'))
print('=' * 30)
v = int(input('Qual valor deseja sacar? R$'))
total = v
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        totcéd = 0
        if total == 0:
            break
