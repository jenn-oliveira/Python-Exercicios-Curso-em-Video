v = int(input("Digite sua velocidade atual em km: "))
multa = (v-80)*7
if v > 80:
    print('VOCÊ EXCEDEU 80KM/H E FOI MULTADO NO VALOR DE R${:.2F}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
