d = int(input('\033[35mQuantidade de dias alugados: \033[m'))
k = float(input('\033[33mQuantidade de km rodados: \033[m'))
a = (d * 60) + (0.15 * k)
print(f'O total a pagar é de \033[32mR${a:.2f}')
