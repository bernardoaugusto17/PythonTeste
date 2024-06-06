from datetime import date
atual = date.today().year
print('\033[32m-' * 23)
print('| ALISTAMENTO MILITAR |')
print('-' * 23)
s = str(input('\033[mQual é o seu sexo? [m] ou [f] '))
if s == 'm' or s == 'M':
    print('\033[37mCerto, continue preenchendo o formulário...\033[m')
elif s == 'f' or s == 'F':
    print('\033[31mVocê não precisa fazer o alistamento obrigatório!\033[m')
    deseja = str(input('Mesmo assim você deseja se alistar? [s] ou [n] '))
    if deseja in 's' or deseja in 'S':
        print('\033[37mCerto, continue preenchendo o formulário...\033[m')
    elif deseja in 'n' or deseja in 'N':
        print('\033[34mTUDO BEM, ATÉ MAIS!\033[m')
        exit()
    else:
        print('\033[31mERRO! ESSA OPÇÃO NÃO EXISTE!\033[m')
        exit()
else:
    print('\033[31mGênero inválido. Tente novamente\033[m')
    exit()
nasc = int(input('Ano de nascimento: '))
print('\033[32m-' * 45)
i = atual - nasc
print(f'\033[mQuem nasceu em {nasc} tem {i} ano(s) em {atual}')
if i == 18:
    print('\033[31mVocê deve se alistar IMEDIATAMENTE!')
elif i < 18:
    saldo = 18 - i
    print(f'Ainda falta(m) {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif i > 18:
    saldo = i - 18
    print(f'Você já deveria ter se alistado há {saldo} ano(s)!')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
print('\033[32m-' * 45)