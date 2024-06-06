nome = str(input('Qual é o seu nome? '))
if nome == 'Bernardo':
    print('Que nome bonito você têm!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Santos Martins':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')