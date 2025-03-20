import tkinter as tk

#instancia da janela
janela = tk.Tk()
janela.title("Primeiro app")
janela.geometry("300x100+20+20")

#label
labelMsg = tk.Label(janela, text="Hello World!")
labelMsg.pack()

#exibir janela

janela.mainloop()
