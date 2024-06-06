from time import sleep
s = 0
maior = 0
multiplicar = 0
print('\033[32m-' * 31)
n1 = int(input('\033[mPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
print('\033[32m-' * 31)
opq = False
while not opq:
    print('''\033[m    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    print('\033[32m-' * 31)
    r = int(input('\033[mQual é a sua opção? '))
    if r == 1:
        s = n1 + n2
        print(f'A soma entre {n1} + {n2} é {s}')
        print('\033[32m-' * 31)
    if r == 2:
        multiplicar = n1 * n2
        print(f'{n1} X {n2} é igual a {multiplicar}')
        print('\033[32m-' * 31)
    if r == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é {maior}')
            print('\033[32m-' * 31)
        if n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}')
            print('\033[32m-' * 31)
        elif n1 == n2:
            print('Os dois valores são iguais.')
            print('\033[32m-' * 31)
    if r == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('\033[32m-' * 31)
        opq = False
    if r == 5:
        print('Finalizando...')
        sleep(1.3)
        print('\033[32m-' * 31)
        print('\033[mFim do programa. Até mais!')
        opq = True
    elif r > 5 or r == 0:
        print('\033[31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE\033[m')
        print('\033[32m-' * 31)

'''RESOLUÇÃO DO GUANABARA:

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(''''''     [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA'''''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} é igual a {produto}')
    elif opção == 3:
        if n1 > n2
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')'''