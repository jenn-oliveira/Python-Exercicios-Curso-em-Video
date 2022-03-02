brasileirão = 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', \
              'Bragantino', 'Fluminense', 'América', 'Atlético', 'Santos', 'Ceará', \
              'Internacional', 'São Paulo', 'Athetlico Paranaense', 'Cuiabá', 'Juventude', \
              'Grêmio', 'Bahia', 'Sport', 'Chapecoense'
print(f'Lista de times no Brasileirão 2021 série A: {brasileirão}')
print('-----' * 62)
print(f'Os 5 primeiros : {brasileirão[0:5]}')
print('-----' * 62)
print(f'Os 4 últimos: {brasileirão[-4:]}')
print('-----' * 62)
print('Times em ordem alfabética: ', sorted(brasileirão))
print('-----' * 62)
print('O time da Chapecoense encontra-se na posição:', brasileirão.index('Chapecoense')+1, 'posição')
