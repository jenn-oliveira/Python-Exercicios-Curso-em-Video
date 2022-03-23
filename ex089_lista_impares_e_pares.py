num = [[], []]
v = 0
for c in range(0,7):
    v = int(input(f'Digite o {c+1}º número: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)
num[0].sort()
num[1].sort()
print(f'Os números pares digitados foram {num[0]}')
print(f'Os números impares digitados foram {num[1]}')