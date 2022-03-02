pal = ('Python', 'Programador', 'Desenvolvedor', 'Aprendiz', 'Senior', 'Junior',
       'Estagiario', 'Tecnologia', 'Futuro', 'Linguagem', 'Codificacao', 'Estudos')
print('-' * 40)
print(f'{"Analisando vogais".upper():^38}')
print('-' * 40)
for p in pal:
    print(f'\nNa palavra \033[1;31m{p} \033[mtemos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
