sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in "FfMm":
    sexo = str(input('Dado inválido! Por favor, informe seu sexo [M/F]: '))
print('Sexo {} registrado com sucesso!'.format(sexo))