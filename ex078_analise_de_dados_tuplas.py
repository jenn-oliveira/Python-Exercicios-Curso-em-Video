val = int(input('Digite um número: ')), int(input('Digite outro número: ')),\
     int(input('Digite mais um número: ')), int(input('Digite mais um número: '))
print(f'Você digitou os números: {val}')
print('O número 9 apareceu:', val.count(9), 'vezes')
if 3 in val:
     print(f'O primeiro número 3 está na posição: {val.index(3)+1}ª')
else:
     print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares são: ',end='')
for n in val:
     if n % 2 == 0:
          print(n, end=',')