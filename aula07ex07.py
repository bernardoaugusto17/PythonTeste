L = float(input('Qual é a \033[33mlargura\033[m da parede? '))
a = float(input('Qual é a \033[31maltura\033[m da parede? '))
at = L * a / 2
print(f'A quantidade de tintas necessárias para pintar essa parede é de \033[34m{at:.1f}\033[m litros!')
