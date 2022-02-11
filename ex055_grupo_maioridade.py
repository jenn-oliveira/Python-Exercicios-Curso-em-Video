from datetime import date
t = 0
tmenor = 0
for c in range(1, 8):
    ano = int(input('Em que ano {}º pessoa nasceu: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        t += 1
    else:
        tmenor += 1
print('{} são maiores de idade.'.format(t))
print("{} são menores de idade.".format(tmenor))

