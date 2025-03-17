# r - read -leitura
# a - append - incrementar
# w - write - escrita
# x - create - criar arquivo
# r+ - leitura + escrita

#arquivo = open("D:/Nathy/Python/data/teste2.txt", "w")

#Leitura

#print(arquivo.readable())
#print(arquivo.read())
#lista = (arquivo.readlines())
#print(lista[1])

#arquivo.write("\nSQL")

import os 
if os.path.exists("D:/Nathy/Python/data/teste2.txt"):
    os.remove("D:/Nathy/Python/data/teste2.txt")
    print("Arquivo existente...Deletando...")
else :
   arquivo = open("D:/Nathy/Python/data/teste2.txt", "w")
   arquivo.write("\nSQL")
   print("Arquivo não existe...Criando...")
   print(arquivo)
    



