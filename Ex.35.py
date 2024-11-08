lado1 = float(input('Qual o tamanho do primeiro lado? '))
lado2 = float(input('Qual o tamanho do segundo lado? '))
lado3 = float(input('Qual o tamanho do terceiro lado? '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Esses segmentos formam um triangulo.')

else:
    print('Esse segmentos não formam um triangulo')