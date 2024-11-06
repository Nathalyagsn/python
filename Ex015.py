km = float(input('Quantos km foram percorridos? '))
dia = int(input('Por quantos dias? '))

precodia = dia * 60
kmpordia = km * 0.15

tot = precodia + kmpordia

print(f'O total a ser pago é : {tot} R$')
