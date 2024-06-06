from random import randint
from time import sleep
lista = 'PEDRA', 'PAPEL', 'TESOURA'
computador = randint(0, 2)
print('\033[32m=' * 36)
print('   GAME:   PEDRA, PAPEL E TESOURA   ')
print('=' * 36)
c = str(input('\033[mQUER MESMO JOGAR CONTRA MIM? \033[32m[s]\033[m ou \033[31m[n]\033[m '))
if c in 's' or c in 'S':
    print('\033[32mINICIANDO...\033[m')
elif c in 'n' or c in 'N':
    print('\033[35mTA BOM, VOCÊ NÃO IA GANHAR MESMO!')
    exit()
else:
    print('\033[31mOPÇÃO INVÁLIDA!')
    exit()
sleep(1.3)
print('''\033[34mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada?\033[m '))
if jogada != 0 and jogada != 1 and jogada != 2:
    print('\033[31mJOGADA INVÁLIDA! TENTE NOVAMENTE!\033[m')
    exit()
print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
print('\033[32m-=\033[m' * 18)
print(f'O COMPUTADOR ESCOLHEU {lista[computador]}')
print(f'O JOGADOR ESCOLHEU {lista[jogada]}')
print('\033[32m-=\033[m' * 18)
if jogada == computador:
    print('\033[33mEMPATE!\033[m')
elif jogada == 0 and computador == 2:
    print('\033[32mJOGADOR VENCE!\033[m VOCÊ DEU SORTEE, VAMOS DE NOVO? 🤔')
elif jogada == 0 and computador == 1:
    print(f'\033[31mJOGADOR PERDE!\033[m EU SOU MUITO BOM MESMO! 😎')
elif jogada == 1 and computador == 0:
    print('\033[32mJOGADOR VENCE!\033[m ESSA EU DEIXEI 😒')
elif jogada == 1 and computador == 2:
    print('\033[31mJOGADOR PERDE!\033[m JAJÁ DEIXO VOCÊ JOGAR 😁 ')
elif jogada == 2 and computador == 1:
    print('\033[32mJOGADOR VENCE!\033[m A PRÓXIMA EU GANHO 😏')
elif jogada == 2 and computador == 0:
    print('\033[31mJOGADOR PERDE!\033[m QUE TAL NA PRÓXIMA?')