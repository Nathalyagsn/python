from datetime import date

nascimento = int(input('Qual o ano do seu nascimento? '))

anoAtual = date.today().year
idade = anoAtual - nascimento
faltam = 18 - idade
atrasado = idade - 18

if (idade == 18):
    print(f'Você tem {idade} anos. Já pode se alistar.')

elif (idade < 18):
    print(f'Você tem {idade} anos. Faltam {faltam} anos para se alistar')

else:
    print(f'Você tem {idade} anos. Se passaram {atrasado} anos do seu alistamento.')


