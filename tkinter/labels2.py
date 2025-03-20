import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de labels")

#label 1
label1 = ttk.Label(
    janela,
    text= "Texto do Label 1",
    font=("Helvetica", 18)
)
label1.pack(ipadx=10, ipady=30)

label2 = ttk.Label(
    janela,
    text = "Texto do Label 2",
    font=("Arial", 22),
    foreground="green"
)
label2.pack(ipadx=10, ipady=60)

janela.mainloop()