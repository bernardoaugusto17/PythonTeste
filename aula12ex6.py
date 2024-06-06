from datetime import date
data = date.today().year
print('\033[36m-=-' * 14)
print('| CLASSIFICAÇÃO DE ATLETAS DE NATAÇÃO 🏊‍♂️|')
print('-=-' * 14)
nasc = int(input('\033[m''\033[37mEm que ano você nasceu?\033[m '))
i = data - nasc
print(f'Você tem {i} ano(s)')
if i <= 9:
    print('Sua categoria é: \033[36mMIRIM 👶')
elif i <= 14:
    print('Sua categoria é: \033[33mINFANTIL 🧒')
elif i <= 19:
    print('Sua categoria é: \033[35mJÚNIOR 🧑')
elif i <= 25:
    print('Sua categoria é: \033[32mSÊNIOR 👨')
else:
    print('Sua categoria é: \033[31mMASTER 👴')