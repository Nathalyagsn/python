valCasa = float(input('Qual o valor da casa? '))
salComprador = float(input('Qual o salario do comprador? ')) 
quantAnos = int(input('Em quantos anos pretende pagar? '))

prestacao = valCasa / (12 * quantAnos)
porcentagem = salComprador * 30 /100

print(f'Para comprar um imóvel de {valCasa}R$ em {quantAnos} anos a prestação será de {prestacao}R$.')

if porcentagem >= prestacao:
    print('Parabéns! Emprestimo aprovado.')
else:
    print('Emprestimo negado.')
