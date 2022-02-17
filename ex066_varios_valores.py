c = cont = soma = 0
c = int(input('Digite um número ou 999 para PARAR: '))
while c != 999:
    soma += c
    cont += 1
    c = int(input('Digite um número ou 999 para PARAR: '))
print('A soma de todos os valores digitados foi {}'.format(soma))
