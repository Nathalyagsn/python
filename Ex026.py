letras = str(input('Digite uma frase: '))
quantA = letras.count('a')
firstA = letras.find('a') + 1
lastA = letras.rfind('a') + 1

print(f'A letra A aparece: {quantA} vezes\nA primeira aparece na posição: {firstA}\nA ultima aparece na posição: {lastA}')