valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))



if (valor1 > valor2 and valor1 >  valor3):
    print(f'{valor1} é o maior valor.')

elif (valor2 > valor1 and valor2 > valor3):
    print(f'{valor2} é o maior valor.')

else:
    print(f'{valor3} é o maior valor.')