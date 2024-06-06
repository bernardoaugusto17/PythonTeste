from time import sleep
print('\033[36m-=-' * 6)
print(' CÁLCULO DE IMC ')
print('-=-' * 6)
p = float(input('\033[mQual é o seu peso? (kg) '))
a = float(input('Qual é a sua altura? (m) '))
if a > 3:
    a = a / 100
imc = p / (a ** 2)
print('\033[35mCÁLCULANDO...\033[m')
sleep(1.5)
print('\033[32m|STATUS|')
print('\033[32m-\033[m' * 18)
print(f'\033[37mO seu imc é: {imc:.2f}\033[m')
if imc < 18.5:
    print('\033[36mABAIXO DO PESO!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mPESO IDEAL!\033[m')
elif 25 <= imc < 30:
    print('\033[35mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[33mOBESIDADE\033[m')
else:
    print('\033[31mOBESIDADE MÓRBIDA! CUIDADO!\033[m')
print('\033[32m-' * 18)