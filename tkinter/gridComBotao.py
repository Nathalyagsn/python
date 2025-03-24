import tkinter as tk
from tkinter import ttk, messagebox


#expandir e mesclar 

def mostrar_mensagem(texto):
    messagebox.showinfo("Botão Clicado", texto)

janela = tk.Tk()
janela.title("Exemplo de Grid")
janela.geometry("170x130")
janela.configure(bg='purple')

botao1 = ttk.Button(janela, text="Botão 1", command=lambda: mostrar_mensagem('Botão 1'))
botao2 = ttk.Button(janela, text="Botão 2", command=lambda:mostrar_mensagem('Botão 2'))
botao3 = ttk.Button(janela, text="Botão 3", command=lambda:mostrar_mensagem('Botão 3'))
botao4 = ttk.Button(janela, text="Botão 4", command=lambda:mostrar_mensagem('Botão 4'))
botao5 = ttk.Button(janela, text="Botão 5", command=lambda:mostrar_mensagem('Botão 5'))

#posicionamento
botao1.grid(row=0, column=0)
botao2.grid(row=1, column=0)
botao3.grid(row=1, column=1, padx=10) 
ttk.Label(janela, text="", background= 'purple').grid(row=2, sticky='ew')
botao4.grid(row=3, column=0, columnspan=2, pady=5)
botao5.grid(row=4, column=0, columnspan=2, sticky='ew')

janela.mainloop()