s = ''
sr = 0
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('\033[31mDados Inválidos! Por favor, informe novamente\033[m')
    sr = s
    if s == 'M' and s == 'F':
        sr = s
print(f'Sexo {sr} registrado com sucesso!')
# RESOLUÇÃO DO GUANABARA:
# s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# while s not in 'MmFf':
#    s = str(input('\033[31mDados inválidos!\033[m Por favor, informe seu sexo: ')).strip().upper()[0]
# print(f'Sexo {s} registrado com sucesso!')