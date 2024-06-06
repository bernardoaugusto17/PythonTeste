print('\033[34m-' * 17)
print(' PALÍNDROMO ')
print('-' * 17)
frase = str(input('\033[mDigite uma frase: '))
print(f'O inverso de {''.join(frase.upper().split())} é {''.join(frase.upper().split())[::-1]}')
if ''.join(frase.upper().split()) == ''.join(frase.upper().split())[::-1]:
    print('Temos um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo!')
# RESOLUÇÃO USANDO O LAÇO FOR:
# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
# if inverso == junto:
#    print('Temos um Palíndromo!')
# else:
#    print('A frase não é um Palíndromo!')