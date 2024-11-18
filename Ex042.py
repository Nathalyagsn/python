primeiro = float(input('Qual o tamanho do primeiro lado? '))
segundo = float(input('Qual o tamanho do segundo lado? '))
terceiro = float(input('Qual o tamanho do terceiro lado? '))

if primeiro == segundo and primeiro == terceiro:
    print('Equilátero. Todos os lados são iguais.')

elif primeiro == segundo and primeiro != terceiro:
    print('Isósceles. Dois lados iguais, um diferente.')    

else:
    print('Escaleno. Todos os lados são diferentes.')    