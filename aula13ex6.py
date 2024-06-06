cont = 0
print('\033[32m=' * 16)
print(' NÚMEROS PRIMOS ')
print('=' * 16)
n = int(input('\033[mDigite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
    print(c, end=' ')
print(f'\nO número {n} foi divisível {cont} vezes')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')