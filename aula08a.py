from math import sqrt
n = int(input('\033[35mDigite um número: \033[m'))
raiz = sqrt(n)
print(f'A raiz de \033[32m{n}\033[m arredondada pra \033[34mcima\033[m é: {raiz.__ceil__()} \nA raiz de \033[32m{n}\033[m arredondada pra \033[31mbaixo\033[m é: {raiz.__floor__()}')
