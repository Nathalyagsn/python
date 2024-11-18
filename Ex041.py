from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano

if idade <= 9:
    print(f'Você tem {idade} e é um nadador Mirim.')

elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} e é um nadador Infantil.')

elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} e é um nadador Júnior.')  

elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} e é um nadador Sênior.')

else:
    print(f'Você tem {idade} e é um nadador Master.')