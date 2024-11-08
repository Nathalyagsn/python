km = int(input('Qual a distancia percorrida? '))

if (km <= 200):
    preco = km * 0.50
    print(f'Custo da viagem: {preco} R$')

else: 
    preco = km * 0.45
    print(f'O custo da viagem: {preco} R$')
