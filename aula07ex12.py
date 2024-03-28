p = float(input('\033[32mQual é o preço do produto? 💲 \033[m'))
d = p - (p*0.15)
a = p + (p*0.10)
print(f'O produto com pagamento á vista recebe \033[34m15%\033[m de desconto, passa a ser \033[32mR${d:.2f}\033[m \nO produto parcelado recebe \033[31m10%\033[m de aumento, passa a ser \033[32mR${a:.2f}\033[m')