import tkinter as tk
from tkinter import ttk

#expandir e mesclar 

janela = tk.Tk()
janela.title("Exemplor de Grid")
janela.geometry("300x200")

label1 = ttk.Label(janela, text="Widget 1", width=20, background="red")
label2 = ttk.Label(janela, text="Widget 2", width=20, background="lightgreen")
label3 = ttk.Label(janela, text="Widget 2", width=40, background="lightblue")