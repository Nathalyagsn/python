soma = 0

for c in range(1, 7):
    numeros = int(input('Digite um valor: '))
    if numeros % 2 == 0:
        soma += numeros

print(f'A soma dos números pares foram: {soma}')    
