n = int(input('\033[34mDigite um número para calcular seu fatorial: \033[m'))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

'''RESOLUÇÃO COM 4 LINHAS:
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''

'''RESOLUÇÃO USANDO LAÇO FOR:
n = int(input('Digite um número para calcular seu fatorial: '))
acumulador = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    acumulador *= c
    if c > 1:
        print(f'{c} x ', end='')
    else:
        print(f'{c} = ', end='')
print(acumulador)'''