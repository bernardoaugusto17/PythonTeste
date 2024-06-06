n = int(input('Digite um número [999 para parar]: '))
pn = n
s = sd = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    if n != 999:
        s += n
        sd = s + pn
print(f'Você digitou {cont} números e a soma entre eles foi {sd}.')