import math
angulo = float(input('Digite um angulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O seno: {seno:.2f}\nConsseno: {cosseno:.2f}\nTangente: {tangente:.2f}')