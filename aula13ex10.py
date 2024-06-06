cont = 0
maior = 0
nome = ''
m = 0
mcm20 = 0
for p in range(1, 5):
    cont += 1
    print(f'----- {cont}ª PESSOA -----')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    m += i
    if p == 1 and s in 'Mm':
        maior = i
        nome = n
    if s in 'Mm' and i > maior:
        maior = i
        nome = n
    if s in 'Ff' and i < 20:
        mcm20 += 1
    elif s in 'qwertyuiopasdghjlkçzxcvbn':
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
        exit()
print('\033[32m-\033[m' * 50)
print(f'A média de idade do grupo é de {m/4}')
print(f'O homem mais velho tem {maior} anos e se chama {nome}.')
print(f'Ao todo são {mcm20} mulheres com menos de 20 anos')
print('\033[32m-\033[m' * 50)