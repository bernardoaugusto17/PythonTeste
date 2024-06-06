a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if b + c > a and a + c > b and a + b > c:
    print('Os Segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo. ')
    exit()
if a == b == c:
    print('O triângulo formado é um EQUILÁTERO')
elif a == b or b == c or a == c:
    print('O triângulo formado é um ISÓSCELES')
elif a != b != c:
    print('O triângulo formado é um ESCALENO')