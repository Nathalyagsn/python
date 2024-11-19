tot = 0
numero = int(input('Digite um número:'))

for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1

print(f'O número {numero} foi divisivel {tot} vezes.')

if tot == 2:
    print('É primo!')
else:
    print('Não é primo!')    