N = str(input('Digite um número: '))      #só funciona com exatamente 4 numeros
NS = N.replace("", " ")
NL = NS.split()
print(f'A milhar é: {NL[ 0 ]}')
print(f'A centena é: {NL[ 1 ]}')
print(f'A dezena é: {NL[ 2 ]}')
print(f'A uniadade é: {NL[ 3 ]}')