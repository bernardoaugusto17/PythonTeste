soma = 0
cont = 0
print('\033[33mAVISO! Todos os valores somados serão ímpares e múltiplos de 3\033[m')
v = int(input('Digite um valor máximo: '))
for c in range(3, v+1, 2):
    if c % 3 == 0:
        cont += +1
        soma += + c
print(f'A soma de todos os {cont} valores solicitados é igual a {soma}')