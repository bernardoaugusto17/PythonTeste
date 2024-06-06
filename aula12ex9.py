print('\033[33m=' * 28)
print('          BN LOJAS          ')
print('=' * 28)
v = float(input('\033[mQual é o valor das compras? '))
print('''\033[34mESCOLHA A FORMA DE PAGAMENTO:
[ 1 ] A VISTA DINHEIRO/CHEQUE: (10% DE DESCONTO!)
[ 2 ] A VISTA NO CARTÃO: (5% DE DESCONTO!)
[ 3 ] EM ATÉ 2 VEZES NO CARTÃO: (PREÇO NORMAL)
[ 4 ] 3 VEZES OU MAIS NO CARTÃO: (COM 20% DE JUROS!)\033[m''')
op = int(input('\033[37mForma de pagamento: \033[m'))
if op == 1:
    t = v - (v*0.10)
    print(f'\033[32mO valor a vista fica: {t:.2f}R$\033[m')
elif op == 2:
    t = v - (v*0.05)
    print(f'\033[32mO valor a vista no cartão fica: {t:.2f}R$\033[m')
elif op == 3:
    t = v
    parcela = t / 2
    print(f'\033[32mSua compra será parcelada em 2x de {parcela:.2f}R$ no cartão\033[m')
elif op == 4:
    t = v + (v*0.20)
    tp = int(input('\033[35mQuantas parcelas? \033[m'))
    parcela = t / tp
    print(f'\033[32mSua compra será parcelada em {tp}x de {parcela:.2f}R$ COM JUROS!\033[m')
else:
    t = v
    print('\033[31mERRO! OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE!')
print(f'Sua compra de {v:.2f}R$ vai custar {t:.2f}R$ no final.')