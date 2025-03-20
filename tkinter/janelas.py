import tkinter as tk

janela = tk.Tk()


#conf da janela
janela.title("Janela Principal")
janela.geometry("500x400+500+300")
janela.config(bg = "lightblue")

#conf da msg

lblMsg = tk.Label(janela, text="Conteudo da primeira janela")
lblMsg.pack()

#icon na janela

janela.iconbitmap('imagens/docker.ico')

#abrir outra janela na janela principal

janela.mainloop()