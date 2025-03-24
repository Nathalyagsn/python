import tkinter as tk
from tkinter import ttk

#expandir e mesclar 

janela = tk.Tk()
janela.title("Exemplo de Grid")
janela.geometry("330x100")
janela.grid_rowconfigure(1, minsize=80)

label1 = ttk.Label(janela, text="Widget 1", width=15, background="pink")
label2 = ttk.Label(janela, text="Widget 2", width=30, background="purple")
label3 = ttk.Label(janela, text="Widget 2", width=30, background="grey")

#posicionamento
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, columnspan=2)
label3.grid(row=1, column=0, rowspan=2, columnspan=3, sticky="ewns") 

janela.mainloop()