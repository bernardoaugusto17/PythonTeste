print('\033[32m=' * 20)
print(' CALCULANDO A MÉDIA ')
print('=' * 20)
n1 = float(input('\033[mPrimeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média é: {m:.1f}')
if m < 5:
    print('Você está \033[31mREPROVADO!😞\033[m Estude mais!')
elif 7 > m >= 5:
    print('Você está de \033[33mRECUPERAÇÃO!\033[m')
elif m >= 7:
    print('Muito bem, você está \033[32mAPROVADO!😁👍\033[m')