prod = ('Notebook', 2.500, 'TV Smart', 1.800, 'Iphone 13', 9.567,
        'Som JBL', 1787, 'Soundbar', 2.356, 'Roteador', 251,
        'Projetor', 578, 'Mouse sem fio', 86, 'Teclado gamer', 98)
print('-' * 42)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 42)
for pos in range(0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end='')
    else:
        print(f'R${prod[pos]:>8.2f}')
print('-' * 42)