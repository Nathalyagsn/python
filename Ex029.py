km = float(input('Qual a velocidade percorrida? '))
multa = (km - 80) * 7

if (km > 80):
    print(f'Limite  de velocidade ultrapassado. Multa aplicada de {multa}R$' )

else:
    print('Nenhuma multa encontrada.')