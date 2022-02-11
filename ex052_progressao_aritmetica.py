t = int(input('Digite um termo: '))
r = int(input('Digite a razão: '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print(' {}'.format(c), end=' →')
print(' FIM')