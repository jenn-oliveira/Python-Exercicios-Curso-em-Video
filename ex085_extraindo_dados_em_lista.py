A = []
B = []
C = []
while True:
    A.append(int(input('Digite um número: ')))
    cont = ' '
    while cont not in 'NS':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break
for i, v in enumerate(A):
    if v % 2 == 0:
        B.append(v)
    else:
        C.append(v)
print(f'Valores digitados: {A}')
print(f'Valores pares digitados: {B}')
print(f'Valores impares digitados: {C}')


