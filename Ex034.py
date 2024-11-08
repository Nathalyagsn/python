salario = float(input('Qual o seu salário? '))

if(salario > 1250):
    bonus = salario * 0.10
    salarioAtual = salario + bonus
    print(f'Bonus de {bonus}R$ aplicado. Seu novo salário é: {salarioAtual}R$')

if(salario <= 1250):
    bonus = salario * 0.15
    salarioAtual = salario + bonus
    print(f'Bonus de {bonus}R$ aplicado. Seu novo salário é: {salarioAtual}R$')