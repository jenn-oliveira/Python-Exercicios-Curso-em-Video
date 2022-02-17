n = soma = cont = maior = menor = 0
r = 'S'
while r in "Ss":
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N] ')).strip()[0]
print('A média entre todos os números digitados é {:.2f}'.format(média))
print('Sendo o maior número {} e o menor {}.'.format(maior, menor))