nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))

media = (nota1 + nota2) / 2

print(media)

if media < 5:
    print('O aluno está reprovado.')

elif (media >= 5) and (media <= 6.9):   
    print('O aluno está de recuperação.') 

else:
    print('O aluno está aprovado.')