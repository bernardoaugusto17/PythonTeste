cont = 0
maior = 0
menor = 0
for p in range(1, 6):
    cont += 1
    peso = float(input(f'Digite o peso da {cont}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')