from math import sqrt
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
x = (oposto**2 + adjacente**2)
raiz = sqrt(x)

print(f'O comprimento da hipotenusa é: {raiz:.2f}')