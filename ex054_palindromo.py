f = str(input("Digite uma frase: ")).strip().upper()
p = f.split()
j = ''.join(p)
print('Você digitou a frase: {}'.format(j))
'''i = '''''
i = j[::-1]
'''for letra in range(len(j)-1, -1, -1):
    i += j[letra]'''
print('O inverso de {} é {}'.format(j,i))
if i == j:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')