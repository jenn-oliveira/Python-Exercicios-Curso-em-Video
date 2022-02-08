p = int(input('Preço do produto R$'))
print('''Formas de pagamento:
[ 1 ] A VISTA (CHEQUE/DINHERO) - DESCONTO 10%
[ 2 ] A VISTA (CARTÃO) - DESCONTO 5%
[ 3 ] 2X NO CARTÃO - PREÇO NORMAL
[ 4 ] 3X OU MAIS NO CARTÃO - 20% DE JUROS''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('Você pagará R${} com 10% de desconto.'.format(p - p * 0.10))
elif opção == 2:
    print('Você pagará R${} com 5% de desconto.'.format(p - p * 5 / 100))
elif opção == 3:
    print('Você pagará 2x R${:.2f}.'.format(p/2))
elif opção == 4:
    vezes = int(input('Quantas vezes? '))
    print('Você pagará {}x R${:.2f} com 20% de juros.'.format(vezes,(p + p * 0.20)/vezes))
else:
    print('Opção inválida, escolha novamente!')