import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Exemplo de Pack")


lbl1 = ttk.Label(janela, text="Label 1", background="blue")
lbl2 = ttk.Label(janela, text="Label 2", background="white")
lbl3 = ttk.Label(janela, text="Label 3", background="yellow")
lbl4 = ttk.Label(janela, text="Label 4", background="red")


lbl1.pack(side="top", pady=5)
lbl2.pack(side="top")
lbl3.pack(side="top")
lbl4.pack(side="top")

janela.mainloop()