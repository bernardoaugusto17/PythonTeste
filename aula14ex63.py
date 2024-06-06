print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
t1 = 0
t2 = 1
t = int(input('Quantos termos você quer mostrar? '))
print('~' * 35)
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= t:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~' * 35)