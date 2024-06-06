from time import sleep
print('\033[32m=' * 29)
print('     10 TERMOS DE UMA PA     ')
print('=' * 29)
t1 = int(input('\033[mPrimeiro termo: '))
r = int(input('Razão: '))
for c in range(t1, t1+10*r, r):
    print(c, end=' → ')
    sleep(0.5)
print('ACABOU')