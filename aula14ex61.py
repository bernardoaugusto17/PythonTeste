print(' 10 TERMOS DE PA')
print('-=' * 10)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
p = t1
cont = 1
while cont <= 10:
    print(p, end=' → ')
    cont += 1
    p += r
print('FIM')