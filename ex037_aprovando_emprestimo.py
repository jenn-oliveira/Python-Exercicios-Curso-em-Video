print('----- BEM VINDO(A) A SIMULAÇÃO DE EMPRÉSTIMOS MOBILIARIOS -----')
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário mensal do comprador? R$'))
t = float(input('Em quantos anos de financiamento?'))
total = casa / (t*12)
print('O valor da parcela mensal do imóvel será de R${:.2f}'.format(total))
if total >= sal * 0.30:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO APROVADO')
print('Obs: Para aprovação o valor da parcela deve ser menor do que 30% do seu salário atual.')