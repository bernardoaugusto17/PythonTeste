t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p = t1
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(p, end=' → ')
        cont += 1
        p += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\033[32m-' * 46)
print(f'\033[mProgressão finalizada com {total} termos mostrados.')