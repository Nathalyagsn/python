from random import randint

pc = randint(1, 3)

print('1- Pedra\n2- Papel\n3- Tesoura')

jogador = int(input('Escolha sua jogada: '))


if pc == jogador:
    print('Empatou')

elif (pc == 1 and jogador == 2) or (pc == 2 and jogador == 3) or (pc == 3 and jogador == 1):
    print('Você venceu!')

else:
    print('Você perdeu.')    


