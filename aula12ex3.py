print('\033[32m-' * 23)
print(' MAIOR, MENOR OU IGUAL ')
print('-' * 23)
n1 = int(input('\033[mDigite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}!')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}!')
else:
    print('Não existe valor maior, os dois são iguais.')