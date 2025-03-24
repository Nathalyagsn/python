import tkinter as tk
from tkinter import ttk

def mostrar_nome_completo() :
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    nome_completo = f"Nome completo: {nome} {sobrenome}"
    label_nome_completo.config(text=nome_completo)


janela = tk.Tk()
janela.title("Captura de Texto")

#criando entry para o nome
label_nome = ttk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = ttk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

#criando entry para o sobrenome
label_sobrenome = ttk.Label(janela, text="Sobrenome:")
label_sobrenome.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_sobrenome = ttk.Entry(janela)
entry_sobrenome.grid(row=1, column=1,padx=10, pady=5 )

#botao criar nome completo
botao_mostrar = ttk.Button(janela, text="Mostrar nome completo", command=mostrar_nome_completo)
botao_mostrar.grid(row=2, columnspan=2, padx=10, pady=10)

#label que mostra o nome completo

label_nome_completo = ttk.Label(janela, text="")
label_nome_completo.grid(row=3, columnspan=2, padx=10, pady=5)

janela.mainloop()