print('\033[32m=' * 17)
print(' BASES NUMÉRICAS ')
print('=' * 17)
n = int(input('\033[mDigite um valor inteiro: '))
print('''Escolha uma das bases para conversão:
\033[31m[ 1 ]\033[m Converter para BINÁRIO
\033[33m[ 2 ]\033[m Converter para OCTAL
\033[36m[ 3 ]\033[m Converter para HEXADECIMAL''')
op = int(input('\033[35mSua opção: \033[m'))
if op == 1:
    print(f'{n} convertido para BINÁRIO é igual a {n:b}')
elif op == 2:
    print(f'{n} convertido para OCTAL é igual a {n:o}')
elif op == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {n:x}')
else:
    print('Opção inválida. Tente novamente.')