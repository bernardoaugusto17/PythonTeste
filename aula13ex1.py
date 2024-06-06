from time import sleep
q = int(input('Você quer contar os pares até quanto? '))
for c in range(2, q+2, 2):
    print(c, end=' ')
    sleep(0.5)
print('Acabou.')