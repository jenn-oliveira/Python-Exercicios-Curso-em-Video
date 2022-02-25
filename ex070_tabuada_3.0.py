n = 'VOLTE SEMPRE!'
while True:
    print('-' * 30)
    t = int(input('Qual tabuada deseja? '))
    print('-' * 30)
    if t <= -1:
        print('----- PROGRAMA ENCERRADO -----')
        print(n.center(30))
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(t, c, t * c))





