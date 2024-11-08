numero = int(input('Escolha um número: '))
binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)

print(f'A conversão de {numero} para Binário: {binario}\nOcatal:{octal}\nHexadecimal:{hexa}')