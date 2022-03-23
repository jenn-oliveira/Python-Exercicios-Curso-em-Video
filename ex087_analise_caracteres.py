frase = str(input('Digite uma frase: ')).strip().upper()
caractere = str(input('Digite um caractere: ')).strip().upper()[0]
print('A letra {} apareceu na posição: '.format(caractere), end='')
for i, v in enumerate(frase):
    if v == caractere:
        print(f'{i+1}º,', end='')