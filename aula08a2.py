from math import lcm
n = int(input('\033[37mDigite um número que começe com 0: \033[m'))
d = lcm(n//1)
print(f'\033[35mO número {n} tem a parte inteira {d}')