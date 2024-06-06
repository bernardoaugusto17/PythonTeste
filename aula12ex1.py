from time import sleep
print('\033[32m-' * 23)
print('| EMPRÉSTIMO BANCÁRIO |')
print('-' * 23)
vcasa = float(input('\033[mQual é o valor da casa? '))
s = float(input('Qual é o seu salário? '))
salario30 = s * 0.3
anos = int(input('Quantos anos de financiamento? '))
print('\033[35mVERIFICANDO...\033[m')
sleep(2)
meses = anos * 12
pmensal = vcasa / meses
if pmensal <= salario30:
    print(f'Para pagar uma casa de {vcasa:.2f}R$ em {anos} anos, a prestação será de {pmensal:.2f}R$\nEmpréstimo pode ser \033[32mCONCEDIDO!')
else:
    print(f'Para pagar uma casa de {vcasa:.2f}R$ em {anos} anos, a prestação será de {pmensal:.2f}R$\nEmpréstimo \033[31mNEGADO!')