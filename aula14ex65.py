resp = 'S'
s = m = cont = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = s / cont
print(f'Você digitou {cont} números e a média foi {m}')
print(f'O maior valor foi {maior} e o menor foi {menor}')