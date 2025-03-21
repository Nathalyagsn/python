import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo de Pack")

btn1 = ttk.Button(janela, text=("Botão 1"))
btn2 = ttk.Button(janela, text=("Botão 2"))
btn3 = ttk.Button(janela, text=("Botão 3"))
btn4 = ttk.Button(janela, text=("Botão 4"))

btn1.pack(side="left")
btn2.pack(side="right")
btn3.pack(side="bottom")
btn4.pack()


janela.mainloop()