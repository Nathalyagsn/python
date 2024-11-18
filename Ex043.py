peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f}. Você está abaixo do peso. ')

elif 18.5 <= IMC < 25:
    print(f'Seu IMC é de {IMC:.2f}. Você está no peso ideal.')  

elif 25 <= IMC < 30:
    print(f'Seu IMC é de {IMC:.2f}. Você está com sobrepeso.')    

elif 30 <= IMC < 35:
    print(f'Seu IMC é de {IMC:.2f}. Você está com obesidade.')    

else: 
    print(f'Seu IMC é de {IMC:.2f}. Você está com obesidade morbida. ')   