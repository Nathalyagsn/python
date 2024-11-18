valor = float(input('Qual o valor do produto? '))

porcentagemDez = valor * (10 / 100)
porcentagemCinco = valor * (5 / 100)
parcela = valor / 2
juros = valor * 1.2


print('Metodos de pagamanto: \n 1- à vista dinheiro\n 2- à vista no cartão\n 3- 2x no cartão\n 4- 3x ou mais no cartão') 
metodoPag = int(input('Escolha a forma de pagamento: '))

if metodoPag == 1:
    disDez = valor - porcentagemDez
    print(f'Desconto de 10% aplicado na sua compra de {valor}R$. O produto agora ficou {disDez}R$. ')

elif metodoPag == 2:
    disCinco = valor - porcentagemCinco
    print(f'Desconto de 5% aplicado na sua compra de {valor}R$. O produto agora ficou {disCinco}R$.')

elif metodoPag == 3:
    print(f'Metodo sem desconto. Compra no valor de {valor}R$. Parcelado em duas vezes de {parcela}R$. ')

elif metodoPag == 4:
    print(f'Metodo com juros. Compra no valor de {valor}R$. O produto agora ficou {juros}R$ ')


