from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
cont3 = 0
for c in range(1, 8):
    cont += 1
    d = int(input(f'Digite a data de nascimento da {cont}ª pessoa: '))
    i = atual - d
    if d <= 2003:
        cont2 += 1
    else:
        cont3 += 1
print('\033[32m-\033[m' * 45)
print(f'Ao todo tivemos {cont2} pessoas maiores de idade')
print(f'E também tivemos {cont3} pessoas menores de idade')
print('\033[32m-\033[m' * 45)
