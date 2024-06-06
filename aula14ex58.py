from random import randint
cont = 1
print('\033[32m-' * 50)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? 🤔')
print('-' * 50)
n = int(input('\033[mQual é seu palpite? '))
escolhido = randint(0, 10)
while n != escolhido:
    cont += 1
    if n > escolhido:
        print('menos... Tente mais uma vez.')
        n = int(input('Qual é seu palpite? '))
    else:
        print('Mais... Tente mais uma vez.')
        n = int(input('Qual é seu palpite? '))
    if n == escolhido:
        print('\033[32m-' * 50)
        print(f'Parabéns você acertou o número que eu escolhi!\nForam necessários {cont} palpites para vencer!')
        print('-' * 50)

'''RESOLUÇÃO DO GUANABARA:
from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')'''