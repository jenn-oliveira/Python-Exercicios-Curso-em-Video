c = s = 0
while True:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Total de números digitados {c} e soma de todos é {s}.')