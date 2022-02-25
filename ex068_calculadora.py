from time import sleep
n = str(input('Qual o seu nome? '))
print(f'Muito prazer {n}!')
sleep(2)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
div = n1 // n2
print(f'Você escolheu {n1} e {n2}\nSoma: {s}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {m}')
print(f'Divisão: {d:.2f}')
print(f'Potência: {p}')
print(f'Divisão inteira: {div}')
print(f'Média: {(n1+n2)/2}')
print(f'Antecessor e sucessor de {n1}: {n1-1} e {n1+1}')
print(f'Antecessor e sucessor de {n2}: {n2-1} e {n2+1}')
print(f'Raiz quadrada de {n1}: {n1**(1/2)}')
print(f'Raiz quadrada de {n2}: {n2**(1/2)}')
