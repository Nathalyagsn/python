from random import randint
numeroJogador = int(input('Adivinhe o número de 0 a 5: '))
numeroMaquina = randint(0, 5)

if (numeroJogador) == numeroMaquina:
    print(f'Paranbéns! O número sorteado foi {numeroMaquina} e o seu {numeroJogador}')

else:
    print(f'Tente novamente! O número sorteador foi {numeroMaquina} e o seu {numeroJogador}')
