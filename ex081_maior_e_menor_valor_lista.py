valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}ª valor: ')))
print(f'Valores digitados: {valores}')
print(f'O maior valor foi {max(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {min(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
print()