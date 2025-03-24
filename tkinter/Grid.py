import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo de Grid")
janela.geometry("300x100")


#widgets

label1 = ttk.Label(janela, text="Widget 1", width=20, background="red")
label2 = ttk.Label(janela, text="Widget 2", width=20, background="lightgreen")
label3 = ttk.Label(janela, text="Widget 2", width=40, background="lightblue")


#posicionamento com Grid

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2) 

janela.mainloop()