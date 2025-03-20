import tkinter as tk
from datetime import date


def mostrar_data():
    hoje = date.today()
    text_data.set(hoje.strftime("%d/%m/%Y"))


#Criando janela principal
janela = tk.Tk()
janela.title("Mostrar da Data")
janela.geometry('300x200')

#variavel para label
text_data = tk.StringVar()

#label
label_data = tk.Label(janela, textvariable=text_data, font=("Arial", 14))
label_data.pack(pady=20)

#criando botao
botao_data = tk.Button(janela, text="Mostrar data", command=mostrar_data,bg="lightblue", fg="black")

botao_data.pack(pady=10)

#exibir janela
janela.mainloop()


