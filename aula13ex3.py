s = 0
cont = 0
n = int(input('\033[32mDigite um número que quer saber a tabuada: \033[m'))
for c in range(n, n*11, n):
    s = s + n
    cont = cont + 1
    print(f'{n} X {cont} = {s}')

# RESOLUÇÃO DO GUANABARA COM APENAS 3 LINHAS:
# for c in range(1, 11):
#    print(f'{n} X {c:2} = {n*c}')