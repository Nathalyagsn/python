import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exercicio")
janela.geometry('300x200')

lblTxt = ttk.Label(janela, text="Clique no botão para mudar o texto")
lblTxt.pack()

def mudar_texto():
    lblTxt.config(text="Boa!")

botao = tk.Button(janela, text="Clique", command=mudar_texto)
botao.pack()




janela.mainloop()