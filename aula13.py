from time import sleep
print('''\033[35mFOGOS\033[m \033[36mDE\033[m \033[33mARTIFÍCIO\033[m
\033[32m[ 1 ]\033[m ACENDER OS FOGOS
\033[31m[ 2 ]\033[m NÃO ACENDER(NADA ACONTECE)''')
op = int(input('\033[37mEscolha Sua Opção: \033[m'))
if op == 1:
        for c in range(10, -1, -1):
                sleep(1)
                print(c)
        print('\033[33mBOOOOMMMM!!!\033[m🎆')
        print('\033[35mMAS QUE ESTOURO FOI ESSE!!\033[m😱')
elif op == 2:
        print('\033[35mCOMO VOCÊ É MEDROSO EM 😒')
        exit()
else:
        print('\033[31mOPÇÃO INVÁLIDA, ACENDA NOVAMENTE!')