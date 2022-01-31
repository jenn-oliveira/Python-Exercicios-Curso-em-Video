n = int(input('Me diga um número qualquer: '))
r = n % 2
if r == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é impar!'.format(n))